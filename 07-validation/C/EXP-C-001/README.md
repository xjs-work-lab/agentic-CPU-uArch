+++
id = "EXP-C-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "READY"
title = "C generic-vs-Agent-aware control-path residual matrix"
direction_ids = ["C"]
tests_claim_ids = ["CLM-C-EXP-001"]
input_source_ids = ["PAPER-009", "PAPER-051", "VENDOR-006"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-C-001 — Generic vs Agent-aware control residual

## Decision question
After strong generic runtime/accelerator tuning, is there still a reusable >=~5% Agent-specific control-path residual?

## Configuration ladder
- G0 — DEFAULT
- G1 — GENERIC_OPTIMIZED
- A1 — AGENT_AWARE_CONTROL

A1 does **not** use A's DemandState / REQUIRED-OPTIONAL-SPECULATIVE variable, keeping C distinct from A.

## State
READY / WAITING-FOR-DATA.

## Boundary
No experiment was executed during migration.

The exact frozen Stage16A matrix is preserved in [deep.md](deep.md).
