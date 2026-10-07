+++
id = "CLM-AGENT-001"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "Agent/runtime semantics"
supersedes = []
+++

# CLM-AGENT-001

## Proposition
Ready or executable Agent work is not necessarily required or authorized work.

## Current interpretation
- PAPER-013 shows safe speculative calls can execute before final user input, while calls may later be modified/cancelled and unsafe effects wait for commit.
- PAPER-015 shows Observe / Awaiting Confirmation / Execute are distinct proactive-assistant states and state-changing execution begins only after proposal acceptance.

Together they establish a semantic distinction between:
- work that can be issued;
- work that is currently needed;
- work that is authorized to publish effects.

## Boundary
Both sources keep these semantics inside the Agent/runtime.
Neither establishes:
- smartphone CPU/NPU system value;
- prevalence/cost of discardable work;
- incremental value of exporting DemandState below the runtime.

## Evidence-depth audit
EDP v1 revalidated 2026-10-07.
