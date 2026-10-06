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
PAPER-052 and TOOL-012 provide separate supporting routes: SMEPilot shows matrix/operator-placement value across platforms; TOOL-012 shows large real-phone SME2 gains and ~40% data-movement share after acceleration.

## Boundary
Does not establish universal CPU superiority over NPU or end-to-end Agent system value.

## Migration
- V1 baseline: `960abb4ef50a8f5b0bd357c067f08346025d`
- Transform: `STRUCTURAL_REPACK`
