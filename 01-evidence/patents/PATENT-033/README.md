+++
id = "PATENT-033"
type = "SOURCE"
source_type = "patent"
record_state = "CURRENT"
independence_assessment = "PATENT_CLAIMS_DIRECTLY_REVIEWED"
title = "Fault fallback method, device, equipment and medium in multi-agent collaborative system — CN120704926A"
primary_url = "https://patents.google.com/patent/CN120704926A/en"
priority = "P0"
evidence_role = "multi-agent transaction prepare/commit/rollback/state-migration prior-art boundary"
venue = "CN120704926A"
+++

# PATENT-033 — Multi-Agent Transaction Fault Fallback

## 30-second read
- Direct claim review completed 2026-10-08.
- Claim 1 directly covers a master coordinator, multiple target Agents each executing an atomic operation, commit-stage fault monitoring, fault-agent localization, and partial or complete rollback.
- Claim 2 adds prepare requests, resource checks/locking, preconditions and resource-state snapshots.
- Claim 4 covers suspending transactions associated with a failed Agent, replacement, valid-state migration, recovery, or full rollback.
- Claim 5 covers packaging latest valid state plus unfinished transactions for migration and route update.
- Claim 6 covers rollback from resource-state snapshots plus consistency verification.
- High prior-art pressure on broad multi-Agent transaction/rollback/state-migration novelty.
- Does not claim LLM semantic lineage, resource frontiers, mobile xPU queue semantics or CPU/uArch support.

See deep.md.