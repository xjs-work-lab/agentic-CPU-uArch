# PAPER-111 — Adaptive AI Agent Placement and Migration — FULL_10Q

## Q1 — Problem
Maintain mobile-user QoS by placing and migrating stateful LLM Agents across heterogeneous edge servers.

## Q2 — Relevance
An Agent carries memory, planning and tool state, so continuation is not fully stateless.

## Q3 — Hypothesis
Transferring only essential Agent state can lower migration overhead while preserving continuity.

## Q4 — Baseline
Generic edge placement/migration and full redeployment.

## Q5 — Mechanism
Target selection → Agent memory/config export → transfer → target initialization/import → source release → resume.

## Q6 — Experiment
AgentScope-based distributed implementation across globally distributed edge servers; reports lower delay/resource cost than baseline placement/migration policies.

## Q7 — Boundary
No smartphone endpoint executes the migration. No phone CPU/KV/cache/energy/thermal measurement.

## Q8 — Evidence
FACT: Agent memory/config can be migrated as portable software state.
INFERENCE: continuation maps directly to T5 + C.
NOT ESTABLISHED: a distinct phone-local continuation primitive.

## Q9 — Project impact
Strongest Agent-specific continuation evidence, but negative pressure on new uArch.

## Q10 — Next
Compare with generic KV/context migration and real product continuity.

Primary: https://arxiv.org/abs/2508.03345
