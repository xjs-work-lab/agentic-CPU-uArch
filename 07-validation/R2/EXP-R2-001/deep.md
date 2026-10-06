> Exact V1 R2 experiment specification and pass-1 result from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# Stage 15 — R2 CPU Continuation Locality Strong-Baseline Kill Test

Updated: 2026-10-05

## Goal

Test the last meaningful CPU-local reserve:

> after strong software affinity/pooling/placement and generic shared/coherent cache support, does Agent continuation locality still leave >=~5% phone performance/energy value?

## Baselines

### B4-locality-software
- role-aware pools;
- soft affinity / preferred cores;
- warm-core placement;
- cache-aware migration;
- runtime pinning / worker reuse;
- topology-aware scheduling.

### B4-locality-generic-hardware
- coherent shared caches;
- shared LLC/system cache;
- flexible shared cache across heterogeneous cores;
- generic locality-friendly cache hierarchy.

### B5-locality
Perfect oracle:
- future continuation identity;
- exact hot-state reuse;
- exact best core/cache domain;
- perfect timing.

### B6-Agent-specific
Only the residual mechanism beyond B4:
- Agent continuation identity / future semantic reuse;
- selective microstate preservation/placement if needed.

B6 receives no credit for value already captured by affinity or shared cache.

## Key quantities

- CPULocalPenaltyShare
- SoftwareLocalityCapture
- GenericHardwareCapture
- CandidateResidualRecovery
- ConversionEfficiency
- continuation reuse distance
- migration / context-switch density
- private/shared-cache miss deltas
- TLB / branch/front-end warmup deltas

## Pass-1 model

```
Gain =
CPULocalPenaltyShare
× (1 - SoftwareLocalityCapture)
× (1 - GenericHardwareCapture)
× CandidateResidualRecovery
× ConversionEfficiency
- Overhead
```

Reference favors R2:
- candidate recovery 75%
- conversion 90%
- overhead 0.2%

Key 5% break-even:
- SW 50%, generic HW 50% -> ~30.8% raw CPU-local penalty required;
- SW 75%, generic HW 25% -> ~41.1%;
- SW 75%, generic HW 50% -> ~61.6%;
- SW 90%, generic HW 25% -> >100%, impossible under reference assumptions.

See:
`analysis/stage15_r2_locality/results/r2-locality-kill-pass1.md`

## Promotion gate

Promote R2 above conditional reserve only if target-phone PMU evidence shows all:
1. repeated short/medium-gap Agent continuations;
2. material CPU-local cache/TLB/branch warmup penalty;
3. software affinity/pooling/warm-core controls leave substantial residual;
4. generic shared/coherent cache still leaves substantial residual;
5. an Agent-specific mechanism adds >=~5% meaningful performance/energy value;
6. residual repeats across representative Agent workloads;
7. cause is CPU-local microstate, not S2/S3 model/KV/memory pressure.

## Kill / further downgrade

If:
- CPU-local penalty share is small;
- software capture is ~75–90%+;
- generic shared cache/coherence captures most remaining cross-core cost;
- continuation reuse distance is too long for private microstate;
- NPU/model/runtime state dominates;
- phone PMU cannot establish causality;
- any benefit is generic workload locality rather than Agent-specific.

## uArch gate

Blocked until:
- target-phone SYSTEM_VALUE;
- SOFTWARE_INSUFFICIENCY;
- hardware-specific cause;
- Direct claim review of decision-critical locality patents;
- product economics.


---

# Stage 15 R2 — CPU Continuation Locality Strong-Baseline Kill Test, Pass 1

Date: 2026-10-05

## Question

After strong software locality control **and** generic shared/coherent cache support, can an Agent-specific CPU-local continuation mechanism still plausibly add >=5% meaningful performance/energy value?

This is not:
- default scheduler vs pinning;
- cold core vs warm core;
- private cache vs shared cache.

Those are strong generic baselines or already productized/prior art.

## Strong baseline

### Software locality baseline
Include:
- role-aware CPU pools;
- task/core affinity;
- soft affinity / Preferred Cores;
- warm-core placement;
- cache-aware migration;
- runtime pinning / worker reuse;
- topology-aware placement.

Direct pressure:
- PAPER-008 / Agora: role-aware pooling + pinning cuts tool CPU demand by up to ~46%, worst-case tool latency by ~13%, while retaining ~99% serving throughput.
- PAPER-049 / Affinity Tailor: production soft-affinity scheduling reports geomean per-CPU throughput gains of 12% on chiplet systems and 3% on non-chiplet systems.

### Generic hardware locality baseline
Include:
- cache coherence;
- shared LLC/system cache;
- flexible shared cache across heterogeneous cores;
- generic cache-aware hardware policies.

Direct mobile product signal:
- Qualcomm Oryon Flex Cache explicitly allows heterogeneous cores to access one dynamically allocated cache pool and markets this for Agentic multi-step work/core handoff.
- Arm CSS for Mobile 2 exposes coherent, QoS-aware system interconnect and system-level mobile data-movement support.

These are not independent measurements of R2 value, but they must be part of the baseline.

## Model

```
R2_gain =
CPULocalPenaltyShare
× (1 - SoftwareLocalityCapture)
× (1 - GenericHardwareCapture)
× CandidateResidualRecovery
× ConversionEfficiency
- Overhead
```

Reference is intentionally favorable to R2:
- CandidateResidualRecovery = 75%
- ConversionEfficiency = 90%
- Overhead = 0.2%
- target = 5%

## Reference break-even

Required **raw CPU-local penalty share** before locality controls:

| Software capture | Generic HW capture | Required CPU-local penalty share |
|---:|---:|---:|
| 25% | 0% | 10.27% |
| 25% | 25% | 13.70% |
| 25% | 50% | 20.54% |
| 50% | 0% | 15.41% |
| 50% | 25% | 20.54% |
| 50% | 50% | 30.81% |
| 75% | 0% | 30.81% |
| 75% | 25% | **41.09%** |
| 75% | 50% | **61.63%** |
| 90% | 0% | **77.04%** |
| 90% | 25% | >100% |
| 90% | 50% | >100% |

Interpretation:
if strong software captures 75% of locality loss and generic shared/coherent cache captures half of the remainder, the original CPU-locality penalty must account for ~61.6% of the meaningful end outcome before an Agent-specific mechanism can add 5% under favorable recovery assumptions.

## Coarse grid

Sweep:
- raw CPU-local penalty share: 5/10/20/30/40/60/80%
- software capture: 25/50/75/90%
- generic hardware capture: 0/25/50/75%
- candidate residual recovery: 50/75/100%
- conversion efficiency: 70/90%
- overhead: 0.2%

42 cells per software+generic-hardware band.

Selected 5% pass counts:
- SW 50% / generic HW 50%: **18/42**
- SW 75% / generic HW 25%: **12/42**
- SW 75% / generic HW 50%: **6/42**
- SW 75% / generic HW 75%: **0/42**
- SW 90% / generic HW 0%: **4/42**
- SW 90% / generic HW 25%: **1/42**
- SW 90% / generic HW >=50%: **0/42**

At SW 75% / generic HW 50%, passing cells require:
- raw CPU-local penalty 60–80%;
- and very strong candidate recovery/conversion.

## Evidence interpretation

### What strengthens R2
- PAPER-008 demonstrates real Agent CPU microarchitectural locality degradation on servers.
- Qualcomm Flex Cache provides a direct mobile product signal that cross-core handoff/locality is important enough to alter cache architecture.

### What weakens R2
- PAPER-008 also shows software pooling/pinning captures large value.
- PAPER-049 shows generic soft-affinity scheduling preserves caches/branch predictors/prefetchers at scale.
- Qualcomm's solution is generic shared cache, not Agent-tagged cache/TLB/predictor state.
- Arm mobile platforms already emphasize coherent, system-level data movement.
- No reviewed source provides direct smartphone Agent PMU evidence for L1/L2/LLC/TLB/branch-predictor continuation loss after these baselines.

## Decision

### Broad CPU-local mechanisms
Remain **KILL as novelty**:
- generic warm-core placement;
- generic cache-aware migration;
- generic cache/TLB/predictor save/restore;
- generic cache partitioning;
- generic shared-cache handoff.

### Narrow R2 residual
**NARROW / DOWNGRADE to conditional Strategic Reserve / phone-PMU measurement hypothesis.**

Surviving question:
> after strong software locality control and generic shared/coherent cache, do real smartphone Agent continuations still lose enough CPU-local cache/TLB/predictor state to create >=5% end-outcome value for an Agent-specific mechanism?

## Required phone evidence before any hardware work

Measure:
1. continuation identity / role;
2. previous and next CPU/core/cluster;
3. suspension time / reuse distance;
4. CPU burst length;
5. L1I/L1D/L2/LLC MPKI where exposed;
6. TLB miss rate;
7. branch misprediction / frontend stall proxies;
8. migration/context-switch count;
9. matched outcomes under:
   - default;
   - strong affinity/pooling;
   - warm/preferred-core placement;
   - generic shared-cache baseline where available;
10. **SoftwareLocalityCapture** and residual B5 oracle headroom.

Do not prototype an Agent cache/TLB/predictor structure before these measurements.

## uArch decision

**No promotion.**

R2 is now phone-PMU-gated.
A CPU-uArch candidate requires direct evidence that:
- CPU-local penalty is large on phone Agent workloads;
- strong software + generic hardware capture is insufficient;
- the residual is stable across workloads;
- a hardware-specific cause remains.
