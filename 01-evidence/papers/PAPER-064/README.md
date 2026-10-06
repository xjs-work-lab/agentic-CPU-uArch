+++
id = "PAPER-064"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_PREPRINT"
title = "Sherlock: Reliable and Efficient Agentic Workflow Execution"
primary_url = "https://arxiv.org/abs/2511.00330"
priority = "P1"
evidence_role = "Agent-workflow verification, speculative downstream execution, rollback/discard and verification-budget baseline for PT-A/A"
venue = "arXiv preprint 2025"
+++

# PAPER-064 — Sherlock

## 30-second read
- **Why it matters:** Makes verification vulnerability, speculative downstream work and rollback/discard explicit scheduling decisions in Agent workflows.
- **What it establishes:** Counterfactual profiling can select vulnerable nodes and cost-appropriate verifiers; downstream nodes can execute speculatively while verification runs and be discarded/rolled back on failure.
- **Reported anchors:** +18.3% average accuracy vs non-verifying baseline; up to 48.7% verification-time reduction / substantial workflow-execution-time reductions depending benchmark; 26.0% verification-cost reduction vs the compared Monte-Carlo method.
- **Portfolio meaning:** further crowds cancel/discard/rollback as a standalone opportunity; strengthens PT-A/A software baseline.
- **Boundary:** preprint; server/A100/vLLM evaluation; no phone evidence.
- **Primary source:** https://arxiv.org/abs/2511.00330

See [deep.md](deep.md) for full Paper Insight 10Q.