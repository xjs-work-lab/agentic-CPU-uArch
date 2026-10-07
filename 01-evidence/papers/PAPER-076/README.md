+++
id = "PAPER-076"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DIRECT_TARGET_SIGNAL_WITH_DEMO_BOUNDARY"
independence_assessment = "PEER_REVIEWED_MOBISYS_DEMO"
title = "Demo: Modality-Aware Long-Term Memory Acquisition for On-Device Mobile Personal Agents"
primary_url = "https://doi.org/10.1145/3812835.3814986"
priority = "P0"
evidence_role = "direct smartphone long-term-memory acquisition signal: modality availability, capture latency, storage overhead and energy across screenshot, A11y, interaction-event and device-state capture"
authors = ["Liyu Zhang", "Xiaomin Ouyang"]
venue = "MobiSys Companion 2026"
+++

# PAPER-076 — Modality-Aware Long-Term Memory Acquisition

## 30-second read
- **Why it matters:** Directly measures the upstream data-acquisition side of persistent mobile-Agent memory rather than assuming memory-ready data already exists.
- **What it establishes:** screenshot, accessibility-tree, interaction-event and device-state capture have different availability, latency, storage, energy and semantic-completeness trade-offs across real mobile apps.
- **Workload:** four acquisition modalities across 15 representative real-world apps with synchronized mobile telemetry.
- **Key qualitative result:** screenshots are broadly stable but costly; A11y trees are cheaper but structurally brittle; events/device state are lightweight but semantically incomplete.
- **Portfolio meaning:** validates acquisition as a real mobile cost layer, but does not establish a differentiated Agent-specific scheduler/control abstraction.
- **Boundary:** 2-page peer-reviewed demo; exact modality-level numeric tables were not available in the accessible text reviewed here.
- **Primary source:** https://doi.org/10.1145/3812835.3814986

See [deep.md](deep.md) for full Paper Insight 10Q.