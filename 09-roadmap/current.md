+++
id = "ROADMAP-CURRENT"
type = "ROADMAP"
record_state = "CURRENT"
roadmap_kind = "DIFFERENTIATION_PORTFOLIO"
direction_ids = ["A", "PT-A", "C", "CG-06", "CG-07", "CG-01", "B-residual", "R1", "R2", "R3"]
scope = "2027_2029_PUBLIC_ONLY_ROUND15E_FORMAL_CONVERGENCE"
+++

# Canonical Current Strategic Investment Portfolio — Round15E

Updated: 2026-10-08
Decision authority: [DEC-PORTFOLIO-002](../08-decisions/events/DEC-PORTFOLIO-002.md), [DEC-A-008](../08-decisions/events/DEC-A-008.md), [DEC-R1-002](../08-decisions/events/DEC-R1-002.md).
Evidence analysis: [Round15E formal reconciliation](../analysis/opportunities/round15e-formal-portfolio-reconciliation-2026-10-08.md).
Timeline: [Round15E integrated roadmap](round15e-integrated-public-roadmap-2027-2029.md).
Rule: **public-source-only / zero new experiments or tests**, throughout final strategic report.

## Decision summary: two investment types that must never be merged

### A. Priority engineering / platform investments — **3**, not three differentiated hardware Primary Bets
- **CG-06 — INVEST ENGINEERING / 86.5 historical score context / STRUCTURAL_SIGNAL:** CPU-local and LLVM/AArch64 inference/control fast path where real phone stage/operator behavior and strong NPU/heterogeneous software economics warrant maintaining an optimized CPU role. No CPU always wins conclusion, no new ISA need.
- **PT-A — PLATFORM_TRACK / 80.0 historical context / SYSTEM_VALUE:** permission/authority-aware Agent tool routing, fresh target binding, outcome verification and bounded recovery, owned primarily by software/OS.
- **C — STRATEGIC_ENABLER / 72.0 historical context / SYSTEM_VALUE:** runtime/OS heterogeneous NPU/CPU/GPU coordination, critical-path and foreground QoE. Existing Android NPU Manager, Agent.xpu/HeRo and utility-aware scheduling are mandatory baselines.

These are real follow/build/invest priorities justified by literature and public product/OS material; they **do not claim differentiated proprietary mobile CPU hardware**.

### B. Independent differentiated Primary Bets — **0 currently supported for budget-grade nomination**
- **A formally downgraded:** `PRIMARY_BET → CONDITIONAL_RESERVE`. Historical `82.5 / SIMULATION_SUPPORT` retired as current allocation confidence; residual private `RequiredProgress` information is still **OPEN**, not publicly demonstrated beyond B4-TX.
- Second/third candidate: **UNFILLED**. **No new CPU-uArch or ISA Primary Bet.** This is an evidence-qualified conclusion, not an obligation to fill a number quota.

### C. Core Strategic Reserves — **3**, conditional public-research options
1. **A — Agent-private RequiredProgress information:** conditional info beyond complete observable history/ledger, user utility, permission, stage, model and OS status.
2. **B-residual — derived Agent physical-state validity across CPU/NPU/memory:** after strong software version/provenance/cache and QNN/HAL OS control.
3. **R2 — CPU continuation microstate/locality:** after role pooling, soft affinity, generic shared/cache facilities, and real published independent phone evidence limits; **no dedicated hardware**.

**R1 post-ready semantic release timing is WATCH**, not a core reserve. **CG-07 EXPLORE/FOLLOW** proactive low-power options; **CG-01 BENCHMARK/FOLLOW PUBLICLY** competitor shared CPU cache and cache migration. **R3 BLOCKED** new Agent semantic ISA/hardware hints.

## Do-not-invest: claim scope, not product abandonment
- New chip merely for generic Agent task scheduler/work cancel/model load priority already in OS APIs.
- Novelty claims for ordinary versioned Agent cache, user intent fulfillment grader, distributed transaction rollback, generic shared buffer/zero-copy or NPU context lifetime.
- Agent-specific CPU cache/predictor/TLB state structure or semantic ISA without public evidence of *both* irreducible physical residual and mobile significance.
- Unqualified dedicated always-on AI tier merely because product copy says Agentic. Existing CHRE/AOP and LP NPU remain important **FOLLOW** product ingredients.

## Reopen conditions within public-only research
- Independent original published work shows user/Agent-private progress carries outcome-relevant conditional information beyond B4-TX, and explains how the team controls it → review **A**.
- Comparable published mobile CPU/NPU stage/operator findings under optimized runtimes, compiler and backend improve/pinch the CPU-fast-path opportunity → update **CG-06**.
- Multiple first-party/peer-reviewed sources isolate costly cross-engine version/cancel/state lifetime beyond OS/SW controls → revisit **B** and uArch hypothesis.
- Future official standards/OEM disclosure show different on-device Agent resources or emerging silicon primitives → update **F/P/V** boundaries.

**Missing public data become confidence ceilings, not experiments planned by this research.**

## Historical provenance
- [DEC-PORTFOLIO-001](../08-decisions/events/DEC-PORTFOLIO-001.md) and [DEC-A-007](../08-decisions/events/DEC-A-007.md) explain the **previous** provisional PRIMARY_BET 82.5 state.
- [Round15D leadership pre-decision](round15d-leadership-portfolio-provisional-2027-2029.md) and [old final snapshot](final-2027-2029.md) are older interpretations, not active investment/experiment instructions.
- Full data lineage remains in canonical directions, claims, EvidenceCases, source IDs and Git history.
