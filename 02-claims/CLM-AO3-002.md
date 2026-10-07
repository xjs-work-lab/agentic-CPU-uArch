+++
id = "CLM-AO3-002"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "state lifecycle validity, version and provenance"
supersedes = []
+++

# CLM-AO3-002

## Proposition
As Agent state is revised, reused across episodes or served across model/adapter versions, correctness increasingly depends on explicit lifecycle information such as identity, version, dependency, provenance, validity and compatible-state inheritance.

## Boundary
Most direct mechanisms are runtime/protocol or server-GPU implementations; phone cross-engine physical-state propagation remains incomplete.