# PAPER-112 — EdgeFlow — FULL_10Q

## Q1 — Problem
Move LLM continuation state across geo-distributed edge nodes under bandwidth/resource constraints.

## Q2 — Relevance
KV state is a large plausible in-flight context a cross-device Agent may need to preserve.

## Q3 — Hypothesis
Hybrid direct transfer plus activation-based recomputation can beat pure transfer or pure recomputation.

## Q4 — Baselines
Direct cross-node KV transfer and recomputation.

## Q5 — Mechanism
Hybrid migration plan with computation/communication overlap.

## Q6 — Experiment
Peer-reviewed IEEE ICDCS 2026 on a real distributed LLM inference platform; reports up to 45% lower migration time.

## Q7 — Boundary
Not Agent-specific, not smartphone-local and does not include tool/authority/postcondition state.

## Q8 — Evidence
FACT: optimized distributed KV-state migration already exists.
INFERENCE: KV handoff alone is not differentiated T8 novelty.

## Q9 — Project impact
Raises generic state-migration baseline.

## Q10 — Next
Require phone evidence for Agent-specific state beyond this baseline.

Primary: https://ieeexplore.ieee.org/document/11619197
DOI: 10.1109/2575-8411.2026.00033
