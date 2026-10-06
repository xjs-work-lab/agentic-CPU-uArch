+++
id = "EXP-R3-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "SIMULATION_SUPPORT"
execution_state = "BLOCKED_BY_PARENT_GATES"
title = "R3 D1→D2 activation / software-insufficiency gate"
direction_ids = ["R3"]
tests_claim_ids = ["CLM-R3-EXP-001"]
input_source_ids = []
evidence_target = "UARCH_CANDIDATE"
+++

# EXP-R3-001 — D1→D2 activation gate

## Purpose
This is **not** an independent hardware PoC.

It packages the frozen device-free parent-gate analysis and defines the evidence required before a D2 experiment can exist.

## Existing device-free pressure
Stage15 D1 residual test:
- reference D1-vs-D0 gain ~3.39% at 50% software capture;
- ~1.55% at 75%;
- ~0.66% at 87.5%;
- ~0.14% at 95%.

Across the tested grid:
- at 87.5% D0 software capture: **0 cells** clear 5%;
- at 95%: **0 cells** clear 5%.

This is SIMULATION_SUPPORT only.

## Activation prerequisite
Before any D2/hardware experiment:
1. D0 semantic value must be real on target phone;
2. D1 must reach SYSTEM_VALUE over D0;
3. D1 software insufficiency must be causal;
4. a hardware-timescale/state cause must be identified.

## Then test
Only after activation, compare:
- best D1 software/system baseline;
- candidate compact derived hardware hint/mechanism.

Promotion target:
>=~5% meaningful incremental value at matched correctness/QoE/energy constraints.

## Current execution state
**BLOCKED_BY_PARENT_GATES**

No hardware mechanism is selected.
No uArch result is fabricated.

Frozen device-free analyses are preserved in [deep.md](deep.md).
