# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-26** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-26

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [EigenGradCAM with AugSmooth: Enhancing Explainability and Precision in Multi-Stage Alzheimer's Disease Detection](https://arxiv.org/abs/2610.32374)
**Arsham Azam, Sagar Ashraf, Tayyaba Farhat, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.32374) · [pdf](https://arxiv.org/pdf/2610.32374)  ·  relevance 35
<br>matched: `alzheimer`, `dementia`, `interpretab`, `explainab`

> Alzheimer's disease (AD) is a progressive neurological disorder associated with memory loss, cognitive decline, and behavioral disturbances. Early and accurate diagnosis is essential, yet MRI-based deep learning models often lack interpretability, limiting their clinical use. This study presents an explainable deep learning approach for four-class AD staging using 2D axial MRI images. The method combines eigenvector-based Grad-CAM with gradient smoothing to improve saliency…

### 2. [Towards Adversarially Robust Multigraph Neural Networks for Financial Crime Analysis](https://arxiv.org/abs/2610.31718)
**Dennis Heijmans, H. \c{C}a\u{g}r{\i} Bilgi, Rui Wang, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.31718) · [pdf](https://arxiv.org/pdf/2610.31718)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Financial transaction networks are naturally represented as multigraphs, where repeated transactions between the same pair of accounts are modeled as distinct edges. Recently proposed multigraph neural network architectures leverage this structure explicitly to achieve a strong performance on anti-money laundering (AML) tasks. However, their robustness to adversaries that manipulate transaction structures to evade detection remains largely unexplored. We present the first…

### 3. [CFBrainAug: Modularity-Induced Counterfactual Brain Network Augmentation for Interpretable fMRI-based Autism Diagnosis](https://arxiv.org/abs/2610.32184)
**Yifan Qiao, Sheng Li**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.32184) · [pdf](https://arxiv.org/pdf/2610.32184)  ·  relevance 30
<br>matched: `brain network`, `fmri`, `interpretab`

> Machine learning on resting-state functional magnetic resonance imaging (rs-fMRI) brain networks is promising for diagnosing Autism Spectrum Disorder (ASD), but existing methods are prone to overfitting on limited training data, and their post-hoc statistical attribution offers limited clinical interpretability. We propose CFBrainAug, a counterfactual brain network learning framework that unifies data augmentation and counterfactual explanation by learning label-altered…

### 4. [Autoregressive Multimodal Anomaly Detection with Large Language Models for Microservice Systems](https://arxiv.org/abs/2610.31722)
**Yixiang Tang, Fagui Liu, Guoxiang Zhong, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.31722) · [pdf](https://arxiv.org/pdf/2610.31722)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Microservice systems have become a dominant architecture for large-scale cloud applications, enabling rapid deployment and elastic scaling. However, ensuring the reliability and availability of microservice systems critically relies on effective anomaly detection, as failures and performance anomalies can quickly propagate across services and severely impact end-to-end system behavior. Existing multimodal anomaly detection approaches for microservice systems often struggle…

### 5. [MedCaseAgent: From Multimodal Clinical Evidence to Rare Disease Case Reports](https://arxiv.org/abs/2610.32258)
**Hongkang Chu, Yifan Shen, Tianjiao Yu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.32258) · [pdf](https://arxiv.org/pdf/2610.32258)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Although Large Language Models (LLMs) have demonstrated potential in clinical documentation, generating the rigorous, evidence-based reasoning required for unprecedented, atypical, and rare disease case reports remains a significant challenge. We present MedCaseAgent, an end-to-end agentic reasoning paradigm that bridges this gap by synthesizing publication-quality reports from unstructured clinical notes. MedCaseAgent leverages a hierarchical structure, integrating…

### 6. [Adaptive Control of Scientific Instruments with Nonstationary Responses through Multimodal Agents](https://arxiv.org/abs/2610.32370)
**Guoyang Shi, Hongwen Li, Yiding Yu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.32370) · [pdf](https://arxiv.org/pdf/2610.32370)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Controlling scientific instruments requires parameters to be adjusted progressively in response to feedback from successive operations. When unobserved operating conditions evolve with operational history, responses become nonstationary, and a static mapping from actions to responses becomes inadequate for decisions across shots. Shot-to-shot tuning of neutral beam injection (NBI) ion sources in magnetic confinement fusion devices is representative of this class of problems:…

### 7. [Representation Learning via Composite Subspace Flow Matching](https://arxiv.org/abs/2610.32256)
**Jos\'e Afonso, M\'ario Figueiredo**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.32256) · [pdf](https://arxiv.org/pdf/2610.32256)  ·  relevance 20
<br>matched: `representation learning`, `self-supervised`, `generative model`, `transformer`

> Distilling semantic meaning from raw image data remains a challenge in machine learning. Current self-supervised paradigms face a trade-off: joint-embedding architectures produce relevant features by aggressively discarding intra-class variance, irreversibly spatial and reconstruction. Conversely, generative models preserve spatial details but struggle to isolate semantics, as their optimization is dominated by pixel variations. To bridge this divide, we propose composite…

### 8. [Hybrid SEIR Temporal Fusion Transformer Framework with SHAP Analysis for Interpretable Pandemic Forecasting](https://arxiv.org/abs/2610.31673)
**Ashish Anton Abraham, Gopi Krishnan R, Aiswarya Anil Nair, et al.**  ·  `physics.soc-ph`  ·  [abs](https://arxiv.org/abs/2610.31673) · [pdf](https://arxiv.org/pdf/2610.31673)  ·  relevance 18
<br>matched: `transformer`, `interpretab`, `explainab`

> Forecasting pandemic spread across heterogeneous regions demands models that are both accurate and interpretable for public health action. This paper proposes a hybrid forecasting framework that integrates an SEIR epidemiological model enhanced with a Temporal Fusion Transformer (TFT) to produce interpretable multi-horizon infection forecasts. Using region-wise COVID-19 data from the Our World in Data corpus, we present a unified pipeline that integrates epidemiological…

### 9. [Behaviour analysis for large language model-driven agents](https://arxiv.org/abs/2610.32087)
**Tianqiang Yan, Lizhen Qu**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.32087) · [pdf](https://arxiv.org/pdf/2610.32087)  ·  relevance 18
<br>matched: `large language model`, `agent`, `interpretab`

> Understanding language-agent behaviour requires learning how actions are organised across a trajectory and how this organisation relates to context and outcomes. We propose a general framework that connects data-driven behavioural discovery with analysis and experimental investigation. Categories developed from recorded activity define what is measured. Analyses preserve the behaviours' positions in the process and express their relationships as interpretable hypotheses.…

### 10. [LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents](https://arxiv.org/abs/2610.32412)
**Shen Liu, Ze Zhou, Zhenguo Xu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.32412) · [pdf](https://arxiv.org/pdf/2610.32412)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Recursive large language model (LLM) agents solve long-horizon tasks through decomposition, execution, and environmental feedback. Yet after producing an atomic subtask, they often invoke the same large model again to translate a familiar instruction into an executable action. We observe that high-level planning is task-specific, whereas leaf-level action grounding recurs across tasks and can be checked against environment-admitted actions. We introduce LeafSkill, an…

### 11. [Async-RBench: Benchmarking Asynchronous Task Execution in LLM Agents](https://arxiv.org/abs/2610.32429)
**Detao Zeng, Guilin Ou, Nuo Chen, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.32429) · [pdf](https://arxiv.org/pdf/2610.32429)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents increasingly execute tasks asynchronously: a main agent continues working while its subagents run, and the task state may change before their results arrive. The main agent must decide which work to update or preserve and which checks to repeat, while avoiding prohibited changes. Final task success alone does not reveal whether these results were handled correctly, and natural asynchronous arrivals are hard to reproduce. We introduce…

### 12. [A Foundation Model for Policy In-Context Longitudinal Causal Effect Estimation](https://arxiv.org/abs/2610.32863)
**Wenxin Chen, Kyra Gan, Mingyu Lu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.32863) · [pdf](https://arxiv.org/pdf/2610.32863)  ·  relevance 18
<br>matched: `foundation model`, `longitudinal`

> Longitudinal causal effect estimation is complicated by time-varying confounding and treatment-confounder feedback loops. Existing methods generally require data-specific nuisance-model fitting, and many are tailored to prespecified treatment sequences or prediction horizons, leading to time-consuming computation at deployment. We introduce *Policy In-Context Longitudinal causal Effect estimation with Prior-data Fitted Networks* (**PICLE-PFN**), the first foundation model…


<sub>Generated 2026-10-26 19:19 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-26](digests/2026-08-26.md) — 12 papers
- [2026-08-25](digests/2026-08-25.md) — 12 papers
- [2026-08-24](digests/2026-08-24.md) — 12 papers
- [2026-08-23](digests/2026-08-23.md) — 12 papers

_…and 58 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
