+++
id = "EC-AO3-002-B"
type = "EVIDENCE_CASE"
record_state = "CURRENT"
relation = "SCOPE_LIMIT"
target_kind = "CLAIM"
target_id = "CLM-AO3-002"
warrant = "Existing sources establish correctness metadata and software cache managers rather than an integrated CPU/NPU/GPU hardware coherence protocol."
scope = "scope of state lifecycle correctness mechanisms"
boundary = "Do not treat software version metadata as proof that fine-grained on-chip/DRAM derived artifacts can be managed at the same cost."
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-104"
locator = "version-aware KV manager and memory-pressure coordination on one GPU"
[[premises]]
ref_kind = "SOURCE"
ref_id = "PAPER-034"
locator = "vLLM-first sidecar capsules with deeper layer-frontier integration deferred"
+++

# EC-AO3-002-B

## Inference and role
**SCOPE_LIMIT** → CLM-AO3-002.

## Warrant
Existing sources establish correctness metadata and software cache managers rather than an integrated CPU/NPU/GPU hardware coherence protocol.

## Scope and counterweight
scope of state lifecycle correctness mechanisms

## Boundary
Do not treat software version metadata as proof that fine-grained on-chip/DRAM derived artifacts can be managed at the same cost.
