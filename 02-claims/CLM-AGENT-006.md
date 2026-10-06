+++
id = "CLM-AGENT-006"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "evaluated Agent action/workflow speculation and rollback systems"
supersedes = []
+++

# CLM-AGENT-006

## Proposition
Agent execution can use explicit effect/commit legality—such as idempotence, reversibility, sandboxability, verification state and dependency-derived rollback scope—to safely execute provisional work early, discard invalid work, or recover after failed verification in evaluated systems.

## Evidence
- PAPER-063 / Speculative Actions: semantic guards plus reversible/idempotent/sandboxed speculative effects and rollback/compensation.
- PAPER-064 / Sherlock: verifier-pending downstream speculation, dependency-aware discard/re-execution and bounded rollback.

## Current interpretation
Cancel/discard/commit legality is a genuine Agent-native control signal.
However, current evidence shows substantial value can already be captured by Agent/workflow runtime software.

## Boundary
PAPER-063 is peer-reviewed but not direct smartphone evidence.
PAPER-064 is preprint/server evidence.
This Claim does not establish:
- target-phone SYSTEM_VALUE;
- lower-layer CPU/NPU scheduling value beyond the Agent runtime;
- software insufficiency;
- hardware/uArch need.