# V2.2 Graph Health — Current Candidate

Updated: 2026-10-06  
Source: GitHub Actions run `37459438555` / job `112255029805`

## Result

**PASS**

- canonical nodes: 103
- canonical semantic edges: 162
- generated reverse edges: 162
- hard errors: 0

## Warnings

20 Sources:
`INDEPENDENCE_UNKNOWN`

Accepted by design.

## CG-07 checks

PASS:
- VENDOR-019 resolves;
- ACT-MEDIATEK resolves;
- MediaTek Capability resolves Actor + evidence Claim;
- DR-CG07-STAGE16A-GAP resolves;
- all five Evidence Cases resolve;
- EXP-CG07-001 can be a premise for a model-only Claim;
- CG-07 resolves six Claims + one Capability;
- Decision Event resolves;
- Roadmap includes CG-07;
- no cycles;
- no strategic-state leakage into Actor/Capability.

## Epistemic boundary

Graph health does not:
- validate the MediaTek 40% number independently;
- convert simulation to product truth;
- infer Huawei internal absence;
- promote CG-07.
