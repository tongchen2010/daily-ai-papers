# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-25** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-25

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries](https://arxiv.org/abs/2610.31467v1)
**Bayram Ayadi, Florian Geissler, Johanna Schmidhuber**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.31467v1) · [pdf](https://arxiv.org/pdf/2610.31467v1)  ·  relevance 18
<br>matched: `longitudinal`, `large language model`, `llm`, `retrieval-augmented`

> As wearable and digital health systems increasingly generate longitudinal physiological records, communicating these observations in patient-accessible language remains a significant challenge. Large Language Models (LLMs) offer a promising mechanism for translating structured clinical information into readable narratives, but this process may introduce semantic drift, where clinically precise meaning is distorted during simplification. We investigate evidence-grounded…

### 2. [PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video Generative Models](https://arxiv.org/abs/2610.31429v1)
**Taekoan Yoo, Wonkyung Jung, Kyunghun Kim, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.31429v1) · [pdf](https://arxiv.org/pdf/2610.31429v1)  ·  relevance 18
<br>matched: `generative model`, `llm`, `interpretab`

> World action models increasingly rely on pretrained video models assumed to capture physical dynamics for prediction, planning, and action generation. Existing evaluations assess plausibility, probe representations, or measure predictive surprise, but rarely identify which history-conditioned physical expectations conflict with observations. We introduce PhysTrace, a training-free framework aligning MLLM-generated, history-conditioned expectations with observed video windows…

### 3. [Evaluation of Uncertainty-Aware Multi-Software Ensembles for Hippocampal Segmentation](https://arxiv.org/abs/2610.31505v1)
**Gabriel Oliveira-Stahl, Anna Schroder, James Moggridge, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.31505v1) · [pdf](https://arxiv.org/pdf/2610.31505v1)  ·  relevance 17
<br>matched: `alzheimer`, `dementia`, `segmentation`

> Accurate hippocampal segmentation can be a useful tool for diagnosing and monitoring neurological conditions such as Alzheimer's disease and epilepsy. While numerous automated segmentation methods exist, their clinical adoption remains limited. Reliable uncertainty assessment can enhance trust and facilitate clinical translation. This study evaluates ensembles of five heterogeneous hippocampal segmentation methods - InnerEye, ASHS, FastSurfer, HippoSeg, and FreeSurfer -…

### 4. [On the Token Collapse Phenomenon in Textual Graph Soft Prompting](https://arxiv.org/abs/2610.31572v1)
**Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.31572v1) · [pdf](https://arxiv.org/pdf/2610.31572v1)  ·  relevance 16
<br>matched: `graph neural network`, `graph neural`, `gnn`, `llm`

> Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts. G-Retriever combines graph soft prompts with a verbalized description of the same graph to strengthen the textual prompt signal. We conduct an in-depth analysis of G-Retriever and uncover a pathological behavior we term token collapse. Across three…

### 5. [EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650v1)
**Qijin Zhang, Hanzhen Wang, Yuehan Zhao, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.31650v1) · [pdf](https://arxiv.org/pdf/2610.31650v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs…

### 6. [The Geometry of Metaphor: Probing and Steering Metaphor Representations in Large Language Models](https://arxiv.org/abs/2610.31520v1)
**Shihui Li, Mette Andersen, Martha Lewis**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.31520v1) · [pdf](https://arxiv.org/pdf/2610.31520v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `interpretab`

> Metaphor is a crucial aspect of human cognition. As such, we would like to understand how it is represented in large language models (LLMs) and how it might be controlled. We use mechanistic interpretability techniques to identify causal subspaces in a range of LLMs covering different architectures and sizes. We show that we are able to steer output on classification tasks across different parts of speech. We are also able to steer output on generation tasks, indicating that…

### 7. [AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack](https://arxiv.org/abs/2610.31404v1)
**Justin Tan, Miao Li, Ding Zhao**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2610.31404v1) · [pdf](https://arxiv.org/pdf/2610.31404v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose…

### 8. [AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents](https://arxiv.org/abs/2610.31366v1)
**Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian, et al.**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2610.31366v1) · [pdf](https://arxiv.org/pdf/2610.31366v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret,…

### 9. [Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash](https://arxiv.org/abs/2610.31351v1)
**Atharv Chandratre, Jai Datar**  ·  `cs.SE`  ·  [abs](https://arxiv.org/abs/2610.31351v1) · [pdf](https://arxiv.org/pdf/2610.31351v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Feature flags are runtime configuration mechanisms used for gradual feature rollouts, experimentation, and kill switches. Once a feature is fully rolled out, the flag and its gated code become technical debt and can introduce operational risk through inadvertently enabling dormant code paths. At DoorDash, over 56,000 feature flags span 623 repositories, with 1,659 currently stale as of May 2026, with internal estimates of one to two hours per manual cleanup. Existing…

### 10. [Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure](https://arxiv.org/abs/2610.31573v1)
**Pellegrino Casoria, Simon Pietro Romano**  ·  `cs.CR`  ·  [abs](https://arxiv.org/abs/2610.31573v1) · [pdf](https://arxiv.org/pdf/2610.31573v1)  ·  relevance 14
<br>matched: `large language model`, `llm`, `agent`

> In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these practices become routine, exposure to social engineering attacks becomes an operational certainty, demanding a shared framework for assessment and mitigation. We make…

### 11. [Cost-Aware Abstention for LLM-Based IT Ticket Classification](https://arxiv.org/abs/2610.31657v1)
**Sachin Gupta**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.31657v1) · [pdf](https://arxiv.org/pdf/2610.31657v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative…

### 12. [How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions](https://arxiv.org/abs/2610.31606v1)
**Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, et al.**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.31606v1) · [pdf](https://arxiv.org/pdf/2610.31606v1)  ·  relevance 12
<br>matched: `llm`, `retrieval-augmented`

> Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with one Yes/No or WH-question per document, were used. Retrieval combined dense embeddings, BM25, and cross-encoder reranking. Chunk sizes of 128 to 1024 tokens,…


<sub>Generated 2026-10-25 17:03 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-22](digests/2026-08-22.md) — 12 papers

_…and 57 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
