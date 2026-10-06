+++
id = "EXP-A-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "READY"
title = "A strong-baseline DemandState residual test"
direction_ids = ["A"]
tests_claim_ids = ["CLM-A-001"]
input_source_ids = ["PAPER-056", "PAPER-058", "PAPER-060", "PAPER-063", "PAPER-064", "PAPER-065"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-A-001 — A strong-baseline DemandState residual test

## Decision question
Does B6-Demand / B6-Full retain >=~5% RequiredProgress/end-outcome value over B4-TX at matched foreground QoE with zero illegal cancellation?

## Baseline
B4-TX, including reconstructible upper-layer proxies for:
- program/control/data-flow and belief state;
- task-level script lowering;
- interaction criticality / dependency propagation;
- effect/commit legality and rollback scope;
- verification vulnerability / provisional work state;
- Agent workflow topology, future invocation distance / STE and reuse identity.

The test must credit DemandState/RequiredProgress only for value not reproduced by these proxies.

## State
READY / WAITING-FOR-DATA.

## Boundary
No new experiment has been executed during migration.

The frozen V1 engineering specification is preserved in [deep.md](deep.md).
