+++
id = "PAPER-084"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_AGENT_SOFTWARE_BASELINE"
independence_assessment = "PEER_REVIEWED_SECURITY_SYSTEM"
title = "IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems"
primary_url = "https://doi.org/10.14722/ndss.2025.241131"
priority = "P0"
evidence_role = "strong Agent-software baseline for third-party app isolation, hub-mediated collaboration and user-permissioned cross-app data flow"
authors = ["Yuhao Wu", "Franziska Roesner", "Tadayoshi Kohno", "Ning Zhang", "Umar Iqbal"]
venue = "NDSS 2025"
+++

# PAPER-084 — IsolateGPT

## 30-second read
- **Why it matters:** Directly addresses the Agent-specific problem of dynamically using mutually distrusting third-party apps/tools while preserving collaboration.
- **Mechanism:** trusted hub + isolated spokes; one app/context per spoke; structured inter-spoke collaboration only through the hub; user-permission model controls cross-app data sharing.
- **Security result:** evaluated attacks are substantially reduced, while the system preserves comparable task functionality in the tested workloads.
- **Performance boundary:** security overhead is under 30% for roughly three-quarters of tested queries; overhead grows with multi-app collaboration.
- **Portfolio meaning:** dynamic app/tool trust relationships and permissions are already expressible in Agent runtime/software; they do not by themselves require a new CPU trust-graph primitive.
- **Boundary:** prototype process isolation and LLM/app orchestration, not smartphone CCA hardware or mobile SoC evaluation.
- **Primary source:** https://doi.org/10.14722/ndss.2025.241131

See [deep.md](deep.md) for full Paper Insight 10Q.