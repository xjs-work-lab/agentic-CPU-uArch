> Exact V1 R1 experiment specification and pass-1 result from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# Stage 15 — R1 Post-ready Continuation Timing Strong-Baseline Kill Test

Updated: 2026-10-05

## Goal

Test the narrow R1 residual:

> after a dependency is physically ready, does explicit Agent semantic timing provide a **safe latest-useful-release bound** that strong generic workflow/mobile scheduling cannot reconstruct?

## Baseline correction

The old comparison:
> eager release vs semantic deferred release

is no longer acceptable.

### New B4-release
Include:
- workflow DAG / critical-path urgency;
- deadline/latest-start/slack analysis;
- online work-duration estimates;
- queue pressure / backlog;
- foreground/device/thermal state;
- learned timing/history;
- mobile OS deadline/window scheduling;
- batching/coalescing;
- existing runtime delay/QoS actuators.

### B5
Perfect oracle:
- true LatestUsefulResume;
- perfect legal release window;
- perfect knowledge of downstream QoS impact.

### B6-semantic
B4 plus practical explicit Agent:
- ReleasePermission;
- LatestUsefulResume / LatestReleaseBound;
- confidence/provenance.

B6 gets no credit for timing already inferable by B4.

## Why this is necessary

Direct 2026 Agent work already demonstrates ready/release decoupling with queue/workflow signals, and mobile operating systems already defer/batch work around deadlines and system state.

Therefore the only differentiated quantity is:
**incremental semantic timing information.**

## Key quantities

- DependencyReady
- LatestUsefulResume
- ResumeBudget = LatestUsefulResume - DependencyReady
- **UsablePostReadyOpportunityShare**
- **GenericReleaseCapture**
- SemanticResidualCapture
- ConversionEfficiency
- late-release violation rate
- foreground QoE
- energy
- required/useful Agent progress

## Pass-1 model

```
Gain =
UsablePostReadyOpportunityShare
× (1 - GenericReleaseCapture)
× SemanticResidualCapture
× ConversionEfficiency
- Overhead
```

Reference:
- 90% semantic residual capture
- 70% conversion efficiency
- 0.2% overhead
- 5% target

Break-even:
- generic capture 50% -> ~16.5% usable post-ready opportunity required;
- 75% -> ~33.0%;
- 90% -> ~82.5%.

See:
`analysis/stage15_r1_timing/results/r1-timing-kill-pass1.md`

## Promotion gate

Promote above conditional reserve only if target-phone evidence shows all:
1. frequent positive ResumeBudget after dependencies are physically ready;
2. enough windows are long enough to be actionable;
3. B4-release captures materially less than ~75–90% of B5 oracle value;
4. B6 adds >=~5% meaningful energy/QoE/useful-progress value;
5. late-release violation remains acceptable/zero for hard bounds;
6. benefit is not reducible to ordinary deadline/slack/history/device-state scheduling.

## Kill / further downgrade

If:
- ready≈must-run for most cost-weighted work;
- positive windows are too short;
- GenericReleaseCapture is high;
- extra delay does not convert into energy/QoE/progress value;
- timing semantics remain only at user-turn/workflow scale;
- runtime/OS windows and batching match B6.

## uArch gate

Blocked.

Only reopen if:
- SYSTEM_VALUE is proven on phone;
- software timing is the causal insufficiency;
- useful windows sit at a timescale where runtime/FFRT cannot reliably act;
- a hardware-specific mechanism has a stable consumer and survives prior-art review.


---

# Stage 15 R1 — Strong-Baseline Timing Kill Test, Pass 1

Date: 2026-10-05

## Question

Does explicit Agent **ReleasePermission / LatestUsefulResume / ResumeBudget** retain a plausible >=5% incremental region after a strong generic release scheduler?

The comparison is no longer eager-release vs deferred-release.

The required comparison is:

- **B4-release:** generic workflow/DAG urgency + queue pressure + execution-history timing + foreground/device state + mobile deadline/window scheduling + batching/coalescing.
- **B6-semantic:** B4 plus explicit Agent semantic safe-release bound / permission.

## Why the baseline changed

A new direct 2026 Agent-systems paper,
**Decoupling Readiness from Release for Tail-Aware Scheduling of Agentic LLM Workflows**,
already treats ready != release as a first-class workflow-scheduling problem and reports up to 3.50x P95 flow-time speedup under contention without requiring an Agent-specific semantic ABI.

Mobile OS/runtime baselines are also strong:
- Android JobScheduler explicitly batches/defers jobs and uses deadlines/system-health signals;
- Android AlarmManager shifts inexact alarms to batch wakeups;
- Huawei FFRT exposes dependency scheduling, QoS, queue priority and microsecond delay attributes.

Therefore the R1 differentiator cannot be “defer ready work”.

It can only be:
> explicit Agent semantics expose a safe latest-useful-release bound that strong generic scheduling cannot reconstruct.

## Model

```
R1_gain =
UsablePostReadyOpportunityShare
× (1 - GenericReleaseCapture)
× SemanticResidualCapture
× ConversionEfficiency
- Overhead
```

Definitions:
- **UsablePostReadyOpportunityShare:** end-outcome-weighted share of ready work with a positive, long-enough ResumeBudget.
- **GenericReleaseCapture:** fraction of oracle safe-deferral value already captured by B4-release.
- **SemanticResidualCapture:** fraction of the remaining oracle value recovered by explicit Agent timing semantics.
- **ConversionEfficiency:** fraction of extra safe deferral that becomes real energy/QoE/useful-progress value.

Reference:
- SemanticResidualCapture = 90%
- ConversionEfficiency = 70%
- Overhead = 0.2%
- target = 5%

## Reference break-even

| Generic release capture | Required usable post-ready opportunity share |
|---:|---:|
| 0% | 8.25% |
| 25% | 11.01% |
| 50% | 16.51% |
| 75% | 33.02% |
| 90% | 82.54% |

Interpretation:
- with weak generic release control, R1 can be plausible;
- once B4 captures ~75% of oracle deferral value, one third of meaningful outcome must lie inside actionable post-ready slack;
- at 90% generic capture, the required share becomes extreme.

## Coarse grid

Sweep:
- usable opportunity share: 5/10/20/30/40/60/80%
- generic capture: 0/25/50/75/90%
- semantic residual capture: 70/90/100%
- conversion efficiency: 50/70/90%
- overhead: 0.2%

63 cells per generic-capture band.

5% passing cells:
- generic capture 0%: **50/63**
- 25%: **48/63**
- 50%: **41/63**
- 75%: **26/63**
- 90%: **4/63**

At 90% generic capture, only four cells pass. They require:
- 60–80% usable post-ready opportunity share;
- and near-perfect semantic capture and/or 90% conversion efficiency.

## Decision

### Broad R1 mechanism
**KILL as novelty:**
- readiness/release decoupling;
- generic deferred-ready queues;
- generic release-budget control;
- generic work batching/coalescing.

These are already active Agent-serving and mobile-OS/runtime mechanisms.

### Narrow R1 residual
**NARROW / DOWNGRADE to conditional Strategic Reserve / measurement hypothesis.**

Surviving question:
> does explicit Agent semantic timing expose a safe ReleasePermission / LatestUsefulResume bound that a strong generic release scheduler cannot infer, and does that residual create >=5% phone energy/QoE/useful-progress value?

## Required target-phone measurements

Do not implement special R1 hardware first.

Measure:
1. DependencyReady timestamp;
2. true LatestUsefulResume / semantic deadline;
3. actual release / first-run;
4. cost-weighted **UsablePostReadyOpportunityShare**;
5. B4-release outcome;
6. B5 oracle release outcome;
7. **GenericReleaseCapture = B4/B5 oracle headroom capture**;
8. B6 semantic incremental value;
9. energy / foreground QoE / required-progress conversion;
10. violation rate for late releases.

## Hardware boundary

No uArch promotion.

Huawei FFRT already exposes microsecond delay attributes and task dependency/QoS controls, but current public docs do not establish that delay is a dynamic dependency-ready-relative semantic bound.

Only reconsider lower-layer/hardware timing if:
- phone traces show useful windows at a timescale software cannot reliably exploit;
- strong FFRT/runtime release control leaves >=5% residual;
- the cause is timing latency, not missing policy.
