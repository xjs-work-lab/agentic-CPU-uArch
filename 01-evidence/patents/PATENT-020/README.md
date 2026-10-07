+++
id = "PATENT-020"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Swapping and Restoring Context-Specific Branch Predictor States on Context Switches — WO2021045811A1"
primary_url = "https://patents.google.com/patent/WO2021045811A1/en"
priority = "P0"
evidence_role = "generic branch-predictor state save/restore prior-art boundary"
origin_paths = ["04-patents/patent-10q/PATENT-020.md"]
origin_blobs = ["9fc9ae9606f9d80045cf9e04f9ac5f848f10b621"]
venue = "WO2021045811A1 / EP4025998B1"
+++

# PATENT-020 — Context-Specific Branch Predictor State Restore

Generic per-context branch-predictor save/restore is established prior art.

**Boundary:** 2026-10-07 direct claim re-audit verifies the restore primitive. The narrow residual is semantic selection/value, not the restore primitive itself; no legal/FTO conclusion.

Exact frozen V1 10Q is preserved in [deep.md](deep.md).


## 2026-10-07 direct-claim re-audit
**VERIFIED.**

Claim 1 directly covers a private branch-prediction memory containing state for a current context and, on a process/context switch, causing branch-prediction state associated with the new context to be loaded into that memory.

Safe conclusion:
generic context-specific branch-predictor state preservation/restoration is direct claim-level prior art.

No Agent semantics or phone-specific value is claimed.
