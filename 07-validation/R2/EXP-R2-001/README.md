+++
id = "EXP-R2-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "SIMULATION_SUPPORT"
execution_state = "READY_FOR_PHONE_PMU_INPUTS"
title = "R2 strong-software plus generic-hardware locality break-even / kill test"
direction_ids = ["R2"]
tests_claim_ids = ["CLM-R2-EXP-001"]
input_source_ids = ["PAPER-008", "PAPER-049", "VENDOR-001", "VENDOR-017", "PATENT-020", "PATENT-021", "PATENT-022", "PATENT-023", "PATENT-024"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-R2-001 — Strong-baseline CPU locality kill test

## Comparison

### B4-locality-software
Role-aware pools, soft affinity / Preferred Cores, warm-core placement, cache-aware migration, runtime pinning/worker reuse and topology-aware scheduling.

### B4-locality-generic-hardware
Coherent/shared caches, system cache, flexible shared cache across heterogeneous cores and generic locality-friendly cache hierarchy.

### B5-locality
Perfect oracle for future continuation identity, exact hot-state reuse, best core/cache domain and timing.

### B6-Agent-specific
Only the residual beyond B4:
- Agent continuation identity / future semantic reuse;
- selective microstate preservation/placement if needed.

B6 receives no credit for value already captured by affinity or shared cache.

## Model
`R2_gain = CPULocalPenaltyShare × (1-SoftwareLocalityCapture) × (1-GenericHardwareCapture) × CandidateResidualRecovery × ConversionEfficiency - Overhead`

Reference assumptions intentionally favor R2:
- CandidateResidualRecovery = 75%;
- ConversionEfficiency = 90%;
- Overhead = 0.2%;
- target = 5%.

## Reference break-even
- SW50 / HW50 → ~30.81% raw CPU-local penalty;
- SW75 / HW25 → ~41.09%;
- SW75 / HW50 → ~61.63%;
- SW90 / HW25 → >100%.

Selected coarse-grid pass counts:
- SW50 / HW50 → 18/42;
- SW75 / HW25 → 12/42;
- SW75 / HW50 → 6/42;
- SW75 / HW75 → 0/42;
- SW90 / HW0 → 4/42;
- SW90 / HW25 → 1/42;
- SW90 / HW>=50 → 0/42.

## Required target-phone inputs
Measure:
1. continuation identity / role;
2. previous and next CPU/core/cluster;
3. suspension time / reuse distance;
4. CPU burst length;
5. L1I/L1D/L2/LLC miss deltas where exposed;
6. TLB miss rate;
7. branch-mispredict / frontend-stall proxies;
8. migration/context-switch count;
9. matched outcomes under default vs strong affinity/pooling vs warm/preferred-core placement vs generic shared-cache baseline where available;
10. SoftwareLocalityCapture, GenericHardwareCapture and B5 oracle headroom.

## Promotion
Only if B6 adds >=~5% meaningful performance/energy value beyond both B4 layers and the cause is CPU-local microstate.

## Boundary
No phone PMU result is fabricated.
No hardware/uArch promotion.

Exact frozen V1 experiment and pass-1 result are preserved in [deep.md](deep.md).
