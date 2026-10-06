+++
id = "CAP-MEDIATEK-DEDICATED-AO-AI-DOMAIN"
type = "CAPABILITY"
record_state = "CURRENT"
title = "MediaTek dedicated always-on low-power AI domain"
maturity = "PUBLIC_PRODUCT_CAPABILITY"
evidence_confidence = "VENDOR_PUBLIC_ARCHITECTURE"
target_scope = "Dimensity 9600 Pro dual-NPU / background always-on Agent AI execution domain"
transfer_boundary = "Architecture is publicly disclosed; exact energy value remains vendor-reported and independent retail-phone validation is absent."
evidence_claims = ["CLM-CG07-001"]
[[actor_links]]
actor_id = "ACT-MEDIATEK"
role = "OWNER"
+++

# CAP-MEDIATEK-DEDICATED-AO-AI-DOMAIN

## Capability
A dedicated low-power NPU domain is publicly productized alongside a high-performance NPU for background/always-on AI/Agent activity.

## Evidence
`CLM-CG07-001`

## Boundary
This object does not encode:
- the vendor 40% power claim as independent truth;
- Huawei absence;
- CG-07 EXPLORE/INVEST state.
