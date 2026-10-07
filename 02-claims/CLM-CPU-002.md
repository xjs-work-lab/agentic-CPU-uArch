+++
id = "CLM-CPU-002"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "INFERENCE"
status = "SUPPORTED"
scope = "CPU matrix/local-AI viability"
supersedes = []
+++

# CLM-CPU-002

## Proposition
Existing CPU matrix acceleration can materially expand the CPU-local AI region, while optimization pressure can shift toward layout/data movement.

## Current interpretation
PAPER-052 and TOOL-012 provide separate supporting routes: SMEPilot shows substantial within-CPU matrix/operator-placement value across phone/PC/server platforms; TOOL-012 shows large real-phone SME2 gains and material data-movement share after acceleration.

## Boundary
SMEPilot's direct baseline is CPU inference, not an optimized smartphone NPU. Its reported energy and GPU comparison are on Apple M4 Pro. Therefore this claim supports CPU-local viability, not universal CPU superiority over NPU or end-to-end Agent value.

## Migration
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`

## Evidence-depth audit
EDP v1 revalidated 2026-10-07; CPU-vs-NPU interpretation narrowed, decision unchanged.
