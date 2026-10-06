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
