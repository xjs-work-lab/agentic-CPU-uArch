+++
id = "R3"
type = "DIRECTION"
record_state = "CURRENT"
title = "uArch Semantic Hints"
direction_class = "STRATEGIC_RESERVE"
investment_lane = "BLOCKED"
score_context = 48.5
evidence_maturity = "NOT_EVALUABLE"
maturity_scope = "D2 is blocked because D0 target-phone SYSTEM_VALUE and D1 software-insufficiency gates are not satisfied; R1/R2 hardware-specific parents remain measurement-only"
strongest_baseline = "D0/D1_SOFTWARE_FIRST + existing generic control/hint mechanisms"
related_claims = ["CLM-R3-001", "CLM-R3-002", "CLM-R3-003", "CLM-R3-004", "CLM-R3-005", "CLM-R3-006", "CLM-R3-EXP-001"]
related_capabilities = []
+++

# R3 — uArch Semantic Hints

## 30-second decision
**BLOCKED / 48.5 / no dedicated hardware program**

R3 is **C1-D2**, not an independent mechanism lane.

It asks only:
> after a lower-layer D1/system-control consumer has already proven SYSTEM_VALUE, does a material residual remain because software reacts too late or cannot access the required hardware state?

Today that prerequisite is not met.

## Deployment-depth chain

### D0 — semantic runtime contract
Agent/compiler/workflow → Agent-aware runtime.

Current parent state:
- Candidate A remains SIMULATION_SUPPORT;
- target-phone DemandState SYSTEM_VALUE is still open.

### D1 — derived system-control contract
Runtime → FFRT / Gewu / OS / kernel.

Prefer generic derived facts:
- ReleasePermission;
- CancelPermission;
- QoS mapping;
- conditional LatestReleaseBound;
- optional ResourceHint / StateHandle.

Raw Agent enums do not propagate below D0 by default.

Stage15 device-free pressure shows D1 residual collapses rapidly as ordinary software capture rises.

### D2 — hardware/uArch hint
System/runtime → CPU or hardware policy.

**Blocked until D1 first survives.**

## Parent-consumer state
- R1 post-ready timing: measurement-only; target-phone semantic residual not established.
- R2 CPU locality: phone-PMU measurement-only; target-phone causal CPU-local residual not established.
- No stable lower-layer hardware consumer currently has SYSTEM_VALUE.

## Broad novelty boundary
Do not claim differentiation from:
- generic compiler→scheduler/locality hints;
- generic Agent graph/topology→resource scheduling;
- planner→executor→resource-scheduler hierarchy;
- raw large Agent semantic ABI into CPU.

These are strong baseline/prior-art territory.

## Reopen gate
R3 may move out of BLOCKED only when all are satisfied:
1. a concrete D1/lower-layer consumer reaches target-phone SYSTEM_VALUE;
2. best software/system translation is causally insufficient;
3. the residual is caused by hardware reaction time, unavailable hardware state, wake/context cost, or another hardware-specific mechanism;
4. a compact derived hint/mechanism has >=~5% plausible incremental value;
5. direct decision-critical prior-art review is complete;
6. product/economics gate is plausible.

## Current action
No dedicated implementation.
No raw Agent-semantic CPU interface.
No silicon/ISA/uArch commitment.

Preserve instrumentation and parent-gate observability only.

Exact frozen V1 lineage is preserved in [deep.md](deep.md).


## Patent direct-claim re-audit — 2026-10-07

### PATENT-028 — VERIFIED broad compiler/runtime hint boundary
Current public claim text supports:
- compiler-produced scheduling-hint information;
- consumption by dynamic runtime scheduling;
- user-space scheduler;
- dependent locality/placement-related scheduling hints.

Safe project conclusion:
**generic compiler → runtime scheduling/locality hints are old/crowded prior art.**

Do not infer:
- Agent DemandState;
- Effect/Commit legality;
- a smartphone D2 interface;
- a specific CPU/uArch semantic hint.

### PATENT-029 — VERIFIED broad Agent workflow/resource-scheduling boundary
Current claim 1 supports a chain containing:
- implicit semantic processing;
- user-demand Agent blueprint;
- Agent workflow;
- task execution scheduling;
- explicit node topology / communication analysis;
- node resource scheduling;
- reinforcement-learning multi-Agent path optimization.

Safe project conclusion:
**broad Agent semantics/workflow/topology → resource scheduling is not whitespace.**

Important boundary:
specific implementation fields such as priority/resource type/duration/upstream/downstream IDs must not be presented as independent-claim language unless separately cited from the specification/dependent claim.

### PATENT-030 — VERIFIED planner/executor/resource hierarchy boundary
Current claim text supports:
- upper planning Agent;
- natural-language intent → workflow/DAG;
- macro planning/constraints;
- lower execution Agent;
- micro resource scheduling;
- resource-ready execution DAG;
- execution feedback;
- dependent CPU/GPU/I/O/memory resource labels and DRL/PPO scheduling details.

Safe project conclusion:
**planner Agent → execution Agent → resource scheduler hierarchy is crowded.**

Do not infer target-phone D2/uArch value or prior coverage of a compact hardware-specific Agent hint.

### R3 decision
CLM-R3-003 remains SUPPORTED with a deliberately narrow scope:
> generic compiler/runtime hints, broad Agent workflow semantics-to-resource scheduling, and planner/executor/resource hierarchy are established prior-art families.

R3 remains BLOCKED for independent reasons:
- D0 target-phone SYSTEM_VALUE is not established;
- D1 software insufficiency is not established;
- R1/R2 remain measurement-only;
- no hardware-specific causal residual has survived.

No score, lane, maturity or hardware change.
