+++
id = "PAPER-069"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "PEER_REVIEWED_MOBILE_SYSTEMS_ADJACENT"
title = "MUSE: A Heterogeneity-Aware Multimedia Search Engine for Mobile SoCs"
primary_url = "https://arxiv.org/abs/2511.19192"
priority = "P0"
evidence_role = "direct commercial-smartphone evidence for dynamic high-dimensional retrieval, continuous ingestion/index maintenance, mobile memory-wall pressure and heterogeneous CPU/GPU/NPU mapping"
authors = ["Xinkui Zhao", "Qingyu Ma", "Yifan Zhang", "Hengxuan Lou", "Sai Liu", "Chang Liu", "Guanjie Cheng", "Naibo Wang", "Yueshen Xu"]
venue = "ACM Multimedia 2026"
+++

# PAPER-069 — MUSE

## 30-second read
- **Why it matters:** Directly measures the execution shape of continuously growing on-device semantic memory/search on commercial smartphone SoCs.
- **What it establishes:** High-dimensional vector retrieval plus ongoing insertion/index maintenance stresses mobile memory bandwidth, layout conversion and heterogeneous-processor coordination; naïve NPU offload can be worse than CPU execution.
- **Mechanism:** asynchronous DMA/HVX/HMX pipeline, zero-copy sharing, hardware-aligned IVF, and workload-aware CPU/GPU/NPU scheduling.
- **Reported anchors:** up to 1.4× higher query throughput at matched recall, up to 7× faster index construction, up to 6× insertion throughput under concurrent streaming, peak temperature capped at 38°C, and up to 4.6× lower total energy vs CPU-bound baselines.
- **Portfolio meaning:** Strong STRUCTURAL_SIGNAL for a new persistent-memory/retrieval workload on phones, but the mechanism is generic multimedia/vector retrieval rather than uniquely Agent-semantic.
- **Boundary:** Do not infer an Agent-memory Bet or CPU/uArch need from this paper alone.
- **Primary source:** https://arxiv.org/abs/2511.19192

## Provenance note
The same arXiv identifier began as v1 **AME: An Efficient Heterogeneous Agentic Memory Engine for Smartphones** (2025). The July 2026 v2 evolved into **MUSE** and is accepted at ACM Multimedia 2026.

Treat AME→MUSE as **one research lineage / one canonical Source**, not independent corroboration.

See [deep.md](deep.md) for full Paper Insight 10Q.
