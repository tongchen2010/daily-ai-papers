# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-15** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-15

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [MALNISI-Infused Graph Construction and Weighted Contrastive Loss based GAT for Unsupervised Representation Learning in HSI](https://arxiv.org/abs/2611.17199v1)
**Soumi Sarkar, Subhadip Boral, Sarbani Palit, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.17199v1) · [pdf](https://arxiv.org/pdf/2611.17199v1)  ·  relevance 21
<br>matched: `graph neural network`, `graph neural`, `representation learning`

> Hyperspectral images (HSI) possess discriminating spectral characteristics with respect to land utilization due to high-dimensional information. Recently, unsupervised representation learning using graph neural networks has unveiled these utilization-specific complex spectral relations. This article has three main contributions. First, it proposes an index, the Mean Absolute Local Neighborhood Inverse Spectral Index (MALNISI), which measures the similarity between two pixels…

### 2. [AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems](https://arxiv.org/abs/2611.17015v1)
**Tian Cai, Andrew Kleist, Jaimin Patel, et al.**  ·  `q-bio.BM`  ·  [abs](https://arxiv.org/abs/2611.17015v1) · [pdf](https://arxiv.org/pdf/2611.17015v1)  ·  relevance 18
<br>matched: `foundation model`, `large language model`, `agent`

> Artificial intelligence (AI) is changing how biological research is done. Biological foundation models trained on millions of nucleotides, protein, and single-cell measurements predict protein structures, mutation effects, and cellular responses to genetic perturbations. Agentic systems, AI assistants built on large language models, can run multistep analyses from plain-language requests and increasingly call foundation models as tools. Yet it is often unclear when these…

### 3. [Morphological Simplification in Alzheimer's Disease: Computational Analysis and Identification From Connected Speech](https://arxiv.org/abs/2611.16968v1)
**Mohamed Zakaria Kurdi**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.16968v1) · [pdf](https://arxiv.org/pdf/2611.16968v1)  ·  relevance 18
<br>matched: `alzheimer`

> Purpose: Morphology is often regarded as relatively spared in Alzheimer's disease (AD) and is rarely modeled in connected speech. This study asked which morphological features distinguish speakers with AD from healthy controls, how well morphology classifies AD compared with other linguistic levels and BERT-based models, and whether the signal exceeds transcript length and vocabulary. Method: Fifty-five automatic measures in eight families, seven of them new and…

### 4. [Temporal Regularized Learning: Self-Supervised Learning Local in Space and Time](https://arxiv.org/abs/2611.17019v1)
**Davide Wiest**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.17019v1) · [pdf](https://arxiv.org/pdf/2611.17019v1)  ·  relevance 16
<br>matched: `representation learning`, `self-supervised`

> Layer-local self-supervised objectives remove the backward pass between layers, but almost all still compute their loss over a batch of samples and are therefore local in space but not in time. We introduce Temporal Regularized Learning (TeReL), a spatially and temporally local learning rule for self-supervised representation learning from sequential input streams. The key idea is to instantiate a VICReg-style objective with temporally adjacent positives and…

### 5. [Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM Pipeline](https://arxiv.org/abs/2611.17220v1)
**Geoffrey Challen, Craig Zilles**  ·  `cs.CY`  ·  [abs](https://arxiv.org/abs/2611.17220v1) · [pdf](https://arxiv.org/pdf/2611.17220v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Oral exams are compelling because (1) students can be asked to provide their reasoning for an answer and (2) their interactive nature permits follow-up questions to resolve ambiguous answers. But oral exams scale poorly. In this paper, we present scalable conversational assessment, an LLM-based system that conducts interactive text-based conversations with students to assess their ability to make and support an argument. We use a two-agent architecture to separate concerns…

### 6. [Al-Ghasali: A Computational Framework for Simulating Islamic Jurisprudential Rulings via Finite State Automata and Large Language Models](https://arxiv.org/abs/2611.17235v1)
**Elnaserledinellah Mahmoud Abdelwahab**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.17235v1) · [pdf](https://arxiv.org/pdf/2611.17235v1)  ·  relevance 14
<br>matched: `transformer`, `large language model`, `llm`

> This paper presents Al Ghasali, a computational framework designed to formalize and simulate Islamic jurisprudential (Fiqh) rulings. Building upon recent set theoretic formalizations of al sabr wa al Taqsim that extract minimal operational rules as simple Horn clause logical programs, this work proves that the semantics of closed Fiqh chapters collapse completely to deterministic Finite State Automata (FSA). We establish a formal computational hierarchy, demonstrating that…

### 7. [Programming Quantum Circuit Parameters with Large Language Models](https://arxiv.org/abs/2611.17246v1)
**Tiago de Souza Farias, Caio Moraes Porto, Matheus da Silva Fonseca, et al.**  ·  `quant-ph`  ·  [abs](https://arxiv.org/abs/2611.17246v1) · [pdf](https://arxiv.org/pdf/2611.17246v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Large language models (LLMs) have recently demonstrated the ability to generate parameters for variational quantum circuits without conventional optimization. However, the conditions under which this approach is effective remain unclear. Here, we investigate a frozen, general-purpose LLM that generates complete circuit parameter vectors from symbolic circuit and Hamiltonian descriptions, with optional iterative energy feedback. We evaluate the approach on general random…

### 8. [Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery](https://arxiv.org/abs/2611.17241v1)
**Samidha Verma, Ankit Anand, Sayan Ranu**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.17241v1) · [pdf](https://arxiv.org/pdf/2611.17241v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Modern automated heuristic discovery (AHD) systems increasingly rival hand-crafted heuristics by leveraging Large Language Models (LLMs) to iteratively mutate and refine solutions. A natural assumption is that more powerful and more expensive models consistently yield better heuristics. We challenge this empirically: across multiple NP-hard combinatorial optimization problems, we find no consistent advantage for larger, costlier models. This raises a deeper question: given a…

### 9. [Reasoning Supervision and Capability Retention in LoRA Domain Adaptation](https://arxiv.org/abs/2611.17072v1)
**Saleh Ashkboos, Dhruv Desai, Lavinia Ghita**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.17072v1) · [pdf](https://arxiv.org/pdf/2611.17072v1)  ·  relevance 12
<br>matched: `foundation model`, `domain adaptation`

> Fine-tuning foundation models on financial data has a wide range of applications, including identifying event types from news, monitoring risk and compliance language, and answering questions over filings and earnings calls. In this setting, the main challenge is to improve task performance without degrading the generalization capabilities of the model. In this paper, we present an extensive set of ablations for fine-tuning Qwen3-8B with low-rank adaptation (LoRA). We…

### 10. [Goal Encoding in LLMs](https://arxiv.org/abs/2611.17297v1)
**Arnab Sen Sharma, Eric Todd, Sheridan Feucht, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.17297v1) · [pdf](https://arxiv.org/pdf/2611.17297v1)  ·  relevance 11
<br>matched: `transformer`, `llm`

> We investigate whether and how LLMs encode goals: internal neural representations that precede and guide action, and that are flexible enough to be realized through many different execution paths. We construct a coding setting with multiple sub-tasks that allows us to evaluate goal-seeking behavior and the selection of sub-goals. In this setting, we localize an encoding of the next sub-goal in the outputs of a sparse set of attention heads. The same heads can be used to…

### 11. [AeroZoo: A Benchmark of Well-Posed Flow Problems for Foundation Models of Aerodynamics](https://arxiv.org/abs/2611.17152v1)
**Peter Sharpe, Carmelo Gonzales, Corey Adams, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.17152v1) · [pdf](https://arxiv.org/pdf/2611.17152v1)  ·  relevance 11
<br>matched: `foundation model`, `transformer`

> Neural surrogates for computational fluid dynamics (CFD) are trained and ranked on datasets that each vary one design family in one flow domain. Such datasets cannot test the least that an aerodynamic foundation model must do: predict CFD-quality incompressible flow in seconds for new shapes in new enclosures. On DrivAerML, larger models and longer training barely lower Transolver's error; doubling the training cases cuts it by about 12% up to 400 cases, exhausting the…

### 12. [Your Vision Foundation Model Is Secretly an EEG Foundation Model](https://arxiv.org/abs/2611.17031v1)
**Guoan Wang, Feng Liu**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.17031v1) · [pdf](https://arxiv.org/pdf/2611.17031v1)  ·  relevance 11
<br>matched: `foundation model`, `transformer`

> Electroencephalography (EEG) foundation models are pretrained on thousands of hours of recordings, yet their frozen features transfer poorly to downstream tasks, and this transfer does not consistently improve with larger models or more pretraining data. We show that a vision foundation model that has never seen EEG is a stronger frozen EEG encoder than these specialized models, once the signals are rendered as images that a vision transformer can read. Our method, SeeEEG,…


<sub>Generated 2026-11-15 19:22 UTC via the arXiv API.</sub>

---

## Archive

- [2026-11-15](digests/2026-11-15.md) — 12 papers
- [2026-11-14](digests/2026-11-14.md) — 12 papers
- [2026-11-13](digests/2026-11-13.md) — 12 papers
- [2026-11-12](digests/2026-11-12.md) — 12 papers
- [2026-11-11](digests/2026-11-11.md) — 12 papers
- [2026-11-10](digests/2026-11-10.md) — 12 papers
- [2026-11-09](digests/2026-11-09.md) — 12 papers
- [2026-11-08](digests/2026-11-08.md) — 12 papers
- [2026-11-07](digests/2026-11-07.md) — 12 papers
- [2026-11-06](digests/2026-11-06.md) — 12 papers
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

_…and 78 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
