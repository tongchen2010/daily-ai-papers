# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-25** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-25

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [ST-GNN-AAAS: Spatio-Temporal Graph Neural Networks for Anytime Automatic Algorithm Selection in the Traveling Salesman Problem](https://arxiv.org/abs/2611.32602)
**Zeyu Zhang, Mustafa Misir**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.32602) · [pdf](https://arxiv.org/pdf/2611.32602)  ·  relevance 39
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Anytime Automatic Algorithm Selection (AAAS) aims to make solver choices under varying time budgets. The existing AAAS approaches largely rely on static instance characteristics and make limited use of temporal information revealed during solver execution. We propose ST-GNN-AAAS, a Spatio-Temporal Graph Neural Network framework for AAAS in the Traveling Salesman Problem (TSP). The framework represents evolving incumbent tours using time-varying node features, including…

### 2. [Analysis of Federated Graph Neural Networks for Predicting Nuclear Core Properties](https://arxiv.org/abs/2611.32509)
**Oliver Ko\v{z}ul, Mihailo Ili\'c, Julia Bartos, et al.**  ·  `cs.DC`  ·  [abs](https://arxiv.org/abs/2611.32509) · [pdf](https://arxiv.org/pdf/2611.32509)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Federated learning has grown in popularity owing to the increasing data privacy and safety concerns. It allows multiple parties to collaboratively train a model without exchanging their raw data. As an example of highly sensitive infrastructure of national importance, nuclear reactors benefit from this approach, where---while pooling multiple large datasets from different institutions could improve machine learning solutions---the confidentiality of the datasets is…

### 3. [Direct Conditioning of Audio Diffusion Transformers on fMRI Reveals Cortical Contributions to Sound Reconstruction](https://arxiv.org/abs/2611.12603)
**Matteo Ciferri, Tonio Weidler, Matteo Ferrante, et al.**  ·  `cs.SD`  ·  [abs](https://arxiv.org/abs/2611.12603) · [pdf](https://arxiv.org/pdf/2611.12603)  ·  relevance 30
<br>matched: `cortical`, `fmri`, `diffusion model`, `transformer`

> Reconstructing audio from brain activity remains challenging. Existing brain-to-audio pipelines typically map neural responses to predefined stimulus representations before synthesis. While recent work in the visual domain has explored direct conditioning on brain activity, this approach has not yet been extended to audio diffusion models. We introduce MAAS (Multi-Area Auditory Synthesis), an end-to-end framework that conditions a pretrained audio diffusion transformer on…

### 4. [CSC-Mamba: Bridging multimodal convolutional sparse coding and state space models for multi-contrast MRI super-resolution](https://arxiv.org/abs/2611.32144)
**Iman Marivani, David Van Hamme, Jan Aelterman, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.32144) · [pdf](https://arxiv.org/pdf/2611.32144)  ·  relevance 24
<br>matched: `interpretab`, `multimodal`, `state space model`, `mamba`

> Multi-contrast MRI super-resolution accelerates clinical protocols by reconstructing high-resolution (HR) target modalities from low-resolution (LR) inputs, guided by easily acquired reference contrasts. While purely data-driven deep neural networks achieve strong performance via rich representation capacity, they rely on heuristic fusion mechanisms (e.g., naive concatenation or black-box cross-attention) that lack theoretical grounding. Alternatively, model-based deep…

### 5. [A multimodal foundation model for tissue proteomics and morphology in cancer](https://arxiv.org/abs/2611.31451)
**Benedikt von Querfurth, Lukas Klein, C\'edric Vincent-Cuaz, et al.**  ·  `q-bio.QM`  ·  [abs](https://arxiv.org/abs/2611.31451) · [pdf](https://arxiv.org/pdf/2611.31451)  ·  relevance 22
<br>matched: `foundation model`, `transformer`, `segmentation`, `multimodal`

> Cancer diagnosis, prognosis, and treatment decisions increasingly rely on integrating tissue morphology with specific molecular readouts of the tumor and its microenvironment. H&E histopathology provides scalable morphology, whereas multiplex spatial proteomics quantifies dozens of proteins in situ with spatial context, but remains selectively deployed, often with different marker panels across cohorts. This creates a translational bottleneck: most patients lack high-depth…

### 6. [Scale-Robust and Global-Aware Representation Learning for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2611.32033)
**Gyuwon Lee, Saejoon Park, Won-Seok Hwang, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2611.32033) · [pdf](https://arxiv.org/pdf/2611.32033)  ·  relevance 21
<br>matched: `graph neural network`, `graph neural`, `representation learning`

> Multivariate time series anomaly detection (MTSAD) is an essential task for identifying abnormal system behaviors and supporting reliable operations across diverse real-world applications. Despite substantial advances in MTSAD, two key challenges in representation learning remain underexplored: (C1) how to learn scale-robust temporal representations that capture anomalies across different temporal scales and (C2) how to learn global-aware relational representations that…

### 7. [ASTERISM: Do Multimodal LLMs Actually Look at All the Images?](https://arxiv.org/abs/2611.32316)
**Chanseul Cho, Dongwoo Kim, Noori Bae, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.32316) · [pdf](https://arxiv.org/pdf/2611.32316)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multi-image benchmarks aim to test whether a multimodal large language model (MLLM) combines evidence across images, but many of their items can be answered from a single image. Across about 33k items from 19 public benchmarks, our audit and a two-stage single-image filter find that one image or the question alone settles 24.2% of them. On these items, MLLMs recover from one image a median 78% of the accuracy that all images add over the text alone, so these items reward…

### 8. [Clinical3D-Bench: Evaluating and Improving Spatial Intelligence of Multimodal LLMs in Hospital Environments](https://arxiv.org/abs/2611.32094)
**Yang Bai, Yingzhi Xia, Ling Lin, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.32094) · [pdf](https://arxiv.org/pdf/2611.32094)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Spatial reasoning in hospitals requires tracking look-alike equipment, interpreting patient-relative directions, and judging passage widths, yet existing benchmarks provide limited coverage of these abilities. We introduce Clinical3D-Bench, a simulated benchmark with 3,368 questions of eight types on egocentric walkthroughs of 373 hospital-room layouts. Layouts follow hospital design guidelines, answers are computed from the 3D scenes, and paired scene states test whether…

### 9. [C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems](https://arxiv.org/abs/2611.32780)
**Guowei Guan, Yurong Hao, Jiaming Zhang, et al.**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2611.32780) · [pdf](https://arxiv.org/pdf/2611.32780)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal large language models (MLLMs) are transforming recommender systems into content-aware decision systems. In these systems, multimodal compression and cross-modal fusion are often viewed as robustness-enhancing mechanisms against content manipulation, as compression can filter noisy signals and cross-modal consensus can suppress inconsistent anomalies. We challenge this assumption by showing that the same process can expose a compression-to-consensus (C2C) bias in…

### 10. [InCue: Making Better Use of What Multimodal LLMs Already See at Test Time](https://arxiv.org/abs/2611.31987)
**Shuwei Wu, Siyue Yu, Longin Jan Latecki**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.31987) · [pdf](https://arxiv.org/pdf/2611.31987)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Even when multimodal large language models (MLLMs) answer incorrectly, their internal cues often point to the relevant region. A widely used remedy re-presents the cue-selected region as an enlarged crop to supply finer detail. However, we find that much of its gain requires no new detail: it largely survives when the crop comes from the already-seen low-resolution input, and partly even when the region's cached tokens are merely copied. Part of re-presentation's gain thus…

### 11. [IMPACT-Seg: Consistent Anatomical Segmentation and Representation Learning Across CT, CBCT, and MRI](https://arxiv.org/abs/2611.32903)
**C\'edric H\'emon, Valentin Boussot, Matthew McCormick, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.32903) · [pdf](https://arxiv.org/pdf/2611.32903)  ·  relevance 21
<br>matched: `representation learning`, `segmentation`, `multimodal`

> Computed tomography (CT), cone-beam CT (CBCT), and magnetic resonance imaging (MRI) provide complementary representations of the same underlying anatomy, yet substantial differences in image appearance challenge consistent segmentation and deformable registration in adaptive radiotherapy. We investigate whether dense anatomical segmentation supervision can promote cross-modality correspondence without explicit feature alignment. We introduce IMPACT-Seg, which segments 126…

### 12. [Evaluating Latent Knowledge Stability in Multimodal Large Language Models](https://arxiv.org/abs/2611.32566)
**Chuancheng Shi, Shangze Li, Wenhua Wu, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.32566) · [pdf](https://arxiv.org/pdf/2611.32566)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Changes in image viewpoint and question formulation can alter latent knowledge representations in multimodal large language models (MLLMs). However, output correctness and overall representational drift provide limited insight into how these changes affect model decisions. We therefore evaluate latent knowledge stability across visual and linguistic elicitation conditions from two complementary perspectives: answer preference and internal support. Specifically, we devise the…


<sub>Generated 2026-11-25 22:32 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-24](digests/2026-09-24.md) — 12 papers

_…and 87 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
