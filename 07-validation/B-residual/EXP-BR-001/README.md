+++
id = "EXP-BR-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "SIMULATION_SUPPORT"
execution_state = "READY_FOR_PHONE_INPUTS"
title = "B-residual strong-baseline break-even / kill test"
direction_ids = ["B-residual"]
tests_claim_ids = ["CLM-BR-EXP-001"]
input_source_ids = ["PAPER-028", "PAPER-029", "PAPER-030", "PAPER-031", "PAPER-032", "PAPER-033", "PAPER-034", "PAPER-035", "PATENT-032"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-BR-001 — Strong-baseline break-even / kill test

## Comparison
### B4-safe-generic
- revision/version event known;
- versions/hashes/scoped provenance used where available;
- unchanged/proven-compatible artifacts preserved;
- unknown validity fails closed;
- stale reuse = 0.

### B6-cross-tier-lineage
Adds only:
- explicit S0/S1 semantic/workflow lineage to S2/S3 phone artifacts;
- additional conservative invalidation/preservation beyond B4;
- stale reuse = 0.

## Device-free result
At the frozen sensitivity sweep:
- generic safe-preservation capture 25%: **26/108** cells pass >=5%;
- 50%: **13/108**;
- 75%: **2/108**, both extreme regimes.

Therefore B-residual was narrowed/downgraded.

## Required phone inputs
- revision frequency;
- revision-weighted S2/S3 rebuild cost;
- affected-state fraction;
- GenericSafePreservationCapture;
- LineageCapture;
- RetentionSurvival;
- metadata overhead;
- stale-reuse correctness.

## Promotion
Only if B6 adds >=~5% meaningful matched-outcome gain over B4-safe-generic with stale reuse = 0 and benefit survives realistic phone memory pressure.

## Boundary
No CPU PMU/uArch fields are required at this stage.

Exact frozen V1 kill-test and pass-1 result are preserved in [deep.md](deep.md).
