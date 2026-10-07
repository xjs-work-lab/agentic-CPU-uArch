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
A strong transactional Agent runtime can construct and enforce substantial Effect/Commit legality when the relevant tool/effect path is mediated and observable and required policy/authority metadata are available.

## Current interpretation
Cordon and TomasuLLM provide independent mechanisms:
- transaction/lineage/shadow-state mediation;
- COW speculative execution;
- dependency tracing;
- observation/effect validation;
- in-order commit.

PAPER-013 further shows a simpler runtime can explicitly classify safe/unsafe tools and hold state-changing effects until commit.

## Boundary
TomasuLLM makes the limit concrete: calls whose dependencies/effects cannot be conservatively traced, or whose effects are irreversible, become speculation barriers.

Opaque/bypassing tools, already-released external effects and unobservable side effects therefore remain outside universal runtime derivability.

This Claim must not be used to imply all legality is reconstructible in every smartphone system.

## Evidence-depth audit
EDP v1 revalidated 2026-10-07.
