# PATENT-017 — Collaborative Workload Management — direct-claim audit

## Source
- US6591262B1
- Original assignee: IBM
- Priority: 2000-08-01
- Primary: https://patents.google.com/patent/US6591262B1

## Direct-claim result
Independent claim 1 centers on:
- a workload scheduler submitting work units;
- a workload manager allocating resources by service class;
- scheduler-supplied work-unit attributes indicating typical resource requirements;
- workload manager tuning resources using those attributes.

Claims 2–3 add observed resource-use statistics such as CPU, I/O, memory and service units.

## Important correction
The patent description/background discusses:
- deadline times;
- known/expected duration;
- detecting a job that starts after deadline minus duration;
- scheduler intervention for late jobs.

That is useful technical ancestry, but it is **not the independent-claim core**.

## Project decision
Do not use PATENT-017 as a direct-claim proof that LatestUsefulResume/latest-start scheduling is claimed.

Use it only as:
- workload/deadline scheduling ancestry;
- scheduler↔resource-manager information-sharing background.

R1's direct claim-level latest-start anchor is PATENT-018.

No FTO/legal conclusion.
