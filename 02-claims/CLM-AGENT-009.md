+++
id = "CLM-AGENT-009"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "SOURCE_CLAIM"
status = "SUPPORTED"
scope = "hierarchical mobile GUI planning/execution cadence"
supersedes = []
+++

# CLM-AGENT-009

## Proposition
High-level semantic planning and low-level GUI action selection can operate at different cadences: one high-level VLM delegation can support multiple fresh-observation-grounded typed actions with lower execution-model time and cost than per-step VLM control in the evaluated AndroidWorld system.

## Current interpretation
PAPER-100 / Jev-Mobile further strengthens A/PT-A's software baseline: per-step expensive-model reasoning is not a credible strongest baseline when hierarchical delegation is available.

## Boundary
Jev is a remote service in the evaluated system; this source is software/control-architecture evidence, not on-device CPU/NPU evidence.
