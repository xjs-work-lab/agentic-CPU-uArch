+++
id = "ROADMAP-CURRENT"
type = "ROADMAP"
record_state = "CURRENT"
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

## Current research frontier
**NONE / UNASSIGNED.**

## Next
Resume the frontier reset outside already-covered families. Do not reopen H-CAL unless direct target-phone evidence shows a material residual beyond LOCAL + MobiLoRA + strongest mobile-training/scheduling baselines that existing C/B/R2 software cannot represent.


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
