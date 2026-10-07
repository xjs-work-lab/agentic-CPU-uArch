# PAPER-048 — Ask Early, Ask Late, Ask Right — FULL_10Q

## Q1 — Problem
When instructions are incomplete, the value of asking for clarification depends on when in a long execution trajectory the missing information arrives.

## Q2 — Agent relevance
This is direct evidence that semantic state has time-dependent value rather than a timeless binary validity flag.

## Q3 — Hypothesis
Different missing-information types should have different optimal timing windows.

## Q4 — Baselines
Never ask, ask at different forced trajectory positions, and natural unscripted model behavior.

## Q5 — Mechanism / control point
The experimental control variable is normalized trajectory position at which a ground-truth clarification is injected.

Information dimensions:
- goal;
- input;
- constraint;
- context.

## Q6 — Experiment
- 3 Agent benchmarks;
- 4 frontier models;
- 84 task variants;
- 6,000+ controlled runs;
- complementary 300 unscripted sessions.

Reported:
- goal clarification loses nearly all value after ~10% of execution;
- input clarification retains value to roughly 50%;
- deferring any clarification type beyond mid-trajectory degrades performance below never asking;
- cross-model Kendall tau indicates substantial consistency for shared task coverage.

## Q7 — Artifact / limitations
Paper states code/data will be publicly released; no artifact was verified in this review.
No target-phone system experiment.
Timing is normalized trajectory progress, not microsecond/millisecond post-ready scheduling slack.

## Q8 — Evidence
FACT: Agent semantic information can have sharply time-dependent utility.
INFERENCE: a semantic timing concept is plausible.
NOT ESTABLISHED: that this timing can be mapped to DependencyReady→LatestUsefulResume or produces phone energy/QoE gains.

## Q9 — Project decision
Supports R1's premise while enforcing a strict timescale-transfer boundary.

It does not overcome PAPER-047's strong generic software release baseline.

## Q10 — Next
EXP-R1-001 must measure actual post-ready semantic slack on phone and compare against B4-release.

## Decision footer
- strong semantic timing-window evidence
- no direct system-level or phone transfer
- no R1 promotion
