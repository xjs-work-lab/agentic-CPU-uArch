+++
id = "PATENT-018"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Task Allocation Method and Task Allocation Device — JP2007140710A"
primary_url = "https://patents.google.com/patent/JP2007140710A/en"
priority = "P1"
evidence_role = "DAG/time-constraint earliest/latest-start prior art"
origin_paths = ["04-patents/M2-burst-continuation.md", "references/patents.md"]
origin_blobs = ["ed8686917f3dcd021ae4ad6773c49bfc551f9544"]
venue = "JP2007140710A"
+++

# PATENT-018 — Task Allocation Method and Device

Derives earliest/latest start times from dependency/time constraints.

**Boundary:** frozen V1 assignee/family metadata remained incomplete; migration does not strengthen it.


## 2026-10-07 direct-claim re-audit
**VERIFIED.**

Claim 1 directly computes, for tasks under dependency/time constraints:
- earliest start time;
- latest start time that still satisfies the time constraint;
- movable/slack range from their difference;
- allocation order using that range.

Safe conclusion:
generic earliest/latest-start and slack-aware task allocation are direct claim-level prior art.

Boundary:
not Agent semantic post-ready timing.

No FTO/legal conclusion is made.
