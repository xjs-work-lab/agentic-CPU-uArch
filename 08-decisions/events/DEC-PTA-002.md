+++
id = "DEC-PTA-002"
type = "DECISION_EVENT"
subject_kind = "DIRECTION"
subject_id = "PT-A"
event_type = "EFFECT_COMMIT_LEGALITY_BASELINE_STRENGTHEN_NO_LANE_CHANGE"
effective_date = "2026-10-06"
transaction_id = "TXN-20261006-FRONTIER-ROUND3-01"
trigger_claims = ["CLM-AGENT-006"]
trigger_experiments = []
+++

# DEC-PTA-002 — PT-A contract strengthened by Agent speculative-effect legality

## Change
PT-A remains:
- PLATFORM_TRACK;
- score context 80.0;
- SYSTEM_VALUE.

No Primary-Bet promotion.

The common actuation contract is strengthened to expose where applicable:
- effect class;
- idempotent / reversible / sandboxed status;
- provisional vs committed state;
- verification guard;
- rollback / compensation capability and scope;
- dependency lineage for invalidating downstream speculative work.

## Why
PAPER-063 shows peer-reviewed Agent-native value from semantic commit guards and reversible/idempotent/sandboxed speculative effects.
PAPER-064 independently supports verification-pending speculative downstream execution and rollback/discard, but remains preprint/server evidence.

These papers strengthen PT-A's platform relevance while also showing that substantial legality/rollback value is already capturable in software.

## Boundary
No direct smartphone lower-layer resource-control residual or CPU/uArch need is established.