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
origin_paths = ["03-academic/paper-10q/PAPER-041.md"]
origin_blobs = ["91447aee130de6ac4f5eb45fd6b807803d4a207b"]
authors = ["Zheng Chen", "Hanqing Liu", "Duling Xu", "Dong Dong", "Jialin Li", "Bangzheng Pu", "Jidong Zhai"]
venue = "arXiv preprint · 2026"
+++

# PAPER-041 — Cordon: Semantic Transactions for Tool-Using LLM Agents

## 30-second read
- **Why it matters:** Demonstrates a concrete transactional runtime that constructs and enforces substantial effect/commit legality.
- **What it establishes:** A strong runtime can derive meaningful commit/rollback legality from transaction state, lineage, shadow state and staged effects.
- **Boundary:** Agent runtime evidence; smartphone-specific residual remains unproven.
- **Primary source:** https://arxiv.org/abs/2606.17573

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
