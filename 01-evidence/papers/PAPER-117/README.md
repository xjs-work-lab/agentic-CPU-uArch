+++
id = "PAPER-117"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-08"
decision_critical = true
decision_use = "AO2_SEMANTIC_TRANSACTION_RUNTIME_STRONG_BASELINE"
independence_assessment = "ACADEMIC_PREPRINT_RUNTIME_SECURITY_SYSTEM_NO_MOBILE"
title = "Cordon: Semantic Transactions for Tool-Using LLM Agents"
primary_url = "https://arxiv.org/abs/2606.17573"
priority = "P0"
evidence_role = "task-level semantic transaction, lineage, authority, effect staging and rollback baseline"
authors = ["Zheng Chen","Hanqing Liu","Duling Xu","Dong Dong","Jialin Li","Bangzheng Pu","Jidong Zhai"]
venue = "arXiv preprint · 2026-06-16"
+++

# PAPER-117 — Cordon

## 30-second read
- Full-text reviewed.
- Replaces isolated tool-RPC thinking with a task-level semantic transaction boundary.
- Binds tool intents and result lineage to reversible shadow state, staged external effects, delegated authority, recovery metadata and audit.
- Uses a transaction manager, shadow-state engine, effect outbox and recovery log.
- Prepare/validate/commit-or-abort occurs before irreversible effects are released.
- In the reported 45 risk-bearing workflows, Cordon catches all 45 before commit while the compared existing-defense strategy catches only 14 before commit.
- Strong software/runtime baseline for AO-2; hardware support is not required by the paper.

See deep.md.