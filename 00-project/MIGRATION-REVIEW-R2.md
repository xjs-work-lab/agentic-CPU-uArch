# R2 V2.2 Migration Slice — Independent Review

Updated: 2026-10-06  
Authority: review record only

## Review question

Does the R2 migration preserve the V1 conclusion that CPU continuation locality remains only a phone-PMU-gated conditional reserve after strong software locality and generic shared/coherent hardware baselines?

## Verdict

**GO**

Not authority cutover.

## Agentic locality signal

PASS.

PAPER-008 is used only to establish a server/datacenter Agentic CPU locality/context-switch signal:
- IPC/backend-stall/L1D-MPKI structure;
- context-switch growth under concurrency;
- role-aware pooling/pinning recovery.

Its magnitude is not transferred to smartphones.

## Software-sufficiency baseline

PASS.

PAPER-049 establishes a strong generic route:
- dynamic soft/permeable preferred cores;
- topology-aware compact placement;
- cache/branch/prefetcher warmth preservation;
- no Agent-specific semantics;
- no new CPU microarchitecture.

R2 therefore cannot compare against only default scheduling or hard pinning.

## Generic hardware baseline

PASS.

R2 reuses canonical:
- VENDOR-001;
- ACT-QUALCOMM;
- CAP-QUALCOMM-ORYON-FLEX-CACHE.

VENDOR-017 adds Arm CSS for Mobile 2 coherent system-level baseline.

Critical state separation is preserved:
- CG-01 = COMPETITIVE_GAP / BENCHMARK;
- R2 = STRATEGIC_RESERVE / CONDITIONAL_RESERVE.

No `competitive_action` field appears on R2.

## Prior-art boundary

PASS.

CLM-R2-004 is intentionally conjunctive:
- PATENT-020 → branch-predictor state restore;
- PATENT-021 → cache/TLB/translation trace restore.

Together they justify the broad microstate-restore family boundary.

CLM-R2-005 is intentionally conjunctive:
- PATENT-022 → cache partitioning;
- PATENT-023 → cache-aware task migration;
- PATENT-024 → cache-demand-aware heterogeneous scheduling.

Together they justify the broader cache placement/migration family boundary.

No legal/FTO conclusion is created.

## Device-free sensitivity

PASS.

Preserved reference thresholds:
- SW50/HW50 → ~30.81% raw CPU-local penalty required;
- SW75/HW25 → ~41.09%;
- SW75/HW50 → ~61.63%;
- SW90/HW25 → >100%.

Preserved pass-count pressure:
- SW75/HW50 → 6/42;
- SW75/HW75 → 0/42.

These remain **SIMULATION_SUPPORT**, not phone SYSTEM_VALUE.

## Negative-evidence safety

PASS.

CLM-R2-007 is a BOUNDARY Claim supported by DR-R2-STAGE15-GAP.

It states only that the reviewed frozen V1 set did not establish a causal target-phone >=~5% PMU residual after strong baselines.

It does not claim real-world or internal absence.

## Experiment state

PASS.

CLM-R2-EXP-001 remains OPEN.

EXP-R2-001 is:
- SIMULATION_SUPPORT;
- READY_FOR_PHONE_PMU_INPUTS;
- evidence target = SYSTEM_VALUE.

No target-phone PMU result is invented.

## uArch gate

PASS.

R2 does not become a hardware program.

Hardware/uArch promotion remains blocked until:
1. CPU-local penalty is material on representative phone Agent workloads;
2. strong software locality is causally insufficient;
3. generic shared/coherent hardware is causally insufficient;
4. residual is stable across workloads;
5. residual maps to CPU-local microstate rather than S2/S3 state;
6. Agent-specific mechanism adds >=~5% meaningful outcome value.

## Graph / CI

PASS.

QA:
- run `37469521784`
- job `112289035823`
- 206 nodes
- 342 canonical semantic edges
- 342 generated reverse edges
- graph projection PASS
- graph health PASS

## MIGRATION_AMBIGUITY

Unresolved:
**NONE**

## Decision

**GO — merge R2.**

Next after closeout:
R3 — uArch Semantic Hints / blocked lineage.
