+++
id = "EXP-CG07-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "SIMULATION_SUPPORT"
execution_state = "READY_FOR_MEASURED_INPUTS"
title = "CG-07 post-gating dedicated-vs-shared front-end break-even"
direction_ids = ["CG-07"]
tests_claim_ids = ["CLM-CG07-EXP-001"]
input_source_ids = ["VENDOR-019", "PAPER-087", "PAPER-088"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-CG07-001 — Post-gating dedicated vs shared front-end break-even

## Decision question
After a PRPF-class lightweight gate suppresses low-value/no-action context observations, when does a dedicated low-power Agent front end still beat the strongest shared-NPU / CPU / small-model front end on useful progress per energy while preserving foreground QoE and thermal limits?

## Why the model changed
The original Stage16A model treated each event as direct active compute.

PAPER-087 + PAPER-088 show a stronger abstraction:

`context observation → lightweight intervene/no-intervene gate → accepted subset → heavy reasoner`

Therefore CG-07 must be decided on **post-gating residual economics**, not raw context-event frequency.

## Strong baseline
- PRPF-class intervention gating;
- candidate-function compression;
- shared NPU with strong power gating / DVFS;
- CPU / small-model gate path;
- batching / effective-wake reduction;
- A semantic-progress control;
- existing background scheduling.

## V2.2 residual model
```text
DedicatedFrontEndEnergy =
T × P_dedicated_idle
+ N_context × E_dedicated_gate_increment
+ N_context × p_accept × E_dedicated_handoff

BaselineFrontEndEnergy =
N_context × E_baseline_gate
+ N_context × p_accept × E_baseline_handoff
```

Common heavy-reasoner active energy can be excluded when both alternatives invoke the same heavy reasoner for the same accepted subset.

### Required measured inputs
- context observations/hour;
- acceptance/intervention rate after gating;
- gate energy/latency on strongest CPU/shared-NPU front end;
- dedicated-domain idle power;
- dedicated gate active power + gate duration;
- handoff/wake energy and latency for accepted observations;
- heavy-reasoner duty cycle;
- batching/residency policy;
- battery / thermal / foreground QoE.

## Critical boundary
PAPER-088's reported −69.3% expected compute and −60.1% end-to-end latency are **not** phone energy measurements and are not inserted as device parameters.

All current numerical grids in `model.py` remain synthetic design-space probes.

## Promotion gate
CG-07 may advance only if measured representative smartphone traces show that the dedicated front end beats the strongest software-sparsified shared/CPU baseline after gate overhead, accepted-event handoff/wake, idle/residency, quality, battery, thermal and foreground QoE are counted.

Historical V1 excerpts remain in [deep.md](deep.md).
