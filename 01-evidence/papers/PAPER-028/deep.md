# PAPER-028 — PBKV — FULL_10Q

## Q1 — Problem
Dynamic Agent workflows create KV reuse, but future Agent invocation order depends on runtime branches/loops, so LRU and static-DAG policies evict useful state.

## Q2 — Agent-specific relevance
The useful information is future workflow structure, not a new cache primitive.

## Q3 — Hypothesis
Multi-step prediction of future Agent calls should improve KV residency and prefetch under memory pressure.

## Q4 — Baselines
LRU on SGLang+HiCache and workflow-aware KVFlow.

## Q5 — Mechanism
Predictor fuses:
- topology-aware Agent embedding from a global call graph;
- attention over workflow-prefix history;
- semantic signal from the last prefill-token hidden state.

It emits multi-step future-Agent probabilities.
The runtime converts them into:
- retired-cache-first hierarchical eviction;
- reuse scoring;
- conservative prefetch using otherwise-idle GPU space/PCIe bandwidth.

## Q6 — Experiment
Server:
- 8× NVIDIA A6000 48 GB;
- NVLink;
- 128 virtual CPUs;
- 512 GB host memory;
- Qwen3-14B and Qwen3-32B.

Workloads:
- HoVer + LangChain;
- SWE-bench + AutoGen;
- FinanceBench + CrewAI.

Reported:
- up to 1.85× speedup over LRU on dynamic workflows;
- up to 1.26× over KVFlow on static workflow;
- up to 2.55× / 1.39× hit-rate improvement respectively;
- predictor ~350K parameters, batch-1024 prediction in ~1.56 ms;
- HoVer/LangChain 1K-trace training gives about 0.94 one-step and 0.77 three-step accuracy.

## Q7 — Artifact / limitations
Public arXiv paper; no official code repository was verified in this review.
No smartphone, battery, thermal or mobile-memory-tier experiment.
Predictor is workload-trained.
The paper does not cleanly isolate how much incremental value comes from semantic hidden state versus topology/history.

## Q8 — Evidence
FACT: rich software-visible workflow signals predict future reuse well enough to improve KV management.
INFERENCE: explicit semantic reuse hints must beat topology/history prediction, not LRU.
NOT ESTABLISHED: semantic hidden state is necessary, or that a phone cross-tier semantic contract adds residual value.

## Q9 — Project decision
PBKV materially raises the B4 baseline and closes broad future-reuse-prediction novelty.

## Q10 — Next
EXP-BR-001 must compare against a PBKV/CacheScout-class predictor before giving credit to semantic StateAffinity/ReuseHint.

## Decision footer
- SYSTEM_VALUE for server Agent KV management
- STRUCTURAL_SIGNAL only for phone transfer
- no B-residual promotion
