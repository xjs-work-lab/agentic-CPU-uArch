+++
id = "VENDOR-018"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Arm C2 CPU Cluster / SME2 Agentic CPU Path"
primary_url = "https://www.arm.com/products/silicon-ip-cpu/c2-cpu-cluster"
priority = "P0"
evidence_role = "official Arm product positioning for CPU+SME2 responsive Agentic/local-AI execution"
origin_paths = ["references/vendor-cards/arm/VENDOR-018.md"]
origin_blobs = ["c2bb206936f852e84c9abe310063bd45364de67b"]
publisher_actor_ids = ["ACT-ARM"]
+++

# VENDOR-018 — Arm C2 CPU Cluster / SME2 Agentic CPU Path

## 30-second read
- **Why it matters:** Arm explicitly productizes CPU matrix capability as part of a mobile Agentic/local-AI path.
- **What it establishes:** Arm's public product/positioning claim and capability surface.
- **Boundary:** Official vendor claim/positioning; independent engineering support is modeled separately and it does not establish a Huawei-equivalent capability.
- **Primary source:** https://www.arm.com/products/silicon-ip-cpu/c2-cpu-cluster

## Migration fidelity
- V1 baseline: `960abb4ef50a8f5b0bd357c067f08346025d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
