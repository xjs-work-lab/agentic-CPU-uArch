+++
id = "VENDOR-022"
type = "SOURCE"
source_type = "vendor"
record_state = "ALIAS"
canonical_source_id = "VENDOR-001"
independence_assessment = "VENDOR_SELF_REPORT"
title = "Qualcomm Oryon Flex Cache — shared cache for heterogeneous mobile CPU cores"
primary_url = "https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache"
priority = "P0"
evidence_role = "official product architecture signal for CPU-core state residency and workload handoff; AO-1/AO-3, not cross-xPU coherent fabric proof"
publisher_actor_ids = ["ACT-QUALCOMM"]
venue = "Qualcomm OnQ official blog · 2026-08-25"
+++


> **Source identity note (2026-10-08):** Historical ID VENDOR-022 is an ALIAS of VENDOR-001 for the same original publication. Keep the archived review for provenance, but use the canonical source in active evidence. The two IDs are not independent confirmations.

# VENDOR-022 — Qualcomm Oryon Flex Cache

- Official source: https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache
- **Disclosed capability:** heterogeneous Oryon CPU cores share a dynamically allocated cache pool; Qualcomm explicitly calls out multi-step Agent tasks migrating between CPU cores.
- **Important boundary:** this is a shared cache *within the CPU subsystem*, not a documented coherent CPU–GPU–NPU Agent state fabric.
- **Evidence class:** vendor product signal (not independent measured uplift).
- See [deep.md](deep.md).
