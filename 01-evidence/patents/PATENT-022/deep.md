# PATENT-022 — Cache System for Concurrent Processes — direct-claim audit

## Source
- US6295580B1 / US6629208B2 family
- Primary: https://patents.google.com/patent/US6295580B1/en

## Direct-claim result
Claim 1 directly recites:
- a processor executing multiple processes;
- cache divided into partitions;
- a partition indicator associated with each process;
- cache refill placement determined by the current process's partition indicator.

Further claim language integrates the process/group identifier with address-space / translation handling.

## Project decision
This is a direct claim-level anchor for generic process-associated cache partitioning.

It does not claim:
- Agent future-reuse semantics;
- dynamic StateAffinity based on future Agent workflow;
- target-phone incremental value beyond generic cache policy.

No FTO/legal conclusion.
