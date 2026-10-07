# PAPER-109 — DevicesWorld — FULL_10Q

## Q1 — Problem
Evaluate Agent goals whose information, actions and final conditions span heterogeneous devices.

## Q2 — Relevance
Cross-device dependency and final-state maintenance are materially harder than single-device GUI execution.

## Q3 — Hypothesis
Frontier Agents should degrade when device roles, state and dependencies must remain coherent across environments.

## Q4 — Baseline
Single-device Agent execution plus ordinary orchestration glue.

## Q5 — Mechanism
Device routing, state transfer, role tracking, dependency management, final-state verification and cleanup.

## Q6 — Experiment
6,140 tasks across mobile, desktop and IoT. Five frontier Agent systems are evaluated; best success reaches 12.5%. About 28.7% of failed runs satisfy at least one scoring condition but miss the full task.

## Q7 — Limitations
No phone CPU state-migration, KV-transfer, battery or thermal measurement.

## Q8 — Evidence
FACT: cross-device Agent tasks remain difficult.
INFERENCE: product/platform support for cross-device continuation is valuable.
NOT ESTABLISHED: a new phone CPU continuation state.

## Q9 — Project impact
Strong T8 product signal; current mechanisms still map to C/PT-A/T5.

## Q10 — Next
Pressure-test against engineered orchestration and explicit Agent-state migration.

Primary: https://arxiv.org/abs/2607.13465
