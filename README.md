# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-01** · browse the full archive below.

## How it works

1. A scheduled GitHub Action queries the public **arXiv API** for the most
   recent submissions in `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`.
2. Each paper is scored against a weighted keyword profile (neuroimaging,
   graph neural networks, representation learning, LLMs, diffusion models, …);
   title hits count more than abstract hits.
3. The top 12 are written to `digests/YYYY-MM-DD.md`, this README is
   refreshed, and `data/history.json` logs the day's counts for trend analysis.

Everything is standard-library Python — the workflow installs nothing.

## Configure

Edit the interest profile (`CATEGORIES`, `KEYWORDS`, `TOP_N`) at the top of
[`scripts/build_digest.py`](scripts/build_digest.py).

---

## Latest

# arXiv AI/ML digest — 2026-11-01

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [LoRe-MIM: Lost-or-Replaced Masked Image Modeling for Self-Supervised Representation Learning in Whole-Body PET/CT](https://arxiv.org/abs/2610.40284v1)
**Amartya Bhattacharya, Bashirul Azam Biswas, Biratal Raj Wagle, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.40284v1) · [pdf](https://arxiv.org/pdf/2610.40284v1)  ·  relevance 29
<br>matched: `representation learning`, `self-supervised`, `segmentation`, `multimodal`

> Deep learning models for whole-body positron emission tomography/computed tomography (PET/CT) hold significant clinical potential for disease detection, treatment planning, and response assessment. However, the time and cost associated with expert annotations remain major bottlenecks in developing robust and generalizable models. Although self-supervised learning (SSL) has emerged as a promising approach to mitigating annotation scarcity, its application to whole-body PET/CT…

### 2. [Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records](https://arxiv.org/abs/2610.40379v1)
**Daniel Palacios, Guantong Qi, Anna Kadi, et al.**  ·  `q-bio.QM`  ·  [abs](https://arxiv.org/abs/2610.40379v1) · [pdf](https://arxiv.org/pdf/2610.40379v1)  ·  relevance 27
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Large language model (LLM) agents are proposed for clinical prediction but are untested in pediatrics, where cohorts are small and outcomes are uncommon. Using records from 2,489 youth with type 2 diabetes (T2D) and 4,018 with type 1 diabetes (T1D), spanning structured data, note-derived social determinants and, in T1D, continuous glucose monitoring data, we predicted seven T2D outcomes, four also in T1D, at 24 months from 18 months of follow-up. CEDAR (Clinical…

### 3. [A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening](https://arxiv.org/abs/2610.40511v1)
**Zach Paris, Emily Finn**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.40511v1) · [pdf](https://arxiv.org/pdf/2610.40511v1)  ·  relevance 18
<br>matched: `fmri`, `large language model`, `llm`, `interpretab`

> Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three naturalistic language-listening datasets spanning intracranial…

### 4. [Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation](https://arxiv.org/abs/2610.40350v1)
**Zheng Zhu, Xiaozhuan Liang, Xi Chen, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.40350v1) · [pdf](https://arxiv.org/pdf/2610.40350v1)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks. However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant information, which dilutes their attention and hinders effective planning and reasoning. To mitigate this challenge, we introduce Cognitive Resource Self-Allocation (CORAL), a novel reasoning paradigm…

### 5. [PhysCount: Do MLLMs Count Visual Appearances or Physical Entities?](https://arxiv.org/abs/2610.40530v1)
**Lidong Lu, Jiaxin Lv, Liangrui Dong, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.40530v1) · [pdf](https://arxiv.org/pdf/2610.40530v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `multimodal`

> Images reveal appearances, but counting often asks about physical objects. A single entity may be visible directly, in several reflections, or through glass, so detecting every visible occurrence does not determine how many entities are present. Existing visual counting benchmarks rarely separate these two operations. We introduce PhysCount, a benchmark for evaluating whether multimodal large language models (MLLMs) can distinguish what appears in an image from what…

### 6. [Latent Prediction Yields Cross-Subject Alignable Representations in Sensory-Evoked fMRI](https://arxiv.org/abs/2610.40280v1)
**Serwan Jassim, Victoria Bosch, Daniel Anthes, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.40280v1) · [pdf](https://arxiv.org/pdf/2610.40280v1)  ·  relevance 13
<br>matched: `fmri`, `self-supervised`

> Decoding sensory-evoked functional magnetic resonance imaging (fMRI) data is a central analytical tool in cognitive neuroscience. Here we ask whether self-supervised learning (SSL), which has been scarcely explored in this domain, can yield representations that support strong downstream performance. To do so, we adapt a joint embedding predictive architecture (JEPA) to train participant-specific encoders on brain data alone. The encoders never see the stimulus images or any…

### 7. [TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races](https://arxiv.org/abs/2610.40613v1)
**Tom Sander, Pierre Fernandez, Itai Gat, et al.**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2610.40613v1) · [pdf](https://arxiv.org/pdf/2610.40613v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> We present TextSeal2, a distortion-free watermark for large language models that keeps its signal under speculative decoding: tokens that replace rejected drafts remain watermarked with the same keys, and the acceptance rate is unchanged. It also preserves output diversity and adds no measurable inference latency. Its predecessor, TextSeal, restores diversity in the Gumbel-max scheme by routing each token to one of two keys via a coin flip. This is suboptimal because the…

### 8. [Comparing Human Role-Players and LLM-Simulated Clients in Online Counselling Training: An Analysis of Counselling Patterns](https://arxiv.org/abs/2610.40563v1)
**Eric Rudolph, Philipp Steigerwald, Jens Albrecht**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.40563v1) · [pdf](https://arxiv.org/pdf/2610.40563v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> This study investigates the capabilities of Large Language Models to simulate counselling clients in educational role-plays in comparison to human role-players. Initially, we recorded role-playing sessions, where novice counsellors interacted with human peers acting as clients, followed by role-plays between humans and clients simulated by Mistrals Mixtral 8x7b using 4-bit quantization. These interactions were analysed with a counselling communication pattern system at…

### 9. [TRACER, a time-to-event EHR foundation model for disease detection across health systems](https://arxiv.org/abs/2610.40536v1)
**Mara Pleasure, Ekaterina Redekop, Vedrana Ivezic, et al.**  ·  `cs.CE`  ·  [abs](https://arxiv.org/abs/2610.40536v1) · [pdf](https://arxiv.org/pdf/2610.40536v1)  ·  relevance 12
<br>matched: `foundation model`, `longitudinal`

> Foundation models trained on longitudinal electronic health records (EHRs) can predict clinical diagnoses years in the future, making them a potential tool for disease screening. We developed TRACER (Temporal Risk Assessment with Clinical EHR Representations), a decoder-based foundation model pretrained on data from over 4.5 million patients from four health systems, and evaluated it on 16 incident diseases at 1-, 2-, and 5-year horizons in more than 2 million patients from…

### 10. [The Athlete as a Scientist of One: Agentic Bayesian Experimental Design for Individualized Physiology from Consumer Wearables](https://arxiv.org/abs/2610.40370v1)
**Behnam Moradi**  ·  `cs.RO`  ·  [abs](https://arxiv.org/abs/2610.40370v1) · [pdf](https://arxiv.org/pdf/2610.40370v1)  ·  relevance 12
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents for personal health read wearable data and recommend, but do not learn about the individual in a way that can be audited or falsified. We present EpiCoach, an agentic system that treats one athlete, a cross-country mountain biker, as the subject of accountable N-of-1 science. Claims about the athlete live in an evidence-gated hypothesis registry: each must issue a probabilistic prediction about a future session before it occurs, and its…

### 11. [Multistep and Multivariate Time Series Explainability with GradientSHAP: A Wind Power Case Study](https://arxiv.org/abs/2610.40330v1)
**Robbie Southam, Zhong Fan, Ke Li**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.40330v1) · [pdf](https://arxiv.org/pdf/2610.40330v1)  ·  relevance 12
<br>matched: `interpretab`, `explainab`

> As the effects of climate change become increasingly apparent, the demand for renewable energy sources such as wind power continues to grow. However, renewables' variable and intermittent nature presents significant challenges in their integration into energy grids. Artificial intelligence (AI) has emerged as a powerful tool to address these issues. Still, its adoption in the energy sector has been hindered by the opacity of many AI models, which often function as black…

### 12. [DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving](https://arxiv.org/abs/2610.40292v1)
**Yishuo Yuan, Shaoyu Yang, Chunrong Fang**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.40292v1) · [pdf](https://arxiv.org/pdf/2610.40292v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Prefill-decode (PD) disaggregation isolates the two phases of large language model serving, but request-level path selection must account for prefill work, cache reuse, and decode demand. We present DolphinRouting, which learns this choice from end-to-end SLO feedback under a given P/D resource allocation. Requests are clustered by raw prompt length, cache-adjusted input lengths on both worker pools, and output-length information. Offline policy search learns one binary…


<sub>Generated 2026-11-01 18:25 UTC via the arXiv API.</sub>

---

## Archive

- [2026-11-01](digests/2026-11-01.md) — 12 papers
- [2026-10-31](digests/2026-10-31.md) — 12 papers
- [2026-10-30](digests/2026-10-30.md) — 12 papers
- [2026-10-29](digests/2026-10-29.md) — 12 papers
- [2026-10-28](digests/2026-10-28.md) — 12 papers
- [2026-10-27](digests/2026-10-27.md) — 12 papers
- [2026-10-26](digests/2026-10-26.md) — 12 papers
- [2026-10-25](digests/2026-10-25.md) — 12 papers
- [2026-10-24](digests/2026-10-24.md) — 12 papers
- [2026-10-23](digests/2026-10-23.md) — 12 papers
- [2026-10-22](digests/2026-10-22.md) — 12 papers
- [2026-10-21](digests/2026-10-21.md) — 12 papers
- [2026-10-20](digests/2026-10-20.md) — 12 papers
- [2026-10-19](digests/2026-10-19.md) — 12 papers
- [2026-10-18](digests/2026-10-18.md) — 12 papers
- [2026-10-17](digests/2026-10-17.md) — 12 papers
- [2026-10-16](digests/2026-10-16.md) — 12 papers
- [2026-10-15](digests/2026-10-15.md) — 12 papers
- [2026-10-14](digests/2026-10-14.md) — 12 papers
- [2026-10-13](digests/2026-10-13.md) — 12 papers
- [2026-10-12](digests/2026-10-12.md) — 12 papers
- [2026-10-11](digests/2026-10-11.md) — 12 papers
- [2026-10-10](digests/2026-10-10.md) — 12 papers
- [2026-10-09](digests/2026-10-09.md) — 12 papers
- [2026-10-08](digests/2026-10-08.md) — 12 papers
- [2026-10-07](digests/2026-10-07.md) — 12 papers
- [2026-10-06](digests/2026-10-06.md) — 12 papers
- [2026-10-04](digests/2026-10-04.md) — 12 papers
- [2026-10-03](digests/2026-10-03.md) — 12 papers
- [2026-10-02](digests/2026-10-02.md) — 12 papers
- [2026-10-01](digests/2026-10-01.md) — 12 papers
- [2026-09-30](digests/2026-09-30.md) — 12 papers
- [2026-09-29](digests/2026-09-29.md) — 12 papers
- [2026-09-28](digests/2026-09-28.md) — 12 papers
- [2026-09-26](digests/2026-09-26.md) — 12 papers
- [2026-09-25](digests/2026-09-25.md) — 12 papers
- [2026-09-24](digests/2026-09-24.md) — 12 papers
- [2026-09-23](digests/2026-09-23.md) — 12 papers
- [2026-09-22](digests/2026-09-22.md) — 12 papers
- [2026-09-21](digests/2026-09-21.md) — 12 papers
- [2026-09-18](digests/2026-09-18.md) — 12 papers
- [2026-09-17](digests/2026-09-17.md) — 12 papers
- [2026-09-16](digests/2026-09-16.md) — 12 papers
- [2026-09-15](digests/2026-09-15.md) — 12 papers
- [2026-09-14](digests/2026-09-14.md) — 12 papers
- [2026-09-12](digests/2026-09-12.md) — 12 papers
- [2026-09-11](digests/2026-09-11.md) — 12 papers
- [2026-09-10](digests/2026-09-10.md) — 12 papers
- [2026-09-09](digests/2026-09-09.md) — 12 papers
- [2026-09-08](digests/2026-09-08.md) — 12 papers
- [2026-09-07](digests/2026-09-07.md) — 12 papers
- [2026-09-06](digests/2026-09-06.md) — 12 papers
- [2026-09-05](digests/2026-09-05.md) — 12 papers
- [2026-09-04](digests/2026-09-04.md) — 12 papers
- [2026-09-03](digests/2026-09-03.md) — 12 papers
- [2026-09-02](digests/2026-09-02.md) — 12 papers
- [2026-09-01](digests/2026-09-01.md) — 12 papers
- [2026-08-31](digests/2026-08-31.md) — 12 papers
- [2026-08-30](digests/2026-08-30.md) — 12 papers
- [2026-08-29](digests/2026-08-29.md) — 12 papers

_…and 64 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
