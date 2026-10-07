# Research Authority Status

Updated: 2026-10-07

```yaml
migration_phase: CUTOVER_COMPLETE
research_authority: V2_2
graph_schema: 2.3
authority_repository: xjs-work-lab/agentic-CPU-uArch
historical_source_authority: V1_FROZEN
historical_source_repository: xiejinsen/agentic-CPU-uArch
historical_source_commit: 960abb4ef50f050da3c6784d30826053d42e5c5d
migration_id: MIG-20261006-02
human_gate: APPROVED
human_gate_date: 2026-10-06
cutover_state: COMPLETE
research_content_migrated: true
evidence_rescue: ACTIVE
evidence_depth_protocol: EDP_V1
frontier_round14: COMPLETE
product_trend_framework: V1
shared_semantic_contract: STRATEGIC_KG_CORE_V1
```

## Authority
**V2.2 is the active Research SSOT.**

Repository: `xjs-work-lab/agentic-CPU-uArch`

## Current graph
- 447 canonical nodes
- 769 canonical semantic edges
- 769 generated reverse edges
- projection validated after Evidence Rescue 1B A deep audit
- Round 13 Graph QA: **PASS** — run `37607500340`, job `112746473467`
- Evidence Rescue Round 1 Graph QA: **PASS** — run `37609685036`, job `112753634718`
- Evidence Rescue 1A PT-A Graph QA: **PASS** — run `37611820867`, job `112760599058`
- Evidence Rescue 1A PT-A squash merge: `e6a83b36494ec9bcc044b3aec6441152efd132f1`
- Evidence Rescue 1B A Graph QA: **PASS** — run `37617038459`, job `112777774022`
- Evidence Rescue 1B A squash merge: `95cb25d3899353206c39c29ebed69ed3d324b4d9`
- Evidence Rescue 1B A work-branch cleanup: **PASS** — run `37617300996`

## Portfolio invariant
- **A — PRIMARY_BET / 82.5 / SIMULATION_SUPPORT**; Rescue-1B keeps it provisionally but narrows differentiation to non-reconstructible DemandState / RequiredProgress information value
- **PT-A — PLATFORM_TRACK / 80.0 / SYSTEM_VALUE**
- **C — STRATEGIC_ENABLER / 72.0 / SYSTEM_VALUE**
- **CG-06 — INVEST / 86.5**
- **CG-07 — EXPLORE / 75.0**
- **CG-01 — BENCHMARK / 71.0**
- B-residual — Conditional Reserve
- R1 — Conditional Reserve
- R2 — Conditional Reserve
- R3 — BLOCKED
- second differentiated Primary Bet — intentionally unfilled
- uArch Primary Bet — none

## Hardware gate
`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

## Evidence Rescue state

### Rescue-0
PAPER-009 / 041 / 051 / 052 re-read under EDP v1.

### Rescue-1A — PT-A
PAPER-037 / 038 / 039 / 040 / 042 re-read.
PAPER-101 Action Rebinding and PAPER-102 VeriGUI added.
PT-A remains PLATFORM_TRACK / 80.0 / SYSTEM_VALUE with a stronger context-bound actuation contract.

### Rescue-1B — A
PAPER-013 / 015 / 043 / 044 / 050 re-read under EDP v1.

Key decision:
- A remains **PRIMARY_BET / 82.5 / SIMULATION_SUPPORT**;
- no maturity promotion;
- no hardware/uArch promotion;
- `CLM-A-001` is now explicitly a **conditional-information residual**;
- `EXP-A-001` is strengthened into a matched-observability test.

Material corrections:
- PAPER-013: speculative/cancel/commit state is largely runtime-visible and naturalistic streaming transfer can regress.
- PAPER-015: effectful execution is gated behind proposal acceptance.
- PAPER-043: venue corrected to **ICLR 2025**; synthetic/generated training vs real test boundary preserved.
- PAPER-044: strong per-user/time-based long-history predictor baseline; observed help-seeking is a proxy, not intrinsic RequiredProgress.
- PAPER-050: runtime can derive substantial dependency/effect legality, but untraceable/irreversible effects remain barriers.

## Evidence-depth debt
After Rescue-1B, validated Graph-QA paper-depth warnings:
- primary A / PT-A / C / CG-06 / CG-07 lanes: **0**
- current reserve lanes B-residual / R1 / R2: **4**
- whole current ROADMAP: **4**

Reserve Rescue Batch 1 complete:
- PAPER-030 AgentProg → FULL_10Q;
- PAPER-029 Libra / on-device LLMaaS → FULL_10Q;
- PAPER-032 Versioned Execution → FULL_10Q;
- PAPER-033 LOCAL → FULL_10Q reused from identical primary source PAPER-104.

B-residual remains **CONDITIONAL_RESERVE / 63.0 / SIMULATION_SUPPORT**.
The rescue raises the strongest software/runtime baseline and does not establish target-phone cross-tier residual SYSTEM_VALUE.

Reserve Rescue Batch 2 complete:
- PAPER-028 PBKV → FULL_10Q;
- PAPER-031 CacheScout → FULL_10Q;
- PAPER-034 PLACEMEM → FULL_10Q;
- PAPER-035 Invalidation Contracts → FULL_10Q.

B-residual paper-depth debt is now **0**.

Batch-2 decision:
- future reuse can be predicted from workflow/history/runtime signals without a semantic ABI;
- semantic/provenance/validity/invalidation can already be represented as typed software control-plane state;
- no target-phone evidence establishes additional S2/S3 physical-artifact value beyond that strong baseline.

B-residual therefore remains **CONDITIONAL_RESERVE / 63.0 / SIMULATION_SUPPORT** with no score/maturity/uArch change.

R3 and other patent-heavy claims remain subject to a separate patent direct-claim audit.

## Shared strategic-model harmonization
CPU/uArch now explicitly conforms to the shared strategic knowledge-graph mother model used across research domains.

Core semantic chain:
`SOURCE → EVIDENCE_CASE → CLAIM → TREND → PRODUCT_EVOLUTION ROADMAP`
with the parallel differentiated path:
`CLAIM → DIRECTION → DIFFERENTIATION_PORTFOLIO ROADMAP`.

No Trend, Direction, score, maturity or portfolio conclusion changed in this harmonization.

## Data-model 2.3
Canonical **TREND** objects now separate product evolution from differentiated research.

- Product Evolution Roadmap → TREND
- Differentiation Portfolio → DIRECTION
- TREND owns Direction classification through `direction_links`

This is additive: research authority remains V2.2; existing evidence/history IDs are unchanged.

## Product-trend framework
Round 14 now uses the two-axis rule:

> **Prior art constrains novelty, not product relevance.**

Product evolution posture and differentiation posture are judged independently.

Current trend map:
- T1 Semantic-aware progress & resource control
- T2 Heterogeneous Agent AI execution continuum
- T3 Verified / transactional Agent actuation
- T4 Always-on proactive Agent front-end
- T5 Agent state lifecycle, reuse & locality
- T6 Local programmable Agent execution & sandboxed skills
- T7 Local multi-Agent concurrency & shared model/state
- T8 Cross-device Agent fabric & continuation

T1–T6 and T8 are now product-relevant/owned to different degrees.
T7 remains FRONTIER_SIGNAL / WATCH, with standalone differentiation closed.

## Operating rule
**Frontier Round 14 is COMPLETE.**

Round 14-A seed triage is complete.

MobiMem FULL_10Q: **COMPLETE**.
LOCAL FULL_10Q: **COMPLETE**.
EcoAgent FULL_10Q: **COMPLETE**.

T7 Round 14-A final:
- product trend = FRONTIER_SIGNAL / WATCH;
- standalone differentiated candidate = KILL_DIFFERENTIATED_BET;
- ownership = C + T5/B-residual + PT-A;
- no new Direction / no uArch candidate.

Round 14-B T6 seed triage: **COMPLETE / NOT DECISION-COMPLETE**.

Initial pressure set:
- **SkillDroid** — direct mobile GUI evidence that successful LLM trajectories can be compiled into typed, executable interaction programs and replayed without per-step LLM inference.
- **Android AppFunctions** — official Android 16+ product baseline for discoverable, permission-controlled, type-safe local Agent tools; this is app-defined capability exposure, not runtime Agent code generation.
- **MCP-SandboxScan** — WASM/WASI runtime-isolation baseline for untrusted Agent tools; strong sandbox evidence but non-mobile.
- **SpecBox** — strong sandbox-lifecycle latency/memory baseline; high-concurrency server setting, not phone evidence.

SkillDroid FULL_10Q: **COMPLETE**.

Android AppFunctions deep vendor card: **COMPLETE**.

MCP-SandboxScan / SandScope FULL_10Q: **COMPLETE**.
SpecBox FULL_10Q: **COMPLETE**.

Round 14-B final T6 decision:
- product trend = **EMERGING_PRODUCT_TREND / BENCHMARK_AND_PREPARE** retained;
- standalone differentiated candidate = **KILL_DIFFERENTIATED_BET**;
- no T6-specific Direction;
- residual ownership = **C + B-residual/T5 + PT-A**;
- second differentiated Primary Bet = **UNFILLED**;
- uArch candidate = **none**.

Why:
- SandScope v2 shows real Agent-tool authority/provenance risk, but WASI is one optional containment backend; no phone CPU/JIT/code-cache residual is measured.
- SpecBox shows sandbox lifecycle can dominate latency/resource use, but its server-side value is recovered with software-visible prewarm/prefetch/cache/shared-memory orchestration.
- no reviewed target-phone source establishes a material dynamic-executable residual after AppFunctions + C + T5 + PT-A.

Round 14-C T8: **COMPLETE**.

T8 final:
- product trend = **EMERGING_PRODUCT_TREND / BENCHMARK_AND_PREPARE**;
- standalone differentiated candidate = **KILL_DIFFERENTIATED_BET**;
- no T8-specific Direction;
- ownership = **C + B-residual/T5 + PT-A**;
- second differentiated Primary Bet = **UNFILLED**;
- uArch candidate = **none**.

**Frontier Round 14 is COMPLETE.**

No second differentiated Primary Bet emerged from T6/T7/T8. This is an evidence result, not a quota problem.

Next program: **reserve-lane evidence rescue for B-residual / R1 / R2**, followed by the separate patent direct-claim audit before final portfolio convergence.

Do not create a new Direction until the frontier survives:
product relevance → smartphone/mobile evidence → ownership check → strongest baseline → residual test.

Reserve-lane paper rescue and patent direct-claim audit remain mandatory before final portfolio convergence.
