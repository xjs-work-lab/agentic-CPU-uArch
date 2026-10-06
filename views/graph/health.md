# V2.2 Graph Health — A + CG-06 Pilot Slice

Updated: 2026-10-06  
Source: GitHub Actions run `37450211533` / job `112224680177`

## Result

**PASS**

```text
candidate write boundary      PASS
graph projection deterministic PASS
graph health                   PASS
```

## Counts

- canonical nodes: 44
- canonical semantic edges: 60
- generated reverse edges: 60
- hard errors: 0

## Warnings

Accepted warnings:

```text
INDEPENDENCE_UNKNOWN:PAPER-003
INDEPENDENCE_UNKNOWN:PAPER-009
INDEPENDENCE_UNKNOWN:PAPER-013
INDEPENDENCE_UNKNOWN:PAPER-015
INDEPENDENCE_UNKNOWN:PAPER-041
INDEPENDENCE_UNKNOWN:PAPER-043
INDEPENDENCE_UNKNOWN:PAPER-044
INDEPENDENCE_UNKNOWN:PAPER-050
INDEPENDENCE_UNKNOWN:PAPER-052
INDEPENDENCE_UNKNOWN:TOOL-012
INDEPENDENCE_UNKNOWN:TOOL-013
INDEPENDENCE_UNKNOWN:VENDOR-018
```

Interpretation:
unknown provenance independence remains UNKNOWN.
It is not converted into verified independence.

No `UNCONNECTED_SOURCE` warning remains.

## Impact — PAPER-052

```text
EC-CG06-002-A
EXP-CG06-001
CLM-CPU-002
CAP-ARM-C2-SME2-CPU-AI
CG-06
DEC-CG06-001
ROADMAP-CURRENT
```

## Impact — PAPER-009

```text
EC-CG06-001-A
EXP-CG06-001
CLM-CPU-001
CG-06
DEC-CG06-001
ROADMAP-CURRENT
```

## Tool defect found and closed

First CI run found a non-determinism bug:
the builder emitted absolute runner paths.

Fix:
canonical paths are now always relative to the repository root.

The second run passed all checks.

## Boundary

Graph health detects structure, grounding, cycles, endpoint errors and impact.

It does not:
- assign Claim truth;
- infer source independence;
- promote Direction state;
- infer Huawei internal absence.
