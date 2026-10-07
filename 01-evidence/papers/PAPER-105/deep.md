# PAPER-105 — EcoAgent: An Efficient Device-Cloud Collaborative Multi-Agent Framework for Mobile Automation

## Source
- Peer-reviewed: AAAI 2026
- Official article: https://ojs.aaai.org/index.php/AAAI/article/view/40230
- arXiv: https://arxiv.org/abs/2505.05440
- Code: https://github.com/Yi-Biao/EcoAgent
- Authors: Biao Yi, Xueyu Hu, Yurun Chen, Shengyu Zhang, Hongxia Yang, Fan Wu
- Institutions: Zhejiang University; Hong Kong Polytechnic University; Shanghai Jiao Tong University
- Review: FULL_10Q / EDP v1
- Priority: P0

## Q1 — Problem + target mapping
EcoAgent asks how a mobile automation system can split work across cloud and device-side specialized Agents without paying the latency, token, uplink and privacy costs of cloud-only verification.

Architecture:
- cloud Planning Agent;
- device-side Execution Agent;
- device-side Observation Agent.

Project mapping:
1. **T3/PT-A:** does action-effect verification + feedback/replanning belong in the product execution contract?
2. **T7:** does multi-Agent decomposition itself create a new local CPU/system control state beyond C/T5/PT-A?
3. **CPU/uArch:** does any measured residual survive strong software decomposition and placement?

## Q2 — Novelty / new-regime relevance
EcoAgent's important contribution is a **closed-loop device-cloud Agent architecture**:
- cloud performs long-horizon planning/reflection;
- device-side executor performs grounding/actions;
- device-side observer verifies expected effects;
- compact semantic summaries are sent upstream instead of repeated raw screenshots.

This is **AMPLIFIED / product-architecture relevant**, not evidence for a new CPU primitive.

The paper's gains derive from:
- role specialization;
- explicit expected effects;
- local verification;
- failure-triggered replanning;
- communication compression.

These are software/system architecture variables.

## Q3 — Falsifiable hypothesis
Paper hypothesis:
> moving execution verification and semantic screen summarization to a lightweight device-side Agent can preserve useful task success while reducing cloud calls, tokens, uplink data and latency versus cloud-centric/open-loop designs.

T7-specific hypothesis:
> if local multi-Agent concurrency is a distinct CPU/system regime, EcoAgent should expose repeated local contention/shared-state behavior that cannot be expressed as role placement, verification state, communication frequency or ordinary resource demand.

The first hypothesis receives support.
The T7-specific hypothesis does not.

## Q4 — Research lineage / strongest competing routes

### Cloud/mobile Agent baselines
- AppAgent;
- MobileAgent;
- M3A;
- Agent S2.

### Device-side specialized Agents
- ShowUI;
- OS-Atlas;
- V-Droid.

### Device-cloud/open-loop
- UGround;
- CogAgent;
- AutoDroid-family approaches.

EcoAgent is best interpreted as a placement/feedback architecture competing with these routes, not as a new local scheduling/cache architecture.

Important comparison boundary:
EcoAgent does **not** lead success rate:
- EcoAgent ShowUI: 25.6%;
- EcoAgent OS-Atlas: 27.6%;
- M3A: 28.4%;
- Agent S2: 54.3%;
- V-Droid: 59.5%.

Thus its value proposition is efficiency/closed-loop balance, not best absolute task success.

## Q5 — Key mechanism / control point

### 1. Dual-ReACT Planning Agent
Cloud GPT-4o:
- global task decomposition;
- local step generation;
- explicit expected effect `EX_t` per step.

Expected effects turn action progress into a verifiable contract.

### 2. Execution Agent
ShowUI-2B or OS-Atlas-Pro-4B generates concrete GUI actions.

### 3. Observation Agent
Qwen2-VL-2B compares post-action screen with the expected effect:
`R_t = OA(S_{t+1}, EX_t)`

This is a direct software realization of action-effect verification.

### 4. Pre-Understanding
Raw screen images consuming >1400 tokens are compressed to ~50–150 token textual summaries.

This reduces cloud token/uplink cost and exposes a semantic handoff representation.

### 5. Memory + Reflection
If verification fails:
- compact screen/action history is retained;
- cloud Planner reflects;
- a new remaining-step plan is generated.

The execution loop is therefore:
`plan → act → verify → compact state → continue/replan`

### T7 implication
The three “Agents” mainly correspond to:
- distinct functions;
- different model specializations;
- different placement.

The paper does not expose:
- concurrent local Agent queues on a phone;
- shared local KV/adapters between Agents;
- local cross-Agent cache coherence;
- phone CPU/NPU scheduling conflicts caused by Agent identity.

## Q6 — Experiment design

### Benchmark
AndroidWorld:
- 116 programmatic tasks;
- 20 Android apps;
- live Android emulator;
- Pixel 6 device model;
- Android 13 / API 33.

### Critical deployment boundary
The paper explicitly states:
> all device-side models are deployed on a local server with an NVIDIA RTX 3090 GPU (24G) to simulate mobile inference.

Therefore:
- Android interaction environment is mobile/emulated;
- model execution is **not measured on a smartphone SoC**.

The official code similarly serves device observer/executor models through vLLM/CUDA endpoints and controls Android via ADB.

### Success rates
- ShowUI single: 7.0%;
- OS-Atlas single: 4.3%;
- V-Droid: 59.5%;
- AppAgent: 11.2%;
- M3A: 28.4%;
- Agent S2: 54.3%;
- UGround-2B: 32.8%;
- UGround-7B: 44.0%;
- EcoAgent ShowUI: 25.6%;
- EcoAgent OS-Atlas: 27.6%.

### Ablation — role decomposition
ShowUI:
- Executor only: 7.0%, MC 0, MT 0;
- + Planner: 15.5%, MC 1, MT 2149;
- + Observer: 25.6%, MC 1.87, MT 3545.

OS-Atlas:
- Executor only: 4.3%;
- + Planner: 19.0%, MC 1, MT 2181;
- + Observer: 27.6%, MC 1.53, MT 3240.

This gives causal support that planning and closed-loop observation/verification each add task-level value in the evaluated stack.

### Operational cost
Reported average cloud MLLM calls / tokens:
- AppAgent: 6.46 / 15309;
- M3A: 13.39 / 87469;
- UGround-2B: 12.21 / 45192;
- EcoAgent ShowUI: 1.87 / 3545;
- EcoAgent OS-Atlas: 1.53 / 3240.

### Latency
Average execution-step latency:
- ShowUI: 1.2 s;
- V-Droid: 3.0 s;
- AppAgent: 7.1 s;
- MobileAgent: 15.9 s;
- M3A: 15.3 s;
- UGround-2B: 18.2 s;
- CogAgent: 6.8 s;
- AutoDroid: 4.9 s;
- EcoAgent ShowUI: 3.9 s.

These cross-system latency comparisons involve different models/architectures and should not be treated as isolated causal attribution.

### Uplink
Per task:
- AppAgent: 2098 kB;
- M3A: 5831 kB;
- EcoAgent ShowUI: 120 kB.

### Device-side compute estimate
Authors report roughly:
- Qwen2-VL-2B: 10.89 TFLOPs / forward;
- ShowUI-2B: 11.46 TFLOPs / forward.

They argue this aligns with modern mobile NPU capability, but this is a compute estimate, **not a measured mobile-NPU run**.

## Q7 — Data / artifact / reproducibility

### Strengths
- peer-reviewed AAAI 2026 paper;
- public official MIT-licensed code;
- programmatic AndroidWorld evaluation;
- architecture ablation;
- cloud calls/tokens, latency, uplink metrics;
- explicit experimental disclosure that device models are simulated on RTX 3090.

### Limitations
1. **No real on-phone model inference.**
2. No phone battery/thermal/foreground-QoE measurement.
3. AndroidWorld is emulator-based.
4. Latency comparison spans heterogeneous systems/models.
5. Privacy benefit is inferred from reducing raw-image upload; no formal privacy/security analysis.
6. EcoAgent is not state-of-the-art in task success.
7. The architecture is device-cloud, not a fully local multi-Agent runtime.
8. No local shared-model/KV/adapter contention experiment.

## Q8 — Evidence vs hypothesis

### [FACT]
Planning + device-side verification improves EcoAgent success over executor-only and planner+executor ablations in AndroidWorld.

### [FACT]
EcoAgent uses far fewer cloud calls/tokens and much lower uplink volume than M3A in the reported evaluation.

### [FACT]
The device-side models were executed on an RTX 3090 local server, not on smartphone silicon.

### [FACT]
EcoAgent's absolute SR trails V-Droid and Agent S2.

### [INFERENCE — project]
EcoAgent strengthens **T3 / PT-A**: explicit expected effects, post-action verification and bounded feedback/replanning are practical product-architecture mechanisms.

### [INFERENCE — project]
EcoAgent does not strengthen a standalone T7 hardware/system residual because its multi-Agent value is role decomposition and placement rather than local shared-resource concurrency.

## Q9 — Real contribution to project decision

### T3 / PT-A — strengthened
EcoAgent independently reinforces:
`plan with expected effect → execute → observe/verify → compact outcome → replan on failure`

This is highly aligned with T3's product contract.

No posture/maturity change:
- T3 remains EMERGING_PRODUCT_TREND / PRODUCTIZE;
- PT-A remains PLATFORM_TRACK / 80.0 / SYSTEM_VALUE.

Why no change:
the verification/product pattern is further corroborated, but device-side inference is simulated rather than on-phone.

### T7 — final negative discriminator
Across the three Round 14-A seeds:
- MobiMem: multi-role workflow value maps to DAG/replay/state;
- LOCAL: even shared-model multi-Agent state maps to context/adapter/version/future-consumer metadata;
- EcoAgent: mobile multi-Agent value maps to role specialization, verification and device-cloud communication placement.

No seed establishes a new local smartphone CPU/NPU control variable tied specifically to multi-Agent identity/concurrency.

### Final T7 outcome
- Product Trend: **KEEP WATCH**;
- Trend maturity: FRONTIER_SIGNAL;
- Product posture: WATCH;
- standalone differentiated Bet/Direction candidate: **KILL_DIFFERENTIATED_BET**;
- ownership: **MERGE INTO C + T5/B-residual + PT-A**;
- no new Direction;
- no second Primary Bet;
- no uArch candidate.

### Reopen condition
Reopen T7 differentiation only if a target-phone experiment shows material residual value after a baseline that already includes:
- Agent-flow/DAG priority and future-consumer state;
- shared-model/KV hotness/residency;
- context namespace and adapter/version validity;
- foreground/background scheduling;
- verified actuation/recovery;
- memory-pressure-aware control.

## Q10 — Next action
1. Keep PAPER-105 as P0 / FULL_10Q.
2. Add EcoAgent closed-loop verification to T3/PT-A strongest baseline.
3. Close Round 14-A T7 standalone differentiation.
4. Preserve T7 as WATCH rather than DROP_PRODUCT_ROUTE.
5. Route future evidence to existing owners unless the reopen condition is met.
6. Move frontier search to **T6 Local programmable Agent execution & sandboxed skills**.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE for evaluated mobile-automation architecture; not target-phone local-model SYSTEM_VALUE
- **Decision impact:** strengthen T3/PT-A; close standalone T7 differentiated candidate; merge ownership into existing lanes
- **Open questions:** true on-phone 2B–4B model execution cost, battery/thermal/QoE, fully local multi-Agent concurrency, shared NPU/CPU state
- **Primary source:** https://ojs.aaai.org/index.php/AAAI/article/view/40230
- **Artifact:** https://github.com/Yi-Biao/EcoAgent
