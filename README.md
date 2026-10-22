# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-22** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-22

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [YingLan: A Multimodal Ocean Foundation Model for Unified Representation Learning from Heterogeneous Observations](https://arxiv.org/abs/2610.29313)
**Sen Jia, Siqi Wei, Junyu Wang, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.29313) · [pdf](https://arxiv.org/pdf/2610.29313)  ·  relevance 30
<br>matched: `representation learning`, `foundation model`, `multimodal`

> Multimodal ocean modeling remains challenging due to substantial heterogeneity in data structures, physical semantics, and spatiotemporal characteristics across satellite imagery, gridded oceanographic fields, and buoy observations. Existing approaches largely focus on task-specific ocean modeling, while learning transferable representations from heterogeneous observations remains an open problem. To address this challenge, we propose YingLan, a multimodal ocean foundation…

### 2. [Balancing Foundation Models and Trait-Specific Learning for Forehead-Crease Recognition](https://arxiv.org/abs/2610.29495)
**Geetanjali Sharma, Aryan Jain, Dev Nagaich, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.29495) · [pdf](https://arxiv.org/pdf/2610.29495)  ·  relevance 24
<br>matched: `foundation model`, `large language model`, `llm`, `interpretab`, `explainab`, `multimodal`

> Biometric recognition often degrades under partial facial vis- ibility, where conventional facial cues are occluded. The forehead region remains consistently visible and contains distinctive crease patterns that can serve as a complementary biometric trait. We present a unified eval- uation of forehead-crease recognition across explainable zero-shot rea- soning, domain-adaptive learning, and trait-specific modeling. FIRE en- ables interpretable zero-shot verification using…

### 3. [Omnilingual-MsASR: Benchmarking Multimodal, Multilingual, Long-Form Multi-Speaker ASR of Omni Large Language Models](https://arxiv.org/abs/2610.29455)
**Yuan Ge, Pei Zhang, Xize Cheng, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.29455) · [pdf](https://arxiv.org/pdf/2610.29455)  ·  relevance 24
<br>matched: `foundation model`, `large language model`, `llm`, `multimodal`

> Omni-modal large language models (LLMs) have achieved remarkable progress in audio and video understanding. However, existing models struggle with long-form, multi-speaker videos, especially in understanding the entire video and recognizing who says what and when. To characterize the capability limit of current omni LLMs and guide future model development, we introduce Omnilingual-MsASR, a multilingual, multimodal benchmark for long-form Multi-speaker Automatic Speech…

### 4. [Fragment-Level Graph Encoding for Interpretable Molecular Property Prediction](https://arxiv.org/abs/2610.29589)
**Rafael Lopes Almeida (School of Pharmacy, University of Eastern Finland, Kuopio, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.29589) · [pdf](https://arxiv.org/pdf/2610.29589)  ·  relevance 22
<br>matched: `graph neural network`, `graph neural`, `gnn`, `interpretab`

> Graph neural networks (GNNs) are among the standard tools for molecular property prediction, but the atom-level explanations of their predictions are hard for medicinal chemists to act on. We propose a change of input representation rather than a new model: molecules are encoded as fragment-level graphs from BRICS decomposition, where each node is a synthetically meaningful fragment whose features are the element-wise sum of its atoms' features. Because only the…

### 5. [Leveraging Time-Series Foundation Models for Financial Crime Detection](https://arxiv.org/abs/2610.29667)
**Danae Natalie Savvidi, H. \c{C}a\u{g}r{\i} Bilgi, Kubilay Atasu, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.29667) · [pdf](https://arxiv.org/pdf/2610.29667)  ·  relevance 22
<br>matched: `graph neural network`, `graph neural`, `gnn`, `foundation model`

> Financial crime detection requires identifying illicit activity within large transaction networks, where suspicious behaviour is rare and unfolds over time. Existing graph-based methods capture relationships among accounts but typically underuse the temporal behaviour encoded in account transaction histories. We introduce Temporal-Context Edge Enrichment (TCEE), a framework that addresses this gap by summarising each account's transaction history with a frozen time-series…

### 6. [S^3martCirc: Self-supervised Smart Circuit Discovery](https://arxiv.org/abs/2609.00755)
**Wendy Zheng, Yinhan He, Liang Wu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2609.00755) · [pdf](https://arxiv.org/pdf/2609.00755)  ·  relevance 21
<br>matched: `self-supervised`, `large language model`, `llm`, `interpretab`

> Large Language Models (LLMs) have demonstrated remarkable performance across diverse tasks, from text summarization to question answering. Despite these capabilities, their black-box nature obscures internal decision-making processes. Mechanistic interpretability (MI) aims to address this by reverse-engineering neural networks into human-understandable algorithms. Current MI approaches for LLMs typically follow a two-stage paradigm: first identifying important components…

### 7. [LLMSeg: Training-Free Text-Prompted Image Segmentation with B-Splines](https://arxiv.org/abs/2610.29409)
**Abdullah Hamdi**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.29409) · [pdf](https://arxiv.org/pdf/2610.29409)  ·  relevance 21
<br>matched: `large language model`, `llm`, `segmentation`, `multimodal`

> Promptable segmentation models such as SAM 3 achieve remarkable open-vocabulary performance but require dedicated architectures, large-scale annotation engines, and task-specific training. We ask a different question: can a general-purpose multimodal large language model (MLLM) segment images directly, without an added segmentation head, mask decoder, or training? We present LLMSeg, a training-free pipeline that turns a vision-capable LLM into a text-prompted image…

### 8. [Asking a Multimodal LLM Whether Someone Fell: Zero-Shot Screening of Low-Resolution Thermal Video in a Laboratory and an Occupied Home](https://arxiv.org/abs/2610.29913)
**Marcos Junca (Senecta Inc.), Mauro Junca (Senecta Inc.)**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.29913) · [pdf](https://arxiv.org/pdf/2610.29913)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Thermal cameras can watch over older people living alone without capturing faces, and multimodal large language models (LLMs) can judge a short video without task-specific training. We evaluate a production multimodal LLM, Gemini 3.8 Flash at temperature 0, as the decision stage of an event-triggered fall screener, used exactly as a deployed prototype uses it: one request per short thermal clip, with its sound track when there is one, and its predecessor Gemini 3.7 Flash on…

### 9. [A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems](https://arxiv.org/abs/2610.28811)
**Wendy Zheng, Liang Wu, Yinhan He, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.28811) · [pdf](https://arxiv.org/pdf/2610.28811)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Agentic systems have demonstrated strong capabilities on complex tasks by enabling multiple interacting large language model (LLM)-based agents to collaborate and execute subtasks in parallel. However, this collaborative structure introduces new challenges for reliably evaluating and diagnosing system failures, particularly failure attribution: tracing a system's execution to identify the agent step responsible for an incorrect final outcome. Because manually performing this…

### 10. [Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents](https://arxiv.org/abs/2610.29346)
**Zixuan Yu, Zhenheng Tang, Xiaowen Chu, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.29346) · [pdf](https://arxiv.org/pdf/2610.29346)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> As Large Language Models (LLMs) evolve into autonomous Deep Search and Deep Research Agents capable of executing long-horizon, multi-step tasks, evaluating their reliability becomes increasingly critical. However, existing evaluation paradigms predominantly focus on final task outcomes, leaving a significant gap in understanding the intermediate execution traces, where agents are highly susceptible to various errors. To address this critical gap, we introduce a comprehensive…

### 11. [SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis Models](https://arxiv.org/abs/2610.28767)
**Berke Arda, Peng Cui, Qiaoyuan Zheng, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.28767) · [pdf](https://arxiv.org/pdf/2610.28767)  ·  relevance 18
<br>matched: `llm`, `interpretab`

> Current evaluation of LLMs on benchmarks typically aggregates performance over individual examples into a single scalar score. This approach is overly coarse and ignores the diverse scope of skills covered by benchmark datasets. To address this limitation and better exploit benchmark data, we propose SkillEval, a new evaluation framework that performs cross-model, skill-level analysis. The framework integrates advances from two areas: (1) it leverages the meta-cognitive…

### 12. [Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets](https://arxiv.org/abs/2610.28787)
**Hieu Tran, Hong Yu**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.28787) · [pdf](https://arxiv.org/pdf/2610.28787)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests enforcement by forcing a member to cheat in counterfactual copies of a market, and use it to study what reinforcement learning (RL) teaches agents in pricing and trading. Small LLMs trained by RL…


<sub>Generated 2026-10-22 17:58 UTC via the arXiv API.</sub>

---

## Archive

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

_…and 54 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
