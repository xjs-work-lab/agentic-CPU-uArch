+++
id = "CLM-CPU-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "mobile heterogeneous placement"
supersedes = []
+++

# CLM-CPU-001

## Proposition
For evaluated mobile LLM stages, the CPU↔NPU winner is stage/operator/shape and overhead dependent rather than universally NPU-first.

## Current interpretation
PAPER-009 directly measures CPU/NPU reversal between Prefill and Decode and quantifies communication/invocation/fallback costs.

## Boundary
Device/software-stack/model specific; not a universal CPU-over-NPU rule.

## Migration
- V1 baseline: `960abb4ef50a8f5b0bd357c067f08346025d`
- Transform: `STRUCTURAL_REPACK`
