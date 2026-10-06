> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# PAPER-028 — Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management

## Source
- Paper: [Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management](https://arxiv.org/abs/2605.06472)
- Authors: Haoyu Zheng, Fangcheng Fu, Jia Wu, Binhang Yuan, Yongqiang Zhang, Hao Wang, Yuanyuan Zhu, Xiao Yan, Jiawei Jiang
- Affiliations: Wuhan University; Dameng Database; Shanghai Jiao Tong University; Macquarie University; HKUST
- Venue/status: arXiv preprint
- Year: 2026
- Artifact: Unknown / Not yet verified
- Target platform: server/GPU Agent workflow serving
- Project relevance: M3 Persistent Agent State Fabric; C1 StateAffinity/future-reuse semantics
- Priority: P0

## Q1 — What problem is the paper solving, and how does it map to smartphones?
**Answer:**  
**[FACT]** Dynamic Agent workflows share substantial context, but the future sequence of Agent invocations depends on runtime branches/loops, so LRU or static workflow cache management can evict KV entries that will be needed later.  
**[INFERENCE]** This maps to smartphones as a state-tiering problem: persistent Agents will also create state that is temporarily idle but likely to be reused after tools/UI/NPU phases.  
**Boundary:** the evaluated state is GPU KV cache, not phone CPU cache/TLB/predictor state.

## Q2 — Is the problem/new mechanism actually new?
**Answer:**  
**[OBSERVATION]** Prediction-guided cache management is not new generically. The Agent-specific contribution is combining dynamic workflow topology/history/semantic signals to forecast several future Agent invocations and translate that forecast into KV retention/prefetch policy.  
Classification: **Agentic-amplified**, not a new cache primitive.

## Q3 — What falsifiable hypothesis is being tested?
**Answer:**  
**[HYPOTHESIS]** Future Agent-workflow information predicts reuse better than recency/static-DAG baselines, and this additional information can improve end-to-end serving performance despite prediction error.  
A falsifier would be that LRU/KVFlow performs equivalently once memory pressure and overhead are controlled, or that prediction overhead/error cancels the benefit.

## Q4 — What is the research lineage / competing route?
**Answer:**  
Closest competing routes include:
- LRU / recency-based KV eviction;
- static workflow-aware KV management such as KVFlow;
- application-semantic/context reuse systems such as Parrot;
- runtime policy layers such as CacheSage / policy-driven Agent runtime;
- mobile KV tiering/reuse systems such as mzCache and Dynamic Flow, Static Graph.

**[INFERENCE]** For our project, PBKV is especially important because it occupies part of the semantic-future-reuse space that an early M3 formulation implicitly treated as whitespace.

## Q5 — What is the key technical mechanism / control point?
**Answer:**  
Information inputs:
- workflow transition structure;
- current workflow history;
- semantic/context signal;
- prediction confidence / future-step probability.

Decision:
- estimate reuse value of KV cache entries.

Actuators:
- retain;
- evict;
- prefetch.

Likely layer:
- Agent-serving runtime / memory manager, not CPU microarchitecture.

## Q6 — How is the experiment designed?
**Answer:**  
**[FACT]** The paper evaluates three workflow benchmarks and compares against LRU and the workflow-aware KVFlow baseline.  
**[FACT]** It reports up to 1.85× speedup over LRU on dynamic workflows and up to 1.26× over KVFlow on static workflows.

The workflow predictor fuses:
- topology-aware Agent embedding;
- attention over workflow-prefix history;
- a semantic signal from the served LLM's prefill hidden state.

On HoVer + LangChain with 1K training traces, the full predictor reports top-1 next-Agent accuracy:
- step 1: **0.935**;
- step 2: **0.848**;
- step 3: **0.771**.

A first-order Markov predictor reports:
- step 1: **0.752**;
- step 2: **0.555**;
- step 3: **0.295**.

The full system's predictor overhead is reported as ~1.56 ms for a batch of 1,024 predictions.

## Q7 — What data/artifact/reproducibility support exists?
**Answer:**  
Artifact/code: **Unknown / Not yet verified**.  
The paper is publicly available on arXiv.  
Reproducibility maturity: incomplete until artifact/configuration is verified.

## Q8 — Do the results actually support the hypothesis?
**Answer:**  
**[FACT]** Reported results support the claim that richer future-workflow prediction can improve KV management over selected baselines in the evaluated server environment.

However, an important Stage 14 limitation is now explicit:

**the paper does not provide a clean ablation isolating the incremental value of the semantic prefill signal from topology + workflow-history representation.**

The full predictor strongly beats first-order Markov, especially at longer horizons, but the gain cannot be attributed solely to semantic state.

**[INFERENCE]** PBKV therefore proves that rich workflow representation is useful, not that an explicit Agent semantic ABI is necessary.

## Q9 — What is the real contribution / technology control point for us?
**Answer:**  
**NARROW M3.**

This paper kills the broad novelty interpretation:
> Agent future semantics → identify future reusable state → retain/prefetch it.

That control pattern already exists for Agent KV cache.

It simultaneously strengthens the **Persistent Agent State Fabric** parent problem because it shows that Agent execution has future-reuse structure worth exploiting.

Residual M3/B questions become:
1. what information remains unavailable to a strong online workflow/history predictor;
2. can semantic validity/version/dependency prevent unsafe stale-state reuse;
3. does that semantic correctness information need to cross into smartphone S2/S3 physical-state management;
4. does any CPU-local state remain material after strong system/runtime baselines.

## Q10 — What should we do next?
**Answer:**  
- **KEEP** as a strong M3/C1 baseline.
- **NARROW** M3 from broad future-state retention to cross-tier/mobile + CPU-local residual.
- Include a predictor-only baseline in B4/B6-style StateAffinity experiments.
- Do not promote CPU-local retention to uArch candidate without direct mobile evidence.
- Revisit artifact/system details if PBKV materially enters Stage 14 scoring.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for server Agent KV management; STRUCTURAL_SIGNAL for mobile M3 transfer
- Decision impact: NARROW / REFRAME M3; strengthen Persistent Agent State Fabric parent problem
- Open questions: artifact; exact system configuration; mobile transfer; explicit semantics vs learned predictor
- Primary source: https://arxiv.org/abs/2605.06472
- Artifact: Unknown / Not yet verified
