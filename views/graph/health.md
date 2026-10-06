# V2.2 Graph Health — Current Candidate

Updated: 2026-10-06  
Source: GitHub Actions run `37454251444` / job `112237852669`

## Result

**PASS**

```text
candidate write boundary       PASS
graph projection deterministic PASS
graph health                   PASS
```

## Counts

- canonical nodes: 67
- canonical semantic edges: 100
- generated reverse edges: 100
- hard errors: 0

## Warnings

17 Sources currently report:
`INDEPENDENCE_UNKNOWN`

This is accepted by design.

The graph does not infer source independence from absent provenance edges.

## PT-A coverage

Validated:
- 5 new Source IDs resolve;
- DR-PTA-STAGE14-GAP resolves;
- all PT-A Evidence Case premises/targets resolve;
- PT-A Direction resolves all related Claims;
- EXP-PTA-001 resolves Direction + tested Claim + inputs;
- DEC-PTA-001 resolves;
- Roadmap includes PT-A;
- no justification cycle;
- no Actor hierarchy cycle;
- no Capability/Actor strategy leakage.

## Boundary

Graph health validates structure and dependency correctness.

It does not assign:
- truth;
- novelty;
- strategic priority;
- source independence.
