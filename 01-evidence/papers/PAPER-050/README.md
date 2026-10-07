+++
id = "PAPER-050"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "TomasuLLM: Out-of-Order Speculative Execution for LLM Agents"
primary_url = "https://arxiv.org/abs/2609.38201"
priority = "P0"
evidence_role = "runtime-derived speculative dependency/effect validation strongest baseline"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Jiangnan Yu", "Ceyu Xu", "Mengming Li", "Shiyu Huang", "Yiran Xia", "Jian Weng", "Hui Xue", "Haohui Mai", "Zhiyao Xie", "Yuan Xie"]
venue = "arXiv preprint · 2026-09-22"
+++

# PAPER-050 — TomasuLLM

## 30-second read
- Strongest direct pressure on A's old Effect/Commit framing: runtime traces dependencies/effects in COW sandboxes and validates before in-order publication.
- 1.31× SWE-bench, 1.35× Terminal-Bench 2.0, 1.27× matched progress on SWE-Marathon; no false accepts in 4,010 audited validation records.
- But opaque/untraceable/irreversible effects become speculation barriers and run serially.
- Therefore substantial legality is runtime-derived **within a bounded observable wrapper scope**, not universally derivable.
- Primary source: https://arxiv.org/abs/2609.38201

See [deep.md](deep.md) for EDP v1 FULL_10Q.
