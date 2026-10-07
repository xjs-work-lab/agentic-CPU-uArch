# PAPER-047 — Decoupling Readiness from Release — FULL_10Q

## Q1 — Problem
Eagerly releasing every ready Agent turn can create too much irreversible queued work under contention and worsen workflow tail latency.

## Q2 — New-regime relevance
Agent workflows expose a real distinction between “dependency ready” and “turn released.”

## Q3 — Hypothesis
A workflow-level release scheduler that reasons about tail risk, estimated turn work and queue pressure should outperform eager release under contention.

## Q4 — Strongest baseline
Eager release. For this project, the paper becomes part of B4-release: generic software already has permission to defer ready work.

## Q5 — Mechanism
Inputs:
- ready turns;
- mean-CVaR tail-risk state;
- online turn-work estimates;
- queue pressure;
- released-but-unfinished work.

Actuators:
- select next ready turn to release;
- adapt released-work budget.

No Agent semantic LatestUsefulResume field is required.

## Q6 — Experiment
Real Agent execution traces from software-engineering tasks across multiple LLMs and arrival rates.

Reported:
- comparable to eager release under light load;
- up to 3.50× improvement in P95 workflow flow time under contention.

## Q7 — Artifact / limitations
Public arXiv preprint.
No official code artifact verified in this review.
Server/workflow latency setting; no smartphone energy, thermal, foreground-QoE or CPU microstate measurement.

## Q8 — Evidence
FACT: Ready≠Release is a useful Agent scheduling primitive.
FACT: substantial value is captured by generic software-visible workflow state.
NOT ESTABLISHED: explicit semantic LatestUsefulResume has zero incremental value.

## Q9 — Project decision
Broad R1 novelty is closed. The only surviving residual is semantic post-ready timing beyond B4-release.

## Q10 — Next
EXP-R1-001 must compare B6 semantic timing against this release-scheduler baseline on a target phone.

## Decision footer
- SYSTEM_VALUE for evaluated server Agent scheduling
- STRUCTURAL_SIGNAL for phone transfer
- R1 remains conditional reserve
