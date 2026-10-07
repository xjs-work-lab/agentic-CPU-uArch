# Round 15A — AO-2 Evidence Skeleton Audit

Date: 2026-10-08
State: EVIDENCE_MAPPED

## Question
Do revision, speculation, cancellation and effect authority form a defensible mobile architecture opportunity after software/runtime and prior-art pressure?

## Deep-read anchors
- PAPER-013 Speculative Interaction Agents — prior FULL_10Q
- PAPER-032 Versioned Execution — prior FULL_10Q
- PAPER-116 Speculative Actions — FULL_10Q
- PAPER-117 Cordon — FULL_10Q
- PAPER-118 Atomix — FULL_10Q

## Patent boundary
- PATENT-033 CN120704926A — direct independent/dependent claim review
- PATENT-032 — prior direct-claim audit

## Result

### Structural change
KEEP.
Agent work can be useful before authority is final, and revision/speculation creates a real need for commit/discard/rollback/version semantics.

### Academic mechanism maturity
STRONG.
Cordon, Atomix and Versioned Execution show a converging family of task-level transaction/version abstractions: lineage, effect staging, authority, epoch/frontier progress, rollback/compensation and compatible-state inheritance.

### Strongest baseline
VERY STRONG SOFTWARE/RUNTIME.
These systems solve much of the correctness/control problem without new hardware.

### Prior art
HIGH pressure on broad multi-Agent prepare/commit/rollback/snapshot/failover novelty.

### Product signal
WEAK / NOT YET PUBLICLY ESTABLISHED as a distinct mobile architecture pattern.
This is a meaningful difference from AO-1.

### Surviving opportunity
Only the lower execution/state residual survives:
if speculative/revised Agent work occupies local xPU queues and derived state, cancellation, invalidation, selective inheritance and resource reclamation may become a new execution-fabric concern.

### Architecture hypothesis
OPEN, not productized and not proven hardware need.

## Decision
AO-2 = KEEP / HIGH-INTEREST ACADEMIC-LEAD OPPORTUNITY.
coverage_state = EVIDENCE_MAPPED.

## Next
Move Round 15A to AO-3 Persistent Agent State / Context Fabric.