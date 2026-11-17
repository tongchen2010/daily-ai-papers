# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-17** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-17

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [One Question, Four Voices: How Advice for Alzheimer's Caregiving Differs Between Caregivers, Clinicians, and Large Language Models](https://arxiv.org/abs/2611.18604)
**Congning Ni, Jinkyung Katie Park, Yang Li, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.18604) · [pdf](https://arxiv.org/pdf/2611.18604)  ·  relevance 38
<br>matched: `alzheimer`, `dementia`, `large language model`, `llm`, `retrieval-augmented`

> Online caregiver forums are an important source of emotional and informational support for Alzheimer's disease and related dementias (ADRD). We compare responses to 85 real caregiver questions from ALZConnected across four responder groups: peer caregivers, physicians, ChatGPT, and a retrieval-augmented CareGPT grounded in peer discussions. Using 28 measures spanning linguistic form, emotional support, informational support, and topic scope, we examine how these voices…

### 2. [GraphPass: A Study of Graph Neural Networks for Compiler Pass Selection](https://arxiv.org/abs/2611.19821)
**Mohammed Saqlain**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.19821) · [pdf](https://arxiv.org/pdf/2611.19821)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Compiler pass selection is usually governed by fixed pipelines (-O2, -O3) or hand-written heuristics. We study whether a graph neural network (GNN) over a program's control-flow graph (CFG) can select among a fixed menu of five pass sequences in a single forward pass. GraphPass encodes each CFG with a graph attention (GAT) or graph convolutional (GCN) encoder and classifies it into one of the five sequences. On a synthetic benchmark of 5,000 generated CFGs in five program…

### 3. [Improving fine-grained expressivity of graph neural networks](https://arxiv.org/abs/2611.20020)
**Yonatan Sverdlov**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.20020) · [pdf](https://arxiv.org/pdf/2611.20020)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> This thesis investigates the expressive power of neural networks for structured data, focusing on graph neural networks and symmetry-aware architectures. We present four main contributions. First, we characterize the generic expressive power of geometric message-passing neural networks on sparse graphs and introduce EGenNet, an architecture achieving the corresponding guarantees. Second, we use representation theory to characterize linear layers equivariant to multiple…

### 4. [Open-fMIND: A Large-Scale Open-Access fMRI Corpus for Pretraining Brain Foundation Models](https://arxiv.org/abs/2611.21215)
**Carlo Alberto Barbano, Giovanni Marraffini, Demian Wassermann**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.21215) · [pdf](https://arxiv.org/pdf/2611.21215)  ·  relevance 29
<br>matched: `functional mri`, `fmri`, `representation learning`, `self-supervised`, `foundation model`

> Self-supervised pretraining has transformed language and vision, but its application to functional MRI (fMRI) is constrained by data access. The largest standardized fMRI resources are governed by data use agreements and dominated by a small number of acquisition protocols, while the thousands of openly licensed datasets on OpenNeuro are individually small, heterogeneously organized, and unprocessed. We present the first release of Open-fMIND, a uniformly preprocessed,…

### 5. [LogicEye: Agent Driven Multimodal Dataset for Interpretable Ophthalmic Diagnosis](https://arxiv.org/abs/2611.18669)
**Jiajie Mu, Lu Chen, Zheyun Qin, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.18669) · [pdf](https://arxiv.org/pdf/2611.18669)  ·  relevance 27
<br>matched: `large language model`, `agent`, `interpretab`, `multimodal`

> Clinical adoption of ophthalmic Artificial Intelligence remains limited by low interpretability and a lack of finely annotated multimodal data. Most existing datasets provide only coarse disease labels without the granular pathological findings required for differential diagnosis. We present LogicEye$^{Agent}$, a dual-pool inference and verification agent that emulates clinical reasoning by jointly verifying positive inclusion signs and negative exclusion criteria. Using…

### 6. [Brain AI Scientist: An Evidence-Based Multi-Agent System for Translational Neuroimaging in Precision Psychiatry](https://arxiv.org/abs/2611.18634)
**Zeyun Zhao, Lin Gu, Ruogu Fang**  ·  `q-bio.QM`  ·  [abs](https://arxiv.org/abs/2611.18634) · [pdf](https://arxiv.org/pdf/2611.18634)  ·  relevance 24
<br>matched: `neuroimaging`, `fmri`, `agent`

> Resting-state functional magnetic resonance imaging (rs-fMRI) has revealed widespread brain-network alterations in psychiatric disorders, yet translating these findings into individualized clinical decision support remains challenging. Here we introduce Brain AI Scientist, an autonomous multi-agent framework that integrates patient-specific fMRI, clinical information, and scientific evidence through retrieval, verification, and prioritization. Guided by Research Domain…

### 7. [FRAAC: A French Multimodal Large Language Model and Dataset forPictogram-Based Augmentative and Alternative Communication](https://arxiv.org/abs/2611.20094)
**Alexandre Audibert, Fran\c{c}ois Portet, Benoit Favre, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.20094) · [pdf](https://arxiv.org/pdf/2611.20094)  ·  relevance 24
<br>matched: `large language model`, `llm`, `retrieval-augmented`, `multimodal`

> Pictograms are a core modality in augmentative and alternative communication (AAC), yet recent multimodal large language models (MLLMs) cannot reliably interpret or produce pictogram sequences. Two obstacles explain this gap: the absence of a standardized pictogram grammar and the scarcity of parallel text-pictogram data. We introduce Retrieval-Augmented Pictogram Selection (RAPS), an annotation method that refines a rule-based transcription system's output with LLM-based…

### 8. [Multimodal AI in Healthcare: Review of Vision-Language Foundation Models for Real-World Medical Applications](https://arxiv.org/abs/2611.19958)
**Taha Razzaq, Murtaza Taj, Asim Iqbal**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.19958) · [pdf](https://arxiv.org/pdf/2611.19958)  ·  relevance 24
<br>matched: `foundation model`, `large language model`, `llm`, `multimodal`

> The emergence of foundation models has marked a transformative shift in AI, enabling robust generalization across diverse downstream tasks through putative zero-shot learning. Large Language Models and Vision Language Models have demonstrated strong capabilities in tasks such as image interpretation, report generation, and question answering by effectively learning from multimodal data-images paired with associated text often with minimal supervision. In the healthcare…

### 9. [How Much Do Foundation Models Add to Gradient Boosting on Financial Event Sequences?](https://arxiv.org/abs/2611.18914)
**Carlos Eduardo Martins Relvas, Gustavo di Giovanni Bernardo**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.18914) · [pdf](https://arxiv.org/pdf/2611.18914)  ·  relevance 22
<br>matched: `graph neural network`, `graph neural`, `self-supervised`, `foundation model`

> Foundation models pretrained on raw transaction sequences are proposed for credit, fraud and churn modeling, with reported gains over gradient boosting, but the data and baselines behind these gains are rarely public. We measure how much the pretraining and adaptation recipes of these models add to a baseline of point-in-time window aggregates and LightGBM, and we propose TBS (Temporal Boosting-Sequence ensemble), which averages the ranks of a boosting model enriched with…

### 10. [Weights & Caches: LLMs Can Program Tabular Foundation Models](https://arxiv.org/abs/2611.20174)
**Shi Bin Hoo, Magnus Buehler, Omar Swelam, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.20174) · [pdf](https://arxiv.org/pdf/2611.20174)  ·  relevance 21
<br>matched: `foundation model`, `large language model`, `llm`

> Neural networks are typically programmed through optimization, rather than by explicitly specifying their computations. Recent work on weight-space programming suggests that large language models (LLMs) can instead reason about and manipulate neural-network weights directly. In this work, we show that LLMs can directly program statistical computations in tabular foundation models (TFMs), whose parameters enable inference across different datasets. We investigate three…

### 11. [Macro Control and Capability Evaluation of Black-Box World Models: A Two-Regime Framework for LLM-Agent Markets](https://arxiv.org/abs/2611.19311)
**Zhiyang Niu, Chuanjie Li, Huayuan Shen, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.19311) · [pdf](https://arxiv.org/pdf/2611.19311)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `interpretab`

> Large language model (LLM) agents can be organized into multi-agent markets that act as world models, mapping macro information to emergent macro dynamics while the evaluator observes only macro inputs and outputs. This paper separates a model's capability into two stages that a single aggregate score cannot separate: information simulation, from macro information to micro behavior, and macro emergence, from micro behavior to the macro outcome. We introduce a soft…

### 12. [Multimodal Fusion: A Review of Breast Cancer Advanced and Traditional Modalities](https://arxiv.org/abs/2611.18793)
**Jawaher Al-Tuweity, Jo\~ao Paulo Papa**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.18793) · [pdf](https://arxiv.org/pdf/2611.18793)  ·  relevance 21
<br>matched: `medical imaging`, `segmentation`, `interpretab`, `explainab`, `multimodal`

> Purpose: Multimodal medical imaging fusion (MMIF) is an increasingly important approach to breast cancer detection (BCD), as different imaging modalities rely on different physical principles and provide complementary information. No single modality can capture all the structural, functional, and biological information needed for accurate diagnosis and characterization. Methods: This review examines more than 15 imaging modalities used in breast cancer detection, including…


<sub>Generated 2026-11-17 21:45 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-18](digests/2026-09-18.md) — 12 papers
- [2026-09-17](digests/2026-09-17.md) — 12 papers
- [2026-09-16](digests/2026-09-16.md) — 12 papers
- [2026-09-15](digests/2026-09-15.md) — 12 papers

_…and 80 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
