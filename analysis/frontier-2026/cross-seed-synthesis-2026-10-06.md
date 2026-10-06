# Frontier Cross-Seed Synthesis — 2026-10-06

## Decision question
After full 10Q review of the first authority-guided frontier seeds, is there credible evidence for a second differentiated Primary Bet?

## Reviewed decision-grade seed set
- PAPER-053 — Agent-X
- PAPER-054 — TimelyLLM
- PAPER-003 — Sereno (existing canonical Source; current 10Q refreshed)
- PAPER-056 — AgentProg
- PAPER-057 — ShadowNPU

All five are now decision-grade within explicit scope boundaries.

## Cross-paper pattern

### 1. Agent-specific structure has real information value
Agent-X and AgentProg independently show that Agent workloads expose exploitable structure beyond generic chat inference:
- tool/prompt/output regularity;
- explicit control-flow;
- persistent task variables;
- semantic step identity;
- belief/environment state.

**But:** both papers consume this structure at the application/runtime layer and obtain large value without new OS/CPU/uArch mechanisms.

### 2. Time utility is real, but already software-actionable
TimelyLLM shows that when an Agent output becomes useful can be more important than raw request completion time.

**But:** segmented generation + slack/remaining-work scheduling captures substantial value in the serving layer.

Consequence:
- broad 'time utility scheduling' is crowded;
- R1 must remain strictly post-ready and beyond strong latest-start/slack baselines.

### 3. Persistent/background AI creates real smartphone user conflict
Sereno provides direct commercial-phone evidence that background NPU inference can severely harm foreground QoE through shared-memory-bandwidth contention.

**But:** a software-only fine-grained yielding/control loop recovers much of the value.

Consequence:
- Foreground-Protected Persistent Agent becomes a mandatory user-value scenario;
- generic QoS/bandwidth protection becomes part of G1/B4, not differentiated C value.

### 4. Heterogeneous placement is important, but the optimized NPU frontier moves
ShadowNPU shows that sophisticated sub-operator numerical-role decomposition, quantization-aware placement, graph bucketing and CPU/NPU pipelining can reclaim CPU/GPU fallback work on real phones.

Consequence:
- heterogeneous placement is a high-value control point;
- the CPU-resident region is **smaller than a naive NPU comparison suggests**;
- CG-06 must beat NPU-OPT/HETERO-OPT, not NPU-BASE.

## Core tension exposed by the five papers

> **Agent semantics are valuable, and mobile resource conflicts are real — yet the direct evidence repeatedly shows large capture by application/runtime/compiler/optimized heterogeneous software before hardware is needed.**

This is not a negative result for the project.
It identifies the real research frontier:

> Which Agent-specific information remains both **non-reconstructible by strong upper-layer software** and **causally useful for reusable lower-layer resource decisions**?

That residual is the only credible path to a differentiated second Bet or later uArch candidate.

## Portfolio impact

| Direction | Cross-seed result | State |
|---|---|---|
| A | semantic-information premise stronger, but B4-TX also stronger | PRIMARY_BET / 82.5 unchanged |
| PT-A | structured actuation/context evidence relevant, no differentiated residual change | PLATFORM_TRACK unchanged |
| C | real phone control/QoE problem stronger, but G1 software baseline stronger | STRATEGIC_ENABLER / 72 unchanged |
| CG-06 | placement thesis stronger, CPU whitespace narrower; NPU-OPT baseline required | INVEST / 86.5 unchanged |
| R1 | broad timing novelty further crowded | CONDITIONAL_RESERVE unchanged |
| R2 | no new direct phone-PMU Agent residual | CONDITIONAL_RESERVE unchanged |
| R3 | software-first evidence becomes stronger | BLOCKED unchanged |

## Second-Bet candidate audit

### Candidate A — Broad Execution-Time Utility Control
**NARROW / NOT A NEW BET.**

TimelyLLM already occupies the broad formulation at serving-runtime level.
Only a residual unavailable to that layer remains worth testing.

### Candidate B — Foreground-Protected Persistent Agent Control Plane
**KEEP AS USER SCENARIO / NOT YET A DIFFERENTIATED BET.**

Sereno proves the problem, but also proves large generic software capture.
A Bet requires Agent-specific incremental value beyond QoS/bandwidth control.

### Candidate C — Agent-Aware Heterogeneous Stage Graph Placement
**NARROW / NOT YET DIFFERENTIATED.**

ShadowNPU and prior mobile LLM work show that model/operator numerical properties alone already support sophisticated placement.
A differentiated Agent route must add value from semantic criticality/useful-time/discardability/state reuse beyond generic operator placement.

### Candidate D — Semantic Execution State Substrate
**NARROW / NOT A NEW BET.**

AgentProg proves semantic state value but also demonstrates application/runtime ownership.
High token/latency cost is pressure for optimization, not proof that state should move to OS/CPU/uArch.

## New residual hypothesis for next snowball

### H-SCL — Semantic Control Lowering
Working hypothesis, **not a Direction**:

> A compiler/runtime layer may derive a small set of portable low-level control facts from rich Agent state (criticality, useful-by time, release/cancel legality, resource budget, state-reuse identity) and map them onto existing OS/runtime/CPU/NPU controls more efficiently than each Agent framework implementing bespoke control.

Why investigate:
- the reviewed papers expose multiple useful semantic variables;
- today they are consumed in siloed application-specific mechanisms;
- a reusable translation layer could be within the team's compiler/runtime control surface;
- it can be tested software-first before any hardware discussion.

Why it may die:
- existing schedulers/workflow runtimes may already reconstruct the same signals;
- per-application specialized mechanisms may outperform a common abstraction;
- translation overhead/semantic mismatch may erase value;
- PT-A/C/A may already cover the useful portion, making a separate Direction unnecessary.

## Next authority-guided snowball

### Stream 1 — Semantic/control lowering and workflow-aware systems
Search ASPLOS / OSDI / SOSP / PLDI / CGO for:
- workflow/task-graph aware scheduling;
- compiler/runtime extraction of criticality/deadline/slack;
- semantic QoS/control lowering;
- heterogeneous runtime resource hints;
- agent/runtime OS integration.

Goal: pressure-test H-SCL and C.

### Stream 2 — Strong on-device mobile Agent software baseline
Deep-review:
- AutoDroid-V2 (MobiSys 2025);
- closely related on-device SLM/code-generation mobile-Agent systems;
- Mobile-Agent-v3 / other strong GUI-Agent execution baselines only where system cost is decision-relevant.

Goal: test whether AgentProg-style semantic-state cost is already software/model-capturable.

### Stream 3 — Optimized heterogeneous/NPU frontier
Deep-review:
- llm.npu / Fast On-device LLM Inference with NPUs (ASPLOS 2025);
- HeteroLLM;
- relevant NPU compiler/quantization work.

Goal: establish the strongest NPU-OPT baseline before interpreting CG-06 whitespace.

### Stream 4 — Architecture residual search
Only after Streams 1-3:
- ISCA / MICRO / HPCA / ASPLOS hardware mechanisms;
- search for hardware-state visibility/reaction-time limitations that software cannot overcome.

Do not start from hardware ideas.

## Current conclusion
**No second differentiated Primary Bet is justified by the first five frontier seeds.**

This result increases confidence in the existing portfolio rather than indicating failure:
- A remains differentiated but faces a stronger baseline;
- C remains the most plausible second-Bet watch, but its residual is unproven;
- CG-06 remains strategically important but should be evaluated against a much stronger optimized-NPU frontier;
- hardware remains gated.
