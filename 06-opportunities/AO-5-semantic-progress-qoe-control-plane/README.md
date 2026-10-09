+++
id = "AO-5"
type = "ARCHITECTURE_OPPORTUNITY"
record_state = "CURRENT"
title = "Semantic Progress / QoE Control Plane"
opportunity_stage = "DISCOVERY"
coverage_state = "EVIDENCE_MAPPED"
priority_rank = 4
research_question = "Which Agent-native semantic fields remain useful for control after history, SLO, dependency, runtime and utility baselines are fully considered?"
claim_links = [
  { claim_id = "CLM-AO5-001", role = "PROBLEM_SIGNAL" },
  { claim_id = "CLM-AO5-002", role = "PRODUCT_SIGNAL" },
  { claim_id = "CLM-AO5-003", role = "MECHANISM" },
  { claim_id = "CLM-AO5-004", role = "STRONG_BASELINE" },
  { claim_id = "CLM-AO5-005", role = "PRIOR_ART_BOUNDARY" },
  { claim_id = "CLM-AO5-006", role = "OPEN_GAP" },
  { claim_id = "CLM-AO5-007", role = "ARCH_HYPOTHESIS" }
]
related_trends = ["T1", "T3"]
related_directions = ["A", "C", "R1"]
related_capabilities = []
related_actors = []
+++

# AO-5 — Semantic Progress / QoE Control Plane

## Round 15A result
**KEEP / NARROW / EVIDENCE_MAPPED — CONDITIONAL-INFORMATION RESIDUAL ONLY.** Do not broaden back into generic 'Agent semantic scheduling'. This is distinct from creating a new DIRECTION or silicon mechanism.

### Seven role-backed Claims and source anchors

1. **Problem / CLM-AO5-001:** [Speculative Interaction Agents, PAPER-013](../../01-evidence/papers/PAPER-013/deep.md) distinguishes ready/executable/speculative from required/committable. [PARE, PAPER-015](../../01-evidence/papers/PAPER-015/deep.md) separates observe, accepted proposal and effectful execute. The runtime already observes much of this.
2. **Product / CLM-AO5-002:** [Huawei FFRT, VENDOR-005](../../01-evidence/vendors/VENDOR-005/README.md), [Kernel Enhance, VENDOR-006](../../01-evidence/vendors/VENDOR-006/README.md) provide generic task/QoS/resource control baseline. [MediaTek, VENDOR-019](../../01-evidence/vendors/VENDOR-019/deep.md), [Qualcomm, VENDOR-023](../../01-evidence/vendors/VENDOR-023/deep.md) show heterogeneous Agent AI positioning **without publicly proving a RequiredProgress hardware interface**.
3. **Mechanism / CLM-AO5-003:** [LAS, PAPER-119](../../01-evidence/papers/PAPER-119/deep.md) dynamically chooses exit, verification and repair using validator/artifact/history/DAG; [SMetric, PAPER-120](../../01-evidence/papers/PAPER-120/deep.md) infers session turn from existing request history to balance load and KV reuse. These are different problems and not one joint system.
4. **Strongest baseline / CLM-AO5-004:** B4-TX includes long personalized [ProAgentBench history, PAPER-044](../../01-evidence/papers/PAPER-044/deep.md), validation and quality routing (LAS), session-stage/KV routing (SMetric), [ready-release tail policy, PAPER-047](../../01-evidence/papers/PAPER-047/deep.md), [runtime-derived Effect/Commit, PAPER-050](../../01-evidence/papers/PAPER-050/deep.md), and TUF/utility/energy policy (PAPER-068).
5. **Prior art / CLM-AO5-005:** [ReUA, PAPER-068](../../01-evidence/papers/PAPER-068/deep.md) established utility-accrual and infeasible/low-value abort for mobile/embedded systems in 2004; current workflows already make quality-conditioned decisions. Novelty is not 'expose a utility curve', 'skip low-value work' or 'send scheduler a semantic stage'.
6. **Open gap / CLM-AO5-006:** Among two states matched on *all* B4-TX-observable history, DAG/control flow, validator, legality, user intent proxy, SLO/utility, environment and resource state, can actual Agent-authored **RequiredProgress / DemandState** still change which work should legally proceed and improve useful end outcomes?
7. **Architecture hypothesis / CLM-AO5-007 OPEN:** *If* incremental conditional information exists, try a minimal revocable and provenance-stamped Need/Value contract, captured first in framework/userspace; only explore OS CPU/NPU cross-layer control if software consumer demonstrates residual cost. Not an ISA/hardware proposal.

### Explicit negative tension
- **EC-AO5-006-B UNDERCUTS EC-AO5-006-A:** LAS, SMetric and personalized history illustrate powerful reconstructible alternatives. This pressure prevents mistaking workflow-state usefulness for hardware-interface necessity.
- **EC-AO5-006-C SCOPE_LIMIT:** Trajectory-level clarification timing (PAPER-048) and historical task utility models do not prove CPU-scale semantic release windows.
- **EC-AO5-007-A SCOPE_LIMIT:** Existing userspace/workflow and FFRT-style generic actuators must be exhausted before adding a new lower-layer contract.

### Matched-observability falsifier / next discovery test
Define B4-TX with the union of **history, request/session stage, validator/verification/commit, workflow topology, profile, critical path, quality-utility/SLO, queue/resource, cancellation, permission**. Compare it with one added hidden Agent-private goal/branch-necessity field at matched foreground QoE and zero illegal cancellation, accounting for labels/provenance, inference and communication overhead.

Reject a claimed AO-5 'incremental information' improvement if:
- it comes from omitting a B4-TX baseline feature;
- hidden labels leak oracle future outcome;
- the only benefit is a better software policy on the same observed features;
- it worsens user task success, foreground responsiveness or action legality.

### Round 15B literature closure and strengthened baseline
[PAPER-121 ProgRouter](../../01-evidence/papers/PAPER-121/deep.md) is now **FULL_10Q**, with original Sections 2–5, GPU-energy measurement Appendix D and progress/route ablations Appendix E reviewed. Its coordinator maintains a ledger of goals, steps and intermediate outputs; a structured path and a **semantic path derived from the coordinator's own state summary** predict next-model progress gain. On HumanEval+ (4800 J per-task-stream cap), full model 93.0% pass, structured-only 90.9%/4400J, semantic-only 87.2%/4784J; the 2.1 percentage-point difference is **not** a matched-energy causal proof of private state value.

The two new Evidence Cases **EC-AO5-004-C (SUPPORT)** and **EC-AO5-006-D (UNDERCUT)** bring ledger-derived progress and next-model progress-prediction into the strong B4-TX baseline. **AO-5 remains KEEP/NARROW**, no new hardware conclusion.

## Decision
AO-5 **KEEP / NARROW / EVIDENCE_MAPPED**. A remains **PRIMARY_BET / 82.5 / SIMULATION_SUPPORT** *as an existing provisional portfolio decision*, not as a newly validated claim. C is generic orchestration baseline; R1 remains conditional reserve. No new Direction, maturity/score adjustment, silicon/ISA/uArch commitment or proposed experiment execution.

**Next:** Round 15B AO-1…5 overlap, evidence bridge/contradiction audit, ProgRouter full-read debt, then 2027–2029 architecture opportunities and portfolio convergence.
