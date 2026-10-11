# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-11** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-11

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417v1)
**Zheyu Fan, Yue Zhang, Mingkai Deng, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.12417v1) · [pdf](https://arxiv.org/pdf/2610.12417v1)  ·  relevance 23
<br>matched: `generative model`, `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do…

### 2. [A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization](https://arxiv.org/abs/2610.12183v1)
**Ming Chen, Rong-Xi Tan, Ke Xue, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.12183v1) · [pdf](https://arxiv.org/pdf/2610.12183v1)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing great potential due to the integration with mathematically rigorous tools. However, existing agentic BBO studies use different task domains and system…

### 3. [HRIL: Learning Multimodal Synergy via Higher-Order Tensor Modeling](https://arxiv.org/abs/2610.12393v1)
**Qun Dai, Liangjian Wen, Jiang Duan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12393v1) · [pdf](https://arxiv.org/pdf/2610.12393v1)  ·  relevance 17
<br>matched: `representation learning`, `self-supervised`, `multimodal`

> Self-supervised multimodal representation learning has achieved remarkable success across diverse domains, yet capturing synergistic information remains challenging due to the complexity of cross-modal interactions. Unlike the shared information across individual modalities, synergy arises when task-relevant signals emerge only from the joint configuration of multiple modalities and cannot be recovered from any modality in isolation. This work focuses on how to preserve the…

### 4. [Looking Inside LLMs: Small-World Connectivity as a Signature of Reasoning Performance](https://arxiv.org/abs/2610.12304v1)
**Zheng Huang, Sansheng Cao, Enpei Zhang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12304v1) · [pdf](https://arxiv.org/pdf/2610.12304v1)  ·  relevance 16
<br>matched: `brain network`, `large language model`, `llm`

> Understanding large language model (LLM) reasoning requires looking beyond behavioral performance to examine how reasoning ability is reflected in internal organization. Inspired by neuroscience findings linking higher intelligence to stronger small-world organization in functional brain networks, we investigate small-world connectivity as a structural signature of LLM reasoning. We construct functional graphs from attention-head activation similarities and find that a…

### 5. [OneSearch-VL: Unified Multimodal Deep Research Agent for Image and Video](https://arxiv.org/abs/2610.12419v1)
**Hongyu Li, Manyuan Zhang, Kaituo Feng, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.12419v1) · [pdf](https://arxiv.org/pdf/2610.12419v1)  ·  relevance 15
<br>matched: `agent`, `multimodal`

> Single-image, multi-image, and video deep research require different visual operations but share a workflow of visual grounding, external retrieval, and fact composition. A key challenge is to preserve the dependencies linking localized visual anchors, entity relations, source-supported facts, and answer-producing operations. We introduce OneSearch-VL, a unified agent centered on the Visually Grounded Evidence Graph (VGEG), which encodes these dependencies as a shared…

### 6. [GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](https://arxiv.org/abs/2610.12391v1)
**Jialu Wang, Ruichen Zhang, Xiaoou Liu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12391v1) · [pdf](https://arxiv.org/pdf/2610.12391v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over. However, effective formalization is highly non-trivial: on Geometry3K, structure injection fixes 28 errors but introduces 13 new ones among 200 examples. Redundant relations can distract the model, while…

### 7. [OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport](https://arxiv.org/abs/2610.12375v1)
**Babak Barazandeh, Connor Swanson, Chinmay Kulkarni, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12375v1) · [pdf](https://arxiv.org/pdf/2610.12375v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Agents are deployed in applications from trip planners and stock trading to IT incident triage. In most cases, LLM agents work autonomously with minimal rule-based safeguarding, leading to cost and safety issues from irreversible actions. Recent works resolve this either by using a safeguard agent to monitor behavior or evaluating logs post-hoc. The first adds cost and latency to every step; the second delivers its verdict after the run, when tokens are burned and damage is…

### 8. [Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict](https://arxiv.org/abs/2610.12360v1)
**Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12360v1) · [pdf](https://arxiv.org/pdf/2610.12360v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> When retrieved evidence contradicts an agent's prior beliefs, does it revise its answer, acknowledge uncertainty, or persist with an incorrect conclusion? Existing evaluations of agentic systems focus primarily on task success, offering limited insight into how agents handle such conflicts. We propose to evaluate agents on epistemic humility (EH): the agent's willingness to recognize, act on, and communicate uncertainty during task execution. We operationalize EH through…

### 9. [From What to Which: Decoding Modifier Grounding in Frozen MLLMs](https://arxiv.org/abs/2610.12305v1)
**Barbara Toniella Corradini, Caterina Gallegati, Ludovica Genovese, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.12305v1) · [pdf](https://arxiv.org/pdf/2610.12305v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `multimodal`

> As Multimodal Large Language Models (MLLMs) can describe increasingly complex visual scenes, token-level grounding becomes crucial. Yet, when an MLLM generates "the yellow banana on the left", established grounding approaches focus on what is in the image ("banana"), overlooking tokens that help describe which instance is meant ("yellow", "left"). In this work, we ask whether frozen MLLM representations contain decodable grounding information about the referred instance…

### 10. [DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception](https://arxiv.org/abs/2610.12266v1)
**Jinghua Hou, Zhe Liu, Hengshuang Zhao**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.12266v1) · [pdf](https://arxiv.org/pdf/2610.12266v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, which suffers from excessive token overhead, or fixed-range quantization, which suffers from range and precision constraints, especially for 3D domains with…

### 11. [Prior or Feedback? What an LLM Uses When Adapting Neural Operators](https://arxiv.org/abs/2610.12325v1)
**Julian Chan, Javier Mora Jimenez**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12325v1) · [pdf](https://arxiv.org/pdf/2610.12325v1)  ·  relevance 14
<br>matched: `large language model`, `llm`, `agent`

> Do LLM scientific agents rely only on their initial task context, or do they adapt their decisions in response to experimental feedback? We study this question in neural operator adaptation, where a large language model (LLM) selects fine-tuning configurations under a limited trial budget. Across transfers within and between partial differential equation (PDE) families, the LLM achieves lower held-out test nRMSE than random search and Bayesian optimisation in nearly every…

### 12. [Long Text to Predictive Features: LLM-Guided Blockwise Feature Engineering via Executable Program Search](https://arxiv.org/abs/2610.12390v1)
**Ziming Dai, Dabiao Ma, Ziheng Guo, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.12390v1) · [pdf](https://arxiv.org/pdf/2610.12390v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Industrial risk-control systems typically rely on structured-data models for efficient prediction, yet substantial valuable information remains embedded in unstructured long text. Extracting this information through manual feature engineering is labor-intensive, while requiring a large language model (LLM) to process every real-time input may not meet practical deployment requirements. To address this challenge, we propose LLM-BlockFE, an LLM-guided offline feature…


<sub>Generated 2026-10-11 18:04 UTC via the arXiv API.</sub>

---

## Archive

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

_…and 43 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
