+++
id = "PAPER-101"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_SECURITY_GROUP"
title = "Mind the Gap: Action Rebinding Attacks against Android GUI Agents"
primary_url = "https://arxiv.org/abs/2601.12349"
priority = "P0"
evidence_role = "negative evidence: observation-to-action TOCTOU and action-target rebinding"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Yi Qian", "Kunwei Qian", "Xingbang He", "Ligeng Chen", "Jikang Zhang", "Tiantai Zhang", "Haiyang Wei", "Linzhang Wang", "Hao Wu", "Bing Mao"]
venue = "ACM CCS 2026"
+++

# PAPER-101 — Mind the Gap: Action Rebinding Attacks against Android GUI Agents

## 30-second read
- CCS'26 negative evidence for PT-A: Android GUI Agents can act on a different foreground target than the one they observed.
- Six agents show 4.18–15.43 s observation→action windows; atomic rebinding reaches 100% in the reported attack evaluation.
- Agent recovery logic can be weaponized into multi-step attack loops; semantic confirmation can be bypassed with intent-aligned context.
- This means post-action verification/recovery is valuable but **not sufficient**: target/context integrity must hold at action delivery.
- Primary source: https://arxiv.org/abs/2601.12349

See [deep.md](deep.md) for EDP v1 FULL_10Q.
