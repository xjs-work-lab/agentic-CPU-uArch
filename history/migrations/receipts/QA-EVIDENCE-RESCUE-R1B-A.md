# QA-EVIDENCE-RESCUE-R1B-A

Date: 2026-10-07
Scope: Candidate A Evidence Rescue 1B deep audit.

## Revalidated sources
- PAPER-013 — Speculative Interaction Agents
- PAPER-015 — PARE
- PAPER-043 — Proactive Agent / ICLR 2025
- PAPER-044 — ProAgentBench
- PAPER-050 — TomasuLLM

## Canonical decision
A remains:
- PRIMARY_BET
- 82.5
- SIMULATION_SUPPORT

The differentiated core is narrowed to:
**non-reconstructible Agent-internal DemandState / RequiredProgress information value beyond B4-TX.**

No literature source directly proves that residual.

## Experiment change
EXP-A-001 becomes a matched-observability conditional-information test.

Kill/downgrade condition:
if long personalized history + runtime state + SLO/utility + topology + legality/reuse proxies reproduce nearly all B6-Demand value and the residual falls below ~5%, A should be downgraded or killed as differentiated research.

## QA
- PR: #17
- run: `37617038459`
- job: `112777774022`
- validated head: `f18e2d5871599f714d88d12d4ff825809b1d3370`
- result: PASS
- deterministic projection: PASS
- hard graph errors: 0
- graph: 384 nodes / 622 canonical semantic edges / 622 generated reverse edges
- primary-lane EDP paper warnings: 0
- whole-roadmap EDP paper warnings: 12, all in B-residual / R1 / R2
- squash merge: `95cb25d3899353206c39c29ebed69ed3d324b4d9`
- cleanup run: `37617300996`
- cleanup: PASS

## Research consequence
A/PT-A/C/CG-06/CG-07 are now paper-depth clean under EDP v1.
Frontier Round 14 is unlocked.

Reserve-lane paper debt and patent direct-claim audit remain mandatory before final portfolio convergence.
