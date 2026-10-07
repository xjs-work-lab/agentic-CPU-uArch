+++
id = "PAPER-035"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "B_RESIDUAL_DEPENDENCY_VERSION_INVALIDATION_BASELINE"
independence_assessment = "PREPRINT_PROTOCOL_EVALUATION_NO_PHONE"
title = "Invalidation Contracts for Cross-Episode Agent Memory"
primary_url = "https://arxiv.org/abs/2609.00243"
priority = "P1"
evidence_role = "dependency/version invalidation baseline"
authors = ["Michael Wu", "Arquimedes Canedo"]
venue = "arXiv preprint · 2026"
+++

# PAPER-035 — Invalidation Contracts

## 30-second read
- Adds version stamps and cacheability hints to reusable recovery memories.
- Separates protocol validity from model compliance.
- Evaluates seven models, three serving paths, two domains and about 9,400 episodes.
- Row-level invalidation recovers 29–33% of baseline token cost on four of seven models.
- Version-stamp validity is deterministic by construction with zero contract failures in the reported evaluation.
- Contract payload overhead is 15%.
- Strong generic software/protocol baseline for dependency-scoped invalidation.
- Not phone S2/S3 evidence.

See [deep.md](deep.md).
