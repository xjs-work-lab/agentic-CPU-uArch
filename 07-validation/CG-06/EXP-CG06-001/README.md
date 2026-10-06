+++
id = "EXP-CG06-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "READY"
title = "CG-06 CPU↔NPU crossover experiment"
direction_ids = ["CG-06"]
tests_claim_ids = ["CLM-CG06-EXP-001"]
input_source_ids = ["PAPER-009", "PAPER-052", "TOOL-012", "TOOL-013"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-CG06-001 — CPU↔NPU crossover

## Decision question
Where does CPU-resident execution beat NPU offload for latency-critical Agent-relevant AI stages after dispatch, communication, fallback and layout costs are counted?

## Paths
- CPU-VECTOR
- CPU-MATRIX
- NPU

## State
READY / WAITING-FOR-DATA.

## Boundary
Existing hardware + compiler/runtime paths first. This is not a new-ISA experiment.

The exact V1 matrix is preserved in [deep.md](deep.md).
