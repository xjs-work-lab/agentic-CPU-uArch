# PAPER-115 — CPU-Centric Agentic AI Execution — FULL_10Q

## Q1 — Problem + target mapping
The paper asks whether CPU/tool execution becomes a first-class bottleneck once LLM inference is embedded in Agent loops.

Target mapping:
AO-1 Execution Fabric, especially CPU orchestration/tool execution and CPU-GPU resource balance.

## Q2 — New-regime relevance
Agent-amplified.

The paper classifies Agent workloads on three system-relevant axes:
- LLM vs host orchestrator;
- static vs dynamic path;
- single-step vs multi-step repetition.

This taxonomy directly affects CPU/GPU demand over time.

## Q3 — Falsifiable hypothesis
If GPU inference remains the dominant bottleneck, moving to a much faster GPU should materially reduce end-to-end latency for all Agent workloads.

The paper shows multiple workloads where tool/CPU stages dominate and faster GPUs shift more of the bottleneck to CPU execution.

## Q4 — Strongest competing explanation
Tool-heavy applications are not unique to Agent systems.
The key Agent-specific amplification is the iterative interleaving of tools, orchestration and model calls.

The paper also demonstrates that software scheduling can recover much of the imbalance.

## Q5 — Mechanism / control point
Observed bottlenecks:
- CPU tool execution;
- CPU core oversubscription and context switching;
- LLC and I/O pressure;
- GPU KV/memory saturation;
- CPU and GPU active in disjoint phases;
- skewed admission between CPU-heavy and GPU-heavy requests.

Software mechanisms:
- COMB: CPU-aware capped micro-batches overlapped across CPU/GPU stages;
- MAS: request-type-aware CPU-heavy/GPU-heavy admission caps plus shared elasticity.

## Q6 — Experiment design + results
Platforms:
1. 64-core Intel Granite Rapids + RTX Pro 6000 Blackwell GPU + 512 GB DDR5.
2. 72-core Nvidia Grace + H200 GPU + 480 GB LPDDR5.
Additional ablation:
- 16-core Intel Emerald Rapids + RTX Pro 6000.

Five workloads:
- Toolformer;
- SWE-Agent;
- Haystack RAG;
- ChemCrow;
- LangChain web Agent.

Examples:
- Haystack ENNS retrieval roughly 81–89% of E2E latency in reported runs;
- LangChain LexRank summarization roughly 40–55%;
- ChemCrow heavy conformer generation roughly 85–88%;
- SWE-Agent Bash/Python roughly 25–65% depending on benchmark/system.

Throughput pressure:
- RAG retrieval saturates from LLC/disk contention;
- CPU-heavy tools saturate under core oversubscription;
- GPU inference can continue scaling better than CPU tools.

Reported optimization results:
- COMB up to about 3.9x lower service latency and 1.8x lower total latency under open-loop load;
- MAS protects minority request types, up to about 2.37x P50 / 2.49x P90 improvement;
- on a 16-core CPU ablation, simple micro-batching can outperform overlapped COMB in some regimes, showing CPU resource availability changes the best policy.

## Q7 — Artifact / limitations
Full paper and repeated-run methodology are public.
No smartphone hardware.
Workloads use large server CPUs/GPUs and several CPU tools not representative of every mobile Agent.
Some measured latency fractions are application/tool-specific.

## Q8 — Evidence vs hypothesis
FACT:
CPU/tool phases can be first-order E2E bottlenecks.

FACT:
the bottleneck can move toward CPU as GPU inference improves.

FACT:
CPU parallelization efficiency differs materially from GPU batching.

FACT:
software co-scheduling can recover substantial value.

NOT ESTABLISHED:
- smartphone fractions;
- need for new CPU microarchitecture;
- that the same tools run locally on phones.

## Q9 — Decision contribution
Supports AO-1 structural problem:
Agentic systems are heterogeneous workflows, not just LLM inference.

Also strengthens the software baseline:
resource-aware admission and overlapped CPU-GPU scheduling solve a meaningful portion without new hardware.

## Q10 — Next action
Use as cross-platform structural evidence, not direct mobile proof.
Prioritize mobile product/SoC evidence and mechanisms that reduce handoff/state/control overhead rather than generic CPU scaling.

## Decision footer
- Evidence maturity: SYSTEM_VALUE on evaluated servers; STRUCTURAL_SIGNAL for mobile transfer
- Decision impact: KEEP AO-1, strengthen CPU critical-path thesis, narrow hardware inference
- Open questions: mobile tool placement, SoC shared-memory interactions, orchestration overhead
- Primary source: https://arxiv.org/abs/2511.00739
