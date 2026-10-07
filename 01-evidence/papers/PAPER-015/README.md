+++
id = "PAPER-015"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "Proactive Agent Research Environment: Simulating Active Users to Evaluate Proactive Assistants"
primary_url = "https://arxiv.org/abs/2604.00842"
priority = "P0"
evidence_role = "proactive demand / proposal / authorization semantic ground truth"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Deepak Nathani", "Cheng Zhang", "Chang Huan", "Jiaming Shan", "Yinfei Yang", "Alkesh Patel", "Zhe Gan", "William Yang Wang", "Michael Saxon", "Xin Eric Wang"]
venue = "arXiv preprint · 2026"
+++

# PAPER-015 — PARE

## 30-second read
- PARE explicitly separates Observe → Awaiting Confirmation → Execute in a 143-scenario stateful simulated phone environment.
- Observe has read-only actions; effectful execution starts only after the simulated user accepts a proposal.
- Frontier models still show premature proposals and limited end-to-end success, making intervention timing a real semantic problem.
- Critical boundary: PARE does **not** execute effectful speculative work before authorization and is not real-phone timing/energy evidence.
- Primary source: https://arxiv.org/abs/2604.00842

See [deep.md](deep.md) for EDP v1 FULL_10Q.
