+++
id = "PAPER-048"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "R1_SEMANTIC_TIMING_WINDOW_EVIDENCE_WITH_TIMESCALE_BOUNDARY"
independence_assessment = "PREPRINT_MULTI_MODEL_TRAJECTORY_STUDY_NO_PHONE_SYSTEM_TIMING"
title = "Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents?"
primary_url = "https://arxiv.org/abs/2605.07937"
priority = "P1"
evidence_role = "semantic timing-window evidence with timescale-transfer boundary"
authors = ["Anmol Gulati", "Hariom Gupta", "Elias Lumer", "Sahil Sen", "Vamse Kumar Subbiah"]
venue = "arXiv preprint · 2026-05-08"
+++

# PAPER-048 — Clarification Timing Windows

## 30-second read
- Forced-injection study of when missing information remains useful during long-horizon Agent execution.
- Four information dimensions, three benchmarks, four frontier models, 84 task variants and 6,000+ runs.
- Goal clarification loses nearly all value after ~10% of execution; input clarification retains value to ~50%.
- Clarification after mid-trajectory can be worse than never asking.
- Strong evidence that semantic information has real timing windows.
- Critical R1 boundary: these are trajectory/user-interaction windows, not CPU DependencyReady→LatestUsefulResume intervals.
- No phone system timing, energy or QoE measurement.

See [deep.md](deep.md).
