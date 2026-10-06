> Frozen V1 D0→D1→D2 gate analyses from baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# Stage 12E — C1 Synthetic Sensitivity, Pass 2

Updated: 2026-10-04

## Purpose

Turn the open-workload observations into explicit **Keep/Kill regions**.

This pass is synthetic sensitivity analysis only.

It does not claim:
- phone timing;
- phone energy;
- Huawei/Kirin behavior;
- real predictor accuracy;
- real speculative-work cost.

Executable:
`analysis/device_free_simulation/c1_sensitivity_grid.py`

---

## 1. Event-frequency × event-cost gate for ASEC core

Let:
- `p` = fraction of events where privileged Agent semantics can change the decision;
- `m` = affected work cost relative to an average event.

Affected-cost share:

```text
s = p × m / (1 + p × m)
```

Reference opportunity gates from Pass 1:
- DemandState practical gate: **14.4%**
- joint Demand + Effect/Commit gate: **6.5%**

### Synthetic grid

| Event fraction | 0.5× cost | 1× | 2× | 4× | 8× |
|---:|---:|---:|---:|---:|---:|
| 2% | 1.0% | 2.0% | 3.8% | 7.4% | 13.8% |
| 4% | 2.0% | 3.8% | 7.4% | 13.8% | 24.2% |
| 6% | 2.9% | 5.7% | 10.7% | 19.4% | 32.4% |
| 8% | 3.8% | 7.4% | 13.8% | 24.2% | 39.0% |
| 10% | 4.8% | 9.1% | 16.7% | 28.6% | 44.4% |
| 15% | 7.0% | 13.0% | 23.1% | 37.5% | 54.5% |
| 20% | 9.1% | 16.7% | 28.6% | 44.4% | 61.5% |

### Interpretation

DemandState alone clears the 14.4% reference gate only when, for example:
- ~10% of events affect work that is ~2× average cost;
- ~6% affect ~4× cost;
- ~4% affect ~8× cost.

The joint Demand + Effect/Commit 6.5% gate is easier:
- ~4% of events at ~2× cost is already above the gate;
- ~2% at ~4× is also above the gate.

### Link to PARE

PARE frontier-model non-immediate-demand proposal share is about 3.6–10.1% of turns.

Therefore:

**[INFERENCE]**
- DemandState is not automatically high-value merely because the semantic exists.
- It becomes material if optional/speculative branches are materially heavier than normal observation/control events, or if similar semantics apply to a broader set of work than proposals.
- Effect/Commit Safety strengthens the joint gate because legality creates actions a generic predictor cannot safely take.

---

## 2. Predictor-strength Kill map for E1/E2/E3

Practical semantic gain model:

```text
B6-B4 = s × (a6-a4) × q - overhead
```

Where:
- `s` = controllable opportunity share;
- `a4` = B4 generic predictor effective accuracy;
- `a6` = practical semantic-contract accuracy;
- `q` = actionability.

Reference assumptions remain explicit sensitivity assumptions.

### Required opportunity share for 5% practical gain

#### E1 — TemporalFlexibility
B6 accuracy 90%, actionability 70%, overhead 0.2%.

| B4 timing predictor | Required opportunity share |
|---:|---:|
| 50% | 18.6% |
| 60% | 24.8% |
| 70% | 37.1% |
| 80% | 74.3% |
| 85% | 148.6% — impossible |
| 90% | impossible |

**Kill ceiling:** if effective B4 timing prediction is above about **82.6%**, 5% gain is unreachable even at 100% opportunity under this reference model.

#### E2 — NextResource
B6 accuracy 95%, actionability 60%, overhead 0.2%.

| B4 next-resource predictor | Required opportunity share |
|---:|---:|
| 50% | 19.3% |
| 60% | 24.8% |
| 70% | 34.7% |
| 80% | 57.8% |
| 85% | 86.7% |
| 90% | 173.3% — impossible |

**Kill ceiling:** about **86.3% B4 accuracy**.

#### E3 — StateAffinity S2/S3
B6 accuracy 90%, actionability 70%, overhead 0.3%.

| B4 reuse predictor | Required opportunity share |
|---:|---:|
| 50% | 18.9% |
| 60% | 25.2% |
| 70% | 37.9% |
| 80% | 75.7% |
| 85% | 151.4% — impossible |

**Kill ceiling:** about **82.4% B4 accuracy**.

#### E3 — StateAffinity S4 CPU-local
B6 accuracy 90%, actionability 60%, overhead 0.2%.

| B4 locality predictor | Required opportunity share |
|---:|---:|
| 50% | 21.7% |
| 60% | 28.9% |
| 70% | 43.3% |
| 80% | 86.7% |
| 85% | 173.3% — impossible |

**Kill ceiling:** about **81.3% B4 accuracy**.

---

## 3. Extension decisions after Pass 2

### E1 TemporalFlexibility
**Status: CONDITIONAL / HIGH KILL PRESSURE**

Keep only because M2's post-ready semantic boundary remains distinct from generic deadline/slack.

But:
- if generic timing predictor is ~80%, E1 needs ~74% controllable opportunity;
- if predictor exceeds ~82.6% under the current assumptions, E1 cannot clear the 5% gate.

**Next evidence needed:** actual post-ready timing distribution, not more semantic examples.

### E2 NextResource
**Status: DEFAULT-OFF OPTIONAL EXTENSION**

Do not place in stable ASEC v0.

Promote only if:
- next-engine/resource transitions are materially unpredictable from ordinary workflow/history;
- B4 accuracy is demonstrably below the kill region;
- prepare/pre-dispatch has enough actionable cost.

### E3 StateAffinity
**Status: DEFAULT-OFF OPTIONAL EXTENSION**

For S2/S3:
- PBKV, Libra and normal context managers already provide strong inferred/control baselines.

For S4:
- task identity, history, cache demand and shared-cache/affinity mechanisms create even stronger pressure.

Do not put explicit StateAffinity in stable ASEC v0 unless predictor and opportunity tests pass.

---

## 4. Consumer-depth sensitivity

ASEC now has three deployment depths:

### D0 — Runtime Contract
Planner/compiler/workflow → Agent-aware runtime.

Examples:
- do not materialize work;
- wait for confirmation;
- cancel before commit;
- derive discardability;
- translate to generic QoS.

### D1 — System Contract
Runtime → FFRT / Gewu / OS / kernel.

Potential value:
- lower layer sees semantics before/without runtime translation;
- tighter timing;
- cross-subsystem coordination;
- system-controlled cancellation/defer.

### D2 — uArch Hint
System/runtime → CPU/hardware mechanism.

Potential value:
- hardware-timescale release/wake/state action.

### Incremental-value rule

Let full semantic benefit be `G`.
If D0 captures fraction `r0`, then maximum D1 incremental benefit is:

```text
D1_increment = G × (1-r0)
```

For D1 to add at least 5%:

| Full semantic benefit G | D0 must capture less than |
|---:|---:|
| 6% | 16.7% |
| 8% | 37.5% |
| 10% | 50.0% |
| 15% | 66.7% |
| 20% | 75.0% |

### Interpretation

If a runtime can already translate most semantic value into:
- submit / do-not-submit;
- cancel / abort;
- existing QoS;
- ordinary dependencies;

then D1 has little room even if the semantic field itself is useful.

**[INFERENCE]**
This is now the most important C1 falsifier.

---

## 5. C1 should be competed by deployment depth

### C1-D0 — Minimal Agent Runtime Contract
**KEEP / strongest structural candidate**

Core:
- identity;
- DemandState;
- Effect/Commit Safety.

This can be valuable even if no new OS/uArch mechanism is required.

### C1-D1 — Cross-System Semantic Contract
**KEEP CONDITIONAL / evidence required**

Must demonstrate:
> raw/preserved Agent semantics below runtime produce value that cannot be achieved by D0 translation to existing system controls.

### C1-D2 — uArch semantic hints
**DOWNGRADE / Strategic Reserve at best**

No direct phone evidence yet.

Do not include as Primary Bet unless:
- D1 first survives;
- hardware-timescale residual is material;
- phone evidence later confirms value.

---

## 6. Current portfolio implication

The project should no longer ask:

> “Is C1 a Primary Bet?”

as one undifferentiated question.

Ask separately:
1. Is **C1-D0** a software/compiler/runtime bet?
2. Does **C1-D1** have system-level incremental value?
3. Does any residual justify **C1-D2 / uArch**?

This avoids forcing a valid Agent semantic idea into hardware.

---

## 7. Next step

The next discriminating work is now:

### D0 vs D1 actuator replay
For each ASEC core field:
- list D0 action;
- list D1 action;
- identify what D1 can do that D0 cannot;
- assign timing/control assumptions;
- replay incremental benefit.

Parallel:
- E1 timing sweep;
- E2 transition-predictor sweep;
- E3 reuse-predictor/state-cost sweep.

Only survivors enter Opportunity Competition 2.0 as separate software/system/uArch candidates.


---

# Stage 12E — C1 D0→D1 Actuator Replay

Updated: 2026-10-04

## Goal

Determine whether ASEC semantics must cross the Agent-runtime boundary.

Core question:

> What can D1 system layers do that D0 Agent runtime cannot already achieve by translating semantics into existing submit / hold / cancel / abort / QoS / dependency controls?

This is a **control-boundary analysis**, not phone performance evidence.

---

## 1. Deployment depths

### D0 — semantic meaning
Planner/compiler/workflow → Agent-aware runtime.

Preserve:
- DemandState;
- Effect / Commit Safety;
- optional predicted TemporalFlexibility;
- identity/provenance.

### D1 — system control
Runtime → FFRT / Gewu / OS / kernel.

The system does not necessarily need raw Agent meaning.

### D2 — hardware
System → CPU/NPU/memory/power mechanism.

No direct value assumed.

---

## 2. Important architectural correction

Do **not** lower raw semantic enums all the way down by default.

Prefer:

```text
Agent meaning
  DemandState
  EffectClass
  CommitState
        ↓ D0 semantic reasoning
derived legal/control facts
  ReleasePermission
  CancelPermission
  LatestReleaseBound
  QoS class
  optional StateHandle / ResourceHint
        ↓ D1 generic system interface
FFRT / Gewu / OS / kernel
        ↓
existing mechanisms
```

### Why

Agent semantics are framework/product concepts.

Kernel/CPU mechanisms need:
- what is legal;
- what is urgent;
- what can be deferred/canceled;
- what deadline/bound applies.

They should not have to understand:
- "speculative Agent branch";
- "planner confidence";
- framework-specific goal types.

**[INFERENCE]**
If C1 survives cross-layer lowering, the differentiated object may be a **semantic-to-control compiler/runtime lowering path**, not a large raw-semantic ABI exposed to hardware.

---

## 3. Field-by-field D0 vs D1 replay

| Semantic | D0 can already do | Potential D1-only residual | Current D1 verdict |
|---|---|---|---|
| **DemandState** | do not materialize/submit optional work; wait for authorization; cancel runtime branch | hold/cancel work whose demand changes **after** it has entered a lower queue; coordinate shared resources across processes/subsystems | **Conditional** |
| **Effect / Commit Safety** | decide legal cancel/defer/rollback; issue cancel/abort before commit | lower layer may stop an already-issued request faster, but raw effect class is usually unnecessary | **Raw propagation default-KILL** |
| **TemporalFlexibility** | withhold submission until release time; runtime timer/coalescing | lower layer can combine release with system idle/wake/resource state at tighter timescale; useful if materialized work must stay dependency-aware | **Most plausible D1 extension** |
| **NextResource** | pre-submit/prewarm next engine; stage data | system can pre-wake/core-place/power-manage before runtime dispatch | **Optional / predictor pressure** |
| **StateAffinity** | runtime retains/prefetches/pins semantic/model state | OS/system can coordinate state across processes/engines/cache/memory tiers | **Optional / predictor pressure** |

---

## 4. DemandState replay

### D0 action
When work is optional/speculative:
- do not create it;
- do not submit it;
- keep it outside the lower scheduler;
- cancel it in Agent runtime when demand disappears.

### D1 residual
D1 only matters when one of these is true:

1. demand changes after work has already entered FFRT/Gewu/system queues;
2. work belongs to another subsystem/process that D0 cannot directly control;
3. system-wide foreground/resource state changes and lower layer can suppress queued optional work faster;
4. runtime cannot cheaply retract already-materialized work.

### Derived D1 interface

Prefer:

`ReleasePermission`

or:

`CancelPermission`

rather than raw:

`DemandState = speculative`.

### Decision

**DemandState remains D0 core.**

D1 propagation is conditional on **late demand changes / already-materialized work**.

This is now a measurable trace condition.

---

## 5. Effect / Commit Safety replay

### D0 action
Agent runtime knows:
- read-only;
- reversible;
- irreversible;
- pre-commit;
- committed.

It can determine:
- legal-to-cancel;
- legal-to-defer;
- compensation-required.

### D1 question
Does FFRT/kernel/CPU need to know the raw effect class?

Usually no.

D1 only needs a derived control fact such as:
- CancelPermission = true/false;
- ReleasePermission = true/false;
- must-complete = true/false.

### Decision

**KEEP Effect/Commit in D0 ASEC core.**

**DEFAULT-KILL raw EffectClass / CommitState propagation below D0.**

If D1 survives, lower **permission**, not raw semantics.

This is a meaningful minimization beyond the previous field-level reduction.

---

## 6. TemporalFlexibility replay

### D0 action
Runtime can:
- wait;
- withhold task submission;
- batch/coalesce;
- schedule a timer.

### D1 residual
D1 becomes interesting if:
- dependency graph is already materialized;
- runtime wants dependency tracking to remain active;
- lower layer has better visibility of idle state / thermal / foreground / core state;
- the useful release decision occurs at a hardware/system timescale.

Public FFRT documentation already creates one practical tension:
task delay and input/output dependency behavior cannot simply be assumed composable.

Therefore:

```text
DependencyReady
        ↓
D1 ReleasePermission / LatestReleaseBound
        ↓
system chooses exact release
```

may be more defensible than pushing a generic "delay" from D0.

### Decision

**E1 remains the strongest D1-specific candidate, but still under high Kill pressure from B4 timing prediction and missing phone ResumeBudget.**

---

## 7. NextResource replay

### D0
Agent runtime/workflow often knows or predicts next engine/tool/resource.

It can:
- stage data;
- prepare request;
- initialize runtime;
- pre-submit.

### D1
Potential:
- pre-wake CPU/core;
- prepare accelerator/system power state;
- choose placement;
- reserve bandwidth.

### Main competitor
Generic transition predictor + current system state.

### Decision

No stable D1 field yet.

If it survives, expose a generic:
`ResourceHint + confidence`

rather than Agent-specific next-step meaning.

---

## 8. StateAffinity replay

### D0
Runtime can:
- retain context/KV;
- choose reuse groups;
- prefetch;
- avoid eviction;
- manage storage/DRAM/NPU state.

### D1
Potential:
- cross-process shared memory identity;
- CPU↔NPU transfer-state retention;
- system memory tiering;
- CPU-local placement/retention.

### Main competitors
- task identity;
- history/reuse predictor;
- PBKV-style workflow prediction;
- mzCache / Libra-like context managers;
- generic cache-aware scheduling.

### Decision

E3 does not belong in stable D1 contract yet.

If needed later, lower a generic:
`StateHandle / ReuseHint / RestorationCostClass`

not raw Agent-memory semantics.

---

## 9. Provisional two-level contract

### ASEC-D0 — semantic contract
Core:
- Continuation/Workflow identity;
- DemandState;
- Effect/Commit Safety.

Optional:
- predicted TemporalFlexibility + provenance;
- internal NextResource / StateAffinity metadata.

### System Control Contract — D1 candidate
Minimal derived controls:
- **ReleasePermission**
- **CancelPermission**
- **QoS mapping**
- conditional **LatestReleaseBound**
- optional **ResourceHint + confidence**
- optional **StateHandle/ReuseHint**

This D1 contract should remain generic enough that:
- non-Agent workloads could also use it;
- kernel/CPU does not need to understand Agent framework internals.

**[INFERENCE]**
This may be the correct software-hardware boundary if C1 survives.

---

## 10. Kill criteria for D1

Kill D1 as a distinct strategic layer if:

1. >~95% of optional work can be prevented before lower-layer submission;
2. demand/commit changes rarely occur after materialization;
3. runtime-issued cancel/abort is sufficiently fast;
4. D0 can translate semantics to existing QoS/dependency controls with <5% loss;
5. E1 timing opportunity is weak;
6. E2/E3 are matched by generic predictors.

If killed:
- keep ASEC-D0 as compiler/runtime design;
- do not invent new kernel/uArch Agent semantic interfaces.

---

## 11. Measurement fields now required

Future trace/replay should explicitly record:

- semantic decision timestamp;
- task materialization timestamp;
- FFRT/system submission timestamp;
- dependency-ready timestamp;
- demand-state transition timestamp;
- commit timestamp;
- cancel/abort timestamp;
- first-run / accelerator-start timestamp.

Key derived quantities:

```text
LateDemandChange =
    DemandTransitionTime > SystemSubmissionTime

CancelableInFlightWindow =
    CommitTime - SystemSubmissionTime

D1Opportunity =
    work already below D0
    AND semantics change / remain actionable
    AND D1 can act before D0 cleanup completes
```

This is a much stronger D0-vs-D1 discriminator than simply asking whether a semantic field exists.


---

# Stage 15 — D1 Residual Kill Test

Updated: 2026-10-05

## Decision

**D1 remains conditional and is now under stronger downgrade pressure.**

This test isolates the incremental value of a new D1 system-control path after D0 semantics already exist.

It does **not** ask whether Agent semantics are useful.
It asks:

> once the Agent-aware runtime already knows DemandState + Effect/Commit and can use existing submit/hold/cancel/QoS/yield/chunking controls, how much extra RequiredProgress could a faster lower-layer control of already-running pre-commit work still recover?

Evidence maturity remains:
**SIMULATION_SUPPORT / device-free only**.

No smartphone SYSTEM_VALUE is claimed.

## Model boundary

D0 is intentionally strong:
- semantic-known queued non-required work is held before submission;
- only already-running work can create a D1 residual;
- only semantic-known, legally cancelable work may be stopped;
- no illegal cancellation is permitted.

The remaining software limitation is compressed into:

**software_capture**

= fraction of otherwise-wasted, cancelable in-flight cost that existing D0 mechanisms can avoid through finer-grained tasks, cooperative checkpoints/yield, QoS reduction and runtime-side control.

D1 is modeled favorably with:
- 97% capture of this remaining cancelable in-flight cost.

Therefore this is a residual test that gives D1 substantial benefit of the doubt.

## Sweep

Fixed:
- semantic coverage: 90%;
- D1 capture: 97%;
- matched background budget: 60%;
- 200 work items/run;
- 500 replicates/cell.

Swept:
- non-required share: 10 / 20 / 30 / 40%;
- in-flight share: 10 / 20 / 30 / 40 / 50%;
- legally cancelable share: 50 / 75 / 100%;
- D0 software capture: 50 / 75 / 87.5 / 95%.

Primary metric:
**relative D1-vs-D0 RequiredProgress gain**.

## Reference point

At:
- 20% non-required;
- 30% in-flight;
- 75% cancelable;

| D0 software capture | D1 incremental gain | Runs >=5% |
|---:|---:|---:|
| 50% | ~3.39% | 13.6% |
| 75% | ~1.55% | 0% |
| 87.5% | ~0.66% | 0% |
| 95% | ~0.14% | 0% |

The D1 value collapses quickly once software can stop or de-prioritize most in-flight pre-commit work.

## Extreme-region check

Across the full grid:

### D0 software capture = 50%
19 grid cells clear a 5% mean-gain gate.

D1 can still matter when:
- non-required work is large;
- much of it is already in flight;
- most of it is legally cancelable.

### D0 software capture = 75%
Only **3** grid cells clear 5%.

They are extreme combinations:
- 30% non-required × 50% in-flight × 100% cancelable;
- 40% non-required × 50% in-flight × 75% cancelable;
- 40% non-required × 50% in-flight × 100% cancelable.

Even the strongest of these is only ~5.75% mean gain.

### D0 software capture = 87.5%
**0** grid cells clear 5%.

Maximum observed mean D1 residual is ~2.26%.

### D0 software capture = 95%
**0** grid cells clear 5%.

Maximum observed mean D1 residual is <0.5%.

## Interpretation

The strongest D1 opportunity is not a generic semantic ABI.

It is a narrow timing residual:

> demand changes after execution has already started, the work is still pre-commit, the remaining work is expensive, and cooperative software cannot reach a safe stop point quickly enough.

This makes **task granularity / checkpoint distance** a first-order architectural variable.

If D0 can recover roughly 87.5%+ of the otherwise-wasted in-flight cost through ordinary software mechanisms, this first-pass sweep finds no region where D1 clears the project’s 5% mean-gain bar.

## D1 promotion condition — refined

D1 should not be implemented as a new system interface unless target-phone traces show all of:

1. cost-weighted non-required work is material;
2. a material fraction is already in flight when demand changes;
3. it remains legally pre-commit cancelable;
4. existing D0 controls recover materially less than ~75–87.5% of the avoidable cost;
5. the remaining D1 incremental value is >=~5% RequiredProgress/end outcome at matched foreground QoE;
6. illegal cancellation remains zero.

## Device measurement implication

The minimum phone trace should now add one derived quantity:

**D0StopDistance / SoftwareCapture**

Estimate how much additional work executes between:
- semantic demand/effect change;
and
- the next safe software stop under realistic task chunking/checkpoint/yield/QoS policy.

Without this quantity, “in-flight cancelable work exists” is insufficient evidence for D1.

## Current decision

- D0: **KEEP / strengthen**
- D1: **KEEP CONDITIONAL, stronger downgrade pressure**
- D2/uArch: **no promotion**
- A overall: **Primary Bet / SIMULATION_SUPPORT unchanged**

Executable:
`analysis/stage15_semantic_progress/d1_residual.py`
