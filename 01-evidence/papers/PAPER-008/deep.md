# PAPER-008 — Architectural Implications of Agentic AI Workflows — FULL_10Q

## Q1 — Problem
Characterize how Agentic workflows change CPU/GPU/system behavior when requests expand into model inference, tool execution and orchestration.

## Q2 — New-regime relevance
Agentic execution is structurally fragmented:
- host orchestration and tools sit on the critical path;
- CPU load is bursty;
- software roles differ;
- many Agents multiplexed on shared cores can lose cache/branch locality.

## Q3 — Hypothesis
Agent workflow structure creates resource/locality behavior distinct enough that uniform server allocation and generic placement are inefficient.

## Q4 — Strongest competing explanation
Ordinary service fragmentation and default scheduler behavior may explain much of the locality loss.

The paper itself tests this by implementing software remedies rather than new hardware.

## Q5 — Mechanism / control point
Agora:
- CPU harvesting with Agent/orchestrator hints and adaptive retreat;
- GPU consolidation/state prefetch;
- role-aware core pools;
- affinity/pinning to preserve locality;
- workload-dependent auto-tuning.

## Q6 — Experiment
Evidence combines:
- hyperscaler production study;
- controlled studies of representative open-source Agent frameworks;
- concurrency scaling.

Existing project extraction records:
- IPC roughly 1.2–1.6;
- backend stalls roughly 43–47%;
- L1D MPKI roughly 14–20;
- SWE-Agent involuntary context switches rising strongly as concurrency scales.

Agora reports:
- CPU harvesting recovers 95% of co-located standalone throughput with under 3% Agent slowdown;
- GPU harvesting frees about one-third of GPUs, +82% generation throughput and 2.5× lower tail latency;
- role-aware pooling: up to 46% lower tool CPU demand, 13% lower worst-case tool latency, 99% serving throughput retained.

## Q7 — Limitations
Datacenter/server workload and topology.
No commercial-phone PMU, battery, thermal or foreground-QoE measurement.
Server role fragmentation need not transfer quantitatively to mobile.

## Q8 — Evidence
FACT: Agentic server execution can generate real CPU locality/context-switch pressure.
FACT: substantial value is recoverable with software role/affinity controls on commodity hardware.
INFERENCE: phone R2 must compare against a strong software-locality baseline, not default scheduling.
NOT ESTABLISHED: phone Agent continuations retain an irreducible CPU-local microstate penalty.

## Q9 — Project decision
PAPER-008 supports the R2 measurement hypothesis but blocks direct uArch promotion.

## Q10 — Next
Require target-phone EXP-R2-001 with matched software locality controls and generic shared-cache baseline.

## Decision footer
- STRUCTURAL_SIGNAL for R2 mobile transfer
- SYSTEM_VALUE for evaluated server Agent control
- no R2 promotion
