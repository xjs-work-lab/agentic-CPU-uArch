+++
id = "CLM-AO4-004"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "Strongest alternative baseline"
supersedes = []
+++

# CLM-AO4-004

## Proposition
The minimum fair baseline for a dedicated always-on Agent NPU combines CHRE-style sensing/batching, a trained lightweight no-action classifier and candidate compression, then CPU/shared-NPU/AP wake management before comparing a separate always-on domain.

## Boundary
PRPF reports GPU benchmark savings (not phone energy) and still has high multimodal failure; commodity AP/NPU power-state economics remain undocumented in this evidence set.
