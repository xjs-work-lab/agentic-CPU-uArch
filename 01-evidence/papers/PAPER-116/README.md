+++
id = "PAPER-116"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-08"
decision_critical = true
decision_use = "AO2_SPECULATIVE_AGENT_ACTION_EXECUTION_AND_REVERSIBILITY"
independence_assessment = "ACADEMIC_PREPRINT_MULTI_ENVIRONMENT_NO_MOBILE_SOC"
title = "Speculative Actions: A Lossless Framework for Faster Agentic Systems"
primary_url = "https://arxiv.org/abs/2510.04371"
priority = "P0"
evidence_role = "direct speculative Agent action execution with commit/discard/rollback semantics"
authors = ["Naimeng Ye","Arnav Ahuja","Georgios Liargkovas","Yunan Lu","Kostis Kaffes","Tianyi Peng"]
venue = "arXiv preprint · 2025-10-05 / 2026 revision"
+++

# PAPER-116 — Speculative Actions

## 30-second read
- Full-text reviewed, not abstract-only.
- Predicts likely next Agent actions/API calls with a faster Speculator while the authoritative Actor is still running.
- Pre-launches predicted next actions and commits the matching branch; wrong branches are discarded or rolled back/compensated.
- Lossless mode requires speculative effects to be idempotent, reversible, sandboxed, or prevented from becoming externally visible before validation.
- Evaluated across chess, e-commerce, multi-hop web search and a lossy OS-tuning extension.
- Reports up to roughly 55% next-action prediction accuracy and about 20% end-to-end latency reduction; chess top-3 reports 54.7% prediction accuracy and 19.5% time saving over the stated runs.
- Strong evidence that speculative Agent work is a real systems abstraction, but the mechanism is software/runtime and does not establish hardware necessity.

See deep.md.