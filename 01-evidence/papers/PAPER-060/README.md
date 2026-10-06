+++
id = "PAPER-060"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
decision_use = "DECISION_GRADE_WITH_SCOPE_BOUNDARY"
independence_assessment = "VENDOR_AFFILIATED_PEER_REVIEWED"
title = "Surviving the Impossible Trinity: Revisiting CPU Scheduling Problem on Modern COTS Mobile Devices"
primary_url = "https://www.usenix.org/conference/osdi26/presentation/xiao"
priority = "P0"
evidence_role = "direct commercial-mobile semantic-aware CPU scheduling baseline; interaction semantics to kernel control via VIP class, dependency propagation and user-space policy"
authors = ["Jun Xiao", "Qinhui Gu", "Ligeng Chen", "Lizhi Sun", "Zicheng Wang", "Yinggang Guo", "Lu Liu", "Hao Wu", "Borui Li"]
venue = "USENIX OSDI 2026"
+++

# PAPER-060 — MUSched

## 30-second read
- **Why it matters:** Directly attacks a mobile semantic gap: the kernel scheduler cannot tell interaction-critical work from background work.
- **What it establishes:** Interaction semantics can be translated into a small scheduling contract—VIP tags/classes plus dependency propagation—and consumed by a COTS Android CPU scheduler with measurable QoE benefit.
- **Reported anchors:** 14.8% lower average cold-start time in 10-app laboratory tests; source-reported deployment on >20M Honor devices since 2024 with 30.7% fewer startup anomalies, 25.0% fewer animation anomalies and 35.7% fewer swipe anomalies.
- **Portfolio meaning:** Strong generic semantic-scheduling baseline for A/C and direct prior-art pressure on H-SCL. Broad semantic-to-low-level CPU scheduling is not white space.
- **Negative boundary:** Highly optimized game workloads show little benefit and can slightly worsen current/temperature; scenario semantics must be discriminating, not merely available.
- **Primary source:** https://www.usenix.org/conference/osdi26/presentation/xiao

See [deep.md](deep.md) for the full Paper Insight 10Q.
