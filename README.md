# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-05** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-05

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [C-WFDM: A ControlNet-Guided Wavelet-Fusion Diffusion Model for Multimodal Brain MRI Completion](https://arxiv.org/abs/2611.05737)
**Muhammad Nabi Yasinzai, Remika Mito, Mangor Pedersen**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.05737) · [pdf](https://arxiv.org/pdf/2611.05737)  ·  relevance 38
<br>matched: `neuroimaging`, `brain mri`, `diffusion model`, `multimodal`

> Multimodal brain MRI provides complementary anatomical, tissue, and pathological information to support downstream artificial intelligence (AI) applications. However, modality availability is uneven across public and pooled neuroimaging datasets: T1-weighted (T1w) MRI is widely represented, T2-weighted (T2w) and fluid-attenuated inversion recovery (FLAIR) MRI are less consistently available, and gadolinium-enhanced T1-weighted (T1Gd) MRI is relatively scarce. Pooled datasets…

### 2. [What Does It Mean to Remove an Edge? Intervention-Aware Fidelity for Graph Neural Network Explanations](https://arxiv.org/abs/2611.04751)
**Rocco Mattia Di Mauro, Marco Grassia, Giuseppe Mangioni**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.04751) · [pdf](https://arxiv.org/pdf/2611.04751)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Graph neural network explanations are often evaluated via deletion fidelity, i.e., by deleting their top-ranked edges and measuring the resulting change in model output. Yet, in a message-passing GNN, "deleting an edge" does not specify a unique intervention. Structural deletion removes the edge from the graph and recomputes quantities such as degree normalization and attention, whereas message suppression leaves this structural context intact while blocking the message…

### 3. [LENS: Reliability-Aware Stock Prediction via LLM-Extracted Priors and News-Driven Semantic Graphs](https://arxiv.org/abs/2611.04217)
**Hao Zhou, Tiejun Ma, Luis Felipe Costa Sperb**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.04217) · [pdf](https://arxiv.org/pdf/2611.04217)  ·  relevance 25
<br>matched: `graph neural network`, `graph neural`, `gnn`, `large language model`, `llm`

> Predicting stock returns requires modeling persistent company relations and time-varying market signals. Graph Neural Network (GNN) approaches combine static priors with dynamic relational graphs, but treat every extracted edge as a trustworthy binary fact, ignoring heterogeneous reliability across relational sources. We propose LENS (LLM-Extracted priors and News-driven Semantics), a static--dynamic graph framework for stock return prediction and ranking that models…

### 4. [RGDM: Robust Graph Diffusion Model](https://arxiv.org/abs/2611.04146)
**Yancheng Wang, Ping Li, Dongfang Sun, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.04146) · [pdf](https://arxiv.org/pdf/2611.04146)  ·  relevance 24
<br>matched: `graph neural network`, `graph neural`, `gnn`, `diffusion model`, `generative model`

> Diffusion models represent a powerful class of generative models known for their solid theoretical foundations and remarkable performance across diverse tasks and domains. Existing node level diffusion methods synthesize nodes and edges within a graph, but are not designed to learn a robust generator from adversarially corrupted graphs. In this study, we introduce the Robust Graph Diffusion Model (RGDM), designed to generate labeled synthetic graph structures consisting of…

### 5. [Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models](https://arxiv.org/abs/2611.05927)
**Donggeun Kim**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.05927) · [pdf](https://arxiv.org/pdf/2611.05927)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Mixture-of-Experts (MoE) enables multimodal large language models (MLLMs) to scale capacity efficiently, but expert parameters dominate memory even though only a few experts are activated per token: they account for over 90% of model size in modern MoE-MLLMs (e.g., 54 GB out of about 58 GB in BF16 for InternVL3.5-30B-A3B and Qwen3-VL-30B-A3B). Expert pruning has emerged as an effective compression strategy, but existing methods aggregate importance uniformly across tokens,…

### 6. [FlyHash for LLM Agent Memory: An Empirical Validation and a New Application](https://arxiv.org/abs/2611.05791)
**Mohan Bheemadolu, Chrisogonas O. Odhiambo**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.05791) · [pdf](https://arxiv.org/pdf/2611.05791)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents increasingly rely on external memory stores to retain information across conversations, typically via dense vector embeddings searched with approximate nearest-neighbor methods. The fruit fly's olfactory circuit computes a locality-sensitive hash of sensory input using a strikingly different mechanism - sparse random projection followed by winner-take-all competition - and prior work (Dasgupta et al., 2017) showed this scheme, dubbed…

### 7. [Graph-Mediated Large Language Model Systems in the Agentic Era: Reasoning, Knowledge, Retrieval, Execution, and Coordination](https://arxiv.org/abs/2611.05953)
**Haihui Liu, Yang Chen, Zice Qiu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.05953) · [pdf](https://arxiv.org/pdf/2611.05953)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Graphs play an increasingly important role in large language model (LLM) systems, supporting structural reasoning, knowledge grounding, retrieval, and memory. As these systems evolve toward the agentic era, graphs also organize execution dependencies and multi-agent communication, linking intermediate observations and retained information to subsequent decisions. However, understanding their contribution requires distinguishing the function of each graph operation, the…

### 8. [HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents](https://arxiv.org/abs/2611.06254)
**Zhi Hong, Qianlong Wang, Hongchen Wei, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.06254) · [pdf](https://arxiv.org/pdf/2611.06254)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through costly end-to-end evaluations. We introduce HarnessFlow, a framework for optimizing complete executable harnesses under a limited candidate-evaluation budget, with the model and task environment held…

### 9. [A Systematic Benchmark for Evaluating Multimodal Personalized Reasoning of Vision-Language Models](https://arxiv.org/abs/2611.06259)
**Dohyun Kim, Junyong Lhim, Kwanyong Park**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.06259) · [pdf](https://arxiv.org/pdf/2611.06259)  ·  relevance 18
<br>matched: `large language model`, `llm`, `interpretab`, `multimodal`

> People often make decisions by holistically reasoning over heterogeneous forms of personal information. In this paper, we study the relatively underexplored capability of multimodal personalized reasoning in multimodal large language models (MLLMs). To this end, we introduce \texttt{MPRBench}, a novel and comprehensive benchmark specifically designed to evaluate personalized reasoning across a wide range of tasks and real-world challenges. \texttt{MPRBench} consists of 12…

### 10. [ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841)
**Xinrui Zhong, Zhiming Wang, Yongqi Liu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.06841) · [pdf](https://arxiv.org/pdf/2611.06841)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) coding agents develop software through experimentation, offering an opportunity to design the serving systems supporting their own operation. Effective serving requires coordinating implementation and operating decisions under session dependencies, latency constraints, and correctness requirements. We introduce ServerBench, a benchmark for agentic design of complete, specialized LLM serving systems. Agents experiment against a common objective,…

### 11. [On Turn-Level Best-of-N Sampling for Scaling LLM Agents](https://arxiv.org/abs/2611.06868)
**Jalaj Bhandari, Dhawal Gupta, Hongli Zhan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.06868) · [pdf](https://arxiv.org/pdf/2611.06868)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> In this work, we evaluate a simple inference-time scaling approach based on \textit{turn-level best-of-N sampling} (\method) for large language model (LLM) agents on complex, long-horizon tasks. We instantiate this using a \textit{generator-selector} framework with two LLMs; at each turn, a \emph{generator} model generates $N$ candidate actions and a \emph{selector} model selects one of them, which is then executed in the environment. This paper is closely related to the…

### 12. [TSFM Meets LLM: Context as Covariates](https://arxiv.org/abs/2611.05515)
**Hemanth Ram, Sai Shankar Narasimhan, Shubhankar Agarwal, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.05515) · [pdf](https://arxiv.org/pdf/2611.05515)  ·  relevance 18
<br>matched: `foundation model`, `large language model`, `llm`, `multimodal`

> Textual information is ubiquitous in real-world time series datasets, appearing as news, reports, and annotations that hold key predictive signals not deducible from numerical history alone. Large Language Models (LLMs) interpret text but lack numerical precision, while Time Series Foundation Models (TSFMs) are quantitatively accurate but cannot reason about the effects of text. Moreover, the lack of large-scale paired multimodal datasets limits progress in bridging this…


<sub>Generated 2026-11-05 20:39 UTC via the arXiv API.</sub>

---

## Archive

- [2026-11-05](digests/2026-11-05.md) — 12 papers
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

_…and 68 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
