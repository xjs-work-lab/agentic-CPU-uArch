# V2.2 Graph Health — Current Research State

Updated: 2026-10-06

## Current projection
- canonical nodes: **254**
- canonical semantic edges: **420**
- generated reverse edges: **420**
- graph projection: refreshed after Frontier Round 2 prior-art pressure test

## Validation status

### Last full CI / cutover QA
**PASS**

Cutover QA:
- run: `37479121798`
- job: `112322303675`
- hard graph errors: **0**

### Post-cutover Round-2 delta check
**PASS — structural delta consistency**

Checked:
- PAPER-058, PAPER-059, PAPER-060 and PAPER-061 resolve as canonical Sources;
- CLM-AGENT-005, CLM-MOBILE-002 and CLM-C-006 resolve;
- EC-A-006-A, EC-CG06-004-B, EC-C-006-A and EC-C-007-A ground their supported Claims;
- A → CLM-AGENT-005 and CLM-MOBILE-002 resolve;
- C → CLM-MOBILE-002 and CLM-C-006 resolve;
- EXP-CG06-001 → PAPER-059 resolves;
- DEC-A-003, DEC-A-004, DEC-C-003, DEC-C-004 and DEC-CG06-003 resolve;
- generated reverse edges were refreshed with the canonical projection.

## Important boundary
The Round-2 recovery did **not** execute the full repository-wide `health.py` CI job in a local clone.

Therefore:
- current projection and changed dependency closure were checked directly against the canonical delta;
- last full repository-wide health run remains the cutover QA above;
- graph structure does not promote research conclusions.

## Research-state boundary
Graph health does not:
- establish a second differentiated Primary Bet;
- infer target-phone Agent-specific residual;
- establish SOFTWARE_INSUFFICIENCY;
- promote C or CG-06;
- unblock R3 or create a uArch candidate.
