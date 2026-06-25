# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-06-25** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-06-25

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Auto-Configured Explainable Graph Neural Networks for Multi-Site Pollution Prediction](https://arxiv.org/abs/2606.24978)
**Abdelkader Dairi, Fouzi Harrou, Ying Sun**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2606.24978) · [pdf](https://arxiv.org/pdf/2606.24978)  ·  relevance 40
<br>matched: `graph neural network`, `graph neural`, `gnn`, `explainab`

> Accurate particulate matter (PM) prediction is crucial for mitigating air pollution. Graph Neural Networks (GNNs) effectively model spatiotemporal dependencies, but predefined graphs limit adaptability, and some datasets complicate learning. This study introduces a graph construction method based on a confusion matrix from a supervised learning process to dynamically capture inter-class relationships. Additionally, a hybrid loss function that combines energy distance and…

### 2. [Neural operator-based digital twins for modeling amyloid-$\beta$ and tau propagation and treatment optimization in Alzheimer's disease](https://arxiv.org/abs/2606.25185)
**Xiaofeng Xu, Tingting Dan, Zifan Zhou, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2606.25185) · [pdf](https://arxiv.org/pdf/2606.25185)  ·  relevance 38
<br>matched: `alzheimer`, `neurodegenerative`, `cortical`, `disease progression`, `longitudinal`, `interpretab`

> Accurately predicting the spatiotemporal evolution of amyloid-$\beta$ and tau proteins at the individual level is critical for improving the diagnosis and treatment of Alzheimer's disease. We consider the problem of constructing patient-specific digital twins that model the propagation of these biomarkers on the cortical surface using reaction--diffusion dynamics. A major challenge is that the underlying nonlinear aggregation mechanisms are unknown and must be inferred from…

### 3. [Convex--Concave Quadratic Spectral Filtering for Graph Neural Networks](https://arxiv.org/abs/2606.24956)
**Ranhui Yan, Jia Cai, Mengzhu Chen, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2606.24956) · [pdf](https://arxiv.org/pdf/2606.24956)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Spectral graph neural networks (GNNs) interpret message passing as frequency-selective filtering. While low-order spectral filters are efficient, their limited selectivity often leads to weak attenuation outside the passband, whereas high-order alternatives introduce optimization challenges. We propose DCQ-GNN, a spectral GNN based on a compact bank of adaptive convex--concave quadratic filters. By restricting the filter order to two while explicitly exploiting complementary…

### 4. [Leaking Circuit Secrets: Gradient Leakage Attacks on Graph Neural Networks](https://arxiv.org/abs/2606.25589)
**Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2606.25589) · [pdf](https://arxiv.org/pdf/2606.25589)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> As graph neural networks (GNNs) become standard tools for critical tasks in circuit design and analysis, their security and privacy risks require careful attention. Here, we present the first comprehensive evaluation of gradient leakage attacks (GLAs) on GNNs in circuit-design and hardware-security tasks, a practical threat that has been largely overlooked. We assess state-of-the-art (SOTA) GNNs, including GraphSAGE, GCN, GIN, and GAT, trained on standard netlist benchmarks…

### 5. [Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface](https://arxiv.org/abs/2606.25941)
**Faliang Yin, Hak-Keung Lam, David Watson**  ·  `cs.HC`  ·  [abs](https://arxiv.org/abs/2606.25941) · [pdf](https://arxiv.org/pdf/2606.25941)  ·  relevance 27
<br>matched: `large language model`, `llm`, `agent`, `explainab`

> Increasing demand for precise and reliable control in complex scenarios has led to the development of increasingly sophisticated controllers, including data-driven approaches employing closed box models and mathematically rigorous yet complex designs. This complexity highlights the needs for explainable control that can provide human-understandable insights into controller behavior. In this paper, an explainable control framework (XCF) along with supporting algorithms and…

### 6. [Retrieval-Augmented Personalization with Foundation Models for Wearable Stress Detection](https://arxiv.org/abs/2606.24985)
**Louis Simon, Mohamed Chetouani**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2606.24985) · [pdf](https://arxiv.org/pdf/2606.24985)  ·  relevance 24
<br>matched: `self-supervised`, `foundation model`, `transformer`, `retrieval-augmented`

> Personalization in wearable-based stress detection remains challenging due to substantial inter-individual variability in physiological and behavioral responses. While traditional approaches rely on user-specific fine-tuning or costly self-supervised pre-training on large datasets, we propose a lightweight alternative based on retrieval-augmented personalization. Our method leverages frozen, out-of-domain foundation models to retrieve similar patterns from a target user's…

### 7. [Yuvion VL: A Multimodal Foundation Model for Adversarial Content and AI Safety](https://arxiv.org/abs/2606.25034)
**Shikai Qiu, Xiaowen Xu, Benlei Cui, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2606.25034) · [pdf](https://arxiv.org/pdf/2606.25034)  ·  relevance 24
<br>matched: `foundation model`, `large language model`, `interpretab`, `multimodal`

> General-purpose models often struggle to reliably identify and understand real-world multimodal risks, largely due to the inherent multimodal adversarial nature of content and AI safety. We present Yuvion VL, a family of multimodal large language models purpose-built for content and AI safety, with both instruction-tuned and reasoning-oriented variants. Yuvion VL addresses this gap by treating safety as an inherently adversarial and multimodal problem and designing the…

### 8. [Efficient Remote Sensing Instance Segmentation with Linear-Time State Space Distilled Visual Foundation Models](https://arxiv.org/abs/2606.25324)
**Qinzhe Yang, Keyan Chen, Jia Xu, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2606.25324) · [pdf](https://arxiv.org/pdf/2606.25324)  ·  relevance 22
<br>matched: `foundation model`, `transformer`, `large language model`, `segmentation`, `state space model`

> The computational complexity of Transformers scales quadratically with the number of tokens, which significantly constrains the efficiency of vision models, particularly recent ViT-based foundation models in dense prediction tasks. Instance segmentation, a typical dense visual prediction task in the remote sensing field, faces similar challenges. In this paper, inspired by the recent advances of knowledge distillation in large language models, we introduce RS4D - a new…

### 9. [Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models](https://arxiv.org/abs/2606.26079)
**Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2606.26079) · [pdf](https://arxiv.org/pdf/2606.26079)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from…

### 10. [Cross-Attention Multimodal Learning for Predicting Response to Neoadjuvant Imatinib in Gastrointestinal Stromal Tumors: A Multicenter Retrospective Study](https://arxiv.org/abs/2606.25579)
**Fariba Tohidinezhad, Douwe J. Spaanderman, Natalia Oviedo Acosta, et al.**  ·  `eess.IV`  ·  [abs](https://arxiv.org/abs/2606.25579) · [pdf](https://arxiv.org/pdf/2606.25579)  ·  relevance 19
<br>matched: `self-supervised`, `interpretab`, `explainab`, `multimodal`

> Background: Response to neoadjuvant imatinib in gastrointestinal stromal tumors (GISTs) is highly variable and cannot be reliably predicted using current clinical or molecular markers. This study developed and evaluated an explainable multimodal deep learning framework integrating computed tomography (CT) imaging and clinical variables to predict treatment response. Methods: Patients from four tertiary centers were retrospectively included between 2000-2023 in independent…

### 11. [Graph-Based Phonetic Error Correction of Noisy ASR](https://arxiv.org/abs/2606.24889)
**Pratik Rakesh Singh, Mohammadi Zaki, Aneesh Mukkamala, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2606.24889) · [pdf](https://arxiv.org/pdf/2606.24889)  ·  relevance 19
<br>matched: `graph neural network`, `graph neural`, `gnn`, `large language model`, `llm`

> Automatic speech recognition (ASR) systems, despite low overall word error rates, produce residual lexical errors that disproportionately affect semantically critical tokens such as named entities, negations, and sentiment-bearing words. These errors are often structured, arising from phonetic similarity rather than random noise, making naive token-level correction insufficient. We propose a structured ASR correction framework, that we call G-SPIN, that combines phonetic…

### 12. [Don't Go Breaking My LLM: The Impact of Pruning Attention Layers on Explanation Faithfulness and Confidence Calibration](https://arxiv.org/abs/2606.24970)
**Pietro Tropeano, Maria Maistro, Tuukka Ruotsalo, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2606.24970) · [pdf](https://arxiv.org/pdf/2606.24970)  ·  relevance 18
<br>matched: `large language model`, `llm`, `interpretab`, `explainab`

> Pruning Large Language Models (LLMs) reduces memory and inference costs by removing parts of the network, producing smaller models that retain most of their accuracy. As attention layers are the most resource-intensive parts of LLMs, pruning them is a promising compression strategy. Prior work shows that up to 33% of attention layers can be pruned with minimal accuracy loss. Nevertheless, the impact of attention pruning on model interpretability, specifically faithfulness…


<sub>Generated 2026-06-25 04:01 UTC via the arXiv API.</sub>

---

## Archive

- [2026-06-25](digests/2026-06-25.md) — 12 papers

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
