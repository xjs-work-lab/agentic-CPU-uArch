+++
id = "PAPER-080"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "PEER_REVIEWED_AGENT_NATIVE_EDGE_SYSTEM"
title = "AgenTEE: Confidential LLM Agent Execution on Edge Devices"
primary_url = "https://doi.org/10.1145/3805621.3807660"
priority = "P0"
evidence_role = "Agent-native trust-domain composition seed: separately attested agent runtime, inference engine and third-party applications on Arm CCA"
authors = ["Sina Abdollahi", "Mohammad M Maheri", "Javad Forough", "Amir Al Sadi", "Josh Millar", "David Kotz", "Marios Kogias", "Hamed Haddadi"]
venue = "EuroMLSys 2026"
+++

# PAPER-080 — AgenTEE

## 30-second read
- **Why it matters:** Directly frames on-device Agent execution as a composition of mutually distrustful stakeholders/components rather than one trusted application.
- **Mechanism:** separate Arm CCA realms for Agent runtime, inference engine and third-party applications; remote attestation; CAEC confidential shared memory for inter-realm communication.
- **Reported result:** evaluated on OpenCCA/Radxa Rock 5B; end-to-end overhead is generally ~4–5.15% vs normal-world processes and ~1–2.85% vs ordinary VMs for the tested chatbot/itinerary agents.
- **Portfolio meaning:** opens a real security/isolation workload blind spot, but most substrate mechanisms come from generic CCA/CAEC rather than an Agent-specific CPU mechanism.
- **Boundary:** no commercial CCA smartphone, no NPU/GPU acceleration, simple agents, side channels/physical attacks out of scope.
- **Primary source:** https://arxiv.org/abs/2604.18231

See [deep.md](deep.md) for full Paper Insight 10Q.