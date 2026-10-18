# Daily AI/ML arXiv Digest

An automated pipeline that, **every day**, pulls the newest papers from
[arXiv](https://arxiv.org/) across machine learning, computer vision, NLP, and
medical/neuro imaging, ranks them against a research-interest profile, and
publishes a dated digest. It runs entirely on GitHub Actions — no server, no
manual step.

**Latest digest: 2026-10-18** · browse the full archive below.

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

# arXiv AI/ML digest — 2026-10-18

_The 12 most relevant new papers across `cs.LG`, `cs.AI`, `cs.CV`, `cs.CL`, `eess.IV`, `q-bio.NC`, ranked against a neuro-AI interest profile. Auto-generated._

### 1. [GNN-Guided Local Refinement for Efficient Layout Decomposition with DSA-MP](https://arxiv.org/abs/2610.22214v1)
**Yu Feng, Liyi Zhou, Haoyu Wang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.22214v1) · [pdf](https://arxiv.org/pdf/2610.22214v1)  ·  relevance 21
<br>matched: `graph neural network`, `graph neural`, `gnn`

> Multiple patterning lithography (MPL) has been widely used to improve lithography resolution in advanced nodes, but it faces cost limits as feature sizes shrink. Directed self-assembly (DSA) offers a cost-effective complement, extending the resolution of optical lithography to sub-10 nm and beyond. Integrating DSA into MPL (DSA-MP) further enhances the resolution of contact/via patterning. Nevertheless, growing design complexity exposes the limits of existing decomposition…

### 2. [Learning to Steer LLM Agents and Multi-Agent Systems](https://arxiv.org/abs/2610.22316v1)
**Leyang Shen, Yaxin Gong, Yang Zhang, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.22316v1) · [pdf](https://arxiv.org/pdf/2610.22316v1)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Large language model (LLM)-based agents and multi-agent systems increasingly tackle complex tasks through long-horizon tool use and inter-agent collaboration. However, these systems are prone to deviating from the overall goal as execution unfolds, which wastes execution resources and leads to undesired outcomes, a failure termed goal drift. In this work, we propose a steering agent that supervises execution on the fly and steers the system back on track when drift occurs.…

### 3. [Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273v1)
**Anikait Singh, Teresa Zhang, Yoonho Lee, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.22273v1) · [pdf](https://arxiv.org/pdf/2610.22273v1)  ·  relevance 18
<br>matched: `large language model`, `llm`, `agent`

> Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to…

### 4. [SurvICL: a Foundation Model for in-context Survival Analysis](https://arxiv.org/abs/2610.22242v1)
**Julie Alberge, Linus Bleistein, Judith Abécassis, et al.**  ·  `stat.ML`  ·  [abs](https://arxiv.org/abs/2610.22242v1) · [pdf](https://arxiv.org/pdf/2610.22242v1)  ·  relevance 15
<br>matched: `foundation model`, `survival analysis`

> Tabular foundation models (TFMs) now outperform gradient-boosted trees in classification and regression. Yet in survival analysis, which predicts when an event occurs from censored data, often on small clinical cohorts, we find that no existing TFM beats the half-century-old Cox model. We address this issue by introducing SurvICL, a TFM that predicts survival curves in-context. SurvICL is pretrained on purely synthetic datasets generated from a novel flexible…

### 5. [MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents](https://arxiv.org/abs/2610.22240v1)
**Huanyao Zhang, Jiepeng Zhou, Jiaye Lin, et al.**  ·  `cs.CV`  ·  [abs](https://arxiv.org/abs/2610.22240v1) · [pdf](https://arxiv.org/pdf/2610.22240v1)  ·  relevance 15
<br>matched: `agent`, `multimodal`

> Multimodal deep search is moving from short queries to long-horizon investigations that continually acquire evidence. However, training such agents remains constrained by limited challenging training questions and insufficient process feedback. We introduce MMSearch-OPD, combining controllable data refinement with joint reinforcement learning (RL) and on-policy distillation (OPD). Our Refine pipeline performs targeted expansion of reasoning chains derived from existing…

### 6. [Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions](https://arxiv.org/abs/2610.22138v1)
**Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.22138v1) · [pdf](https://arxiv.org/pdf/2610.22138v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> LLM systems increasingly rely on groups of agents that discuss, critique, and check one another, assuming that peers will catch individual errors. We test this assumption against a minimal adversary. In a ten-agent factual discussion, one or three adversarial agents repeatedly assert a plausible false answer. After each round we probe each benign agent's private answer through a separate call whose response is hidden from its peers, and we separately label its public stance…

### 7. [CART: Compatible Routing for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2610.22137v1)
**Ling-Xiang Zhang, Tao Hu, Da-Wei Zhou**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.22137v1) · [pdf](https://arxiv.org/pdf/2610.22137v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `multimodal`

> Multimodal Large Language Models (MLLMs) achieve strong performance through instruction tuning, yet real-world applications often require them to continually acquire new capabilities from sequential tasks, i.e., Multimodal Continual Instruction Tuning (MCIT). In typical MLLMs, a projector is employed to align visual representations with the language model. However, existing methods primarily protect the language model from forgetting while continuously updating the projector…

### 8. [Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization](https://arxiv.org/abs/2610.22127v1)
**Sekh Mainul Islam, Pepa Atanasova, Isabelle Augenstein**  ·  `cs.CL`  ·  [abs](https://arxiv.org/abs/2610.22127v1) · [pdf](https://arxiv.org/pdf/2610.22127v1)  ·  relevance 15
<br>matched: `large language model`, `llm`, `interpretab`

> Personalization of Large Language Models (LLMs) is increasingly important for user-centric applications, yet prior methods mainly adapt dense LLMs, whose polysemantic neurons, each encoding multiple unrelated concepts, hinder localizing the components behind personalization, and thus understanding and controlling it. We propose to personalize Mixture-of-Experts (MoE) LLMs, which sparsely route each token to a few specialized experts, reducing polysemanticity and enabling…

### 9. [PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents](https://arxiv.org/abs/2610.22124v1)
**Kshitij Mishra, Abhijith Sharma, Nils Lukas, et al.**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.22124v1) · [pdf](https://arxiv.org/pdf/2610.22124v1)  ·  relevance 15
<br>matched: `llm`, `agent`

> Modern agentic systems extend language models with external tools, enabling them to complete complex tasks through multi-turn interactions. As these agents are deployed in consequential settings, they are often constrained by policies governing pricing, privacy, confirmation, safety, and other requirements. However, existing evaluation methods leave a critical gap: capability benchmarks measure what agents can accomplish, while content-safety red-teaming measures harmful…

### 10. [CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty](https://arxiv.org/abs/2610.22292v1)
**Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel, et al.**  ·  `cs.LG`  ·  [abs](https://arxiv.org/abs/2610.22292v1) · [pdf](https://arxiv.org/pdf/2610.22292v1)  ·  relevance 14
<br>matched: `large language model`, `llm`, `agent`

> Large language models (LLMs) are becoming prevalent in scenarios where honesty is critical. However, despite alignment training, these models still exhibit dishonest behaviour, such as outputting claims that contradict some knowledge or are not supported by what is accessible in context. We introduce Continuous Adversarial Training for Consistent Honesty (CATCH), inspired by a method originally developed to robustly refuse harmful queries. CATCH trains the model towards an…

### 11. [X-RIC: An Agentic RAN-Intelligent Controller Benchmark for Enhancing Reinforcement Learning](https://arxiv.org/abs/2610.22269v1)
**Adhwaa Al-Chaab, Ayman Younis, Dario Pompili**  ·  `cs.AI`  ·  [abs](https://arxiv.org/abs/2610.22269v1) · [pdf](https://arxiv.org/pdf/2610.22269v1)  ·  relevance 14
<br>matched: `transformer`, `agent`, `interpretab`, `explainab`

> The O-RAN ALLIANCE introduces architectural flexibility through disaggregation and AI-driven control. While the RAN Intelligent Controller (RIC) enables centralized optimization, current AI approaches lack reasoning capabilities and explainability. We propose eXplainable RIC (X-RIC), a novel framework integrating agentic AI into O-RAN architectures. X-RIC combines reactive Reinforcement Learning (RL) with strategic agentic reasoning through: (i) automated Behavioral Cloning…

### 12. [Discovering state-of-the-art quantum circuits with large language models](https://arxiv.org/abs/2610.22367v1)
**Andi Gu, Alek H. Kemeny, Susanne F. Yelin, et al.**  ·  `quant-ph`  ·  [abs](https://arxiv.org/abs/2610.22367v1) · [pdf](https://arxiv.org/pdf/2610.22367v1)  ·  relevance 12
<br>matched: `large language model`, `llm`

> Significant efforts are currently being directed toward the implementation of large-scale quantum information processors, but realizing useful quantum advantage also requires the development of efficient quantum algorithms. While for many practical problems the dominant resource costs are associated with a small set of computational primitives, optimizing them in the quantum setting presents unique challenges, including a reversibility constraint absent from ordinary…


<sub>Generated 2026-10-18 16:31 UTC via the arXiv API.</sub>

---

## Archive

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
- [2026-08-21](digests/2026-08-21.md) — 12 papers
- [2026-08-20](digests/2026-08-20.md) — 12 papers
- [2026-08-19](digests/2026-08-19.md) — 12 papers
- [2026-08-18](digests/2026-08-18.md) — 12 papers
- [2026-08-17](digests/2026-08-17.md) — 12 papers
- [2026-08-16](digests/2026-08-16.md) — 12 papers
- [2026-08-15](digests/2026-08-15.md) — 12 papers

_…and 50 earlier digests in [`digests/`](digests/)._

---

<sub>Built by [Tong Chen](https://tongchen2010.github.io). MIT licensed. Paper
metadata © their authors, via arXiv.</sub>
