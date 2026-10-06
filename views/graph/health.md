# V2.2 Graph Health — Current Candidate

Updated: 2026-10-06  
Source: GitHub Actions run `37455555156` / job `112242160296`

## Result

**PASS**

```text
candidate write boundary       PASS
graph projection deterministic PASS
graph health                   PASS
```

## Counts
- canonical nodes: 85
- canonical semantic edges: 132
- generated reverse edges: 132
- hard errors: 0

## Warnings

19 Source objects remain:
`INDEPENDENCE_UNKNOWN`

This is correct by design.

## C-specific validation

PASS:
- PAPER-051 resolves;
- VENDOR-006 resolves and links to ACT-HUAWEI;
- CAP-HUAWEI-GENERIC-RESOURCE-CONTROL resolves Actor + Claim;
- DR-C-STAGE16A-GAP resolves;
- all C Evidence Cases resolve;
- C resolves all six Claims and one Capability;
- EXP-C-001 resolves C, tested Claim and three Source inputs;
- DEC-C-001 resolves;
- Roadmap includes C;
- no justification cycle;
- no Actor hierarchy cycle;
- no strategy leakage into Capability.

## Many-to-many Source reuse

PAPER-009 is now reused by:
- CG-06 evidence;
- C evidence;
- CG-06 Experiment input;
- C Experiment input.

This is valid N:M structure.

## Boundary

Graph health validates structural correctness.
It does not:
- infer phone transfer;
- assign evidence independence;
- promote C;
- infer uArch necessity.
