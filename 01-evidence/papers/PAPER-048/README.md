+++
id = "PAPER-048"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?"
primary_url = "https://arxiv.org/abs/2605.07937"
priority = "P1"
evidence_role = "semantic timing-window evidence with timescale-transfer boundary"
origin_paths = ["references/papers.md", "09-research-log/2026-10-05-stage15-r1-timing-kill-test.md"]
origin_blobs = ["4d6a94f6d6b2d99c55d168e55893b527b74da664"]
authors = ["Anmol Gulati", "Hariom Gupta", "Elias Lumer", "Sahil Sen", "Vamse Kumar Subbiah"]
venue = "arXiv preprint · 2026-05-08"
+++

# PAPER-048 — Clarification Timing Windows

- Supports time-dependent semantic value in long-horizon Agent execution.
- Frozen V1 anchors: goal clarification loses nearly all value after ~10% of execution; input clarification retains value to ~50%; >6,000 runs across 84 task variants.
- **Boundary:** trajectory/user-interaction scale, not CPU DependencyReady→LatestUsefulResume timing.
