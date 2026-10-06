# PAPER-056 — AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management

## Source
- Paper: https://arxiv.org/abs/2512.10371
- ACM DOI: https://doi.org/10.1145/3745756.3809245
- Artifact: https://github.com/MobileLLM/AgentProg
- Authors: Shizuo Tian, Hao Wen, Yuxuan Chen, Jiacheng Liu, Shanhui Zhao, Guohong Liu, Ju Ren, Yunxin Liu, Yuanchun Li
- Venue: ACM MobiSys 2026
- Research lineage: THU-AIR / MobileLLM + collaborators; related mobile-Agent line includes AutoDroid / AutoDroid-V2 and subsequent mobile-GUI-agent work
- Benchmarks: AndroidWorld (116 tasks) + AW-Extend (19 long-horizon tasks)
- Main planning model: Gemini-2.5-Pro
- GUI grounding component: UI-TARS-1.5-API
- Deployment in paper: cloud/API-backed model execution controlling Android environment; not an on-device SLM result
- Priority: P0

## Q1 — Problem + target mapping

### Paper problem
Long-horizon mobile GUI Agents can require dozens or hundreds of steps. Their interaction history grows continuously, creating three coupled failure modes:
1. loss of overall task/progress structure;
2. loss of task-critical information from earlier subtasks;
3. partial observability / hidden mobile-UI state causing plan-reality mismatch.

Existing context methods force a poor trade-off:
- sliding windows discard old but potentially critical state;
- summarization can erase details and lacks explicit future-use structure;
- hierarchical planning can still forget important information and adds replanning overhead.

### Mobile target
The paper constructs **AW-Extend**, 19 AndroidWorld-derived long-horizon tasks:
- compositional tasks preserve information across dependent subtasks/apps;
- iterative tasks scale repeated operations to n=10 / n=20 and stress irrelevant-history filtering.

### Project mapping
This is direct evidence that future mobile Agents carry **semantic execution state** beyond ordinary request/token state:
- current program position;
- active control-flow path;
- persistent task variables;
- hidden-state beliefs;
- execution history tied to specific semantic steps.

However, the paper optimizes Agent correctness/context management at the application/runtime level. It does not test CPU scheduling, NPU placement, energy, thermal, foreground QoE or uArch.

## Q2 — Novelty / new-regime relevance

### Agent-native / amplified
The long-horizon regime genuinely changes the information-management problem:
- not all history is equally relevant;
- some information must survive for tens of steps;
- repeated loop iterations create harmful history interference;
- partially observed app state requires a persistent belief representation.

AgentProg reframes context management around a **Semantic Task Program (STP)** rather than chronological history.

### Generic foundations
The ingredients have strong prior lineage:
- programs/control flow;
- variables/data flow;
- POMDP/belief-state ideas;
- code-as-action/program-synthesis Agents;
- summarization, sliding window and hierarchical planning.

Therefore the new-regime value is not 'programs are novel'. The contribution is applying explicit program semantics as the retention/pruning contract for long-horizon GUI Agent context.

Classification: **Agent-native/amplified semantic-state management; generic software primitives.**

## Q3 — Falsifiable hypothesis

Core hypothesis:
> If Agent history is organized by explicit task control/data-flow and hidden-state belief rather than raw chronology, the system can retain future-relevant information while discarding irrelevant history, improving long-horizon task completion.

Falsifiers include:
- control/data-flow structure does not improve success over strong context baselines;
- execution-tree pruning discards needed information;
- explicit variables provide little value;
- belief state does not improve partial-observability recovery;
- program generation errors dominate;
- extra LLM calls/tokens make the approach operationally impractical.

Within AndroidWorld/AW-Extend, the functional-success part of the hypothesis survives; the efficiency/productability part remains weak.

## Q4 — Research lineage / competing route

### Group lineage
The MobileLLM/THU-AIR line is sustained rather than one-off:
- AutoDroid / AutoDroid-V2: smartphone GUI automation and code-generation routes;
- AgentProg: long-horizon context management through program semantics;
- adjacent 2026 work from the group studies mobile GUI verification, benchmarks and threats.

### Strong competing routes
- M3A summarization;
- UI-TARS sliding-window / native GUI-agent approach;
- Mobile-Agent-v3 hierarchical planning with GUI-Owl;
- MobileGPT-like app memory;
- code-as-action / persistent scripting;
- long-context models;
- generic retrieval / memory compression;
- replanning/reflection.

AgentProg does not eliminate these routes. It demonstrates a strong explicit-structure baseline that future lower-layer proposals must beat.

## Q5 — Key mechanism / control point

### 1. Semantic Task Program
High-level task logic is represented with:
- sequences;
- branches;
- loops/functions;
- explicit variables;
- natural-language semantic steps rather than brittle fully specified UI APIs.

### 2. Execution Tree-guided pruning
Execution history is organized as a dynamic tree tied to program structure.
Only the active root→current path is retained; completed loop iterations and non-taken branches can be pruned.

### 3. Step-aware retrieval
When a semantic program step repeats, history from prior executions of **the same step ID** can be selectively retrieved rather than using generic similarity search.

### 4. Explicit variable persistence
Task-critical values are declared and retained as semantic anchors across long execution horizons.

### 5. Global Belief State
The runtime maintains beliefs about hidden/dynamic environment state and updates them when observed execution contradicts the current assumption.

### 6. Dual-mode execution
Each semantic step alternates between:
- Action Generation: generate Python UI actions for the current environment;
- Program Counter Update: decide hold/continue/branch/repeat based on result.

### Artifact confirmation
The public code exposes:
- `BeliefState` as explicit runtime state;
- program/workflow context, variables and current-line state;
- code-generation and Program Counter Update modes;
- belief updates after model responses;
- reuse of prior same-step code where safe.

### Project interpretation
The control point is currently **application/runtime-owned semantic execution state**.
It is not evidence that raw Agent semantics should cross into OS/CPU/uArch.

## Q6 — Experiment design

### Benchmarks
- AndroidWorld: 116 tasks;
- AW-Extend: 19 long-horizon tasks.

### Baselines
On AW-Extend, representative context-management baselines are deliberately different:
- M3A: summarization;
- UI-TARS: sliding window (max five screenshots);
- Mobile-Agent-v3: hierarchical planning, evaluated with GUI-Owl 7B/32B.

### AgentProg implementation
- Gemini-2.5-Pro planning/reasoning model;
- UI-TARS-1.5-API for UI element localization;
- Android environment/emulator integration;
- standard AndroidWorld success metric.

### Main results
- AndroidWorld success: **78.0%**;
- previous Mobile-Agent-v3 32B result shown: **73.3%**;
- AW-Extend success: **68.4%**;
- best listed AW-Extend baseline UI-TARS: **36.8%**.

### Component ablations
Global Belief State removed:
- AndroidWorld: 78.0 → **53.9%**;
- AW-Extend: 68.4 → **35.1%**.

Execution Tree removed:
- AndroidWorld: 78.0 → **61.6%**;
- AW-Extend: 68.4 → **39.5%**.

Explicit Variables removed:
- AndroidWorld: 78.0 → **64.2%**;
- AW-Extend: 68.4 → **50.0%**.

STP generation error rate reported on AndroidWorld: **2.5%**.

These ablations make the mechanism evidence substantially stronger than a top-line benchmark result alone.

## Q7 — Data / artifact / reproducibility

### Artifact strengths
Public repository `MobileLLM/AgentProg` includes:
- installable AgentProg package;
- Android/ADB execution path;
- Docker setup with emulator;
- AndroidWorld evaluation code;
- AW-Extend release;
- workflow/program execution implementation;
- belief-state and program-counter logic.

Artifact presence and key implementation paths were inspected in this research round.

### Reproducibility boundary
The project did **not** independently rerun AgentProg.
The implementation also depends on external model/API access (Gemini-2.5-Pro and UI-TARS service credentials in the released setup).

Therefore:
- mechanism/artifact visibility: strong;
- exact numerical independent reproduction: not established.

### Critical efficiency cost
For AW-Extend tasks where AgentProg, UI-TARS and Mobile-Agent-v3 all succeed, the paper reports:

| Method | Static Prefix (k tokens) | Dynamic (k) | Output (k) | Latency (s) |
|---|---:|---:|---:|---:|
| UI-TARS | 8.1 | 315.5 | 3.2 | 312 |
| Mobile-Agent-v3 | 7.9 | 809.4 | 22.1 | 1604 |
| AgentProg | **1026.4** | **301.3** | **179.7** | **2662** |

The AgentProg static prefix is about **12.5k tokens per call**; the paper notes much of it is cacheable.
AgentProg uses **two model queries per step** and emits substantial intermediate belief/program-counter content.

Dynamic context itself is compact and stable (~9k tokens after long execution in the paper's 50-step analysis), which validates the pruning objective, but total execution cost remains high.

## Q8 — Evidence vs hypothesis

### [FACT — evaluated benchmarks]
Explicit execution-tree context management, variables and global belief state materially affect long-horizon mobile GUI task success in the reported ablations.

### [FACT — artifact]
The released implementation explicitly carries semantic workflow state, variables, belief state and program-counter transitions in software.

### [FACT — cost]
The evaluated AgentProg configuration has substantially greater token/output/latency cost than the strongest fast baseline in the successful-task comparison.

### [OBSERVATION]
Long-horizon Agent correctness depends not merely on 'more context' but on distinguishing:
- active vs irrelevant control-flow history;
- persistent vs disposable data;
- expected vs observed hidden environment state.

### [INFERENCE — project]
Agent semantic execution state has real information value, but much of that information is already representable and consumable in application/runtime software.

### Not established
- on-device SLM feasibility/performance;
- phone energy/thermal impact;
- foreground QoE;
- DemandState / RequiredProgress residual;
- CPU/NPU/uArch value;
- software insufficiency.

## Q9 — Real contribution to the project decision

### A — Agent Semantic Progress Control
**Support broad semantic-information premise + strengthen B4-TX baseline; no promotion.**

AgentProg supports the broad idea that explicit Agent execution semantics can matter.
But it does **not** test A's discriminating claim:
> explicit DemandState retains >=~5% RequiredProgress/end-outcome value beyond B4-TX.

Instead it raises the baseline A must beat:
- program/control-flow state;
- explicit data-flow variables;
- belief/environment state;
- current semantic step;
- step-specific prior history
should be treated as reconstructible runtime information where available.

Therefore PAPER-056 is not positive evidence for CLM-A-001; it is both premise support and falsification pressure.

### PT-A — Heterogeneous Verified Agent Actuation Runtime
**Contextual support only; no lane change.**
AgentProg demonstrates structured action generation plus runtime state checking/recovery, but does not compare the PT-A common backend/OutcomeReceipt contract.

### B-residual
**No direct support.**
Persistent semantic variables are not the same as S0/S1→S2/S3 physical-artifact lineage.

### C
**No direct promotion.**
The demonstrated control loop is still primarily application/runtime-level context management, not target-phone OS/resource-control residual.

### R3 / uArch
**Remain BLOCKED.**
AgentProg is a strong counterexample to the inference:
> semantic state is valuable → hardware should see semantic state.

It shows large functional value can be captured through software representations. Hardware only becomes relevant if later measurements show a lower-layer consumer with SYSTEM_VALUE and causal software insufficiency.

### Second-Bet search
A broad **Semantic Execution State Substrate** should **not** be created as a new Bet from this paper.

The white space, if any, is narrower:
> can the high cost of semantic state maintenance be reduced by a reusable runtime/system mechanism while preserving AgentProg-level information value?

That is an open hypothesis, not yet a Direction, because the paper provides no evidence that OS/CPU control is the limiting factor.

## Q10 — Next action

1. **KEEP PAPER-056 as P0**.
2. Create a canonical Claim for the demonstrated long-horizon semantic-state information value.
3. Strengthen A's B4-TX baseline to include reconstructible program/control/data-flow/belief state.
4. Do not change A's 82.5 Primary-Bet lane or maturity.
5. Do not create a new semantic-state second Bet.
6. Treat AgentProg's latency/token cost as a workload pressure to investigate later, not as proof of lower-layer need.
7. Snowball the MobileLLM/THU-AIR lineage, especially AutoDroid-V2 and related mobile-Agent verification/benchmark work.
8. In future target-phone experiments, separate:
   - semantic information value;
   - cost of maintaining/processing that information;
   - incremental lower-layer/system value beyond optimized application/runtime representation.

## Decision footer
- **New-regime relevance:** Agent-native/amplified long-horizon semantic state
- **Evidence maturity:** **SYSTEM_VALUE** for task-completion/context correctness on evaluated Android benchmarks; **NOT_EVALUATED** for on-device resource efficiency
- **Decision impact:** strengthen semantic-information premise and A software/runtime baseline; no Direction promotion
- **A impact:** baseline strengthening; no direct support for CLM-A-001
- **PT-A impact:** contextual support only
- **C impact:** no target-phone system-control residual
- **R3 impact:** remain BLOCKED; reinforces software-first semantic handling
- **Second-Bet impact:** broad semantic-state substrate not promoted
- **Open questions:** on-device SLM transfer, latency/token reduction, energy/thermal/QoE, semantic-state compression, lower-layer residual after optimized runtime
- **Primary source:** https://arxiv.org/abs/2512.10371
- **ACM source:** https://doi.org/10.1145/3745756.3809245
- **Artifact:** https://github.com/MobileLLM/AgentProg
