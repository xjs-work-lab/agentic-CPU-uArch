# Agentic CPU-uArch Data Model 2.4 — Architecture Opportunity Extension

Date: 2026-10-08
Scope: additive CPU/uArch domain extension for public-evidence opportunity discovery.
Research authority remains V2.2.

## Why
V2.3 is strong at evidence grounding and at separating Product Trend from differentiated Direction.

Round 15 asks a different synthesis question:

> Why does a new architecture opportunity exist, what tension creates it, what already solves part of it, and what plausible cross-layer hypothesis remains?

Jumping directly from CLAIM to DIRECTION collapses problem, baseline, gap and architecture hypothesis into prose.

## Shared core remains unchanged

SOURCE → EVIDENCE_CASE → CLAIM → TREND → PRODUCT_EVOLUTION ROADMAP

CLAIM → DIRECTION → DIFFERENTIATION_PORTFOLIO ROADMAP

ARCHITECTURE_OPPORTUNITY is a CPU/uArch domain synthesis/search object. It does not replace TREND or DIRECTION.

## Domain extension

CLAIM / TREND / CAPABILITY
→ ARCHITECTURE_OPPORTUNITY
→ DIRECTION

An Opportunity may also reference recurring ACTOR signals.

## ARCHITECTURE_OPPORTUNITY semantics
An Opportunity is a bounded, evidence-linked architecture problem space worthy of deeper analysis.

It is not:
- a Source;
- a Claim;
- a Product Trend;
- a differentiated Direction;
- a silicon commitment.

Required fields:
- opportunity_stage: DISCOVERY / ASSESSED / SHORTLISTED / CLOSED
- coverage_state: SKELETON / SEED_MAPPED / EVIDENCE_MAPPED / ASSESSED / CLOSED
- priority_rank
- research_question
- claim_links
- related_trends
- related_directions
- related_capabilities
- related_actors

## Claim roles
Each claim link has one role:
- PROBLEM_SIGNAL
- PRODUCT_SIGNAL
- MECHANISM
- STRONG_BASELINE
- PRIOR_ART_BOUNDARY
- OPEN_GAP
- ARCH_HYPOTHESIS

Roles classify how an already-grounded Claim participates in the Opportunity argument.
They do not create new evidence.

## Evidence tension rule
Round 15 should not represent all evidence as SUPPORT.

Decision-critical Opportunity work should use Evidence Cases to capture:
- SUPPORT;
- REBUT;
- UNDERCUT;
- SCOPE_LIMIT.

Strong baselines and prior art should be represented as real inferential pressure where appropriate.

## Two graph projections

### current.json
Bidirectional navigation projection.
Contains canonical semantic edges plus generated reverse edges.
Useful for browsing.

### dependency.json
Single-direction derived dependency/inference projection.
Generated from canonical semantics only.
Excludes generated reverse edges and identity/navigation-only relations.

Use dependency.json for:
- impact traversal;
- centrality with causal/inferential intent;
- bridge analysis;
- path analysis;
- opportunity coverage analysis.

Neither generated projection is authority.

## Compatibility
- no existing Source, Claim, Evidence Case, Trend, Direction, Capability, Experiment or Decision ID changes;
- existing V2.3 semantics remain valid;
- schema projection version increments 2.3 → 2.4;
- AO-1..AO-5 begin as SEED_MAPPED and must be evidence-closed in Round 15A.
