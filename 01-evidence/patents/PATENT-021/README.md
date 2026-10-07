+++
id = "PATENT-021"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Mechanism to Save and Restore Cache and Translation Trace for Fast Context Switch — US7634642B2"
primary_url = "https://patents.google.com/patent/US7634642B2/en"
priority = "P0"
evidence_role = "generic cache/TLB/translation warm-state restoration prior-art boundary"
origin_paths = ["04-patents/patent-10q/PATENT-021.md"]
origin_blobs = ["db030a828cf16af5d3ce6dc89afe990080ef5448"]
venue = "US7634642B2"
+++

# PATENT-021 — Cache / Translation Trace Restore

Generic cache/TLB/translation-footprint save/restore for fast context return is established prior art.

**Boundary:** 2026-10-07 direct claim re-audit verifies cache/TLB/translation footprint restore; no legal/FTO conclusion.

Exact frozen V1 10Q is preserved in [deep.md](deep.md).


## 2026-10-07 direct-claim re-audit
**VERIFIED.**

Claim 1 tracks/saves cache-access footprint before switch-out.
Claims 8 and 11–13 directly cover loading saved information and restoring execution footprint including TLB, SLB, instruction-cache and data-cache state.

Safe conclusion:
generic context warm-state save/restore is direct claim-level prior art.
