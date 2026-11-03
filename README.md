# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-03** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-03

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Interpretable structural temperature scaling for calibrating graph neural networks and point-cloud segmentation](https://arxiv.org/abs/2611.00175)
**Chenyi Huang**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.00175) · [pdf](https://arxiv.org/pdf/2611.00175)  ·  relevance 46
<br>matched: `graph neural network`, `graph neural`, `gnn`, `segmentation`, `interpretab`

> Graph-aware calibrators make graph neural networks (GNNs) more trustworthy by predicting a temperature for each node, usually with auxiliary networks whose decisions are hard to inspect. We propose Interpretable Structural Temperature Scaling (ISTS), a twelve-parameter linear model that sets each node's temperature from named descriptors of its confidence, neighbourhood and closeness to labelled nodes, so every temperature traces back to descriptor contributions. ISTS…

### 2. [AdaptAD: Foundation Model Adaptation with Missing Modality Robustness for Alzheimer's Disease Staging Across the Disease Continuum](https://arxiv.org/abs/2611.00084)
**Dawa Chyophel Lepcha, Sophie A. Martin, Pierrick Coup\'e, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.00084) · [pdf](https://arxiv.org/pdf/2611.00084)  ·  relevance 32
<br>matched: `alzheimer`, `dementia`, `foundation model`

> Staging Alzheimer's disease (AD) across its continuum, from cognitively normal (CN) through mild cognitive impairment (MCI) to dementia from a single structural MRI remains difficult because 3-D networks overfit small cohorts, and FreeSurfer morphometry is often unavailable. We present AdaptAD, which reads a registered T1-weighted scan as 16 anatomically placed 2.5-D slices through the medial temporal lobe and adapts a frozen ImageNet-pretrained ViT-B/16 with low-rank…

### 3. [Omni-iEEG Planner: an open-source Python platform integrating multimodal neuroimaging and intracranial EEG data for epilepsy surgery research](https://arxiv.org/abs/2611.00018)
**Yuta Tanoue, Masaki Izumi, Yipeng Zhang, et al.**  ·  `physics.med-ph`  ·  [abs](https://arxiv.org/abs/2611.00018) · [pdf](https://arxiv.org/pdf/2611.00018)  ·  relevance 31
<br>matched: `neuroimaging`, `cortical`, `diffusion mri`, `multimodal`

> Multimodal intracranial EEG (iEEG) research for epilepsy surgery combines anatomical and functional imaging, implanted electrode locations, interictal biomarkers, and functional mapping--outputs produced by different applications and reconciled by hand before they can be viewed on the same anatomy. Omni-iEEG Planner is an open-source Python platform that brings these inputs into one patient coordinate frame for research data analysis. The workflow starts from the…

### 4. [A Surrogate Model for Variation-Aware Clock-Mesh Analysis and Design-Space Exploration using Graph Neural Networks](https://arxiv.org/abs/2611.01473)
**Muhammad Hadir Khan, Wajid Ali, Arya Thottiparambil Manikandan, et al.**  ·  `cs.AR`  ·  [abs](https://arxiv.org/abs/2611.01473) · [pdf](https://arxiv.org/pdf/2611.01473)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Clock meshes are widely used in high-performance VLSI systems to minimize skew and tolerate On-Chip Variation (OCV) in nanometer technologies. However, analyzing meshes is difficult because reconvergent paths and multi-source drivers prevent static timing analysis (STA) tools from handling mesh loops, making SPICE the industrial standard. SPICE simulations are accurate but slow, so clock-mesh synthesis relies on approximate models that overlook critical effects such as…

### 5. [Resilient Cell-Free MIMO ISAC Under Uncertainties: An Impairment-Aware Graph Neural Network Framework](https://arxiv.org/abs/2611.03054)
**Oways Alsoloh, Robert-Jeron Reifert, Aymen Khaleel, et al.**  ·  `eess.SP`  ·  [abs](https://arxiv.org/abs/2611.03054) · [pdf](https://arxiv.org/pdf/2611.03054)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Beamforming designs for integrated sensing and communication (ISAC) in cell-free multiple-input multiple-output (MIMO) systems face the challenge to stay reliable under uncertainties from both channel state information (CSI) as well as clutter. To this end, this paper proposes an impairment-aware heterogeneous graph neural network (GNN) framework for beamforming that obtains the CSI error level and the clutter covariance as edge features, which enables a single trained model…

### 6. [Predicting Cognitive Profiles from Structural MRI using Spatial Graph Representation Learning](https://arxiv.org/abs/2611.00113)
**Taslima Ferdaus Shuva, Md. Tanvir Rahman, Risala Tasin Khan, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.00113) · [pdf](https://arxiv.org/pdf/2611.00113)  ·  relevance 30
<br>matched: `neuroimaging`, `graph neural network`, `graph neural`, `gnn`, `representation learning`

> Predicting cognitive abilities from structural neuroimaging remains challenging due to the high dimensionality and geometric complexity of brain morphology. Conventional models typically flatten regional morphometry into tabular features, failing to explicitly represent spatial relationships. We propose a Spatial-Topological Graph Neural Network (ST-GNN) to predict four distinct cognitive phenotypes across large pediatric cohorts (N = 2,378 to 2,424). By projecting regional…

### 7. [Certifying Graph Neural Networks Against Label and Structure Poisoning](https://arxiv.org/abs/2611.03350)
**Lukas Gosch, Xichuan Chen, Yan Scholten, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.03350) · [pdf](https://arxiv.org/pdf/2611.03350)  ·  relevance 27
<br>matched: `graph neural network`, `graph neural`

> Robust machine learning for graph-structured data has made significant progress against test-time attacks, yet certified robustness to poisoning - where adversaries manipulate the training data - remains largely underexplored. For image data, state-of-the-art poisoning certificates rely on partitioning-and-aggregation schemes. However, we show that these methods fail when applied in the graph domain due to the inherent label and structure sparsity found in common graph…

### 8. [Efficient NPN Classification for Large Functions using Graph Neural Network](https://arxiv.org/abs/2611.00339)
**Chengdi Cao, Hanyu Wang, Wan-Hsuan Lin, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.00339) · [pdf](https://arxiv.org/pdf/2611.00339)  ·  relevance 27
<br>matched: `graph neural network`, `graph neural`

> Two Boolean functions are considered NPN equivalent if one can be transformed into the other by negating inputs, permuting inputs, or negating the output. Efficient NPN classification is valuable in fields such as logic synthesis, quantum computing, and information theory. However, exact NPN classification demands exhaustive enumeration of all possible input permutations and negations. Its complexity grows exponentially, making it impractical for larger functions with more…

### 9. [CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging](https://arxiv.org/abs/2611.01449)
**Yuxiang Wei, Lijing Zhu, Qizhen Lan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.01449) · [pdf](https://arxiv.org/pdf/2611.01449)  ·  relevance 27
<br>matched: `neuroimaging`, `large language model`, `llm`, `agent`

> Large language model (LLM) agents can autonomously run neuroimaging analyses from research questions to reported findings. Existing agentic systems use tools to check that code runs and reported values match its output, but rely on LLM judgment to decide which results warrant scientific reporting. We show that LLM judges endorse site-confounded findings even when the confound is presented as evidence. We present \textbf{CONFIRM}, a framework that separates running an…

### 10. [Learning to Group and Order: Cross-Instance Self-Supervised RL for Vision-Centric MLLMs](https://arxiv.org/abs/2611.00892)
**Songming Yang, Hong-Tao Yu, Xiu-Shen Wei**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.00892) · [pdf](https://arxiv.org/pdf/2611.00892)  ·  relevance 27
<br>matched: `self-supervised`, `large language model`, `llm`, `multimodal`

> Reinforcement learning (RL) post-training has become an important paradigm for improving multimodal large language models (MLLMs), especially with automatically verifiable rewards. Self-supervised visual pretext tasks provide such rewards without human annotations. However, existing methods mainly exploit within-instance structure, offering limited supervision for cross-instance discrimination and fine-grained comparison. We introduce Group-and-Order Self-Supervised…

### 11. [LLM-Enhanced Multimodal House Price Prediction using Structured, Textual, and Visual Features](https://arxiv.org/abs/2611.01615)
**Khandokar Md. Rahat Hossain, Souvik Das, Tahsina Hashem, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.01615) · [pdf](https://arxiv.org/pdf/2611.01615)  ·  relevance 26
<br>matched: `large language model`, `llm`, `agent`, `interpretab`, `multimodal`

> Accurate house price prediction is essential for real estate buyers, sellers, agents, and financial institutions. Traditional methods rely primarily on structured data, e.g., number of bedrooms, bathrooms, parkings, but they overlook rich contextual information embedded in textual descriptions and property photos. Previous deep learning approaches for house price prediction have fused multimodal data but they fall short to extract structured spatio-temporal and contextual…

### 12. [Stage-aware Multimodal Brain Graph Contrastive Learning for Neurodegenerative Disorder Diagnosis](https://arxiv.org/abs/2611.02771)
**Jingjing Zhou, Chenxuan Meng, Ciyuan Peng, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.02771) · [pdf](https://arxiv.org/pdf/2611.02771)  ·  relevance 24
<br>matched: `neurodegenerative`, `multimodal`

> Neurodegenerative disorders are characterized by their progressive nature, with distinct stages that require precise identification and tracking of progression trajectories for accurate diagnosis. However, existing diagnostic methods often fail to fully capture the unique brain patterns associated with different stages, limiting their ability to effectively target specific stages of the disorders. To address this issue, we propose a Stage-aware Multimodal Brain Graph…


<sub>Generated 2026-11-03 20:05 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-02](digests/2026-09-02.md) — 12 papers
- [2026-09-01](digests/2026-09-01.md) — 12 papers
- [2026-08-31](digests/2026-08-31.md) — 12 papers

_…and 66 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
