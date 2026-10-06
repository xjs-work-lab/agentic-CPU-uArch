# V2.2 Graph Health — Current Research State

Updated: 2026-10-06

## Current projection

- canonical nodes: **238**
- canonical semantic edges: **396**
- generated reverse edges: **396**
- graph projection: refreshed after the 2026-10-06 frontier 10Q round

## Validation status

### Last full CI / cutover QA
**PASS**

Cutover QA:
- run: `37479121798`
- job: `112322303675`
- hard graph errors: **0**

### Post-cutover frontier delta check
**PASS — structural delta consistency**

Checked after the frontier 10Q round:
- PAPER-053, PAPER-054, PAPER-056, PAPER-057 resolve as canonical Sources;
- PAPER-003 remains the sole Sereno identity; duplicate PAPER-055 is removed;
- CLM-AGENT-004 and CLM-CPU-004 resolve;
- EC-A-005-A and EC-CG06-004-A ground the new supported Claims;
- A → CLM-AGENT-004 resolves;
- C → CLM-MOBILE-001 resolves;
- CG-06 → CLM-CPU-004 resolves;
- EXP-CG06-001 → PAPER-057 resolves;
- DEC-A-002, DEC-C-002 and DEC-CG06-002 resolve;
- generated reverse edges were refreshed with the canonical projection.

## Important boundary

The post-cutover frontier recovery did **not** execute the full `health.py` CI job in a local clone because the execution environment has no outbound GitHub network access.

Therefore:
- the current graph projection and changed dependency closure were checked directly against the canonical delta;
- the last full repository-wide health run remains the cutover QA above;
- no research conclusion is promoted on the basis of graph structure alone.

## Research-state boundary

Graph health validates structure only.

It does not:
- infer target-phone SYSTEM_VALUE;
- infer Agent-specific residual beyond strong software/runtime baselines;
- establish SOFTWARE_INSUFFICIENCY;
- promote C or CG-06 to a differentiated Primary Bet;
- unblock R3 or create a uArch candidate.
