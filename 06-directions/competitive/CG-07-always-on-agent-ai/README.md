+++
id = "CG-07"
type = "DIRECTION"
record_state = "CURRENT"
title = "Dedicated Always-On Agent AI Domain"
direction_class = "COMPETITIVE_GAP"
competitive_action = "EXPLORE"
score_context = 75.0
evidence_maturity = "PRODUCT_SIGNAL_PLUS_SYNTHETIC_MODEL"
maturity_scope = "MediaTek product architecture is public; exact power benefit is vendor-reported; synthetic economics are ready; independent retail-phone SYSTEM_VALUE is not established."
related_claims = ["CLM-CG07-001", "CLM-CG07-002", "CLM-CG07-003", "CLM-CG07-004", "CLM-CG07-005", "CLM-CG07-EXP-001"]
related_capabilities = ["CAP-MEDIATEK-DEDICATED-AO-AI-DOMAIN"]
+++

# CG-07 — Dedicated Always-On Agent AI Domain

## 30-second decision
**EXPLORE / 75.0 / Architecture benchmark + co-design study**

MediaTek provides a concrete public competitor architecture:
high-performance NPU + dedicated low-power always-on AI domain.

That is a strong **product signal**, not yet independent proof of battery/system value.

## Strong baseline
CG-07 must beat:
- shared NPU with strong DVFS/power gating;
- batching/effective-wake reduction;
- CPU/small-model path;
- A semantic-progress control;
- existing background scheduling.

## Current evidence
- product architecture: public vendor evidence;
- 40% lower always-on AI power: vendor claim only;
- synthetic break-even model: complete;
- independent 9600 Pro wake/idle/duty-cycle/battery data: absent in reviewed V1 set;
- equivalent Huawei smartphone dual-domain architecture: not publicly established in reviewed V1 set.

## Promotion gate
Real representative persistent-Agent workloads must show clear useful-progress / energy / thermal / foreground-QoE value over the strong shared-domain baseline.

## Boundary
- no dual-NPU hardware program from vendor marketing;
- no SYSTEM_VALUE from synthetic parameters;
- no Huawei internal-absence claim;
- no uArch/SoC commitment before measured economics.
