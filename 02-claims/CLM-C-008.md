+++
id = "CLM-C-008"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "utility-accrual scheduling for mobile embedded real-time tasks"
supersedes = []
+++

# CLM-C-008

## Proposition
Application-specific time/utility functions can express graded task value under delay, and utility-aware schedulers can combine that information with resource constraints, energy concerns and low-value/infeasible-task abort decisions in mobile embedded systems.

## Evidence
PAPER-068 / ReUA and its TUF/utility-accrual lineage.

## Boundary
Foundational real-time/embedded task-model evidence.
This does not establish:
- automatic utility derivation from Agent semantic state;
- smartphone Agent SYSTEM_VALUE;
- modern heterogeneous SoC control;
- hardware/uArch necessity.