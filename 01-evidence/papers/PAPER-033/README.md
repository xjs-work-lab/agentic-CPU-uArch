+++
id = "PAPER-033"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q_REUSED_FROM_PAPER_104"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_VERSION_AWARE_KV_VALIDITY_BASELINE_DUPLICATE_PRIMARY_SOURCE"
independence_assessment = "SAME_PRIMARY_SOURCE_AS_PAPER_104"
title = "LOCAL: Enabling Learning On-device Contiguously for Agent LLMs"
primary_url = "https://arxiv.org/abs/2608.15241"
priority = "P0"
evidence_role = "version-aware Agent KV validity baseline"
authors = ["Xinxin Liu", "Jiaxin Li", "Zibo Wang", "Yun Ji", "Zhangqi Zhu", "Qing Hu", "Zhibin Wang", "Rong Gu", "Sheng Zhong", "Chen Tian"]
venue = "arXiv preprint · 2026"
+++

# PAPER-033 — LOCAL

## Review status
PAPER-033 and PAPER-104 resolve to the same primary paper:
https://arxiv.org/abs/2608.15241

The decision-grade FULL_10Q review was completed under PAPER-104 on 2026-10-07.

This historical source ID is retained for migration/evidence-graph fidelity and reuses that review rather than pretending to be an independent second paper.

## B-residual impact
LOCAL shows adapter/version-aware KV validity and staged refresh can be represented in software runtime state.

Boundary:
- 24 GB single-GPU evaluation;
- no target-phone SYSTEM_VALUE;
- no standalone B-residual promotion.
