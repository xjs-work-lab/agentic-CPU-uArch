+++
id = "PAPER-041"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Cordon: Semantic Transactions for Tool-Using LLM Agents"
primary_url = "https://arxiv.org/abs/2606.17573"
priority = "P0"
evidence_role = "runtime-derived effect/commit/rollback baseline"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
origin_paths = ["03-academic/paper-10q/PAPER-041.md"]
origin_blobs = ["91447aee130de6ac4f5eb45fd6b807803d4a207b"]
authors = ["Zheng Chen", "Hanqing Liu", "Duling Xu", "Dong Dong", "Jialin Li", "Bangzheng Pu", "Jidong Zhai"]
venue = "EuroSys 2027 / arXiv 2026"
+++

# PAPER-041 — Cordon: Semantic Transactions for Tool-Using LLM Agents

## 30-second read
- Cordon creates a task-scoped transaction boundary spanning runtime-tracked lineage, shadow state, pending external effects, delegated authority and recovery metadata.
- It can strongly **construct/enforce** commit and rollback legality when tools/effects remain mediated and observable.
- It does **not** infer universal semantic correctness: policy/authority/effect metadata and runtime mediation are prerequisites.
- 45/45 constructed risk workflows were intercepted before commit in the reported evaluation; opaque/bypassing effects remain a boundary.
- Primary source: https://arxiv.org/abs/2606.17573

See [deep.md](deep.md) for EDP v1 FULL_10Q.
