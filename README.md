# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-16** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-16

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Transferable conditional brain charts link cortico-subcortical structure to Alzheimer's disease progression](https://arxiv.org/abs/2610.21660)
**Nitin Sharma, Sicheng Dai, Francesco A. Mallus, et al.**  ·  `q-bio.NC`  ·  [abs](https://arxiv.org/abs/2610.21660) · [pdf](https://arxiv.org/pdf/2610.21660)  ·  relevance 55
<br>matched: `alzheimer`, `dementia`, `neuroimaging`, `cortical`, `disease progression`

> Normative models chart how brain measures vary across the lifespan, expressing each individual as a deviation from a healthy reference. However, most regional models of cortical thickness disregard dependencies between cortical and subcortical anatomy, and transferring them to a new site typically requires retraining or a recalibration of location and scale alone. We condition lifespan norms of cortical thickness on subcortical volume, such that each deviation indicates…

### 2. [Decomposing Brain-LLM Alignment with Interpretable Semantic Representations](https://arxiv.org/abs/2610.21508)
**Camila Kolling, Mariya Toneva**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.21508) · [pdf](https://arxiv.org/pdf/2610.21508)  ·  relevance 24
<br>matched: `fmri`, `large language model`, `llm`, `interpretab`

> Large language models (LLMs) predict neural responses during naturalistic language comprehension, but the linguistic information underlying this brain alignment remains difficult to interpret. We use SCRIBE, an interpretable contextual semantic representation spanning 65 neurocognitively grounded semantic properties, as a lens for decomposing the brain alignment of one LLM, LLaMA2-7B. Using variance partitioning between LLaMA2-7B and SCRIBE on naturalistic fMRI data from…

### 3. [MedPAO-VL: Interpretable and Protocol-Compliant Agent for Structured Radiology Report Generation](https://arxiv.org/abs/2610.21794)
**Shrish Shrinath Vaidya, Gowthamaan Palani, Minmini Selvam, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.21794) · [pdf](https://arxiv.org/pdf/2610.21794)  ·  relevance 24
<br>matched: `large language model`, `agent`, `interpretab`, `explainab`, `multimodal`

> Despite the remarkable generalization capabilities of Large Language Models, generating clinically accurate and structured radiology reports from medical images remains a significant challenge. Current end-to-end approaches function as black boxes, prone to factual hallucinations and generating ungrounded findings. This lack of reliability and failure to adhere to domain-specific structuring protocols, fundamentally limits their clinical utility. We present MedPAO-VL, a…

### 4. [CoViG: Coarsened Vision GNN for Image Classification](https://arxiv.org/abs/2610.21321)
**Martial Guidez, Stefan Duffner, Christophe Garcia**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.21321) · [pdf](https://arxiv.org/pdf/2610.21321)  ·  relevance 23
<br>matched: `graph neural network`, `graph neural`, `gnn`, `transformer`

> Although Graph Neural Networks are widely used in various domains, they remained mostly unexplored in computer vision. Convolutional Neural Networks and Vision Transformers were leading the field, until the quite recent introduction of Vision Graphs (ViG) that treat images as a set of nodes and apply graph convolution on their k-NN graphs. ViGs show impressive accuracy on image classification but their computational cost remains relatively high. Inspired by optimization…

### 5. [MSP: Modality Self-Play for Training Multimodal LLMs Without Paired Cross-Modal Data](https://arxiv.org/abs/2610.20965)
**Robert Moseley, Md Kaykobad Reza, Ameya Patil, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.20965) · [pdf](https://arxiv.org/pdf/2610.20965)  ·  relevance 21
<br>matched: `foundation model`, `llm`, `multimodal`

> Large multimodal models have achieved remarkable progress by scaling model capacity and training on massive paired multimodal data. However, this paradigm introduces a fundamental bottleneck: aligned multimodal datasets are expensive to curate, difficult to scale across diverse modality combinations, and increasingly constrain further progress. We introduce Modality Self-Play (MSP), a training framework for multimodal foundation models based on proxy-mediated modality…

### 6. [AutoOnboarder: Autonomously Onboarding LLM Agents](https://arxiv.org/abs/2610.21218)
**Tanay Arora, Cong Liu**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.21218) · [pdf](https://arxiv.org/pdf/2610.21218)  ·  relevance 21
<br>matched: `foundation model`, `large language model`, `llm`, `agent`

> Agentic large language models have been documented to lose reasoning capability when placed inside a harness, the software that mediates their observations and actions. To reconcile these losses, we introduce AutoOnboarder, an autonomous system that adapts an agent to a task the way a trainer onboards a new employee. It places the agent under the supervision of an intelligent ``Onboarder'' coding agent, which iteratively tailors its foundation model, prompt, and harness…

### 7. [When Reasoning Is Not Enough: Proactive Inquiry for Cross-Modal Safety in Multimodal Large Language Models](https://arxiv.org/abs/2610.22068)
**Wei Cai, Jian Zhao, Yuchen Yuan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.22068) · [pdf](https://arxiv.org/pdf/2610.22068)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) can act unsafely when individually benign images and texts are interpreted jointly. Beyond implicit reasoning risk, where reasoning drifts toward harm, we identify intent-level risk, where cross-modal ambiguity silently commits the model to a hazardous premise that path-level optimization alone cannot correct. We propose SAFE-PRO, which uses a Risk-Conditioned Uncertainty (RCU) signal, combining predictive entropy with a learned…

### 8. [GNN-Guided Local Refinement for Efficient Layout Decomposition with DSA-MP](https://arxiv.org/abs/2610.22214)
**Yu Feng, Liyi Zhou, Haoyu Wang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.22214) · [pdf](https://arxiv.org/pdf/2610.22214)  ·  relevance 21
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Multiple patterning lithography (MPL) has been widely used to improve lithography resolution in advanced nodes, but it faces cost limits as feature sizes shrink. Directed self-assembly (DSA) offers a cost-effective complement, extending the resolution of optical lithography to sub-10 nm and beyond. Integrating DSA into MPL (DSA-MP) further enhances the resolution of contact/via patterning. Nevertheless, growing design complexity exposes the limits of existing decomposition…

### 9. [Hierarchical Interpretable Multitask Audio Representation Learning: An Analysis of Event-Scene Relationships through the Information Bottleneck](https://arxiv.org/abs/2610.21520)
**Claudia Montero-Ram\'irez, Alba Mart\'inez-Serrano, Carmen Pel\'aez-Moreno**  ·  `eess.AS`  ·  [abs](https://arxiv.org/abs/2610.21520) · [pdf](https://arxiv.org/pdf/2610.21520)  ·  relevance 21
<br>matched: `representation learning`, `interpretab`

> Joint Acoustic Scene Classification (ASC) and Audio Tagging (AT) models traditionally rely on unconstrained multihead architectures. However, this design ignores the natural hierarchical dependency between sounds and acoustic scenes. In this work, we investigate a hierarchical (sequential) conditioning paradigm that predicts scene categories directly from intermediate event probabilities. Through a large-scale empirical benchmark with 66 full training runs across three…

### 10. [Agentic-Priors: Using Large Language Models to Address the Cold Start Problem in Preference Elicitation](https://arxiv.org/abs/2610.21938)
**Bruno Arcanjo, Zhaoxing Li, Sebastian Stein**  ·  `cs.MA`  ·  [abs](https://arxiv.org/abs/2610.21938) · [pdf](https://arxiv.org/pdf/2610.21938)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `interpretab`

> An agent that learns a user's preferences from their choices faces a cold start problem: before any choices are observed, it must rely solely on a prior. Informative priors are usually fitted to historical choice data, which new tasks and deployments lack. To address this, we present Agentic-Priors, which lets agentic systems use the implicit knowledge of large language models (LLMs) instead. Specifically, an LLM states a new user's trade-offs in interpretable terms, such as…

### 11. [CausalEvo: Causal Skill Self-Evolution for Health LLM Agents](https://arxiv.org/abs/2610.21016)
**Yuchen Zhang**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.21016) · [pdf](https://arxiv.org/pdf/2610.21016)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents for health can accumulate reusable textual skills from task feedback, such as calculation criteria, measurement time points, and formula units. Deciding which skills to retain is consequential: useful rules improve later answers, while faulty generalizations propagate errors. We propose CausalEvo, a method for causal skill self-evolution that estimates the relative effects of deliberately changed skill sets while holding the model weights,…

### 12. [GraphBEAT: Graph-based Bucketized Event Aggregation Over Time for Early Risk Stratification of Gastrointestinal Cancers](https://arxiv.org/abs/2610.22014)
**Leo Y. Li-Han, Chris Varghese, Elizabeth B. Habermann, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.22014) · [pdf](https://arxiv.org/pdf/2610.22014)  ·  relevance 18
<br>matched: `graph neural network`, `graph neural`, `representation learning`, `longitudinal`, `transformer`

> Longitudinal electronic health records (EHRs) contain complementary diagnostic and laboratory information about patient health. However, irregularity, sparsity, heterogeneity, and incompleteness in documentation complicate EHR modeling. To address the problem, we introduce GraphBEAT (Graph-based Bucketized Event Aggregation over Time), a temporal graph representation learning framework that groups clinical events into time buckets and transforms observed features into…


<sub>Generated 2026-10-16 17:23 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-17](digests/2026-08-17.md) — 12 papers
- [2026-08-16](digests/2026-08-16.md) — 12 papers
- [2026-08-15](digests/2026-08-15.md) — 12 papers
- [2026-08-14](digests/2026-08-14.md) — 12 papers
- [2026-08-12](digests/2026-08-12.md) — 12 papers

_…and 48 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
