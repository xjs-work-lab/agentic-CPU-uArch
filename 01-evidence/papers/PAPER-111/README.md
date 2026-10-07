+++
id = "PAPER-111"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T8_EXPLICIT_AGENT_STATE_MIGRATION_BOUNDARY"
independence_assessment = "INDEPENDENT_MULTI_INSTITUTION_RESEARCH"
title = "Adaptive AI Agent Placement and Migration in Edge Intelligence Systems"
primary_url = "https://arxiv.org/abs/2508.03345"
priority = "P0"
evidence_role = "explicit Agent memory/config state migration across distributed edge servers"
authors = ["Xingdan Wang", "Jiayi He", "Zhiqing Tang", "Jianxiong Guo", "Jiong Lou", "Liping Qian", "Tian Wang", "Weijia Jia"]
venue = "arXiv preprint, 2025"
+++

# PAPER-111 — Adaptive AI Agent Placement and Migration

## 30-second read
- Adaptive placement/migration for stateful LLM Agents in edge systems.
- Lightweight migration transfers essential Agent state.
- AgentScope implementation exports/imports Agent memory.
- Target initializes and loads state, source is released, execution resumes.
- Evaluation uses distributed edge servers, not phones.
- Proves stateful Agent migration is real but not phone CPU execution-state migration.

See [deep.md](deep.md).
