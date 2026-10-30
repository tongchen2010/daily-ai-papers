# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-30** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-30

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Predicting Sparse Observables in Parameterized Unsteady Flows Using Coarse-Mesh Graph Neural Networks](https://arxiv.org/abs/2610.37986)
**Brener Ramos, William R. Wolf, Tarc\'isio C. D. Oliveira, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.37986) · [pdf](https://arxiv.org/pdf/2610.37986)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Full-order surrogates for high-dimensional nonlinear flows are often unnecessary when applications require only selected degrees of freedom. We propose reduced-order models that bypass full-state reconstruction by deploying graph neural networks (GNNs) directly on coarse meshes. Applied to parameterized 2D/3D confined cylinder flows and an unevenly heated cavity over Reynolds/Rayleigh-number ranges, the models generalize to unseen conditions and accurately predict sparse…

### 2. [A Separation Principle for Adversarial Attacks and Defense of Graph Neural Networks](https://arxiv.org/abs/2610.38127)
**Farid Mafi, Saber Jafarpour, Mohammad Pirani**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.38127) · [pdf](https://arxiv.org/pdf/2610.38127)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Adversarial attacks on graph neural networks (GNNs) have been studied as a model-centric optimization problem driven by gradients, learned policies, or meta-learning, with the graph treated as a passive substrate. This view overlooks a defining feature of GNNs: their predictions are produced by structured message passing along the graph, so their adversarial vulnerabilities are encoded as much in the geometry of the graph as in the learned weights. We develop a…

### 3. [Benchmarking Graph Neural Networks for AC Power Flow: The Role of Inductive Biases and Physical Constraints](https://arxiv.org/abs/2610.38985)
**Federico Clerici, Ferran Bohigas-Daranas, Hamid Latif-Mart\'inez, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.38985) · [pdf](https://arxiv.org/pdf/2610.38985)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Fast and accurate models for AC power flow (ACPF) are increasingly important as modern electrical grids require more frequent system analyses. Graph neural networks (GNNs) naturally exploit electrical grid topology, yet the effects of architectural design choices on predictive performance remain poorly understood given differences in graph representations and evaluation settings across studies. We present a unified benchmark of representative GNN architectures for ACPF…

### 4. [Recurrent Bipartite Graph Neural Networks for QC-MDPC Error Decoding in McEliece Cryptosystems](https://arxiv.org/abs/2610.38479)
**Parth Rajeshkumar Tandel, Elisabeth Fink**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2610.38479) · [pdf](https://arxiv.org/pdf/2610.38479)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> As the advent of large-scale quantum computing threatens classical encryption, Quasi-Cyclic Moderate Density Parity-Check (QC-MDPC) codes have emerged as a foundational element of Post-Quantum Cryptography (PQC). However, decoding these relatively dense codes using classical Belief Propagation algorithms often leads to failures caused by short graph cycles that stall the decoder. In cryptographic applications, these failures are severe security vulnerabilities that leak…

### 5. [MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments](https://arxiv.org/abs/2610.39936)
**Zhiliang Wu, Xinye Zheng, Kun Li, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.39936) · [pdf](https://arxiv.org/pdf/2610.39936)  ·  relevance 29
<br>matched: `generative model`, `large language model`, `llm`, `multimodal`

> Novel view synthesis (NVS) in degraded scenes aims to reconstruct 3D scenes from multi-view observations affected by various degradations, and to generate clear and photorealistic images at unseen viewpoints. Despite recent advances, existing methods often rely on degradation-specific models, limiting their generalization across diverse extreme environments. Generative models provide rich visual priors, but their outputs often suffer from pixel misalignment and color…

### 6. [LoRe-MIM: Lost-or-Replaced Masked Image Modeling for Self-Supervised Representation Learning in Whole-Body PET/CT](https://arxiv.org/abs/2610.40284)
**Amartya Bhattacharya, Bashirul Azam Biswas, Biratal Raj Wagle, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.40284) · [pdf](https://arxiv.org/pdf/2610.40284)  ·  relevance 29
<br>matched: `representation learning`, `self-supervised`, `segmentation`, `multimodal`

> Deep learning models for whole-body positron emission tomography/computed tomography (PET/CT) hold significant clinical potential for disease detection, treatment planning, and response assessment. However, the time and cost associated with expert annotations remain major bottlenecks in developing robust and generalizable models. Although self-supervised learning (SSL) has emerged as a promising approach to mitigating annotation scarcity, its application to whole-body PET/CT…

### 7. [LLM-Integrated Bayesian State Space Models for Multimodal Time-Series Forecasting](https://arxiv.org/abs/2510.20952)
**Sungjun Cho, Changho Shin, Suenggwan Jo, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2510.20952) · [pdf](https://arxiv.org/pdf/2510.20952)  ·  relevance 27
<br>matched: `large language model`, `llm`, `multimodal`, `state space model`

> Forecasting in the real world requires integrating structured time-series data with unstructured textual information, but existing methods are architecturally limited by fixed input/output horizons and are unable to model or quantify uncertainty. We address this challenge by introducing LLM-integrated Bayesian State space models (LBS), a novel probabilistic framework for multimodal temporal forecasting. At a high level, LBS consists of two components: (1) a state space model…

### 8. [Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records](https://arxiv.org/abs/2610.40379)
**Daniel Palacios, Guantong Qi, Anna Kadi, et al.**  ·  `q-bio.QM`  ·  [abs](https://arxiv.org/abs/2610.40379) · [pdf](https://arxiv.org/pdf/2610.40379)  ·  relevance 27
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Large language model (LLM) agents are proposed for clinical prediction but are untested in pediatrics, where cohorts are small and outcomes are uncommon. Using records from 2,489 youth with type 2 diabetes (T2D) and 4,018 with type 1 diabetes (T1D), spanning structured data, note-derived social determinants and, in T1D, continuous glucose monitoring data, we predicted seven T2D outcomes, four also in T1D, at 24 months from 18 months of follow-up. CEDAR (Clinical…

### 9. [Post-Training Large Language Models with LLMON](https://arxiv.org/abs/2610.38120)
**Basel Shbita, Michael Hind, Chad DeLuca, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.38120) · [pdf](https://arxiv.org/pdf/2610.38120)  ·  relevance 26
<br>matched: `transformer`, `large language model`, `llm`, `retrieval-augmented`, `interpretab`

> Large Language Models (LLMs) treat all context tokens uniformly, lacking explicit separation between executable instructions and passive data. This leads to prompt injection vulnerabilities, ambiguous instruction binding, and unreliable execution control. We present a post-training methodology using LLMON (LLM Object Notation), a framework that enables separating instructions from data and requires explicit identifier-based execution. We construct a large-scale structured…

### 10. [BRIDGE: Learning Brain-Gut Metabolic Evidence for Alzheimer's Disease Diagnosis](https://arxiv.org/abs/2610.39520)
**Pengli Zhu, Ruxi Chang, Tianliang Yao, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.39520) · [pdf](https://arxiv.org/pdf/2610.39520)  ·  relevance 24
<br>matched: `alzheimer`, `large language model`, `llm`

> Alzheimer's disease (AD) diagnosis may benefit from gut metabolic information associated with brain-gut interactions, yet existing models largely analyze cerebral glucose metabolism alone. Although whole-body fluorodeoxyglucose positron emission tomography (FDG-PET) can provide paired brain-gut observations, routine brain examinations rarely include gut imaging, limiting direct use of this information for diagnosis. In this paper, we present BRIDGE (Brain and Gut…

### 11. [Jailbreak Connectivity: Towards Diverse, Transferable, and Universal Multimodal Large Language Model Jailbreak](https://arxiv.org/abs/2610.38091)
**Xu Zhang, Ziqing Hu, Shuo Han, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.38091) · [pdf](https://arxiv.org/pdf/2610.38091)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) are vulnerable to visual jailbreak attacks that bypass safety safeguards. Existing methods typically optimize isolated adversarial examples, limiting attack diversity, transferability, and generalization. We propose Jailbreak Connectivity (JC), a framework based on the observation that effective adversarial inputs can be connected through low-loss regions in image space. JC optimizes continuous adversarial paths: path sampling yields…

### 12. [Data Amount Heterogeneity Improves Performance in Federated Learning for Neuroimaging](https://arxiv.org/abs/2610.38172)
**Paul Kurian, Tamoghna Chattopadhyay, Abhijith Shaji, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.38172) · [pdf](https://arxiv.org/pdf/2610.38172)  ·  relevance 21
<br>matched: `alzheimer`, `neuroimaging`

> Federated Learning (FL) allows for secure analysis of distributed data without data sharing. We and others have successfully applied FL to neuroimaging tasks, such as Alzheimer's disease classification from structural magnetic resonance imaging (MRI). FL trains a deep learning model locally at each site, encrypts the local model parameters and sends them to a federation controller that aggregates the local models under homomorphic encryption, the resulting community model is…


<sub>Generated 2026-10-30 18:37 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-27](digests/2026-08-27.md) — 12 papers

_…and 62 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
