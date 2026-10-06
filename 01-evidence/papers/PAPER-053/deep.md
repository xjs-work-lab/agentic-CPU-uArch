# PAPER-053 — Agent-X: Full Pipeline Acceleration of On-device AI Agents

## Source
- Paper: https://arxiv.org/abs/2605.10380
- ACM DOI: https://doi.org/10.1145/3745756.3809195
- Authors: Jinha Chung, Byeongjun Shin, Jiin Kim, Minsoo Rhu
- Affiliation: KAIST, VIA Research Group
- Venue: ACM MobiSys 2026, pp. 144–157
- Evaluated system: TinyAgent / LLMCompiler-style plan-out Agent
- Main model: TinyAgent-7B (WizardLM-2-7B derivative)
- Platform: Apple Mac mini, M4 Pro, 64 GB memory, 512 GB SSD, 12 CPU cores, 16 GPU cores
- Software: MLX 0.25.2, modified MLX-LM 0.25.1, MLX-engine commit ecc2cf4, macOS Sequoia 15.5
- Dataset: 1,022 TinyAgent test examples, up to 16 tools
- Priority: P0
- Project relevance: Agent workload model; strongest software baseline for A/C; second-Bet search; software-vs-hardware boundary

## Q1 — Problem + target mapping

### Paper problem
On-device Agents are slow because the full Agent pipeline is not well represented by the usual cloud-LLM assumption that decode dominates.

In TinyAgent's plan-out flow:
1. Planner consumes a long prompt containing system instructions, tool descriptions/guidelines, few-shot tool-use examples and the user request.
2. Tools execute.
3. Arbiter consumes the call/observation history and decides whether the task is complete.

On the evaluated M4 Pro system:
- average task latency: **35.4 s**;
- Planner: **43.5%** of end-to-end latency;
- Arbiter: **46.9%**;
- combined LLM components: **90.4%**;
- prefill: **21.7%**;
- decode: **68.7%**.

### Mapping to this project
This is highly relevant to the smartphone Agent workload model because it shows that an Agent's execution structure changes where the latency sits.

However:
- the device is a Mac mini, not a smartphone;
- the Agent is plan-out/tool-API based, not a long-horizon GUI/multimodal Agent;
- the result is not target-phone SYSTEM_VALUE.

The correct use is:
> **strong edge-Agent workload characterization + software-baseline pressure**, not smartphone/uArch proof.

## Q2 — Novelty / new-regime relevance

### What is genuinely Agent-specific
Agent-X does not merely run a generic LLM kernel faster. It exploits structure caused by Agent workflows:

- dynamic tool selection creates prompt fragments that are individually static but dynamically composed;
- tools exhibit **co-activation locality**;
- Planner/Arbiter outputs are highly correlated with few-shot examples and user prompt;
- 96% of Planner output tokens and 87% of Arbiter output tokens overlap with corresponding input content in the reported analysis.

This is a real **Agent-native / Agent-amplified operating regime**.

### What is generic
The implementation primitives are established generic ideas:
- prefix/KV caching;
- prompt reconstruction;
- speculative decoding;
- n-gram lookup;
- autoregressive fallback.

Therefore the novelty is primarily:
> recognizing Agent-specific regularities and composing generic inference primitives around them.

It is **not** evidence for new ISA/uArch.

## Q3 — Falsifiable hypothesis

Agent-X effectively tests:

> If on-device Agent prompts and outputs contain exploitable Agent-specific structural regularity, then restructuring the prompt for cache reuse and using prompt-derived lightweight draft tokens should reduce end-to-end Agent latency without degrading task accuracy.

The hypothesis would be falsified if:
- prompt reconstruction lost task accuracy;
- storage/loading overhead erased prefill savings;
- output regularity were too weak for lightweight speculative decoding;
- full-system end-to-end speedup disappeared after integration.

Within the evaluated TinyAgent setup, the hypothesis survives.

It remains open for:
- smartphones;
- larger tool universes;
- GUI/multimodal Agents;
- long-horizon/highly dynamic Agents;
- stronger modern inference runtimes.

## Q4 — Research lineage / competing route

### Lineage
The same KAIST VIA group published **The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective** at HPCA 2026, characterizing the system/energy cost of Agentic reasoning.

Agent-X is a natural next step:
> **characterize Agent cost → identify Agent-specific latency structure → build workload-aware software acceleration.**

The underlying edge-Agent substrate comes from TinyAgent / LLMCompiler:
- TinyAgent makes local function-calling Agents practical;
- LLMCompiler / plan-out execution reduces repeated LLM calls and exposes structured planning/execution.

This is a sustained research lineage rather than an isolated "Agent" label.

### Strong competing routes
Agent-X must be compared conceptually with:
- ordinary prefix caching;
- Prompt Cache / CacheBlend-style KV reuse;
- generic prompt shortening / ToolRAG;
- conventional LLM-based speculative decoding;
- prompt-lookup decoding (PLD);
- model quantization / generic LLM inference acceleration;
- accelerator/NPU execution improvements;
- smaller/fine-tuned Agent models.

Important result:
a conventional 1B draft LLM is not automatically a strong edge baseline because draft latency + multi-token verification tax can erase the theoretical advantage.

## Q5 — Key mechanism / control point

### PromptWeaver — prefill
Control point:
**prompt layout + offline KV state placement**.

Mechanisms:
1. replace early dynamically selected tool descriptions with an all-inclusive static prefix;
2. cluster tools using observed co-activation locality;
3. precompute selected cluster-prefix KV states;
4. store KV cache states in SSD;
5. append a small number of dynamic relevant examples to preserve task accuracy.

Important trade:
the prompt becomes longer, but much more of it becomes reusable.

### ExSpec — decode
Control point:
**whether and how to speculate based on prompt-derived output regularity**.

Mechanisms:
1. build an n-gram LUT from few-shot examples + user query;
2. use LUT lookup instead of another LLM to draft;
3. use selective fallback to autoregressive decoding when a LUT hit is absent;
4. avoid paying speculative multi-token verification cost when speculation is unlikely to help.

### Project interpretation
The strategic lesson is:
> Agent semantics/structure can be converted into low-level execution value entirely in software.

That strengthens the software-first gate for A/C/R3.

## Q6 — Experiment design

### Workload
- 1,022 TinyAgent test examples;
- tasks use up to 16 tools;
- plan-out Planner + Execution + Arbiter flow.

### Model
- primary: TinyAgent-7B;
- additional smaller-model check: TinyAgent-1.1B.

### Hardware/software
- Apple M4 Pro Mac mini;
- 64 GB memory;
- 512 GB SSD;
- MLX-based inference stack.

### Baselines / ablations
PromptWeaver:
- baseline prompt;
- static-only caching;
- varying number of dynamic examples;
- varying KV cache cluster budget.

ExSpec:
- normal autoregressive decoding;
- draft-LLM speculative decoding;
- non-selective n-gram speculation;
- selective ExSpec;
- different n-gram orders;
- different extraction regions.

System:
- PromptWeaver only;
- ExSpec only;
- PromptWeaver + ExSpec.

### Reported anchors
- baseline average Agent task: **35.4 s**;
- Planner + Arbiter: **90.4%** of total latency;
- PromptWeaver: **1.97x** aggregate prefill acceleration reported by the paper;
- ExSpec: **1.73x** decode acceleration;
- PromptWeaver only: **1.16x** end-to-end;
- ExSpec only: **1.43x** end-to-end;
- full Agent-X: **1.61x** end-to-end.

Accuracy:
- baseline Planner DAG accuracy: **0.836**;
- selected PromptWeaver K=1: **0.841**.

## Q7 — Data / artifact / reproducibility

### Strengths
The paper provides unusually useful reproducibility detail:
- exact test-set size;
- model identity;
- platform;
- memory/storage;
- software versions;
- MLX-engine commit;
- ablation structure;
- explicit accuracy metric;
- TinyAgent dataset/model are publicly available from the upstream project.

### Artifact status
TinyAgent, MLX and MLX-engine are public ecosystem components.

**Agent-X's own complete research artifact/code has not been independently verified in the current source set.**

Therefore reproducibility is:
- stronger than paper-only black-box evidence;
- weaker than an independently reproduced artifact.

### Important resource costs
PromptWeaver is not "free":
- KV budget 15 clusters gives **74.4%** coverage;
- total SSD cache footprint reported: **6.26 GB**;
- Planner average input grows from **1,739 → 3,790 tokens**;
- this adds about **256 MB** KV-cache memory in the reported setup;
- decode time/token increases **2.2%** from the longer prompt;
- LUT construction for ExSpec costs about **83 ms/query**.

These costs matter for smartphone transfer.

## Q8 — Evidence vs hypothesis

### [FACT — evaluated system]
For TinyAgent-7B on the evaluated M4 Pro platform:
- both prefill and decode materially contribute to end-to-end Agent latency;
- Planner/Arbiter dominate overall latency;
- Agent prompt/output structure is highly regular;
- Agent-X reports 1.61x end-to-end acceleration without task-accuracy degradation under the paper's metric.

### [FACT — mechanism-specific]
- PromptWeaver substantially reduces uncached prompt work;
- ExSpec beats conventional draft-LLM speculation in the evaluated edge setting;
- large SSD-resident KV state is part of the cost.

### [OBSERVATION]
Agent execution creates exploitable regularity beyond generic conversation-style LLM serving.

### [INFERENCE — project]
A strong Agent-aware software stack can capture substantial value **before** OS/uArch intervention.

### Not established
- smartphone energy/thermal gain;
- foreground QoE gain;
- Huawei-phone transfer;
- DemandState / RequiredProgress value;
- Agent-specific CPU scheduling value;
- NPU-vs-CPU placement;
- hardware insufficiency;
- new ISA/uArch need.

## Q9 — Real contribution to the project decision

### A — Agent Semantic Progress Control
**No promotion.**

Agent-X does not test DemandState or RequiredProgress.

But it raises A's baseline:
> A must beat not only generic predictors/runtime legality, but also Agent-aware software mechanisms that exploit semantic/workflow structure for concrete execution savings.

So PAPER-053 is a **baseline-strengthening / falsification-pressure** source for A, not positive proof for A.

### C — Efficient System-Control Substrate
**No promotion.**

Agent-X demonstrates material Agent-specific execution optimization, but it does so above the OS/system-control layer using prompt/cache/decode mechanisms.

Implication:
> some apparently "Agent-system" latency is still highly software-capturable before C gets credit.

This raises C's strongest baseline rather than proving C's residual.

### CG-06
Only weak indirect relevance:
Agent-X confirms the end-to-end Agent workload contains different compute/memory phases, but it does not compare CPU/NPU placement.

No CG-06 state change.

### R3 / uArch
The paper argues **against premature hardware promotion**:
1. meaningful Agent-specific information exists;
2. substantial value is obtained using software and existing hardware;
3. therefore semantic information value alone does not justify a hardware hint.

R3 remains BLOCKED.

### Second-Bet search
Agent-X does **not** create a second Bet.

It does reveal a broader candidate research question:
> Which Agent-specific structural information survives strong application/runtime exploitation and still yields a reusable lower-layer residual?

That question should pressure-test A/C rather than become a new Direction by default.

## Q10 — Next action

1. **KEEP as P0**.
2. Treat Agent-X as a mandatory strong software baseline for future Agent latency/system-control claims.
3. Do not change Direction lane/score from this paper alone.
4. Snowball the KAIST VIA lineage:
   - HPCA 2026 dynamic-reasoning characterization;
   - related phase-aware LLM serving work;
   - subsequent Agent/on-device execution work.
5. In future phone experiments, measure whether Agent-X-like capture removes the apparent Agent-specific residual before crediting A/C.
6. Explicitly test smartphone feasibility of:
   - multi-GB SSD KV cache;
   - memory footprint;
   - flash read energy/latency;
   - larger tool catalogs;
   - distribution drift;
   - GUI/multimodal/long-horizon Agents.

## Decision footer
- **New-regime relevance:** Agent-native workload structure; generic implementation primitives
- **Evidence maturity:** **SYSTEM_VALUE** for software acceleration on the evaluated M4 Pro TinyAgent system; **STRUCTURAL_SIGNAL** for smartphone transfer
- **Decision impact:** strengthen Agent-aware software baseline; no Direction promotion/demotion
- **A impact:** CHALLENGE / stronger baseline, not support for CLM-A-001
- **C impact:** CHALLENGE / stronger upper-layer capture, no SYSTEM_VALUE residual for C
- **CG-06 impact:** no material state change
- **R3 impact:** remain BLOCKED; reinforces software-first gate
- **Open questions:** smartphone transfer, flash/KV economics, broader Agent forms, stronger inference baseline, energy/thermal/QoE
- **Primary source:** https://arxiv.org/abs/2605.10380
- **ACM source:** https://doi.org/10.1145/3745756.3809195
