+++
id = "PAPER-070"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_PEER_REVIEWED"
title = "LEANN: A Low-Storage Overhead Vector Index"
primary_url = "https://proceedings.mlsys.org/paper_files/paper/2026/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html"
priority = "P0"
evidence_role = "strong personal-device software/data-structure baseline for local semantic memory: recomputation and graph pruning trade compute for large vector-index storage reduction"
authors = ["Yichuan Wang", "Zhifei Li", "Shu Liu", "Yongji Wu", "Ziming Mao", "Yilong Zhao", "Xiao Yan", "Zhiying Xu", "Yang Zhou", "Ion Stoica", "Sewon Min", "Matei Zaharia", "Joseph E. Gonzalez"]
venue = "MLSys 2026 — Best Paper Award"
+++

# PAPER-070 — LEANN

## 30-second read
- **Why it matters:** Strong counterexample to assuming persistent personal/Agent memory requires large resident embedding/index storage.
- **What it establishes:** Recompute embeddings on demand and compress/prune the proximity graph instead of storing all embeddings.
- **Reported anchors:** index storage under ~5% of raw data, up to ~50× smaller than conventional indices while retaining strong retrieval quality and practical RAG latency.
- **Portfolio meaning:** Persistent-memory capacity/index pressure has a strong software/data-structure baseline; any Bet must survive compute-for-storage recomputation and compact ANN structures.
- **Boundary:** Personal-device/local RAG, but evaluated primarily on laptop/server-like hardware rather than smartphone SoCs; does not address high-frequency mobile ingestion/interference.
- **Primary source:** https://proceedings.mlsys.org/paper_files/paper/2026/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html
- **Artifact:** https://github.com/StarTrail-org/LEANN

See [deep.md](deep.md) for full Paper Insight 10Q.
