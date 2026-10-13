# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-13** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-13

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Amortized Counterfactual Prediction with Graph Neural Networks](https://arxiv.org/abs/2610.13724v1)
**Hendrik Stumpf, Francesco Quinzan**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13724v1) · [pdf](https://arxiv.org/pdf/2610.13724v1)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Counterfactual inference asks how an observed outcome might have differed under different circumstances, such as whether a patient would have recovered had they received a different treatment. Such questions arise whenever decisions depend on the outcomes of alternatives that were not observed. Answering counterfactual queries generally requires knowledge of the underlying causal structure, which is often unavailable in practice. A common approach is therefore to first…

### 2. [Neurons++: A Unified Visual-Stream Framework for Image and Video Reconstruction from fMRI with Neural-to-Visual Interpretability](https://arxiv.org/abs/2610.13763v1)
**Haonan Wang, Yuchen Wang, Jingyu Lu, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.13763v1) · [pdf](https://arxiv.org/pdf/2610.13763v1)  ·  relevance 22
<br>matched: `cortical`, `fmri`, `interpretab`

> Decoding visual experience from fMRI is important for understanding human perception and developing brain-computer interfaces. Recent generative decoding methods can reconstruct plausible images and videos, but visual plausibility alone does not ensure that the output is faithfully grounded in brain activity. In this work, we propose Neurons++, a visual-stream fMRI reconstruction framework for both static image and dynamic video reconstruction. Compared with our conference…

### 3. [UkrMeme: Multimodal Explainable Persuasion Detection in Ukrainian Memes](https://arxiv.org/abs/2610.13783v1)
**Nazar Andrushko, Vera Schmitt, Veronika Solopova**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.13783v1) · [pdf](https://arxiv.org/pdf/2610.13783v1)  ·  relevance 18
<br>matched: `explainab`, `multimodal`

> Memes play a central role in modern online communication, especially in contexts of political conflict where visual and textual cues combine to convey persuasive messages. We study persuasive technique detection in Ukrainian memes using vision-language models (VLMs). We introduce UkrMeme, a dataset of 200 organically produced Ukrainian wartime memes annotated for persuasion techniques, and PTM-UA, a Ukrainian translation of a subset of the Propaganda 950 benchmark that…

### 4. [A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models](https://arxiv.org/abs/2610.13663v1)
**Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.13663v1) · [pdf](https://arxiv.org/pdf/2610.13663v1)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems…

### 5. [Where to Look Matters: Rethinking Sub-Volume Sampling in 3D Medical Self-supervised Learning](https://arxiv.org/abs/2610.13915v1)
**Junkai Liu, Le Zhang**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.13915v1) · [pdf](https://arxiv.org/pdf/2610.13915v1)  ·  relevance 16
<br>matched: `representation learning`, `self-supervised`

> Self-supervised learning on 3D medical images commonly relies on random sub-volume sampling during pretraining. However, random cropping implicitly treats all spatial regions as equally worth observing, despite anatomical priors and spatial redundancy that make regions inherently unequal in their value for representation learning. To this end, we first show through controlled crop-quality manipulations that better sub-volumes lead to better downstream transfer, revealing the…

### 6. [Matched-Context Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2610.13755v1)
**Chenxu Zhang, Yaorui Shi, Wenlong Zhang, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13755v1) · [pdf](https://arxiv.org/pdf/2610.13755v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-Context Group Policy Optimization (MCGPO), a procedure for constructing weighted action preferences from already collected trajectories. MCGPO defines comparison…

### 7. [Transformer-based In-Context Score Operator Learning for Diffusion Models](https://arxiv.org/abs/2610.13690v1)
**Wuzhe Xu, Zhaiming Shen, Yulong Lu, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13690v1) · [pdf](https://arxiv.org/pdf/2610.13690v1)  ·  relevance 15
<br>matched: `diffusion model`, `transformer`

> Diffusion models typically learn the generative dynamics of a single target distribution or a family of distributions indexed by conditioning variables fixed during training. This limits their ability to adapt to a previously unseen distribution from only a small set of examples. We introduce an in-context solution operator learning framework for diffusion models, in which each target distribution is treated as a task drawn from a meta-distribution and is specified at…

### 8. [TabMF: Learning Dataset Representations with Tabular Foundation Models](https://arxiv.org/abs/2610.13818v1)
**Rafiq Kamel, Nicolas Atienza, Aziz Fouché, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13818v1) · [pdf](https://arxiv.org/pdf/2610.13818v1)  ·  relevance 13
<br>matched: `representation learning`, `foundation model`

> Representations of supervised datasets support higher-level machine-learning tasks such as dataset retrieval and distribution-shift monitoring. However, existing approaches typically rely either on hand-crafted meta-features or on dataset encoders trained specifically for representation learning. We introduce TabMF, a framework that repurposes pretrained tabular foundation models (TFMs) as encoders of supervised datasets. TabMF equips a predictive TFM with an…

### 9. [Tracking the Invisible: Self-Supervised Wheel Track Detection with Thermal-RGB Fusion](https://arxiv.org/abs/2610.13872v1)
**Yiming Yang, Jeremy P. Bos**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.13872v1) · [pdf](https://arxiv.org/pdf/2610.13872v1)  ·  relevance 12
<br>matched: `self-supervised`

> Accurate detection of drivable area is essential for autonomous driving and advanced driver assistance systems. While state-of-the-art methods focus on general traversability estimation, they prove inadequate for snow-covered roads where following existing wheel tracks offers crucial advantages: improved traction, predictable vehicle dynamics, and verified path stability. To address this, we propose a low-cost, self-supervised approach detecting safety-critical wheel tracks…

### 10. [QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code](https://arxiv.org/abs/2610.13811v1)
**Meriem Terki, Nouhaila Innan, Minghao Shao, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13811v1) · [pdf](https://arxiv.org/pdf/2610.13811v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a…

### 11. [Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering and Breadth-Aware Selection for LLM Query Expansion](https://arxiv.org/abs/2610.13810v1)
**Amit Kumar Jaiswal, Sagar Uprety, Prayag Tiwari**  ·  `cs.IR`  ·  [abs](https://arxiv.org/abs/2610.13810v1) · [pdf](https://arxiv.org/pdf/2610.13810v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Large language models (LLMs) are now a standard source of query expansion terms but they hallucinate. They inject non existent entities and off-topic terms that add ranking noise and can hurt strong retrievers. Existing remedies such as corpus grounding, mutual verification and preference alignment treat hallucinated terms as an undifferentiated nuisance to be filtered by agreement heuristics, without a mechanistic account of why a given term appears or a principled…

### 12. [Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction](https://arxiv.org/abs/2610.13672v1)
**Jiwon Jeon, Myungsik Cho, Jeonghye Kim, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.13672v1) · [pdf](https://arxiv.org/pdf/2610.13672v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Large language models struggle to reliably identify and correct errors in their own reasoning. Unlike prior training-based approaches that fine-tune an LLM to generate revisions or feedback, we learn where to intervene in failed rollouts and determine how to redirect them. To choose where to intervene, we train a 130K-parameter MLP head on a frozen encoder using only final-answer correctness. For redirection, we find that under a fixed generation budget, the tested inline…


<sub>Generated 2026-10-13 19:51 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-10](digests/2026-08-10.md) — 12 papers
- [2026-08-09](digests/2026-08-09.md) — 12 papers

_…and 45 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
