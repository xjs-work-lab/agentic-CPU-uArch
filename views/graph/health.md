# V2.2 Graph Health — Current Research State

Updated: 2026-10-07

## Current projection
- canonical nodes: **360**
- canonical semantic edges: **568**
- generated reverse edges: **568**
- graph projection: refreshed after Frontier Round 12 H-CAL closure

## Validation status
### Last full CI / cutover QA
**PASS**
- run: `37479121798`
- job: `112322303675`
- hard graph errors: **0**

### Round-12 full PR Graph QA
**PASS**
- run: `37599649724`
- job: `112720612564`
- validated head: `0da17e438bd8d708fe644aea079d640f44b47830`
- squash merge to main: `7fa99ba2ae56a997e6d35bd68b508623dd2d577a`
- deterministic projection: PASS
- graph health: PASS

Checked:
- PAPER-094 through PAPER-096 resolve as SOURCE nodes;
- CLM-CAL-004 / 005 are grounded;
- three new EC-CAL cases connect all Round-12 sources;
- DEC-H-CAL-002 records the roadmap-level closure decision;
- no H-CAL DIRECTION node exists;
- generated reverse edges are refreshed.

## Research-state boundary
Graph health does not create a new Direction, change portfolio scores, establish CPU/uArch insufficiency, or claim that contiguous learning is unimportant.

Current state:
- H-CAL — CLOSED / killed as standalone candidate;
- contiguous Agent learning — retained as workload/evaluation scenario;
- second differentiated Primary Bet — unfilled;
- next frontier — unassigned.
