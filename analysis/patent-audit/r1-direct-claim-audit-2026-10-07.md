# Patent Direct-Claim Audit — R1

Date: 2026-10-07
State: COMPLETE

## Scope
- PATENT-005
- PATENT-017
- PATENT-018
- PATENT-019

## PATENT-005
DIRECT VERIFIED.
Claim 26 predicts I/O completion, compares it with known exit latency and issues a wake command.
Boundary: pre-completion predictive wake.

## PATENT-018
DIRECT VERIFIED.
Claim 1 computes earliest/latest start under dependencies/time constraints and derives movable/slack range for allocation.
Boundary: generic deadline/slack scheduling.

## PATENT-019
DIRECT VERIFIED.
Claim 1 wakes a sleeping heterogeneous execution unit before migrating/scheduling a thread task to it.
Boundary: generic wake-and-migrate.

## PATENT-017
CORRECTED.
Independent claims concern work-unit attributes exchanged between scheduler/workload manager for resource allocation.
Deadline-duration/latest-start behavior is in the specification/background, not the independent-claim core.

## Claim decision
CLM-R1-004 remains SUPPORTED, but evidence quality is now explicit:
- 3 direct-claim anchors;
- 1 specification/background ancestry source.

## R1 portfolio decision
Unchanged:
- CONDITIONAL_RESERVE
- 55.5
- SIMULATION_SUPPORT
- no uArch promotion

The narrow post-ready semantic timing residual remains outside these patents.

## Patent audit progress
8 / 13 complete.
5 remain, all R2.
