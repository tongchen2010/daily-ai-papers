#!/usr/bin/env python3
"""Build a daily arXiv digest of the most relevant new AI/ML papers.

Runs with the Python standard library only (no pip installs) so the GitHub
Action stays fast and reliable. Queries the public arXiv API, ranks recent
papers against an interest profile, and writes:

  digests/YYYY-MM-DD.md   one dated digest (the day's top papers)
  README.md               landing page: latest digest inline + archive
  data/history.json       append-only log (date, count, ids) for trends
"""
import json
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone, date, timedelta
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent

# ----------------------------- interest profile -----------------------------
CATEGORIES = ["cs.LG", "cs.AI", "cs.CV", "cs.CL", "eess.IV", "q-bio.NC"]

# keyword -> weight when it appears in the abstract; title hits count 3x.
KEYWORDS = {
    "alzheimer": 6, "lewy body": 6, "dementia": 5, "neurodegenerative": 5,
    "neuroimaging": 5, "brain mri": 5, "cortical": 4, "connectome": 4,
    "brain network": 4, "diffusion mri": 3, "functional mri": 3, "fmri": 3,
    "graph neural network": 5, "graph neural": 4, "gnn": 4,
    "representation learning": 4, "self-supervised": 4, "foundation model": 3,
    "disease progression": 5, "longitudinal": 3, "survival analysis": 2,
    "diffusion model": 3, "generative model": 2, "transformer": 2,
    "large language model": 3, "llm": 3, "agent": 2, "retrieval-augmented": 3,
    "medical imaging": 4, "segmentation": 2, "interpretab": 3, "explainab": 3,
    "domain adaptation": 3, "multimodal": 3, "state space model": 2, "mamba": 2,
}

TOP_N = 12            # papers per daily digest
LOOKBACK_DAYS = 3     # consider papers announced within this many days
FETCH = 120           # how many recent papers to pull before ranking
ARXIV_API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARX = "{http://arxiv.org/schemas/atom}"
# ---------------------------------------------------------------------------


UA = {"User-Agent": "daily-ai-papers/1.0 (+https://github.com/tongchen2010/daily-ai-papers)"}
RSS_BASE = "https://rss.arxiv.org/rss/"
DC = "{http://purl.org/dc/elements/1.1/}"


def _get(url):
    """HTTP GET with polite backoff (arXiv throttles bursts; clean IPs are fine)."""
    req = urllib.request.Request(url, headers=UA)
    delays = [0, 5, 15, 30, 60]
    last = None
    for i, wait in enumerate(delays):
        if wait:
            time.sleep(wait)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 503) and i < len(delays) - 1:
                print(f"  {e.code} from arXiv, retrying in {delays[i+1]}s…", file=sys.stderr)
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
            if i < len(delays) - 1:
                print(f"  network error ({e}), retrying…", file=sys.stderr)
                continue
            raise
    raise last


def parse_rss(xml_bytes, today_str):
    """Parse one arXiv RSS feed (today's announcements for a category)."""
    root = ET.fromstring(xml_bytes)
    out = []
    for it in root.iter("item"):
        title = text(it.find("title"))
        link = text(it.find("link"))
        desc = text(it.find("description"))
        if not title or not link:
            continue
        m = re.search(r"Announce Type:\s*([\w-]+)", desc)
        atype = (m.group(1).lower() if m else "")
        if atype.startswith("replace"):      # skip revisions; feature genuinely new/cross-listed
            continue
        abstract = desc
        ma = re.search(r"Abstract:\s*(.*)$", desc, re.S)
        if ma:
            abstract = re.sub(r"\s+", " ", ma.group(1)).strip()
        cr = it.find(DC + "creator")
        authors = [a.strip() for a in text(cr).split(",") if a.strip()] if cr is not None else []
        cats = [text(c) for c in it.findall("category") if text(c)]
        mid = re.search(r"arXiv:([0-9.]+)", desc) or re.search(r"/abs/([0-9.]+)", link)
        aid = mid.group(1) if mid else link.rstrip("/").split("/")[-1]
        out.append({
            "title": title, "summary": abstract, "authors": authors,
            "categories": cats, "primary": (cats[0] if cats else ""),
            "published": today_str, "updated": today_str,
            "abs": link.replace("http://", "https://"),
            "pdf": link.replace("/abs/", "/pdf/").replace("http://", "https://"),
            "arxiv_id": aid, "announce": atype,
        })
    return out


def fetch_all_rss(today_str):
    """Pull and merge the per-category RSS feeds, de-duplicated by arXiv id."""
    seen, merged = set(), []
    for i, c in enumerate(CATEGORIES):
        if i:
            time.sleep(1)                     # be polite between feeds
        try:
            items = parse_rss(_get(RSS_BASE + c), today_str)
        except Exception as e:
            print(f"  RSS {c} failed: {e}", file=sys.stderr)
            continue
        added = 0
        for p in items:
            if p["arxiv_id"] in seen:
                continue
            seen.add(p["arxiv_id"])
            merged.append(p)
            added += 1
        print(f"  RSS {c}: {len(items)} items ({added} new)")
    return merged


def fetch_recent():
    """arXiv Atom API (fallback if the RSS feeds are unavailable)."""
    q = " OR ".join(f"cat:{c}" for c in CATEGORIES)
    params = urllib.parse.urlencode({
        "search_query": q, "sortBy": "submittedDate",
        "sortOrder": "descending", "max_results": FETCH,
    })
    return _get(f"{ARXIV_API}?{params}")


def text(el):
    return re.sub(r"\s+", " ", (el.text or "").strip()) if el is not None else ""


def parse(xml_bytes):
    root = ET.fromstring(xml_bytes)
    papers = []
    for e in root.findall(f"{ATOM}entry"):
        title = text(e.find(f"{ATOM}title"))
        summary = text(e.find(f"{ATOM}summary"))
        published = text(e.find(f"{ATOM}published"))
        updated = text(e.find(f"{ATOM}updated"))
        abs_id = text(e.find(f"{ATOM}id"))
        authors = [text(a.find(f"{ATOM}name")) for a in e.findall(f"{ATOM}author")]
        cats = [c.get("term") for c in e.findall(f"{ATOM}category") if c.get("term")]
        prim = e.find(f"{ARX}primary_category")
        primary = prim.get("term") if prim is not None else (cats[0] if cats else "")
        pdf = ""
        for ln in e.findall(f"{ATOM}link"):
            if ln.get("title") == "pdf":
                pdf = ln.get("href", "")
        if not title or not abs_id:
            continue
        papers.append({
            "title": title, "summary": summary, "authors": authors,
            "categories": cats, "primary": primary,
            "published": published, "updated": updated,
            "abs": abs_id.replace("http://", "https://"),
            "pdf": (pdf or abs_id.replace("/abs/", "/pdf/")).replace("http://", "https://"),
            "arxiv_id": abs_id.rstrip("/").split("/abs/")[-1],
        })
    return papers


def score(p):
    title = p["title"].lower()
    abstract = p["summary"].lower()
    s = 0
    hits = []
    for kw, w in KEYWORDS.items():
        in_title = kw in title
        in_abs = kw in abstract
        if in_title:
            s += w * 3
        elif in_abs:
            s += w
        if in_title or in_abs:
            hits.append(kw)
    p["score"] = s
    p["hits"] = hits
    return s


def within_lookback(p, today):
    stamp = p["published"][:10] or p["updated"][:10]
    try:
        d = date.fromisoformat(stamp)
    except ValueError:
        return False
    return (today - d).days <= LOOKBACK_DAYS


def select(papers, today):
    for p in papers:
        score(p)
    recent = [p for p in papers if within_lookback(p, today)]
    pool = recent if len(recent) >= TOP_N else papers          # fallback if a quiet day
    pool.sort(key=lambda p: (p["score"], p["published"]), reverse=True)
    return pool[:TOP_N]


def fmt_authors(authors):
    if not authors:
        return "—"
    if len(authors) <= 3:
        return ", ".join(authors)
    return ", ".join(authors[:3]) + ", et al."


def digest_md(picks, today_str):
    lines = [f"# arXiv AI/ML digest — {today_str}", ""]
    lines.append(f"_The {len(picks)} most relevant new papers across "
                 f"{', '.join('`'+c+'`' for c in CATEGORIES)}, ranked against a "
                 f"neuro-AI interest profile. Auto-generated._\n")
    for i, p in enumerate(picks, 1):
        abstract = p["summary"]
        if len(abstract) > 480:
            abstract = abstract[:480].rsplit(" ", 1)[0] + "…"
        tags = ", ".join(f"`{h}`" for h in p["hits"][:6]) or "_general_"
        lines += [
            f"### {i}. [{p['title']}]({p['abs']})",
            f"**{fmt_authors(p['authors'])}**  ·  `{p['primary']}`  ·  "
            f"[abs]({p['abs']}) · [pdf]({p['pdf']})  ·  relevance {p['score']}",
            f"<br>matched: {tags}",
            "",
            f"> {abstract}",
            "",
        ]
    lines.append(f"\n<sub>Generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC} "
                 f"via the arXiv API.</sub>")
    return "\n".join(lines)


def build_readme(today_str, latest_md, archive):
    arch_lines = "\n".join(
        f"- [{d}](digests/{d}.md) — {n} papers" for d, n in archive[:60]
    )
    more = "" if len(archive) <= 60 else f"\n\n_…and {len(archive)-60} earlier digests in [`digests/`](digests/)._"
    return f"""# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: {today_str}** · browse the full archive below.

## How it works

1. A scheduled GitHub Action queries the public **arXiv API** for the most
   recent submissions in `{'`, `'.join(CATEGORIES)}`.
2. Each paper is scored against a weighted keyword profile (neuroimaging,
   graph neural networks, representation learning, LLMs, diffusion models, …);
   title hits count more than abstract hits.
3. The top {TOP_N} are written to `digests/YYYY-MM-DD.md`, this README is
   refreshed, and `data/history.json` logs the day's counts for trend analysis.

Everything is standard-library Python — the workflow installs nothing.

## Configure

Edit the interest profile (`CATEGORIES`, `KEYWORDS`, `TOP_N`) at the top of
[`scripts/build_digest.py`](scripts/build_digest.py).

---

## Latest

{latest_md}

---

## Archive

{arch_lines}{more}

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
"""


def main():
    today = datetime.now(timezone.utc).date()
    today_str = today.isoformat()

    papers = []
    try:
        papers = fetch_all_rss(today_str)
    except Exception as e:
        print(f"RSS error: {e}", file=sys.stderr)
    if not papers:                              # fall back to the Atom API
        print("RSS empty; trying the arXiv API…", file=sys.stderr)
        try:
            papers = parse(fetch_recent())
        except Exception as e:
            print(f"ERROR fetching/parsing arXiv: {e}", file=sys.stderr)
            return 1
    if not papers:
        print("No papers returned; aborting without changes.", file=sys.stderr)
        return 1

    picks = select(papers, today)
    print(f"{today_str}: fetched {len(papers)}, selected {len(picks)} "
          f"(top score {picks[0]['score'] if picks else 0})")

    (ROOT / "digests").mkdir(exist_ok=True)
    (ROOT / "data").mkdir(exist_ok=True)

    latest_md = digest_md(picks, today_str)
    (ROOT / "digests" / f"{today_str}.md").write_text(latest_md + "\n")

    # history log
    hist_path = ROOT / "data" / "history.json"
    history = json.loads(hist_path.read_text()) if hist_path.exists() else []
    history = [h for h in history if h.get("date") != today_str]
    history.append({"date": today_str, "count": len(picks),
                    "ids": [p["arxiv_id"] for p in picks]})
    history.sort(key=lambda h: h["date"], reverse=True)
    hist_path.write_text(json.dumps(history, indent=2) + "\n")

    archive = [(h["date"], h["count"]) for h in history]
    (ROOT / "README.md").write_text(build_readme(today_str, latest_md, archive))
    print(f"Wrote digests/{today_str}.md, README.md, data/history.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
