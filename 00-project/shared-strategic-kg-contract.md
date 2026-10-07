# Shared Strategic Knowledge-Graph Contract

Version: STRATEGIC_KG_CORE_V1
Date: 2026-10-07

This repository uses the same domain-neutral strategic knowledge-graph language as sibling research programs.

Directory numbering and domain-specific objects may differ. The semantics below must not drift.

## Mother model

```text
SOURCE → EVIDENCE_CASE → CLAIM → TREND → PRODUCT_EVOLUTION ROADMAP
                              ↘ DIRECTION → DIFFERENTIATION_PORTFOLIO ROADMAP
```

## Object semantics

### SOURCE
A provenance object for a paper, patent, vendor/official source, benchmark, artifact or other evidence source.

SOURCE stores source-grounded facts and metadata.
It does not own cross-source analyst synthesis.

### EVIDENCE_CASE
An explicit inferential route from one or more premises to a target Claim.

Required reasoning semantics:
- SUPPORT
- REBUT
- UNDERCUT
- SCOPE_LIMIT

Warrant, scope and boundary must remain explicit.

Important cross-paper support/rebut/undercut must be modeled here rather than only described in audit prose.

### CLAIM
The current proposition that can be supported, challenged, narrowed or falsified.

A Claim is not made true by graph connectivity or source count.

### TREND
A statement about how the **2027–2029 product / technology stack should evolve**.

TREND is independent of originality.
A Trend may be important even if the broad idea is already well-covered by prior art.

### DIRECTION
A statement about **remaining differentiated / original research space** available to the team.

Product importance alone does not create a Direction or Bet.

## Product posture vocabulary

Use exactly one canonical primary posture per Trend:

- PRODUCTIZE
- ADAPT_AND_DIFFERENTIATE
- BENCHMARK_AND_PREPARE
- WATCH
- DROP_PRODUCT_ROUTE

Secondary implementation activities may be described in prose; do not encode a second product posture token.

## Differentiation posture vocabulary

Use only:

- DIFFERENTIATED_BET
- RESIDUAL_RESEARCH
- CROWDED_BUT_VALUABLE
- FRONTIER_UNPROVEN
- CLOSED_DIFFERENTIATION

Differentiation posture applies to a Direction in the context of a Trend.

## Kill scope vocabulary

Use the canonical `kill_scope` field:

- KILL_BROAD_NOVELTY
- KILL_DIFFERENTIATED_BET
- KILL_MECHANISM
- KILL_ARCHITECTURE_NECESSITY
- KILL_PRODUCT_ROUTE
- KILL_WORDING_ONLY

A Kill scope must not be silently widened.

In particular:

> **Prior art constrains novelty, not product relevance.**

`KILL_DIFFERENTIATED_BET` or `KILL_BROAD_NOVELTY` can coexist with a highly important Product Trend.

Only `KILL_PRODUCT_ROUTE` says the product route itself should be dropped; the corresponding Trend posture may become `DROP_PRODUCT_ROUTE`.

## Management views

Two views must remain separate:

### Product Evolution Map
What future products should gain or prepare for.

### Differentiation Portfolio
Where the team should make original/differentiated research investments.

A leadership summary may combine both, but the canonical management semantics stay separate.

## CPU/uArch domain gate

CPU/uArch retains its domain-specific final promotion gate:

`STRUCTURAL_SIGNAL → SYSTEM_VALUE → SOFTWARE_INSUFFICIENCY → hardware-specific cause → UARCH_CANDIDATE`

The mother model ends before this domain-specific gate.
Product relevance never bypasses it.

## Compatibility rule

Do not introduce alternative strategic object types that duplicate TREND or DIRECTION semantics.
Do not migrate mature canonical objects merely to make directory layouts match another repository.
Semantic compatibility is more important than path compatibility.
