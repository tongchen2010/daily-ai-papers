# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-10** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-10

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [ReCast: Attribution-Oriented Step Representation Learning for LLM-Based Agent Systems](https://arxiv.org/abs/2610.11334)
**Weilin Jin, Mingyu Wang, Taiyu Zhu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.11334) · [pdf](https://arxiv.org/pdf/2610.11334)  ·  relevance 27
<br>matched: `representation learning`, `llm`, `agent`

> In LLM-based agent systems, failures can originate from early steps whose effects propagate through subsequent interactions, making their origins difficult to identify. To trace such failures back to their origin, failure attribution has been formulated as the task of identifying the earliest step responsible for the failure. Recent methods leverage LLM internal signals for failure attribution, typically using hidden states as step representations. We therefore conduct an…

### 2. [OA-MAP: Evidence-Grounded Multi-Agent Multimodal Framework for Interpretable Knee Osteoarthritis Progression](https://arxiv.org/abs/2610.12134)
**Sixu Chen, Mingrui Yang, Qiang Guan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12134) · [pdf](https://arxiv.org/pdf/2610.12134)  ·  relevance 24
<br>matched: `agent`, `interpretab`, `multimodal`

> Knee osteoarthritis (KOA) progression prediction can support patient monitoring, requiring the integration of multimodal data and multidomain expertise. Moreover, isolated risk estimates provide limited insight underlying a prediction. To automate the progression assessment workflow and reduce manual effort while providing interpretable findings and supporting evidence, we present OA-MAP, an autonomous multi-agent framework for evidence-grounded assessment of structural and…

### 3. [From Pixels, Without Pre-training: Joint Generative and Self-Supervised Representation Learning in One Model](https://arxiv.org/abs/2610.05711)
**Vicente Balmaseda, Ching-Long Lin, Tianbao Yang**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.05711) · [pdf](https://arxiv.org/pdf/2610.05711)  ·  relevance 24
<br>matched: `representation learning`, `self-supervised`

> Strong image generation models are conditioned on class labels, aligned to frozen pretrained encoders, or built on separately trained autoencoders. While effective, generation then depends on supervision or pretraining: labels must be annotated, and encoders or autoencoders pretrained for the target domain. We study joint generative and self-supervised representation learning in a single model, enabling self-conditioned generation without labels or pretrained models. This is…

### 4. [Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent System](https://arxiv.org/abs/2610.11899)
**Irene Weber (University of Applied Sciences Kempten, Germany)**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.11899) · [pdf](https://arxiv.org/pdf/2610.11899)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `retrieval-augmented`

> Large language models (LLMs) are increasingly embedded as components in software systems, marketed under labels such as chatbot, copilot, retrieval-augmented generation, workflow, coding agent and AI agent. Whether these labels denote genuine architectural forms or serve as branding has not been assessed systematically. In the sources surveyed, labels do carry architectural content, most clearly in vendor usage: copilot denotes a router-worker architecture operating a host…

### 5. [LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models](https://arxiv.org/abs/2610.11253)
**Surya Shetty, Ulisses Braga-Neto**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.11253) · [pdf](https://arxiv.org/pdf/2610.11253)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model agents are being increasingly deployed as autonomous scientists, designing experiments and inferring mechanistic world models with minimal human oversight. Yet identifiability is often overlooked: when a plateau is reached, the agent needs to know whether it is not yet capable enough or the model simply is not identifiable from the data, in which case no amount of further experimentation of the same kind can help. We propose the Identifiability-Driven…

### 6. [Memory Type Varies: Empowering LLM Agents for Long-Term Memory with Diverse Strategies](https://arxiv.org/abs/2610.11573)
**Yi Wen, Derong Xu, Pengyue Jia, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.11573) · [pdf](https://arxiv.org/pdf/2610.11573)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> The memory capabilities of Large Language Models (LLMs) have garnered increasing attention recently. Despite great success achieved, existing retrieval-based memory approaches typically overlook the differences between memories and employ a unified strategy to process all memories, leading to suboptimal performance. Thus, an intuitive question arises: can we categorize memory into different types and select appropriate strategies? However, given the topic-rich,…

### 7. [MemTrial: Learning When to Trust Memory in LLM Portfolio Agents](https://arxiv.org/abs/2610.11732)
**Guanghao Wu, Zhuo Cai, Shoujin Wang**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.11732) · [pdf](https://arxiv.org/pdf/2610.11732)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents for portfolio management learn from experience: they credit each experience in their memory with the outcome of the decisions that used it. In financial markets, however, this outcome mostly reflects the market move shared by all decisions on that date, so the credit tracks the market rather than the experience, and these agents often do worse than simply holding the equal-weight (1/$N$) portfolio. We ask how an agent can credit an…

### 8. [Use and Disuse: Intent-Structured Experience Consolidation for Memory and Learning in LLM Agents](https://arxiv.org/abs/2610.12124)
**Xiangyi Zeng, Baihang Liu, Xutong Wang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12124) · [pdf](https://arxiv.org/pdf/2610.12124)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> The evolution of Large Language Model agents from single-task execution to long-term autonomous operation highlights the critical challenge of transforming continuous experiences into reusable knowledge. To address this, we propose Hippocam, a hierarchical memory and continual learning architecture. Hippocam draws inspiration from two characteristics of human memory: cognitive processes selectively maintain information relevant to current goals, while long-term memories form…

### 9. [From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage](https://arxiv.org/abs/2610.10608)
**Saimon Amanuel Tsegai (Daphne), Alex Kantchelian (Daphne), Danfeng (Daphne), et al.**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2610.10608) · [pdf](https://arxiv.org/pdf/2610.10608)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Security operations centers (SOCs) must triage large volumes of alerts, most of which are benign, while missed attacks can remain uninvestigated. Tool-using large language model (LLM) agents can retrieve evidence during triage, but it remains unclear how reasoning strategies determine what to gather and when an investigation is sufficient to close an alert. We study five representative approaches spanning single-pass tool use, iterative retrieval, sampled investigations,…

### 10. [RFChipAgent: Multi-Agentic AI Flow for Analog/RF Chip Design](https://arxiv.org/abs/2610.10858)
**Awani Khodkumbhe, Yunfei Feng, Raj Rangarajan, et al.**  ·  `cs.AR`  ·  [abs](https://arxiv.org/abs/2610.10858) · [pdf](https://arxiv.org/pdf/2610.10858)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`, `retrieval-augmented`, `multimodal`

> Analog/RF circuits remain the critical interface between digital computation and the physical world, and emerging standards from Wi-Fi 7 to 6G place stringent demands on them, yet analog/RF design remains one of the most labor-intensive steps in chip development. We present RFChipAgent, a first-of-its-kind multi-agent flow of large language model (LLM) agents for end-to-end analog/RF circuit design automation, in which AI agents collaboratively orchestrate the complete…

### 11. [Closed-loop evaluation of LLM agents for embedded software development](https://arxiv.org/abs/2610.11447)
**Jorge Garc\'ia-Carrasco, Sergio Garc\'ia-Carrasco, Alejandro Mat\'e, et al.**  ·  `cs.SE`  ·  [abs](https://arxiv.org/abs/2610.11447) · [pdf](https://arxiv.org/pdf/2610.11447)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language models (LLMs) are increasingly deployed as coding agents that edit files, run builds and tests, inspect execution results, and repair software iteratively. Embedded firmware is a demanding target because correctness depends on closed-loop behavior under sensing, timing, and safety constraints, not only on static source quality. Yet embedded-agent evaluation remains limited and often emphasizes one-shot synthesis or offline correctness. We present a benchmark…

### 12. [Narrow and Deep: An Ontology Tower as the Knowledge of an LLM Agent for an Industrial Equipment System](https://arxiv.org/abs/2610.11768)
**Younghwan Joo, Sung-il Kim**  ·  `eess.SY`  ·  [abs](https://arxiv.org/abs/2610.11768) · [pdf](https://arxiv.org/pdf/2610.11768)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents are beginning to operate industrial energy equipment, and what they get right depends on what they are told about the plant. Established building ontologies name many kinds of points across many sites, whereas an industrial equipment system needs few entities with much knowledge about each. This study proposes the ontology tower, a narrow-and-deep ontology of a single equipment system whose knowledge deepens in two ways: through quantities…


<sub>Generated 2026-10-10 17:51 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-28](digests/2026-08-28.md) — 12 papers
- [2026-08-27](digests/2026-08-27.md) — 12 papers
- [2026-08-26](digests/2026-08-26.md) — 12 papers
- [2026-08-25](digests/2026-08-25.md) — 12 papers
- [2026-08-24](digests/2026-08-24.md) — 12 papers
- [2026-08-23](digests/2026-08-23.md) — 12 papers
- [2026-08-22](digests/2026-08-22.md) — 12 papers
- [2026-08-21](digests/2026-08-21.md) — 12 papers
- [2026-08-20](digests/2026-08-20.md) — 12 papers
- [2026-08-19](digests/2026-08-19.md) — 12 papers
- [2026-08-18](digests/2026-08-18.md) — 12 papers
- [2026-08-17](digests/2026-08-17.md) — 12 papers
- [2026-08-16](digests/2026-08-16.md) — 12 papers
- [2026-08-15](digests/2026-08-15.md) — 12 papers
- [2026-08-14](digests/2026-08-14.md) — 12 papers
- [2026-08-12](digests/2026-08-12.md) — 12 papers
- [2026-08-11](digests/2026-08-11.md) — 12 papers
- [2026-08-10](digests/2026-08-10.md) — 12 papers
- [2026-08-09](digests/2026-08-09.md) — 12 papers
- [2026-08-08](digests/2026-08-08.md) — 12 papers
- [2026-08-07](digests/2026-08-07.md) — 12 papers
- [2026-08-06](digests/2026-08-06.md) — 12 papers

_…and 42 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
