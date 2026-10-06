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

B-residual closeout:
- score preserved at 63.0;
- remains Conditional Strategic Reserve;
- not promoted to an active second Bet;
- no CPU/uArch promotion;
- merged via PR #6 after machine QA, semantic-fidelity review and independent GO;
- temporary migration branch deleted after merge.

## Reserve wave — active

### 1. R1 — NEXT

**Post-ready Continuation Timing**

Frozen V1 state:
- score: 55.5
- Conditional Strategic Reserve
- measurement hypothesis
- broad ready/release decoupling novelty killed
- no uArch promotion

Migration intent:
- preserve the narrow continuation-timing residual;
- preserve killed broad novelty;
- keep measurement evidence separate from strategic promotion;
- do not infer SYSTEM_VALUE without target-device evidence.

### 2. R2 — queued

**CPU Continuation Locality**

Reuse canonical CG-01 objects where semantically valid:
- VENDOR-001;
- ACT-QUALCOMM;
- CAP-QUALCOMM-ORYON-FLEX-CACHE.

Do not inherit CG-01 BENCHMARK state.

### 3. R3 — queued / blocked lineage

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
