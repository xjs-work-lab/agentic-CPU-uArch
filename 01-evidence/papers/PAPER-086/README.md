+++
id = "PAPER-086"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "FRESH_STRONGEST_BASELINE_WITH_PREPRINT_BOUNDARY"
independence_assessment = "FRESH_PREPRINT_MULTI_AGENT_SECURITY"
title = "Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks"
primary_url = "https://arxiv.org/abs/2610.05640"
priority = "P0"
evidence_role = "fresh strongest software baseline for provenance/capability preservation across hierarchical agent-as-tool boundaries"
authors = ["James Peters-Gill", "Avi Semler", "Henning Bartsch", "Ilia Shumailov", "Christian Schroeder de Witt"]
venue = "arXiv preprint 2026-10-05"
+++

# PAPER-086 — multi-CaMeL

## 30-second read
- **Why it matters:** Directly attacks the final plausible software residual in the security frontier: trust/provenance being lost when one Agent invokes another Agent as a tool.
- **Finding:** single-Agent CaMeL does not automatically compose; untrusted data can be laundered into a downstream Agent's trusted instruction channel.
- **Mechanism:** separate trusted natural-language instruction channel from untrusted data channel; preserve provenance/capabilities across Agent boundaries; enforce channel integrity at runtime.
- **Reported security:** MultiAgentDojo attack success rate 0.0% with multi-CaMeL vs 0.2% individual CaMeL vs 12.9% no CaMeL.
- **Utility:** incurs a cost, but the paper reports the gap shrinking with stronger models and becoming modest for the strongest evaluated models.
- **Portfolio meaning:** even dynamic hierarchical Agent trust/data-flow composition has a concrete software-level enforcement route; no hardware trust-graph Bet is justified.
- **Boundary:** very fresh preprint (2026-10-05), not peer reviewed as of this review; no mobile system measurement.
- **Primary source:** https://arxiv.org/abs/2610.05640

See [deep.md](deep.md) for full Paper Insight 10Q.