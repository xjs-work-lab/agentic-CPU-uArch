# PAPER-073 — Beyond Training: Enabling Self-Evolution of Agents with MobiMem

## Source
- arXiv:2512.15784, 2025 preprint
- Authors: Shanghai Jiao Tong University IPADS + collaborators
- Workloads: AndroidWorld + real-world top-50 mobile applications
- On-device platform: Qualcomm Snapdragon 8 Elite with llama.cpp
- Cloud/reference platforms: Intel Xeon Platinum 8378A + NVIDIA A100; Ascend 910B also used in hardware comparison
- Agent models include MobiMind-4B, UI-TARS-1.5-7B, GUI-Owl-7B, Qwen3-VL-30B-A3B and Gemini-2.5-Flash depending experiment
- Priority: P0

## Q1 — Problem + target mapping
Mobile/desktop Agents need to improve after deployment without repeatedly retraining model weights.

MobiMem reframes this as a memory-system problem with three distinct long-lived memory classes:
- **Profile Memory** — user facts/preferences/behavior;
- **Experience Memory** — reusable task logic/templates;
- **Action Memory** — reusable fine-grained UI action sequences.

These memories are coupled to OS-inspired services:
- Agent Scheduler;
- Agent Record-and-Replay (AgentRR);
- Agent Exception Handler.

Project mapping:
this is the strongest direct evidence so far that an Agent-memory lifecycle contains **operation classes with different execution semantics**, not merely one vector-search API.

## Q2 — Novelty / new-regime relevance

### Profile Memory
Uses DisGraph:
- semantic information stored in concept/entity nodes rather than expensive semantic edges;
- one LLM call on update;
- vector search selects entry nodes;
- zero-LLM BFS/graph traversal performs retrieval.

### Experience Memory
Distills execution traces into multi-level templates:
- invariant control logic;
- variable parameter slots;
- reusable subtask/step dependencies.

### Action Memory
Stores interaction trajectories in:
- ActTree for prefix reuse;
- ActChain for prefix + suffix reuse tied to experience templates.

### OS integration
Memory state directly feeds:
- fine-grained step DAG scheduling;
- action record/replay;
- stale-action verification and fallback;
- interruption/exception recovery and template evolution.

Classification:
**DIRECT_AGENTIC memory + mobile execution evidence**, but mechanisms are software/runtime/OS-level.

## Q3 — Falsifiable hypothesis

Core hypothesis:
> If different kinds of Agent experience are represented by specialized memory structures and connected to execution services, then a deployed Agent can improve personalization, capability and efficiency without continual model retraining.

Falsifiers:
- specialized memories provide no gain over generic RAG/trace replay;
- template abstraction fails to generalize;
- replay miss/staleness rate eliminates latency benefit;
- verification/recovery overhead dominates;
- memory writes/maintenance become too expensive;
- real phone inference remains dominant despite reuse;
- cross-app dependencies are too dynamic for DAG reuse.

The reported experiments support the hypothesis in the evaluated Android workloads.

## Q4 — Research lineage / competing route

Strong competing routes:
- vanilla RAG;
- GraphRAG / Mem0-like graph memory;
- MemGPT/A-MEM conversational memory;
- AutoDroid-style app/trace memory;
- AutoDroid-V2 task-level code/script lowering;
- M3-Agent long-term multimodal memory;
- generic vector indexes such as MUSE/LEANN/CD-ANN;
- continual fine-tuning / RL;
- ordinary system record-and-replay.

Important distinction:
MobiMem's novelty is not merely persistent storage. It assigns different semantics to profile, execution experience and actions, then exploits those semantics in execution services.

## Q5 — Key mechanism / control point

### 1. Profile Memory — DisGraph
Profile update:
- extracts/classifies user facts/preferences;
- attaches them to concept/entity nodes;
- avoids expensive semantic-edge maintenance.

Profile retrieval:
- embedding search finds starting nodes;
- BFS traverses concept/entity structure;
- no LLM call during graph traversal.

### 2. Experience Memory — multi-level templates
Execution histories are abstracted into reusable templates with:
- invariant steps;
- variable slots;
- explicit subtask/step dependencies.

Templates reduce reasoning load and expose dependency DAGs to the scheduler.

### 3. Action Memory — ActTree / ActChain
ActTree:
- app-level UI-state/action tree;
- prefix reuse.

ActChain:
- experience-template-specific action sequences;
- prefix/suffix reuse;
- invariant steps replay directly;
- variable steps replay only when parameter values match, otherwise fall back to fresh LLM reasoning.

### 4. Correctness check + rollback
Before replay, MobiMem validates target UI state/element using UI hierarchy fields such as resource ID, class and text plus fuzzy matching.

On mismatch/staleness:
- discard cached action;
- fall back to Operator Agent;
- record new trace;
- update stale Action Memory.

### 5. Agent Scheduler
Uses Experience Memory dependencies to exploit:
- planning-time parallel profile/template retrieval;
- coarse application-level parallelism;
- fine-grained step-level DAG parallelism.

### 6. AgentRR
Records:
- screenshots/UI hierarchy;
- decision context;
- actions;
- template/action mapping.

Replay is semantic/adaptive rather than deterministic system replay.

### 7. Exception Handler
On user interruption or conflicting manual UI action:
- suspend current execution;
- preserve UI state, partial plan and action history;
- yield control to user;
- integrate user corrections;
- update improved experience templates.

### Project interpretation
Agent memory operation semantics **are already consumed by upper-layer execution software**.

This matters twice:
- it supports H-PAM's premise that memory classes are operationally different;
- it raises the strongest baseline, because a large part of their value is already captured without new CPU/uArch mechanisms.

## Q6 — Experiment design

### Profile Memory
Synthetic user-profile benchmark:
- 500 historical tasks per user;
- 30 ambiguous test tasks;
- metrics: write latency, retrieval latency, profile alignment;
- baselines: Vanilla RAG and GraphRAG/Mem0-style graph.

Reported:
- Vanilla RAG: 66.4% alignment, 1.76 ms write, 19.58 ms retrieval;
- GraphRAG: 81.1%, 37.69 s write, 6.68 s retrieval;
- MobiMem DisGraph: **83.1%**, **6.14 s write**, **23.83 ms retrieval**.

Scaling:
- 100 → 100,000 profile nodes;
- graph traversal remains ~0.15–0.35 ms;
- total retrieval grows to ~1.29 s at 100k nodes / ~135 MB, dominated by initial vector search.

### Experience Memory
AndroidWorld:
- 116 tasks / 20 Android apps;
- four Agent models compared with/without experience templates.

Reported:
- up to **50.3% relative success improvement** for UI-TARS-1.5-7B;
- roughly 21–22% for stronger Gemini/Qwen models;
- 10.5% for GUI-Owl;
- 116 templates consume ~900 KB total.

ID/OOD real-world tasks:
- larger relative gains on OOD workloads;
- reported ~44.1% OOD vs ~22.0% ID improvement for the evaluated UI-TARS setup.

### Action Memory
Workload:
- 454 tasks across email, train, food, hotel, shopping, browser, media and maps.

Reuse:
- ActTree prefix-only: 37.5% average;
- ActChain + LLM-generated templates: 59.7%;
- ActChain + human-crafted templates: **77.3%**.

Memory footprint:
- ~1.54 MB for ~6,000 cached actions.

### Hardware comparison
MobiMind-4B:
- A100 baseline average ~14.1 s;
- Ascend 910B ~27.4 s;
- Snapdragon 8 Elite ~153.2 s without Action Memory in the reported CPU-only on-device setup.

With Action Memory:
- mobile task speedup **1.6×–9×** depending task;
- A100 still gets 1.3×–2.1× from avoiding redundant inference.

Interpretation:
Action Memory mainly shifts the bottleneck from expensive LLM inference toward lightweight UI/action execution.

### Multi-task scheduling
Fine-grained Experience-Memory-derived dependency scheduling:
- coarse app-level parallelism up to 1.41×;
- fine-grained scheduling up to **1.98×**;
- example multi-shop+social: 48.27 s serial → 37.65 s coarse → 29.84 s fine-grained.

## Q7 — Data / artifact / reproducibility

Strengths:
- real Android workloads;
- AndroidWorld benchmark;
- top-50-app scenarios;
- direct Snapdragon 8 Elite evaluation;
- multiple Agent models;
- memory size/retrieval/reuse/success/latency quantified;
- source reports Experience Memory + AgentRR already deployed on a flagship smartphone.

Limitations:
- preprint, not peer-reviewed publication in current review;
- no public artifact/repository identified in this review;
- flagship deployment statement is author-reported;
- real deployments still use cloud inference for strict latency; on-device Snapdragon path uses llama.cpp and is CPU-only in the reported comparison;
- no direct NPU/memory-bandwidth/thermal profiling;
- Profile Memory update is still dominated by an LLM call;
- exact deployment architecture/product is not independently verified.

## Q8 — Evidence vs hypothesis

### [FACT — evaluated]
Different Agent memory classes have different operations, data structures, validity rules and execution effects.

### [FACT — evaluated]
Experience Memory exposes step dependencies that enable fine-grained parallel scheduling.

### [FACT — evaluated]
Action Memory exposes replayable vs stale/non-replayable actions and can replace substantial on-device LLM inference.

### [FACT — evaluated]
Profile retrieval cost becomes dominated by vector-start search as the profile grows, while graph traversal itself stays small.

### [SOURCE CLAIM]
Experience Memory and AgentRR are reported as deployed on a flagship smartphone.

### [OBSERVATION]
Agent memory lifecycle semantics can change control flow and scheduling, not just lookup accuracy.

### [INFERENCE — project]
H-PAM's strongest remaining question is **not whether memory operation classes exist**—MobiMem shows they do.

It is whether those classes expose a lower-level mobile systems residual **after** template/replay/DAG/exception software captures their value.

### Not established
- direct CPU/NPU/DDR operation-class mapping;
- memory-bandwidth/thermal benefit;
- persistent background ingestion duty cycle comparable to MUSE;
- hardware insufficiency;
- uArch requirement.

## Q9 — Real contribution to project decision

### H-PAM
**KEEP / NARROW. Do not promote.**

MobiMem strengthens H-PAM in one important way:
> Agent memory types and lifecycle states directly affect execution semantics (parallelizability, replayability, validity, recovery).

But it weakens any broad substrate claim because:
- profile retrieval is solved through software graph/vector structure;
- experience value is consumed through templates and DAG scheduling;
- action-memory value is consumed through application/OS replay and validation;
- exceptions are handled through context capture + template evolution.

Therefore the surviving H-PAM residual becomes:
> Do Agent-memory lifecycle states change **CPU/NPU/memory/data-placement decisions** in ways that MobiMem-style upper-layer execution plus MUSE/LEANN/CD-ANN-class storage/search software cannot capture?

### PT-A
MobiMem strongly reinforces PT-A concepts around:
- verified action reuse;
- stale-action detection;
- rollback/fallback;
- execution context capture;
- interruption recovery.

However PT-A already owns this platform territory; do not create a second memory-specific actuation lane.

### A
Experience templates and dependency DAGs further strengthen B4-TX reconstructible control-flow baselines.

### B-residual
Stale Action Memory is a concrete example of validity/invalidation, but it is UI-state/action validity rather than the broader semantic-to-physical lineage residual.

### C / hardware
No new differentiated system-control or uArch evidence.

## Q10 — Next action

1. KEEP PAPER-073 as P0, but mark publication boundary as preprint.
2. Add a canonical Claim: specialized Agent memory lifecycle states can drive different execution services.
3. Strengthen H-PAM strongest baseline with MobiMem-style upper-layer capture.
4. Do **not** promote H-PAM.
5. Find an independent Agent-memory architecture with explicit update/consolidate/forget/retrieve operations.
6. Prefer a source with direct phone/system-cost measurements; otherwise use it only to establish cross-framework recurrence of operation classes.
7. Keep the MobiSys 2026 memory-architecture benchmark PENDING_FULLTEXT until full text is available.

## Decision footer
- **New-regime relevance:** DIRECT_AGENTIC / mobile execution
- **Evidence maturity:** SYSTEM_VALUE for memory-centric Agent software on evaluated Android workloads; publication boundary = preprint
- **H-PAM impact:** KEEP / NARROW; no Direction
- **PT-A impact:** strong contextual support / no lane change
- **A impact:** stronger software baseline / no lane change
- **hardware impact:** none
- **Open questions:** recurring operation classes across independent systems, phone duty cycle, CPU/NPU/data-placement residual, energy/thermal, Huawei transfer
- **Primary source:** https://arxiv.org/abs/2512.15784