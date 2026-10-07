+++
id = "PATENT-028"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Compiler-Based Scheduling Optimization Hints for User-Level Threads — US20070124732A1 / US8205200B2"
primary_url = "https://patents.google.com/patent/US20070124732A1/en"
priority = "P0"
evidence_role = "direct-claim prior-art boundary for generic compiler-to-runtime scheduling/locality hints"
origin_paths = ["04-patents/patent-10q/PATENT-028.md"]
origin_blobs = ["88c051749c8d3b269cbfd0a9462e2577793082a6"]
venue = "US20070124732A1 / US8205200B2"
+++

# PATENT-028 — Compiler-Based Scheduling Optimization Hints

Direct claim review in frozen V1 establishes the broad `compiler → scheduling/locality hint → user-space runtime scheduler` pattern, including locality and nearby/shared-cache placement hints.

**Decision use:** broad compiler/runtime hint interfaces are not R3 differentiated novelty.

**Boundary:** does not directly claim Agent-native DemandState or Effect/Commit semantics; no legal/FTO conclusion.

Exact frozen V1 10Q is preserved in [deep.md](deep.md).


## 2026-10-07 direct-claim re-audit
**VERIFIED for project boundary use.**

Current public claim text directly supports the broad compiler-generated scheduling-hint → user-space runtime scheduler pattern.

The audit supports only the generic scheduling/locality-hint prior-art boundary. It does not establish Agent-native DemandState, Effect/Commit semantics, target-phone D1 value, or a D2 CPU/uArch mechanism.

No FTO/legal conclusion is made.
