+++
id = "PATENT-019"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Task Scheduling Method and Electronic Device — WO2026056682A1"
primary_url = "https://patents.google.com/patent/WO2026056682A1/en"
priority = "P1"
evidence_role = "generic wake-sleeping-unit and heterogeneous task-migration prior art"
origin_paths = ["04-patents/M2-burst-continuation.md", "references/patents.md"]
origin_blobs = ["ed8686917f3dcd021ae4ad6773c49bfc551f9544"]
venue = "WO2026056682A1"
+++

# PATENT-019 — Task Scheduling Method and Electronic Device

Covers waking a sleeping execution unit and moving work under heterogeneous/load considerations.

**Boundary:** generic wake-and-migrate prior art; not proof that the narrow semantic residual is zero.


## 2026-10-07 direct-claim re-audit
**VERIFIED.**

Claim 1 directly covers:
- a thread running on a first execution unit;
- a different-performance second execution unit in sleep;
- a load-based migration condition;
- waking the second unit first;
- then scheduling/migrating the thread's task to the second unit.

Safe conclusion:
generic heterogeneous wake-before-migrate scheduling is direct claim-level prior art.

Boundary:
not Agent semantic ReleasePermission / LatestUsefulResume.

No FTO/legal conclusion is made.
