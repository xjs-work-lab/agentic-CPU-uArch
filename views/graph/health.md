# V2.2 Graph Health — Current Research State

Updated: 2026-10-07

## Current projection
- canonical nodes: **349**
- canonical semantic edges: **552**
- generated reverse edges: **552**
- graph projection: refreshed after Frontier Round 11 Contiguous Agent Learning

## Validation status
### Last full CI / cutover QA
**PASS**
- run: `37479121798`
- job: `112322303675`
- hard graph errors: **0**

### Round-11 structural delta check
**PASS — expected structural delta is internally consistent**

Checked:
- PAPER-089 through PAPER-093 resolve as SOURCE nodes;
- CLM-CAL-001 / 002 / 003 are grounded;
- five EC-CAL cases connect all five new sources;
- DEC-H-CAL-001 records the roadmap-level hypothesis decision;
- no H-CAL DIRECTION node exists;
- generated reverse edges are refreshed.

## Research-state boundary
Graph health does not make H-CAL a Direction, change portfolio scores, establish CPU/uArch insufficiency, or turn generic mobile training into Agent-specific differentiation.

Current state:
- training workload SYSTEM_VALUE — direct phone evidence exists;
- generic software capture — strong;
- Agent-specific version/coherence/concurrency residual — open;
- H-CAL — narrow analysis hypothesis only.
