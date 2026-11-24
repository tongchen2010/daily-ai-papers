# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-24** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-24

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Spatiotemporal Graph Neural Networks for Fault Detection and Structural Learning in Chemical Processes: Use Case on the Tennessee Eastman Process](https://arxiv.org/abs/2611.27698)
**Rayane Ammar Khodja, Alexandre Voisin, Victor Costa, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.27698) · [pdf](https://arxiv.org/pdf/2611.27698)  ·  relevance 34
<br>matched: `graph neural network`, `graph neural`, `gnn`, `interpretab`

> Classical Fault Detection and Diagnosis (FDD) methods, including many data-driven approaches, assume a static normal operating space and interpret deviations from a fixed reference as fault indicators. When Operating Conditions (OCs) vary over time, this assumption breaks down: legitimate transitions trigger false alarms while moderate faults go undetected. We propose a spatiotemporal Graph Neural Network (GNN) framework that decomposes the normal operating space into…

### 2. [LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT](https://arxiv.org/abs/2611.27876)
**Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.27876) · [pdf](https://arxiv.org/pdf/2611.27876)  ·  relevance 21
<br>matched: `foundation model`, `longitudinal`, `llm`, `agent`

> Every few months, a cancer patient's CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides which findings are lesions, which are the same lesion months later and whether a new spot means progression, and checks each decision against the extensive rules of a clinical guideline. We introduce LesionAgent, an LLM agent that performs this…

### 3. [CanopyFormer: Attention-Guided SegFormer for Explainable Forest Cover Segmentation](https://arxiv.org/abs/2611.27674)
**Dhinanjaya Fernando, Dinura Ginige, Kalana Lakshan, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.27674) · [pdf](https://arxiv.org/pdf/2611.27674)  ·  relevance 20
<br>matched: `transformer`, `segmentation`, `interpretab`, `explainab`

> In transformer segmentation models, attention is usually visualized after training rather than supervised. Although attention supervision has been explored for natural images and driving scenes, aerial forest segmentation typically uses attention only as an architectural component and evaluates interpretability qualitatively. We present CanopyFormer, an attention-guided SegFormer-B0 that uses an Attention Consistency Loss to align attention with the ground-truth forest mask,…

### 4. [Decision Columns as an Index: Interpretable Embeddings for Explainable Entity Matching and Search](https://arxiv.org/abs/2611.27910)
**Aadharsh Kannan, Robert Bruckner, Philip A. Bernstein**  ·  `cs.IR`  ·  [abs](https://arxiv.org/abs/2611.27910) · [pdf](https://arxiv.org/pdf/2611.27910)  ·  relevance 20
<br>matched: `agent`, `interpretab`, `explainab`

> Business data systems must determine whether records refer to the same entity and retrieve records satisfying requests whose decisive properties are implicit. As agents act on these records, both tasks require auditable reasons. Dense embeddings perform well but offer opaque coordinates, cannot be filtered by meaning, and require corpus re-encoding to add new properties. We propose interpretable embeddings built from decision columns: each column stores a decision model's…

### 5. [UDA-Restoration: Bridging Unsupervised Domain Adaptation and Multi-Degradation Denoising for Enhanced AV Semantic Segmentation](https://arxiv.org/abs/2611.27097)
**Zainab Bibi, Mohsin Kamal**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.27097) · [pdf](https://arxiv.org/pdf/2611.27097)  ·  relevance 19
<br>matched: `self-supervised`, `segmentation`, `domain adaptation`

> Autonomous vehicles rely heavily on vision-based perception systems for safe navigation and decision-making. Adverse weather conditions, sensor noise, moving artifacts and illumination changes, however, often degrade the image quality and hence reduce perception performance. This paper introduces a diffusion-guided unsupervised domain adaptation algorithm for autonomous driving environments, namely UDA-Restoration, which is designed to enhance and denoise images. The…

### 6. [FM4SAR-Bench 1.0: Towards A Fair Benchmark for Evaluating Foundation Models for SAR Image Interpretation](https://arxiv.org/abs/2611.27158)
**Mingyao Chen, Yongxiang Liu, Tianpeng Liu, et al.**  ·  `eess.IV`  ·  [abs](https://arxiv.org/abs/2611.27158) · [pdf](https://arxiv.org/pdf/2611.27158)  ·  relevance 18
<br>matched: `foundation model`, `large language model`, `interpretab`, `multimodal`

> Foundation models have advanced SAR image interpretation but created a heterogeneous, fragmented model ecosystem. Existing models differ substantially in their input, training data, objectives, architectures, and release policy, yet the field lacks a unified taxonomy and comparative framework. Current evaluations rely primarily on task-specific benchmarks, which are ill-suited to fair comparison among models with fundamentally different input-output formats and task…

### 7. [ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization](https://arxiv.org/abs/2611.26782)
**Trupti Mohanty, Ming Du, Mitchell A. Wood, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.26782) · [pdf](https://arxiv.org/pdf/2611.26782)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Molecular dynamics (MD) simulation resolves atomic-scale motion and predicts the structural, mechanical, and dynamic properties of materials, making it cen- tral to materials design and discovery. Yet an MD study requires an expert-driven workflow: designing the simulation, writing reliable input scripts, executing them, and analyzing the results with separate tools. Here we present ChatAtom, a multi-agent large language model system that translates a natural-language…

### 8. [Beyond Final Answers: Interpretable Tumor Immune Microenvironment Reasoning from H&E and mIF](https://arxiv.org/abs/2611.26794)
**Yixuan Duan, Kexin Geng, Hanwen Xu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.26794) · [pdf](https://arxiv.org/pdf/2611.26794)  ·  relevance 18
<br>matched: `large language model`, `llm`, `interpretab`, `multimodal`

> Readouts of the tumor immune microenvironment (TIME), such as CD8+ T-cell density, intra-epithelial infiltration and the Ki67 index, combine tissue architecture from H&E with cell phenotypes from multiplex immunofluorescence (mIF). Multimodal large language models (MLLMs) could automate these readouts with an explanation, but two gaps remain. Pathology MLLMs read H&E alone, while these readouts need the cell phenotypes that mIF measures. And their reasoning has no step-level…

### 9. [DermKG: A Concept-Centric Knowledge Graph for Interpretable Skin Disease Diagnosis from Dermatological Morphology](https://arxiv.org/abs/2611.27283)
**Cheng Huang, Yanmei Li, Mao Lin**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.27283) · [pdf](https://arxiv.org/pdf/2611.27283)  ·  relevance 18
<br>matched: `graph neural network`, `graph neural`, `interpretab`

> Dermatologists describe lesions with a standardized morphological lexicon, which makes concept-based models attractive for interpretable skin disease diagnosis. How much diagnostic information these concepts actually carry, however, is rarely quantified. We present DermKG, a concept-centric knowledge graph built on the expert-annotated SkinCon subset of Fitzpatrick17k (3,230 images, 48 concepts, 113 diseases). DermKG has 3,452 nodes of 8 types and 19,365 edges of 11 relation…

### 10. [Neurodegenerative Differential Diagnosis with Knowledge-enhanced Structural Reasoning](https://arxiv.org/abs/2611.27427)
**Mingxuan Wang, Siyuan Du, Yanfeng Wang, et al.**  ·  `cs.CE`  ·  [abs](https://arxiv.org/abs/2611.27427) · [pdf](https://arxiv.org/pdf/2611.27427)  ·  relevance 18
<br>matched: `neurodegenerative`, `multimodal`

> Accurate differential diagnosis of neurodegenerative disorders remains challenging due to overlapping clinical manifestations and heterogeneous, often incomplete multimodal observations. Existing multimodal models can integrate imaging and clinical measurements but often overlook disease-specific evidence patterns and pairwise relations among competing diagnoses. We therefore propose Knowledge-enhanced Structural Reasoning (KnowSR), which aligns multimodal patient…

### 11. [Bringing AI Assistance to the Beznau Nuclear Power Plant: A Hierarchical System of LLM Agents for Reactor Monitoring](https://arxiv.org/abs/2611.27556)
**Wenqi Zhou, Leonardo Baldo, Edwin Kolbe, et al.**  ·  `cs.MA`  ·  [abs](https://arxiv.org/abs/2611.27556) · [pdf](https://arxiv.org/pdf/2611.27556)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Beznau Unit 1 in Switzerland, in operation since 1969, is the most experienced nuclear reactor still running worldwide. Five decades of incremental modernization have left its monitoring systems, alarm logs, variable catalogs, technical specifications and investigation reports in separate silos that were never designed to be queried together. As a result, investigating a core instrumentation anomaly means slow, manual gathering of knowledge scattered across databases,…

### 12. [Interpretable Tissue Architecture Complements Pathology Foundation Models](https://arxiv.org/abs/2611.27881)
**Zeeshan Shahid, Hammam M. AlGhamdi**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.27881) · [pdf](https://arxiv.org/pdf/2611.27881)  ·  relevance 18
<br>matched: `foundation model`, `interpretab`

> Tissue architecture provides important information for histopathological assessment, yet its complementary predictive value alongside pathology foundation-model representations remains insufficiently understood. This study investigates whether interpretable measurements of cellular and multicellular tissue organization provide additional predictive information beyond learned representations. We introduce a 139-dimensional cellular-to-community representation comprising nine…


<sub>Generated 2026-11-24 00:50 UTC via the arXiv API.</sub>

---

## Archive

- [2026-11-24](digests/2026-11-24.md) — 12 papers
- [2026-11-22](digests/2026-11-22.md) — 12 papers
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

_…and 86 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
