# Research Authority Status

> **CURRENT AUTHORITY (Round15G, 2026-10-08):** [最新管理报告](../09-roadmap/management-final-public-evidence-2027-2029.md) · [正式组合](../09-roadmap/current.md) · [证据与入口审计](../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md). **A 当前是 CONDITIONAL_RESERVE，绝非 PRIMARY_BET；R1 是 WATCH；0 独立差异化 CPU-uArch Primary Bets。** 本文件后续大量 Rescue/EXP/Old Portfolio 段落均为按时间保留的历史记录，不能覆盖当前投资和零实验约束。


Updated: 2026-10-08

```yaml
migration_phase: CUTOVER_COMPLETE
research_authority: V2_2
graph_schema: 2.4
authority_repository: xjs-work-lab/agentic-CPU-uArch
historical_source_authority: V1_FROZEN
historical_source_repository: xiejinsen/agentic-CPU-uArch
historical_source_commit: 960abb4ef50f050da3c6784d30826053d42e5c5d
migration_id: MIG-20261006-02
human_gate: APPROVED
human_gate_date: 2026-10-06
cutover_state: COMPLETE
research_content_migrated: true
evidence_rescue: COMPLETE
evidence_depth_protocol: EDP_V1
frontier_round14: COMPLETE
portfolio_convergence: ROUND15E_PUBLIC_ONLY_FORMAL_CUTOVER
execution_plan_2027: HISTORICAL_NONOPERATIVE_EXPERIMENT_ARCHIVE
research_mode: PUBLIC_EVIDENCE_STRATEGIC_INSIGHT
study_execution_policy: PUBLIC_SOURCES_ONLY_NO_NEW_EXPERIMENTS
owned_experiment_environment: false
next_program: POST15H_LEADERSHIP_PACK_DELIVERED_USER_TRIGGERED_ONLY
round15a_progress: AO5_EVIDENCE_MAPPED_5_OF_5
product_trend_framework: V1
shared_semantic_contract: STRATEGIC_KG_CORE_V1
source_identity_gate: ACTIVE
round_end_reporting_contract: COMPILER_STYLE_GOAL_FQ7_COVERAGE_DRIFT_V1
management_final_report: 09-roadmap/management-final-public-evidence-2027-2029.md
source_claim_audit: analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md
leadership_decision_pack: 09-roadmap/leadership-decision-pack/README.md
```

## Authority
**V2.2 is the active Research SSOT.**

Repository: `xjs-work-lab/agentic-CPU-uArch`

## Current graph
- 632 canonical nodes
- 1202 canonical semantic edges
- 1202 generated reverse edges
- 1148 derived single-direction dependency edges
- V2.4 Opportunity-layer additive upgrade active
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
- current reserve lanes B-residual / R1 / R2: **0**
- whole current ROADMAP: **0**

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

Reserve Rescue R1 complete:
- PAPER-047 Tail-aware ready/release scheduling → FULL_10Q;
- PAPER-048 Clarification Timing Windows → FULL_10Q.

R1 paper-depth debt is now **0**.

R1 remains **CONDITIONAL_RESERVE / 55.5 / SIMULATION_SUPPORT**:
- generic Ready→Release decoupling is already demonstrated as useful software scheduling;
- semantic timing windows are real at long-horizon Agent/user-interaction scale;
- no target-phone evidence transfers those windows into a post-ready CPU/system control interval with >=5% incremental value.

No score/maturity/uArch change.

Reserve Rescue R2 complete:
- PAPER-008 Agentic AI architectural characterization / Agora → FULL_10Q;
- PAPER-049 Affinity Tailor → FULL_10Q.

R2 paper-depth debt is now **0**.

R2 remains **CONDITIONAL_RESERVE / 54.5 / SIMULATION_SUPPORT**:
- Agentic server execution clearly creates locality/context-switch pressure;
- role-aware pooling/pinning already captures substantial value on commodity servers;
- production soft-affinity scheduling further shows generic software can recover cache/branch/prefetcher locality at scale;
- no target-phone PMU evidence establishes >=5% Agent-specific residual after strong software + generic shared/coherent-cache baselines.

**Current-roadmap paper-depth debt is now 0.**

Patent direct-claim audit: **ACTIVE**.

R3 core audit complete:
- PATENT-028 — current public claim text verifies compiler scheduling hints consumed by a user-space runtime scheduler; locality-related dependent claims reinforce the generic hint baseline.
- PATENT-029 — current public claim text verifies a broad implicit-semantics / Agent-workflow / topology-analysis / node-resource-scheduling / RL path-optimization chain.
- PATENT-030 — current public claim text verifies a broad upper-planning-Agent → lower-execution-Agent → resource-scheduling hierarchy.

R3 result:
- CLM-R3-003 remains **SUPPORTED**, but only at the broad prior-art boundary;
- these patents do **not** establish that Agent-native DemandState/Effect-Commit semantics, a target-phone D1 residual, or a compact D2 CPU/uArch hint are already claimed or technically sufficient;
- R3 remains **BLOCKED / 48.5 / NOT_EVALUABLE** because its parent SYSTEM_VALUE/software-insufficiency gates remain unmet.

Patent audit inventory: **4 / 13 complete; 9 remain**.

B-residual patent audit complete:
- PATENT-032 current claim 1 directly verifies Agent dialogue/result/reasoning cache validity gated by identity, time window and service-version consistency, followed by semantic demand-satisfaction grading and reasoning reuse/correction.
- CLM-BR-004 remains **SUPPORTED**.
- Boundary confirmed: the claim does not extend to smartphone NPU/DRAM/UFS or other S2/S3 derived physical-artifact lineage/preservation.

B-residual remains **CONDITIONAL_RESERVE / 63.0 / SIMULATION_SUPPORT**; no score/maturity/uArch change.

R1 patent audit complete:
- PATENT-005 — claim 26 directly verifies completion-time prediction compared with known exit latency, followed by pre-completion wake command.
- PATENT-018 — claim 1 directly verifies dependency/time-constraint earliest/latest-start computation and task movable range.
- PATENT-019 — claim 1 directly verifies wake-before-migrate across heterogeneous running units.
- PATENT-017 — **corrected**: independent claims center on scheduler→workload-manager resource attributes/resource allocation. The deadline-duration/latest-start material is in the specification/background, not the independent-claim core.

CLM-R1-004 remains **SUPPORTED**, but the evidence model is now explicitly:
**3 direct-claim anchors + 1 specification/background ancestry source.**

R1 remains **CONDITIONAL_RESERVE / 55.5 / SIMULATION_SUPPORT**; no score/maturity/uArch change.

R2 patent audit complete:
- PATENT-020 — claim 1 directly covers per-context branch-predictor state selection/restoration on context switch.
- PATENT-021 — claims directly cover tracking cache access footprint and restoring TLB/SLB/I-cache/D-cache state on context return.
- PATENT-022 — claim 1 directly covers process-associated cache partitioning through a partition indicator.
- PATENT-023 — claim 1 directly covers cache-miss-ratio/MPKI-aware task migration between processor cores.
- PATENT-024 — claim 1 directly covers cache-demand + processor-workload-driven migration across heterogeneous processor clusters in a portable computing device; dependent claim 23 explicitly includes smartphone/tablet.

CLM-R2-004 and CLM-R2-005 remain **SUPPORTED** with direct claim-level provenance.

R2 remains **CONDITIONAL_RESERVE / 54.5 / SIMULATION_SUPPORT**; no score/maturity/uArch change.

Patent direct-claim audit: **13 / 13 COMPLETE**.
Current-roadmap paper-depth debt: **0**.
Evidence Rescue: **COMPLETE**.

Final portfolio convergence: **PROVISIONAL / REFRAME REQUIRED**.

Frozen management conclusion:
- differentiated Primary Bet: **A only**;
- second differentiated Primary Bet: **intentionally UNFILLED**;
- competitive/product investment: **CG-06 INVEST**;
- platform must-build tracks: **PT-A PLATFORM_TRACK + C STRATEGIC_ENABLER**;
- measured competitive options: **CG-07 EXPLORE + CG-01 BENCHMARK**;
- Strategic Reserves: **B-residual + R1 + R2**;
- hardware semantic-hint route: **R3 BLOCKED**;
- uArch Primary Bet: **none**.

No score, lane or maturity was changed merely to satisfy a portfolio quota.

Leadership view:
09-roadmap/final-2027-2029.md

Current research mode:
**public-evidence strategic insight only; no owned target-phone experiment environment is assumed.**

The previous 2027 discriminating experiment plan is retained as a **future validation reference**, not the current execution phase.

Next research phase:
**Round 15 — architecture opportunity discovery and cross-layer co-design reframing.**

The goal is to identify:
- structural Agentic workload changes;
- user-experience changes;
- unresolved cross-layer tensions;
- academic mechanisms ahead of productization;
- productized competitor mechanisms worth following;
- plausible compiler/runtime/OS/SoC/uArch co-design opportunities.

A hardware idea may enter **ARCHITECTURE_HYPOTHESIS** without target-phone experimental proof.
Actual silicon/product commitment still requires the stricter hardware gate.

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

Round 14-B T6: **COMPLETE / DECISION-COMPLETE**.

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

Reserve-lane evidence rescue and patent direct-claim audit: **COMPLETE**.

Historical note: the former 2027 experiment-execution plan is retained only as future validation reference after the 2026-10-08 research-premise realignment.

Do not create a new Direction until the frontier survives:
product relevance → smartphone/mobile evidence → ownership check → strongest baseline → residual test.

Those evidence-integrity gates are complete. Future portfolio changes must come from measured experiment results or materially new evidence, not from reopening already-closed broad novelty arguments.


## Research-premise realignment — 2026-10-08

The project is a **forward-looking public-evidence insight program**, not an internal device-validation program.

### Discovery gate
A candidate can be retained as an **ARCHITECTURE_HYPOTHESIS** when public evidence supports:
1. an Agentic-era structural workload/user-experience change;
2. a cross-layer control or data-movement tension;
3. a technically plausible software/hardware co-design lever;
4. a meaningful product or UX outcome;
5. a prior-art/productization boundary showing what is already solved vs still open.

This gate does **not** require owned phone measurements.

### Commitment gate
The existing strict gate remains valid only for future product/silicon commitment:
STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE.

Do not use the commitment gate to suppress early architecture opportunity discovery.


## Data-model V2.4 — Opportunity layer
Round 15 now uses a domain-specific canonical **ARCHITECTURE_OPPORTUNITY** synthesis object.

The shared strategic core remains:
SOURCE → EVIDENCE_CASE → CLAIM → TREND / DIRECTION → ROADMAP.

CPU/uArch adds:
CLAIM / TREND / CAPABILITY → ARCHITECTURE_OPPORTUNITY → DIRECTION.

AO-1..AO-5 are canonical DISCOVERY / SEED_MAPPED nodes.
They are not evidence and not portfolio commitments.

Graph projections:
- views/graph/current.json — bidirectional navigation projection;
- views/graph/dependency.json — single-direction inference/dependency projection for graph algorithms.

Round 15A must upgrade each AO from SEED_MAPPED to EVIDENCE_MAPPED using explicit claim roles and real SUPPORT / REBUT / UNDERCUT / SCOPE_LIMIT tension where decision-critical.


## Round 15A — AO-1 Evidence Closure
AO-1 Agent Execution Fabric: **EVIDENCE_MAPPED / KEEP / HIGH-PRIORITY CO-DESIGN OPPORTUNITY**.

New FULL_10Q anchors:
- PAPER-113 Agent.xpu;
- PAPER-114 MARS;
- PAPER-115 CPU-Centric Agentic AI.

New product-signal cards:
- VENDOR-001 Qualcomm Oryon Flex Cache;
- VENDOR-023 Qualcomm Hexagon Agentic NPU.

Canonical AO-1 evidence roles now include:
PROBLEM_SIGNAL / PRODUCT_SIGNAL / STRONG_BASELINE / PRIOR_ART_BOUNDARY / OPEN_GAP / ARCH_HYPOTHESIS.

AO-1 is explicitly narrowed away from:
- CPU-vs-NPU as the thesis;
- generic Agent-aware scheduling;
- premature new-ISA/new-cache claims.

Surviving opportunity:
cross-xPU execution/state/control fabric under mixed-criticality Agent flows.

Round 15A progress: **1 / 5 Opportunities evidence-mapped**.

Next: **AO-2 Revisable / Transactional Agent Execution**.

## Round 15A — AO-2 Evidence Closure
AO-2 Revisable / Transactional Agent Execution: **EVIDENCE_MAPPED / KEEP / HIGH-INTEREST ACADEMIC-LEAD OPPORTUNITY**.

New FULL_10Q anchors:
- PAPER-116 Speculative Actions;
- PAPER-117 Cordon;
- PAPER-118 Atomix.

New direct-claim patent anchor:
- PATENT-033 CN120704926A — multi-Agent prepare/commit/rollback/snapshot/state-migration claims reviewed directly.

Key narrowing:
- broad Agent transaction / commit / rollback is not whitespace;
- versioned authority, effect staging, progress-frontier settlement and compatible-state inheritance are already software/runtime mechanisms;
- current public mobile product signal for a distinct Agent-transaction hardware architecture is weak/not established.

Surviving opportunity:
only the lower execution/state residual remains credible — whether frequent speculative/revised local xPU work makes cancellation, invalidation, selective inheritance and reclamation expensive below runtime control.

Round 15A progress: **2 / 5 Opportunities evidence-mapped**.

Next: **AO-3 Persistent Agent State / Context Fabric**.


## Source Identity Gate — 2026-10-08
Source dedup governance is now **ACTIVE**.

Hard identity checks:
- DOI;
- arXiv work ID, version-insensitive;
- patent publication number;
- canonical primary URL.

Historical alias rule:
- PAPER-104 is canonical for LOCAL / arXiv 2608.15241;
- PAPER-033 is retained as ALIAS only;
- active evidence/experiment references were migrated to PAPER-104;
- aliases cannot be used as active evidence inputs.

QA now triggers on both pull requests and direct pushes to main.

Policy: 00-project/source-identity-policy.md
Validator: analysis/graph/source_identity.py


## Round 15A — AO-3 Evidence Closure
AO-3 Persistent Agent State / Context Fabric: **EVIDENCE_MAPPED / KEEP / PRODUCT-SIGNAL BACKED, SOFTWARE-PRESSURED CO-DESIGN OPPORTUNITY**.

- Reused prior FULL_10Q anchors PAPER-103 / 104 / 032 / 028 / 031 / 034 / 035 and previously direct-claim-audited PATENT-024 / 032; MobiMem primary HTML Sections 4–7 cross-checked.
- Reused canonical VENDOR-001 Qualcomm Oryon Flex Cache source and preserved VENDOR-022 supplemental review as an alias; carefully separated CPU-core Flex Cache from VENDOR-023's NPU-local shared memory.
- Connected CLM-AO3-001..007 through 12 evidence cases including explicit UNDERCUT and SCOPE_LIMIT against a hardware-necessity leap.
- Strong software baseline rules out broad cache/semantic invalidation novelty. Cross-engine derived-state lifetime/validity/residency remains a public-evidence architecture hypothesis, **not** a committed uArch feature.
- No differentiated Direction, score, portfolio lane or experiment requirement changed.

Round 15A progress: **3 / 5 Opportunities EVIDENCE_MAPPED**.
Next: **AO-4 Always-On Proactive Front-End** (then AO-5).


## Source identity correction — 2026-10-08
GitHub QA identified pre-existing duplicate-source identity groups and the newly added Qualcomm duplicate. Canonicalization preserved historical records as aliases:
- PAPER-097 → PAPER-113 (Agent.xpu)
- PAPER-073 → PAPER-103 (MobiMem)
- PAPER-041 → PAPER-117 (Cordon)
- PAPER-089 → PAPER-104 (LOCAL)
- PAPER-033 → PAPER-104 was already ALIAS
- VENDOR-022 → VENDOR-001 (Qualcomm Oryon Flex Cache)

Active Evidence Case premises and Experiment source inputs were migrated to canonical IDs. History and older reviews remain preserved, with no duplicate treated as independent evidence. **AO-3 result and portfolio are unchanged.**


## Source identity audit completion — 2026-10-08
Strong-identity duplicates are canonicalized and guarded by QA.

One cross-identifier soft duplicate identified by normalized-title review was also resolved:
- AgentProg: PAPER-030 is canonical and now records both arXiv 2512.10371 and DOI 10.1145/3745756.3809245;
- PAPER-056 is retained as a historical alias only;
- active EC-A-005-A and EXP-A-001 references now use PAPER-030.

Rule:
same work is one evidence source even when discovered through arXiv and publisher DOI separately.

## Round 15A — AO-4 Evidence Closure (2026-10-08)
AO-4 Always-On Proactive Personal-Agent Front End: **EVIDENCE_MAPPED / KEEP / SOFTWARE-PRESSURED CROSS-LAYER HYPOTHESIS**.

- Reused existing FULL_10Q PAPER-087 ProactiveMobile, PAPER-088 PRPF, VENDOR-019 MediaTek; cross-checked first-hand ProactiveMobile CVPR/arXiv and PRPF method, evaluation, ablations and limitations.
- Added distinct deep official Sources VENDOR-024 AOSP CHRE, VENDOR-025 Qualcomm Sensing Hub, VENDOR-026 Apple 2017 AOP two-pass detection after URL source-dedup preflight.
- Seven explicit claim roles CLM-AO4-001..007 and fifteen Evidence Cases contain genuine UNDERCUT and SCOPE_LIMIT pressure.
- **Key boundary:** CHRE/AP offload and two-stage wake are established prior art; PRPF-class gating substantially suppresses heavy reasoning in GPU benchmarks but is neither real-phone joules/day evidence nor enough to prove dedicated silicon.
- Retained context→intent→reason adaptive escalation and bounded permission/state handoff as **OPEN** cross-layer hypothesis, not a new CPU ISA or uArch candidate.
- CG-07 stays EXPLORE / 75.0; C generic orchestration; no new Direction, bet, score or hardware investment.
- Round 15A progress: **4 / 5 opportunities EVIDENCE_MAPPED**.
- Next: **AO-5 Semantic Progress / QoE Control Plane**, then AO1–AO5 cross-opportunity synthesis.

Deep audit: analysis/opportunities/AO-4-evidence-skeleton-2026-10-08.md
Transaction: history/research-transactions/TXN-20261008-ROUND15A-AO4-01.md

## Round 15A — AO-5 Evidence Closure (2026-10-08)

AO-5 Semantic Progress / QoE Control Plane: **EVIDENCE_MAPPED / KEEP-NARROW / conditional-information residual only**.

- Added PAPER-119 LAS ACL 2026 and PAPER-120 SMetric as FULL_10Q, including original methods, tables, experimental design, counterfactual/ablation checks and transfer boundaries.
- Added PAPER-121 ProgRouter as **METADATA_ONLY deepread debt**, not a source of decision-grade Evidence Cases; full text was not retrievable in this round.
- Reused prior deep-reviewed PAPER-013/015/043/044/047/048/050/068 and official platform/vendor baselines.
- CLM-AO5-001..007 now map seven roles; 15 evidence cases include an explicit UNDERCUT and multiple SCOPE_LIMITS against unearned differentiated/hardware claims.
- LAS and SMetric show that runtime-visible validation/artifact history/session signals can already give real *software/server* value; prior ReUA documents graded utility scheduling. None prove target-phone Agent-private RequiredProgress residual.
- AO-5 retains only the conditional information question **given complete B4-TX**. A stays PRIMARY_BET / 82.5 / SIMULATION_SUPPORT **as prior provisional state**, not newly verified. C/R1 and all portfolio lanes remain unchanged.
- **Round 15A: 5 / 5 ARCHITECTURE_OPPORTUNITY objects EVIDENCE_MAPPED.** This is evidence skeleton closure, **not** AO1…5 final cross-synthesis.
- **Next Round 15B:** full-read ProgRouter and any decision-critical late papers; AO1…5 overlap, inferential bridge, duplicates/contradictions; 2027–2029 co-design/product roadmap and portfolio convergence.

Canonical synthesis: analysis/opportunities/AO-5-evidence-skeleton-2026-10-08.md
Transaction: history/research-transactions/TXN-20261008-ROUND15A-AO5-01.md

## Round 15B — Cross-AO architecture opportunity synthesis (2026-10-08)

**PROVISIONAL SYNTHESIS / NO PORTFOLIO CHANGE.** PAPER-121 ProgRouter now FULL_10Q, original arXiv Sections 2–5, Appendix D/E reviewed; energy is GPU-board-based, software-ledger progress is already observable, no phone CPU-uArch promotion.

AO1+AO2+AO3 form an interdependent **execution/state lifecycle theme F** (do not conflate legal authorization with physical state validity). AO4 is **proactive always-on admission theme P**. AO5 is **Agent progress/QoE information-and-policy theme V** that feeds software decisions and only conditionally affects lower-level control. Three themes are NOT three investment bets.

Cross-AO graph reasoning: CLM-XAO-001..003 and EC-XAO-001-A/B, 002-A/B, 003-A/B. AO5 strongest baseline also receives EC-AO5-004-C and EC-AO5-006-D UNDERCUT.

No new Source ID, patent novelty conclusion, silicon feature, Differentiated Direction, Investment Lane or score change. The 2027–29 roadmap still requires refitting to these themes.

**Anti-drift round-end SSOT:** `00-project/final-questions-status.md` records final goal, FQ1..FQ7 progress and next gates and must be updated/reported every research round.

Next: **Round15C** public target-mobile cross-xPU mechanism pressure and 2027–29 layer/year roadmap.

## Hard research execution boundary — user reaffirmed 2026-10-08

The project must finish an evidence-based 2027–2029 Agentic mobile CPU/SoC strategic insight and roadmap using **public papers, patents, technical whitepapers, product/vendor documentation, and published third-party evaluations only**. **Do not execute or require any new device testing, lab experiments, PoC runs, local simulation or benchmark reproduction.** Published author experiments can be deeply audited and discussed with their original setup/limitations.

Gate A (public strategic opportunity judgment) is deliverable without direct measurement. Gate B hardware/product proof is outside scope. `EXP-*` are inherited historical contingency reference files, not project work to execute or complete. Missing public evidence calls for bounded, conditional conclusions, **not** postponement of the research goal or invented confirmation.

Canonical contract: `00-project/research-goal-lock-agentic-mobile.md`; end-of-round anti-drift tracker: `00-project/final-questions-status.md`.

## Round 15C — public Android17/QAIRT pressure and no-experiment roadmap (2026-10-08)

**Stage: PUBLIC_PLATFORM_BASELINE_AUDITED / 2027–29 ROADMAP PROVISIONAL**.

- New official source cards VENDOR-027 Android17 NPU Manager, VENDOR-028 AOSP NN HAL burst, VENDOR-029 Qualcomm QNN shared buffers (**SECTION_REVIEW**, manual full-page inaccessible), VENDOR-030 NNAPI NDK migration, VENDOR-031 Android AICore. Prior PAPER-009 original FULL_10Q reused; no duplicate source.
- Four Claims CLM-R15C-001..004 (004 OPEN) and eight Evidence Cases including UNDERCUT and SCOPE_LIMIT pressure established.
- AO1+AO2+AO3 software/OS base strengthens materially: NPU resource admission, model unload, preemption/cancel/status, memory resource lifetime and fast dispatch already documented; do not invent Agent NPU scheduler/zero-copy novelty.
- Public-only roadmap authority: `09-roadmap/round15c-public-source-roadmap-2027-2029.md`. Old `09-roadmap/final-2027-2029.md` marked historical, **no EXP instructions operative**.
- Three provisional themes F/P/V remain, four workload shifts shortlisted, existing investment lanes/scores unchanged, no hardware candidate promoted.
- End-state and FQ1..FQ7 updated in `00-project/final-questions-status.md`. **No experiments, hardware testing, PoC or simulation planned**.
- Next Round15D: patent/control claim pressure and public evidence leadership portfolio shortlist.

## Round15D — patent claims + vendor/OEM product convergence + leadership pre-decision (2026-10-08)

Research result: **PRE_DECISION_PORTFOLIO_MATRIX_READY**.
- Re-audited PATENT-024, PATENT-032, PATENT-033 original independent/dependent claims; no duplicate Source IDs and no FTO/legal conclusions.
- Added VENDOR-032 Apple Foundation Models sessions/tools, VENDOR-033 Google Pixel10 Tensor G5/Gemini Nano proactive assistance, VENDOR-034 Samsung Galaxy S26 Agentic AI announcement. OEM Samsung/Snapdragon evidence not counted twice as independent silicon.
- Research claims CLM-R15D-001..004 and Evidence Cases EC-R15D-001-A/B, 002-A/B, 003-A/B, 004-A/B include SUPPORT/UNDERCUT/SCOPE_LIMIT. No experimental results created.
- Technical prioritization from published evidence: PT-A verified action substrate + CG-06 CPU/LLVM fast paths + C software QoE/OS resources are strongest P0 actionable; A remains **conditional differentiated hypothesis** while canonical A PRIMARY_BET 82.5 stays a provisional legacy score/lane **not formally changed**; B/R1/R2 reserves, CG07 product-follow, R3 Blocked. 2nd primary Bet unfilled.
- Historical patents cover generic cache-demand task migration, Agent dialogue-demand/version cache and software Agent transaction recovery, **not** the conjectured physical CPU↔NPU Agent version coherence.
- Reports: `analysis/opportunities/round15d-prior-art-vendor-portfolio-2026-10-08.md` and `09-roadmap/round15d-leadership-portfolio-provisional-2027-2029.md`. Seven FQs refreshed.
- No tests, experiments, PoC, data instrumentation or simulation; strict public-source-only policy remains in force.

Next: Round15E formal reconciled portfolio SSOT and management-ready final answers without false confidence.

## Round-end reporting alignment (2026-10-08)
Adopted the compiler optimization insight project's fixed goal → final questions → cumulative progress/status → technology-area coverage → anti-drift check → next step format, retaining CPU-uArch's seven final questions and public-sources-only/no-experiment scope. Canonical template: `00-project/round-end-reporting-contract.md`. This change is reporting governance only, not an additional research round or portfolio decision.

## Round15E — canonical portfolio cutover (2026-10-08)

**Current:** evidence-limited, public-only formal investment decisions, `DEC-PORTFOLIO-002`.

- Exactly 3 priority engineering/platform directions CG-06 INVEST, PT-A PLATFORM_TRACK, C STRATEGIC_ENABLER. These are implementation and platform strategy, not 'new differentiated uArch Primary Bets'.
- **0 supported independent differentiated Primary Bets** currently; A **formally** downgraded to CONDITIONAL_RESERVE/HYPOTHESIS_OPEN via DEC-A-008; the historical 82.5 and SIMULATION_SUPPORT label archived, not used as present probability or new score.
- Exactly 3 **core** strategic research Reserves A/B-residual/R2. R1 downgraded to WATCH by DEC-R1-002, reflecting better priority for CPU architecture relevant R2 amid low directly published phone evidence. R3 BLOCKED; CG-07 and CG-01 unchanged.
- Evidence chain: `CLM-R15E-001` with its EVIDENCE_CASE SUPPORT/SCOPE_LIMIT anchors. Original source identities reused (PAPER-119/121/044, VENDOR-027/032, PATENT-032) — no duplicate.
- Current roadmap authority `09-roadmap/current.md` and `09-roadmap/round15e-integrated-public-roadmap-2027-2029.md`; older experiment plans remain historical and nonoperative.
- FQ1–7 and technical area cumulative coverage updated. No research experiments, tests, PoC or local simulation.
- Next Round15F leadership synthesis plus CPU/LLVM public-primary source pressure / final source links audit.

## Round15F — public CPU LLVM and optimized NPU source audit (2026-10-08)
Five original official LLVM/MLIR/Arm software Source IDs TOOL-014..018, existing TOOL-012 phone SME2 results **reused, not duplicated**. Four Claims and 8 EvidenceCases with scope limits and an explicit undercut; synthesis `analysis/engineering/round15f-cpu-llvm-compiler-pressure-2026-10-08.md`; latest leadership technical brief in `09-roadmap/round15f-leadership-technical-brief-2027-2029.md`.
CG-06 INVEST unchanged; strong NPU counterpressure checked in PAPER-009/059/057/098; no claim CPU universally beats NPU or Agent requires a new ISA. 0 new Primary Bets; three core reserves unchanged. No experiment/benchmark/PoC.
Next Round15G final public source/link/claim audit and management report closing.


## Round15G — final public-source strategic report delivered (2026-10-08)

- Latest leadership report: \`09-roadmap/management-final-public-evidence-2027-2029.md\`.
- Original source and SSOT entry audit: \`analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md\`: 22 decision/entrypoint markdown files, 84 local relative links, 0 broken targets; scoped public original URL access classification with JS/direct-fetch/section-indexed caveats.
- Root README stale historical A PRIMARY_BET 82.5 / graph 515 corrected; archived final roadmap points to latest report; present investment portfolio remains DEC-PORTFOLIO-002.
- **Formal portfolio unchanged:** CG-06/PT-A/C prioritized engineering/platform, zero independent differentiated Primary Bets, A/B-residual/R2 conditional reserves, R1 Watch, R3 Blocked, CG07 Explore, CG01 Follow.
- FQ1,2,3,5,6,7 closed for bounded public-source leadership decision; FQ4 software+compiler path answered but no publicly demonstrated new Agent-only CPU-uArch necessity. Final status is a decision with explicit uncertainty ceiling, not hardware innovation declaration.
- No new Source/Claim/EC nodes and no experiment, test, PoC, simulation, or automated monitoring. Future task only on user's new request.

## Round15H — technical leadership decision pack completed (2026-10-08)

Communication-only follow-up to completed Round15G research: no additional evidence objects, changed scores, altered lanes or hardware claims. [Decision pack](../09-roadmap/leadership-decision-pack/README.md) is the new stakeholder-facing short entry; [Round15G full report](../09-roadmap/management-final-public-evidence-2027-2029.md) and [DEC-PORTFOLIO-002](../08-decisions/events/DEC-PORTFOLIO-002.md) remain authoritative.

- Five-minute one-page executive summary, [CPU+LLVM / Runtime / OS ownership table](../09-roadmap/leadership-decision-pack/technical-matrix.md), [14 technically skeptical questions](../09-roadmap/leadership-decision-pack/technical-qa.md), [nine-slide academic presentation outline](../09-roadmap/leadership-decision-pack/slide-outline.md).
- Four document links audited: **58 relative links checked, 0 missing**, alongside normal graph/identity GitHub CI.
- Actual organization owner, funding, PM execution dates, permission to modify SoC IP and chip plans were **not** supplied, hence no made-up organizational commitments.
- No experimental work, phone testing, PoC, simulation or research Source additions.
- Formal directions **unchanged**: engineering CG-06 INVEST/PT-A PLATFORM_TRACK/C STRATEGIC_ENABLER, **0 differentiated Primary Bets**, core A/B-residual/R2 reserves, R1 WATCH/R3 BLOCKED, CG-07 EXPLORE/CG-01 BENCHMARK.
- Next work **only on explicit user request**: convert to a polished slide or document artifact if asked, or incorporate genuinely consequential fresh publicly published research.
