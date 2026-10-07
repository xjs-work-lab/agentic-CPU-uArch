+++
id = "EC-AO3-001-B"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SCOPE_LIMIT"
target_kind = "CLAIM"
target_id = "CLM-AO3-001"
warrant = "The state types and measured efficiency gains are heterogeneous: persistent semantic/action memory on a mobile workflow and KV/adapter state in a desktop-class GPU runtime have different capacity, reuse, legality and physical placement."
scope = "transfer from application memory and single-GPU KV to phone CPU/NPU/GPU physical state"
boundary = "Does not negate persistence or reuse; it limits any inference to a single physical state-fabric primitive."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-103"
locator = "Section 6.3 Snapdragon CPU-only Action Memory and Section 7 portability limits"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-104"
locator = "single RTX 3090-class GPU, adapter-version KV and no phone energy/thermal results"
+++

# EC-AO3-001-B

## Inference and role
**SCOPE_LIMIT** → CLM-AO3-001.

## Warrant
The state types and measured efficiency gains are heterogeneous: persistent semantic/action memory on a mobile workflow and KV/adapter state in a desktop-class GPU runtime have different capacity, reuse, legality and physical placement.

## Scope and counterweight
transfer from application memory and single-GPU KV to phone CPU/NPU/GPU physical state

## Boundary
Does not negate persistence or reuse; it limits any inference to a single physical state-fabric primitive.
