# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-15** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-15

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Towards Training and Inference of Graph Neural Networks in Graph Databases](https://arxiv.org/abs/2610.19142)
**Victor Pekkari, Harry Wik, Alfred Clemedtson, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.19142) · [pdf](https://arxiv.org/pdf/2610.19142)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Graph Neural Networks on large graphs commonly rely on in-memory graph storage with ad hoc data processing pipelines for both training and inference. Graph databases provide scalable storage and efficient traversal for graphs that can evolve over time, but their applicability in GNN training and inference are rarely studied. We show that graph DBs can be used in GNN training and inference directly, executing sampling, feature retrieval, and even the full forward pass. We…

### 2. [Simulating Alzheimer's amyloid-like pathology on a fly central nervous system connectome](https://arxiv.org/abs/2610.19153)
**Taeho Jo**  ·  `q-bio.NC`  ·  [abs](https://arxiv.org/abs/2610.19153) · [pdf](https://arxiv.org/pdf/2610.19153)  ·  relevance 30
<br>matched: `alzheimer`, `connectome`

> In Alzheimer's disease, the amount of pathology in the brain is an imperfect predictor of how much function is lost. Pathology leads to that loss through neural circuits, but these cannot be observed neuron by neuron in patients. This study therefore simulated the central nervous system of the adult male Drosophila melanogaster: 166,700 integrate-and-fire neurons wired by the MaleCNS connectome. The simulator reproduced a published fly brain model (rate correlation 0.9997).…

### 3. [FireGraphNet: Sub-daily wildfire spread prediction with directed graph neural networks](https://arxiv.org/abs/2610.19191)
**Aiyshwariya Paulvannan Kanmani, Miguel Esparza, Ali Mostafavi**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.19191) · [pdf](https://arxiv.org/pdf/2610.19191)  ·  relevance 27
<br>matched: `graph neural network`, `graph neural`

> Wildfire decisions are made in hours, yet most learned spread models predict daily on targets including burned area. We propose FireGraphNet which formulates 12-hour growth as node classification on directed H3 graphs, with candidates ahead of the front and wind alignment, terrain, fuel continuity and barriers on edges. On satellite perimeters it achieves average precision 1.7-1.9x the strongest distance baseline on test California fires and 1.62x out of state. We show this…

### 4. [HGRP: Heterogeneous Graph Neural Network for Routability Prediction](https://arxiv.org/abs/2610.20209)
**Yule Sheng, Yue Yuan, Shan Shen, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.20209) · [pdf](https://arxiv.org/pdf/2610.20209)  ·  relevance 27
<br>matched: `graph neural network`, `graph neural`

> Routability prediction enables rapid evaluation of placement quality without routing, providing effective feedback for routability-driven placement optimization. Recent machine learning methods have achieved efficient routability prediction through data-driven approach. However, their prediction performance highly depends on the capability of input representations to capture essential circuit information. To address the limitations of existing circuit representations in…

### 5. [Toward System One Clinical Intelligence: Parameter-Efficient Fine-Tuning and Counterfactual Explainability of Decision Foundation Models](https://arxiv.org/abs/2610.15029)
**S. M. Mahbub Uddin Ahmed**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.15029) · [pdf](https://arxiv.org/pdf/2610.15029)  ·  relevance 27
<br>matched: `foundation model`, `large language model`, `llm`, `interpretab`, `explainab`

> Automated disease classification from patient-reported symptoms requires balancing the speed of lightweight discriminative models against the contextual understanding and latency costs of autoregressive large language models (LLMs). Decision foundation models offer an alternative by mapping representations directly to candidate classes without free-form text generation. We adapt Clef-Flash, a 9-billion-parameter decision model built on a Qwen3.5 backbone, for 24-class…

### 6. [Quantifying privacy risks in foundation model representations of brain MRI](https://arxiv.org/abs/2610.20494)
**Imen Bajar, H\'eber Hwang Arcolezi, Antoine Boutet, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.20494) · [pdf](https://arxiv.org/pdf/2610.20494)  ·  relevance 27
<br>matched: `brain mri`, `foundation model`, `longitudinal`

> Pretrained representations are increasingly used to share and reuse information from medical images without exposing the original scans, but it is unclear how much patient-specific information these representations retain. We investigate this question for brain magnetic resonance imaging (MRI) by evaluating five frozen pretrained encoders spanning different architectures, pretraining objectives, and training domains on two longitudinal T1-weighted datasets, OASIS-2 and…

### 7. [Benchmarking Self-Supervised 3D Medical Vision Foundation Models and Transferability Estimation](https://arxiv.org/abs/2610.17573)
**Jiaqi Tang, Yu Wang, Yang Liu, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.17573) · [pdf](https://arxiv.org/pdf/2610.17573)  ·  relevance 25
<br>matched: `self-supervised`, `foundation model`, `transformer`, `segmentation`

> Self-supervised pretraining has expanded the pool of 3D medical foundation models, but published evaluations use different datasets, endpoints and fine-tuning protocols. Models also differ in architecture, pretraining objective and data, while downstream targets range from voxel-level masks to patient-level diagnoses and outcomes. As a result, published findings provide little directly comparable evidence for choosing a model for a new task. Direct comparison of adaptation…

### 8. [SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation](https://arxiv.org/abs/2610.15766)
**Angen Ye, junjie xie, Yujia Song, et al.**  ·  `cs.RO`  ·  [abs](https://arxiv.org/abs/2610.15766) · [pdf](https://arxiv.org/pdf/2610.15766)  ·  relevance 24
<br>matched: `large language model`, `llm`, `agent`, `interpretab`, `multimodal`

> Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning. In surgical robotics, however, end-to-end prediction of low-level actions remains limited by insufficient precision, opaque decisions, and scarce data. This paper presents SurgiCLAW, a hierarchical skill-based framework for precision surgical manipulation. SurgiCLAW confines an MLLM to intraoperative…

### 9. [MemeTrace: A Multimodal LLM-Based Agent for Safety-Aware Meme Provenance Analysis](https://arxiv.org/abs/2610.19267)
**Bo Shao, Yihan Ma, Yiting Qu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.19267) · [pdf](https://arxiv.org/pdf/2610.19267)  ·  relevance 24
<br>matched: `llm`, `agent`, `multimodal`

> Online memes are often carriers of unsafe content such as disinformation and propaganda. Their rapid evolution in response to news events and strong dependence on contextual information make it difficult for platforms and moderators to detect and moderate them effectively. Moreover, existing moderation studies typically classify memes as safe or unsafe based on individual images, lacking the ability to perform broader provenance analysis, i.e., where a meme originates, how…

### 10. [Towards a Data-Centric Understanding of Spatial Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2610.19108)
**Mahdieh Mallahnezhad, Masoud Jafaripour, Mohamadali Tofigh, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.19108) · [pdf](https://arxiv.org/pdf/2610.19108)  ·  relevance 23
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Multimodal Large Language Models (MLLMs) have been widely applied in embodied agents and robotics for vision tasks. However, MLLMs suffer from limitations in spatial reasoning and perception. Post-training techniques have shown promise for improving these capabilities; yet, there are limited data-driven surveys of such approaches. In this survey, we consider approaches to fine-tuning pretrained MLLMs for spatial reasoning tasks, ranging from supervised to reinforcement…

### 11. [DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning](https://arxiv.org/abs/2610.16822)
**Yuxiang Zeng, Kun Xie, Yang Wang, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.16822) · [pdf](https://arxiv.org/pdf/2610.16822)  ·  relevance 22
<br>matched: `gnn`, `representation learning`, `transformer`

> Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves…

### 12. [On the Limits of Representation-Based Test-Time Adaptation for Multimodal LLMs](https://arxiv.org/abs/2610.19892)
**Miko{\l}aj Pi\'orczy\'nski, Wojciech Masarczyk, Damian S\'ojka, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.19892) · [pdf](https://arxiv.org/pdf/2610.19892)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Vision-language models suffer significant accuracy drops under common corruptions. While test-time adaptation (TTA) successfully mitigates these shifts in CLIP-like contrastive models, its application to generative multimodal large language models (MLLMs) remains underexplored and uniquely challenging due to their sequential token generation. In this work, we demonstrate that representation-based TTA fails to recover performance in MLLMs. Our experiments reveal that even…


<sub>Generated 2026-10-15 17:46 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-18](digests/2026-08-18.md) — 12 papers
- [2026-08-17](digests/2026-08-17.md) — 12 papers
- [2026-08-16](digests/2026-08-16.md) — 12 papers
- [2026-08-15](digests/2026-08-15.md) — 12 papers
- [2026-08-14](digests/2026-08-14.md) — 12 papers
- [2026-08-12](digests/2026-08-12.md) — 12 papers
- [2026-08-11](digests/2026-08-11.md) — 12 papers

_…and 47 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
