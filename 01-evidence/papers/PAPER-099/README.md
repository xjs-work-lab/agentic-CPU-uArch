+++
id = "PAPER-099"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "MOBILE_GUI_SPECULATIVE_EXPLORATION_BASELINE"
independence_assessment = "PREPRINT_PHONE_INFERENCE_DUAL_DEVICE_BENCHMARK"
title = "MobileExplorer: Accelerating On-Device Inference for Mobile GUI Agents via Online Exploration"
primary_url = "https://arxiv.org/abs/2605.26546"
priority = "P1"
evidence_role = "mobile GUI Agent evidence for overlapping slow VLM reasoning with lightweight speculative UI exploration and rollback"
authors = ["Runxi Huang", "Liyu Zhang", "Shengzhong Liu", "Xiaomin Ouyang"]
venue = "arXiv preprint 2026"
+++

# PAPER-099 — MobileExplorer

## 30-second read
- **Structural signal:** on-device VLM reasoning can take tens of seconds while UI interactions take ~1–2 s, creating a large reasoning window.
- **Mechanism:** task-relevance-driven UI probing runs in parallel with VLM reasoning; a two-level rollback restores the original UI state; traces become compact hints.
- **Reported result:** roughly 23% reduction in steps/latency in headline settings, with up to 5% success improvement; Samsung Galaxy S24 is among evaluated inference devices.
- **Boundary:** main AndroidWorld evaluation uses emulator/device separation for stable measurement; not all interaction and inference are on one physical phone.
- **Project impact:** strengthens PT-A speculation/rollback workload; not a new Direction.

See [deep.md](deep.md) for full Paper Insight 10Q.
