+++
id = "PAPER-067"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "INDEPENDENT_PEER_REVIEWED_MOBILE"
title = "Smartphone Background Activities in the Wild: Origin, Energy Drain, and Optimization"
primary_url = "https://doi.org/10.1145/2789168.2790107"
priority = "P0"
evidence_role = "direct smartphone prior art for personalized background-task usefulness estimation and OS suppression under energy/user-experience tradeoff"
authors = ["Xiaomeng Chen", "Abhilash Jindal", "Ning Ding", "Y. Charlie Hu", "Maruti Gupta", "Rath Vannithamby"]
venue = "ACM MobiCom 2015"
+++

# PAPER-067 — HUSH

## 30-second read
- **Why it matters:** Directly demonstrates that a smartphone OS can estimate whether background activity is useful to a particular user and suppress low-value background work.
- **What it establishes:** Background→foreground correlation/history can be used as a personalized usefulness proxy; HUSH suppresses Android framework wakeups and trades energy saving against app staleness.
- **Reported anchors:** 2000 Galaxy S3/S4 trace; background screen-off apps/services contribute 28.9% of total daily energy on average; HUSH reports ~15.7% average total-energy saving in trace analysis with bounded staleness, plus small real-phone deployment evaluation.
- **Portfolio meaning:** Broad 'background-work usefulness/impact budget' is old mobile prior art. H-FIB only survives if Agent-internal dynamic marginal value is not reconstructible from user/app history or ordinary utility/QoS.
- **Boundary:** Screen-off/background app activity, not long-running Agent progress under simultaneous foreground CPU/NPU/memory contention.
- **Primary source:** https://doi.org/10.1145/2789168.2790107

See [deep.md](deep.md) for full Paper Insight 10Q.