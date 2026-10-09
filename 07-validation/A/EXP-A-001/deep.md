> Exact V1 experiment specification copied from frozen baseline.

# Stage 15 — A 2027 PoC Engineering Specification

Updated: 2026-10-04

## Objective

Turn **A — Agent Semantic Progress Control** into an implementable 2027 PoC.

Primary hypothesis:

> At the **same foreground QoE envelope**, a practical policy using **DemandState / required-progress value** preserves more required/useful Agent progress than **B4-TX**, where B4-TX already has strong history prediction plus runtime-derived Effect/Commit legality.

The PoC is software/runtime first.

It is **not** a CPU-uArch prototype.

---

# 1. Experimental architecture

```text
Agent / workflow runtime
    │
    ├─ semantic labels
    │   DemandState
    │   SideEffectClass
    │   CommitState
    │   Workflow/Continuation ID
    │
    ▼
A Semantic Policy Layer
    │
    ├─ B4 generic policy
    ├─ B5 oracle
    └─ B6 practical semantic policy
    │
    ▼
Actuation API
    │
    ├─ submit
    ├─ defer
    ├─ yield
    ├─ cancel
    ├─ resume
    └─ QoS / resource-policy mapping
    │
    ▼
Runtime / OS / scheduler / PT-A
    │
    ▼
CPU / NPU / memory / UI / tool execution
```

The first PoC may implement the policy entirely in a userspace harness.

D1/system integration is tested **only after** the D0 semantic-value gate is positive.

---

# 2. Core entities

Every unit of schedulable Agent work must have:

- `SessionID`
- `AgentID`
- `TaskID`
- `StepID`
- `ContinuationID`
- optional `ParentContinuationID`
- optional `DependencyID`

A continuation is the primary policy unit.

A continuation is not assumed to equal:
- one thread;
- one model invocation;
- one tool call;
- one OS task.

Adapters map framework operations to continuation records.

---

# 3. Minimum D0 semantic contract

## DemandState

Enum:
- `REQUIRED`
- `OPTIONAL`
- `SPECULATIVE`

Definition:
- REQUIRED — currently belongs to active goal/demand closure;
- OPTIONAL — useful but not required for current goal correctness;
- SPECULATIVE — launched before necessity is confirmed.

Required provenance field:
- authored;
- runtime-resolved;
- compiler-derived;
- offline-oracle;
- predicted.

Predicted DemandState must not be treated as oracle ground truth.

## SideEffectClass

Enum:
- `READ_ONLY`
- `REVERSIBLE`
- `IRREVERSIBLE`
- `UNKNOWN`

## CommitState

Enum:
- `PRE_COMMIT`
- `COMMITTED`

Optional:
- `CommitTimestamp`
- `CompensationAvailable`

## Identity

Required:
- workflow/continuation identity.

Identity is infrastructure, not strategic novelty.

---

# 4. Derived legality

The stable policy interface should derive:

## CancelPermission
Values:
- allowed;
- forbidden;
- compensation-required;
- unknown.

## DeferPermission
Values:
- allowed;
- bounded;
- forbidden;
- unknown.

## ReleasePermission
Values:
- release-now;
- may-hold;
- blocked.

These are derived facts.

Do not propagate raw semantic enums into lower layers unless later evidence proves a consumer needs them.

---

# 5. Required trace events

Extend the stable `events.csv` contract with:

### Lifecycle
- `continuation_created`
- `dependency_ready`
- `semantic_required`
- `semantic_optional`
- `semantic_speculative`
- `release`
- `first_run`
- `yield`
- `cancel_requested`
- `cancel_effective`
- `resume`
- `commit`
- `complete`
- `fail`

### Foreground/QoE
- `foreground_interaction_start`
- `foreground_interaction_end`
- `frame_start`
- `frame_end`
- `jank_event`
- `input_latency_sample`

### Resource
- `cpu_run`
- `npu_submit`
- `npu_complete`
- `tool_submit`
- `tool_complete`
- `backend_transition`
- `thermal_sample`
- `energy_sample`

---

# 6. Required per-event fields

Minimum stable fields:

- `timestamp`
- `event_type`
- `SessionID`
- `AgentID`
- `TaskID`
- `StepID`
- `ContinuationID`
- `DependencyID`
- `DemandState`
- `DemandProvenance`
- `SideEffectClass`
- `CommitState`
- `ForegroundState`
- `QoSClass`
- `BackendClass`
- `PolicyID`
- `Decision`
- `DecisionReason`

Optional when available:
- CPU core/frequency/idle;
- runnable latency;
- NPU phase;
- DDR pressure;
- PMU;
- thermal;
- energy;
- PT-A outcome receipt ID.

Unknown values remain explicit `UNKNOWN`.

---

# 7. Baselines

## B0 — default system
No special Agent-semantic control.

## B1 — correct generic QoS
Correct foreground/background/reactive classification.

## B2 — static protection
Examples:
- fixed background throttle;
- fixed yield interval;
- fixed resource cap.

## B3 — generic learned history
Can use:
- workflow/task identity;
- recent transitions;
- historical timing;
- historical completion/resource behavior.

Cannot use:
- actual DemandState;
- effect/commit legality.

## B4 — strongest generic baseline
Must include:
- correct QoS;
- dependency state;
- current load;
- thermal;
- bandwidth;
- current CPU/NPU state;
- recent history;
- generic learned timing/resource prediction;
- legal generic submit/cancel/yield controls;
- SERENO-like generic yielding/protection.

B4 is the primary competitor.

## B5 — perfect semantic oracle
Perfect:
- DemandState;
- effect/commit legality.

Optional isolated oracle studies:
- Demand only;
- Effect/Commit only;
- full core.

## B6 — practical semantic policy
Uses only labels realistically available before the decision.

Required first version:
**B6-Min**
- DemandState;
- Effect/Commit Safety;
- continuation identity.

Do not add TemporalFlexibility, NextResource or StateAffinity in first A PoC.

---

# 8. B6-Min policy

Reference policy:

### Under no foreground pressure
- run REQUIRED normally;
- permit OPTIONAL according to normal policy;
- permit SPECULATIVE within resource budget.

### Under rising foreground pressure
1. cancel/defer legal SPECULATIVE work first;
2. then defer/cancel legal OPTIONAL work;
3. preserve REQUIRED work subject to product safety limits;
4. never cancel COMMITTED irreversible work;
5. if legality unknown, choose conservative behavior.

### Under thermal/power pressure
Use the same semantic ordering but allow product policy to impose:
- required progress floor;
- thermal ceiling;
- total background budget.

The first PoC should intentionally keep the policy simple.

The research question is the **value of information**, not sophisticated policy optimization.

---

# 9. Useful-progress definition

Raw background throughput is not the target metric.

Define:

## RequiredProgress
Weighted completed work that belongs to the currently active required goal closure.

Initial implementation:
- completed REQUIRED continuations;
- normalized by required-work cost or work units.

## UsefulAgentProgress
May include:
- REQUIRED work at weight 1.0;
- OPTIONAL work at configurable lower weight;
- SPECULATIVE work credited only if later demanded/used.

All weights must be declared before comparison.

Primary Stage 15 gate should use **RequiredProgress** first.

---

# 10. Foreground QoE envelope

B4 and B6 must be compared at a matched foreground QoE envelope.

At minimum record:
- jank rate;
- frame-time p95/p99;
- input/interaction latency;
- optional application-specific foreground latency.

Recommended comparison modes:

### Mode Q1 — fixed jank ceiling
Example:
policy must remain within a declared delta of native/foreground-only behavior.

### Mode Q2 — matched QoE
Select B4 and B6 operating points with statistically similar foreground QoE, then compare required progress.

Never compare a more aggressive B6 against a more conservative B4.

---

# 11. Workload matrix

Mandatory:

### Negative/control
- C0 traditional foreground app;
- C1 single-shot local LLM;
- W1 reactive assistant.

Purpose:
semantic background selectivity should be small/irrelevant here.

### Core positive
- W5 proactive/background Agent;
- W6 foreground user + background Agent.

### Generalization
- W2 reactive GUI Agent;
- W3 Agentic RAG;
- W4 long-horizon cross-app Agent.

A should not survive solely on one synthetic proactive workload.

---

# 12. Perturbation dimensions

Sweep:

## Semantic mix
- REQUIRED fraction;
- OPTIONAL fraction;
- SPECULATIVE fraction.

## Work cost
- short CPU continuation;
- model/NPU work;
- tool/API work;
- UI action;
- network wait.

## Effect mix
- read-only;
- reversible;
- irreversible;
- pre/post commit.

## Foreground pressure
- low;
- medium;
- high.

## Thermal/power
- unconstrained;
- moderate cap;
- sustained thermal pressure.

## Prediction quality
For B3/B4 history predictors:
- low;
- medium;
- strong.

---

# 13. Primary metrics

## Strategic
- RequiredProgress / second
- RequiredProgress completed in fixed window
- required task completion latency
- B6 vs B4 RequiredProgress gain at matched QoE

## Correctness
- illegal cancellation count
- irreversible-effect duplication
- required-work loss
- stale decision count

All correctness violations are fatal.

## Foreground
- jank
- frame p95/p99
- input latency

## Efficiency
- CPU active time
- wake count
- energy
- thermal
- NPU utilization
- memory bandwidth

Efficiency metrics are secondary until semantic progress value is established.

---

# 14. Core decision quantities

## Information value
`B5 - B4`

## Deployable value
`B6 - B4`

## Capture ratio
`(B6-B4)/(B5-B4)`

## Software capture
Compare:
- D0-only B6;
- D0→existing generic actuators;
- optional later D1.

If D0 existing actuators capture ~80–90%+ oracle value, do not push deeper.

---

# 15. Stage 15 Go / No-Go

## GO — confirm A
Normally require:
- >=~5% meaningful RequiredProgress gain vs B4;
- matched foreground QoE;
- zero illegal cancellation;
- positive result across multiple pressure/workload regimes;
- practical B6 captures material B5 headroom.

## NARROW
If:
- value exists only in specific proactive regimes;
- value is strong but remains fully inside Agent runtime.

Then narrow product/workload scope rather than immediately kill.

## DOWNGRADE
If:
- B5-B4 small;
- B6 captures little B5;
- B4 history predicts demand almost as well;
- semantic work density/cost too low.

## KILL cross-layer A
If:
- useful value exists only inside the Agent framework;
- no durable runtime/system control point remains.

---

# 16. D1 test — only after GO

Candidate derived D1 fields:
- CancelPermission;
- ReleasePermission;
- LatestReleaseBound only if timing evidence exists.

Experiment:
- D0 policy using existing runtime controls
vs
- D0 + minimal D1 integration.

Promotion requires a material incremental outcome gain.

Do not expose raw DemandState/EffectClass to kernel/CPU merely because D0 is useful.

---

# 17. Reusable instrumentation for other lanes

The A trace must also support:

## C
- backend transitions;
- dispatch;
- NPU submit/complete;
- wake/poll/sync;
- CPU active intervals.

## R1
- DependencyReady;
- Release;
- FirstRun;
- later empirical LatestUsefulResume.

## R2
- core placement;
- migration;
- PMU samples where available.

## B-residual
- semantic revision event;
- ArtifactID/StateHandle;
- invalidate/restore events can be added later.

This avoids separate instrumentation stacks.

---

# 18. Required outputs

A 2027 PoC run should produce:

1. normalized `events.csv`;
2. policy decision log;
3. semantic-label audit;
4. B0/B1/B3/B4/B5/B6 summary;
5. matched-QoE comparison;
6. correctness audit;
7. sensitivity matrix;
8. promotion/kill recommendation;
9. explicit evidence maturity:
   - STRUCTURAL_SIGNAL;
   - SIMULATION_SUPPORT;
   - SYSTEM_VALUE if real-device causal re-execution exists.

---

# 19. Implementation sequence

### Sprint A0
Trace/schema + synthetic runtime.

### Sprint A1
B4/B5/B6 replay.

### Sprint A2
Live software controller with synthetic foreground/Agent workload.

### Sprint A3
Integrate representative Agent adapters.

### Sprint A4
Real-phone re-execution when environment is available.

### Sprint A5
Only if A4 positive:
D0 vs D0+D1 residual test.

No uArch work is part of A0–A4.


# 20. Stage 15 E1 first result

Device-free executable:
- `../analysis/stage15_semantic_progress/simulate.py`
- `../analysis/stage15_semantic_progress/generate_events.py`

Archived result:
- `../analysis/stage15_semantic_progress/results/pass1-summary.md`

First decision:
**SIMULATION_SUPPORT — KEEP A, but narrow the key real-workload questions.**

The synthetic surface indicates:
- low optional/speculative cost share (~5–10%) is often insufficient against strong B4;
- ~20–30%+ non-required cost share can create >=5% headroom, depending on generic predictor strength;
- Effect/Commit cancelability materially changes the result;
- a strong generic runtime with broad safe-cancel visibility compresses semantic advantage.

Therefore real-phone characterization must prioritize **cost-weighted semantic mix and cancelability**, not merely count semantic events.


# 21. Pass 2 — B4 hardening from real proactive-workload evidence

New P0 sources:
- PAPER-043 Proactive Agent
- PAPER-044 ProAgentBench

The B4 definition is strengthened.

A real promotion experiment should include:
- B4-L2 learned long-history predictor;
- B4-L3 real-world-trained predictor where feasible;
- approximately five minutes of behavioral history where the workload supports it;
- ordinary generic effect/cancel visibility;
- participant/session-separated evaluation.

Reference pressure:
- ProAgentBench LLaMA-3.1-8B real-world SFT: 74.0% When-to-Assist accuracy / 78.5% F1;
- Qwen3-VL-8B real-world SFT: 63.5% accuracy / 72.4% F1.

These are not universal accuracies and not direct DemandState prediction.

### Updated A confirmation rule
Do not confirm A merely because B6 beats shallow/static B4.

A must show >=~5% meaningful RequiredProgress/end-outcome gain at matched foreground QoE against the strongest feasible **B4-L3**.

If B4-L3 captures ~80–90%+ of B5 headroom, narrow or downgrade deeper semantic propagation.


# 22. Strong-B4 residual refinement

Stage 15 strong-B4 sensitivity changes the interpretation of D0.

Reference device-free result:
- moderate B4 (~74% proxy): DemandState can provide >=5% by itself in a favorable 20%-non-required regime;
- strong B4 (~90–95%): Demand-only residual compresses, while Effect/Commit legality can become the larger incremental field;
- when ordinary runtime exposes 100% cancellation legality, Effect-only value disappears.

Therefore the real PoC must report three ablations:
1. **B6-Demand**
2. **B6-EffectCommit**
3. **B6-Min Full**

Do not report only Full D0.

The first real-phone trace must also measure:
- GenericCancelVisible;
- GenericEffectStateVisible;
- true pre-commit cancelability.

Canonical minimal trace:
历史记录所指的 `stage15-minimum-target-device-trace.md` 未在当前V2.2仓库单独归档；本研究不执行新的手机trace，现行禁测边界与结题判断见[最终研究归档验收](../../../00-project/final-research-archive-acceptance-2026-10-09.md)。


### Stage 15C baseline hardening — B4-TX

TomasuLLM and Cordon make a transaction-aware legality baseline mandatory.

**B4-TX**
- B4-L3 long-history demand prediction;
- dependency/QoS/device-state baseline;
- transaction/sandbox/lineage-derived effect state;
- commit/rollback/publication barriers where runtime can establish them.

**B6-Demand**
- B4-TX + explicit DemandState / required-progress value.

**B6-LegalityResidual**
- only legality information that cannot be derived by B4-TX.

**B6-Full**
- B4-TX + DemandState + any proven legality residual.

Primary Stage15D/phone question:
> does B6-Demand or B6-Full add >=~5% RequiredProgress at matched foreground QoE over B4-TX?

Do not credit Effect/Commit information twice.
