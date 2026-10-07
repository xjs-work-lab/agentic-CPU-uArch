+++
id = "PAPER-085"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_AGENT_SOFTWARE_BASELINE"
independence_assessment = "PEER_REVIEWED_AGENT_SECURITY"
title = "Defeating Prompt Injections by Design"
primary_url = "https://arxiv.org/abs/2503.18813"
priority = "P0"
evidence_role = "strong Agent-software baseline for trusted control-flow extraction, untrusted data-flow separation, value provenance/capabilities and deterministic tool-call security policies"
authors = ["Edoardo Debenedetti", "Ilia Shumailov", "Tianqi Fan", "Jamie Hayes", "Nicholas Carlini", "Daniel Fabian", "Christoph Kern", "Chongyang Shi", "Andreas Terzis", "Florian Tramer"]
venue = "IEEE SaTML 2026"
+++

# PAPER-085 — CaMeL

## 30-second read
- **Why it matters:** Moves Agent security policy from heuristic prompt filtering into an explicit deterministic control/data-flow layer.
- **Mechanism:** privileged LLM generates trusted program/control flow; quarantined LLM processes untrusted data; interpreter tracks dependencies; capabilities/provenance constrain data flow into tool calls.
- **Current v2 result:** o3-high solves about 77.3% of AgentDojo utility tasks with CaMeL vs 84.5% native tool calling; updated paper reports very low/zero successful prompt-injection attacks for several models under its threat model.
- **Portfolio meaning:** fine-grained Agent data provenance, authorization and tool-flow policy are software-visible and enforceable; this sharply narrows any hardware trust-graph hypothesis.
- **Boundary:** tasks whose legitimate control flow itself depends on untrusted data remain difficult; side channels and model/tool semantics outside policy assumptions remain.
- **Primary source:** https://arxiv.org/abs/2503.18813
- **Artifact:** https://github.com/google-research/camel-prompt-injection

See [deep.md](deep.md) for full Paper Insight 10Q.