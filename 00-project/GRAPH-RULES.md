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

## TREND
A product-evolution thesis: what the 2027–2029 smartphone stack is likely to need, regardless of who invented the mechanism.

## DIRECTION
A research/investment route: where original or target-specific whitespace remains.

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
Only an explicit `DROP_PRODUCT_ROUTE` decision kills product relevance.

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
