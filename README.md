# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-09** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-09

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Interpretable Context-Aware Multi-Label Retinal Classification with Dual-Hub Heterogeneous Graph Neural Network](https://arxiv.org/abs/2611.09309)
**Proshanto Chanda, Munib Mesinovic, Tingting Zhu, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.09309) · [pdf](https://arxiv.org/pdf/2611.09309)  ·  relevance 43
<br>matched: `graph neural network`, `graph neural`, `gnn`, `interpretab`, `multimodal`

> Multi-label retinal screening requires capturing co-occurring pathologies and clinical context, yet standard multimodal fusion remains opaque. We propose a dual-hub heterogeneous graph neural network (GNN) that couples spatial fundus features and structured clinical covariates through cross-modal message passing while providing inherent interpretability. Rather than relying on post-hoc saliency approximations, our architecture exposes multi-level decision pathways during…

### 2. [Scaling Graph Similarity Learning with Graph Neural Networks](https://arxiv.org/abs/2611.09805)
**Ahmet T\"uzen, Helge Langseth, Kjetil N{\o}rv{\aa}g**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.09805) · [pdf](https://arxiv.org/pdf/2611.09805)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Graph similarity computation is an important task in graph mining with many real-world applications, such as chemical compound analysis, program dependence comparison, and social network analysis. The problem is computationally challenging: Graph Edit Distance (GED) and Maximum Common Subgraph (MCS), which quantify the distance between graphs and identify their largest shared subgraph, respectively, are NP-hard to compute exactly. To address these computational challenges,…

### 3. [RAG-Enhanced LLMs for Interactive Explainability in Clinical Decision Support Systems](https://arxiv.org/abs/2611.09232)
**Lorenzo Mannocci, Francesca Naretto, Lucia Passaro, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.09232) · [pdf](https://arxiv.org/pdf/2611.09232)  ·  relevance 27
<br>matched: `large language model`, `llm`, `retrieval-augmented`, `interpretab`, `explainab`

> Artificial Intelligence (AI) is increasingly embedded in high-risks decision-making systems across domains such as healthcare, finance, and the judicial system. As reliance on predictive models grows, so does the demand for Explainable AI (XAI) to ensure transparency, trust, and interpretability. However, existing XAI approaches often fail to present explanations in a format accessible to domain experts, limiting their practical utility. Large Language Models (LLMs) have…

### 4. [Measurement-Aware Multimodal LLM for No-Reference Low-Dose CT Quality Assessment](https://arxiv.org/abs/2611.08754)
**Kerem Basim, Tolga Demiroglu, Mehmet Ozan Unal, et al.**  ·  `eess.IV`  ·  [abs](https://arxiv.org/abs/2611.08754) · [pdf](https://arxiv.org/pdf/2611.08754)  ·  relevance 23
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> No-reference image quality assessment (IQA) of low-dose CT predicts the score that radiologists would assign to a slice without a full-dose reference, as needed to compare dose protocols and denoisers. Trained CT IQA networks agree well with radiologists but output only a score, whereas multimodal large language models (MLLMs) can explain a score but perform poorly on CT when only prompted. We propose a measurement-aware MLLM, built on Qwen3.8-27B, that rates a slice from…

### 5. [Federated training performs as well as centralized for 3D Latent Diffusion for Diagnosis-Conditioned Brain MRI Synthesis](https://arxiv.org/abs/2611.08771)
**Abhijith Shaji, Paul Kurian, Greg Ver Steeg, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.08771) · [pdf](https://arxiv.org/pdf/2611.08771)  ·  relevance 22
<br>matched: `neuroimaging`, `brain mri`, `generative model`

> Generative models of brain MRI are useful to understand brain conditions, and to enrich scarce and imbalanced neuroimaging data. However, training these models requires large, multi-site training sets, which is challenging. Federated learning (FL) allows for training deep learning models without sharing data. We show that training a 3D conditional latent model federatedly (where data is kept private at each site) performs similarly to centralized training (where all the data…

### 6. [ROSE: Risk-Aware Orthogonal Subspace Navigation for Lifelong Knowledge Editing in Multimodal Large Language Models](https://arxiv.org/abs/2611.09770)
**Lingyun Song, Ziyao Chen, Kang Pan, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.09770) · [pdf](https://arxiv.org/pdf/2611.09770)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal Large Language Models (MLLMs) require continuous factual updates to stay current, yet lifelong knowledge editing remains a daunting challenge. The primary obstacle is the severe Locality Erosion and Catastrophic Forgetting, where sequential edits inevitably interfere with pre-trained capabilities and prior updates. In this paper, we propose \textbf{ROSE}, a \textbf{R}isk-aware \textbf{O}rthogonal \textbf{S}ubspace navigation framework for lifelong knowledge…

### 7. [DINO-Nucleus: Multi-Level Self-Supervised Features for Nucleus Instance Segmentation](https://arxiv.org/abs/2611.09133)
**Mohammad Sarhangzadeh, Elyar Esmaeilzadeh, Doruk Oner**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.09133) · [pdf](https://arxiv.org/pdf/2611.09133)  ·  relevance 20
<br>matched: `self-supervised`, `transformer`, `segmentation`

> Nucleus instance segmentation and counting are essential for quantitative microscopy, enabling reliable analysis of cell populations, tissue organization, and disease-related changes. However, accurately separating touching nuclei remains difficult, and many existing approaches rely on complex models or sensitive post-processing procedures. We present DINO-Nucleus, a parameter-efficient framework that leverages multi-level self-supervised DINOv2 representations for nucleus…

### 8. [Generative Reconstruction of Full-Field Sensor States for Safety-Critical Digital Twins](https://arxiv.org/abs/2611.08499)
**Umme Mahbuba Nabila, Linyu Lin, Majdi I. Radaideh**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.08499) · [pdf](https://arxiv.org/pdf/2611.08499)  ·  relevance 18
<br>matched: `graph neural network`, `graph neural`, `gnn`, `diffusion model`, `generative model`

> Accurate reconstruction of incomplete sensor fields is critical for state awareness in safety-critical digital twins (DTs). Thermocouples in high-temperature and radiation environments may drift, fail, or become intermittently unavailable, causing partial observability. This study develops a sparse-sensor reconstruction framework for Oregon State University's High Temperature Test Facility (HTTF) and evaluates six methods under intra- and inter-experiment protocols: three…

### 9. [StreamTab: Training-Free Temporal Link Prediction with Tabular Foundation Models](https://arxiv.org/abs/2611.09052)
**Mingqi Yang, Renqi Wu**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.09052) · [pdf](https://arxiv.org/pdf/2611.09052)  ·  relevance 18
<br>matched: `graph neural network`, `graph neural`, `foundation model`

> Temporal link prediction uses past interactions to predict whether two nodes will interact in the future. Temporal graph neural networks achieve strong results on this task, but they are trained separately for each graph. How a model should use interaction history also depends on the candidates it is compared with. A past interaction can distinguish a recurring link from a random pair that has never interacted, but when the negative candidates have also interacted before,…

### 10. [ELPAC: Endpoint-Anchored Latent Progression with Stage-Varying Multimodal Coordination](https://arxiv.org/abs/2611.08541)
**Shengxian Ding, Yifei Zhang, Xinyuan Tian, et al.**  ·  `stat.ML`  ·  [abs](https://arxiv.org/abs/2611.08541) · [pdf](https://arxiv.org/pdf/2611.08541)  ·  relevance 18
<br>matched: `alzheimer`, `interpretab`, `multimodal`

> Aging cohorts increasingly combine imaging, plasma, and cognitive measurements, but most subjects provide only a partially observed cross-sectional snapshot, leaving latent stage, progression subtype, and stage-varying multimodal coordination to be inferred jointly. Existing methods estimate the cohort-level aging process, model covariance under observed covariates, or fuse modalities for prediction. However, they rarely target the joint problem of endpoint-anchored staging…

### 11. [Authorization Drift in LLM Agents: Evaluating Boundary Compliance in Multi-Step Tool Use](https://arxiv.org/abs/2611.09113)
**Chuxue Cao, Jingru Zeng, Boqin Yin, et al.**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2611.09113) · [pdf](https://arxiv.org/pdf/2611.09113)  ·  relevance 18
<br>matched: `llm`, `agent`, `interpretab`

> LLM agents can exceed their authorization boundaries while pursuing user goals without an adversary. We formalize this phenomenon as authorization drift across data, tool, scope, and time, and introduce the Authorization Drift Benchmark (ADB): 648 samples across seven domains, each pairing a sufficient compliant path with an attractive unauthorized shortcut. To ensure executable tasks, tempting shortcuts, and feasible compliant paths, Staged Execution-Reflective Synthesis…

### 12. [Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation](https://arxiv.org/abs/2611.08718)
**Emilly Pitman de Castro, Vanessa Silva, Gustavo Kanno, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.08718) · [pdf](https://arxiv.org/pdf/2611.08718)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time. While large language models (LLMs) have improved semantic understanding, they are typically used as isolated components, without addressing how memory, retrieval, and decision-making should be integrated at the system level. In this work, we propose a memory-aware multi-agent architecture for conversational recommendation, in which…


<sub>Generated 2026-11-09 22:58 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-11](digests/2026-09-11.md) — 12 papers
- [2026-09-10](digests/2026-09-10.md) — 12 papers
- [2026-09-09](digests/2026-09-09.md) — 12 papers
- [2026-09-08](digests/2026-09-08.md) — 12 papers
- [2026-09-07](digests/2026-09-07.md) — 12 papers
- [2026-09-06](digests/2026-09-06.md) — 12 papers

_…and 72 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
