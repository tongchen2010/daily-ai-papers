# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-06** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-06

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Graph Neural Networks for Resource Allocation in Integrated Sensing and Communication](https://arxiv.org/abs/2611.07277)
**Junyu Liao, Lili Chen, Tian Han, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.07277) · [pdf](https://arxiv.org/pdf/2611.07277)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> In vehicular integrated sensing and communication (ISAC) networks, each service-provider vehicle uses a limited power budget to serve multiple sensing targets and communication receivers. Maximizing the communication sum-rate subject to sensing signal-to-interference-plus-noise ratio (SINR) constraints is nonconvex, and iterative optimization is costly to rerun for every network layout. This paper proposes a graph neural network (GNN)-based power allocation algorithm, termed…

### 2. [Module-Aware Optimization for Graph Neural Networks](https://arxiv.org/abs/2611.08379)
**Guy Hadad, Haggai Roitman, Moshe Eliasof, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.08379) · [pdf](https://arxiv.org/pdf/2611.08379)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Different optimizers impose different geometries on parameter updates. Adaptive methods such as Adam and AdamW use coordinate-wise updates, while matrix-aware optimizers such as Muon utilize weight-matrix structure through orthogonalized updates. For Graph Neural Networks (GNNs), however, the effective geometry of its weight matrices is shaped not only by its learned channel-mixing weights, but also by the graph-propagated representations it acts on. Thus, even if an update…

### 3. [VINO: Revisiting 3D Representation Learning with Volume Transformers](https://arxiv.org/abs/2611.07176)
**Adrian Kruse, Kadir Yilmaz, Daan de Geus, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.07176) · [pdf](https://arxiv.org/pdf/2611.07176)  ·  relevance 25
<br>matched: `representation learning`, `self-supervised`, `foundation model`, `transformer`

> Self-supervised learning has given rise to vision foundation models that learn general-purpose image representations transferable across downstream tasks, yet representation learning for 3D scenes has not achieved comparable success. Motivated by this, we identify key limitations of current 3D representation learning approaches and revisit their core design choices. We first replace the commonly used hierarchical PTv3 backbone with the Volume Transformer, a ViT-like…

### 4. [PSGAgent: Enhancing MLLMs' Dynamic Visual Perception for Panoptic Scene Graph Generation via Agentic Reasoning](https://arxiv.org/abs/2611.07408)
**Qingyun Liu, Yuankun Liu, Jiaye Feng, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.07408) · [pdf](https://arxiv.org/pdf/2611.07408)  ·  relevance 23
<br>matched: `large language model`, `llm`, `agent`, `segmentation`, `multimodal`

> Panoptic Scene Graph generation (PSG) requires holistic yet fine-grained reasoning over complex relations among objects. However, current Multimodal Large Language Models (MLLMs) applied to PSG suffer from a perception bottleneck: they function as static observers limited by fixed-resolution views. As a result, models often overlook critical relations involving small or peripheral objects and struggle to differentiate ambiguous predicates in complex scenes. To address these…

### 5. [Foundation Models as Modular Tools for fMRI Analysis](https://arxiv.org/abs/2611.06926)
**Joseph Kilgore, Noemia Mahmud, Shinjae Yoo, et al.**  ·  `q-bio.NC`  ·  [abs](https://arxiv.org/abs/2611.06926) · [pdf](https://arxiv.org/pdf/2611.06926)  ·  relevance 23
<br>matched: `fmri`, `foundation model`, `llm`, `agent`

> Foundation models (FMs) for the brain are rapidly growing in number and each captures a different aspect of the same data. A single scientific question often needs several of them at once, alongside classical analysis and the literature, but no established method combines them, because each model defines its own inputs, outputs, and spatial conventions. Representation alignment, the usual route from an FM into a language model, binds one FM to one LLM and requires retraining…

### 6. [Multimodal Information Interactions Bottleneck for Multimodal Self-Supervised Learning](https://arxiv.org/abs/2611.07718)
**Liangjian Wen, Jiangtao Zheng, Jiang Duan, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.07718) · [pdf](https://arxiv.org/pdf/2611.07718)  ·  relevance 21
<br>matched: `self-supervised`, `multimodal`

> Multimodal self-supervised learning is challenged by heterogeneity, unequal informativeness, and complex information interactions across multimodal data sources such as images, text, audio, and tabular data. While contrastive methods effectively align shared semantics, they typically rely on strong multi-view redundancy assumptions, overlooking modality-specific and synergistic information, thus leading to suboptimal representations. We propose the Multimodal Information…

### 7. [Self-Supervised Diffusion Models for Handwritten Signature Verification via Ruin Reconstruction](https://arxiv.org/abs/2611.07810)
**Peirong Zhang, Zhenhua Yang, Jiaxin Zhang, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.07810) · [pdf](https://arxiv.org/pdf/2611.07810)  ·  relevance 21
<br>matched: `self-supervised`, `diffusion model`

> Handwritten signature verification (HSV) is a critical biometric technique in legal and forensic authentication, whose efficacy hinges on the discriminability of signature representations. Current HSV methods predominantly adopt supervised learning to enhance representation quality, leaving self-supervised learning largely unexplored. We propose \emph{SigDiffuser}, a diffusion-based self-supervised framework for signature representation and verification. At its core,…

### 8. [Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models](https://arxiv.org/abs/2611.05927)
**Donggeun Kim**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.05927) · [pdf](https://arxiv.org/pdf/2611.05927)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Mixture-of-Experts (MoE) enables multimodal large language models (MLLMs) to scale capacity efficiently, but expert parameters dominate memory even though only a few experts are activated per token: they account for over 90% of model size in modern MoE-MLLMs (e.g., 54 GB out of about 58 GB in BF16 for InternVL3.5-30B-A3B and Qwen3-VL-30B-A3B). Expert pruning has emerged as an effective compression strategy, but existing methods aggregate importance uniformly across tokens,…

### 9. [A Generative Foundation Model for Multimodal Tokamak Tasks](https://arxiv.org/abs/2611.08153)
**Yingshuai Ji, Haodong Feng, Guohong Deng, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.08153) · [pdf](https://arxiv.org/pdf/2611.08153)  ·  relevance 20
<br>matched: `foundation model`, `transformer`, `multimodal`

> Tokamak experiments record diverse measurements, including waveforms, profiles, fields, and scalars, which are used to reconstruct the plasma, forecast its evolution, recover associated control signals, and estimate disruption risk. Most models are built separately for one task and a fixed set of inputs and outputs, and each relies on a prescribed subset of diagnostics rather than structuring the full multimodal observation set to extract global, cross-signal information…

### 10. [Binding Paraphrased Instructions to Encountered Objects in sLLM Agents under Partial Observability](https://arxiv.org/abs/2611.07599)
**Chanyoung Kim, Harim Song, Byoungchan Ko, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.07599) · [pdf](https://arxiv.org/pdf/2611.07599)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Reliable deployment of LLM agents requires grounding diverse user expressions in their environments. Although RL-finetuned smaller large language model (sLLM) agents rival larger prompted LLMs on embodied tasks, their robustness to instruction paraphrases remains unclear. We introduce ALFWorld-Para to evaluate this robustness under controlled paraphrases, revealing 21-52% declines in success rates (SRs), predominantly driven by object synonyms. Despite retaining knowledge of…

### 11. [Towards Multiscale Molecular Representation Learning through Geometry-Based Fragmentation for Polymer Property Prediction](https://arxiv.org/abs/2611.07998)
**Makoto Takamoto, Chaitanya Sampara, Viktor Zaverkin, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.07998) · [pdf](https://arxiv.org/pdf/2611.07998)  ·  relevance 18
<br>matched: `representation learning`, `explainab`, `multimodal`

> It is well established that molecular substructures can contribute unequally to chemical and physical properties, with specific motifs or side chains often playing dominant roles. Fragment-based representations have therefore emerged as an effective strategy for incorporating chemically meaningful inductive biases, as exemplified by molecular fingerprints and fragment-based attention mechanisms. However, many existing fragmentation-based machine learning methods rely on…

### 12. [Interpretable Multimodal MRI-Clinical Fusion for Functional Outcome Prediction After Acute Ischemic Stroke](https://arxiv.org/abs/2611.08154)
**Sina Raeisadigh, Henning M\"uller, Abderrahmane Hedjoudje**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.08154) · [pdf](https://arxiv.org/pdf/2611.08154)  ·  relevance 18
<br>matched: `interpretab`, `multimodal`

> This study evaluates the added prognostic value of day-1 multimodal MRI for predicting three-month functional outcome after acute ischemic stroke (AIS). Sixty-six AIS patients with ADC, DWI, FLAIR, and clinical data were analyzed. Three-dimensional pretrained ResNet embeddings were extracted from each MRI modality, reduced using fold-isolated principal component analysis, and combined with structured clinical variables and ADC-derived lesion biomarkers. Linear support vector…


<sub>Generated 2026-11-06 19:57 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-07](digests/2026-09-07.md) — 12 papers
- [2026-09-06](digests/2026-09-06.md) — 12 papers
- [2026-09-05](digests/2026-09-05.md) — 12 papers
- [2026-09-04](digests/2026-09-04.md) — 12 papers
- [2026-09-03](digests/2026-09-03.md) — 12 papers

_…and 69 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
