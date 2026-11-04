# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-04** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-04

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [What Does It Mean to Remove an Edge? Intervention-Aware Fidelity for Graph Neural Network Explanations](https://arxiv.org/abs/2611.04751)
**Rocco Mattia Di Mauro, Marco Grassia, Giuseppe Mangioni**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.04751) · [pdf](https://arxiv.org/pdf/2611.04751)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Graph neural network explanations are often evaluated via deletion fidelity, i.e., by deleting their top-ranked edges and measuring the resulting change in model output. Yet, in a message-passing GNN, "deleting an edge" does not specify a unique intervention. Structural deletion removes the edge from the graph and recomputes quantities such as degree normalization and attention, whereas message suppression leaves this structural context intact while blocking the message…

### 2. [Measure Before You Repair: An Explainable Agent for Blind Restoration of Multi-Artifact 3-D MRI](https://arxiv.org/abs/2611.03996)
**Necati Sefercioglu, Mehmet Ozan Unal, Metin Ertas, et al.**  ·  `eess.IV`  ·  [abs](https://arxiv.org/abs/2611.03996) · [pdf](https://arxiv.org/pdf/2611.03996)  ·  relevance 29
<br>matched: `brain mri`, `large language model`, `llm`, `agent`, `explainab`, `multimodal`

> A brain MRI scan can carry an unknown mix of artifacts, so restoration has to be blind, yet most deep-learning methods are built to correct one known artifact. We present Dx-Rx, an agent in which a multimodal large language model (MLLM) measures suspected artifacts before it repairs them. To our knowledge, it is the first agent to restore whole 3-D MRI volumes, whereas earlier MRI agents restore 2-D slices. In a loop, it looks at slices of the 3-D volume, calls five…

### 3. [LENS: Reliability-Aware Stock Prediction via LLM-Extracted Priors and News-Driven Semantic Graphs](https://arxiv.org/abs/2611.04217)
**Hao Zhou, Tiejun Ma, Luis Felipe Costa Sperb**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.04217) · [pdf](https://arxiv.org/pdf/2611.04217)  ·  relevance 25
<br>matched: `graph neural network`, `graph neural`, `gnn`, `large language model`, `llm`

> Predicting stock returns requires modeling persistent company relations and time-varying market signals. Graph Neural Network (GNN) approaches combine static priors with dynamic relational graphs, but treat every extracted edge as a trustworthy binary fact, ignoring heterogeneous reliability across relational sources. We propose LENS (LLM-Extracted priors and News-driven Semantics), a static--dynamic graph framework for stock return prediction and ranking that models…

### 4. [RGDM: Robust Graph Diffusion Model](https://arxiv.org/abs/2611.04146)
**Yancheng Wang, Ping Li, Dongfang Sun, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.04146) · [pdf](https://arxiv.org/pdf/2611.04146)  ·  relevance 24
<br>matched: `graph neural network`, `graph neural`, `gnn`, `diffusion model`, `generative model`

> Diffusion models represent a powerful class of generative models known for their solid theoretical foundations and remarkable performance across diverse tasks and domains. Existing node level diffusion methods synthesize nodes and edges within a graph, but are not designed to learn a robust generator from adversarially corrupted graphs. In this study, we introduce the Robust Graph Diffusion Model (RGDM), designed to generate labeled synthetic graph structures consisting of…

### 5. [GlucoAgent: Personalized Glucose Forecasting from Multimodal Personal Context](https://arxiv.org/abs/2611.04126)
**Xingzhi Sun, Hyo Jin Kim, Zhiyuan Wang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.04126) · [pdf](https://arxiv.org/pdf/2611.04126)  ·  relevance 21
<br>matched: `foundation model`, `llm`, `agent`, `multimodal`

> Continuous glucose monitors, smartwatches, meal logs, and health profiles form a rich multimodal personal context that can significantly enhance glucose forecasting. However, existing methods struggle to effectively utilize these signals to improve glucose prediction because the relevance of different modalities varies drastically across individuals and time. We present GlucoAgent, an LLM-based agentic system that addresses this challenge through dynamic, case-by-case…

### 6. [What Does the Model See? Representation Validity in Multimodal LLM-Based Video Analysis](https://arxiv.org/abs/2611.05181)
**Christian Pipal, Eva-Maria Vogel, Morgan Wack**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.05181) · [pdf](https://arxiv.org/pdf/2611.05181)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) allow social scientists to analyze video at scale, but researchers must decide which parts of a video to provide as input. We use the term representation validity to examine how text, audio, video, and combined inputs affect measurement and subsequent analysis. We compare input representations across six open-weight MLLMs and three human-annotated video datasets. No representation consistently performs best. On seven news-related…

### 7. [Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling](https://arxiv.org/abs/2611.04916)
**Kling Team, Dong Chen, Jialu Chen, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.04916) · [pdf](https://arxiv.org/pdf/2611.04916)  ·  relevance 20
<br>matched: `foundation model`, `llm`, `agent`, `explainab`, `multimodal`

> Video generation has progressed from isolated clips to coherent short-form audiovisual sequences, and the bottleneck is shifting from rendering to semantic control. This report summarizes the observations and insights on multimodal understanding gained from successive generations of Kling. We argue that generation quality is the projection of multimodal understanding through the entire data--conditioning--alignment--evaluation chain, and we examine this chain module by…

### 8. [PATTS: Parallel-Aware Test-Time Scaling for Thought-Image Generation in Multimodal Discrete Diffusion LLMs](https://arxiv.org/abs/2611.04948)
**Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.04948) · [pdf](https://arxiv.org/pdf/2611.04948)  ·  relevance 20
<br>matched: `generative model`, `llm`, `multimodal`

> Test-time scaling (TTS) improves generative models by allocating additional inference-time computation to sampling, search, and verification. Existing image generation approaches, however, typically rank completed images or image-centric intermediate states. We study TTS for parallel multimodal discrete diffusion language models, in which reasoning tokens and image tokens are decoded jointly within a single generation trajectory. We first diagnose a limitation of…

### 9. [Behavioral Prior Elicitation via LLM for Heterogeneous-Agent Bitcoin Flash-Crash Simulation](https://arxiv.org/abs/2611.03660)
**Tran Phuong Linh Pham, Thi Minh Phuong Ngo, Phuong Thao Nguyen, et al.**  ·  `stat.AP`  ·  [abs](https://arxiv.org/abs/2611.03660) · [pdf](https://arxiv.org/pdf/2611.03660)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Bitcoin perpetual futures trade continuously with shallow liquidity and high price impact, making them prone to millisecond-scale flash crashes. Agent-based limit order book simulators are a natural tool for studying such events, but their behavioral parameters are usually hand-crafted or require full order book histories that are rarely available at scale. We propose a four-stage pipeline that constructs a reproducible 100 ms BTCUSDT flash-crash event panel from 66 detected…

### 10. [LLMs as MDP Designers: A Dependency-Aware Agentic Framework for Automated Robot Policy Generation](https://arxiv.org/abs/2611.04974)
**Hong Je-Gal, Jinwoo Kim, Chanbin Yi, et al.**  ·  `cs.RO`  ·  [abs](https://arxiv.org/abs/2611.04974) · [pdf](https://arxiv.org/pdf/2611.04974)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> We investigate the automated generation of executable robot reinforcement learning (RL) policies from natural-language task descriptions. Rather than using large language models (LLMs) as execution-time decision makers, we use them as designers that construct RL pipelines before deployment, including Markov decision process (MDP) formulation and simulator implementation. We identify a phase-wise structure in this problem: MDP formulation is dependency-structured and…

### 11. [TraceRouter++: Causal Semantic Routing Realignment via Optimal Transport](https://arxiv.org/abs/2611.04878)
**Chuancheng Shi, Shangze Li, Wenhua Wu, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.04878) · [pdf](https://arxiv.org/pdf/2611.04878)  ·  relevance 18
<br>matched: `foundation model`, `diffusion model`, `large language model`, `llm`, `interpretab`, `multimodal`

> Despite their remarkable capabilities, large foundation models (LFMs) remain susceptible to adversarial manipulation. Current safety intervention methods primarily rely on the \textit{locality hypothesis}, rigidly suppressing isolated neurons or features. However, harmful semantics manifest as distributed, cross-layer circuits, rendering localized ablations both brittle against complex jailbreaks and detrimental to general utility. To bridge this gap, we propose…

### 12. [OpenBrain: An Auditable Generated-Label Release for Whole-Brain MRI Parcellation](https://arxiv.org/abs/2611.05348)
**Qizhen Lan, Yu-Chun Hsu, Yuxiang Wei, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.05348) · [pdf](https://arxiv.org/pdf/2611.05348)  ·  relevance 17
<br>matched: `brain mri`, `segmentation`

> Automatic tools can now generate whole-brain MRI parcellations at cohort scale, but generated-label releases often provide little evidence about which cases are reliable enough to reuse. We introduce OpenBrain, a confidence-aware release of 35,838 provenance-verified OpenNeuro T1w cases from 607 source datasets. OpenBrain is organized as an auditable case-record release rather than a directory of standalone segmentation files: each record links a primary parcellation, two…


<sub>Generated 2026-11-04 20:25 UTC via the arXiv API.</sub>

---

## Archive

- [2026-11-04](digests/2026-11-04.md) — 12 papers
- [2026-11-03](digests/2026-11-03.md) — 12 papers
- [2026-11-02](digests/2026-11-02.md) — 12 papers
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

_…and 67 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
