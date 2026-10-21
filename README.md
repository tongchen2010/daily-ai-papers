# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-21** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-21

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Brain2Vec: A Self-Supervised 3D Foundation Model for Structural Brain MRI](https://arxiv.org/abs/2610.28411)
**Spiros Maggioros, Guray Erus, Gareth Harman, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.28411) · [pdf](https://arxiv.org/pdf/2610.28411)  ·  relevance 45
<br>matched: `neuroimaging`, `brain mri`, `self-supervised`, `foundation model`, `medical imaging`

> Deep learning models have become essential tools in medical imaging, yet training them end-to-end for diverse tasks remains challenging due to limited labeled data and computational constraints. To address this, we introduce Brain2Vec, a foundation model pre-trained on 74,425 T1-weighted Magnetic Resonance Imaging (MRI) scans pooled from multiple studies. Brain2Vec can serve both as a weight initialization backbone for fine-tuning downstream tasks and as a standalone feature…

### 2. [Convergent Performance, Divergent Mechanisms in LoRA-Adapted Vision Foundation Models for Brain MRI](https://arxiv.org/abs/2610.28255)
**Cecilia Diana-Albelda, Fiona Kekwick, Raghav Mehta, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.28255) · [pdf](https://arxiv.org/pdf/2610.28255)  ·  relevance 36
<br>matched: `alzheimer`, `brain mri`, `foundation model`, `medical imaging`, `segmentation`

> Adapting Vision Foundation Models (VFMs) to medical imaging via LoRA has become standard practice, yet model selection is guided almost entirely by downstream task metrics, treating backbones with similar performance as interchangeable. We investigate whether equal performance implies equal internal representational shift. We analyse four ViT-B/16 backbones, DINOv3, SigLIP2, MerMED-FM, and BiomedCLIP, pre-trained with different objectives (self-distillation vs. contrastive…

### 3. [Contrastive Adversarial Training for Robust Graph Neural Networks under Label Poisoning](https://arxiv.org/abs/2610.24685)
**Manshika Charvi Bissessur, Melis Ilayda Bal, Michael Muehlebach**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.24685) · [pdf](https://arxiv.org/pdf/2610.24685)  ·  relevance 35
<br>matched: `graph neural network`, `graph neural`, `gnn`, `representation learning`

> Graph Neural Networks (GNNs) are effective for modeling relational data but are vulnerable to label poisoning, where a small number of corrupted training labels can propagate errors across the graph via message passing. Despite this risk, defenses against label poisoning remain underexplored: existing methods are primarily designed for label noise and often rely on robust losses or heuristic data cleaning that fail to distinguish adversarial poisoning from naturally hard…

### 4. [HypTI: Hyperbolic Geometry-Aware Multimodal Feature Fusion Framework for Dementia Detection Based on Tabular-Image Data](https://arxiv.org/abs/2610.27941)
**Jianfei Xu, Huizhi Liang, Judith Harrison, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.27941) · [pdf](https://arxiv.org/pdf/2610.27941)  ·  relevance 33
<br>matched: `dementia`, `neuroimaging`, `representation learning`, `multimodal`

> AI-assisted dementia detection usually requires multimodal fusion of diverse data, such as clinical tabular assessments and neuroimaging data. However, most existing approaches perform feature fusion in Euclidean space. This overlooks the geometric structure of representation, including hierarchical organization in clinical assessments and multi-scale anatomical patterns in neuroimaging data. Recent studies have proved hyperbolic space provides a natural geometry for…

### 5. [RAFT: Redundancy-Aware Input Filtering for Temporal Graph Neural Network Training](https://arxiv.org/abs/2610.24875)
**Yue Dai, Sarah Zhou, Youtao Zhang**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.24875) · [pdf](https://arxiv.org/pdf/2610.24875)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Temporal graph neural networks (TGNNs) have shown strong performance on dynamic graph learning tasks by continuously updating node memories from evolving interactions (i.e., events) and leveraging these memories for downstream predictions. As graphs grow rapidly in modern applications, training requires processing an increasing number of events; meanwhile, each event can update node memories used by later events, creating dependencies that constrain parallel execution and…

### 6. [Declarative Explanations for Graph Neural Networks: A Demonstration](https://arxiv.org/abs/2610.26104)
**Cibo Yu, Haitong Tang, Yinghui Wu, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.26104) · [pdf](https://arxiv.org/pdf/2610.26104)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Graph Neural Networks (GNNs) have proven effective for graph analytical tasks, yet their "black-box" nature complicates the understanding of their layer-wise behavior and hinders their application to large graphs. We demonstrate SliceGXQ, an end-to-end declarative and interactive system for querying and exploring layer-wise explanations for GNNs over large-scale graphs. In particular, SliceGXQ provides (1) an interactive graphical user interface for dataset, model, and…

### 7. [Learning SOCP Solver Dynamics with Graph Neural Networks](https://arxiv.org/abs/2610.26285)
**Adam Ghalem, Lou Sala\"un, Davide Rinaldi, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.26285) · [pdf](https://arxiv.org/pdf/2610.26285)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Second-order cone programs (SOCPs) are a fundamental class of convex optimization problems widely applied across engineering domains. Classical interior-point methods are robust and accurate, but their iterative nature can be costly in real-time or repeated-solve settings. This has motivated learning-based solvers that approximate optimizer solutions with neural networks. Recent work has increasingly studied graph neural networks (GNNs) for linear, quadratic, and…

### 8. [Rate as a Feature, Not a Nuisance: Curriculum FiLM Training for Event-Based Graph Neural Networks](https://arxiv.org/abs/2610.26933)
**Kavyansh Tyagi, Andreas Ziegler**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.26933) · [pdf](https://arxiv.org/pdf/2610.26933)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> An event camera emits events at a rate given by the scene motion, object texture, illumination, its own contrast thresholds, and other settings. Across the N-Caltech101 dataset, recorded by a single event camera, the event rate varies by roughly 26x. Standard event-based Graph Neural Network GNN pipelines do not make use of the variable event rate. They either normalize each event's timestamp into a fixed window or train the network to be invariant to the event rate. We…

### 9. [Cross-disorder Learning of Imaging-derived Joint Mophometric Markers in Alzheimer's and Parkinson's Diseases](https://arxiv.org/abs/2610.27150)
**Yuji Zhao, Boris Gutman**  ·  `q-bio.QM`  ·  [abs](https://arxiv.org/abs/2610.27150) · [pdf](https://arxiv.org/pdf/2610.27150)  ·  relevance 31
<br>matched: `alzheimer`, `neurodegenerative`, `neuroimaging`, `interpretab`

> As two most prevalent neurodegenerative diseases (NDDs), Alzheimer's disease (AD) and Parkinson's disease (PD) shared commonalities both in symptomology and pathophysiology. However, to what extent and in what way these two distinct disorders overlap remain underexplored. In this study, we propose an explicit, interpretable and spatially adaptive transfer learning framework to elucidate the morphometric biomarkers linked to AD and PD. We applied such high-dimensional machine…

### 10. [AnchorRM: Parallel Intra-Batch State Reconstruction with Anchor-Based Residual Memory for Temporal Graph Neural Networks](https://arxiv.org/abs/2610.27558)
**Haroon Gharwi, Kai Shu, Yue Dai**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.27558) · [pdf](https://arxiv.org/pdf/2610.27558)  ·  relevance 27
<br>matched: `graph neural network`, `graph neural`

> Memory-based temporal graph neural networks (TGN) rely on recurrent node memories to capture evolving interaction histories. However, temporal mini-batching introduces a trade-off between computational efficiency and temporal fidelity: when a node appears multiple times within the same batch, later interactions are evaluated using stale pre-batch memory because the intermediate memory updates have not yet been committed. This problem becomes more severe as temporal batch…

### 11. [PI-MLLM: Psychophysics-Inspired Multimodal Large Language Model for Oddly Satisfying Video Emotion Analysis](https://arxiv.org/abs/2610.28264)
**Yuheng Zhang, Jie Zhang, Yuecong Min, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.28264) · [pdf](https://arxiv.org/pdf/2610.28264)  ·  relevance 27
<br>matched: `large language model`, `llm`, `multimodal`

> Oddly Satisfying Videos (OSVs) can evoke strong viewer responses through repetitive motion, visual tactility, and ASMR-like sounds despite containing few explicit semantic emotion cues. This makes OSVs a challenging setting for Video Emotion Analysis (VEA), since most existing methods focus on semantic video content and under-model the physical sensory dynamics that shape viewer responses. To support Oddly Satisfying Video Emotion Analysis (OSVEA), we construct the Oddly…

### 12. [Uncovering Semantic Hierarchies in Text-Attributed Graphs via Variational EM-based LLM-GNN Synergy](https://arxiv.org/abs/2610.24624)
**Yunhui Liu, Xudong Jin, Qizhuo Xie, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.24624) · [pdf](https://arxiv.org/pdf/2610.24624)  ·  relevance 25
<br>matched: `gnn`, `representation learning`, `llm`

> While hierarchical structures are intrinsic to organizing human knowledge, current representation learning on text-attributed graphs predominantly operates on flat semantic spaces, overlooking the rich coarse-to-fine granularity inherent in real-world data. To bridge this gap, we propose SHiFT, which synergizes the reasoning power of LLMs with the structural representation capability of GNNs within an Expectation-Maximization (EM) paradigm. In the E-step, we harness LLMs as…


<sub>Generated 2026-10-21 18:02 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-18](digests/2026-08-18.md) — 12 papers

_…and 53 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
