+++
id = "CLM-AO2-005"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "load-bearing software transaction boundary limitations"
supersedes = []
+++

# CLM-AO2-005

## Proposition
Current Agent transaction systems remain dependent on complete software mediation and correct metadata: opaque/bypassed effects escape rollback, incorrect scopes/effect classes can violate safety, hot resources may serialize, and atomic settlement across independent irreversible endpoints may require external transaction support.

## Boundary
These limitations primarily identify runtime/tool/distributed-system boundaries, not a proven microarchitecture bottleneck.