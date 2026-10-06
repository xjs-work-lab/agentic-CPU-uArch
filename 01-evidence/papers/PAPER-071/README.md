+++
id = "PAPER-071"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "PEER_REVIEWED_AGENT_NATIVE"
title = "Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory"
primary_url = "https://arxiv.org/abs/2508.09736"
priority = "P0"
evidence_role = "Agent-native evidence that persistent episodic + semantic + multimodal memory is useful and continuously built/retrieved in long-horizon agents"
authors = ["Lin Long", "Yichen He", "Wentao Ye", "Yiyuan Pan", "Yuan Lin", "Hang Li", "Junbo Zhao", "Wei Li"]
venue = "ICLR 2026"
+++

# PAPER-071 — M3-Agent

## 30-second read
- **Why it matters:** Establishes persistent long-term memory as a first-class Agent capability rather than a speculative systems workload.
- **What it establishes:** Continuous visual/audio streams are transformed into episodic and semantic memories organized as an entity-centric multimodal graph; a control Agent iteratively retrieves that memory during reasoning.
- **Reported outcome:** meaningful accuracy gains over strong prompting baselines across M3-Bench and VideoMME-long; code/models/data are public.
- **Portfolio meaning:** Strong Agent-native workload signal for memory build/update/retrieval, but no smartphone systems performance evidence.
- **Boundary:** It proves memory helps Agent capability, not that a particular vector DB, CPU cache, NPU, or uArch feature is required.
- **Primary source:** https://arxiv.org/abs/2508.09736
- **Artifact:** https://github.com/ByteDance-Seed/m3-agent

See [deep.md](deep.md) for full Paper Insight 10Q.
