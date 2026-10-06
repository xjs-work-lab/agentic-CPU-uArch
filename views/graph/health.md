# V2.2 Graph Health — Current Candidate

Updated: 2026-10-06  
Source: GitHub Actions run `37460975903` / job `112260161412`

## Result

**PASS**

## Counts
- canonical nodes: 119
- canonical semantic edges: 190
- generated reverse edges: 190
- hard errors: 0

## Warnings
21 Source objects:
`INDEPENDENCE_UNKNOWN`

Accepted by design.

## CG-01 checks

PASS:
- VENDOR-001 resolves to ACT-QUALCOMM;
- Flex Cache Capability resolves Actor + two evidence Claims;
- DR-CG01-STAGE15D-GAP resolves;
- all four Evidence Cases resolve;
- Huawei BOUNDARY Claim has Discovery Run grounding;
- CG-01 resolves five Claims + Capability;
- EXP-CG01-001 resolves Direction, tested Claim and Source;
- DEC-CG01-001 resolves;
- roadmap includes CG-01;
- no justification cycle;
- no strategic-state leakage into Actor/Capability.

## Boundary
Graph health is structural.
It does not infer:
- vendor positioning as independent fact;
- Huawei internal absence;
- phone SYSTEM_VALUE;
- hardware necessity.
