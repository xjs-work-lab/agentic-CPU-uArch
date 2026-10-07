+++
id = "PAPER-078"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "PRIOR_ART_BASELINE"
independence_assessment = "PEER_REVIEWED_FOUNDATIONAL_MOBILE_SYSTEMS"
title = "SeeMon: Scalable and Energy-efficient Context Monitoring Framework for Sensor-rich Mobile Environments"
primary_url = "https://doi.org/10.1145/1378600.1378630"
priority = "P0"
evidence_role = "foundational mobile-systems prior art for translating high-level context requirements into shared incremental monitoring and dynamic essential-sensor selection under processing/energy constraints"
authors = ["Seungwoo Kang", "Jinwon Lee", "Hyukjae Jang", "Hyonik Lee", "Youngki Lee", "Souneil Park", "Taiwoo Park", "Junehwa Song"]
venue = "MobiSys 2008"
+++

# PAPER-078 — SeeMon

## 30-second read
- **Why it matters:** Strong prior art against treating semantic/energy-aware capture selection as a new Agent-memory mechanism.
- **Mechanism:** high-level Context Monitoring Queries are translated downward; shared/incremental evaluation exploits continuity; an Essential Sensor Set dynamically activates only sensors required by current context and queries.
- **Reported anchors:** 4.6× higher throughput at 2,100 samples/s and >60% transmission reduction at ~4,000 queries; >90% reduction for lower query counts in reported tests.
- **Key strategic point:** application semantics already controlled low-level sensing/resource activation in mobile systems long before Agent memory.
- **Portfolio meaning:** broad 'Agent-aware modality selection / adaptive capture' novelty is killed; only genuinely new Agent-specific information not reconstructible from application requirements could survive.
- **Primary source:** https://doi.org/10.1145/1378600.1378630

See [deep.md](deep.md) for full Paper Insight 10Q.