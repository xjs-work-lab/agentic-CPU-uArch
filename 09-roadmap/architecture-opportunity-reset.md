# Architecture Opportunity Reset — Agentic Mobile 2027–2029

Updated: 2026-10-08
State: ROUND15_STARTING_POINT

## Why this reset

Earlier portfolio convergence correctly improved evidence depth and prior-art discipline, but it became too restrictive for a public-evidence-only foresight project.

The corrected question is not:
> Which hardware idea can we prove on a target phone today?

It is:
> Which Agentic-era workload changes plausibly demand new cross-layer designs, which mechanisms are academics/competitors already exploring, and where should a mobile CPU/SoC team place research and product technology bets?

## Core architecture themes

### AO-1 — Agent Execution Fabric: heterogeneous CPU/GPU/NPU orchestration
**Posture: FOLLOW + HIGH-PRIORITY CO-DESIGN**

Structural change:
Agent workloads repeatedly move among reasoning/model execution, tool execution, orchestration, state access and action.

Public signals:
- academic workload characterization finds fragmented/bursty Agent execution with CPU on the critical path and locality pressure;
- orchestrator↔engine co-design work shows semantic/runtime information can improve cache and overlap;
- mobile vendors now explicitly position CPU, NPU, shared memory/cache and scheduling as an Agentic system.

Software/compiler levers:
- Agent/workflow IR;
- stage/operator/sub-operator lowering;
- model/precision selection;
- dynamic CPU/GPU/NPU placement;
- asynchronous dispatch;
- persistent sessions;
- data-layout/state-reuse planning.

Architecture hypotheses:
- lower-latency cross-xPU command path;
- persistent execution contexts;
- coherent/shared state closer to CPU/NPU;
- shared or flexible cache/memory pools;
- efficient scalar/vector/matrix support for orchestration + residual AI kernels;
- hardware-visible lightweight stage/priority metadata.

Important boundary:
do not reduce this to “CPU beats NPU.”
The opportunity is the **fabric and handoff/control path**.

### AO-2 — Revisable + Transactional Agent Execution
**Posture: HIGH-INTEREST ACADEMIC-LEAD OPPORTUNITY**

Structural change:
Agent tasks are revised, interrupted, speculated, cancelled and may create irreversible side effects.

Academic signals:
- versioned execution separates authority from resources and preserves compatible state;
- semantic transaction systems introduce task-level commit/rollback/lineage;
- speculative-action systems execute predicted future actions before authoritative confirmation.

Software/runtime levers:
- execution epochs / versions;
- commit/abort boundaries;
- effect outbox / shadow state;
- dependency lineage;
- selective inheritance after revision;
- cancelable speculative work.

Architecture hypotheses:
- cheap epoch/version tags attached to queued xPU work/state;
- fast cancellation and resource reclamation;
- low-overhead shadow/checkpoint state for reversible work;
- copy-on-write / selective preservation assistance;
- accelerator command queues with cancel/commit semantics;
- rapid invalidation of obsolete derived state.

Why interesting:
this is one of the clearest areas where **academic abstractions are forming before a standard mobile product architecture has stabilized**.

Boundary:
existing software systems prove the abstraction can exist in software; hardware value is a research hypothesis, not a conclusion.

### AO-3 — Persistent Agent State / Context Fabric
**Posture: FOLLOW + DIFFERENTIATION SEARCH**

Structural change:
Agent execution repeatedly re-enters models/tools while carrying long-lived KV, context, plans, tool outputs, memory, adapters and versioned intermediate state.

Public signals:
- Agent workload studies show repeated model re-entry and growing dependence on persistent KV/cache state;
- serving systems increasingly co-design scheduling with multi-tier state placement;
- mobile vendors are enlarging shared/on-chip memory and flexible cache structures for Agentic workloads.

Software/runtime levers:
- state identity and lifetime;
- version/provenance;
- multi-tier placement;
- prefetch/reuse prediction;
- selective invalidation/preservation;
- memory-pressure policy.

Architecture hypotheses:
- flexible on-chip shared memory/cache allocation across heterogeneous engines;
- cross-engine coherent state residency;
- state lifetime classes / epoch tags;
- low-cost tier migration;
- retained working-set domains across short Agent pauses;
- hardware support for state handoff without full serialization/copy.

Boundary:
generic cache/KV management is crowded.
The opportunity is **Agent state lifecycle + cross-engine/mobile memory economics**, not “invent a cache.”

### AO-4 — Always-On Proactive Personal-Agent Front End
**Posture: PRODUCT TREND + CO-DESIGN FOLLOW**

Structural change:
user interaction shifts from explicit prompt→response toward continuous context observation, intervene-or-stay-silent gating and proactive assistance.

Evidence:
- proactive-mobile research formalizes latent-intent inference from device context;
- Qualcomm/MediaTek publicly position always-on sensing/AI domains and ultra-efficient NPU paths for personal Agent experiences.

Software/model levers:
- intervention gating;
- context compression;
- event coalescing;
- hierarchical small-model→large-model escalation;
- privacy/consent policy.

Architecture hypotheses:
- ultra-low-power always-on Agent island;
- retained SRAM/context buffer;
- event-driven sensor→gate path;
- small scalar/vector/tensor front end;
- fast wake/handoff to main NPU/CPU;
- compute-in-memory or similarly low-energy gating where appropriate.

Boundary:
this is already entering product.
Research value is in **best architecture split and cross-domain handoff**, not claiming the idea is globally new.

### AO-5 — Semantic Progress / QoE Control Plane
**Posture: DIFFERENTIATION SEARCH / CROSS-LAYER BET**

Structural change:
Agent work has semantics not captured by classic runnable/priority/deadline alone:
- required vs optional/speculative;
- goal survival;
- revision/invalidity;
- effect reversibility;
- confidence;
- user-interaction boundary;
- useful progress.

Academic signals:
orchestrator/engine co-design and Agent-aware schedulers increasingly expose workflow semantics to lower layers.

Software/compiler levers:
- Agent IR with progress/effect/state annotations;
- propagation to runtime/OS;
- utility/QoE-aware scheduling;
- resource reservation/cancellation;
- state-retention hints.

Architecture hypotheses:
- lightweight metadata carried with work queues/memory state;
- semantic-aware xPU admission/preemption;
- progress/commit-aware retention and wake policies;
- low-cost OS↔CPU/NPU control channel.

Boundary:
“semantic scheduling” broadly is old/crowded.
The research question is whether **Agent-native semantic fields create useful control information that ordinary history/SLO/runtime state cannot reconstruct**.

## Secondary / watch themes

### Agent continuation locality
Keep as a mechanism under AO-1/AO-3.
Potential levers: fast wake, warm-core reuse, retained cache/TLB/predictor state.
Prior-art pressure is high, so do not treat generic microstate save/restore as a standalone Bet.

### Local multi-Agent concurrency
Keep as workload pressure on AO-1/AO-3/AO-5.
Look for shared model/KV/adapters, QoS and interference problems before creating a new architecture.

### Dynamic skills / local code
Keep WATCH.
Reopen architecture work only if public evidence shows substantial mobile interpreter/JIT/code-cache/sandbox-transition pressure.

### Cross-device continuation
Keep product trend.
Architecture opportunity is more likely state packaging/memory/continuity fabric than a unique CPU primitive.

## What changed relative to the prior portfolio

Do **not** discard:
- A / semantic-progress research;
- CG-06 / heterogeneous fast path;
- PT-A / verified actuation;
- C / system-control substrate;
- state lifecycle;
- always-on trend;
- prior-art analyses.

Reframe:
- A becomes one component of a broader semantic-control-plane theme;
- CG-06 becomes AO-1 heterogeneous Agent Execution Fabric, not only CPU-vs-NPU crossover;
- B-residual/R2/CG-01 become pieces of AO-3 state/context fabric;
- PT-A + speculative/versioned systems motivate AO-2;
- CG-07 remains AO-4;
- R3 should not be treated as “no hardware ideas”; it means no **committed D2 hardware mechanism** yet.

## Round 15 research questions

1. Which architecture themes already have sustained academic lineages rather than isolated papers?
2. Which are now appearing in Qualcomm/MediaTek/Arm/Android product architecture?
3. For each theme, what has been solved in software and what remains structurally expensive?
4. Which mobile constraints change the answer versus datacenter work?
5. What concrete CPU/SoC mechanisms are plausible without inventing unjustified new ISA?
6. Which mechanisms are likely 2027 product-follow, 2028 co-design, or 2029 architecture reserve?
7. Which themes deserve 2–3 Primary Architecture Bets under a **public-evidence foresight** standard?

## Current provisional priority

1. AO-1 Heterogeneous Agent Execution Fabric
2. AO-2 Revisable / Transactional Agent Execution
3. AO-3 Persistent Agent State / Context Fabric
4. AO-5 Semantic Progress / QoE Control Plane
5. AO-4 Always-On Proactive Front End

This ranking is a Round-15 starting hypothesis, not final convergence.


## V2.4 graph state
AO-1..AO-5 are now canonical ARCHITECTURE_OPPORTUNITY nodes.

The prose in this file remains the Round-15 starting synthesis.
Detailed evidence roles move into the AO objects and their linked Claims/Evidence Cases.

Round 15A completion requires each AO to expose:
Problem Signal → Existing Mechanism → Strongest Baseline/Prior Art → Open Gap → Architecture Hypothesis,
with important negative pressure represented through REBUT / UNDERCUT / SCOPE_LIMIT where appropriate.
