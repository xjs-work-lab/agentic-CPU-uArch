# PAPER-089 — LOCAL: Enabling Learning On-device Contiguously for Agent LLMs

## Source
- arXiv:2608.15241, 2026 preprint
- authors: Nanjing University group
- evaluated on a single 24 GB consumer GPU with 7B-class models
- Priority: P0 Agent-native seed

## Q1 — Problem + target mapping
Local Agents repeatedly interact with one user, creating private traces that are useful for adaptation.
The target problem is **contiguous learning**: update the Agent from interaction feedback without suspending foreground inference.

This matters because it changes the execution regime from stable-weight serving to mixed:
- foreground inference;
- delayed reward/judge work;
- adapter training;
- adapter publication;
- KV-cache refresh/invalidations;
- multi-agent shared-model activity.

## Q2 — Novelty / new-regime relevance
The Agent-specific novelty is not generic fine-tuning alone.
LOCAL argues that ordinary inference runtimes assume stable weights, while RL systems assume separable accelerator resources.

Contiguous local Agent learning violates both assumptions.

Classification:
**NATIVE / Agent-contiguous-learning structural signal**.

## Q3 — Falsifiable hypothesis
If local Agents must learn from private interaction traces while remaining responsive, scheduling, adapter versioning and KV-cache validity cannot be managed independently.

Falsifiers:
- adaptation is infrequent enough to run only when the Agent is idle;
- cloud/federated training is acceptable;
- KV reuse can be safely discarded with negligible cost;
- training and inference can be isolated onto different accelerators without material overhead;
- personalization gains do not justify repeated local updates.

## Q4 — Research lineage / competing route
Competing routes include:
- static on-device inference;
- offline local fine-tuning;
- server/federated adaptation;
- inference runtimes with prefix/KV caching;
- distributed RL systems with separated rollout/training resources;
- generic foreground/background scheduling.

For this project, the key distinction is **evolving adapter state while an interactive Agent remains live**.

## Q5 — Key mechanism / control point
LOCAL exposes three shared control variables:
1. task priority / safe preemption boundary;
2. adapter identity + version;
3. KV-cache validity / residency.

Mechanisms:
- strict foreground-priority cooperative scheduler;
- version-aware KV cache key;
- adapter-scoped invalidation;
- hot-prefix refresh/offload;
- multi-agent identity/provenance over shared model state.

## Q6 — Experiment design
Prototype workload mixes foreground inference, judge inference, training and cache maintenance.

Reported results include:
- foreground queue-wait p95: 3.1× lower than FIFO;
- foreground queue p99: 3.4× lower than FIFO;
- TTFT p95: 1.55× lower than non-preemptible training;
- accumulated training blocking: 2.6× lower;
- post-publish first-hit prefill p99: 25.6% lower;
- cross-agent TTFT p99: 21.9% lower;
- peak GPU memory roughly 21.6–23.5 GB in tested workloads.

## Q7 — Data / artifact / reproducibility
Strengths:
- explicit mixed inference/training runtime;
- detailed mechanism decomposition;
- tail-latency and memory metrics;
- Agent identity/version semantics are explicit.

Limitations:
- preprint;
- single consumer GPU, not smartphone SoC;
- 24 GB memory budget is above common phones;
- no phone battery, rail power or thermal measurements;
- learning quality over long mobile sessions remains limited.

## Q8 — Evidence vs hypothesis
### [FACT]
Adapter updates invalidate KV tensors generated under older adapter versions.

### [FACT]
LOCAL demonstrates a software runtime that coordinates inference, training, versioning and cache management on one GPU.

### [OBSERVATION]
Agent learning introduces cross-layer state coherence that inference-only runtimes do not need.

### [INFERENCE — project]
This is a credible new workload family for the frontier reset, but LOCAL itself is a strong software-capture baseline.

## Q9 — Real contribution to project decision
Positive:
- provides an Agent-native reason to study concurrent learning + serving;
- exposes versioned model/KV state as a recurring control variable.

Negative:
- much of the residual maps naturally to existing lanes:
  - foreground/background scheduling → C;
  - semantic-to-physical version coherence → B-residual;
  - KV locality/cache behavior → R2 / CG-01;
- no CPU/uArch insufficiency is established.

## Q10 — Next action
1. KEEP as the primary Agent-native seed for the new frontier family.
2. Compare against real-phone training evidence and strong mobile training baselines.
3. Test whether any Agent-specific control variable survives after generic training/runtime software.
4. Do not create a Direction until smartphone SYSTEM_VALUE and software insufficiency are shown.

## Decision footer
- **Evidence maturity:** STRUCTURAL_SIGNAL / software SYSTEM_VALUE on non-phone GPU
- **Decision impact:** opens H-CAL analysis hypothesis; no Direction
- **Open questions:** phone duty cycle, energy/thermal, update frequency, foreground QoE, software-vs-hardware residual
- **Primary source:** https://arxiv.org/abs/2608.15241
