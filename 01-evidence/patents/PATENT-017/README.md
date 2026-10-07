+++
id = "PATENT-017"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Collaborative Workload Management Incorporating Work Unit Attributes in Resource Allocation — US6591262B1"
primary_url = "https://patents.google.com/patent/US6591262B1"
priority = "P1"
evidence_role = "workload-management claim baseline plus specification-level deadline/latest-start ancestry"
origin_paths = ["04-patents/M2-burst-continuation.md", "references/patents.md"]
origin_blobs = ["ed8686917f3dcd021ae4ad6773c49bfc551f9544"]
venue = "US6591262B1"
+++

# PATENT-017 — Collaborative Workload Management

**Direct-claim correction:** independent claims focus scheduler-provided work-unit resource attributes and workload-manager resource allocation/tuning. The patent specification/background discusses deadline, expected-duration and latest-start-like intervention behavior.

**Boundary:** generic workload/deadline scheduling; not Agent-specific post-ready phone timing.


## 2026-10-07 direct-claim re-audit
**CORRECTED / MIXED EVIDENCE ROLE.**

Independent claim 1 does **not** directly claim a latest-start computation.
It claims collaborative scheduler/workload-manager resource allocation using work-unit attributes.

The description/background explicitly discusses:
deadline, known duration, late-start detection and intervention around a latest-start concept.

Project use:
- specification/background ancestry for generic deadline/workload timing;
- not a direct-claim LatestUsefulResume anchor.

No FTO/legal conclusion is made.
