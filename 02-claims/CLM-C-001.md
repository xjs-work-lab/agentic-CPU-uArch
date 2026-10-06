+++
id = "CLM-C-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "generic mobile host/control-path baseline"
supersedes = []
+++

# CLM-C-001

## Proposition
Generic phone host/accelerator communication, scheduling, fallback and synchronization costs can be material.

## Current interpretation
PAPER-009 provides direct smartphone evidence that CPU↔NPU launch/communication/fallback economics can materially change the winner by stage.

## Boundary
This is generic control-path cost and must not be counted as Agent-specific C value.

## Migration
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
