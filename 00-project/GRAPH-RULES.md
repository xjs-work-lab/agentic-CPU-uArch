# Graph Rules — Data Model 2.4

SOURCE / DISCOVERY_RUN / upstream CLAIM / EXPERIMENT
→ EVIDENCE_CASE
→ SUPPORT / REBUT / UNDERCUT / SCOPE_LIMIT
→ CLAIM

CLAIM → TREND → PRODUCT_EVOLUTION ROADMAP
CLAIM → DIRECTION → DIFFERENTIATION_PORTFOLIO ROADMAP

CPU/uArch Round-15 extension:
CLAIM / TREND / CAPABILITY → ARCHITECTURE_OPPORTUNITY → DIRECTION

## SOURCE / EVIDENCE_CASE / CLAIM
- SOURCE records provenance and source-grounded content.
- EVIDENCE_CASE owns the inferential route, warrant, scope and boundary.
- CLAIM is the proposition that can be supported, rebutted, undercut, narrowed or falsified.

## TREND
A product-evolution thesis. Product relevance is independent of originality.

## ARCHITECTURE_OPPORTUNITY
A synthesis/search object for a bounded cross-layer architecture problem space.

Opportunity claim roles:
- PROBLEM_SIGNAL
- PRODUCT_SIGNAL
- MECHANISM
- STRONG_BASELINE
- PRIOR_ART_BOUNDARY
- OPEN_GAP
- ARCH_HYPOTHESIS

Opportunity is not evidence and does not by itself justify investment or hardware.

## DIRECTION
A research/investment route where differentiated or target-specific work may remain.

## ROADMAP
- PRODUCT_EVOLUTION schedules TREND.
- DIFFERENTIATION_PORTFOLIO schedules DIRECTION.
- INTEGRATED may schedule both.

## Core invariant
Prior art constrains novelty, not product relevance.

## Opportunity invariant
Architecture opportunity discovery and silicon commitment are separate gates.

Public evidence may justify an ARCHITECTURE_OPPORTUNITY / ARCH_HYPOTHESIS.
It does not automatically justify UARCH_CANDIDATE.

## Evidence-case rules
- one Evidence Case = one inferential route;
- multiple premises = AND;
- multiple Cases = alternative routes;
- no automatic probability aggregation;
- strongest-baseline pressure should use REBUT / UNDERCUT / SCOPE_LIMIT where semantically correct rather than being hidden only in prose.

## Projection rule
views/graph/current.json is for navigation and includes generated reverse edges.
views/graph/dependency.json is the single-direction dependency/inference projection for graph algorithms.

## Non-negotiable
- path != proof;
- count != strength;
- centrality != authority;
- no edge != absence;
- Actor identity != Capability;
- Capability != strategic action;
- Trend != Opportunity;
- Opportunity != Direction;
- Opportunity != silicon commitment;
- product relevance != novelty.
