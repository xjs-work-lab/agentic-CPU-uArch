+++
id = "EXP-CG07-001"
type = "EXPERIMENT"
record_state = "CURRENT"
status = "SIMULATION_SUPPORT"
execution_state = "READY_FOR_MEASURED_INPUTS"
title = "CG-07 dedicated-vs-shared always-on energy break-even"
direction_ids = ["CG-07"]
tests_claim_ids = ["CLM-CG07-EXP-001"]
input_source_ids = ["VENDOR-019"]
evidence_target = "SYSTEM_VALUE"
+++

# EXP-CG07-001 — Dedicated vs shared always-on break-even

## Decision question
When does a dedicated low-power AI domain beat waking/sharing a high-performance NPU after idle, wake, active duration, batching and real Agent duty cycle are counted?

## Strong baseline
- shared NPU with strong power-gating / DVFS;
- batching / effective-wake reduction;
- CPU / small-model path;
- A semantic-progress control;
- existing background scheduling.

## Synthetic model status
Stage16A synthetic self-check is complete.

Reference example used only for model behavior:
- dedicated idle: 20 mW
- dedicated active: 200 mW
- shared active: 700 mW
- shared wake: 8 mJ
- one wake/event
- one-hour window

Synthetic break-even examples:
- 5 ms/event: ~6792 events/hour (~1.89/s)
- 20 ms/event: ~3913/hour (~1.09/s)
- 100 ms/event: ~1200/hour (~0.33/s)

Lowering dedicated idle from 20 mW to 5 mW moves the 20 ms / 8 mJ synthetic break-even from ~1.09/s to ~0.28/s.

## Critical boundary
These are **synthetic design-space examples**, not Dimensity 9600 Pro measurements.

The MediaTek 40% vendor claim is not injected as measured input.

## Promotion gate
Dedicated domain must beat the strong shared-domain baseline on representative persistent-Agent workloads using measured:
- event rate/duty cycle;
- wake energy/latency;
- idle/residency power;
- active power;
- battery/thermal/foreground QoE.

Exact V1 sections are preserved in [deep.md](deep.md); the exact model is preserved in [model.py](model.py).
