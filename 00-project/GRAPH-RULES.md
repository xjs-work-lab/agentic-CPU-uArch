# Graph Rules — Data Model 2.3

```text
SOURCE / DISCOVERY_RUN / upstream CLAIM / EXPERIMENT
                         ↓
                    EVIDENCE_CASE
                         ↓
         SUPPORT / REBUT / UNDERCUT / SCOPE_LIMIT
                         ↓
                       CLAIM
                      /     \
                     v       v
                  TREND   DIRECTION
                    |       |
                    |   associated by
                    |   direction_links
                    v       v
         PRODUCT_EVOLUTION  DIFFERENTIATION_PORTFOLIO
                 ROADMAP       ROADMAP
```

## SOURCE / EVIDENCE_CASE / CLAIM

- **SOURCE** records provenance and source-grounded facts/claims. It is not the place for cross-source analyst synthesis.
- **EVIDENCE_CASE** is the explicit inferential route from one or more premises to a target Claim, with a typed relation such as SUPPORT / REBUT / UNDERCUT / SCOPE_LIMIT plus warrant, scope and boundary.
- **CLAIM** is the current proposition that can be supported, challenged, narrowed or falsified. Cross-paper support/rebut/undercut must be represented through Evidence Cases rather than living only in a long audit narrative.

## TREND
A product-evolution thesis: what the 2027–2029 smartphone stack is likely to need, regardless of who invented the mechanism. TREND never means “our original research Bet.”

## DIRECTION
A research/investment route: where original or target-specific whitespace remains. Product importance alone never promotes a Trend into a Direction or Bet.

TREND owns `direction_links`, each with:
- `direction_id`
- `differentiation_posture`

This avoids duplicating trend membership across Direction files and allows one Direction to play different roles in different Trends.

## ROADMAP
- `PRODUCT_EVOLUTION` schedules TREND.
- `DIFFERENTIATION_PORTFOLIO` schedules DIRECTION.
- `INTEGRATED` may schedule both.

## Core invariant
> **Prior art constrains novelty, not product relevance.**

A source may strengthen a Trend while narrowing a Direction.

Canonical Kill scopes:
- `KILL_BROAD_NOVELTY`
- `KILL_DIFFERENTIATED_BET`
- `KILL_MECHANISM`
- `KILL_ARCHITECTURE_NECESSITY`
- `KILL_PRODUCT_ROUTE`
- `KILL_WORDING_ONLY`

`KILL_PRODUCT_ROUTE` is a Decision scope. `DROP_PRODUCT_ROUTE` is the corresponding Trend product posture after such a decision is supported.

## Evidence-case rules
- one Evidence Case = one inferential route;
- multiple premises = AND;
- multiple Cases = alternative routes;
- no automatic probability aggregation.

Non-negotiable:
- path != proof;
- count != strength;
- no edge != independence;
- no edge != absence;
- graph direction != causality;
- centrality != authority;
- Actor identity != Capability;
- Capability != strategic action;
- Trend != Direction;
- product relevance != novelty.
