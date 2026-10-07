+++
id = "EC-AO2-005-A"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SUPPORT"
target_kind = "CLAIM"
target_id = "CLM-AO2-005"
warrant = "Cordon and Atomix explicitly identify correctness limits at mediation, metadata, opaque-effect and distributed/external transaction boundaries."
scope = "software transaction boundary limitations"
boundary = "These limits are primarily runtime/tool/distributed-system problems; they do not by themselves motivate microarchitecture."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-117"
locator = "mediated-operation boundary, opaque effects, released external effects and future host-runtime integration"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-118"
locator = "adapter bypass, scope/effect metadata sensitivity, frontier contract, distributed/irreversible endpoint limitations"
+++

# EC-AO2-005-A

## Inference
PAPER-117 plus PAPER-118 support CLM-AO2-005.

## Warrant
Cordon and Atomix explicitly identify correctness limits at mediation, metadata, opaque-effect and distributed/external transaction boundaries.

## Boundary
These limits are primarily runtime/tool/distributed-system problems; they do not by themselves motivate microarchitecture.