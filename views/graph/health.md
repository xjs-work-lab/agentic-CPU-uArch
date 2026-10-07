# V2.2 Graph Health — Current Research State

Updated: 2026-10-07

## Current projection
- canonical nodes: **374**
- canonical semantic edges: **587**
- generated reverse edges: **587**
- graph projection: prepared for Frontier Round 13 Agent-flow heterogeneous SoC orchestration

## Round-13 full PR Graph QA
**PASS**
- run: `37607500340`
- job: `112746473467`
- validated head: `03e3554b2734e0b83d4186bec20b3714e9f45ac5`
- squash merge to main: `4e1515e8f09a8e288a343d220ba3c0ea17cd8e53`
- deterministic projection: PASS
- graph health: PASS
- work-branch cleanup: PASS / run `37607556023`

Validated structural delta:
- PAPER-097 through PAPER-100 added as SOURCE nodes;
- CLM-C-009 / CLM-CPU-005 / CLM-PTA-005 / CLM-AGENT-009 grounded;
- five Evidence Cases connect the four FULL_10Q sources;
- DEC-FRONTIER-013 records the roadmap decision;
- C evidence_maturity changes to SYSTEM_VALUE;
- no new DIRECTION node created.

## Research-state boundary
Round 13 does not:
- promote C beyond Strategic Enabler;
- change any score;
- establish software insufficiency;
- create a second differentiated Primary Bet;
- create a uArch candidate.

Round 13 is validated and merged. No hard graph errors remain in the validated PR state.


## Evidence Rescue Round 1 — EDP v1
**PASS**
- PR: #15
- Graph QA run: `37609685036`
- job: `112753634718`
- validated head: `17ae04746f74eec4e5aa4ef6d3e520ea479e9a1c`
- squash merge: `192e3fc816fd96d3112b1a0f94da916f8f869e33`
- work-branch cleanup: PASS / run `37609721034`
- deterministic projection: PASS
- graph health hard errors: 0

EDP warning state after Round 1:
- whole current ROADMAP: **22** decision-critical paper sources not yet FULL_10Q under current metadata;
- primary A/PT-A/C/CG-06/CG-07 lanes: **10** remain;
- additional current reserve-lane warnings: **12** in B-residual / R1 / R2.

Round 1 makes no graph-semantic node/edge change and no portfolio lane/score/maturity change.
It narrows canonical claim wording and introduces warning-only evidence-depth enforcement.
