# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-11** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-11

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Predicting Time-to-conversion for Dementia of Alzheimer's Type using Multi-modal Deep Survival Analysis](https://arxiv.org/abs/2205.01188)
**Ghazal Mirabnahrazam, Da Ma, C\'edric Beaulac, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2205.01188) · [pdf](https://arxiv.org/pdf/2205.01188)  ·  relevance 49
<br>matched: `alzheimer`, `dementia`, `neuroimaging`, `disease progression`, `survival analysis`

> Dementia of Alzheimer's Type (DAT) is a complex disorder influenced by numerous factors, but it is unclear how each factor contributes to disease progression. An in-depth examination of these factors may yield an accurate estimate of time-to-conversion to DAT for patients at various disease stages. We used 401 subjects with 63 features from MRI, genetic, and CDC (Cognitive tests, Demographic, and CSF) data modalities in the Alzheimer's Disease Neuroimaging Initiative (ADNI)…

### 2. [Differential Diagnosis of Frontotemporal Dementia and Alzheimer's Disease using Generative Adversarial Network](https://arxiv.org/abs/2109.05627)
**Da Ma, Donghuan Lu, Karteek Popuri, et al.**  ·  `eess.IV`  ·  [abs](https://arxiv.org/abs/2109.05627) · [pdf](https://arxiv.org/pdf/2109.05627)  ·  relevance 33
<br>matched: `alzheimer`, `dementia`

> Frontotemporal dementia and Alzheimer's disease are two common forms of dementia and are easily misdiagnosed as each other due to their similar pattern of clinical symptoms. Differentiating between the two dementia types is crucial for determining disease-specific intervention and treatment. Recent development of Deep-learning-based approaches in the field of medical image computing are delivering some of the best performance for many binary classification tasks, although…

### 3. [TimeOmni-o1: Bidirectionally Coupling Time Series Foundation Models and LLMs for Multimodal Reasoning and Forecasting](https://arxiv.org/abs/2611.12902)
**Ziyang Zhang, Shenyi Li, Wen Wu, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.12902) · [pdf](https://arxiv.org/pdf/2611.12902)  ·  relevance 30
<br>matched: `foundation model`, `large language model`, `llm`, `multimodal`

> Time series from real-world systems are often accompanied by text, such as a report on an event that affects them. Two common tasks on these series are understanding, e.g., answering questions about a series, and forecasting its future values. Both tasks require reasoning over the series and the text together. Moreover, understanding outputs text while forecasting outputs a time series, so serving both requires a model that reads and generates both modalities. Large language…

### 4. [LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation](https://arxiv.org/abs/2611.14004)
**Zehui Wang, Wolfram H\"opken, Dietmar Jannach**  ·  `cs.IR`  ·  [abs](https://arxiv.org/abs/2611.14004) · [pdf](https://arxiv.org/pdf/2611.14004)  ·  relevance 27
<br>matched: `representation learning`, `large language model`, `llm`, `multimodal`

> As multimodal tourism-related information collected from heterogeneous data sources has become increasingly available, learning effective representations has attracted attention for improving recommendation performance. Existing approaches often tightly couple multimodal fusion with the architecture and optimization objective of a specific downstream model, which limits the generality and reusability of the learned representations. To address these limitations, we propose…

### 5. [CroCoMAE: Cross-modal self-supervised collaborative representation learning for SAR-optical remote sensing data](https://arxiv.org/abs/2611.14124)
**Vito Recchia, Giuseppe Guarino, C\'assio Fraga Dantas, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.14124) · [pdf](https://arxiv.org/pdf/2611.14124)  ·  relevance 26
<br>matched: `representation learning`, `self-supervised`, `segmentation`

> Remote sensing increasingly captures the Earth's surface through complementary sensors such as SAR and optical, yet ground-truth annotations remain scarce, limiting supervised approaches. Self-supervised learning (SSL) addresses the label scarcity, and cross-modal SSL further exploits the complementarity between co-located sensors, but existing cross-modal frameworks align modalities mostly through global image-level representations or treat them as largely redundant,…

### 6. [IC-GNN: Modeling Individualized Brain Community Organization for Disease Prediction](https://arxiv.org/abs/2611.13070)
**Yang Zhang, Xiao Zhou, Jonathan Warrell, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.13070) · [pdf](https://arxiv.org/pdf/2611.13070)  ·  relevance 25
<br>matched: `alzheimer`, `brain network`, `fmri`, `gnn`

> Brain networks exhibit modular organization, where community structures vary substantially across individuals and diseases. Understanding these individual differences is crucial for advancing both basic neuroscience research and precision medicine. However, widely used predefined group-level brain atlases often overlook this heterogeneity. While individualized functional parcellations capture subject-specific variability in community boundaries, they often require lengthy…

### 7. [Hierarchical Graph Representation Learning with Pooling-Induced Substructures](https://arxiv.org/abs/2611.14126)
**Luca Sbicego, Xiaowen Dong, Dorina Thanou**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.14126) · [pdf](https://arxiv.org/pdf/2611.14126)  ·  relevance 25
<br>matched: `graph neural network`, `graph neural`, `gnn`, `representation learning`

> Hierarchical graph-level tasks that require reasoning over substructures that extend beyond local neighborhoods are posing challenges for standard Graph Neural Networks (GNNs). While graph pooling aims to address this by coarsening graphs into hierarchical representations, existing methods often fail to explicitly preserve the substructures they induce, leading to inconsistent empirical performance. Moreover, evaluating such approaches remains challenging due to the lack of…

### 8. [Beyond Proxy Metrics: MLLMs as Human Surrogates for Explainable AI Evaluation](https://arxiv.org/abs/2611.13926)
**Eoin M. Kenny, Salim I. Amoukou, Tom Bewley**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.13926) · [pdf](https://arxiv.org/pdf/2611.13926)  ·  relevance 24
<br>matched: `large language model`, `llm`, `explainab`, `multimodal`

> Explainable AI (XAI) has expanded into a broad and impactful research area, but the fundamental question of how best to evaluate explanation techniques has proven frustratingly elusive. Methodologies typically revolve around either proxy metrics which tell us little about the utility of an explanation, or human evaluation which---while generally considered the gold standard---is expensive, difficult to scale, and challenging to reproduce. In this paper, we investigate if…

### 9. [Domain adaptation of a video Foundation model for Heart Failure Diagnosis from Echocardiography](https://arxiv.org/abs/2611.13297)
**Mahyar Bolhassani, Tijana Geroski, Narayana S. Singam, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.13297) · [pdf](https://arxiv.org/pdf/2611.13297)  ·  relevance 22
<br>matched: `foundation model`, `medical imaging`, `domain adaptation`

> The rapid advancement of foundation models has transformed computer vision, yet their adaptation to medical imaging, particularly purpose built foundation models for spatio temporal echocardiography videos, remains limited. In this work, we explore the feasibility of fine tuning a pretrained foundation model for video (TimeSformer) for automated diagnosis of reduced ejection fraction heart failure (HFrEF) from apical four chamber videos. The model is finetuned on the…

### 10. [Discovering Structurally Plausible and Interpretable Cognitive Models with Large Language Models](https://arxiv.org/abs/2611.13561)
**Boyoung Kwon, Jiyoon Seo, Sang Ho Lee**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.13561) · [pdf](https://arxiv.org/pdf/2611.13561)  ·  relevance 21
<br>matched: `large language model`, `llm`, `interpretab`

> Computational cognitive modeling has traditionally relied on manual model construction, which is a time-intensive process that requires substantial domain expertise. Although recent LLM-based approaches have begun to automate model generation, they often prioritize predictive accuracy at the expense of structural plausibility and parameter identifiability. We introduce DisCo, an LLM-guided framework that discovers interpretable symbolic cognitive models through evolutionary…

### 11. [Physics-Constrained Autoencoder for Interpretable Health Representation Learning in Turbofan Engines](https://arxiv.org/abs/2611.14266)
**Leonardo Baldo, Jokin Alcibar Ibarzabal, Daniel Cisneros Acevedo, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.14266) · [pdf](https://arxiv.org/pdf/2611.14266)  ·  relevance 21
<br>matched: `representation learning`, `interpretab`

> Health Indices (HIs) summarize degradation from operational data and support diagnostic and prognostic tasks in Prognostics and Health Management (PHM). Their usefulness depends on capturing degradation and interpreting system condition. Autoencoders learn such representations from unlabelled monitoring data; however, when training is driven only by reconstruction, the physical meaning of latent variables remains undefined, limiting their interpretation and diagnostic value.…

### 12. [VIGOR: Benchmarking Visual Rationale Correctness in Multimodal Large Language Models](https://arxiv.org/abs/2611.13150)
**Yanlin Chen, Tang Li, Xi Peng**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.13150) · [pdf](https://arxiv.org/pdf/2611.13150)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) are typically evaluated by whether they produce correct answers, but correctness alone does not reveal whether their outputs are supported by the right visual evidence. We introduce VIGOR, a benchmark for evaluating VIsually GrOunded Rationales in MLLMs. VIGOR represents visual rationales as explicit concepts paired with pixel-level groundings, covering multiple abstraction levels including low-level visual properties, intermediate…


<sub>Generated 2026-11-11 20:11 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-11](digests/2026-09-11.md) — 12 papers
- [2026-09-10](digests/2026-09-10.md) — 12 papers
- [2026-09-09](digests/2026-09-09.md) — 12 papers
- [2026-09-08](digests/2026-09-08.md) — 12 papers

_…and 74 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
