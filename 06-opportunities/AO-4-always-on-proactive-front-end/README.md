+++
id = "AO-4"
type = "ARCHITECTURE_OPPORTUNITY"
record_state = "CURRENT"
title = "Always-On Proactive Personal-Agent Front End"
opportunity_stage = "DISCOVERY"
coverage_state = "EVIDENCE_MAPPED"
priority_rank = 5
research_question = "What should remain continuously active when the interaction model shifts from prompt-response to observe-gate-intervene?"
claim_links = [
  { claim_id = "CLM-AO4-001", role = "PROBLEM_SIGNAL" },
  { claim_id = "CLM-AO4-002", role = "PRODUCT_SIGNAL" },
  { claim_id = "CLM-AO4-003", role = "MECHANISM" },
  { claim_id = "CLM-AO4-004", role = "STRONG_BASELINE" },
  { claim_id = "CLM-AO4-005", role = "PRIOR_ART_BOUNDARY" },
  { claim_id = "CLM-AO4-006", role = "OPEN_GAP" },
  { claim_id = "CLM-AO4-007", role = "ARCH_HYPOTHESIS" }
]
related_trends = ["T4"]
related_directions = ["CG-07", "C"]
related_capabilities = ["CAP-MEDIATEK-DEDICATED-AO-AI-DOMAIN"]
related_actors = ["ACT-MEDIATEK", "ACT-QUALCOMM"]
+++

# AO-4 — Always-On Proactive Personal-Agent Front End

## Round 15A judgment
**KEEP / EVIDENCE_MAPPED / PRODUCT-FOLLOW + SOFTWARE-PRESSURED CROSS-LAYER HYPOTHESIS.**

The surviving inquiry is not a 'new dual NPU', generic wake-word detector, or mandatory CPU-uArch block. It is a budgeted event→intent→reason escalation contract across trusted sensing, low-power ML, CPU/shared NPU and high-performance NPU, with explicit false-negative/privacy/foreground trade-offs.

### Seven evidence roles
- **Problem / CLM-AO4-001:** [ProactiveMobile, PAPER-087](../../01-evidence/papers/PAPER-087/deep.md) formalizes user/device/world/trajectory context and no-action vs executable assistance. CVPR 2026 benchmark, not 24/7 phone workload trace.
- **Product / CLM-AO4-002:** [MediaTek VENDOR-019](../../01-evidence/vendors/VENDOR-019/deep.md) dedicated Super Efficient NPU; [Qualcomm VENDOR-025](../../01-evidence/vendors/VENDOR-025/deep.md) sensing hub with Dual Micro NPUs. Different product domains; neither is independently measured as an Agent-specific system win.
- **Mechanism / CLM-AO4-003:** [PRPF PAPER-088](../../01-evidence/papers/PAPER-088/deep.md) MPP gate and function candidate compression; [AOSP CHRE VENDOR-024](../../01-evidence/vendors/VENDOR-024/deep.md) event-driven low-power nanoapps; [Apple VENDOR-026](../../01-evidence/vendors/VENDOR-026/deep.md) 2017 AOP two-pass trigger. These are complementary ingredients, **not** one measured production architecture.
- **Strong baseline / CLM-AO4-004:** CHRE-class context batching + PRPF-class pre-reasoning gate/candidate compression + CPU/shared-NPU wake/DVFS, before adding new efficient hardware. PRPF preprint reports −69.3% expected inference compute and −60.1% latency **on GPU benchmark**, not phone energy. Multimodal success 17.19% remains weak.
- **Prior art / CLM-AO4-005:** Apple 2017 two-pass AOP/AP wake and Android CHRE predate Agentic branding. The generic always-on-offload proposition is crowded. No AO-4 patent independent-claim review is asserted.
- **Open gap / CLM-AO4-006:** The residual is context-rate, wake granularity, rich intent-state transfer, permission-preserving observation, and false trigger/missed-assistance versus energy/foreground costs after the strong baseline. Its incremental hardware value is **not measured**.
- **Hypothesis / CLM-AO4-007 OPEN:** A selective event→intent→reason escalation fabric with bounded context/permission handoff and adaptive wake batching; software sufficiency remains a competing hypothesis.

### Explicit counterpressure
- **EC-AO4-006-B UNDERCUTS EC-AO4-006-A:** CHRE+PRPF may capture most value without new silicon; a dedicated third tier may increase idle and handoff cost.
- **EC-AO4-006-C SCOPE_LIMIT:** PRPF multimodal 17.19% SR and privacy/governance constraints prevent extrapolating compute reductions into better user QoE.
- **EC-AO4-007-A SCOPE_LIMIT:** old hardware wake hierarchy and new learned gating already exist, so architecture hypothesis is not proof of novelty or necessity.

### Architectural split to evaluate
1. **Observe:** low-power hub or event-source handlers collect consented minimal context; batch/deduplicate.
2. **Gate:** small model decides *when not to act*, with personalized thresholds, calibrated false-negative risk and top-K candidate intent/tool filtering.
3. **Escalate:** CPU/shared NPU or high NPU handles deeper contextual reasoning only if value exceeds wake/resume cost.
4. **Handoff / govern:** bounded context validity, provenance, permission, expiration, wake reason and foreground policy accompany each escalation.
5. **Outcome:** optimize useful correct intervention under battery, thermal, latency, privacy and foreground-QoE budgets, not tokens/sec alone.

### Strongest competing hypotheses
- H0: CHRE + PRPF-class software + shared NPU DVFS/batching already suffice for cost/UX, making extra hardware unnecessary.
- H1: dedicated efficient Agent ML domain improves *residual* persistent gate economics while protecting foreground QoE.
- H2: hardware placement matters less than accurate multimodal/permission-aware context reduction, personalization and state-transfer software.

### Public-evidence gaps / follow-up
- Real 24-hour context arrival and actionable-event distribution (audio/sensor/GUI/notification/calendar), no-action share and privacy restrictions.
- Normalized total energy: sensing + encoding + gating + context transfer + wake/residency + reasoning + false wake/retry.
- Compare CHRE-only/event filter, CPU tiny model, shared NPU DVFS, dual-NPU with matched model accuracy and uncertainty.
- False negatives, false triggers, per-user intervention quota and foreground QoE under same daily budget.
- Whether on-hub trusted nanoapp constraints can safely represent the multi-app Agent state needed for gating.

## Decision and ownership
AO-4: **KEEP / EVIDENCE_MAPPED** (follow competitive productization and preserve bounded cross-layer research). **CG-07 remains EXPLORE / 75.0; C owns generic orchestration.** No new DIRECTION, PRIMARY_BET, score, maturity promotion, Agent-specific hardware commitment or CPU-uArch candidate.

Next: **AO-5**, then cross-AO overlap and differentiated portfolio synthesis.
