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

R1 closeout:
- score preserved at 55.5;
- remains Conditional Strategic Reserve / measurement hypothesis;
- broad ready/release decoupling remains killed as differentiated novelty;
- target-phone >=~5% semantic residual remains unproven;
- no uArch promotion;
- merged via PR #7 after graph QA, semantic-fidelity review and independent GO.

## Reserve wave — active

### 1. R2 — NEXT

**CPU Continuation Locality**

Frozen V1 state:
- score: 54.5
- Conditional Strategic Reserve
- phone-PMU measurement hypothesis
- broad generic locality mechanisms killed as novelty
- no hardware/uArch promotion without target-phone residual

Migration intent:
- preserve strong software-locality and generic shared/coherent-cache baselines;
- preserve the missing direct phone-PMU residual;
- reuse canonical CG-01 objects only where semantically valid;
- do not inherit CG-01 BENCHMARK state into R2;
- do not convert competitor-product evidence into proof of R2 SYSTEM_VALUE.

Canonical CG-01 objects available for reuse where justified:
- VENDOR-001;
- ACT-QUALCOMM;
- CAP-QUALCOMM-ORYON-FLEX-CACHE.

### 2. R3 — queued / blocked lineage

**uArch Semantic Hints**

Migrate blocked lineage last because it depends on lower-layer consumers already proving SYSTEM_VALUE.

## After reserve-wave completion

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
