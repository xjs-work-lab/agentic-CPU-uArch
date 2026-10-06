+++
id = "PAPER-066"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "PEER_REVIEWED_CLOUD_SYSTEM"
title = "Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms"
primary_url = "https://www.usenix.org/conference/osdi26/presentation/chaudhry"
priority = "P0"
evidence_role = "strong Agent-aware cross-layer workflow/SLO/model/hardware/resource orchestration baseline for H-FIB/C"
authors = ["Gohar Irfan Chaudhry", "Esha Choukse", "Haoran Qiu", "Íñigo Goiri", "Rodrigo Fonseca", "Adam Belay", "Ricardo Bianchini"]
venue = "USENIX OSDI 2026"
+++

# PAPER-066 — Murakkab

## 30-second read
- **Why it matters:** Strongest reviewed proof that Agent workflow structure and per-request SLOs can already drive end-to-end model/hardware/resource orchestration.
- **What it establishes:** A declarative Agent-workflow graph plus offline profiles and an adaptive runtime can jointly choose workflow knobs, models/tools, GPU types/parallelism, instance counts, routing and multiplexing under quality/latency/cost/resource constraints.
- **Reported anchors:** up to 2.8× lower GPU usage, 3.7× lower energy and 4.3× lower cost than the evaluated LangGraph baselines while maintaining SLOs.
- **Portfolio meaning:** Broad 'Agent-aware resource budget/orchestration' is not H-FIB white space. H-FIB would need an Agent-internal marginal-value/tolerance variable not expressible as ordinary quality/latency/cost SLO or workflow configuration.
- **Boundary:** Cloud GPU/multi-tenant serving, not smartphone foreground/background QoE; SLOs are request/workflow objectives rather than RequiredProgress-like in-task marginal value.
- **Primary source:** https://www.usenix.org/conference/osdi26/presentation/chaudhry

See [deep.md](deep.md) for full Paper Insight 10Q.