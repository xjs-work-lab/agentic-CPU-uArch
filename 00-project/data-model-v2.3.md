# Agentic CPU-uArch Data Model 2.3

Date: 2026-10-07
Scope: graph/data-model evolution only. Research authority remains V2.2.

## Why
The project now distinguishes:
1. **Product Evolution** — what future 2027–2029 smartphone CPU/SoC/system products should gain.
2. **Differentiation** — where original or target-specific research whitespace remains.

The previous `ROADMAP → DIRECTION` model conflated these questions.

## Additive upgrade
Add canonical object type **TREND**.

Do not rename/move:
- existing Sources;
- Claims;
- Evidence Cases;
- Capabilities;
- Directions;
- Experiments;
- historical Decision Events.

## Dual decision chain

```text
SOURCE → EVIDENCE_CASE → CLAIM → TREND → PRODUCT_EVOLUTION ROADMAP
                              ↘ DIRECTION → DIFFERENTIATION_PORTFOLIO ROADMAP
```

TREND↔DIRECTION is an ownership/classification relation, not an evidence relation.

## TREND required fields
- trend_maturity: ESTABLISHED_PRODUCT_TREND / EMERGING_PRODUCT_TREND / FRONTIER_SIGNAL / UNSUPPORTED
- product_posture: PRODUCTIZE / ADAPT_AND_DIFFERENTIATE / BENCHMARK_AND_PREPARE / WATCH / DROP_PRODUCT_ROUTE
- coverage_state
- related_claims
- related_capabilities
- direction_links

Each direction link records a `differentiation_posture`:
- DIFFERENTIATED_BET
- RESIDUAL_RESEARCH
- CROWDED_BUT_VALUABLE
- FRONTIER_UNPROVEN
- CLOSED_DIFFERENTIATION

## Kill semantics
Use the shared strategic-model `kill_scope` vocabulary exactly:

- `KILL_BROAD_NOVELTY`
- `KILL_DIFFERENTIATED_BET`
- `KILL_MECHANISM`
- `KILL_ARCHITECTURE_NECESSITY`
- `KILL_PRODUCT_ROUTE`
- `KILL_WORDING_ONLY`

Prior art may constrain broad novelty or a differentiated Bet without reducing product relevance.

`KILL_PRODUCT_ROUTE` is the only Kill scope that directly says the product route itself should be dropped. A Trend may then move to product posture `DROP_PRODUCT_ROUTE` if that decision is supported.

Historical prose may use natural-language terms such as “killed as standalone,” but new/current canonical Decision Events should carry the normalized `kill_scope` field when a Kill decision is made.

## Hardware gate
Unchanged:

`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

Product relevance does not bypass the hardware gate.

## Compatibility
Schema projection version increments **2.2 → 2.3**.
Research authority remains V2.2.
