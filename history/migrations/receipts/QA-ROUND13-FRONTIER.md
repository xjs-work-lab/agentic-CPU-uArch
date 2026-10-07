# Round 13 Graph QA Receipt

Purpose: validate Frontier Round 13 Agent-flow heterogeneous SoC canonical state.

Expected projection before PR QA:
- nodes: 374
- canonical semantic edges: 587
- generated reverse edges: 587

Expected semantic decision:
- C evidence maturity → SYSTEM_VALUE
- C lane/score unchanged
- no new Direction
- no second differentiated Primary Bet
- no uArch candidate


Final validation:
- V2.2 Graph QA run: 37607500340
- job: 112746473467
- conclusion: PASS
- validated head: 03e3554b2734e0b83d4186bec20b3714e9f45ac5
- squash merge to main: 4e1515e8f09a8e288a343d220ba3c0ea17cd8e53
- delete-merged-work-branch run: 37607556023
- branch cleanup conclusion: PASS

ID-integrity note:
- an intermediate PR QA run detected collisions with pre-existing CLM-AGENT-009, EC-C-009-A and EC-PTA-005-A;
- all three original canonical objects were restored unchanged from main;
- Round 13 moved to CLM-AGENT-012, EC-C-012-A, EC-PTA-006-A and EC-AGENT-012-A;
- final generator and health checks passed.
