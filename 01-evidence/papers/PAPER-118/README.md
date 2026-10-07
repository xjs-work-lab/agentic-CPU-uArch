+++
id = "PAPER-118"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-08"
decision_critical = true
decision_use = "AO2_PROGRESS_AWARE_TRANSACTION_AND_EFFECT_SETTLEMENT_BASELINE"
independence_assessment = "ACADEMIC_PREPRINT_RUNTIME_MULTI_BENCHMARK_NO_MOBILE"
title = "Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows"
primary_url = "https://arxiv.org/abs/2602.14849"
priority = "P0"
evidence_role = "progress-aware transaction, resource frontier and effect-settlement baseline"
authors = ["Bardia Mohammadi","Nearchos Potamitis","Lars Klein","Akhil Arora","Laurent Bindschaedler"]
venue = "arXiv preprint · v2 2026-05-29"
+++

# PAPER-118 — Atomix

## 30-second read
- Full-text reviewed.
- Separates tool execution from final effect settlement.
- Tags transactions with epochs, records read/effect scopes, seals the footprint, and allows commit only when per-resource progress frontiers show earlier conflicting work is exhausted.
- Distinguishes bufferable, reversible-eager and irreversible-gated effects; abort suppresses unreleased effects and compensates reversible externalized effects.
- Evaluated on tau-bench retail, WebArena, OSWorld, multi-Agent tau-bench and controlled stress tests.
- Reports zero leakage for correctly classified irreversible sends in its main 500-trial test and microsecond-scale wrapper overhead relative to typical tool latency.
- Strong software/runtime baseline; correctness depends heavily on accurate adapter metadata and frontier management.

See deep.md.