# Round 14-A — T7 Local Multi-Agent Concurrency Seed Triage

Date: 2026-10-07
State: SEED_TRIAGE_COMPLETE / NOT DECISION-COMPLETE

Question:
> Does local multi-Agent execution create a distinct smartphone system/physical control problem beyond ordinary workflow scheduling/xPU orchestration (C) and state/KV/adapter lifecycle (T5/B)?

## Seed 1 — MobiMem
Primary: https://arxiv.org/abs/2512.15784

Why it matters:
- direct mobile/Android system;
- evaluates top-50 apps and AndroidWorld;
- includes specialized agents, three memory types, Agent Scheduler, AgentRR and exception handling;
- reports real Snapdragon 8 Elite measurements;
- Experience Memory + AgentRR are reported as deployed in a flagship smartphone.

Important measured signals:
- Action Memory average reuse up to 77.3% with human-crafted templates;
- mobile Action Memory speedup 1.6×–9× in reported Snapdragon 8 Elite CPU-only setup;
- fine-grained multi-app scheduling up to 1.98× over serial;
- representative multi-shop+social: 48.27 s serial → 37.65 s coarse parallel → 29.84 s fine-grained.

T7 interpretation:
- strong **product trend** signal for Agent memory/state reuse + fine-grained workflow parallelism;
- weak evidence that “multiple agents” itself is the new control point;
- scheduler mechanics look primarily C-like;
- Action/Experience Memory and replay look primarily T5/PT-A-like.

Pressure:
**MobiMem currently argues against a standalone T7 Direction unless a separate local multi-Agent physical residual appears.**

## Seed 2 — LOCAL
Primary: https://arxiv.org/abs/2608.15241

Why it matters:
- multiple Agents share one model instance;
- explicit agent/adaptor/KV provenance;
- cooperative foreground/background scheduler;
- cross-agent pre-prefill driven by pending Agent communication.

Reported setup:
- RTX 3090-class 24 GB single GPU;
- 7B-class model;
- real tau-bench retail workload.

Reported signals:
- foreground queue-wait p95 3.1× lower than FIFO;
- p95 TTFT 1.55× lower than non-preemptible training;
- cross-agent pre-prefill lowers TTFT p99 by 21.9%;
- adapter version and KV validity are jointly managed.

T7 interpretation:
- stronger evidence that multi-Agent identity/communication can become a reusable state signal;
- however the control points are still software-visible:
  scheduler priority, adapter version, KV provenance, memory pressure;
- no smartphone/phone SoC evidence.

Pressure:
**LOCAL strengthens T5/C and supplies a potential T7 residual seed, but not phone SYSTEM_VALUE.**

## Seed 3 — EcoAgent
Primary: https://ojs.aaai.org/index.php/AAAI/article/view/40230
Venue: AAAI 2026

Why it matters:
- explicit three-Agent mobile architecture;
- cloud Planning Agent;
- device Execution Agent;
- device Observation Agent;
- AndroidWorld evaluation.

Important boundary:
The “multi-Agent” decomposition is mainly logical role specialization and device-cloud collaboration.
The device-side Execution and Observation roles form a closed loop, but current evidence does not establish simultaneous local model execution or a distinct shared-resource concurrency bottleneck.

T7 interpretation:
- strong product architecture signal for hierarchical role decomposition;
- most control remains PT-A / C territory;
- not standalone evidence for a new CPU/uArch trend.

## Cross-seed synthesis

### Product trend
**KEEP T7 as a product trend candidate.**

The shift from monolithic Agent to specialized planners/executors/observers/memory updaters is real enough to track.

### New Direction
**NOT YET.**

Current mechanisms mostly collapse into existing ownership:
- DAG/subtask parallelism → C;
- agent/KV/adapter/version state → T5/B;
- verified replay and action validation → PT-A;
- device-cloud role placement → C / CG-06 boundary.

### Surviving T7 residual question
A standalone T7 Direction would require evidence that:
1. multiple local Agents are concurrently active on a representative phone;
2. they share model/KV/state or contend for CPU/NPU/memory in a repeated way;
3. the relevant control variable is not reducible to generic queue priority, DAG criticality, state versioning or cache reuse;
4. the residual has measurable end-to-end phone value.

## Next
FULL_10Q in this order:
1. MobiMem — strongest mobile/product seed.
2. LOCAL — strongest shared-model/state systems seed.
3. EcoAgent — peer-reviewed mobile multi-Agent architecture baseline.

After all three:
- NEW DIRECTION;
- MERGE INTO C;
- MERGE INTO T5/B/PT-A;
- WATCH;
- KILL differentiated novelty.

No score/lane/uArch change at seed-triage stage.
