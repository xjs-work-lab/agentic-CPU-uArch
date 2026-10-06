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
