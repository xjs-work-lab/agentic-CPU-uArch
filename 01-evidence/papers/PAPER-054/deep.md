# PAPER-054 — TimelyLLM: Time-sensitive LLM Serving System for Physical-I/O Limited Agents

## Source
- Final paper: https://doi.org/10.1145/3745756.3809203
- Final author page: https://www.anuragkhandelwal.com/papers/timelyllm/
- Earlier detailed preprint: https://arxiv.org/abs/2412.18695
- Artifact: https://github.com/Neawhen/TimelyLLM
- Final authors: Neiwen Ling, Guojun Chen, Anurag Khandelwal, Lin Zhong
- Affiliation / lineage: Yale Efficient Computing Lab + NOVA Lab
- Venue: ACM MobiSys 2026
- Awards: Best Paper Award Runner-Up; Best Artifact Award Runner-Up
- Evaluated workload family: physical-I/O-limited Agents including drones, robot arms and quadrupeds in the final paper
- Artifact reference platform: single NVIDIA RTX 4090 / CUDA 12.1; Meta-Llama-3-8B-Instruct default
- Priority: P0
- Project relevance: time-utility semantics; strongest timing/scheduling baseline for R1; software/system-control pressure for C; boundary for any "execution-time utility" second-Bet hypothesis

## Version note — final paper vs earlier preprint

The detailed 2024 preprint is titled:
**TimelyLLM: Segmented LLM Serving System for Time-sensitive Robotic Applications**
and reports up to **1.97x** time-utility improvement.

The final MobiSys 2026 paper is titled:
**TimelyLLM: Time-sensitive LLM Serving System for Physical-I/O Limited Agents**
and its final abstract reports up to **1.52x** time-utility improvement and **84%** lower overall waiting time.

These values must not be merged as if they came from one identical experiment version.

For decision use:
- use the **final MobiSys 2026 1.52x / 84%** as the headline published result;
- use the earlier preprint only for detailed mechanism/evaluation reconstruction where the final public abstract is less detailed.

## Q1 — Problem + target mapping

### Paper problem
Conventional LLM serving optimizes request/token throughput and latency as if generated output becomes equally valuable immediately.

Physical-I/O Agents violate that assumption:
- the LLM generates a multi-step plan;
- the Agent can begin physically executing an early action before the whole plan is generated;
- physical action can take much longer than generation of the next segment;
- therefore some future generation can be delayed without delaying the Agent, while other requests may be urgent.

TimelyLLM reframes the objective from:
> "finish this entire generation as soon as possible"

to:
> "generate each actionable segment before the physical Agent needs it."

### Mapping to this project
This is directly relevant to our broader question:
**when is Agent computation actually useful?**

But its control point is not identical to our surviving R1 residual.

TimelyLLM primarily schedules computation **before a future output/dependency is fully ready**:
- generate one actionable segment;
- exploit the physical execution interval as slack;
- schedule later generation so the next segment arrives in time.

R1 is deliberately narrower:
> **after a dependency is already physically ready**, does explicit ReleasePermission / LatestUsefulResume expose additional safe delay that a strong generic scheduler cannot reconstruct?

Therefore:
- TimelyLLM is strong adjacent prior art and baseline pressure;
- it does not directly test or kill the surviving R1 post-ready residual.

Target-transfer boundary:
- physical robots / edge GPU serving, not smartphone persistent Agents;
- no target-phone energy/thermal/foreground-QoE evidence.

## Q2 — Novelty / new-regime relevance

### Agent-native / amplified element
The key operating regime is **coupling between LLM generation and physical execution time**.

A generated token/segment has a time-dependent utility:
- too late → Agent waits;
- sufficiently early → no extra Agent benefit from being even earlier;
- generating far ahead can consume serving capacity that a more urgent Agent needs.

This is not ordinary chat-serving semantics.

### Generic elements
TimelyLLM builds on generic serving/scheduling mechanisms:
- continuous batching;
- FCFS / EDF-like urgency baselines;
- suspend/resume;
- KV/context preservation;
- remaining-work estimation;
- priority scheduling.

Thus the project-relevant novelty is:
> exposing a time-utility structure from Agent execution and using it to drive software scheduling.

It does **not** establish a need for a new CPU instruction, scheduler primitive or uArch state.

## Q3 — Falsifiable hypothesis

The core hypothesis is:

> If plan generation can be segmented at actionable boundaries and the system can estimate when the next segment will be needed, then serving capacity can be reallocated during physical-execution slack, improving time utility and reducing Agent waiting under contention.

Expected falsifiers include:
- action boundaries cannot be detected reliably;
- execution-time estimates are too unstable to expose useful slack;
- suspend/resume overhead consumes the slack;
- segmented generation harms model/plan correctness;
- under multi-Agent contention, priority scheduling does not improve useful-time delivery over strong baselines.

Within the evaluated physical-Agent workloads, the published result supports the hypothesis.

Smartphone transfer remains untested.

## Q4 — Research lineage / competing route

### Lineage
TimelyLLM sits in a sustained Yale systems line rather than appearing as an isolated Agent paper.

Relevant lineage includes:
- **TypeFly** — low-latency drone planning that streams generated plans so physical execution can start before full generation;
- **Prompt Cache (MLSys 2024)** — modular reuse of attention state to reduce inference latency;
- later programmable/Agent-oriented serving work in the same research ecosystem.

TimelyLLM's step beyond TypeFly is important:
> it not only starts execution early; it can stop/defer later generation and reallocate the serving resource according to when output will actually be needed.

### Strong competing baselines
Decision-grade comparison should include:
- vLLM / conventional continuous batching;
- full-plan generation before execution;
- streaming execution without service reallocation;
- segmented generation + FCFS;
- segmented generation + EDF/deadline scheduling;
- generic slack/latest-start scheduling;
- generic workload/remaining-time prediction;
- application/runtime supplied deadlines.

### Project boundary
For R1, this paper reinforces why our B4-release baseline must already include:
- deadlines;
- latest-start/slack;
- execution-duration estimates;
- batching/coalescing;
- urgency-aware scheduling.

Any R1 novelty that overlaps those mechanisms is already crowded.

## Q5 — Key mechanism / control point

TimelyLLM has two coupled control points.

### 1. Segmented generation
The system identifies an actionable program/plan segment and can stop generation once that segment is executable.

The public artifact's MiniSpec stop checker parses generated program structure and detects executable actions, making the segmentation mechanism inspectable in code.

### 2. Time-aware serving scheduler
For each task, the artifact tracks information including:
- predicted previous physical-execution completion (`exe_end_pre`);
- finished generated tokens;
- remaining work estimate;
- communication time;
- robot/workload-specific timing parameters.

The scheduler compares remaining generation work against available slack and selects the most urgent task.

This turns **future physical execution time** into a scheduling signal.

### Why this matters
This is a concrete example of:
> Agent/application semantic state → runtime scheduling value.

But the demonstrated consumer is a software LLM serving scheduler.

That is strong evidence for **semantic value**, not hardware necessity.

## Q6 — Experiment design

### Final-paper scope
The final MobiSys abstract reports workloads derived from:
- drones;
- robot arms;
- quadrupeds.

### Detailed preprint / artifact reconstruction
The earlier detailed evaluation and current artifact expose:
- drone / TypeFly-style workloads;
- robot-arm workloads;
- Llama-class serving;
- single-GPU edge execution;
- multi-Agent request contention.

Artifact defaults/presets include:
- single RTX 4090 target;
- Meta-Llama-3-8B-Instruct;
- TimelyLLM vs vLLM;
- TimelyLLM vs EDF;
- TimelyLLM vs FCFS;
- high-load drone preset with 42 Agents;
- robot-arm preset with 94 Agents.

### Published headline
Final MobiSys 2026:
- up to **1.52x** improvement in time utility;
- up to **84%** reduction in overall waiting time.

### Earlier-version detailed anchors
The earlier preprint reports:
- up to **1.97x** time-utility improvement;
- the same up-to **84%** waiting-time reduction;
- experiments comparing FCFS / EDF / segmented scheduling under contention.

These earlier-version numbers are retained only with the version boundary above.

## Q7 — Data / artifact / reproducibility

### Strong points
TimelyLLM has a public artifact with:
- environment instructions;
- Docker and direct setup;
- experiment presets;
- datasets/traces;
- plotting scripts;
- scheduler implementation;
- stop-rule implementation;
- vLLM-based serving engine modifications.

The artifact was recognized as **Best Artifact Award Runner-Up** at MobiSys 2026.

This is materially stronger than a paper-only claim.

### Artifact-level inspectable details
The public config exposes:
- TimelyLLM / vLLM / EDF / FCFS presets;
- agent counts;
- robot-system modes;
- batch size;
- segment execution estimates;
- model and request paths.

The scheduler source exposes the urgency calculation and task timing state.

### Remaining reproducibility boundary
This review did **not** independently rerun the GPU experiments.

Therefore:
- artifact availability = verified;
- exact published numerical reproduction = not independently verified by this project.

## Q8 — Evidence vs hypothesis

### [FACT — final published scope]
The final MobiSys paper reports that TimelyLLM improves time utility by up to 1.52x and lowers overall Agent waiting by up to 84% on its evaluated physical-I/O Agent workloads.

### [FACT — implementation]
The public artifact implements:
- segmented action-aware stopping;
- task timing state;
- remaining-work/slack-aware priority scheduling;
- explicit FCFS and EDF comparison presets.

### [OBSERVATION]
For physical-I/O Agents, token-generation urgency is coupled to **when a generated action will become useful**, not only to request arrival or token throughput.

### [INFERENCE — project]
A time-indexed notion of output utility can be an actionable system-control variable.

### Not established
- smartphone SYSTEM_VALUE;
- phone energy or thermal value;
- foreground-app QoE;
- DemandState / RequiredProgress residual;
- R1's strictly post-ready semantic residual;
- CPU↔NPU placement;
- software insufficiency;
- hardware/uArch necessity.

## Q9 — Real contribution to the project decision

### R1 — Post-ready Continuation Timing
**NARROW / stronger baseline pressure; no lane/score change.**

TimelyLLM makes it harder to claim broad "semantic timing" novelty.

It demonstrates that substantial value can already be captured by:
- execution-duration awareness;
- segmentation;
- slack;
- remaining-work estimation;
- software scheduling.

Therefore R1's surviving question must stay strictly:
> after work/dependency is already ready, is there additional semantic LatestUsefulResume / ReleasePermission information that TimelyLLM/EDF/slack/latest-start-style software cannot infer?

This paper does **not** kill that residual because it targets an earlier stage of the timeline.

### A — Agent Semantic Progress Control
**No promotion / no direct support for CLM-A-001.**

TimelyLLM shows that "useful now" differs from "can compute now", but it does not test:
- Required / Optional / Speculative progress;
- DemandState;
- cancellation legality;
- B4-TX residual.

It is best treated as an adjacent strong scheduling baseline.

### C — Efficient System-Control Substrate
**Strengthen problem relevance + strengthen software baseline; no promotion.**

The paper proves that Agent/physical-execution state can improve serving decisions.

But the demonstrated value lives in:
- application/serving runtime;
- existing GPU;
- software scheduling.

Therefore C cannot claim this value again unless it finds a residual beyond such upper-layer scheduling on a target phone.

### R3 / hardware
**Remain BLOCKED.**

TimelyLLM strengthens the software-first case:
the relevant timing semantics can already be consumed by software.

### Second-Bet hypothesis — Execution-Time Utility Control
**Do not create a new Direction yet.**

The broad idea:
> "schedule Agent compute by when output will be useful"

is already materially occupied by TimelyLLM.

Any surviving differentiated candidate must be narrower and smartphone-specific, for example a residual involving:
- cross-engine CPU/NPU/GPU coordination;
- foreground-QoE / thermal budgets;
- persistent background Agent operation;
- useful-time state unavailable or too late at the application serving layer.

Those are hypotheses for later testing, not conclusions from this paper.

## Q10 — Next action

1. **KEEP as P0**.
2. Add TimelyLLM to the strongest timing/scheduling prior-art baseline for R1.
3. Preserve the strict distinction:
   - **pre-ready useful-time generation scheduling** (TimelyLLM);
   - **post-ready semantic release timing** (surviving R1).
4. Do not change A/C/R1/R3 lane or score from this paper alone.
5. When designing future phone experiments, include:
   - EDF/latest-start/slack baselines;
   - execution-duration prediction;
   - segmented/deferred generation where applicable.
6. Snowball the Yale physical-Agent/system-serving lineage before claiming a new "time utility" direction.
7. Test whether smartphone Agents expose a residual after the upper-layer TimelyLLM-style control is applied.

## Decision footer
- **New-regime relevance:** Agent-native/amplified physical-I/O timing; generic scheduling implementation primitives
- **Evidence maturity:** **SYSTEM_VALUE** for the evaluated physical-Agent serving system; **STRUCTURAL_SIGNAL** for smartphone transfer
- **Decision impact:** narrow broad timing novelty; strengthen R1/C software baseline; no portfolio promotion
- **A impact:** no direct support; adjacent baseline pressure
- **C impact:** problem signal + stronger upper-layer capture; no target-phone residual established
- **R1 impact:** NARROW wording / strengthen B4-release baseline; surviving strictly post-ready residual remains open
- **R3 impact:** remain BLOCKED
- **Second-Bet impact:** broad "Execution-Time Utility Control" is too crowded to promote as a new Bet from this paper
- **Open questions:** phone transfer; execution-time prediction robustness; GUI/tool Agents; energy/thermal/QoE; cross-engine scheduling; residual unavailable to application runtime
- **Primary source:** https://doi.org/10.1145/3745756.3809203
- **Earlier detailed preprint:** https://arxiv.org/abs/2412.18695
- **Artifact:** https://github.com/Neawhen/TimelyLLM
