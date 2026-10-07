+++
id = "PAPER-013"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "INDEPENDENT_GROUP"
title = "Speculative Interaction Agents: Building Real-Time Agents with Asynchronous I/O and Speculative Tool Calling"
primary_url = "https://arxiv.org/abs/2605.13360"
priority = "P1"
evidence_role = "speculative/cancellable Agent work semantics and runtime-derived commit baseline"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
authors = ["Coleman Hooper", "Minwoo Kang", "Suhong Moon", "Nicholas Lee", "Eric Wen", "John Wawrzynek", "Michael W. Mahoney", "Yakun Sophia Shao", "Amir Gholami", "Kurt Keutzer"]
venue = "arXiv preprint · 2026"
+++

# PAPER-013 — Speculative Interaction Agents

## 30-second read
- Runtime can start safe/read-only tool work before user input is complete, cancel invalidated calls, discard stale observations and hold unsafe effects until an explicit commit point.
- On HotpotQA/TinyAgent, SI-SFT small models report 1.6–2.2× latency speedups with small benchmark accuracy loss.
- Naturalistic Human Instructions is an important negative result: speculative streaming can become slower and less accurate because of repeated/degenerate actions.
- This supports ready≠required and cancel/discard/commit semantics, but also shows much of that state is already maintained by the Agent runtime itself.
- Primary source: https://arxiv.org/abs/2605.13360

See [deep.md](deep.md) for EDP v1 FULL_10Q.
