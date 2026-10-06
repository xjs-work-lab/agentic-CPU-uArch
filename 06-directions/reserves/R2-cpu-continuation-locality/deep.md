# M3 — Persistent Agent State Fabric

**Status:** broad M3a DOWNGRADED / B-residual conditional Strategic Reserve / M3b conditional Strategic Reserve / phone-PMU measurement hypothesis  
**Agentic relevance:** Agentic-amplified; some state classes are Agent-native  
**Evidence maturity:** SYSTEM_VALUE for mobile model-state management; STRUCTURAL_SIGNAL for cross-tier Agent state; CPU-uArch value not yet established  
**Mobile transfer:** Strong for memory/state pressure; Medium-Low for CPU-local microarchitectural state  
**Stage 11C result:** Generic cache/TLB/predictor retention, generic cache-aware migration, generic cache partitioning, and generic warm-state restoration remain **KILL as novelty**.

## 2026-10-04 reframe — state tiers first

The old framing was too CPU-cache centric. The parent problem is now:

> **Persistent Agent State Fabric** — preserve, place, move, evict and recover long-lived Agent state across semantic memory, workflow state, model/KV state, shared CPU–accelerator memory, storage and CPU-local microarchitectural state.

“Fabric” means a logical cross-tier identity/policy plane, not one physically unified cache.

| Tier | State examples | Natural control layer | CPU-uArch status |
|---|---|---|---|
| **S0 Semantic / episodic** | user facts, summaries, retrieved memories | Agent runtime / DB / storage | Not CPU-uArch by default |
| **S1 Workflow / executor** | DAG progress, tool results, action history, checkpoints, commit/effect state | Agent runtime / OS / storage | Not CPU-uArch by default |
| **S2 Model state** | KV cache, weights, experts, activations | inference runtime / NPU-GPU memory / DRAM / UFS | Memory-system/NPU problem first |
| **S3 Shared transfer/control** | CPU↔NPU buffers, descriptors, reusable intermediate data | heterogeneous runtime / shared memory / OS | system co-design candidate |
| **S4 CPU-local microstate** | L1/L2/LLC, TLB, branch predictor, warm-core state | scheduler + CPU uArch | true uArch candidate, weakest direct phone evidence |

### Strong mobile evidence is concentrated in S2, not S4

- **[FACT]** [mzCache](https://arxiv.org/abs/2609.01338) shows that smartphone multitasking can evict model/KV state and that fine-grained shared-buffer restoration can materially reduce TTFT.
- **[FACT]** [Dynamic Flow, Static Graph](https://arxiv.org/abs/2609.34727) uses hierarchical KV management, cost-aware prefetch/eviction and compute-storage co-design for mobile NPUs.
- **[FACT]** [EStream](https://arxiv.org/abs/2609.06551) virtualizes MoE expert state between UFS and NPU-addressable memory on a commercial Snapdragon phone.
- **[FACT]** [PBKV](https://arxiv.org/abs/2605.06472) predicts future Agent invocations and uses predicted reuse to retain/evict/prefetch KV state.

**[INFERENCE]** The broad idea “Agent future information tells the system which state to keep” is therefore already demonstrated for Agent/model state. M3 cannot use that as broad novelty.

### Residual M3 questions

1. Can one compact state identity/reuse contract coordinate multiple phone state tiers?
2. Does explicit ASEC `StateAffinity` add value beyond task identity, history and learned workflow predictors?
3. Does S3 shared CPU–NPU state movement create a hardware/system control point?
4. Does S4 CPU-local state matter enough to justify CPU-uArch support?

### Split the opportunity

#### M3a — Persistent Agent State Fabric
**DOWNGRADE as an Agentic Primary-Bet candidate.**

Persistent mobile AI state remains a real system/platform problem, but Stage 14 now shows that the broad Agent-specific differentiation is heavily compressed by:
- strong D0 semantic/context management;
- online history-based Agent reuse prediction;
- prediction-guided KV management;
- version-aware Agent serving;
- semantic/version-aware Agent cache invalidation prior art.

Likely ownership:
- Agent/runtime state representation;
- OS/memory management;
- NPU/runtime;
- DRAM/UFS tiering;
- heterogeneous shared-memory/data-path co-design.

#### M3b — CPU Continuation Locality
**DOWNGRADE further to conditional Strategic Reserve / phone-PMU measurement hypothesis; no current hardware investment.**

It only returns to a CPU-uArch bet if cache/TLB/predictor/warm-core continuity shows meaningful latency/energy value after strong generic affinity/shared-cache/runtime baselines.

### ASEC StateAffinity boundary

Useful fields may include:
- StateID / ReuseGroup;
- StateClass;
- ReuseHorizon;
- expected NextResource;
- reuse probability/confidence;
- Discardability;
- restoration/recompute cost class.

But **StateAffinity is not differentiated merely because it predicts reuse**. It must show incremental information/deployability beyond generic history/cache-demand/workflow prediction.

### New validation baseline

For state experiments compare:
- **B4-state:** task identity + history + current memory pressure + learned prediction;
- **B5-state:** perfect future-reuse oracle;
- **B6-state:** practical explicit Agent semantics + confidence.

A CPU-local M3b candidate is killed if B5−B4 is small (working threshold ~5% on meaningful end outcomes) or if S2 model/KV/storage state dominates the total opportunity.

---

## Structural question
Does a smartphone Agent create a repeatable **cross-step / cross-core / cross-engine hot-state** whose loss materially hurts CPU-side continuation efficiency, and can Agent future semantics improve state placement/retention beyond generic scheduler and cache policies?

This is the real M3 question. It is broader than “make cache bigger” but narrower than “Agent needs a special cache”.

## Strong evidence that locality/state can matter

### 1. Agentic server characterization
**Architectural Implications of Agentic AI Workflows (2026)**  
https://arxiv.org/abs/2608.04458

[FACT] The paper reports that multiplexing Agent workloads on shared CPU cores degrades microarchitectural locality, with cache/pipeline effects, and uses role-aware pinning to recover locality.

[BOUNDARY] This is datacenter evidence, not direct smartphone proof.

### 2. Qualcomm mobile product signal
**Qualcomm Oryon Flex Cache (2026)**  
https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache

[CLAIM] Qualcomm explicitly links Agentic AI / multi-step work moving across CPU cores to shared dynamic cache residency so work does not restart cold after handoff.

[BOUNDARY] This is vendor product/marketing evidence, not independent measurement of Agent cache bottlenecks.

### 3. Mobile AI state persistence is already a real systems problem
**mzCache: On-Device LLM Memory Management under Multitasking (MobiCom 2026)**  
https://arxiv.org/abs/2609.01338

[FACT] Mobile multitasking can evict LLM weights/KV state and make resumed inference pay storage restoration or KV recomputation cost; mzCache reports 2.1–5.5× TTFT reduction over storage-backed partial offload.

[BOUNDARY] This is model/KV memory state, not CPU cache/TLB/branch predictor state.

## What Stage 11C killed

### A. Generic branch-predictor state save/restore is old
**WO2021045811A1 / EP4025998B1 — Swapping and restoring context-specific branch predictor states on context switches**  
https://patents.google.com/patent/WO2021045811A1/en  
https://patents.google.com/patent/EP4025998B1/en

Covers per-context branch-predictor state storage, swapping and restoration, including preloading likely-next context state.

Therefore:
- “save Agent branch predictor state and restore later” is not new;
- “preload predictor state for the next context” is not new.

### B. Generic cache/TLB footprint save/restore is old
**US7634642B2 — Mechanism to save and restore cache and translation trace for fast context switch**  
https://patents.google.com/patent/US7634642B2/en

Covers tracking and restoring execution footprint including TLB, instruction-cache and data-cache state.

Therefore:
- “retain/restore cache/TLB footprint across continuation” is not new.

### C. Per-process cache partitioning is old
**US6295580B1 / US6629208B2 — Cache system for concurrent processes**  
https://patents.google.com/patent/US6295580B1/en  
https://patents.google.com/patent/US6629208B2/en

Covers cache partitions associated with process/group identifiers to prevent one process from evicting another.

Therefore:
- “Agent-tagged cache partition” by itself is not new.

### D. Cache-aware migration is already mature, including Huawei
**Huawei EP2894565B1 / US9483321B2 — Method/apparatus for determining task to be migrated based on cache awareness**  
https://patents.google.com/patent/EP2894565B1/en  
https://patents.google.com/patent/US9483321B2/en

Covers task migration decisions considering cache behavior/locality.

**Qualcomm US9626295 — scheduling tasks in a heterogeneous processor cluster using cache-demand monitoring**  
https://patents.justia.com/patent/9626295

Covers portable heterogeneous processor clusters and task migration based on processor workload and shared-cache demand.

Therefore:
- “prefer a cache-warm core / cache-aware migration” is not new.

### E. Huawei already considers task migration interference with LLC/memory bandwidth
**Huawei WO2024007922A1 — Task migration method and apparatus**  
https://patents.google.com/patent/WO2024007922A1/en

The description explicitly discusses cases where waking/migrating a low-priority task can occupy shared LLC and memory bandwidth and hurt higher-priority tasks.

Therefore:
- “do not migrate background work when it will disturb foreground cache/bandwidth” is not a new broad concept.

## Surviving M3 formulation

### Agent Continuation Hot-State Contract
The potentially surviving question is not whether hardware can preserve state; it can.

It is whether Agent execution exposes **future semantic information that lets the system identify which small state is worth preserving, where, and for how long**.

Candidate semantic facts:
- ContinuationID / AgentStepID;
- expected next execution domain;
- estimated next-resume window;
- state-affinity identifier;
- criticality;
- expected reuse probability;
- discardability/speculation.

Potential consumers:
- core-placement policy;
- selective cache retention;
- prefetch/prewarm;
- predictor/TLB restoration policy;
- CPU–NPU shared metadata placement;
- state eviction priority.

## Key differentiating hypothesis
Generic locality systems react to:
- current cache demand,
- task identity,
- observed history,
- current load.

M3 only remains strategically interesting if an Agent planner/runtime can provide **future cross-step reuse information** that materially improves decisions beyond those generic signals.

## Strongest competing baseline
M3 must beat:
- task affinity / cache-aware scheduler;
- history-based warm-core selection;
- generic cache partitioning;
- generic memory pressure/state restoration;
- Qualcomm-style shared cache flexibility.

## What is NOT yet publicly demonstrated
As of this research round, direct smartphone Agent measurements of:
- L1/L2/LLC MPKI across Agent continuations;
- TLB miss increase after step/core migration;
- branch mispredict warmup after Agent continuation;
- exact hot-state size and reuse distance;
- incremental benefit of Agent semantic hints over history-based affinity

remain **not publicly evidenced** in the sources reviewed.

## Stage 12 measurement requirement
For each Agent continuation, trace:
- previous and next core;
- migration;
- L1/L2/LLC misses;
- TLB misses;
- branch mispredictions;
- CPU burst length;
- time since prior same-Agent execution;
- dependency/next-resource type;
- working-set/state identifiers where instrumentable.

Compare:
1. default scheduling;
2. generic task/core affinity;
3. history-based warm-core policy;
4. perfect Agent future-state oracle.

## Go / No-Go
**GO** if:
- real Agent workloads show repeated stateful reuse across short/medium suspension windows;
- migration/context loss produces measurable execution or energy cost;
- future Agent semantics outperform history-only locality control.

**NO-GO / downgrade** if:
- Agent CPU bursts have little reusable CPU-side microarchitectural state;
- NPU/model memory dominates and CPU locality contribution is negligible;
- generic affinity/shared-cache mechanisms capture nearly all benefit.

## Stage 11C verdict
- Generic “Agent cache” → **KILL**
- Generic predictor/TLB/cache retention → **KILL**
- Generic cache-aware migration → **KILL**
- **Agent future-state-guided locality/retention → KEEP as hypothesis**
- Direct mobile evidence strength → **Medium-Low; Stage 12 is mandatory**


## 2026-10-04 open-workload event-density update

MemGUI-3K reports:
- 28.8 average steps per trajectory;
- 1.17 memory_add + 0.03 memory_update + 0.04 memory_delete = about **1.24 explicit memory actions / trajectory**;
- explicit memory-action density ≈ **4.3% of steps**;
- 65.1% of trajectories contain at least one memory action;
- 88.7% contain at least one span-level fold.

**[OBSERVATION]**
State/context management is common at the trajectory level but explicit semantic-memory actions are sparse relative to all GUI steps.

**Boundary:** this is not a direct measure of state reuse. Many ordinary steps may still consume previously stored context.

**Decision:** this further supports:
- M3a Persistent Agent State Fabric → KEEP as system problem;
- E3 explicit StateAffinity ABI → optional / high Kill pressure;
- M3b CPU-local StateAffinity/locality → remains gated Strategic Reserve with weak direct evidence.

StateAffinity must beat capable runtime/context managers plus task/history/PBKV-style prediction; explicit memory actions alone are insufficient justification.


## Stage 12E unified mechanism-sensitivity update

### M3a system value vs semantic residual

mzCache reports:
- TTFT can rise from ~0.8 s to ~16 s in a restoration-pressure example;
- full-eviction OS paging can increase TTFT by 18–20×;
- specialized runtime/memory management reduces TTFT by 2.1–5.5× vs partial offload.

This makes S2/S3 persistent state a **strong real mobile system problem**.

However, a semantic StateAffinity/ReuseHint only adds value beyond B4 if it improves future-reuse decisions.

Reference semantic residual model:
- B6 reuse accuracy 90%;
- actionability 70%;
- overhead 0.3%.

Examples:
- restore penalty share 25%, B4 reuse 80% → ~1.45% gain;
- 50%, B4 70% → ~6.7%;
- 95%, B4 80% → ~6.35%.

**[INFERENCE]**
Explicit Agent state semantics can matter in severe restore/recompute regimes, but ordinary regimes are easily dominated by PBKV/history/context-manager baselines.

### M3b CPU-local break-even

For a 5% target:
- software captures 50%, hardware recovers 50% residual → CPU-local penalty must be ~20.4% of end outcome;
- software captures 75%, hardware recovers 50% → ~40.8%;
- software captures 90% → most reference regions become implausible.

Server Agent evidence shows locality disruption, but also shows pooling/pinning can recover significant value in software.

### Updated decision

- **M3a:** KEEP as system Strategic Candidate; generic state manager value is strong, Agent-specific StateHandle/ReuseHint remains conditional.
- **M3b:** experiment-only reserve. No dedicated CPU-cache/TLB/predictor program before direct phone PMU evidence.


## Stage 14 Candidate B differentiation audit

Detailed audit:
[stage14-candidate-b-differentiation-audit.md](stage14-candidate-b-differentiation-audit.md)

### What changed

The broad thesis:

> Agent semantics tell the system which future state to retain/evict/prefetch

is no longer differentiated enough.

**[FACT]** CacheScout shows that an online first-order Agent-transition model can capture substantial KV reuse value without an explicit semantic ABI.

**[FACT]** PBKV shows that richer workflow representation improves future-Agent prediction, but does not isolate the incremental value of its semantic hidden-state signal from topology + history.

**[FACT]** AgentProg shows that explicit semantic/program state has direct mobile value, but much of that value is captured entirely at D0 Agent runtime/context construction.

**[FACT]** Versioned Execution, LOCAL, PlaceMem and Invalidation Contracts show that version/validity/dependency-aware Agent state is already an active 2026 systems direction.

**[FACT]** PATENT-032 directly claims Agent semantic/version-aware cache validity/invalidation at the dialogue/reasoning-memory layer.

### What is therefore killed/narrowed

**KILL as B strategic center**
- explicit StateAffinity / ReuseHint as the main differentiator;
- generic “Agent future reuse → retain/prefetch state”;
- generic versioned Agent state;
- generic semantic/version-aware Agent cache invalidation.

### Surviving B-residual

> **Mobile Agent Semantic-to-Physical State Coherence**

Narrow question:

```text
S0/S1 semantic/workflow revision
        ↓ dependency/provenance lineage
derived smartphone S2/S3 artifacts
        ↓
selectively invalidate stale state
preserve certified compatible state
        ↓
NPU / DRAM / UFS / runtime
```

This is a correctness + reconstruction-cost problem, not primarily a reuse-prediction problem.

### Strong safe baseline

Do not compare against unsafe stale reuse.

**B4-safe:**
on a known semantic/workflow revision, safely invalidate the entire derived-state scope and rebuild as needed.

**B6-coherence:**
use dependency lineage to invalidate only affected artifacts and preserve compatible state.

### First device-free break-even

For a 5% outcome target and 0.2% metadata overhead:

- if only 25% of derived state is affected per revision and practical preservation captures 90% of the opportunity, revision-weighted reconstruction cost must be about **7.7%** of the end outcome;
- at 5% revision frequency, that corresponds to roughly **1.67× average-event reconstruction cost per revision**;
- if 50% of state is affected, required weighted reconstruction share rises to about **11.6%**, or roughly **2.6× average-event cost** at 5% revision frequency.

These are sensitivity assumptions, not phone measurements.

### Updated decision

- **Broad Persistent Agent State Fabric:** valuable platform engineering, but **DOWNGRADE from Primary Bet finalist**.
- **B-residual / Semantic-to-Physical State Coherence:** **KEEP as Strategic Reserve / challenger**.
- **M3b CPU-local continuity:** remains experiment-only Reserve.

### Promotion gate

Promote B-residual only if phone trace/prototype evidence shows:
1. semantic/workflow revisions create meaningful S2/S3 stale-state events;
2. strong safe-generic version/hash/provenance handling still leaves material avoidable restoration/recompute cost;
3. cross-tier lineage-aware preservation adds **>=~5% meaningful outcome value** over B4-safe-generic;
4. benefit survives realistic memory-pressure bands;
5. the control point stays differentiated after direct prior-art review.

### Kill gate

Kill B-residual if:
- revisions are rare;
- rebuild is cheap;
- nearly all state becomes invalid anyway;
- generic hashes/versioning already provide equivalent precision;
- or the useful value remains entirely in S0/S1 context management.


## Stage 15 B-residual strong-baseline kill test

Detailed experiment:
[stage15-b-residual-kill-test.md](../07-experiments/stage15-b-residual-kill-test.md)

### Baseline correction

The old comparison:
> safe full flush vs dependency-aware selective invalidation

is too weak.

PAPER-032, PAPER-045 and PAPER-046 now show that versioned execution, dependency/provenance validity and selective preservation/replay are already concrete Agent-system mechanisms.

The required baseline is now **B4-safe-generic**:
- known revision/version event;
- safe version/hash/provenance-scoped preservation where possible;
- fail closed when validity is unknown;
- stale reuse = 0.

B6 receives credit only for additional S0/S1 -> S2/S3 compatibility information not already captured by that baseline.

### Device-free break-even result

Reference assumptions:
- 90% lineage capture;
- 75% retention survival under pressure;
- 0.2% metadata overhead;
- 5% target gain.

At 5% revision frequency and only 25% true affected state:
- 0% generic capture -> ~10.27% revision-weighted rebuild share needed;
- 50% generic capture -> ~20.54%;
- 75% generic capture -> ~41.09%.

At 50% true affected state:
- 50% generic capture -> ~30.81%;
- 75% generic capture -> ~61.63%.

Coarse sweep, 108 cells per generic-capture band:
- 25% generic capture: 26 pass >=5%;
- 50%: 13 pass;
- 75%: only 2 pass, both extreme revision/rebuild regimes.

### Updated decision

**B-residual: NARROW / DOWNGRADE to conditional Strategic Reserve / measurement hypothesis.**

It is no longer an active second-Bet challenger in the device-free portfolio.

Re-open only if target-phone evidence shows:
1. frequent semantic/workflow revision events;
2. expensive S2/S3 rebuild;
3. low GenericSafePreservationCapture after a strong baseline;
4. high RetentionSurvival under memory pressure;
5. >=~5% matched-outcome residual with zero stale reuse.

No CPU-uArch promotion.


## Stage 15 R2 strong-software-baseline kill test

Detailed experiment:
[stage15-r2-locality-kill-test.md](../07-experiments/stage15-r2-locality-kill-test.md)

### Baseline strengthened again

R2 must now beat two generic layers.

**Software locality capture**
- PAPER-008 / Agora: role-aware pooling + pinning reduces tool CPU demand by up to ~46%, worst-case tool latency by ~13%, while retaining ~99% serving throughput.
- PAPER-049 / Affinity Tailor: soft Preferred Cores preserve cache/branch/prefetcher locality while allowing bursts; production geomean per-CPU throughput improves 12% on chiplet and 3% on non-chiplet systems.

**Generic hardware locality capture**
- Qualcomm Oryon Flex Cache exposes one dynamically allocated cache pool across heterogeneous cores and explicitly uses Agent multi-step/core-handoff as a product scenario.
- Arm CSS for Mobile 2 provides coherent, QoS-aware system interconnect for heterogeneous AI-native mobile execution.

These vendor sources are capability/product signals, not independent R2 performance proof.

### Device-free break-even

Reference intentionally favors R2:
- candidate residual recovery 75%;
- end-outcome conversion 90%;
- overhead 0.2%;
- target 5%.

Required **raw CPU-local penalty share** before locality controls:
- SW 50%, generic HW 0% -> ~15.4%;
- SW 50%, generic HW 50% -> ~30.8%;
- SW 75%, generic HW 25% -> ~41.1%;
- SW 75%, generic HW 50% -> **~61.6%**;
- SW 90%, generic HW 0% -> ~77.0%;
- SW 90%, generic HW 25% -> >100%.

Coarse sweep, 42 cells per software+generic-HW band:
- 50% / 50% -> 18 pass;
- 75% / 25% -> 12;
- 75% / 50% -> 6;
- 75% / 75% -> 0;
- 90% / 0% -> 4;
- 90% / 25% -> 1;
- 90% / >=50% -> 0.

### Updated decision

**R2 NARROW / DOWNGRADE to conditional Strategic Reserve / phone-PMU measurement hypothesis.**

This does **not** mean CPU locality is irrelevant.
It means an Agent-specific CPU-uArch locality mechanism has not earned investment because:
- direct phone Agent PMU evidence is still missing;
- strong software can capture material locality value;
- generic mobile shared/coherent cache hardware is also advancing;
- generic state-retention/migration mechanisms are already old prior art.

Re-open only if target-phone traces show a large residual after strong software + generic hardware baselines.

No uArch promotion.
