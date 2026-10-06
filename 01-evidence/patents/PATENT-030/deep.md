# PATENT-030 — Workflow Scheduling Method Based on Layered Agent — CN121957815A

## Source
- Publication: CN121957815A
- Assignee: Wuhan University of Technology
- Earliest priority: 2026-01-19
- Primary source: https://patents.google.com/patent/CN121957815A/en
- Project relevance: M1 / C1
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
High-level intent/workflow planning and low-level resource scheduling operate at different timescales and information levels.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Agent-specific but platform-general. Highly relevant to our M1 planner→executor reframe.

## Q3 — How crowded is this prior-art space?
The broad hierarchy is now crowded enough that “planner Agent + execution Agent” should not be treated as novel by itself.

## Q4 — What is the control point of the independent claims?
**Direct claim review.**

Independent claim 1 recites a hierarchical Agent workflow-scheduling method including:
- an upper planning Agent and lower execution Agent platform;
- natural-language intent → workflow/DAG generation;
- macro planning/constraint setting;
- lower-agent micro resource scheduling;
- resource-ready execution-plan DAG;
- task-path splitting/allocation;
- execution feedback returned to the upper planning Agent.

This directly constrains broad novelty of `planner Agent → executor Agent → resource scheduler`.

## Q5 — What do dependent claims / embodiments add or narrow?
**Direct dependent-claim review.**

Relevant dependents include:
- upper planning Agent as an LLM Agent;
- computing-resource labels such as CPU/GPU/I/O/memory and deadline/processor constraints;
- claim 5: lower execution Agent as a DRL/PPO scheduler encoding DAG topology, task attributes and resource state;
- bottom resource manager embodiments such as Kubernetes/Slurm.

This is strong software/workflow scheduling prior art, but it does not directly claim a smartphone D0 semantic core of DemandState + Effect/Commit or the D1 permission-lowering boundary.

## Q6 — Is the disclosed mechanism technically implementable/productizable?
Yes as a hierarchical software runtime/control architecture.

## Q7 — What do inventor / assignee / patent-family signals tell us?
Academic assignee means product deployment is not implied, but novelty pressure remains technically relevant.

## Q8 — How does it overlap with Huawei / competitor public capability and our candidate?
Overlaps with broad M1 planner/executor hierarchy and C1 macro→micro semantic transfer.

## Q9 — What is background IP vs residual / foreground opportunity?
Background:
- planner/executor layering;
- macro constraints to micro resource scheduling.

Residual:
- the **specific CPU-sensitive lightweight executor/control substrate**;
- ASEC fields;
- smartphone implementation and quantitative value.

## Q10 — What should we do next?
- Use this as a mandatory M1 reframe prior-art anchor.
- Avoid claiming hierarchy alone as novelty.
- Deep claim review before final M1 novelty positioning.

## Decision footer
- Evidence role: **DIRECT_AGENTIC**
- Prior-art pressure: High
- Decision impact: NARROW M1/C1
- Claim-review completeness: **Direct**
- Open questions: prosecution/status evolution; no legal/FTO conclusion
- Primary patent source: link above
