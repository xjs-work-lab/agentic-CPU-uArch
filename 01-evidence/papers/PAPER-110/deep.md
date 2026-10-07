# PAPER-110 — UFO³ — FULL_10Q

## Q1 — Problem
Make cross-device Agent workflows robust, parallel and recoverable.

## Q2 — Relevance
A mutable distributed task graph is a credible architecture for multi-device Agents.

## Q3 — Hypothesis
Explicit dependencies, persistent channels and adaptive graph updates improve completion and recovery.

## Q4 — Baselines
Sequential and simpler cross-device orchestration.

## Q5 — Mechanism
TaskConstellation DAG, explicit dependency edges, Constellation Orchestrator, persistent AIP channels and dynamic reassignment.

## Q6 — Experiment
NebulaBench has 55 tasks across 5 machines and 10 categories. Reported 83.3% subtask completion, 70.9% task success, average parallel width 1.72 and 31% latency reduction versus sequential execution.

## Q7 — Boundary
Main benchmark hardware is Windows/Linux/A100. Android integration exists but is not in the main evaluation. Persistent shared cross-device memory is future work.

## Q8 — Evidence
FACT: explicit cross-device orchestration has system value.
INFERENCE: measured variables are software-visible and C-class.
NOT ESTABLISHED: live phone inference-state migration.

## Q9 — Project impact
Raises strongest software baseline and narrows standalone T8 differentiation.

## Q10 — Next
Compare against explicit Agent memory migration and generic state-transfer systems.

Primary: https://arxiv.org/abs/2511.11332
Artifact: https://github.com/microsoft/UFO
