+++
id = "VENDOR-006"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Huawei Kernel Enhance Kit / Gewu"
primary_url = "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/kernel-enhance-overview"
priority = "P1"
evidence_role = "existing Huawei generic QoS/resource/inference-control baseline"
origin_paths = ["references/vendor-cards/huawei/VENDOR-006.md"]
origin_blobs = ["951c5c16344cf1b5af93cdefd7467b618be4b841"]
venue = "Huawei developer documentation"
publisher_actor_ids = ["ACT-HUAWEI"]
+++

# VENDOR-006 — Huawei Kernel Enhance Kit / Gewu

## 30-second read
- **Why it matters:** Establishes that generic task/thread QoS, resource-management and on-device inference control surfaces already exist publicly in Huawei's stack.
- **What it establishes:** A public Huawei lower system-control baseline exists and generic missing-control-surface claims should be rejected.
- **Boundary:** Does not by itself establish Agent-native DemandState, effect/commit, ReleasePermission or Agent-specific locality/resource semantics.
- **Primary source:** https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/kernel-enhance-overview

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN`.
