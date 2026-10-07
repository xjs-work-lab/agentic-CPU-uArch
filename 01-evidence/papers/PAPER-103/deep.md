# PAPER-103 — Beyond Training: Enabling Self-Evolution of Agents with MobiMem

## Source
- Primary: https://arxiv.org/abs/2512.15784
- Submitted: 2025-12-15
- Authors: Zibin Liu, Cheng Zhang, Xi Zhao, Yunfei Feng, Bingyu Bai, Dahu Feng, Erhu Feng, Yubin Xia, Haibo Chen
- Affiliation: IPADS, Shanghai Jiao Tong University
- Artifact lineage: https://github.com/IPADS-SAI/MobiAgent
- Review: FULL_10Q / EDP v1
- Priority: P0

## Q1 — Problem + target mapping
MobiMem asks how a deployed mobile/desktop Agent can improve after deployment without repeatedly fine-tuning its model.

It decomposes “self-evolution” into:
1. learning user preferences;
2. expanding task capability;
3. reducing repeated execution cost.

Target mapping for this project:
> does persistent Agent state become a reusable product-level resource on smartphones, and does a multi-Agent architecture create a distinct CPU/system control point beyond ordinary software-visible workflow/state management?

The paper is directly relevant to **T5 Agent state lifecycle/reuse** and is a discriminating pressure source for **T7 local multi-Agent concurrency**.

## Q2 — Novelty / new-regime relevance
The important idea is not merely “memory for Agents.”

MobiMem composes three memory classes with OS-like services:
- Profile Memory — persistent preference/fact state;
- Experience Memory — parameterized procedural templates;
- Action Memory — reusable concrete GUI action state;
- Agent Scheduler — parallel planning/execution and background memory work;
- AgentRR — record/replay with validation;
- Exception Handler — suspend/preserve/recover after user/runtime interruption.

Classification:
**AMPLIFIED / Agent-native composition.**

Graph memory, record/replay and DAG scheduling are mature primitives. The Agent-specific shift is that a long-lived Agent accumulates reusable semantic, procedural and action state whose validity and usefulness change across tasks and UI revisions.

This is a strong product trend even though the broad mechanisms are not globally novel.

## Q3 — Falsifiable hypothesis
Primary paper hypothesis:
> structured external memory can capture a large fraction of post-deployment Agent improvement more cheaply than continual model training.

Operational predictions:
- structured profile memory should improve retrieval/alignment without GraphRAG-scale latency;
- reusable experience templates should improve task success with less data/compute than fine-tuning;
- action replay should reduce model calls and latency when workflows recur;
- fine-grained dependency scheduling should beat serial/coarse execution for multi-app tasks.

Project-specific T7 hypothesis:
> if “multiple local Agents” itself creates a new system regime, MobiMem should expose a repeated resource/control variable that cannot be represented as ordinary DAG dependency, queue priority, state validity or replay eligibility.

The paper supports the first set but does **not** establish the T7-specific hypothesis.

## Q4 — Research lineage / competing route
MobiMem belongs to the same IPADS-SJTU lineage as MobiAgent (arXiv:2509.00531).

MobiAgent already introduced:
- Planner / Decider / Grounder role decomposition;
- AgentRR;
- ActTree experience replay;
- reported 2–3× latency optimization in recurring mobile tasks.

MobiMem extends this trajectory toward:
- explicit Profile / Experience / Action memory;
- ActChain prefix-suffix reuse;
- multi-task scheduling;
- exception handling;
- memory-centric “self-evolution.”

Therefore MobiMem and MobiAgent are **trajectory evidence, not independent replication**.

Competing routes include:
- per-user fine-tuning / RL;
- Vanilla RAG / GraphRAG / Mem0 / A-MEM;
- AutoDroid-style trace memory;
- sequential GUI-Agent execution;
- ordinary DAG schedulers and record/replay systems.

## Q5 — Key mechanism / control point

### 1. Profile Memory / DisGraph
- concept + entity nodes;
- semantics moved into nodes;
- edges encode membership/relevance rather than LLM-generated semantic relations;
- one LLM call for update;
- embedding + graph traversal for zero-LLM retrieval.

### 2. Experience Memory
- separates invariant control flow from variable parameters;
- stores multi-level templates;
- Task Rewriter fills slots for a concrete request;
- Experience Generator creates new templates after successful novel execution.

### 3. Action Memory
Two structures:
- **ActTree** — prefix reuse for tasks sharing early UI states/actions;
- **ActChain** — prefix-suffix reuse when an experience template identifies invariant vs variable steps.

A lightweight predictor controls reuse eligibility.

### 4. Correctness check / fallback
Before replay:
- current UI hierarchy/XML is examined;
- target element properties such as resource ID, class and text are matched;
- fuzzy matching tolerates small variations.

If validation fails:
- cached action is discarded;
- execution falls back to Operator/LLM reasoning;
- the new trace updates action memory.

This is an important software baseline for PT-A-style verified execution.

### 5. Agent Scheduler
Planning:
- Profile Memory and Experience Memory retrieval can run concurrently.

Execution:
- app-level independent subtasks can overlap;
- step-level DAG dependencies allow downstream preparation before all upstream work completes;
- background memory update work can be prioritized separately.

## Q6 — Experiment design

### Profile Memory
Benchmark construction:
- synthetic user profiles;
- 500 historical tasks per user;
- 30 ambiguous test tasks;
- LLM-assisted required-profile generation and LLM judging.

Reported:
- Vanilla RAG: 1.76 ms write / 19.58 ms retrieval / 66.4% alignment;
- GraphRAG: 37.69 s write / 6.68 s retrieval / 81.1%;
- MobiMem DisGraph: 6.14 s write / 23.83 ms retrieval / 83.1%.

Important boundary:
this is a synthetic-profile + LLM-judge benchmark, not a longitudinal real-user phone study.

### Experience Memory
Reported across multiple GUI-Agent models:
- task-success improvement up to 50.3%.

Cost comparison:
- fine-tuning: ~100 examples, 4 person-hours, 0.25 GPU-hours, 58.5% accuracy;
- manual templates: ~5 examples, 0.2 person-hours, 0 GPU-hours, 63.5%;
- automatic templates: ~5 examples, 0 person-hours, 0.0027 GPU-hours, 60.1%.

### Action Memory
Workload:
- 454 tasks;
- 8 categories: email, train ticketing, food delivery, hotel booking, shopping, browser, media playback, maps.

Average reuse:
- ActTree: 37.5%;
- ActChain + LLM template: 59.7%;
- ActChain + human template: 77.3%.

Model latency with human-template ActChain:
- MobiMind-4B: 14.1 s → 8.6 s;
- UI-TARS-1.5-7B: 14.7 s → 8.8 s;
- GUI-Owl-7B: 38.0 s → 16.2 s;
- high-reuse task classes report up to 4.5×.

Memory footprint:
- ~1.54 MB for ~6,000 cached actions.

### Cross-hardware Action Memory
MobiMind-4B:
- A100: baseline average 14.1 s;
- Ascend 910B: 27.4 s;
- Snapdragon 8 Elite: 153.2 s baseline in a **CPU-only** llama.cpp configuration.

On the Snapdragon setup, Action Memory reports **1.6×–9×** speedup across tasks by bypassing repeated inference.

This is direct phone value for software replay, but it is not an optimized phone NPU comparison.

### Multi-task scheduler
Six multi-app categories combine search / shop / social workflows.

Reported:
- coarse-grained: up to 1.41× over serial;
- fine-grained: up to 1.98× over serial.

Representative multi-shop+social:
- serial 48.27 s;
- coarse parallel 37.65 s;
- fine-grained 29.84 s.

The causal lever is explicit step dependency/DAG overlap, not an isolated multi-Agent hardware state.

## Q7 — Data / artifact / reproducibility

### Strengths
- direct Android/mobile workload focus;
- real top-app workflows in addition to AndroidWorld;
- public IPADS-SAI MobiAgent repository includes AgentRR, memory and multi-task code paths;
- concrete action-reuse, latency, memory and scheduler measurements;
- cross-hardware evaluation includes Snapdragon 8 Elite.

### Important limitations
1. **Publication status:** current source is an arXiv preprint; no peer-reviewed venue was verified.
2. **Lineage:** AgentRR overlaps prior MobiAgent work from the same group.
3. **Phone path:** the reported Snapdragon Action Memory experiment is CPU-only; it does not establish value over an optimized NPU/GPU Agent path.
4. **Scheduler hardware:** the paper reports multi-app scheduler speedups, but the exact hardware placement of the 1.98× experiment is not clearly isolated as a Snapdragon-phone system result.
5. **Profile benchmark:** synthetic users/tasks plus LLM judging limit external validity.
6. **Human templates:** the highest 77.3% Action Memory reuse relies on human-crafted templates.
7. **Artifact completeness:** the public repo exposes AgentRR/multi-task/experience paths, while ActChain integration is described in the repo as still experimental/integration work.
8. **Product deployment:** the paper says **Experience Memory and AgentRR** are deployed in a flagship smartphone, but does not identify the product/vendor, provide independent corroboration, or claim the full MobiMem stack is deployed.
9. **Missing phone metrics:** no battery, rail energy, thermal, foreground-app QoE or silicon-cost evidence.

## Q8 — Evidence vs hypothesis

### [FACT]
MobiMem demonstrates that reusable action/experience state can materially reduce repeated model inference in evaluated mobile Agent tasks.

### [FACT]
Its replay path checks current UI state and falls back to model execution when cached actions become invalid.

### [FACT]
On the reported Snapdragon 8 Elite CPU-only setup, software Action Memory produces large task-level latency gains.

### [FACT]
Fine-grained workflow dependencies allow step-level overlap and materially reduce end-to-end time in evaluated multi-app tasks.

### [CLAIM — authors]
Experience Memory and AgentRR have been deployed in a flagship smartphone.

### [INFERENCE — project]
MobiMem strongly strengthens **T5 product relevance** but primarily raises the software/runtime baseline.

### [INFERENCE — project]
MobiMem does not establish that multiple local Agent identities create a distinct physical/resource-control state. Its measured gains are explainable by software-visible DAG, reuse eligibility, state validity and replay/fallback state.

## Q9 — Real contribution to the project decision

### T5 — strengthened
MobiMem is direct evidence that:
- procedural/action state can be treated as a reusable product resource;
- state validity matters;
- reuse can change the economic balance between repeated local inference and deterministic execution.

This supports keeping:
**T5 = EMERGING_PRODUCT_TREND / ADAPT_AND_DIFFERENTIATE**

No maturity promotion yet because:
- the strongest phone result is CPU-only;
- the product deployment statement is component-scoped and not independently corroborated;
- MobiMem/MobiAgent are one research lineage.

### T7 — narrowed
The paper has a “Multi-Agent Layer,” but:
- specialized roles are logical decomposition;
- the key scheduler consumes ordinary step dependencies;
- memory/replay state is explicit software state;
- it does not isolate simultaneous local multi-Agent shared-model/CPU/NPU/memory contention.

Therefore:
**T7 remains FRONTIER_SIGNAL / WATCH.**
No new Direction from MobiMem.

### C / PT-A — strongest-baseline pressure
- C must already assume fine-grained workflow-DAG scheduling and overlapping independent steps.
- PT-A must already assume replay validity checks + fallback rather than blind action caching.

### CPU/uArch
MobiMem gives **negative pressure on premature hardware conclusions**:
a large fraction of apparent “mobile Agent compute cost” can disappear when software reuses validated execution state instead of re-running a model.

No software-insufficiency or hardware-specific cause is established.

## Q10 — Next action
1. Keep MobiMem as P0 / FULL_10Q decision-critical evidence.
2. Add its direct phone replay result to T5 product evidence.
3. Do not create a T7 Direction.
4. Do not promote T5 maturity yet.
5. Make validated action/experience reuse part of the strongest software baseline for later CPU/NPU/uArch claims.
6. Deep-read **LOCAL** next because it is a stronger discriminator for T7: multiple Agents share one model, KV cache, adapters and memory budget.
7. Then deep-read EcoAgent before final T7 ownership decision.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE for software memory/replay on evaluated mobile workloads; FRONTIER_SIGNAL only for T7
- **Decision impact:** strengthen T5 product trend; narrow T7; raise C/PT-A software baseline; no new Direction
- **Open questions:** optimized phone NPU baseline, energy/thermal/QoE, independent product corroboration, local multi-Agent resource contention
- **Primary source:** https://arxiv.org/abs/2512.15784
- **Artifact lineage:** https://github.com/IPADS-SAI/MobiAgent
