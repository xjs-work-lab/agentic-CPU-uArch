# V2.2 Graph Health — Current Research State

Updated: 2026-10-07

## Current projection
- canonical nodes: **384**
- canonical semantic edges: **622**
- generated reverse edges: **622**
- graph projection: validated after Evidence Rescue 1B A deep audit

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


## Evidence Rescue 1A — PT-A
**PASS**
- PR: #16
- final Graph QA run: `37611820867`
- job: `112760599058`
- validated head: `d091b6d142edfe1fbb6eb87ffefd08ccc9e951d7`
- squash merge: `e6a83b36494ec9bcc044b3aec6441152efd132f1`
- work-branch cleanup: PASS / run `37611888348`
- deterministic projection: PASS
- graph hard errors: 0
- current projection: **383 nodes / 610 canonical edges / 610 reverse edges**

### Structural delta
- PAPER-101 Action Rebinding added as negative/context-integrity evidence.
- PAPER-102 VeriGUI added as strongest software verification/recovery baseline.
- CLM-PTA-006 adds the observation→action context-integrity claim.
- CLM-PTA-EXP-002 + EXP-PTA-002 create the fresh-context action-binding residual test.
- DEC-PTA-RESCUE-001 records PT-A REFRAME with no lane/score/maturity change.
- PAPER-037/038/039/040/042 are EDP v1 FULL_10Q revalidated.

### EDP warning state
- primary-lane paper warnings: **5**, all in A.
- reserve-lane paper warnings: **12**.
- whole current ROADMAP: **17**.

### QA correction note
The first PR QA run (`37611716486`) failed deterministic projection because the updated EC-PTA-003-B added PAPER-102 as a canonical premise but the manually refreshed projection initially omitted that edge.
The canonical Evidence Case was correct; the projection was repaired, regenerated and then passed.


## Evidence Rescue 1B — A
**PASS**
- PR: #17
- Graph QA run: `37617038459`
- job: `112777774022`
- validated head: `f18e2d5871599f714d88d12d4ff825809b1d3370`
- squash merge: `95cb25d3899353206c39c29ebed69ed3d324b4d9`
- work-branch cleanup: PASS / run `37617300996`
- deterministic projection: PASS
- graph hard errors: 0
- current projection: **384 nodes / 622 canonical edges / 622 reverse edges**

### Structural delta
- PAPER-013 / 015 / 043 / 044 / 050 revalidated as EDP v1 FULL_10Q.
- PAPER-043 venue corrected to ICLR 2025.
- CLM-AGENT-001 / 002 / 003 boundaries tightened.
- CLM-A-001 narrowed to conditional information value of non-reconstructible DemandState / RequiredProgress.
- EXP-A-001 strengthened into a matched-observability residual test.
- DEC-A-007 records revalidation/narrowing with no lane/score/maturity promotion.
- six additional historical/strong-baseline Sources are explicitly connected to EXP-A-001.

### EDP warning state
- A / PT-A / C / CG-06 / CG-07 paper warnings: **0**.
- B-residual / R1 / R2 paper warnings: **12**.
- whole current ROADMAP paper warnings: **12**.

### Portfolio boundary
A remains PRIMARY_BET / 82.5 / SIMULATION_SUPPORT, provisionally.
No source directly proves CLM-A-001.
No SOFTWARE_INSUFFICIENCY pass.
No hardware-specific cause.
No uArch candidate.

Frontier Round 14 is unlocked after this validation.
