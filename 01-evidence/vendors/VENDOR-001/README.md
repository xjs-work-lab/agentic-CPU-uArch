+++
id = "VENDOR-001"
type = "SOURCE"
source_type = "vendor"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Qualcomm Oryon CPU / Flex Cache"
primary_url = "https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache"
priority = "P0"
evidence_role = "COMPETITIVE_GAP / BOUNDARY_BASELINE"
origin_paths = ["references/vendor-cards/qualcomm/VENDOR-001.md"]
origin_blobs = ["0ea4ddcf922f554b946632446c9a6cde3ce03b50"]
publisher_actor_ids = ["ACT-QUALCOMM"]
+++

# VENDOR-001 — Qualcomm Oryon / Flex Cache

## 30-second read
Qualcomm publicly discloses a next-generation mobile Oryon CPU with **Flex Cache**:
heterogeneous CPU cores access a dynamically allocated shared cache pool.

Qualcomm explicitly positions the mechanism around:
- large working sets;
- cross-core handoff;
- multi-step / Agentic execution;
- avoiding cold private-cache restart after handoff.

## Evidence classification
- Flex Cache product architecture: **PUBLIC_CAPABILITY**
- working-set/locality benefit: **VENDOR_CLAIM / mechanism rationale**
- Agentic multi-step handoff relevance: **POSITIONING**

No independent Flex-Cache Agent benchmark is contained in this source.

## Project boundary
This Source supports CG-01 as a competitor-gap/adaptation benchmark.

It does not prove:
- global shared-cache novelty;
- >=5% Agent-specific value;
- Huawei internal absence;
- need for an Agent-specific cache/uArch mechanism.

## Migration fidelity
Frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`

Exact V1 vendor card is preserved in [deep.md](deep.md).
