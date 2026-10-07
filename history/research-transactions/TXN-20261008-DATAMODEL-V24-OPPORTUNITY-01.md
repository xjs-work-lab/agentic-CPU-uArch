# TXN-20261008-DATAMODEL-V24-OPPORTUNITY-01

Date: 2026-10-08

## Purpose
Add a minimal Architecture Opportunity synthesis layer before Round 15 evidence closure.

## Additive changes
- schema projection 2.3 → 2.4;
- new canonical type ARCHITECTURE_OPPORTUNITY;
- AO-1..AO-5 seeded as DISCOVERY / SEED_MAPPED;
- typed Opportunity→Claim roles;
- Opportunity links to Trend / Direction / Capability / Actor;
- generated single-direction views/graph/dependency.json;
- graph QA extended for Opportunity semantics and both projections.

## Preserved
No existing Source, Evidence Case, Claim, Actor, Capability, Trend, Direction, Experiment, Decision Event or Roadmap ID was renamed or migrated.

## Graph counts after upgrade
- nodes: 453
- canonical semantic edges: 837
- generated reverse edges: 837
- derived dependency edges: 787

## Next
Round 15A — Architecture Opportunity Evidence Skeleton Audit for AO-1..AO-5.
