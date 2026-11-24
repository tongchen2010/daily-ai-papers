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

### 1. [Towards Global Counterfactual-Based Self-Explainable Graph Neural Networks](https://arxiv.org/abs/2611.29681)
**Wendy Zheng, Yinhan He, Jundong Li**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.29681) · [pdf](https://arxiv.org/pdf/2611.29681)  ·  relevance 40
<br>matched: `graph neural network`, `graph neural`, `gnn`, `explainab`

> Graph Counterfactual Explanations (GCEs) have emerged as an effective approach for interpreting Graph Neural Network (GNN) predictions by identifying minimal graph modifications needed to change predictions. However, existing methods suffer from two fundamental limitations: (1) They rely on a post-hoc explanation paradigm, where a separate explainer is trained after the GNN. This sequential optimization prevents the explainer from leveraging how the GNN learned its…

### 2. [Direct Conditioning of Audio Diffusion Transformers on fMRI Reveals Cortical Contributions to Sound Reconstruction](https://arxiv.org/abs/2611.12603)
**Matteo Ciferri, Tonio Weidler, Matteo Ferrante, et al.**  ·  `cs.SD`  ·  [abs](https://arxiv.org/abs/2611.12603) · [pdf](https://arxiv.org/pdf/2611.12603)  ·  relevance 30
<br>matched: `cortical`, `fmri`, `diffusion model`, `transformer`

> Reconstructing audio from brain activity remains challenging. Existing brain-to-audio pipelines typically map neural responses to predefined stimulus representations before synthesis. While recent work in the visual domain has explored direct conditioning on brain activity, this approach has not yet been extended to audio diffusion models. We introduce MAAS (Multi-Area Auditory Synthesis), an end-to-end framework that conditions a pretrained audio diffusion transformer on…

### 3. [LimeTree: Linear-Memory Graph Neural Networks over Tree-Graphs for Resource-Efficient Language Modeling and Context Extrapolation](https://arxiv.org/abs/2611.30934)
**Elisabeth Fink**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.30934) · [pdf](https://arxiv.org/pdf/2611.30934)  ·  relevance 29
<br>matched: `graph neural network`, `graph neural`, `transformer`

> The search for computationally efficient alternatives to the Transformer has yielded numerous architectures in recent years; however, most exhibit severe weaknesses in associative recall-such as key-value (KV) retrieval-and length extrapolation, where even standard Transformers struggle. This paper introduces LimeTree, a linear-complexity architecture in both memory and compute for sequence modeling. By integrating synthetic KV retrieval tasks directly into standard language…

### 4. [From Observation to Explanation: Mechanistic Interpretability of LLM-Generated Code for Principled Repair](https://arxiv.org/abs/2611.28153)
**Musfiqur Rahman**  ·  `cs.SE`  ·  [abs](https://arxiv.org/abs/2611.28153) · [pdf](https://arxiv.org/pdf/2611.28153)  ·  relevance 28
<br>matched: `longitudinal`, `transformer`, `large language model`, `llm`, `agent`, `interpretab`

> Large language models (LLMs) have transformed software development, yet our understanding of how they generate code remains critically underdeveloped. We address this gap by triangulating evidence across three layers. Longitudinally, autonomous agent-attributed code is statistically indistinguishable from human code under a semantic modification definition (HR = 1.019, p = 0.490), yet attracts disproportionately corrective modifications in production (49.1% vs 37.9% human…

### 5. [Aggregation Dispersion: An Information-Geometric Diagnostic of Oversmoothing in Graph Neural Networks](https://arxiv.org/abs/2611.29600)
**Abdessalam Ed-dib, Amine Mohamed Aboussalah**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.29600) · [pdf](https://arxiv.org/pdf/2611.29600)  ·  relevance 27
<br>matched: `graph neural network`, `graph neural`

> Message-passing neural networks (MPNNs) learn node representations by iteratively aggregating information from neighbors, but stacking too many layers causes all representations to converge, an effect known as oversmoothing. We propose a geometric perspective on this phenomenon. At each depth $k$, the propagation operator assigns to every node $v$ a walk distribution $p_v^{(k)}$, a probability distribution over source nodes. These walk distributions form a point cloud on the…

### 6. [Potential Games for Self-Neighborhood Channel Mixing in Graph Neural Networks](https://arxiv.org/abs/2611.30829)
**Marco Lavorini, Davide Bacciu, Giancarlo Bigi**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.30829) · [pdf](https://arxiv.org/pdf/2611.30829)  ·  relevance 27
<br>matched: `graph neural network`, `graph neural`

> Graph message passing must balance two competing objectives: incorporating neighborhood signals while preserving node-specific information. We model this trade-off as a game in which nodes choose how to mix their own representations with strict-neighborhood aggregates. For fixed channel representations, task supervision defines a common-payoff game, while local distinctness payoffs induce an exact potential game whose potential is the degree-normalized strict Dirichlet…

### 7. [StudioBench: Benchmarking Agentic Multimodal Large Language Models for Productive Audiovisual Creation](https://arxiv.org/abs/2611.28902)
**Xinglong Xu, Yuxia Zhu, Siyuan Li, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.28902) · [pdf](https://arxiv.org/pdf/2611.28902)  ·  relevance 27
<br>matched: `large language model`, `llm`, `agent`, `multimodal`

> Video generators can now render convincing short clips, yet complete audiovisual works require coordinating visuals, sound, and editing across multiple stages. Existing benchmarks focus on individual generators or video agents under narrower production settings, leaving end-to-end creation by general multimodal large language models (MLLMs) underexplored. We introduce StudioBench, a benchmark comprising 160 tasks across eight video genres and five task types, spanning…

### 8. [Lorentz symmetry in self-supervised representation learning](https://arxiv.org/abs/2611.31011)
**Andreas Hermansen, Tobias Golling, Slava Voloshynovskiy**  ·  `hep-ph`  ·  [abs](https://arxiv.org/abs/2611.31011) · [pdf](https://arxiv.org/pdf/2611.31011)  ·  relevance 26
<br>matched: `representation learning`, `self-supervised`, `transformer`

> Self-supervised learning (SSL) and explicit physical inductive biases have driven major advances in jet tagging, yet they are typically pursued along separate tracks. In this work, we unify both paradigms by integrating the Lorentz-equivariant Geometric Algebra Transformer slim (L-GATr-slim) architecture with the LeJEPA framework for representation learning. Pre-training on 100 million jets from the JetClass dataset, we optimize towards a latent space, which is invariant…

### 9. [HEART: Hierarchical Expert Adaptive Refinement Transformer for ECG Representation Learning](https://arxiv.org/abs/2611.30298)
**Junho Song, Jong-Hwan Jang, Joon-Myoung Kwon, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.30298) · [pdf](https://arxiv.org/pdf/2611.30298)  ·  relevance 25
<br>matched: `representation learning`, `self-supervised`, `foundation model`, `transformer`

> Learning robust representations from electrocardiograms (ECGs) is challenging because repeated cardiac cycles coexist with subtle and sparse diagnostic cues in local morphology and rhythm-level context. Existing ECG foundation models commonly rely on Transformerbased patch encoders with uniformly shared dense refinement pathways, limiting adaptive processing across heterogeneous ECG tokens. We propose HEART (Hierarchical Expert Adaptive Refinement Transformer), an ECG…

### 10. [Learning from Another Angle: Rotation-Based Test-Time Training for Multimodal Large Language Models](https://arxiv.org/abs/2611.28972)
**Changyu Liu, Fei Zhao, Yiyang Liu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.28972) · [pdf](https://arxiv.org/pdf/2611.28972)  ·  relevance 25
<br>matched: `self-supervised`, `large language model`, `llm`, `multimodal`

> Multimodal Large Language Models (MLLMs) achieve strong performance on vision-language tasks but often remain vulnerable to distribution shifts due to their fixed parameters during inference. While Test-Time Training (TTT) offers a pathway for dynamic adaptation, existing approaches suffer from prohibitive computational overhead due to multiple sampling and the risk of error reinforcement from biased self-generated supervision. In light of this view, we propose RoTTT…

### 11. [SleepXA: Composing Pretrained Neural and Cardiac Foundation Models for Sleep Representation Learning](https://arxiv.org/abs/2611.29364)
**Xiaoyu Chen, Xiao Gu, Chao Zhang, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.29364) · [pdf](https://arxiv.org/pdf/2611.29364)  ·  relevance 24
<br>matched: `representation learning`, `foundation model`, `multimodal`

> Physiological signals recorded during sleep provide synchronized views of neural, cardiac, respiratory, and other bodily systems, while preserving modality-specific information. Existing EEG and ECG foundation models already capture rich but distinct physiological structure, motivating an alternative to training a multimodal sleep model from scratch: composing existing pretrained models. We introduce SleepXA, a framework that uses synchronized polysomnography (PSG) to…

### 12. [From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.31063)
**Wenlong Yu, Bingxu Lu, Qilong Wang, et al.**  ·  `cs.MA`  ·  [abs](https://arxiv.org/abs/2611.31063) · [pdf](https://arxiv.org/pdf/2611.31063)  ·  relevance 24
<br>matched: `large language model`, `llm`, `agent`, `retrieval-augmented`, `interpretab`

> In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through intermediate messages and compromise final answers. However, outcome-based evaluation obscures how agents amplify, attenuate, or correct these errors. We propose Response-Aware Error Propagation among Agents (REPA), a structural model that connects measured local responses to system-level error propagation. REPA separately estimates input assembly and agent processing across…


<sub>Generated 2026-11-24 23:00 UTC via the arXiv API.</sub>

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
