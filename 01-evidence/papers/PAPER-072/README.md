+++
id = "PAPER-072"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_PEER_REVIEWED"
title = "CD-ANN: Scalable Approximate Nearest Neighbor search on client-side devices"
primary_url = "https://doi.org/10.1016/j.sysarc.2026.103771"
priority = "P1"
evidence_role = "generic dynamic-client ANN baseline: segmented HNSW, on-demand segment caching, incremental insertion and bounded client memory"
authors = ["Chaoxia Qin", "Yixiong Tang", "Bing Guo", "Kan Zhong", "Duo Liu"]
venue = "Journal of Systems Architecture 2026"
+++

# PAPER-072 — CD-ANN

## 30-second read
- **Why it matters:** Directly challenges the idea that frequent insertion/update and limited client memory are unique to Agent memory.
- **What it establishes:** Segmented HNSW plus on-demand segment caching can reduce client memory and incremental insertion cost under dynamic vector growth.
- **Reported anchors:** the paper reports large client-memory reductions and roughly 70–97% lower incremental insertion latency across evaluated settings.
- **Portfolio meaning:** Dynamic ANN mutation itself is generic prior art; an Agent-memory Bet must require operation semantics or mobile heterogeneous behavior beyond a generic dynamic client index.
- **Boundary:** evaluated on an Apple M4 Pro workstation/client simulation rather than a smartphone SoC; blockchain integrity mechanism is not central to our CPU/uArch question.
- **Primary source:** https://doi.org/10.1016/j.sysarc.2026.103771

See [deep.md](deep.md) for full Paper Insight 10Q.
