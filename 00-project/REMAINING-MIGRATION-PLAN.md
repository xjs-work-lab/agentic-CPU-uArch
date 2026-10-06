# Remaining Migration Wave Plan

Updated: 2026-10-06  
Baseline: MIG-20261006-02  
Authority: planning record only

## Completed

1. A + CG-06 — CLOSED / GO
2. PT-A — CLOSED / GO
3. C — CLOSED / GO
4. CG-07 — CLOSED / GO
5. CG-01 — CLOSED / GO
6. B-residual — CLOSED / GO
7. R1 — CLOSED / GO
8. R2 — CLOSED / GO

R2 closeout:
- score preserved at 54.5;
- remains Conditional Strategic Reserve / phone-PMU measurement hypothesis;
- broad generic locality novelty remains killed;
- target-phone >=~5% causal CPU-local residual remains unproven;
- CG-01 BENCHMARK state did not propagate into R2;
- no hardware/uArch promotion;
- merged via PR #8 after graph QA, semantic-fidelity review and independent GO.

## Reserve wave — active

### 1. R3 — NEXT / blocked lineage

**uArch Semantic Hints**

Frozen V1 state:
- score: 48.5
- BLOCKED
- no independent mechanism program
- D0 only SIMULATION_SUPPORT
- D1 strongly gated by software sufficiency
- R1/R2 hardware-specific parents are measurement-only
- no stable lower-layer consumer has SYSTEM_VALUE

Migration intent:
- preserve R3 as blocked lineage rather than accidentally reviving it as a candidate;
- preserve D0 / D1 / D2 separation;
- preserve the rule that hardware hints need a proven software-visible consumer first;
- preserve the dependency on SYSTEM_VALUE + SOFTWARE_INSUFFICIENCY;
- do not invent a new uArch mechanism merely to complete the migration.

## After R3

Before authority cutover:
1. run full-graph machine QA;
2. perform cross-slice semantic-fidelity review;
3. reconcile generated views and roadmap;
4. verify V1 frozen-baseline parity / intentional structural normalization;
5. record unresolved migration ambiguities, if any;
6. pass a separate Human Gate for authority cutover.

## Rule

Migration order is not strategic promotion.

Each Direction owns its own state even when evidence is shared.

V1 remains authoritative until explicit cutover.
