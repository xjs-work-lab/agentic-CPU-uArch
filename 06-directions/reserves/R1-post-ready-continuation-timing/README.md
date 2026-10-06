+++
id = "R1"
type = "DIRECTION"
record_state = "CURRENT"
title = "Post-ready Continuation Timing"
direction_class = "STRATEGIC_RESERVE"
investment_lane = "CONDITIONAL_RESERVE"
score_context = 55.5
evidence_maturity = "SIMULATION_SUPPORT"
maturity_scope = "broad novelty killed; strong generic release baseline and device-free break-even established; target-phone >=5% semantic residual not established"
strongest_baseline = "B4-release"
related_claims = ["CLM-R1-001", "CLM-R1-002", "CLM-R1-003", "CLM-R1-004", "CLM-R1-005", "CLM-R1-006", "CLM-R1-007", "CLM-R1-EXP-001"]
related_capabilities = []
+++

# R1 — Post-ready Continuation Timing

## 30-second decision
**Conditional Strategic Reserve / 55.5 / measurement hypothesis**

Broad ready/release decoupling is **KILL as differentiated novelty**.

Surviving residual:
> after a heterogeneous dependency is physically ready, does explicit Agent `ReleasePermission / LatestUsefulResume` expose safe post-ready timing that a strong generic release scheduler cannot reconstruct and that creates >=~5% phone energy/QoE/useful-progress value?

## Core quantity
`ResumeBudget = LatestUsefulResume - DependencyReady`

Strictly separate dependency wait, scheduler latency after runnable, and intentional post-ready semantic release flexibility.

## Strong baseline
`B4-release` includes DAG/critical-path urgency, deadline/latest-start/slack, online duration estimates, queue pressure, foreground/device/thermal state, learned history, mobile deadline/windows, batching/coalescing and existing runtime delay/QoS actuators.

## Device-free pressure
Reference 5% break-even:
- GenericReleaseCapture 50% → ~16.51% usable opportunity;
- 75% → ~33.02%;
- 90% → ~82.54%.
At 90% generic capture only **4/63** coarse cells pass.

## Current lane
Conditional measurement reserve only. No uArch promotion.

## Promotion
Requires `EXP-R1-001` target-phone evidence showing frequent/actionable ResumeBudget, incomplete B4 capture, >=~5% B6 semantic incremental value, and acceptable/zero hard-bound violations.

## Hardware boundary
Only reconsider lower-layer/hardware timing after phone SYSTEM_VALUE is proven and software timing is causally insufficient.
