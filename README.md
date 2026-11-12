# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-12** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-12

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [CroCoMAE: Cross-modal self-supervised collaborative representation learning for SAR-optical remote sensing data](https://arxiv.org/abs/2611.14124v1)
**Vito Recchia, Giuseppe Guarino, Cássio Fraga Dantas, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.14124v1) · [pdf](https://arxiv.org/pdf/2611.14124v1)  ·  relevance 26
<br>matched: `representation learning`, `self-supervised`, `segmentation`

> Remote sensing increasingly captures the Earth's surface through complementary sensors such as SAR and optical, yet ground-truth annotations remain scarce, limiting supervised approaches. Self-supervised learning (SSL) addresses the label scarcity, and cross-modal SSL further exploits the complementarity between co-located sensors, but existing cross-modal frameworks align modalities mostly through global image-level representations or treat them as largely redundant,…

### 2. [Hierarchical Graph Representation Learning with Pooling-Induced Substructures](https://arxiv.org/abs/2611.14126v1)
**Luca Sbicego, Xiaowen Dong, Dorina Thanou**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.14126v1) · [pdf](https://arxiv.org/pdf/2611.14126v1)  ·  relevance 25
<br>matched: `graph neural network`, `graph neural`, `gnn`, `representation learning`

> Hierarchical graph-level tasks that require reasoning over substructures that extend beyond local neighborhoods are posing challenges for standard Graph Neural Networks (GNNs). While graph pooling aims to address this by coarsening graphs into hierarchical representations, existing methods often fail to explicitly preserve the substructures they induce, leading to inconsistent empirical performance. Moreover, evaluating such approaches remains challenging due to the lack of…

### 3. [Physics-Constrained Autoencoder for Interpretable Health Representation Learning in Turbofan Engines](https://arxiv.org/abs/2611.14266v1)
**Leonardo Baldo, Jokin Alcibar Ibarzabal, Daniel Cisneros Acevedo, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.14266v1) · [pdf](https://arxiv.org/pdf/2611.14266v1)  ·  relevance 21
<br>matched: `representation learning`, `interpretab`

> Health Indices (HIs) summarize degradation from operational data and support diagnostic and prognostic tasks in Prognostics and Health Management (PHM). Their usefulness depends on capturing degradation and interpreting system condition. Autoencoders learn such representations from unlabelled monitoring data; however, when training is driven only by reconstruction, the physical meaning of latent variables remains undefined, limiting their interpretation and diagnostic value.…

### 4. [Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs](https://arxiv.org/abs/2611.14122v1)
**Federico Ravenda, Mirko Cesarini, Daniele Montagnani, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.14122v1) · [pdf](https://arxiv.org/pdf/2611.14122v1)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Large language models (LLMs) achieve expert-level diagnostic accuracy in static evaluations, where the model receives a curated vignette or case report that already condenses the diagnostically relevant findings. Such evaluations measure inference over already selected evidence; the evaluations do not account for the inquiry used to obtain it. In clinical practice, however, diagnosis is an iterative process of inquiry. Clinicians take the patient's history, or anamnesis…

### 5. [Stagewise and interpretable emergence of inside-outside computation in Transformer-based language models](https://arxiv.org/abs/2611.14221v1)
**Jack T. Parley**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.14221v1) · [pdf](https://arxiv.org/pdf/2611.14221v1)  ·  relevance 18
<br>matched: `transformer`, `llm`, `interpretab`

> Variability in syntactic structure and parsing ambiguity are fundamental aspects of natural language which modern LLMs have to learn to deal with proficiently. Previous "post-mortem" studies have shown that fully trained Transformers indeed approximate canonical parsing algorithms such as inside-outside, but little is established theoretically about how this is actually learned. Here, we make a first step towards addressing this by studying the learning dynamics in synthetic…

### 6. [Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training](https://arxiv.org/abs/2611.14519v1)
**Emre Kutlusan, Yongmin Li**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.14519v1) · [pdf](https://arxiv.org/pdf/2611.14519v1)  ·  relevance 15
<br>matched: `foundation model`, `segmentation`

> Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be…

### 7. [EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities](https://arxiv.org/abs/2611.14356v1)
**Zhengxiang Huang, Yujie Sun, Shengheng Chen, et al.**  ·  `cs.OS`  ·  [abs](https://arxiv.org/abs/2611.14356v1) · [pdf](https://arxiv.org/pdf/2611.14356v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly system challenge. Each model may require coordinated changes across conversion, graph construction, operators, and hardware backends. Existing coding agents often miss these cross-layer dependencies and struggle to diagnose failures across host--device execution paths. We present EngineAgent, an agentic system for automating…

### 8. [When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents](https://arxiv.org/abs/2611.14326v1)
**Runxuan Tang, Haoyu Gao, Yuyan Ding, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.14326v1) · [pdf](https://arxiv.org/pdf/2611.14326v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that…

### 9. [Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320v1)
**Yukyeong Lee, Yumin Choi, Jinheon Baek, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.14320v1) · [pdf](https://arxiv.org/pdf/2611.14320v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled only with task success or failure, yet are typically provided…

### 10. [Chain of Physics: Supporting Fault Diagnosis with Engineering-Inspired Large Language Model Reasoning](https://arxiv.org/abs/2611.14263v1)
**Wenqi Zhou, Leonardo Baldo, Kai Goebel, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.14263v1) · [pdf](https://arxiv.org/pdf/2611.14263v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `retrieval-augmented`

> Fault diagnosis in complex systems requires linking observed changes in physical quantities to the failure mechanisms that produce them. Experienced engineers perform this task by combining sensor information with knowledge of system behavior and fault propagation. Large Language Models (LLMs) can support this process, but their diagnostic reasoning depends on the availability of asset-specific engineering knowledge and on how this knowledge is represented and used during…

### 11. [A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents](https://arxiv.org/abs/2611.14256v1)
**Jingjing Jiang**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.14256v1) · [pdf](https://arxiv.org/pdf/2611.14256v1)  ·  relevance 15
<br>matched: `agent`, `multimodal`

> Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey investigates the structural source of asymmetric mechanism transfer across four scenarios: multimodal reasoning, multimodal generation, GUI and Web navigation, and embodied manipulation. We first…

### 12. [TAMEing the Open-World Personalization: Towards Open-Set Personalized MLLM Assistant](https://arxiv.org/abs/2611.14118v1)
**Rongpei Hong, Jian Lang, Ting Zhong, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.14118v1) · [pdf](https://arxiv.org/pdf/2611.14118v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `multimodal`

> Personalizing Multimodal Large Language Models (MLLMs) as intelligent assistants has recently emerged as an active research topic, where an MLLM is expected to go beyond generic, one-size-fits-all replies, and instead generate responses grounded in user-specific objects, entities, and concepts encountered during interactions. Nevertheless, existing studies mainly focus on personalizing MLLMs on a static, predefined set of personalized concepts and require users to manually…


<sub>Generated 2026-11-12 20:49 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-14](digests/2026-09-14.md) — 12 papers
- [2026-09-12](digests/2026-09-12.md) — 12 papers
- [2026-09-11](digests/2026-09-11.md) — 12 papers
- [2026-09-10](digests/2026-09-10.md) — 12 papers
- [2026-09-09](digests/2026-09-09.md) — 12 papers

_…and 75 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
