# Software / Hardware Boundary

## Principle
First prove semantic value; then prove system value; then prove software insufficiency; only then justify uArch.

## Current deployment-depth model

### D0 — Semantic runtime contract
Agent/compiler/workflow → Agent-aware runtime.

Preferred differentiated raw semantic:
- DemandState / required-progress value.

Required safety/infrastructure facts:
- Effect/Commit legality, preferably runtime-derived from transactions/tool state where possible;
- continuation/workflow identity.

### D1 — Derived system-control contract
Runtime → FFRT / Gewu / OS / kernel.

Prefer generic derived controls:
- ReleasePermission;
- CancelPermission;
- QoS mapping;
- conditional LatestReleaseBound;
- optional ResourceHint / StateHandle.

Do not propagate framework-specific raw Agent semantics below D0 by default.

### D2 — uArch / hardware hint
Only after D1 leaves a material residual.

## Software-first if
- D0/D1 captures ~80–90% of oracle gain;
- useful timing windows are long enough for software control;
- benefit comes mainly from policy/selectivity;
- submit/cancel/abort/QoS/dependency controls are sufficient;
- runtime/context managers capture state value;
- generic prediction captures next-resource/reuse/timing information.

## Hardware becomes plausible if
- useful windows are sub-ms and software reacts too late;
- wake/interrupt/context restore dominates;
- cpuidle/DVFS decisions require earlier future knowledge;
- CPU-local cache/TLB/predictor loss remains material after strong affinity/pooling;
- a stable phone system-control workload class emerges;
- D1 derived controls demonstrably outperform D0-only translation.

## Current Stage 12E implication

- Candidate A (Semantic Progress Control): **software/runtime first**.
- PT-A (Heterogeneous Verified Agent Actuation): **runtime/OS/platform track; no hardware justification by default**.
- B-residual (Semantic-to-Physical State Coherence): **runtime/NPU/memory-system first; reserve only**.
- Candidate C (System-Control Substrate): **runtime/OS/system first; Strategic Enabler unless promoted**.
- M2/M3b/C1-D2: **reserve-only hardware hypotheses**.

## Required evidence
- Stage12 device-free break-even maps;
- target-device trace/PMU when environment is available;
- strong B4/B5/B6 comparison;
- software-capture ratio;
- direct decision-critical patent claim review before final investment wording.


## Stage 15 hardware gate

No lane reaches uArch by roadmap date alone.

Required progression:
```text
STRUCTURAL_SIGNAL
→ SYSTEM_VALUE
→ SOFTWARE_INSUFFICIENCY
→ hardware-specific cause
→ UARCH_CANDIDATE
```

Hardware-specific cause may include:
- sub-ms reaction that software cannot meet;
- low-energy always-available control;
- inaccessible CPU-local state;
- wake/context-restore cost;
- stable hardware resource guarantee.

If runtime/OS/system captures the value, the correct decision is to stop before uArch.


## Stage 15C boundary correction

Cordon/TomasuLLM strengthen the case that substantial Effect/Commit legality can stay in a transaction-aware runtime.

Therefore:
- do not export raw Agent Effect/Commit merely to recreate a safety decision lower layers can receive as CancelPermission/ReleasePermission;
- treat DemandState as the primary differentiated Agent-native input;
- only move legality below runtime when a lower-layer action needs information that cannot be safely derived/translated above it.

Separately, Arm SME2/SMEPilot evidence opens a **CPU-resident AI execution** path, but this is a compute-placement/ISA-runtime question rather than a semantic-hint justification.
