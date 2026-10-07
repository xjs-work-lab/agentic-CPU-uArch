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
- **C — Efficient System-Control Substrate** — STRATEGIC_ENABLER / 72.0

C's previous second-Bet watch is closed on current evidence. Generic/Agent-aware system-control patterns are heavily occupied by strong existing baselines.

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

## Current research frontier — H-CAL
**H-CAL — Contiguous Agent Learning**  
Status: **ANALYSIS HYPOTHESIS / NARROWED / NOT A DIRECTION**

PAPER-089 exposes a genuinely Agent-native regime: live inference continues while feedback/judge/training work updates adapters and changes KV-cache validity.

PAPER-091 establishes that sustained phone training has real battery/thermal/runtime cost.

Strong generic baselines already capture much of mobile training:
- FBLayout — layout/data movement;
- MobileFineTuner — mobile-native memory/energy runtime;
- MeSP — activation-memory reduction;
- repaired phone backward kernel — major speed/energy recovery.

### Surviving question
> On a real smartphone, does **live Agent serving + repeated adaptation + versioned KV/model state** create a reusable residual beyond C, B-residual and R2 after strongest training/runtime baselines?

## Next
Run one targeted residual round for direct smartphone concurrent inference + local adaptation / online Agent learning.

Promotion requires smartphone SYSTEM_VALUE plus software insufficiency. Kill/merge if the residual is reconstructible by C/B/R2/runtime software.
