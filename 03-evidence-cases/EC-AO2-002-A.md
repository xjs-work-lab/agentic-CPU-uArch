+++
id = "EC-AO2-002-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AO2-002"
warrant = "Cordon and Atomix independently make task-level authority, effect settlement and rollback explicit runtime abstractions rather than per-call behavior."
scope = "semantic transaction and progress-aware settlement mechanisms"
boundary = "Software/runtime implementations; no hardware requirement."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-117"
locator = "semantic transaction, lineage, shadow state, effect outbox, commit/abort"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-118"
locator = "epoch, scopes/effects, per-resource frontiers, seal/commit/abort/settle"
+++

# EC-AO2-002-A

## Inference
PAPER-117 plus PAPER-118 support CLM-AO2-002.

## Warrant
Cordon and Atomix independently make task-level authority, effect settlement and rollback explicit runtime abstractions rather than per-call behavior.

## Boundary
Software/runtime implementations; no hardware requirement.