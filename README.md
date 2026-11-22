# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-11-22** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-11-22

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [DeepQuest: From Knowledge Gaps to Scientific Discovery in Alzheimer's Disease](https://arxiv.org/abs/2611.26343v1)
**Chunbo Jiang, Yifei Chen, Beining Wu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.26343v1) · [pdf](https://arxiv.org/pdf/2611.26343v1)  ·  relevance 32
<br>matched: `alzheimer`, `dementia`, `cortical`, `longitudinal`, `agent`

> Automating experiments does not necessarily advance scientific understanding. Research agents must identify meaningful knowledge gaps, determine what available data can resolve, and assess whether their findings advance existing knowledge. We introduce DeepQuest, a knowledge-gap-driven AI scientist framework for Alzheimer's disease research. DeepQuest transforms unresolved questions from domain reviews into traceable, testable hypotheses and prioritizes them through data…

### 2. [SEEC: A Large-Scale Dataset and Benchmark for Self-Supervised External-Eye Representation Learning](https://arxiv.org/abs/2611.26386v1)
**George R. Nahass, Michelle Fleishaker, Sanjay Ganesh, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.26386v1) · [pdf](https://arxiv.org/pdf/2611.26386v1)  ·  relevance 24
<br>matched: `representation learning`, `self-supervised`

> External-eye photography captures clinically relevant periocular anatomy at low acquisition cost, yet no large-scale standardized resource exists for evaluating self-supervised external-eye representations. We introduce a 4.35-million-image Standardized External-Eye Corpus (SEEC) derived from fourteen heterogeneous public face datasets, together with a benchmark for external-eye representation learning. For evaluation, we provide held-out evaluation distributions,…

### 3. [Perfumer: A Large Language Model-based Agentic Framework Accelerating Structural Relaxation and Electronic Band Prediction for First-Principle Calculation](https://arxiv.org/abs/2611.26349v1)
**Zhiwei Li, Yuhao Zhou, Yikai Yang, et al.**  ·  `cond-mat.mtrl-sci`  ·  [abs](https://arxiv.org/abs/2611.26349v1) · [pdf](https://arxiv.org/pdf/2611.26349v1)  ·  relevance 24
<br>matched: `graph neural network`, `graph neural`, `large language model`, `agent`

> First-principles structural relaxation and band calculations require substantial computation and expertise. Here we present Perfumer, a large language model-based agentic framework that couples Quantum ESPRESSO with two predictive models. Across tested structures, pre-relaxation with Perfumer-relax model followed by QE refinement yielded a 2.75-fold overall speedup over QE alone. Perfumer-band model combines a periodic graph neural network with a latent Hermitian spectral…

### 4. [Reasoning-Trace Analysis Using Large Language Models for Interpretable Q-Matrix Construction](https://arxiv.org/abs/2611.26422v1)
**Jihong Zhang, Zijing Jin, Mingfeng Xue**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.26422v1) · [pdf](https://arxiv.org/pdf/2611.26422v1)  ·  relevance 21
<br>matched: `large language model`, `llm`, `interpretab`

> Large language models (LLMs) can generate Q-matrices for diagnostic classification models that approximate expert specifications, but evaluations have focused on the final matrices, leaving the basis of individual item-attribute assignments unexamined. This opacity limits the responsible use of AI in measurement. We propose Reasoning-Trace Analysis (RTA), a framework in which an LLM generates attribute-labeled reasoning steps through chain-of-thought (CoT) prompting and…

### 5. [One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617v1)
**Yuxin Jiang, Wenqiang Sun, Jiaqi Li, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.26617v1) · [pdf](https://arxiv.org/pdf/2611.26617v1)  ·  relevance 18
<br>matched: `self-supervised`, `transformer`

> Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and…

### 6. [Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence](https://arxiv.org/abs/2611.26492v1)
**Yanda Cheng, Bo Wen, Yuhao Lu**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2611.26492v1) · [pdf](https://arxiv.org/pdf/2611.26492v1)  ·  relevance 18
<br>matched: `large language model`, `multimodal`

> Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. We compare it with a keyword-and-negation rule baseline given the same reports and scores. Evaluation uses controlled report-score pairings from OpenI, with consistency labels derived…

### 7. [C-LiTE: A Lightweight Foundation Model for Cellular feature learning in Histopathology](https://arxiv.org/abs/2611.26316v1)
**Esha Sadia Nasir, Jiaqi Lv, Gozde N. Gunesli, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.26316v1) · [pdf](https://arxiv.org/pdf/2611.26316v1)  ·  relevance 17
<br>matched: `representation learning`, `self-supervised`, `foundation model`

> Characterising individual cells is fundamental to computational pathology, as cellular morphology informs tasks such as tumour grading, mitotic assessment and immune profiling. However, most pathology foundation models are trained on tissue patches and capture cellular features only implicitly, while existing cell-level models are either restricted to specific cell populations or rely on computationally expensive architectures with hundreds of millions of parameters.…

### 8. [How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents](https://arxiv.org/abs/2611.26361v1)
**K. R. Jayaram, Vatche Isahagian, Aswath Vaithinathan Aravindan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.26361v1) · [pdf](https://arxiv.org/pdf/2611.26361v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> LLM agents on long-horizon tasks fail in recurring, procedural ways. They mis-paginate an API, resolve the wrong entity, or answer when no answer was asked. We built a pipeline that lets an agent learn from its own history. It first mines short \emph{lessons} from the agent's own trajectories, one to three per episode. It then consolidates those lessons into a smaller set of \emph{guidelines}, where each guideline records how many lessons it merged. At inference the agent…

### 9. [Client Exits - A Way to Increase LLM Transparency on the Client Side](https://arxiv.org/abs/2611.26309v1)
**Marc Jansen**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.26309v1) · [pdf](https://arxiv.org/pdf/2611.26309v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `interpretab`

> Textual recommendations generated by large language models (LLMs) can be difficult to inspect. This paper introduces \emph{Client Exits}, a lightweight mechanism for enriching LLM responses while separating semantic intent from client-specific presentation. The model inserts predefined, machine-interpretable markers into its output, and the receiving client decides whether and how to realize the corresponding enrichments. This allows supplementary information to be presented…

### 10. [Training Vision Models for LLM-Driven Weight-Space Programming](https://arxiv.org/abs/2611.26408v1)
**Timo Ropinski, Sebastian Kranz**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2611.26408v1) · [pdf](https://arxiv.org/pdf/2611.26408v1)  ·  relevance 14
<br>matched: `transformer`, `large language model`, `llm`

> It has been demonstrated that, in certain settings, large language models can perform weight-space programming to directly modify the weights of neural networks. However, it is unknown how dedicated training of these networks can contribute to the successes of weight-space programming. We present a benchmark of LLM-driven weight-space programming on vision models, in which five LLMs edit convolutional networks and vision transformers on relabeling and error-correction tasks…

### 11. [Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)](https://arxiv.org/abs/2611.26553v1)
**Mengxiao Wang, Mahbub Alam, Kalyan Nakka, et al.**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2611.26553v1) · [pdf](https://arxiv.org/pdf/2611.26553v1)  ·  relevance 12
<br>matched: `large language model`, `llm`, `agent`

> Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the…

### 12. [The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception in Large Language Models](https://arxiv.org/abs/2611.26545v1)
**Md. Abdullah Al Zami, Suraiya Shanaz, Mahdi Hasan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2611.26545v1) · [pdf](https://arxiv.org/pdf/2611.26545v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Linear probes are the cheapest LLM lie detectors but often fail to transfer across kinds of lie. Label-free directions from honest and deceptive role-play are untested at 70B scale and on lies about knowledge, where a lie and an honest denial can be identical. We widen a published persona bank with roles that deny knowledge they have, plus honest counterparts. At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than…


<sub>Generated 2026-11-22 20:20 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-09-22](digests/2026-09-22.md) — 12 papers

_…and 85 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
