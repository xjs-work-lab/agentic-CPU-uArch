+++
id = "CAP-QUALCOMM-ORYON-FLEX-CACHE"
type = "CAPABILITY"
record_state = "CURRENT"
title = "Qualcomm Oryon Flex Cache"
maturity = "PUBLIC_PRODUCT_CAPABILITY"
evidence_confidence = "VENDOR_PUBLIC_ARCHITECTURE"
target_scope = "dynamically allocated shared cache pool across heterogeneous mobile CPU cores"
transfer_boundary = "Product architecture is public; Agent-specific performance value is vendor-positioned and not independently established."
evidence_claims = ["CLM-CG01-001", "CLM-CG01-002"]
[[actor_links]]
actor_id = "ACT-QUALCOMM"
role = "OWNER"
+++

# CAP-QUALCOMM-ORYON-FLEX-CACHE

## Capability
A productized flexible shared-cache pool accessible across heterogeneous mobile CPU cores.

## Why it matters
It raises the **generic hardware locality baseline** for both:
- CG-01 competitive-gap analysis;
- later R2 locality-residual analysis.

## Boundary
This Capability does not own:
- CG-01 BENCHMARK action;
- R2 reserve state;
- a claim of Agent-specific cache novelty.
