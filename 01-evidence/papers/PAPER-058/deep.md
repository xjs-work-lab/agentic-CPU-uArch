# PAPER-058 — AutoDroid-V2: Boosting SLM-based GUI Agents via Code Generation

## Source
- MobiSys 2025, Best Artifact Award
- DOI: https://doi.org/10.1145/3711875.3729134
- arXiv: https://arxiv.org/abs/2412.18116
- Artifact: https://github.com/MobileLLM/AutoDroid-V2
- Main evaluation: DroidTask (158 tasks / 13 apps) + executable AitW subset (68 tasks), total 226 tasks across 23 apps
- Phone: OnePlus ACE 2 Pro / Snapdragon 8 Gen2
- Higher-capacity reference: Apple M2 Pro
- Local model family: fine-tuned Llama-3.1-8B, Q8 deployment via llama.cpp for phone latency
- Priority: P0

## Q1 — Problem + target mapping
Step-wise GUI Agents repeatedly query an LLM after every UI state. This creates:
- high reasoning/query frequency;
- repeated dynamic GUI prompt processing;
- long on-device latency;
- high token/compute cost.

AutoDroid-V2 asks whether a mobile Agent can instead:
> compile the whole task into a multi-step program once, then execute it locally with a deterministic interpreter.

This is directly relevant to smartphone persistent Agents because it is a real Android task-automation workload and includes real phone inference.

## Q2 — Novelty / new-regime relevance
The Agent-native element is not code generation itself. It is exploiting the fact that many app tasks have enough stable structure to move repeated online reasoning into:
- offline app-document construction;
- task-level code generation;
- explicit script/program state;
- deterministic status/error handling;
- reusable static prompt/KV state.

Classification: **Agent-native/amplified workload restructuring using generic software primitives.**

## Q3 — Falsifiable hypothesis
If app/task structure is sufficiently predictable and can be summarized into a compact executable interface, then replacing repeated step-wise reasoning with task-level script generation should improve success/efficiency on device.

Falsifiers:
- dynamic UI invalidates preplanned scripts too often;
- app-document generation is too expensive/stale;
- small models cannot generate reliable scripts;
- error recovery forces per-step LLM calls again;
- one-time offline cost overwhelms deployment economics.

The evaluated benchmarks support the hypothesis for the tested apps, while the paper explicitly identifies highly dynamic UIs as a weakness.

## Q4 — Research lineage / competing route
This belongs to the sustained Tsinghua AIR / MobileLLM line:
- AutoDroid — step-wise mobile Agent + app memory;
- AutoDroid-V2 — task-level script/code lowering;
- AgentProg (PAPER-056) — long-horizon program-guided context and belief state.

Strong competing routes:
- step-wise AutoDroid;
- SeeClick/CogAgent visual agents;
- Mind2Web-style agents;
- MobileGPT/app-memory approaches;
- long-context reasoning;
- AgentProg-style program-guided iterative reasoning.

Important lineage observation:
PAPER-058 and PAPER-056 are group-overlapping evidence and must not be counted as independent corroboration.

## Q5 — Key mechanism / control point
AutoDroid-V2 moves semantic work into four software objects:

1. **App document**
   - compresses GUI states/elements;
   - records abstract elements, identifiers, effects and dependencies.

2. **Element Transition Graph**
   - represents forward/backward dependencies between GUI elements.

3. **Task-level script**
   - one generated Python-like DSL program replaces repeated per-step model decisions.

4. **Runtime interpreter / code status tracker**
   - grounds elements, follows dependencies, catches errors and triggers regeneration only when needed.

Efficiency mechanisms:
- runtime prompt shortened from ~15.4k to ~2.8k tokens on average;
- static document prefix is cacheable/reusable;
- 97.6% of the prompt is reported as document/static prefix in the relevant configuration.

Project interpretation:
> rich Agent semantics can already be **lowered into executable software control state** before the OS/CPU sees them.

## Q6 — Experiment design
Datasets:
- DroidTask: 158 tasks, 13 apps;
- AitW executable subset: 68 tasks.

Baselines:
- AutoDroid;
- SeeClick;
- CogAgent;
- Mind2Web;
- GPT-4o and fine-tuned Llama-3.1 variants.

Phone:
- OnePlus ACE 2 Pro, Snapdragon 8 Gen2;
- fine-tuned Llama-3.1-8B quantized to 8-bit via llama.cpp.

Metrics:
- task success;
- reversed redundancy ratio;
- LLM inference latency;
- input/output token consumption.

Headline phone results:
- AutoDroid-V2: **46.3 s/task**;
- step-wise AutoDroid: **669.2 s/task**;
- **93.1% inference-latency reduction**.

Token results per task:
- AutoDroid uncached/remaining input: 3021.2;
- AutoDroid-V2 remaining input: 67.9;
- AutoDroid output: 832.4;
- AutoDroid-V2 output: 122.9.

AitW subset:
- AutoDroid-V2 Llama-3.1-8B-ft: **47.1%**;
- AutoDroid Llama-3.1-8B-ft: **36.7%**.

Model-size sweep on DroidTask:
- Llama3.2-3B: 44.6%;
- Qwen2.5-7B: 50.0%;
- Llama3.1-8B: 54.4%.

## Q7 — Data / artifact / reproducibility
Strengths:
- MobiSys 2025;
- Best Artifact Award;
- public code;
- public fine-tuned model and dataset links;
- evaluation scripts for DroidTask and LlamaTouch;
- phone latency reproduction path via llama.cpp;
- Android emulator/device setup documented.

Important artifact boundary:
- accuracy/evaluation workflow can require external GPT/OpenAI access for some pipeline stages;
- authors' offline data generation/validation is expensive.

Offline GPT-4o cost reported per app:
- document generation: ~$4.11;
- data synthesis: ~$7.83;
- solution validation: ~$70.48.

This cost is amortized/offline, but it is part of productization economics.

## Q8 — Evidence vs hypothesis
### [FACT]
On the evaluated Snapdragon 8 Gen2 system, task-level script execution substantially reduces local LLM inference latency and runtime uncached/output tokens compared with the step-wise AutoDroid baseline.

### [FACT]
The public artifact exposes app-document generation, training, accuracy validation and phone latency-validation workflows.

### [OBSERVATION]
A large portion of repeated Agent reasoning can be converted into static/reusable knowledge plus executable control flow when the UI/task structure is predictable.

### [INFERENCE — project]
The semantic gap between Agent intent and low-level execution can be compressed significantly **inside the Agent/application runtime itself**.

### Not established
- persistent multi-Agent resource arbitration;
- foreground/background QoE;
- cross-engine CPU/NPU placement;
- lower-layer semantic-control residual;
- CPU/uArch necessity.

## Q9 — Real contribution to project decision
### A
**Baseline strengthening / no score change.**

A's B4-TX must assume that stable task semantics may already be compiled into:
- task-level script/control flow;
- app dependency graph;
- status/error state;
- cached static knowledge.

DemandState only earns differentiated value if it adds information beyond these software representations.

### H-SCL — Semantic Control Lowering
**NARROW substantially.**

The broad proposition:
> "lower Agent semantics into executable control facts"

is already materially demonstrated at application level by AutoDroid-V2.

A surviving H-SCL hypothesis must therefore be:
> a **portable cross-framework lowering layer** that derives a small set of reusable resource-control facts not already captured by task scripts/app-specific runtimes, and maps them to OS/runtime/CPU/NPU controls.

### C
No direct promotion. AutoDroid-V2 reduces upper-layer Agent overhead; it does not establish reusable OS-level Agent-specific residual.

### R3 / uArch
Remain BLOCKED. The paper is strong evidence for software-first semantic handling.

## Q10 — Next action
1. KEEP as P0.
2. Add a canonical software-baseline Claim.
3. Strengthen A/B4-TX with task-level script/code lowering where structure permits.
4. Narrow H-SCL to **portable cross-framework resource-control lowering**, not generic semantic-to-code lowering.
5. Preserve dynamic-UI failure mode as negative evidence.
6. Do not create a new Direction from this paper.
7. Compare future H-SCL proposals against AutoDroid-V2/AgentProg as upper-layer semantic-capture baselines.

## Decision footer
- **New-regime relevance:** Agent-native/amplified
- **Evidence maturity:** SYSTEM_VALUE for evaluated on-device mobile GUI Agent efficiency/task success
- **Decision impact:** strong software-baseline strengthening; H-SCL narrowing; no Bet promotion
- **A impact:** stronger B4-TX
- **C impact:** no promotion
- **R3 impact:** remain BLOCKED
- **Open questions:** dynamic-UI regime, per-app offline economics, generalization across app versions/frameworks, residual reusable system control
- **Primary source:** https://doi.org/10.1145/3711875.3729134
- **Artifact:** https://github.com/MobileLLM/AutoDroid-V2
