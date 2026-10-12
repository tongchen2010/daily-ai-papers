# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-12** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-12

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Amortized Counterfactual Prediction with Graph Neural Networks](https://arxiv.org/abs/2610.13724)
**Hendrik Stumpf, Francesco Quinzan**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13724) · [pdf](https://arxiv.org/pdf/2610.13724)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Counterfactual inference asks how an observed outcome might have differed under different circumstances, such as whether a patient would have recovered had they received a different treatment. Such questions arise whenever decisions depend on the outcomes of alternatives that were not observed. Answering counterfactual queries generally requires knowledge of the underlying causal structure, which is often unavailable in practice. A common approach is therefore to first…

### 2. [Acoustic Biomarkers for Alzheimer's Disease Detection from Spontaneous Speech](https://arxiv.org/abs/2610.12500)
**Anh L Tran, Arjee Javellana Restar, Bereket Kindo**  ·  `eess.AS`  ·  [abs](https://arxiv.org/abs/2610.12500) · [pdf](https://arxiv.org/pdf/2610.12500)  ·  relevance 29
<br>matched: `alzheimer`, `dementia`, `longitudinal`, `multimodal`

> Alzheimer's disease (AD) remains a major public health challenge, and early identification is crucial for timely intervention and care planning. Recent work has shown that speech-based digital biomarkers can capture subtle changes in vocal production, prosody, and timing that often precede or accompany cognitive decline. In this study, we investigate whether acoustic features extracted from spontaneous speech can reliably distinguish individuals with AD from healthy…

### 3. [Bridging Human and Model Attention: Explainability Analysis of CNN, Mamba, and ViT Architectures with Gaze-Based Validation](https://arxiv.org/abs/2610.12703)
**Marco Stefani, Edoardo Parpaiola, Matteo Bino, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.12703) · [pdf](https://arxiv.org/pdf/2610.12703)  ·  relevance 24
<br>matched: `transformer`, `medical imaging`, `interpretab`, `explainab`, `mamba`

> High-risk applications of deep learning require precise characterization of model decision-making. We conduct a systematic explainability evaluation across Convolutional Neural Networks (CNNs), Vision Transformers (ViTs), and Vision Mamba (ViM). Unlike predominantly qualitative studies, we quantify the alignment between model attention and human visual perception using eye-tracking ground truth. We formalize this comparison via a standardized normalization pipeline mapping…

### 4. [SmartSalesBench: A Resistance-Aware Multi-Turn Benchmark for Evaluating LLM Sales Agents](https://arxiv.org/abs/2610.12975)
**P N Bhargav Teja, Velpula Lokesh Reddy, Madhu Basumata, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.12975) · [pdf](https://arxiv.org/pdf/2610.12975)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `retrieval-augmented`

> We present SmartSalesBench, the first multi-turn conversational benchmark explicitly designed to evaluate large language model (LLM) sales agents against psychologically grounded, resistant buyer personas. Existing task-oriented dialogue benchmarks assume cooperative users and measure task completion; SmartSalesBench inverts this assumption, placing agents against personas programmed to resist and challenge across conversations of up to twenty turns. The benchmark includes…

### 5. [Retrieval-Augmented Multimodal Language Model with Heterogeneous Evidence Integration for Clinical Prognosis](https://arxiv.org/abs/2610.13510)
**Hamza Shafiq, Jialu Tang, Ting Dang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.13510) · [pdf](https://arxiv.org/pdf/2610.13510)  ·  relevance 21
<br>matched: `longitudinal`, `retrieval-augmented`, `multimodal`

> Clinical prognosis requires integrating structured measurements, physiological waveforms, longitudinal history, and population context. We introduce PRISM (Population-Retrieved Inference for Structured Multimodal Prognosis), a multimodal language model that combines per-feature numerical tokenization, recency-weighted aggregation of longitudinal ECGs, and a dual-modality population memory bank. Retrieval operates in representation space: the model receives mean-pooled…

### 6. [The Evidence Anchoring Boundary: Where Visual Interventions Matter and When They Help in Multimodal LLMs](https://arxiv.org/abs/2610.12981)
**Qiji Zhou, Junyi Hu, Peiyu Wang, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.12981) · [pdf](https://arxiv.org/pdf/2610.12981)  ·  relevance 21
<br>matched: `large language model`, `llm`, `multimodal`

> Visual interventions provide a training-free way to reduce hallucinations in multimodal large language models. However, an intervention may have little leverage at some layers and may damage a correct answer even when it changes the output. We investigate where visual interventions retain leverage and when they improve predictions. First, we apply the same visual-residual edit at successive decoder layers, matching its RMS strength across depth. Across six checkpoints from…

### 7. [CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits](https://arxiv.org/abs/2610.13064)
**Jiahang Sun, Zhiwei Shang, Zhipiao Liu, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13064) · [pdf](https://arxiv.org/pdf/2610.13064)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large Language Model (LLM) agents have demonstrated remarkable capabilities in tackling complex tasks through agentic workflows. However, manually designing these workflows is labor-intensive and lacks flexibility to adapt to diverse queries. While automated workflow optimization is a promising direction, existing methods often incur expensive API costs during training-phase feedback collection. Furthermore, they fail to adaptively reuse high-quality workflows, which creates…

### 8. [AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents](https://arxiv.org/abs/2610.13335)
**R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.13335) · [pdf](https://arxiv.org/pdf/2610.13335)  ·  relevance 18
<br>matched: `llm`, `agent`, `retrieval-augmented`

> Tool-using agents increasingly require a common substrate for building, training, evaluating, distilling, and maintaining agentic systems, yet existing tooling typically addresses these stages in isolation. We present AgentTune, a source-available Python library that provides a unified framework for developing and optimizing tool-using agents. At its core, AgentTune introduces a two-tier EventLog representation that preserves agent trajectories while supporting consistent…

### 9. [A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models](https://arxiv.org/abs/2610.13663)
**Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.13663) · [pdf](https://arxiv.org/pdf/2610.13663)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems…

### 10. [DRYLAB-Bench: Benchmarking the Biosecurity Risk of Agentic LLM Mutation Design](https://arxiv.org/abs/2610.13116)
**Yuzhen Wang, Chunxiao Li, Baichen Le, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.13116) · [pdf](https://arxiv.org/pdf/2610.13116)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> As large language models (LLMs) acquire advanced biological design capabilities, they offer substantial research benefits but simultaneously introduce severe dual-use risks, such as engineering enhanced pathogens or drug-resistant bacteria. While biosecurity frameworks recognize these threats, the actual risk of LLMs executing dangerous biological modifications remains unquantified, particularly when augmented with specialized biological design tools (BDTs). Existing…

### 11. [Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA](https://arxiv.org/abs/2610.13128)
**Wenlin Lin, Fanzhe Wei**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.13128) · [pdf](https://arxiv.org/pdf/2610.13128)  ·  relevance 18
<br>matched: `agent`, `retrieval-augmented`, `multimodal`

> Question answering over large heterogeneous document collections requires first finding the right passages and then reading them, yet current retrieval-augmented agents give one model both kinds of tools and let it schedule itself. We present KnowForge, a pipeline separated by job: a hybrid-retrieval knowledge-point index; a Locator agent that can only search; a code-scheduled bridge judge that forces the missing second hop; a typed, size-bounded evidence pool that merges…

### 12. [Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents](https://arxiv.org/abs/2610.13267)
**Lei Liu, Yunji Liang, Xiaowen Zhang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.13267) · [pdf](https://arxiv.org/pdf/2610.13267)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents are highly vulnerable to memory-poisoning attacks. Existing defenses primarily rely on external modules for either static memory isolation or continuous online auditing, resulting in low memory efficiency and high computational overhead. To address these limitations, inspired by neuroscientific mechanisms that weak reactivation can destabilize memories and induce decay in the absence of reinforcement, we propose an agent-intrinsic…


<sub>Generated 2026-10-12 21:44 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-08](digests/2026-08-08.md) — 12 papers

_…and 44 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
