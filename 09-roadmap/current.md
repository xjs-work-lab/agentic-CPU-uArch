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


## Product Evolution Map — new governing view

Round 14 now separates **product value** from **research novelty**.

> **Prior art constrains novelty, not product relevance.**

Current product-trend families:
- **T1** Semantic-aware progress & resource control — A / C
- **T2** Heterogeneous Agent AI execution continuum — C / CG-06
- **T3** Verified / transactional Agent actuation — PT-A
- **T4** Always-on proactive Agent front-end — CG-07
- **T5** Agent state lifecycle, reuse & locality — B-residual / CG-01 / R2
- **T6** Local programmable Agent execution & sandboxed skills — frontier audit
- **T7** Local multi-Agent concurrency & shared model/state — frontier audit
- **T8** Cross-device Agent fabric & continuation — frontier audit

T1–T5 can remain important product programs even when broad novelty is crowded.
T6–T8 are not Directions until they survive structural-residual testing.

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
- KILL differentiated novelty

No product trend is killed merely because prior art exists.

## Current research frontier
**ROUND 14 ACTIVE — MobiMem FULL_10Q complete; LOCAL next.**

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

## Next
FULL_10Q in order:
1. LOCAL
2. EcoAgent

Then issue an ownership/residual decision:
NEW DIRECTION / MERGE INTO C / MERGE INTO T5-B-PT-A / WATCH / KILL differentiated novelty.

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
