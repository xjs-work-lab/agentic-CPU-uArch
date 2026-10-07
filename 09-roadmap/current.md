+++
id = "ROADMAP-CURRENT"
type = "ROADMAP"
record_state = "CURRENT"
roadmap_kind = "DIFFERENTIATION_PORTFOLIO"
direction_ids = ["A", "PT-A", "C", "CG-06", "CG-07", "CG-01", "B-residual", "R1", "R2", "R3"]
scope = "ACTIVE_V2_2_RESEARCH_AUTHORITY"
+++

# Current Roadmap Projection

Updated: 2026-10-07

## Authority
**V2.2 / xjs-work-lab/agentic-CPU-uArch is the active Research SSOT.**

## Active differentiated / platform lanes
- **A — Agent Semantic Progress Control** — PRIMARY_BET / 82.5 / SIMULATION_SUPPORT
- **PT-A — Heterogeneous Verified Agent Actuation Runtime** — PLATFORM_TRACK / 80.0 / SYSTEM_VALUE
- **C — Efficient System-Control Substrate** — STRATEGIC_ENABLER / 72.0 / SYSTEM_VALUE

C's previous second-Bet watch remains closed. Round 13 upgrades C's evidence maturity to **SYSTEM_VALUE** because HeRo demonstrates direct commercial-phone Agent-aware heterogeneous orchestration value; however, Agent.xpu/HeRo simultaneously raise the strongest software baseline, so differentiated residual remains unproven.

## Competitive-gap lanes
- **CG-06 — CPU-Resident Latency-Critical Agent AI Fast Path** — INVEST / 86.5
- **CG-07 — Dedicated Always-On Agent AI Domain** — EXPLORE / 75.0
- **CG-01 — Flex Cache / heterogeneous shared-cache handoff** — BENCHMARK / 71.0

### CG-07 Round-10 baseline update
PAPER-087 ProactiveMobile strengthens the workload premise: proactive smartphone Agents must repeatedly decide **intervene vs remain silent** from ongoing context before executable assistance.

PAPER-088 PRPF raises the strongest software/model baseline: lightweight pre-reasoning gating + candidate-function compression can suppress a large fraction of heavy reasoning in the evaluated benchmark.

Therefore CG-07 remains **EXPLORE / 75.0**:
- workload relevance strengthened;
- hardware residual narrowed;
- no score change.

The promotion question is now post-gating:
> Does a dedicated low-power front end beat the strongest CPU/shared-NPU gate after context-arrival rate, acceptance rate, gate cost, accepted-event handoff/wake cost, idle/residency, battery, thermal and foreground QoE are measured?

## Conditional reserves
- **B-residual** — 63.0
- **R1** — 55.5
- **R2** — 54.5

## Blocked
- **R3 — uArch Semantic Hints** — 48.5 / BLOCKED

## Current strategic gap
Second differentiated Primary Bet: **UNFILLED**.

H-FIB/system-control converged without a standalone Bet. H-PAM is killed as standalone. Confidential execution is platform/radar. Proactive/always-on gating is now covered inside CG-07 at seed + strongest-baseline level.

This is an evidence result, not a quota problem.

## H-CAL final decision
**H-CAL — Contiguous Agent Learning: CLOSED / KILLED AS STANDALONE CANDIDATE.**

Round 12 adds:
- PAPER-094 K-Merge — adapter lifecycle/merge is software-managed;
- PAPER-095 MobiLoRA — LoRA identity, mobile app lifecycle and KV retention/reuse are strong software-visible signals;
- PAPER-096 ZeroLock — training update dependency and activation lifetime can be changed algorithmically, including in an Android prototype.

The remaining workload is merged into existing ownership:
- update timing / foreground protection / thermal budget → **C**;
- adapter publication / stale-KV correctness → **B-residual**;
- cache locality/residency → **R2 / CG-01** only with direct phone residual;
- backward kernels/layout/training runtime → generic platform/compiler optimization.

The reviewed public source set still lacks a direct commercial-phone experiment combining live Agent serving with repeated local adaptation. That is a **reopen condition**, not evidence for promotion.

## Current strategic gap
Second differentiated Primary Bet remains **UNFILLED**.


## Product Evolution Map — cross-reference only

This file is the canonical **Differentiation Portfolio**. The canonical Product Evolution management view is `09-roadmap/product-evolution-map.md`.

Round 14 separates **product value** from **research novelty**.

> **Prior art constrains novelty, not product relevance.**

Current product-trend families:
- **T1** Semantic-aware progress & resource control — A / C
- **T2** Heterogeneous Agent AI execution continuum — C / CG-06
- **T3** Verified / transactional Agent actuation — PT-A
- **T4** Always-on proactive Agent front-end — CG-07
- **T5** Agent state lifecycle, reuse & locality — B-residual / CG-01 / R2
- **T6** Local programmable Agent execution & sandboxed skills — EMERGING_PRODUCT_TREND / BENCHMARK_AND_PREPARE; standalone differentiation closed; owned by C + B-residual/T5 + PT-A
- **T7** Local multi-Agent concurrency & shared model/state — frontier audit
- **T8** Cross-device Agent fabric & continuation — frontier audit

T1–T6 can remain important product programs even when broad novelty is crowded.
T6 is an emerging Product Trend whose standalone differentiated candidate is closed; T7 remains WATCH/owned by existing lanes and T8 is the next frontier audit.

Detailed view: `09-roadmap/product-evolution-map.md`.

## Round 14 trend reset

Initial coverage audit prioritizes **T7 Local Multi-Agent Concurrency** first.

Reason:
the seed scan shows stronger mobile/multi-agent/state-sharing signals than expected, but it is unclear whether they create a new control point or simply strengthen C/T5.

Round 14-A asks:
> Does local multi-Agent execution create a repeated smartphone system/physical control problem beyond ordinary workflow scheduling/xPU orchestration and state/KV lifecycle?

Possible outcomes:
- NEW DIRECTION
- MERGE INTO C
- MERGE INTO T5/B
- WATCH
- KILL_DIFFERENTIATED_BET

No product trend is killed merely because prior art exists.

## Current research frontier
**ROUND 14 ACTIVE — T7 Round 14-A complete; T6 Round 14-B complete; T8 Round 14-C next.**

## Evidence Rescue 1B — A
A remains **PRIMARY_BET / 82.5 / SIMULATION_SUPPORT**, with no promotion.

Its differentiated core is now deliberately narrow:

> **Does explicit Agent-internal DemandState / RequiredProgress contain end-outcome-relevant information that a strongest long-history + runtime-state + utility/SLO + topology + legality baseline cannot reconstruct?**

Deep-read corrections:
- PAPER-013 shows speculative/cancel/commit state is substantially runtime-visible and has negative transfer on naturalistic streaming instructions.
- PAPER-015 establishes proactive demand/authorization states, but effectful execution is already confirmation-gated.
- PAPER-043 is ICLR 2025 and shows behavioral history is learnable while false alarms remain substantial.
- PAPER-044 strengthens B4-TX with real, per-user, time-based long-history prediction.
- PAPER-050 strengthens runtime-derived Effect/Commit legality while exposing irreversibility/traceability barriers.

`EXP-A-001` is now a matched-observability residual test.
If B4-TX reproduces nearly all B6-Demand value, A must be downgraded or killed as differentiated research.

No SYSTEM_VALUE or hardware/uArch promotion.

## Evidence-depth state
Graph QA validates **0 paper-depth warnings** across A / PT-A / C / CG-06 / CG-07.
The remaining **12** current-roadmap paper warnings are all in B-residual / R1 / R2.

## T7 seed-triage result
Initial seeds:
- MobiMem
- LOCAL
- EcoAgent

Current pressure:
- MobiMem strongly supports Agent memory/replay/fine-grained mobile workflow productization, but mainly maps to C + T5/PT-A.
- LOCAL shows genuine cross-agent model/KV/adapter state sharing, but only on a 24 GB single-GPU setup, not a phone.
- EcoAgent validates mobile multi-Agent role decomposition, but not a distinct local shared-resource CPU control point.

Therefore T7 remains a **product trend candidate**, not a new Direction.

## MobiMem FULL_10Q
PAPER-103 materially strengthens **T5 product relevance** but does not establish a standalone T7 control point.

Key corrections:
- Snapdragon 8 Elite Action Memory result is CPU-only;
- highest 77.3% action reuse uses human-crafted templates;
- Experience Memory + AgentRR, not the full MobiMem stack, are claimed as deployed in a flagship smartphone;
- MobiMem/AgentRR shares the IPADS-SJTU MobiAgent lineage;
- fine-grained multi-app speedup is explained by explicit step-DAG dependencies.

No Trend maturity, portfolio lane, score or uArch promotion.

## LOCAL FULL_10Q
PAPER-104 strengthens T5's versioned-state lifecycle baseline and further narrows T7 standalone differentiation.

Key findings:
- one model instance serves foreground inference while judge/training/cache work compete for the same 24 GB GPU;
- KV validity is keyed by token span + context namespace + adapter + adapter version;
- Agent identity is provenance rather than an unconditional hard KV key;
- cross-Agent pending-consumer state drives speculative pre-prefill and reduces reported TTFT p99 by 21.9%;
- the useful signal maps to software-visible dependency/demand + state/version validity;
- no smartphone SoC, battery, thermal or foreground-app QoE evidence.

H-CAL's software baseline is strengthened but its standalone KILL_DIFFERENTIATED_BET remains unchanged.

No Trend maturity, portfolio lane, score or uArch promotion.

## EcoAgent FULL_10Q + T7 final decision
PAPER-105 / EcoAgent is AAAI 2026 and independently strengthens T3/PT-A's closed-loop verified-actuation product pattern.

Critical boundary:
the device-side ShowUI/OS-Atlas/Qwen2-VL models execute on an RTX 3090 24 GB local server to simulate mobile inference; AndroidWorld uses a Pixel 6 / Android 13 emulator.

Round 14-A T7 final:
- **Product Trend:** FRONTIER_SIGNAL / WATCH retained;
- **Differentiation:** KILL_DIFFERENTIATED_BET for a standalone T7 Bet/Direction;
- **Ownership:** merge into C + T5/B-residual + PT-A;
- **new Direction:** none;
- **second differentiated Primary Bet:** still UNFILLED;
- **uArch candidate:** none.

This does not kill the product trend.

## T6 Round 14-B seed-triage result

Initial seeds:
- **SkillDroid** — direct mobile GUI skill compilation/replay;
- **Android AppFunctions** — official Android local Agent-tool product baseline;
- **MCP-SandboxScan** — WASM/WASI sandbox security baseline;
- **SpecBox** — sandbox lifecycle / prewarm / memory-latency systems baseline.

Current pressure:
- SkillDroid establishes that repeated mobile Agent behavior can become a persistent executable interaction artifact, but the artifact is a typed GUI action program interpreted/replayed through Android automation rather than native/JIT-generated CPU code.
- Android AppFunctions establishes a real Android 16+ local tool/function substrate for privileged Agents, including type-safe sandboxed tool definitions and permission-controlled discovery/execution; its normal path is app-defined functionality, not Agent-generated executable code.
- MCP-SandboxScan shows that untrusted Agent tools create real runtime capability/provenance problems and that WASM/WASI is a viable isolation baseline, but it provides no smartphone-system value evidence.
- SpecBox shows that sandbox instantiation/residency can create latency-memory tradeoffs, but its multi-tenant server regime is a strongest generic systems baseline rather than evidence for a phone-specific Direction.

Therefore T6 remains **FRONTIER_SIGNAL / WATCH** and no Direction is created.

The surviving residual question is deliberately narrow:

> On a representative phone, do frequently created or changing Agent-executable artifacts create material compile/validate/load/instantiate/interpreter/JIT/code-cache/sandbox-transition costs, with a control variable that cannot be reduced to ordinary AppFunction invocation, workflow scheduling (C), state/version lifecycle (T5) or authority/verification (PT-A)?

## SkillDroid FULL_10Q
PAPER-106 strengthens T6's **product signal** but narrows the differentiated CPU/uArch case.

What survives:
- successful LLM-guided Android GUI trajectories can be materialized into persistent parameterized action programs;
- a controlled same-stack baseline shows higher success and lower LLM-call demand with skill reuse;
- pure replay can execute without an LLM call and the skill library can be versioned/recompiled after failures.

What does **not** survive:
- "compile" does not mean native code generation, WASM, bytecode/JIT or a new instruction-stream regime;
- experiments run on a Windows 11 host driving a Pixel 9a/API 35 emulator through ADB;
- the paper notes ~100 ms ADB action latency versus ~4 ms for native AccessibilityService performAction();
- no physical-phone CPU, energy, thermal, code-cache, JIT/interpreter or foreground-QoE residual is measured.

Ownership pressure after FULL_10Q:
- versioned executable procedural state / reuse → **T5**;
- verification, fallback and execution provenance → **PT-A**;
- execution/warm-cold/resource policy → **C**.

Therefore T6 remains **FRONTIER_SIGNAL / WATCH** with no new Direction, no score/lane change and no uArch candidate.

## Android AppFunctions deep vendor baseline
VENDOR-020 changes the **product** conclusion but not the differentiated portfolio.

Official Android documentation now establishes:
- Android 16+ platform + Jetpack AppFunctions for exposing app capabilities to Agent callers;
- an OS-managed registry for discovery and local execution;
- typed schemas/tool definitions generated from app declarations;
- explicit enabled state and permission/access-level control;
- experimental runtime registration in AndroidX 1.0.0-alpha12 / API 37, with callback lifetime tied to the registering process/context.

Combined with PAPER-106 / SkillDroid, this is enough to promote T6 from **FRONTIER_SIGNAL / WATCH** to:
- **EMERGING_PRODUCT_TREND**
- **BENCHMARK_AND_PREPARE**

Why not PRODUCTIZE / ESTABLISHED_PRODUCT_TREND:
- AppFunctions remains an experimental preview / limited end-to-end access path;
- SkillDroid is emulator/ADB evidence rather than target-phone native execution;
- representative phone frequency, cost, energy and QoE are still missing.

Differentiation remains conservative:
- AppFunctions raises the strongest platform baseline for function discovery, typed execution, permissions and lifecycle;
- runtime registration registers callbacks/functions; it is not evidence of arbitrary Agent-generated native/JIT code;
- T6 still has **no Direction**, no score/lane change and no uArch candidate.

## Next
Pressure-test **MCP-SandboxScan** and **SpecBox** only as strongest runtime baselines for truly dynamic executable artifacts (WASM/DSL/bytecode/sandbox instances).

The remaining discriminator is:
> after AppFunctions + T5 state/version reuse + PT-A authority/verification + C lifecycle/resource control, is there a material target-phone compile/validate/instantiate/JIT/code-cache/sandbox-transition residual?

Reserve-lane/patent audit remains required before final portfolio convergence.

## Round 13 — Agent-flow heterogeneous SoC orchestration

FULL_10Q:
- **PAPER-097 Agent.xpu** — mixed reactive/proactive Agent-flow scheduling on commodity hetero-SoC;
- **PAPER-098 HeRo** — direct commercial-phone dynamic Agentic-RAG orchestration across CPU/GPU/NPU;
- **PAPER-099 MobileExplorer** — reasoning-window speculative GUI exploration + rollback;
- **PAPER-100 Jev-Mobile** — low-frequency semantic planning + high-frequency typed GUI execution.

### Portfolio decision
- **C:** evidence maturity **STRUCTURAL_SIGNAL → SYSTEM_VALUE**; lane **STRATEGIC_ENABLER / 72.0 unchanged**.
- **CG-06:** baseline raised to include Agent.xpu/HeRo-class dynamic xPU orchestration; **INVEST / 86.5 unchanged**.
- **PT-A:** MobileExplorer strengthens speculative-effect/rollback workload; **80.0 unchanged**.
- **A:** Jev-Mobile strengthens hierarchical software decomposition baseline; **82.5 unchanged**.
- **new Direction:** none.
- **second differentiated Primary Bet:** still **UNFILLED**.

### Why no new Bet
HeRo establishes that dynamic Agent workflow state has real phone system value, but the decisive control variables—partial DAG, stage criticality, accelerator affinity, shape and bandwidth—are already explicit software/runtime state. The same evidence that upgrades C's maturity also raises the baseline any differentiated C/CG-06 mechanism must beat.

## Current frontier
**NONE / UNASSIGNED after Round 13.**

Continue frontier reset outside already-owned scheduling/orchestration, memory, security, proactive gating and continual-learning families.


## T6 Round 14-B final — SandScope + SpecBox pressure closeout

### PAPER-107 — MCP-SandboxScan / SandScope v2
SandScope makes Agent-tool authority/provenance and runtime containment concrete, but its v2 evidence is negative pressure on a standalone T6 mechanism:
- WASI is one optional backend for portable artifacts/shims;
- real-world MCP coverage also uses native stdio and OS-level containment;
- its contribution is not “WASM instead of OS sandboxing”;
- no smartphone, JIT, code-cache, battery or thermal residual is measured.

### PAPER-108 — SpecBox
SpecBox demonstrates meaningful sandbox lifecycle cost, but in a 16-core / 256 GiB / Docker server regime. Its effective mechanisms are software-visible intent prediction, prewarm/prefetch, workflow-history state, semantic result reuse and shared-memory transport.

### Final decision
- T6 Product Trend: **KEEP EMERGING_PRODUCT_TREND / BENCHMARK_AND_PREPARE**
- standalone T6-specific candidate: **KILL_DIFFERENTIATED_BET**
- ownership: **C + B-residual/T5 + PT-A**
- no T6-specific Direction
- no second Primary Bet
- no uArch candidate

### Reopen gate
Only reopen standalone T6 differentiation with representative physical-phone evidence showing residual dynamic-code/bytecode/WASM generation, interpreter/JIT cost, code-cache churn, sandbox-transition cost, or energy/thermal/QoE after native AppFunctions + C/T5/PT-A baselines.

## Next
**Round 14-C — T8 Cross-device Agent fabric & continuation.**
