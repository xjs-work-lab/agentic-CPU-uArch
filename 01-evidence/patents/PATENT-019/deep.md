# PATENT-019 — Task Scheduling Method and Electronic Device — direct-claim audit

## Source
- WO2026056682A1
- Assignee: Huawei Technologies
- Priority: 2024-09-14
- Primary: https://patents.google.com/patent/WO2026056682A1/en

## Direct-claim result
Claim 1 directly recites:
- a first thread executing on a first running unit;
- a second running unit with different performance in sleep;
- a migration condition including sustained load threshold;
- waking the second running unit;
- after wake, scheduling/migrating the first thread's task to the second unit.

The family is directly relevant to electronic/mobile heterogeneous processing and power/performance control.

## Project decision
This is a clean claim-level anchor for generic wake-before-migrate scheduling.

It does not claim the surviving R1 hypothesis:
intentional delay **after dependency readiness** based on Agent semantic LatestUsefulResume.

No FTO/legal conclusion.
