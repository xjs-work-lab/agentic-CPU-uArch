+++
id = "VENDOR-017"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Arm CSS for Mobile 2"
primary_url = "https://www.arm.com/products/mobile/css-for-mobile-2"
priority = "P0"
evidence_role = "generic mobile coherent interconnect/system-level locality baseline"
origin_paths = ["references/vendor-cards/arm/VENDOR-017.md"]
origin_blobs = ["1b6ee16cdb403d8fd1824cb51579426dcda4f235"]
venue = "Arm official product architecture"
publisher_actor_ids = ["ACT-ARM"]
+++

# VENDOR-017 — Arm CSS for Mobile 2

Arm CSS for Mobile 2 publicly packages CPU/GPU/interconnect/software into an AI-native mobile subsystem. For R2, the relevant baseline is coherent SI L2 system interconnect plus QoS/system-level data movement.

**Boundary:** official vendor architecture/positioning. It is not an independent measurement that generic coherence removes the R2 residual, and it does not prove a Huawei gap.

Exact frozen V1 vendor card is preserved in [deep.md](deep.md).
