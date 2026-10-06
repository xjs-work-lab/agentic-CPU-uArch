+++
id = "PAPER-063"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_ACADEMIC"
title = "Speculative Actions: A Lossless Framework for Faster AI Agents"
primary_url = "https://openreview.net/forum?id=P0GOk5wslg"
priority = "P0"
evidence_role = "Agent-native speculation with semantic commit guards, reversible/idempotent/sandboxed side-effect envelopes, rollback/repair; PT-A and A strongest baseline"
authors = ["Naimeng Ye", "Arnav Ahuja", "Georgios Liargkovas", "Yunan Lu", "Kostis Kaffes", "Tianyi Peng"]
venue = "ICLR 2026"
+++

# PAPER-063 — Speculative Actions

## 30-second read
- **Why it matters:** Directly makes action legality, commit safety and rollback semantics operational in Agent execution.
- **What it establishes:** Agents can speculate likely future actions in parallel, but correctness depends on semantic guards plus safety envelopes that restrict externally visible speculative effects to idempotent, reversible or sandboxed operations, with rollback/compensation on mismatch.
- **Reported anchors:** up to ~55% next-action prediction accuracy and ~20% end-to-end latency reduction across evaluated agentic environments; chess with 3 predictions reports 54.7% prediction accuracy and 19.5% average time saving.
- **Portfolio meaning:** cancel/discard/commit legality is Agent-native and valuable, but strong upper-layer Agent runtimes can already exploit it. It strengthens PT-A/A baseline rather than opening a new lower-layer Bet.
- **Boundary:** Mostly non-mobile environments; OS-tuning extension is lossy/server-side. No smartphone CPU/uArch necessity.
- **Primary source:** https://openreview.net/forum?id=P0GOk5wslg
- **Artifact:** https://github.com/naimengye/speculative-action

See [deep.md](deep.md) for full Paper Insight 10Q.