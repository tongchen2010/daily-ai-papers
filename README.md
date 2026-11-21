# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-21** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-21

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Phantom of the Masquerade: Graph Neural Network-Based Detection of Masquerade Attacks in Controller Area Networks](https://arxiv.org/abs/2611.26094)
**Nehal Ameen, Pablo Moriano, Irfan Ahmed**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2611.26094) · [pdf](https://arxiv.org/pdf/2611.26094)  ·  relevance 35
<br>matched: `graph neural network`, `graph neural`, `gnn`, `representation learning`

> The lack of built-in security in controller area networks (CANs) exposes modern vehicles and industrial systems to masquerade attacks that can compromise safety and reliability. These attacks inject malicious messages that mimic legitimate communication patterns, making them difficult to detect using existing intrusion detection systems (IDS). Prior graph-based IDS approaches often rely on shallow embeddings that decouple representation learning from classification, which…

### 2. [AdsNet: A Graph Neural Network for Direct Adsorption Energy Prediction](https://arxiv.org/abs/2611.25646)
**Changzhi Ai, Frank Abild-Pedersen, Johannes Voss**  ·  `cond-mat.mtrl-sci`  ·  [abs](https://arxiv.org/abs/2611.25646) · [pdf](https://arxiv.org/pdf/2611.25646)  ·  relevance 30
<br>matched: `graph neural network`, `graph neural`, `interpretab`

> Fast and accurate prediction of adsorption energies is critical for high-throughput computational catalyst screening, existing methods compromise either on evaluation speed (full-graph machine learning potentials) or geometric sensitivity (coordination-based models like the alpha-scheme). Here, we present AdsNet, an equivariant graph neural network that directly predicts adsorption energies in a single forward pass, which operates on a local graph restricted only to…

### 3. [Perfumer: A Large Language Model-based Agentic Framework Accelerating Structural Relaxation and Electronic Band Prediction for First-Principle Calculation](https://arxiv.org/abs/2611.26349)
**Zhiwei Li, Yuhao Zhou, Yikai Yang, et al.**  ·  `cond-mat.mtrl-sci`  ·  [abs](https://arxiv.org/abs/2611.26349) · [pdf](https://arxiv.org/pdf/2611.26349)  ·  relevance 24
<br>matched: `graph neural network`, `graph neural`, `large language model`, `agent`

> First-principles structural relaxation and band calculations require substantial computation and expertise. Here we present Perfumer, a large language model-based agentic framework that couples Quantum ESPRESSO with two predictive models. Across tested structures, pre-relaxation with Perfumer-relax model followed by QE refinement yielded a 2.75-fold overall speedup over QE alone. Perfumer-band model combines a periodic graph neural network with a latent Hermitian spectral…

### 4. [On the Informativeness of Structural Stability Bounds for GNNs: GINs versus GATs](https://arxiv.org/abs/2611.25603)
**Alan Gany, Paul Landrier, Bogdan Cautis, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.25603) · [pdf](https://arxiv.org/pdf/2611.25603)  ·  relevance 21
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Stability bounds for graph neural networks limit how much node representations can drift when the graph changes, but they are rarely compared with the simplest alternative: a bound on the distance between any two outputs, whatever the graph. We derive structural stability bounds for Graph Isomorphism Networks (GINs) and single-head GATv1 networks under deterministic edge perturbations that need not be small, and compare each with such a perturbation-independent diameter…

### 5. [Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark](https://arxiv.org/abs/2611.25252)
**Zhenling Chen, Zhiguo Zeng, Anne Barros**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.25252) · [pdf](https://arxiv.org/pdf/2611.25252)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Coding agents built on large language models (LLMs) now help develop many models published as general solutions. Should generality instead reside in the agent that builds a model for each new task? We examine this question in prognostics and health management (PHM), where every model must work on unseen equipment. Our deployment-style benchmark, NextUnit-Bench, covers 24 public datasets split into 58 folds that hold out units or operating conditions; each agent has two hours…

### 6. [LLM Complexity: Towards a Computational Complexity View of Large Language Model Inference](https://arxiv.org/abs/2611.24943)
**Yu-Hung Wu, Shao-Xiang Yuan, Chan-Hung Yu, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.24943) · [pdf](https://arxiv.org/pdf/2611.24943)  ·  relevance 18
<br>matched: `large language model`, `llm`

> Computational complexity theory offers a principled framework for characterizing the efficiency of computational problems, and Large Language Models (LLMs) can similarly be viewed as computational systems executing a structured process of input, inference-time compute, and output. In this context, the number of generated tokens emerges as a natural and directly observable proxy for inference-time compute. However, we show that the tempting analogy between LLM token length…

### 7. [Statistical, Machine Learning and Deep Learning Methods for Missing Covariates: An Empirical Evaluation with Applications to Alzheimer's Disease Research](https://arxiv.org/abs/2611.25219)
**Yiqing Pan, Sharon X. Xie, Shujie Ma, et al.**  ·  `stat.ML`  ·  [abs](https://arxiv.org/abs/2611.25219) · [pdf](https://arxiv.org/pdf/2611.25219)  ·  relevance 18
<br>matched: `alzheimer`

> Missing data are common in biomedical research, particularly when biomarkers are costly or require invasive procedures to obtain, such as cerebrospinal fluid measures in Alzheimer's disease. Although a wide range of missing data methods exists, from traditional statistical approaches to modern machine learning (ML) and deep learning (DL) algorithms, their comparative performance under different missingness mechanisms remains insufficiently understood. In this study, we…

### 8. [Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](https://arxiv.org/abs/2611.25898)
**Youssef ElNahas, Adel Ammar, Soumaya Chaffar, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.25898) · [pdf](https://arxiv.org/pdf/2611.25898)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demographic shortcuts can pass conventional evaluation. This critical review covers four paradigms in turn: how clinical hallucination arises and why static metrics miss it; the agentic hallucination cascade,…

### 9. [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617)
**Yuxin Jiang, Wenqiang Sun, Jiaqi Li, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.26617) · [pdf](https://arxiv.org/pdf/2611.26617)  ·  relevance 18
<br>matched: `self-supervised`, `transformer`

> Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and…

### 10. [Empirical Variational Bayes Factorization for Longitudinal Matrix Data](https://arxiv.org/abs/2611.25065)
**Jiakun Li, Eric F. Lock**  ·  `stat.ML`  ·  [abs](https://arxiv.org/abs/2611.25065) · [pdf](https://arxiv.org/pdf/2611.25065)  ·  relevance 17
<br>matched: `disease progression`, `longitudinal`, `interpretab`

> Collecting high-dimensional data over time for multiple individuals is increasingly common in biomedical research, particularly in studies of disease progression or molecular time-course experiments. Often data are missing or the timepoints are irregularly spaced across individuals. There is a lack of flexible methodology to explore latent patterns of change over time and account for missing data. We propose an empirical variational Bayes (EVB) approach to factorize…

### 11. [Separating Interpretability and Reconstruction in Sparse Autoencoders](https://arxiv.org/abs/2611.25165)
**Anh Tien Nguyen, Dimitris Samaras, Mahdi S. Hosseini**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.25165) · [pdf](https://arxiv.org/pdf/2611.25165)  ·  relevance 16
<br>matched: `representation learning`, `llm`, `interpretab`

> Sparse Autoencoders (SAEs) are effective tools for mechanistic interpretability by decomposing neural representations into sparse and interpretable features. However, a single sparse representation in traditional SAEs is responsible for both reconstruction fidelity and interpretability, which are not guaranteed to align. To separate these objectives, we propose DualSAE, a modular framework that augments standard SAEs with a plug-in Residual Branch. A standard SAE serves as…

### 12. [Antom 3-in-1 Transformer: A Payment Foundation Model](https://arxiv.org/abs/2611.25403)
**Weiyu Han, Haoyu Jiang, Jie Sheng, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.25403) · [pdf](https://arxiv.org/pdf/2611.25403)  ·  relevance 15
<br>matched: `foundation model`, `transformer`

> We report the development of Antom 3-in-1 Transformer, a payment foundation model that integrates sequence, tabular, and graph representations for payment risk detection. The model contains approximately 7B parameters, with approximately 1.7B activated per task route. Antom 3-in-1 Transformer is pretrained to learn reusable behavioral and relational representations, primarily on Ant International's internal payment data. In a cross-business transfer experiment, pretraining…


<sub>Generated 2026-11-21 20:05 UTC via the arXiv API.</sub>

---

## Archive

- [2026-11-21](digests/2026-11-21.md) — 12 papers
- [2026-11-20](digests/2026-11-20.md) — 12 papers
- [2026-11-19](digests/2026-11-19.md) — 12 papers
- [2026-11-18](digests/2026-11-18.md) — 12 papers
- [2026-11-17](digests/2026-11-17.md) — 12 papers
- [2026-11-16](digests/2026-11-16.md) — 12 papers
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

_…and 84 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
