+++
id = "PATENT-030"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Workflow Scheduling Method Based on Layered Agent — CN121957815A"
primary_url = "https://patents.google.com/patent/CN121957815A/en"
priority = "P0"
evidence_role = "direct planner-Agent to executor-Agent/resource-scheduler hierarchy prior-art boundary"
origin_paths = ["04-patents/patent-10q/PATENT-030.md"]
origin_blobs = ["37d194277aa97c0cc6423401ef5b1a961c7d9bef"]
venue = "CN121957815A"
+++

# PATENT-030 — Layered Agent Workflow Scheduling

Direct claims cover upper planning Agent → lower execution Agent → resource scheduling / execution feedback.

**Decision use:** broad planner→executor→resource-scheduler hierarchy is not differentiated R3 novelty.

**Boundary:** does not establish a smartphone D2/uArch semantic-hint benefit; no legal/FTO conclusion.

Exact frozen V1 10Q is preserved in [deep.md](deep.md).


## 2026-10-07 direct-claim re-audit
**VERIFIED for project boundary use.**

Current public claim text supports the broad hierarchical pattern:
upper planning Agent → workflow/DAG and macro constraints → lower execution Agent / micro resource scheduling → execution feedback.

Dependent claim material further describes CPU/GPU/I/O/memory resource labels and DRL/PPO-style lower scheduling.

This supports a software/workflow prior-art boundary, not a finding that smartphone Agent-specific CPU/uArch hints are already solved or claimed.

No FTO/legal conclusion is made.
