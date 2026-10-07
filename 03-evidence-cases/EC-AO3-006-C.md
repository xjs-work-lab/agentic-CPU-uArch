+++
id = "EC-AO3-006-C"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SCOPE_LIMIT"
target_kind = "CLAIM"
target_id = "CLM-AO3-006"
warrant = "Oryon Flex Cache publicly describes CPU-core sharing and Hexagon describes NPU-local shared memory; neither establishes a direct versioned CPU↔NPU state-fabric mechanism or its latency/energy advantage."
scope = "product-to-hardware leap boundary"
boundary = "Disclosed memory capacity/sharing are relevant but not equivalent to persistent logical-Agent state lifetime/validity contract."
[[premises]]
ref_kind = "SOURCE"
ref_id = "VENDOR-001"
locator = "shared CPU-core Flex Cache architectural boundary"
[[premises]]
ref_kind = "SOURCE"
ref_id = "VENDOR-023"
locator = "NPU-shared-memory local boundary"
+++

# EC-AO3-006-C

## Inference and role
**SCOPE_LIMIT** → CLM-AO3-006.

## Warrant
Oryon Flex Cache publicly describes CPU-core sharing and Hexagon describes NPU-local shared memory; neither establishes a direct versioned CPU↔NPU state-fabric mechanism or its latency/energy advantage.

## Scope and counterweight
product-to-hardware leap boundary

## Boundary
Disclosed memory capacity/sharing are relevant but not equivalent to persistent logical-Agent state lifetime/validity contract.
