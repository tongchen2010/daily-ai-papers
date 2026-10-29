# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-29** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-29

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [Multiple Leak Localization in Water Distribution Networks through Graph Neural Networks](https://arxiv.org/abs/2610.35972)
**Arvin Ajoodani, Sara Nazif, Pouria Ramazi**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.35972) · [pdf](https://arxiv.org/pdf/2610.35972)  ·  relevance 31
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Leak localization in water distribution networks is challenging when multiple leaks occur simultaneously, particularly under sparse monitoring. Existing data-driven methods often assume a single or predefined number of leaks or require extensive enumeration of leak combinations. This study proposes a graph neural network (GNN) model that localizes a variable number of simultaneous leaks without specifying the leak count in advance or exhaustively generating every possible…

### 2. [Interpretable Deep Learning Models for Breast Cancer Diagnosis Using Medical Imaging](https://arxiv.org/abs/2610.37026)
**Sami Alnawali, Muhammad Atif Saeed, Abdul Hadi, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.37026) · [pdf](https://arxiv.org/pdf/2610.37026)  ·  relevance 26
<br>matched: `transformer`, `medical imaging`, `interpretab`, `explainab`

> Deep learning shows promise for breast cancer diagnosis, but limited interpretability hinders clinical adoption. We benchmark ten ImageNet-pretrained models (ResNet50, VGG19, InceptionV3, DenseNet121, Xception, MobileNetV2, EfficientNet, ConvNeXt, ViT, and Swin Transformer) for benign-versus-malignant classification on the BreakHis histopathology dataset using a patient-level split, and explain their predictions with Grad-CAM, LIME, Integrated Gradients, and LRP. DenseNet121…

### 3. [How Reliable Is Individualized Functional-Network Attribution in Resting-State fMRI Cognitive Prediction in ADNI?](https://arxiv.org/abs/2610.37472)
**Sheethal Bhat, Mahfuzur Rahman Chowdhury, Imam Ahmed Shaik, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.37472) · [pdf](https://arxiv.org/pdf/2610.37472)  ·  relevance 23
<br>matched: `alzheimer`, `neuroimaging`, `fmri`, `interpretab`

> Individualized attribution estimates which functional networks drive a model prediction for a given subject and is often proposed as an interpretable resting-state fMRI (rs-fMRI) biomarker, but its test-retest reliability is rarely quantified. We evaluate per-subject network-ablation attribution for a frozen resting-state functional connectivity (FC) predictor (Schaefer-200 FC predicting MMSE/ADAS-Cog13) trained on N=875 subjects from the Alzheimer's Disease Neuroimaging…

### 4. [Ontology-guided multi-agent reasoning for explainable differential diagnosis](https://arxiv.org/abs/2610.36325)
**Roxana Ramona Szomiu, George Ursu, Adrian Groza**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.36325) · [pdf](https://arxiv.org/pdf/2610.36325)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `explainab`

> Effective differential diagnosis depends on well structured and unambiguous patient case descriptions, since incomplete or ambiguous clinical information readily leads to diagnostic errors and inconsistent reasoning. Large Language Models (LLMs) have recently shown promising capabilities in medical question answering and clinical reasoning; however, even when achieving competitive performance on medical benchmarks, they often rely on pattern recognition learned from training…

### 5. [OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning](https://arxiv.org/abs/2610.36335)
**Hui Yang, Jiaoyan Chen, Yongsheng Gao**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.36335) · [pdf](https://arxiv.org/pdf/2610.36335)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `retrieval-augmented`

> Large language models (LLMs) perform well across many real-world tasks but remain prone to hallucination, limiting their reliability in domains such as biomedicine and healthcare, where answers must be grounded in established knowledge. Retrieval-augmented generation (RAG) mitigates this problem by incorporating external information, but often overlooks logical relationships and relies heavily on the LLM's own reasoning, which can compromise answer faithfulness. We propose…

### 6. [Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation](https://arxiv.org/abs/2610.37242)
**Saiful Khan, Afrah Farea**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.37242) · [pdf](https://arxiv.org/pdf/2610.37242)  ·  relevance 21
<br>matched: `large language model`, `llm`, `agent`, `retrieval-augmented`

> Large language model (LLM) agents that call enterprise APIs must select the correct endpoints, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and therefore misses process and schema constraints. We address this limitation by integrating Open Data Protocol (OData) metadata and Business Process Model and Notation (BPMN) reference processes in a…

### 7. [LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction](https://arxiv.org/abs/2610.36433)
**Xianxiang Zhao, Advik Mehta, Falak Sethi, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.36433) · [pdf](https://arxiv.org/pdf/2610.36433)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`, `retrieval-augmented`, `multimodal`

> Construction safety management still struggles to produce daily safety bulletins (DSBs), structured daily communications that identify site-specific hazards, convey safety protocols, and set preventive measures for workers. Manual DSB creation takes 2-3 hours daily and yields inconsistent quality, with 25% of crews never conducting pretask planning (Olson et al., 2016), diverting safety personnel from field supervision. This study proposes the Lightweight Multi-Agent DSB…

### 8. [RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Document RAG](https://arxiv.org/abs/2610.36444)
**Zekai Chen, Hao Zhu, Yu Liu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.36444) · [pdf](https://arxiv.org/pdf/2610.36444)  ·  relevance 18
<br>matched: `agent`, `retrieval-augmented`, `multimodal`

> Web-based applications increasingly rely on understanding long multimodal documents, where answering questions often requires combining information across pages, tables, and figures. Agentic retrieval-augmented generation addresses these tasks through iterative retrieval and reasoning. However, Agentic execution is not always necessary, introducing additional computation and potentially incorrect answers. Our empirical analysis reveals that Agentic execution provides…

### 9. [CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](https://arxiv.org/abs/2610.36484)
**Kiant\'e Fernandez, Caitlin Chen, Jialu Zhou, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.36484) · [pdf](https://arxiv.org/pdf/2610.36484)  ·  relevance 18
<br>matched: `large language model`, `agent`, `multimodal`

> Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI agents can now complete online behavioral tasks and produce human-like data, which raises concerns that online datasets in the social and behavioral sciences are increasingly open to contamination. We…

### 10. [Proactive Memory for Event-Driven LLM Agents](https://arxiv.org/abs/2610.36967)
**Jinyang Li, Zichuan Fu, Xian Wu, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.36967) · [pdf](https://arxiv.org/pdf/2610.36967)  ·  relevance 18
<br>matched: `longitudinal`, `llm`, `agent`

> Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, providing limited support for validating recurring behavioral regularities and assessing their applicability to the current event. We propose Proactive Memory (ProactMem), which organizes history into recent events, temporal trajectories, and behavioral regularities. Trajectory facts are…

### 11. [AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations](https://arxiv.org/abs/2610.36980)
**Qiming Shi, Yikun Li, Beidi Luan, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.36980) · [pdf](https://arxiv.org/pdf/2610.36980)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution. Evaluating such agents requires going beyond individual transactions to ask whether decisions made online turn into sustained economic returns. We introduce AutoVend, a benchmark in which one LLM…

### 12. [Concordat: Typed Sessions for LLM Agents](https://arxiv.org/abs/2610.37461)
**Milad Sikaroudi**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.37461) · [pdf](https://arxiv.org/pdf/2610.37461)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Agents built on large language models are increasingly allowed to take consequential actions: cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions, such as "obtain the customer's explicit confirmation before changing anything", are usually stated in the prompt and followed only as reliably as the model chooses to follow them. We present Concordat, a Python library that treats an agent as an object whose interface is a finite-state…


<sub>Generated 2026-10-29 18:57 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-30](digests/2026-08-30.md) — 12 papers
- [2026-08-29](digests/2026-08-29.md) — 12 papers
- [2026-08-28](digests/2026-08-28.md) — 12 papers
- [2026-08-27](digests/2026-08-27.md) — 12 papers
- [2026-08-26](digests/2026-08-26.md) — 12 papers

_…and 61 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
