# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-31** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-31

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Benchmarking Graph Neural Networks for AC Power Flow: The Role of Inductive Biases and Physical Constraints](https://arxiv.org/abs/2610.38985)
**Federico Clerici, Ferran Bohigas-Daranas, Hamid Latif-Mart\'inez, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.38985) · [pdf](https://arxiv.org/pdf/2610.38985)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Fast and accurate models for AC power flow (ACPF) are increasingly important as modern electrical grids require more frequent system analyses. Graph neural networks (GNNs) naturally exploit electrical grid topology, yet the effects of architectural design choices on predictive performance remain poorly understood given differences in graph representations and evaluation settings across studies. We present a unified benchmark of representative GNN architectures for ACPF…

### 2. [LLM-Integrated Bayesian State Space Models for Multimodal Time-Series Forecasting](https://arxiv.org/abs/2510.20952)
**Sungjun Cho, Changho Shin, Suenggwan Jo, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2510.20952) · [pdf](https://arxiv.org/pdf/2510.20952)  ·  relevance 27
<br>matched: `large language model`, `llm`, `multimodal`, `state space model`

> Forecasting in the real world requires integrating structured time-series data with unstructured textual information, but existing methods are architecturally limited by fixed input/output horizons and are unable to model or quantify uncertainty. We address this challenge by introducing LLM-integrated Bayesian State space models (LBS), a novel probabilistic framework for multimodal temporal forecasting. At a high level, LBS consists of two components: (1) a state space model…

### 3. [Post-Training Large Language Models with LLMON](https://arxiv.org/abs/2610.38120)
**Basel Shbita, Michael Hind, Chad DeLuca, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.38120) · [pdf](https://arxiv.org/pdf/2610.38120)  ·  relevance 26
<br>matched: `transformer`, `large language model`, `llm`, `retrieval-augmented`, `interpretab`

> Large Language Models (LLMs) treat all context tokens uniformly, lacking explicit separation between executable instructions and passive data. This leads to prompt injection vulnerabilities, ambiguous instruction binding, and unreliable execution control. We present a post-training methodology using LLMON (LLM Object Notation), a framework that enables separating instructions from data and requires explicit identifier-based execution. We construct a large-scale structured…

### 4. [Can LLMs Faithfully Solve Ontology Engineering Tasks? A Mechanistic Interpretability Study](https://arxiv.org/abs/2610.38326)
**Bohui Zhang, Albert Mero\~no-Pe\~nuela, Elena Simperl**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.38326) · [pdf](https://arxiv.org/pdf/2610.38326)  ·  relevance 21
<br>matched: `large language model`, `llm`, `interpretab`

> Ontological knowledge underpins large language model (LLM) performance on knowledge-intensive tasks. However, existing evaluations of LLMs' ontological understanding largely rely on behavioral correctness, leaving the underlying mechanisms unexplained. Existing mechanistic interpretability work has largely focused on instance-level factual knowledge, leaving ontological knowledge under-explored. To bridge this gap, we introduce MIOE, a causal-abstraction benchmark that…

### 5. [Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems](https://arxiv.org/abs/2610.38869)
**Zhuoyun Li, Boxuan Wang, Jinwei Hu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.38869) · [pdf](https://arxiv.org/pdf/2610.38869)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Large Language Models (LLMs) are increasingly being used as cognitive interfaces that shape how users interpret evidence, communicate, and make decisions. As deployed systems become more multimodal, tool-using, and multi-agent, safety failures no longer arise only from isolated harmful outputs, but also from how agents update, store, and propagate epistemic commitments across retrieval, memory, tools, and peer communication. In this paper, we define belief as an engineering…

### 6. [Interpretable Feature Discovery from Unstructured Data Using LLMs and Statistical Choice Models](https://arxiv.org/abs/2610.38082)
**Baptiste Arnaudo, Amine Bennouna, S\'ebastien Martin**  ·  `stat.ML`  ·  [abs](https://arxiv.org/abs/2610.38082) · [pdf](https://arxiv.org/pdf/2610.38082)  ·  relevance 21
<br>matched: `large language model`, `llm`, `interpretab`

> Feature extraction from unstructured data typically relies on opaque embeddings unsuited to interpretable decision-making. Interpretable features, on the other hand, typically require costly, and often infeasible, hand-engineering. Large language models (LLMs) offer a natural bridge, as they can read raw data and describe it in interpretable terms. One could simply ask an LLM to extract features from a large sample of the dataset, but context limitations and diluted…

### 7. [Jailbreak Connectivity: Towards Diverse, Transferable, and Universal Multimodal Large Language Model Jailbreak](https://arxiv.org/abs/2610.38091)
**Xu Zhang, Ziqing Hu, Shuo Han, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.38091) · [pdf](https://arxiv.org/pdf/2610.38091)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) are vulnerable to visual jailbreak attacks that bypass safety safeguards. Existing methods typically optimize isolated adversarial examples, limiting attack diversity, transferability, and generalization. We propose Jailbreak Connectivity (JC), a framework based on the observation that effective adversarial inputs can be connected through low-loss regions in image space. JC optimizes continuous adversarial paths: path sampling yields…

### 8. [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://arxiv.org/abs/2610.38095)
**NVIDIA, :, Aastha Jhunjhunwala, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.38095) · [pdf](https://arxiv.org/pdf/2610.38095)  ·  relevance 21
<br>matched: `transformer`, `agent`, `multimodal`, `mamba`

> We introduce Nemotron 3.5 Super and Nemotron 3.5 Lightning, open and efficient Mixture-of-Experts Hybrid Mamba-Transformer models designed for reasoning, long-context understanding, and agentic workloads. Super is a 120B-parameter, 12B-active multimodal model, while Lightning is a smaller 30B-parameter, 3B-active text model; both designed for efficient deployment. Both models combine large-scale distillation, long-context training, and native speculative decoding, while…

### 9. [Raincheck: Deferred Multimodal Prefill for Efficient Multi-Turn MLLM Inference](https://arxiv.org/abs/2610.39562)
**Wenjie Huang, Jun Zhang, Hongyaoxing Gu, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.39562) · [pdf](https://arxiv.org/pdf/2610.39562)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multi-turn conversations with multimodal large language models (MLLMs) reuse input context, but long multimodal inputs increase time to first token (TTFT). Query-aware hard pruning reduces prefill tokens but permanently excludes information that later questions may require. We propose Raincheck, a framework for deferred multimodal prefill that decouples initial token selection from later information availability. An existing pruning method selects tokens for initial prefill;…

### 10. [DecompGym: Benchmarking LLM Agents on Designing Decomposition Algorithms](https://arxiv.org/abs/2610.38175)
**Sikai Cheng, Tinghan Ye, Arnaud Deza, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.38175) · [pdf](https://arxiv.org/pdf/2610.38175)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Benders decomposition and column generation solve large optimization problems by passing cuts, columns, and dual values between a master problem and subproblems, and are hard to implement correctly. Large language models now automate parts of algorithm design, which points toward agents that build decomposition solvers for new problems. As a first step toward such agents, we study how well current coding agents design and implement these two algorithms, and how they fail. We…

### 11. [Vendster: An Evaluation Arena to Investigate How Forecasting Tool Quality Affects LLM Agent Behaviors in Buyer-Vendor Negotiation](https://arxiv.org/abs/2610.38292)
**Charin Polpanumas**  ·  `cs.GT`  ·  [abs](https://arxiv.org/abs/2610.38292) · [pdf](https://arxiv.org/pdf/2610.38292)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Time-series forecasters are ranked almost entirely by accuracy metrics, but a forecast's decision value, its effect on the downstream decision, need not track accuracy and is rarely measured. This problem compounds as large language model (LLM) agents increasingly consume forecasters as tools, mediating them through stochastic, opaque policies. We present Vendster, an evaluation arena measuring how a forecaster's bias and prediction-interval width change the outcome of a…

### 12. [REALM: Identifying Minimal Task Assets for LLM Agents](https://arxiv.org/abs/2610.39155)
**Zihou Ren, Byungchul Tak, Long Wang**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2610.39155) · [pdf](https://arxiv.org/pdf/2610.39155)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents often receive access to more files, accounts, and services than a task requires. Prompt injection turns this excess access into an opportunity to redirect execution toward unrelated resources. Applying least privilege therefore requires identifying the assets needed by a task, including assets whose identities emerge only during execution. We present REALM (Required Execution Assets Linked to a Mission), an approach to identifying and…


<sub>Generated 2026-10-31 17:43 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-28](digests/2026-08-28.md) — 12 papers

_…and 63 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
