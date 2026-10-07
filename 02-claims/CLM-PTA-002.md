+++
id = "CLM-PTA-002"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "actuation outcome verification and recovery value"
supersedes = []
+++

# CLM-PTA-002

## Proposition
Explicit action-effect verification and bounded recovery have measurable reliability value in evaluated GUI/mobile Agent systems.

## Current interpretation
- ClawMobile and UIAnchor incorporate explicit execution checking/recovery in successful mobile systems.
- VeriGUI provides stronger causal software evidence: verification-aware training improves recovery metrics over ordinary action training.
- PhoneHarness reinforces the need for observable side-effect receipts and traceable task completion.

## Boundary
Verification/recovery is **necessary but not sufficient for safe actuation**.

PAPER-101 shows that the action can be rebound to a different foreground context before post-action verification occurs, and recovery logic itself can be weaponized. This claim must not be interpreted as proof of target/context integrity.

No differentiated Bet or lower-hardware mechanism follows from verification value alone.

## Evidence-depth audit
EDP v1 revalidated 2026-10-07.
