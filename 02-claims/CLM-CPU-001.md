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
For evaluated mobile LLM stages, the CPU↔NPU winner is stage/operator/shape, backend implementation and boundary-overhead dependent rather than universally NPU-first.

## Current interpretation
PAPER-009 directly measures a CPU/NPU reversal between Prefill and Decode in its Snapdragon 8 Gen 3 + llama.cpp/Hexagon stack and quantifies communication, lightweight-op invocation and fallback costs.

## Boundary
The Prefill CPU win is partly attributed by the source to Hexagon backend maturity, VTCM constraints and unsupported-op fallback. It is **not** evidence that Prefill is intrinsically CPU-owned or that the crossover survives a fully optimized future NPU stack.

## Migration
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`

## Evidence-depth audit
EDP v1 revalidated 2026-10-07; wording narrowed, decision unchanged.
