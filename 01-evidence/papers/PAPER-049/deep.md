# PAPER-049 — Affinity Tailor — FULL_10Q

## Q1 — Problem
Work-conserving load balancing spreads threads across cores and destroys cache, branch-predictor and prefetcher locality; hard pinning preserves locality but strands idle capacity.

## Q2 — New-regime relevance
This is generic multicore locality, not Agent-specific. That makes it a critical baseline for R2.

## Q3 — Hypothesis
Demand-sized, topologically compact soft affinity can preserve warm microarchitectural state while still allowing bursts onto other cores.

## Q4 — Baselines
Google's heavily optimized Linux CFS-based production scheduler and hard/static partitioning concepts.

## Q5 — Mechanism
- userspace estimates near-term CPU demand;
- assigns per-cgroup Preferred Cores;
- selects compact sets minimizing LLC-domain spread/interference;
- kernel treats Preferred Cores as a soft affinity hint;
- threads can escape when necessary to preserve utilization.

No Agent semantic contract is needed.

## Q6 — Experiment
Fleet deployment across thousands of Google machines and four server platforms over a week.

Reported:
- +12% geometric-mean per-CPU throughput on chiplet systems;
- +3% on non-chiplet systems;
- +3–7% per-GB throughput;
- P99 thread scheduling latency increases by as much as 17% in evaluated platforms, yet application throughput improves.

The paper attributes gains to reduced cross-LLC/main-memory traffic and better cache/prefetcher locality.

## Q7 — Artifact / limitations
Strong production operational evidence.
Not a reproducible smartphone experiment.
No Agent continuation trace, phone PMU, battery or thermal measurement.

## Q8 — Evidence
FACT: generic soft affinity can recover meaningful locality value in production.
FACT: preserving locality may be worth some extra scheduler queueing latency.
INFERENCE: R2 must beat topology-aware dynamic soft affinity, not default scheduler/hard pinning.
NOT ESTABLISHED: Agent semantics provide additional placement value on phones.

## Q9 — Project decision
Affinity Tailor materially strengthens B4-locality-software and narrows R2.

## Q10 — Next
EXP-R2-001 must measure residual phone cache/TLB/branch warmup after strong software affinity and generic shared/coherent-cache support.

## Decision footer
- SYSTEM_VALUE for generic datacenter locality scheduling
- STRUCTURAL_SIGNAL for mobile transfer
- no R2 promotion
