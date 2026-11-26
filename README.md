# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-26** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-26

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Adaptive attention routing multimodal expert graph neural network for drug-drug interaction prediction](https://arxiv.org/abs/2611.33200)
**Jingyi Yang, Chengcheng Yan, Hongri Cong, et al.**  ·  `q-bio.QM`  ·  [abs](https://arxiv.org/abs/2611.33200) · [pdf](https://arxiv.org/pdf/2611.33200)  ·  relevance 40
<br>matched: `graph neural network`, `graph neural`, `gnn`, `multimodal`

> Accurate prediction of drug-drug interactions (DDIs) is essential for drug safety in combination therapy. Multimodal methods built on knowledge graphs (KGs) already combine molecular structures, substructures, targets and biomedical relations into drug representations, but they still face three problems: features are heterogeneous across modalities, fusion does not adapt to individual drug pairs, and modality-specific information is diluted during integration. We propose the…

### 2. [Scaling and Cross-Simulation Generalization of Graph Neural Networks for Cosmic-Web Classification in CAMELS](https://arxiv.org/abs/2611.34332)
**Kalash Thakkar, Unnati Shah**  ·  `astro-ph.CO`  ·  [abs](https://arxiv.org/abs/2611.34332) · [pdf](https://arxiv.org/pdf/2611.34332)  ·  relevance 33
<br>matched: `graph neural network`, `graph neural`, `gnn`, `transformer`

> Graph-based methods can classify galaxies by their dark-matter cosmic-web environments, but reliability beyond development simulations remains uncertain. Galaxy-formation models alter tracer populations and spatial distributions, potentially shifting graph features. We test how graph neural networks scale with independent training realizations and transfer across hydrodynamical simulations. Using the $z=0$ CAMELS IllustrisTNG, SIMBA and Astrid suites, we label galaxies with…

### 3. [ChemoMAE: Self-Supervised Spectral Representation Learning Reveals Chemical Heterogeneity in Historical Wood](https://arxiv.org/abs/2611.34581)
**Ryuji Yamaguchi, Miyuki Matsuo**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.34581) · [pdf](https://arxiv.org/pdf/2611.34581)  ·  relevance 26
<br>matched: `representation learning`, `self-supervised`, `transformer`

> In historical timber buildings, multiple environmental factors act over centuries on wood whose chemical composition varies across anatomical regions, producing complex patterns of degradation. Understanding how timber members degrade is important for the effective conservation and restoration of historical buildings, yet the mechanisms underlying these patterns remain unclear. To investigate these mechanisms, we used self-supervised learning to establish a common basis for…

### 4. [GeoCAM: Self-Supervised Sonar-Optical Representation Learning via Geographic Overlap Supervision](https://arxiv.org/abs/2611.34218)
**Fadi Abdeladhim Zidi, Andrea De Salve, Giuseppe Celeste, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.34218) · [pdf](https://arxiv.org/pdf/2611.34218)  ·  relevance 24
<br>matched: `representation learning`, `self-supervised`

> Cross-modal self-supervised learning for paired side-scan sonar and underwater optical imagery is a promising direction for benthic habitat understanding, but it remains underexplored because existing methods do not fully exploit the one-to-many correspondences and geographic metadata available in real opti-acoustic surveys. This limits the ability to learn representations that are both semantically meaningful and geometrically consistent from abundant unlabeled marine data.…

### 5. [Variation-aware Temporal Correspondence for Self-Supervised Video Representation Learning](https://arxiv.org/abs/2611.34220)
**Yang Liu, Qianqian Xu, Peisong Wen, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.34220) · [pdf](https://arxiv.org/pdf/2611.34220)  ·  relevance 24
<br>matched: `representation learning`, `self-supervised`

> Self-supervised video representation learning has achieved remarkable progress by leveraging large-scale unlabeled video data. Recent methods commonly extend Masked Image Modeling (MIM) to Masked Video Modeling (MVM), where video representations are learned by capturing semantic information from temporal contexts during masked content recovery. Unlike static images, videos exhibit inherent temporal variation, as visual objects continuously change their positions,…

### 6. [Privileged On-Policy Distillation for Calibrated Alzheimer's Diagnosis With Missing Modalities](https://arxiv.org/abs/2611.34721)
**Vo Minh Khoi Nguyen, Dat Tien Chung, Quang Minh Khoa Le, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.34721) · [pdf](https://arxiv.org/pdf/2611.34721)  ·  relevance 23
<br>matched: `alzheimer`, `neuroimaging`

> Alzheimer's disease is diagnosed from clinical, biospecimen and imaging evidence, but few patients undergo every test. Because these modalities are complementary, a missing one has many plausible values. Most existing methods leave it out or train on one estimate, so their classifier never sees its other values, and the estimate is never checked against the diagnosis. We address both gaps with on-policy distillation: the model fills in the missing modalities itself, and…

### 7. [EVA: Evidence-seeking Visual Agent for Hallucination-Resistant Multimodal Reasoning](https://arxiv.org/abs/2611.33706)
**Ting Lei, Yu Chen, Yang Liu**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.33706) · [pdf](https://arxiv.org/pdf/2611.33706)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Hallucinations in multimodal large language models (MLLMs) often arise from visual assumptions that go unchecked. Self-reflection, multi-agent debate, and counterfactual verification can reinforce erroneous conclusions when they rely on the same unverified visual assumptions. External visual tools can provide verifiable evidence, but models may select the wrong tools, supply incorrect parameters, or ignore or contradict the evidence they obtain. In this work, we propose EVA,…

### 8. [Lost in the Grid: Where Multimodal LLMs Fail Between Seeing and Planning](https://arxiv.org/abs/2611.34152)
**Luoxi Zhang, Tianyi Tan, Jiawei Liu, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.34152) · [pdf](https://arxiv.org/pdf/2611.34152)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) excel at static visual understanding and are increasingly applied to spatial planning, where a model interprets a visual layout and outputs an action sequence to reach a goal. Grid games are a common testbed for this ability because their rules are explicit and a solver can verify every move. Yet existing benchmarks mostly report end-to-end success rates, which hide whether a failure stems from visual perception, rule application, or…

### 9. [SPiXSeg: Rethinking MLLM-based Image Segmentation as Superpixel Classification](https://arxiv.org/abs/2611.33842)
**Piyush Tiwary, Sohini Dutta, Prathosh A. P**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.33842) · [pdf](https://arxiv.org/pdf/2611.33842)  ·  relevance 21
<br>matched: `large language model`, `llm`, `segmentation`, `multimodal`

> Multimodal large language models (MLLMs) are widely used for image segmentation. However, existing methods either use a decoder or use patch-based approach which trades boundary precision against the number of decisions as coarse grid cells mix foreground and background pixels, while finer grids require many more predictions, and autoregressive mask generation adds sequential decoding overhead. We propose SPiXSeg, which shifts the output from per-patch to per-superpixel…

### 10. [Text-Conditioned Low-Rank Adaptation of Time-Series Foundation Models for Multimodal Forecasting](https://arxiv.org/abs/2611.34206)
**Kunqi Li, Bin Liang, Zhidong Li**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.34206) · [pdf](https://arxiv.org/pdf/2611.34206)  ·  relevance 18
<br>matched: `foundation model`, `multimodal`

> Time-series foundation models (TSFMs) provide transferable numerical forecasting priors. However, forecast-relevant information may be conveyed in text without being reflected in the observed series. Many multimodal forecasting methods integrate such context through model inputs or intermediate representations. We investigate a complementary mechanism: text-conditioned parameter adaptation. We propose Context-to-LoRA for Time Series (C2LoRA-TS), which encodes text and…

### 11. [LLM-coupled interpretable tool wear monitoring with multi-evidence reasoning in CNC machining](https://arxiv.org/abs/2611.34270)
**Yuntong Chen, Yingqi Li, Qiwen Shen, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.34270) · [pdf](https://arxiv.org/pdf/2611.34270)  ·  relevance 18
<br>matched: `llm`, `interpretab`

> Interpretable tool wear assessment in CNC machining is challenging. Existing diagnostic models have high accuracy but provide limited guidance for tool replacement. This study proposes a two layer framework combining deep learning wear classification and LLM assisted reasoning. The first layer uses PCA Loading feature selection and optimized GRU to recognize three wear states, achieving 98.38 percent macro F1 score on the PHM2010 dataset. The second layer uses LLMs to…

### 12. [Feature-Based Explainability of Transformer Scoring Models: A Fidelity-First Framework for Automated Writing Assessment](https://arxiv.org/abs/2611.33175)
**Michael Hemenway, Edward W. Wolfe**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.33175) · [pdf](https://arxiv.org/pdf/2611.33175)  ·  relevance 18
<br>matched: `transformer`, `interpretab`, `explainab`

> Transformer-based automated writing scoring models can achieve strong agreement with human scores while providing limited transparency into the response characteristics associated with their predictions. This study evaluated a feature-based post-hoc explanation approach in which explanatory fidelity was established before feature importance was interpreted. English Language Arts responses from three writing prompts in Grades 6 and 8 were analyzed, with about 12,700 responses…


<sub>Generated 2026-11-26 22:20 UTC via the arXiv API.</sub>

---

## Archive

- [2026-11-26](digests/2026-11-26.md) — 12 papers
- [2026-11-25](digests/2026-11-25.md) — 12 papers
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

_…and 88 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
