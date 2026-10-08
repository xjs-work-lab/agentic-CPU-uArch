+++
id = "R1"
type = "DIRECTION"
record_state = "CURRENT"
title = "Post-ready Continuation Timing"
direction_class = "STRATEGIC_RESERVE"
investment_lane = "WATCH"
historical_score_context = 55.5
score_context_status = "RETIRED_HISTORICAL_NOT_CURRENT_ALLOCATION_SCORE"
evidence_maturity = "SIMULATION_SUPPORT"
maturity_scope = "broad novelty killed; strong generic release baseline and device-free break-even established; target-phone >=5% semantic residual not established"
strongest_baseline = "B4-release"
related_claims = ["CLM-R1-001", "CLM-R1-002", "CLM-R1-003", "CLM-R1-004", "CLM-R1-005", "CLM-R1-006", "CLM-R1-007", "CLM-R1-EXP-001"]
related_capabilities = []
+++

> **CURRENT Round15E decision:** `WATCH`, **not a core Strategic Reserve**. Post-ready semantic timing retains a narrowly framed hypothesis, but generic ready/release/utility software and lack of direct phone Agent-specific value make it lower priority than A, B-residual and CPU continuation locality. Historical 55.5 is not an active confidence score. The archived EXP-R1-001 is not to be executed; use published evidence only. [DEC-R1-002](../../../08-decisions/events/DEC-R1-002.md).

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


## Reserve Rescue — 2026-10-07

### PAPER-047
Tail-risk-aware release scheduling makes release itself a software decision:
- ready turns need not be released immediately;
- mean-CVaR tail risk, online turn-work estimates and queue pressure drive priority/budget;
- real software-engineering Agent traces show up to 3.50× P95 workflow flow-time improvement under contention.

This closes broad Ready≠Release novelty.

### PAPER-048
Controlled forced-clarification experiments over 6,000+ runs / 84 task variants show:
- goal clarification loses nearly all value after ~10% of execution;
- input clarification retains value to roughly 50%;
- clarification after mid-trajectory can be worse than never asking.

This is direct evidence that Agent semantics have timing windows.

But the timescale and actuator differ:
- trajectory/user interaction;
- not DependencyReady→LatestUsefulResume;
- not phone CPU residency/wake/scheduling;
- not energy/QoE.

### Final R1 interpretation
The surviving residual is deliberately narrow:
> can an explicit Agent semantic timing bound outperform B4-release on a representative phone?

No score, lane, maturity or hardware change.

### Evidence-depth state
R1 paper-depth debt: **0**.


## Patent direct-claim audit — 2026-10-07

### PATENT-005 — direct claim VERIFIED
Claim 26 directly recites:
- determine I/O transfer rate;
- calculate/update predicted completion time;
- compare completion time with known exit latency;
- send wake command when completion time falls within exit latency.

Boundary:
this is **pre-completion predictive wake**, not intentional post-ready semantic release.

### PATENT-018 — direct claim VERIFIED
Claim 1 directly recites:
- predecessor/dependency and time constraints;
- earliest start;
- latest start that still completes within time constraint;
- task movable range = latest minus earliest start;
- allocation order based on that movable range.

Boundary:
this is generic dependency/deadline slack scheduling, not Agent semantic LatestUsefulResume.

### PATENT-019 — direct claim VERIFIED
Claim 1 directly recites:
- first thread on one running unit;
- heterogeneous second unit asleep;
- migration condition based on load;
- wake second unit first;
- then schedule/migrate the first thread's task to it.

Boundary:
generic wake-before-migrate / heterogeneous scheduling, not semantic post-ready timing.

### PATENT-017 — evidence-role CORRECTION
Current independent claims primarily recite:
- workload scheduler;
- workload manager;
- work-unit resource attributes;
- resource allocation/tuning according to those attributes and service class.

Its description/background explicitly discusses deadlines, expected duration and latest-start-like intervention.

Therefore:
- keep PATENT-017 as **specification/background ancestry** for deadline/workload scheduling;
- do not label it a direct-claim latest-start anchor.

### R1 decision
CLM-R1-004 remains SUPPORTED because the broad mechanism family is independently anchored by PATENT-005 / 018 / 019 and reinforced by PATENT-017's specification-level scheduling ancestry.

This audit does not touch the surviving R1 residual:
> post-ready Agent semantic ReleasePermission / LatestUsefulResume beyond strong generic release/slack/wake/migrate scheduling.

No score, lane, maturity or hardware change.
