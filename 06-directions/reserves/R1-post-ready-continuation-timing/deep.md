# M2 Prior Art — Burst / Continuation / Wake

## Strong prior art

### [Dynamic Predictive Wake-up Techniques — US20170168853A1](https://patents.google.com/patent/US20170168853A1/en)
**Assignee:** Qualcomm-related; exact assignee metadata pending verification

Predicts I/O completion and reasons about low-power exit latency to wake the CPU at the appropriate time.

**Implication:** “predict NPU/I/O completion and wake CPU just in time” is not new.

### [Collaborative Workload Management — US6591262B1](https://patents.google.com/patent/US6591262B1)
**Assignee:** metadata pending verification

Uses deadline and expected duration to derive latest useful start behavior.

### [Task Allocation Method and Device — JP2007140710A](https://patents.google.com/patent/JP2007140710A/en)
**Assignee:** metadata pending verification

Derives earliest/latest start times from task-graph/deadline relationships.

### [Task Scheduling Method and Electronic Device — WO2026056682A1](https://patents.google.com/patent/WO2026056682A1/en)
**Assignee:** Huawei

Covers waking a sleeping execution unit and moving work based on heterogeneous core/load considerations.

### [US9384036B1 — Park/resume around coprocessor waits](https://patents.google.com/patent/US9384036B1/en)
**Assignee:** Google

Covers parking/resuming execution around coprocessor/accelerator waits with context-related behavior.

## Decision

**KILL as broad novelty:**
- predictive wake;
- latest-start/slack scheduling;
- generic wake-and-migrate;
- generic continuation scheduling.

## Residual M2 hypothesis

**Post-ready Agent continuation release control**:

`DependencyReady → DeferredReady → ContinuationRelease`

The surviving question is whether Agent semantics reveal a useful:
`ResumeBudget = LatestUsefulResume - DependencyReady`

at µs–ms timescales that generic predictors cannot capture.


---

# M2 — Agent Burst & Continuation Efficiency

**Status:** CONDITIONAL STRATEGIC RESERVE / measurement hypothesis — semantic post-ready timing residual  
**Agentic relevance:** Agentic-amplified  
**Mobile transfer:** Likely–Strong  
**Stage 11B result:** Generic predictive wake, generic latest-start scheduling, generic task wake/migration and generic continuation scheduling are **KILL as novelty**.

## Core quantity
`ResumeBudget = LatestUsefulResume - DependencyReady`

Strictly distinguish:
- wait time = dependency is not ready;
- scheduler latency = runnable but not scheduled;
- temporal flexibility = ready now, but can intentionally remain unreleased without hurting downstream QoS.

## What Stage 11B killed

### 1. Predictive wake / just-in-time wake is old
**US20170168853A1 — Dynamic Predictive Wake-up Techniques**  
https://patents.google.com/patent/US20170168853A1/en

The mechanism predicts I/O completion, compares it with low-power entry/exit latency, and can issue an early wake so the CPU is ready when the transfer completes.

Therefore:
- “predict accelerator completion and wake CPU just in time” is not new;
- “use completion prediction to choose sleep state” is not new.

### 2. Generic latest-start / slack scheduling is old
**US6591262B1 — Collaborative workload management**  
https://patents.google.com/patent/US6591262B1

Uses deadline and expected duration to detect a latest useful start time.

**JP2007140710A — Task allocation method/device**  
https://patents.google.com/patent/JP2007140710A/en

Explicitly derives earliest/latest start time from DAG/deadline constraints.

Therefore:
- “compute latest start and defer work” is not new.

### 3. Generic wake-and-migrate on heterogeneous cores is covered
**Huawei WO2026056682A1 — Task scheduling method and electronic device**  
https://patents.google.com/patent/WO2026056682A1/en

Wakes a sleeping execution unit and migrates a thread/task based on load and heterogeneous core performance.

Therefore:
- “wake another core then migrate a task” is not new.

### 4. Generic continuation-model scheduling exists
Historical continuation/thread schedulers and hardware schedulers already exist; continuation terminology itself is not sufficient novelty.

## What still survives

### Stage 15 correction
Broad **post-ready release control itself is now KILL as novelty**.

PAPER-047 directly demonstrates readiness/release decoupling for Agent workflows using generic workflow/tail-risk/work-estimate/queue-pressure signals.

Therefore the surviving question is narrower.

### Narrow surviving research question
**Agent semantic release-bound residual**:

> After a heterogeneous dependency has physically completed, can the system intentionally hold the dependent CPU continuation in a non-runnable/deferred-ready state until an Agent-derived latest useful resume time, in order to improve energy/foreground QoE/state locality?

Define:
- `t_ready`: dependency physically completes;
- `t_release`: continuation is released into runnable domain;
- `t_first_run`: continuation actually executes;
- `t_latest`: latest useful resume/start time;
- `ResumeBudget = t_latest - t_ready`;
- `Delta_release = t_release - t_ready`.

Constraint:
`0 <= Delta_release <= ResumeBudget`.

## Why this is narrower than prior art
Predictive wake usually tries to align CPU readiness **with dependency completion**.

Our surviving hypothesis asks whether an Agent continuation can remain intentionally unreleased **after dependency completion**, using future workflow semantics rather than only device history or transfer-time prediction.

Latest-start scheduling is broad workflow/task scheduling; the remaining M2 formulation is specifically:
- mobile Agent;
- heterogeneous dependency completion;
- CPU continuation;
- post-completion release budget;
- foreground-phone QoE / low-power state interaction;
- µs–ms control timescale.

This combination is **not yet proven novel**. Stage 11 only establishes that the broad ancestors are crowded.

## Candidate mechanisms
- deferred-ready continuation state;
- release coalescing;
- continuation-aware idle-depth decision;
- warm-core/state-aware release;
- foreground-frame-aware release;
- completion coalescing only when bounded by Agent semantics.

## Required comparison
The key baseline is not default scheduling.

Compare:
- **B4-release:** workflow/DAG urgency + deadline/latest-start + queue pressure + work estimate + history + foreground/device state + mobile job windows/batching;
- **B5:** perfect semantic timing oracle: true LatestUsefulResume;
- **B6:** practical explicit ReleasePermission / LatestReleaseBound.

B6 receives credit only for value not already captured by B4-release.

If B5 adds little beyond B4, M2 loses strategic value.

## Required trace
Joint distribution:
`P(ResumeBudget, CPU BurstLength, ContinuationFrequency, Criticality)`.

## Stage 12E mechanism-sensitivity result

Reference practical model:

```text
M2_gain =
    post_ready_opportunity_share
    × (B6_timing_accuracy - B4_timing_accuracy)
    × actionability
    - overhead
```

With B6=90%, actionability=70%, 0.2% overhead, a 5% gain requires:
- B4 timing 50% → ~18.6% post-ready opportunity;
- B4 70% → **~37.1%**;
- B4 80% → **~74.3%**;
- B4 85% → impossible under the reference model.

There is currently no direct smartphone evidence that such a large share of meaningful continuation outcome lies inside a positive post-ready ResumeBudget.

### Updated decision

**DOWNGRADE M2 from standalone KEEP to Strategic Reserve / M4 timing sub-mechanism.**

Preserve:
- DependencyReady vs SemanticReleasePermission;
- LatestUsefulResume / ResumeBudget trace fields;
- release/coalescing hypothesis.

Do not invest in dedicated M2 hardware until phone traces demonstrate:
- frequent positive ResumeBudget;
- short continuation density;
- real energy/QoE opportunity;
- generic timing predictors below the kill region.

## Kill criterion
Kill M2 even as a reserve if:
1. real Agent continuations rarely have meaningful positive post-ready ResumeBudget; or
2. generic history/device-state policy captures nearly all value; or
3. measurable gains are too small to justify cross-layer complexity.


## 2026-10-04 C1 open-workload replay implication

PARE provides strong semantic evidence that an intervention can be **premature / awaiting confirmation**, but its time unit is Agent/user turns, not CPU post-ready timing.

Frontier-model gather-context events occupy only about **2.3–6.6% of total turns** under the reported setup.

This does **not** measure:
- DependencyReady;
- LatestUsefulResume;
- µs–ms ResumeBudget;
- wake/idle opportunity.

**Decision:** PARE does not rescue M2 from its existing evidence gate.

M2 remains **KEEP, narrow**, but C1 TemporalFlexibility stays a conditional extension with high Kill pressure until a separate post-ready timing sweep (and later phone trace) shows sufficient opportunity.


## Stage 15 R1 strong-baseline kill test

Detailed experiment:
[stage15-r1-timing-kill-test.md](../07-experiments/stage15-r1-timing-kill-test.md)

### New prior-art / system pressure

**PAPER-047** directly separates readiness from release in Agentic LLM workflows and reports up to 3.50× P95 flow-time speedup under contention using workflow-level signals, online work estimates and queue pressure.

Generic mobile mechanisms are also mature:
- Android JobScheduler batches/defers work and adapts execution around system health/deadlines;
- Android AlarmManager batches inexact alarms to reduce wakeups;
- Huawei FFRT publicly exposes dependency scheduling, QoS/priority and microsecond delay attributes.

**[INFERENCE]** R1 can no longer claim deferred-ready/release-budget control as strategic novelty.

### Strong-baseline break-even

Model:
```
Gain =
UsablePostReadyOpportunityShare
× (1 - GenericReleaseCapture)
× SemanticResidualCapture
× ConversionEfficiency
- Overhead
```

Reference assumptions:
- semantic residual capture 90%;
- conversion efficiency 70%;
- overhead 0.2%;
- target 5%.

Required usable post-ready opportunity share:
- generic capture 0% -> 8.25%;
- 25% -> 11.01%;
- 50% -> 16.51%;
- 75% -> **33.02%**;
- 90% -> **82.54%**.

Coarse sweep, 63 cells per generic-capture band:
- 0%: 50 pass;
- 25%: 48;
- 50%: 41;
- 75%: 26;
- 90%: only 4.

### Updated decision

**NARROW / DOWNGRADE R1 to conditional Strategic Reserve / measurement hypothesis.**

Surviving residual:
> explicit Agent semantic ReleasePermission / LatestUsefulResume must add >=~5% phone energy/QoE/useful-progress value beyond a strong generic release scheduler.

Required phone measurements:
- cost-weighted UsablePostReadyOpportunityShare;
- GenericReleaseCapture versus B5 oracle;
- B6 semantic incremental value;
- timing-window scale;
- actual energy/QoE/progress conversion.

No uArch promotion.
