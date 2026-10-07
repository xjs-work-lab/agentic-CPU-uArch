+++
id = "R2"
type = "DIRECTION"
record_state = "CURRENT"
title = "CPU Continuation Locality"
direction_class = "STRATEGIC_RESERVE"
investment_lane = "CONDITIONAL_RESERVE"
score_context = 54.5
evidence_maturity = "SIMULATION_SUPPORT"
maturity_scope = "Agentic server locality signal exists; strong software and generic mobile hardware baselines compress residual; direct target-phone PMU SYSTEM_VALUE is not established"
strongest_baseline = "B4-locality-software + B4-locality-generic-hardware"
related_claims = ["CLM-R2-001", "CLM-R2-002", "CLM-R2-003", "CLM-R2-004", "CLM-R2-005", "CLM-R2-006", "CLM-R2-007", "CLM-R2-EXP-001"]
related_capabilities = ["CAP-QUALCOMM-ORYON-FLEX-CACHE"]
+++

# R2 — CPU Continuation Locality

## 30-second decision
**Conditional Strategic Reserve / 54.5 / phone-PMU measurement hypothesis**

Broad generic locality mechanisms remain **KILL as differentiated novelty**.

Surviving residual:
> after strong software locality control and generic shared/coherent cache, do real smartphone Agent continuations still lose enough CPU-local cache/TLB/branch-predictor state to create >=~5% meaningful end-outcome value for an Agent-specific mechanism?

## Strong baseline

### B4-locality-software
Includes:
- role-aware CPU pools;
- task/core affinity;
- soft affinity / Preferred Cores;
- warm-core placement;
- cache-aware migration;
- runtime pinning / worker reuse;
- topology-aware placement.

### B4-locality-generic-hardware
Includes:
- cache coherence;
- shared LLC / system cache;
- flexible shared cache across heterogeneous cores;
- generic cache-aware hardware policies.

## Shared evidence, separate strategic state
R2 reuses:
- `VENDOR-001`;
- `ACT-QUALCOMM`;
- `CAP-QUALCOMM-ORYON-FLEX-CACHE`.

But R2 does **not** inherit CG-01's `BENCHMARK` action.

- CG-01 asks whether Flex Cache is a competitor gap worth benchmarking/adapting.
- R2 asks whether any **Agent-specific CPU-local residual** remains after that class of generic hardware plus strong software locality.

## Device-free pressure
Reference 5% break-even:
- SW 50% / generic HW 50% → ~30.81% raw CPU-local penalty required;
- SW 75% / generic HW 25% → ~41.09%;
- SW 75% / generic HW 50% → ~61.63%;
- SW 90% / generic HW 25% → >100% under the favorable reference assumptions.

At SW 75% / generic HW 50%, only **6/42** coarse cells pass; SW 75% / HW 75% passes **0/42**.

## Current lane
Phone-PMU measurement reserve only.
No hardware/uArch promotion.

## Promotion
Requires `EXP-R2-001` target-phone evidence showing:
- repeated short/medium-gap Agent continuations;
- material CPU-local cache/TLB/branch warmup penalty;
- incomplete software locality capture;
- incomplete generic shared/coherent-cache capture;
- >=~5% Agent-specific incremental value;
- repeatability across representative workloads;
- causal attribution to CPU-local microstate rather than S2/S3 model/KV/memory pressure.

## Hardware boundary
Do not prototype an Agent cache/TLB/predictor structure before the phone PMU residual survives.

Exact frozen V1 direction text is preserved in [deep.md](deep.md).


## Reserve Rescue — 2026-10-07

### PAPER-008 — Agentic architectural characterization / Agora
The paper gives strong Agentic server structural evidence:
- fragmented LLM/tool/orchestration execution repeatedly crosses CPU↔GPU boundaries;
- CPU utilization is bursty and the CPU is on the critical path;
- multiplexing Agent roles degrades microarchitectural locality.

But the same paper provides a strong software sufficiency baseline:
- role-aware core pools;
- task pinning/affinity;
- adaptive CPU harvesting;
- Agent-aware GPU-state prefetch/consolidation.

Reported role-aware pooling:
- tool CPU demand down up to 46%;
- worst-case tool latency down 13%;
- 99% serving throughput retained.

This is server evidence, not target-phone PMU SYSTEM_VALUE.

### PAPER-049 — Affinity Tailor
Google production deployment shows dynamic soft Preferred Cores can preserve spatial locality without hard partitioning:
- online workload-demand estimate;
- topologically compact preferred CPU set;
- kernel soft-affinity enforcement with burst escape.

Reported:
- +12% geomean per-CPU throughput on chiplet systems;
- +3% on non-chiplet systems;
- +3–7% per-GB throughput;
- P99 scheduling latency can increase up to 17%, yet aggregate application throughput still improves.

The result raises B4-locality-software substantially.

### Final R2 interpretation
Generic software already controls:
- role pools;
- task/core affinity;
- demand-sized preferred cores;
- topology/LLC placement;
- warm-domain reuse;
- adaptive escape for load.

R2 therefore survives only if target-phone PMU measurement shows an Agent-specific CPU-local microstate residual after those controls and generic shared/coherent-cache support.

No score, lane, maturity or hardware change.

### Evidence-depth state
R2 paper-depth debt: **0**.
Current-roadmap paper-depth debt: **0**.


## Patent direct-claim audit — 2026-10-07

### PATENT-020 — VERIFIED
Claim 1 directly binds branch-prediction state to process/context identity and loads state for a newly swapped-in context.

Conclusion:
generic context-specific branch-predictor state retention/restore is direct claim-level prior art.

### PATENT-021 — VERIFIED
Claims directly cover:
- tracking an execution entity's cache access pattern before switch-out;
- addresses/page/segment translation information;
- TLB/SLB/cache access;
- loading saved information on switch-in;
- restoring TLB/SLB/I-cache/D-cache footprint.

Conclusion:
generic cache/TLB/translation warm-state restoration is direct claim-level prior art.

### PATENT-022 — VERIFIED
Claim 1 directly covers:
- dividing cache into partitions;
- assigning each process a partition indicator;
- loading misses into the partition associated with the current process.

Conclusion:
generic process-associated cache partitioning is direct claim-level prior art.

### PATENT-023 — VERIFIED
Claim 1 directly covers:
- source/destination core selection from load;
- per-task cache misses and executed instructions;
- cache-miss ratio/MPKI;
- selecting the migrated task based on source/destination cache behavior.

Conclusion:
generic PMU/cache-aware task migration is direct claim-level prior art.

### PATENT-024 — VERIFIED / MOBILE-RELEVANT
Claim 1 directly covers:
- heterogeneous processor clusters with different shared-cache/performance characteristics;
- monitoring processor workload and task cache demand;
- weighted decision;
- task migration between clusters.

Dependent claim 23 explicitly covers smartphone/tablet portable devices.

Conclusion:
generic cache-demand-aware heterogeneous mobile scheduling/migration is direct claim-level prior art.

### R2 decision
CLM-R2-004 and CLM-R2-005 remain SUPPORTED.

The patents close broad novelty for:
- microstate restore primitives;
- cache partitioning;
- PMU/cache-aware migration;
- cache-demand-aware hetero-cluster placement.

They do **not** close the surviving R2 residual:
> whether future Agent continuation semantics contain predictive value beyond observed task/process identity, PMU/history, software affinity and generic shared/coherent-cache behavior on a representative phone.

No score, lane, maturity or hardware change.

### Evidence-integrity milestone
Patent audit 13 / 13 complete.
Paper-depth debt 0.
Evidence Rescue COMPLETE.
