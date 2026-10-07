+++
id = "CLM-AGENT-003"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "INFERENCE"
status = "SUPPORTED"
scope = "runtime-derived safety baseline"
supersedes = []
+++

# CLM-AGENT-003

## Proposition
A strong transactional Agent runtime can construct and enforce substantial Effect/Commit legality **when the relevant tool/effect path is mediated and observable and required policy/authority metadata are available**.

## Current interpretation
Cordon and TomasuLLM provide concrete runtime mechanisms for transaction/effect isolation, validation and commit safety. They are alternative supporting routes, not jointly required proof.

Cordon specifically demonstrates task-level lineage, shadow state, staged external effects and authority-aware validation; it does not create universal semantic legality from runtime state alone.

## Boundary
Opaque/bypassing tools, unobservable side effects and already-released external effects can fall outside complete containment. This claim must not be used to assume all legality is reconstructible in every Agent or smartphone system.

## Migration
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`

## Evidence-depth audit
EDP v1 revalidated 2026-10-07; unconditional derivability wording removed, decision unchanged.
