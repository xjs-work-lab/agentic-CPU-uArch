+++
id = "PAPER-047"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "R1_READY_RELEASE_DECOUPLING_STRONG_SOFTWARE_BASELINE"
independence_assessment = "PREPRINT_SERVER_WORKFLOW_NO_TARGET_PHONE"
title = "Decoupling Readiness from Release for Tail-Aware Scheduling of Agentic LLM Workflows"
primary_url = "https://arxiv.org/abs/2609.10964"
priority = "P0"
evidence_role = "direct Agent-workflow ready/release decoupling; strong R1 novelty constraint"
authors = ["Bochao Feng", "Jianjiang Li", "Haojie Wang", "Lin Qiao", "Yinghui Li", "Yukun Yan", "Jidong Zhai"]
venue = "arXiv preprint · 2026-09-10"
+++

# PAPER-047 — Decoupling Readiness from Release

## 30-second read
- Directly treats release of a ready Agent turn as a scheduling decision.
- Uses mean-CVaR tail risk, online turn-work estimates and queue pressure.
- Chooses both which ready turn to release and how much released-but-unfinished work to maintain.
- Real software-engineering Agent traces across multiple LLMs/arrival rates.
- Up to 3.50× P95 workflow-flow-time speedup under contention; comparable to eager release under light load.
- Strong R1 software baseline; broad Ready≠Release is not differentiated novelty.
- No phone energy/QoE or CPU post-ready timing evidence.

See [deep.md](deep.md).
