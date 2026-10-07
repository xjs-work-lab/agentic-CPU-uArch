+++
id = "CG-07"
type = "DIRECTION"
record_state = "CURRENT"
title = "Dedicated Always-On Agent AI Domain"
direction_class = "COMPETITIVE_GAP"
competitive_action = "EXPLORE"
score_context = 75.0
evidence_maturity = "PRODUCT_SIGNAL_PLUS_AGENT_WORKLOAD_PLUS_SOFTWARE_BASELINE_PLUS_SYNTHETIC_MODEL"
maturity_scope = "MediaTek product architecture is public; ProactiveMobile provides peer-reviewed proactive-mobile workload evidence; PRPF raises the software/model strongest baseline; independent retail-phone SYSTEM_VALUE and dedicated-domain residual economics are not established."
related_claims = ["CLM-CG07-001", "CLM-CG07-002", "CLM-CG07-003", "CLM-CG07-004", "CLM-CG07-005", "CLM-CG07-006", "CLM-CG07-007", "CLM-CG07-EXP-001"]
related_capabilities = ["CAP-MEDIATEK-DEDICATED-AO-AI-DOMAIN"]
+++

# CG-07 — Dedicated Always-On Agent AI Domain

## 30-second decision
**EXPLORE / 75.0 / stronger workload premise, narrower architecture residual**

MediaTek provides a concrete public competitor architecture: high-performance NPU + dedicated low-power always-on AI domain.

PAPER-087 ProactiveMobile supplies a direct proactive-smartphone workload premise: ongoing mobile context must first be judged for **intervene vs remain silent** before executable assistance is generated.

PAPER-088 PRPF raises the strongest software/model baseline: lightweight pre-reasoning gating and candidate-function compression can suppress much heavy reasoning before any dedicated hardware is considered.

Therefore workload relevance is stronger, architecture necessity is harder to prove, and no score change is justified.

## Strong baseline
CG-07 must beat:
- PRPF-class lightweight intervention gating + candidate-function compression;
- shared NPU with strong DVFS/power gating;
- CPU / small-model front-end path;
- batching / effective-wake reduction;
- A semantic-progress control;
- existing background scheduling.

The architecture question is no longer “is the Agent workload always-on?” It is:

> After lightweight gating sparsifies the context stream, does a dedicated low-power front end still beat the strongest shared/CPU front end on the residual gate + handoff + wake/residency economics?

## Current evidence
- product architecture: public MediaTek vendor evidence;
- 40% lower always-on AI power: vendor claim only;
- proactive smartphone workload: PAPER-087 / CVPR 2026 / peer reviewed;
- lightweight pre-reasoning software baseline: PAPER-088 / 2026 preprint;
- PAPER-088 reports large benchmark/GPU compute and latency reduction, but not phone battery/rail/thermal measurements;
- synthetic break-even model: upgraded to post-gating residual economics;
- independent retail-phone wake/idle/duty-cycle/battery data: absent in the current reviewed set.

## Promotion gate
On representative proactive/persistent Agent smartphone workloads, a dedicated domain must beat the strongest software-sparsified shared/CPU baseline using measured:
- raw context-observation rate;
- intervention/acceptance rate after gating;
- gate energy and latency;
- heavy-domain handoff/wake energy and latency;
- idle/residency power;
- active power;
- battery / thermal / foreground QoE.

## Boundary
- no dual-NPU hardware program from vendor marketing;
- no SYSTEM_VALUE from synthetic parameters;
- no architecture promotion from “always-on” workload existence alone;
- no uArch/SoC commitment before measured residual economics.
