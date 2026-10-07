# Patent Direct-Claim Audit — R3 Core

Date: 2026-10-07
State: COMPLETE
Scope: PATENT-028 / PATENT-029 / PATENT-030

## Audit question
Does the current public claim text actually support CLM-R3-003:
> broad compiler/runtime scheduling hints and broad Agent workflow/topology-to-resource scheduling hierarchies are crowded prior-art territory?

## PATENT-028
Verified at claim level:
- compiler provides scheduling-hint information for a user-level thread;
- runtime scheduling takes the hint into account;
- scheduling is performed by a user-space scheduler;
- dependent claims further cover locality/work characteristics and related placement behavior.

Supported boundary:
generic compiler→runtime scheduling/locality hint interface.

Not supported:
Agent-native DemandState, Effect/Commit legality, target-phone D1/D2 value.

## PATENT-029
Verified at claim level:
- implicit semantic processing;
- Agent blueprint/workflow construction;
- task execution scheduling;
- node topology/communication analysis;
- node resource scheduling;
- RL-based multi-Agent decision-path optimization.

Supported boundary:
broad Agent workflow/semantics/topology → resource scheduling.

Important correction:
implementation fields in the specification are not promoted to independent-claim language.

## PATENT-030
Verified at claim level:
- upper planning Agent;
- intent→workflow/DAG;
- macro constraints;
- lower execution Agent and micro resource scheduling;
- resource-ready execution plan;
- feedback to planning layer.

Supported boundary:
planner→executor→resource scheduler hierarchy.

Not supported:
a target-phone CPU/uArch semantic hint or its incremental system value.

## Decision
CLM-R3-003 remains SUPPORTED, but the scope is deliberately broad and technical.

R3 remains:
- BLOCKED
- 48.5
- NOT_EVALUABLE
- no dedicated hardware program

This audit does not itself cause the block. The block is still driven primarily by unmet D0/D1/R1/R2 parent gates.

## Audit progress
Patent-linked current-roadmap set:
- total: 13
- audited: 3
- remaining: 10

Next: PATENT-032 / B-residual.
