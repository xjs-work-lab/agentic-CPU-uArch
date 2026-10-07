# PAPER-104 — LOCAL: Enabling Learning On-device Contiguously for Agent LLMs

## Source
- Primary: https://arxiv.org/abs/2608.15241
- Submitted: 2026-08-15
- Authors: Xinxin Liu, Jiaxin Li, Zibo Wang, Yun Ji, Zhangqi Zhu, Qing Hu, Zhibin Wang, Rong Gu, Sheng Zhong, Chen Tian
- Affiliation: Nanjing University
- Publication state: arXiv preprint
- Artifact: no official public code repository was verified during this review
- Review: FULL_10Q / EDP v1
- Priority: P0

## Q1 — Problem + target mapping
LOCAL targets a runtime regime in which an Agent:
- serves interactive foreground requests;
- recovers delayed feedback through judge inference;
- trains LoRA adapters in the background;
- publishes new adapter versions;
- maintains/reuses KV state;
- potentially shares one model instance across multiple Agents.

All of this competes for one GPU and one memory budget.

Project mapping:
1. **T5:** does Agent state lifecycle now require version/provenance-aware validity, refresh and residency?
2. **T7:** do multiple Agents sharing one model create a control point that is not already representable by C scheduling and T5 state lifecycle?
3. **H-CAL:** does live serving + local adaptation expose a residual beyond software/runtime capture?
4. **uArch:** is any residual shown after strongest software control?

## Q2 — Novelty / new-regime relevance
LOCAL identifies two assumptions that fail under contiguous local learning:
- inference runtimes assume **stable weights**;
- distributed RL systems assume **separated resources**.

With live adapter updates on one device:
- old-version KV becomes invalid even if visible tokens are unchanged;
- foreground inference and training contend for the same accelerator;
- retained KV reduces training headroom;
- aggressive eviction destroys reuse;
- multiple adapters/Agents add provenance and validity dimensions.

Classification:
**AMPLIFIED / Agent-native composition.**

The component primitives are not individually new:
priority scheduling, LoRA serving, prefix caches, versioning, offload and prefetch all have prior art.

The new operating regime is their coupling under:
**long-lived Agent interaction + local adaptation + mutable inference state + one constrained model instance**.

## Q3 — Falsifiable hypothesis
Paper hypothesis:
> making adapter version, task priority and KV validity common runtime state allows foreground inference and background learning/cache maintenance to coexist more efficiently and correctly than independent subsystems.

Predictions:
- foreground-first cooperative admission should reduce latency tails over FIFO/round-robin;
- bounded training interruption should reduce foreground blocking;
- version-aware hot-prefix refresh should reduce first-hit post-publish prefill;
- cross-Agent future-consumer information should reduce downstream TTFT when reused context is predictable;
- memory-aware KV offload should preserve both foreground reserve and background progress.

T7-specific hypothesis:
> if multiple Agent identities introduce a new system control state, identity should remain necessary after conditioning on serialized context, namespace, adapter/version, pending consumers, resource demand and workflow dependency.

LOCAL's own design pressures this hypothesis **against** standalone identity:
Agent identity is stored as provenance, not always as a cache-validity key.

## Q4 — Research lineage / strongest competing routes

### Inference/runtime baselines
- vLLM / PagedAttention;
- SGLang prefix reuse;
- FlashInfer;
- Sarathi-Serve / serving schedulers.

### Multi-adapter / multi-Agent state baselines
- Punica;
- S-LoRA;
- LoRAX;
- LRAgent;
- ForkKV.

LOCAL explicitly states that it does **not** invent a new adapter algorithm or LoRA serving engine.

### RL/training baselines
- HybridFlow;
- OpenRLHF;
- ReaL;
- AReaL / other asynchronous RL frameworks.

Their stronger assumption is multiple/separated resources, unlike LOCAL's single-device setting.

### Project baseline
Within this repository:
- C already owns foreground/background admission, QoS and software-visible workflow scheduling;
- T5/B own state/version validity and reusable state lifecycle;
- H-CAL was already killed as a standalone Bet because adapter/KV lifecycle was expected to be software-visible.

LOCAL is therefore a strongest-baseline challenge, not a blank-slate Direction seed.

## Q5 — Key mechanism / control point

### 1. Cooperative scheduler
A single GPU admission point separates:
- foreground inference;
- judge inference;
- training;
- cache refresh/prefill.

Foreground has strict priority.
Background work is represented as bounded chunks with safe yield/commit boundaries.

This is software-visible scheduling state.

### 2. Version-aware KV-cache manager
Reusable KV validity key:

`(token span, context namespace, adapter, adapter version)`

Key consequence:
visible token-prefix equality alone is insufficient after adapter updates.

Logical validity is separated from physical residency using a radix-indexed prefix table.

### 3. Agent identity is provenance, not necessarily validity
LOCAL explicitly allows KV sharing across different producer Agents when:
- serialized prefix matches;
- context namespace matches;
- adapter matches;
- adapter version matches.

If role/private-memory/mailbox/communication differences matter, they are encoded into context namespace or adapter binding.

This is a critical T7 result:
**Agent ID itself is not demonstrated as a unique physical control variable.**

### 4. Stale-coverage prefill
After training generates a staged adapter version but before publication:
- hot prefixes are selected;
- bounded prefill work builds KV under the staged version;
- foreground continues using the last committed version;
- prefetched KV becomes visible only when publication/correctness conditions are satisfied.

Adapter readiness is separated from adapter visibility.

### 5. Cross-Agent pre-prefill
Pending multi-Agent communication proposes speculative prefix work for a downstream consumer.

Proposal contains:
- target Agent;
- context namespace;
- adapter/version;
- prefix span;
- covered length;
- estimated token cost;
- memory demand;
- downstream confidence;
- pending-consumer count.

The signal becomes predicted demand for ordinary cache/scheduler policy.

Thus cross-Agent semantics are converted into a software-visible **future-consumer / reuse-demand signal**.

### 6. Memory-pressure coordination
Before training/background work:
- projected workspace demand is compared to foreground reserve;
- runtime requests KV offload if headroom is insufficient;
- cache manager selects colder state for host offload.

Again, physical pressure is mediated by runtime-visible budget/state.

## Q6 — Experiment design

### Platform
- RTX 3090-class 24 GB GPU;
- CUDA 13.0;
- single model instance;
- xLAM-7b-r by default;
- 7B-class model;
- LoRA rank 4;
- FlashInfer-based runtime.

This is consumer/edge-like hardware, **not a smartphone SoC**.

### Workload
- most runs: 24 tasks;
- real tau-bench retail train split;
- up to four Agent steps/task;
- judge budget 512 output tokens.

Success/reward are used as run-completion checks, not model-quality claims.

### Scheduler policy comparison
Same mixed foreground/judge/training/stale-prefill workload:

Foreground-first:
- queue p95 1.433 s;
- p99 1.758 s;
- 34 training commits / adapter publishes.

Round-robin:
- p95 1.530 s;
- p99 3.625 s;
- 21 training commits.

FIFO:
- p95 4.403 s;
- p99 5.908 s.

Foreground-first vs FIFO:
- 3.1× lower p95;
- 3.4× lower p99.

### Training interruption ablation
Foreground-only:
- p95 queue wait ~0.0018 s.

+ judge:
- p95 queue wait 1.424 s.

+ non-preemptible training:
- p95 queue wait 4.140 s;
- p95 TTFT 4.247 s.

+ interruptible training:
- p95 queue wait 2.676 s;
- p95 TTFT 2.749 s.

Trade-off:
- training throughput 346.8 → 271.8 steps/hour;
- ~21.6% training-throughput reduction;
- accumulated training-attributed foreground blocking 108.4 s → 41.2 s.

### vLLM full-LoRA comparison
Sleep/train/wake baseline on same workload:

Foreground-first:
- vLLM 8.418 s p95 queue vs LOCAL 1.433 s.

Round-robin:
- vLLM 19.609 s vs LOCAL 1.530 s.

FIFO:
- vLLM 27.643 s vs LOCAL 4.403 s.

Reported median vLLM sleep/train/wake window:
- ~1.0 s sleep;
- ~9.7 s train;
- ~1.5 s wake;
- ~12.1 s total.

Interpretation:
this comparison strongly favors finer-grain coexistence, but it compares different adaptation/runtime granularities rather than isolating one scheduling primitive.

### Stale-coverage prefill
Baseline vs pre-publication hot-prefix warmup:
- mean first-hit prefill 1.064 → 0.789 s;
- p95 1.146 → 0.894 s;
- p99 1.210 → 0.900 s;
- p99 reduction 25.6%;
- first-hit cache-coverage p50 0 → 0.210.

This provides causal support that materialized new-version KV, rather than request-mix change, drives the first-hit benefit.

### Cross-Agent pre-prefill
Enabled condition adds:
- 43 prefill tasks;
- 5.184 s prefill GPU time.

Without:
- mean TTFT 0.711 s;
- p95 1.587 s;
- p99 2.042 s.

With:
- mean 0.441 s;
- p95 1.384 s;
- p99 1.595 s.

Reduction:
- mean 38.0%;
- p95 12.8%;
- p99 21.9%.

Queued foreground time attributed to this prefill is only 0.018 s in the reported run.

### Memory-budget sweep
xLAM configurations from 512–1280 FlashInfer KV pages complete without OOM/publish failure.

Reported:
- peak GPU memory 21.6–23.5 GB;
- 31–35 training commits;
- 146–283 stale-prefill progress events.

Example:
- 512 pages: queue p95 1.312 s;
- 1024 pages: 0.850 s;
- 1280 pages with larger graph/cache budget: 0.997 s and 23.5 GB peak.

This shows memory configuration changes latency through admission/headroom, not only OOM risk.

## Q7 — Data / artifact / reproducibility

### Strengths
- explicit mixed serving/training/cache workload;
- real tau-bench retail workload;
- absolute latency and tail numbers;
- multiple ablations;
- correctness-aware adapter/KV version contract;
- memory sweeps near the device limit;
- implementation size disclosed as 24,447 Python LOC.

### Limitations
1. **No phone hardware.** RTX 3090-class 24 GB GPU is materially different from phone GPU/NPU/shared-memory/thermal constraints.
2. **No smartphone energy/thermal/QoE.**
3. **Short workload scale.** Most runs use 24 tasks.
4. **7B single-model focus.**
5. **Learning quality not the evaluation target.** Reward/success is mainly run-completion control.
6. **Cross-Agent prefill is one runtime mechanism**, not evidence of all multi-Agent concurrency patterns.
7. **No official public code artifact was verified** during this review despite the implementation description.
8. **Preprint status**, no verified peer-reviewed venue.
9. Future work explicitly includes longer multi-Agent sessions, larger adapter populations and policy-level learning quality.

## Q8 — Evidence vs hypothesis

### [FACT]
LOCAL demonstrates material latency-tail improvements from cooperative software scheduling under mixed foreground inference, judging and adapter training on the evaluated 24 GB GPU.

### [FACT]
Adapter version must be represented in KV validity to avoid stale hidden-state reuse after updates.

### [FACT]
Staged hot-prefix refresh and cross-Agent pre-prefill improve evaluated first-consumer latency.

### [FACT]
Agent identity is not always a hard cache key in LOCAL; validity is determined by token/context/adapter/version state.

### [INFERENCE — project]
T5 is strengthened: versioned Agent state lifecycle, validity and reuse are first-class product/runtime concerns.

### [INFERENCE — project]
T7's strongest demonstrated control signal is **pending future consumption of shared context**, not Agent identity itself.

### [INFERENCE — project]
That signal is largely reducible to software-visible dependency/topology + reuse probability + state/version validity, which are already natural C/T5 control variables.

## Q9 — Real contribution to project decision

### T5 — strong strengthening
LOCAL shows a concrete state lifecycle:
`valid → stale-by-adapter-update → staged refresh → publish → reuse/offload`

This is exactly the type of product capability T5 is intended to track.

T5 remains:
- EMERGING_PRODUCT_TREND;
- ADAPT_AND_DIFFERENTIATE.

No maturity promotion because target-phone transfer is unproven.

### T7 — further narrowed
LOCAL is the strongest T7 discriminator so far because it truly shares:
- one model;
- KV budget;
- adapter versions;
- runtime memory;
- future cross-Agent context.

Yet its own architecture decomposes the problem into:
- scheduler priority/admission → C;
- state/version validity and residency → T5/B;
- pending consumer / communication dependency → C-style topology/demand signal.

Most importantly, producer Agent identity can disappear from the hard cache key.

Therefore:
**T7 remains FRONTIER_SIGNAL / WATCH and does not earn a Direction from LOCAL.**

### H-CAL — software baseline strengthened
LOCAL fills part of the old H-CAL evidence gap:
live foreground inference and local adapter publication **can** coexist in a unified software runtime.

But it still does not satisfy the reopen condition:
- not a commercial phone;
- no phone battery/thermal/foreground QoE;
- no residual beyond C/T5 shown.

So H-CAL remains closed as a standalone differentiated Bet.

### CPU/uArch
No hardware gate advance:
- STRUCTURAL_SIGNAL: plausible;
- target-phone SYSTEM_VALUE: absent;
- SOFTWARE_INSUFFICIENCY: contradicted rather than established;
- hardware-specific cause: absent.

LOCAL therefore raises the software baseline for any future state/cache/scheduling hardware claim.

## Q10 — Next action
1. Keep PAPER-104 P0 / FULL_10Q.
2. Add version-aware Agent KV lifecycle to T5 strongest product baseline.
3. Add cross-Agent prefill to T7 strongest software baseline.
4. Do not create a T7 Direction.
5. Keep H-CAL standalone Kill unchanged.
6. Require future T7 candidates to beat a baseline that already knows:
   - dependency/future-consumer state;
   - context namespace;
   - adapter identity/version;
   - KV hotness/residency;
   - memory pressure;
   - foreground/background priority.
7. Deep-read **EcoAgent** next as the remaining independent mobile multi-Agent architecture seed.
8. After EcoAgent, issue final Round 14-A T7 ownership/residual decision.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE on a single consumer GPU runtime; not target-phone SYSTEM_VALUE
- **Decision impact:** strengthen T5 and H-CAL software baseline; narrow T7; no new Direction; no uArch promotion
- **Open questions:** target-phone transfer, shared-memory SoC behavior, energy/thermal/QoE, long sessions, larger adapter populations, independent replication
- **Primary source:** https://arxiv.org/abs/2608.15241
- **Artifact:** no official public code artifact verified
