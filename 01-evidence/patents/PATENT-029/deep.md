# PATENT-029 — Agent Decision Path Optimization Integrating Explicit Topology and Implicit Semantics — CN120409874A/B

## Source
- Publication/family: CN120409874A/B
- Assignee: Beijing Zhongshuruizhi Technology Co., Ltd.
- Earliest priority: 2025-07-03
- Primary source: https://patents.google.com/patent/CN120409874A/en
- Project relevance: C1
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
Multi-Agent workflows need to optimize execution paths while considering topology, dependencies, priorities and resource characteristics.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Agent-specific but not phone-CPU specific. Strong adjacent prior art for Agent graph semantics feeding scheduling.

## Q3 — How crowded is this prior-art space?
Increasingly crowded in 2025–2026. Agent DAG/topology plus resource/priority metadata is no longer open white space.

## Q4 — What is the control point of the independent claims?
**Direct claim review.**

Independent claim 1 directly recites a chain that includes:
- multimodal/document/knowledge processing;
- implicit semantic detection;
- building a user-demand Agent blueprint;
- building an Agent workflow;
- task-execution scheduling;
- explicit node-topology / communication-anomaly analysis;
- node resource scheduling;
- reinforcement-learning multi-Agent decision-path optimization.

This is direct prior art for a broad **semantic Agent workflow → task/resource/path scheduling** pipeline.

Important correction:
the often-cited task fields `priority / resource type / operation duration / upstream/downstream IDs` are described in the specification implementation; they are **not the independent-claim wording itself**.

## Q5 — What do dependent claims / embodiments add or narrow?
**Direct dependent-claim review.**

Claim 3 further narrows node resource scheduling around resource-status analysis, bottleneck-node identification, task migration, migration communication overhead and scheduling-path analysis.

Claims 9–10 narrow the RL decision engine and multi-level path optimization/conflict-priority process.

The direct claims still do not specifically recite:
- DemandState = required/optional/speculative;
- effect/commit safety;
- semantic useful-progress preservation under foreground QoE.

## Q6 — Is the disclosed mechanism technically implementable/productizable?
Yes as Agent orchestration/runtime software.

## Q7 — What do inventor / assignee / patent-family signals tell us?
Assignee appears specialized rather than a top mobile SoC vendor; technical overlap still matters regardless of prestige.

## Q8 — How does it overlap with Huawei / competitor public capability and our candidate?
Strong overlap with broad:
- Agent DAG;
- priority/resource type;
- dependency-aware scheduling.

Less direct overlap with demand/commit/discardability semantic ABI.

## Q9 — What is background IP vs residual / foreground opportunity?
Background:
- Agent semantic graph → resource-aware scheduling.

Residual:
- smallest stable semantic ABI;
- phone runtime/OS lowering;
- demand/commit/state-affinity semantics;
- proof of value below Agent runtime.

## Q10 — What should we do next?
- Keep as C1 narrowing evidence.
- Review independent claims before claiming specific semantic fields are open.
- Do not use “Agent DAG + resource annotations” as novelty.

## Decision footer
- Evidence role: **DIRECT_AGENTIC**
- Prior-art pressure: High
- Decision impact: NARROW C1
- Claim-review completeness: **Direct**
- Open questions: granted-claim evolution and enforceable scope; no legal/FTO conclusion
- Primary patent source: link above
