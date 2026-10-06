+++
id = "VENDOR-019"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "MediaTek Dimensity 9600 Pro / Dedicated Always-On Agent AI Domain"
primary_url = "https://www.mediatek.com/products/smartphones/mediatek-dimensity-9600-pro"
priority = "P0"
evidence_role = "COMPETITIVE_GAP / DIRECT_PRODUCT"
origin_paths = ["references/vendor-cards/mediatek/VENDOR-019.md"]
origin_blobs = ["974fbcc45d8116eee135d13629832dffa214b160"]
publisher_actor_ids = ["ACT-MEDIATEK"]
+++

# VENDOR-019 — MediaTek Dimensity 9600 Pro

## 30-second read
MediaTek publicly discloses:
- dual-NPU architecture;
- NPU 1090;
- Super Efficient NPU 2.0;
- Agentic AI Engine;
- scheduling/fusion integration;
- a dedicated always-on low-power domain for background AI/Agent work.

## Vendor quantitative claim
MediaTek reports **40% lower always-on AI power vs predecessor** for Super Efficient NPU 2.0.

This remains a **VENDOR_CLAIM**.

It is not an independently measured CG-07 model parameter.

## Why it matters
It creates a concrete competitor architecture for the same user problem as persistent/background Agent execution:
useful progress without visible battery, thermal or foreground-QoE cost.

## Boundary
- product architecture disclosure: strong public vendor evidence;
- exact power/performance percentages: vendor-reported;
- independent retail-phone always-on Agent power/wake validation: not established;
- Huawei equivalent smartphone dual-domain implementation: not publicly established in the reviewed V1 set.

## Migration fidelity
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
- exact V1 vendor card preserved in [deep.md](deep.md).
