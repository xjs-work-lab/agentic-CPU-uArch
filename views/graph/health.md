# V2.2 Graph Health — Current Candidate

Updated: 2026-10-06  
Source: GitHub Actions run `37462894570` / job `112266611377`

## Result

**PASS**

## Counts
- canonical nodes: 148
- canonical semantic edges: 238
- generated reverse edges: 238
- hard errors: 0

## Warnings
30 Source objects:
`INDEPENDENCE_UNKNOWN`

Accepted by design.

## B-residual checks

PASS:
- 9 new Source IDs resolve;
- DR-BRES-STAGE15-GAP resolves;
- all B-residual Evidence Cases resolve;
- supported Claims are grounded;
- OPEN hypothesis has no fabricated SUPPORT case;
- EXP-BR-001 resolves Direction, tested Claim and all input Sources;
- DEC-BR-001 resolves;
- Roadmap includes B-residual;
- no justification cycle;
- no strategic-state leakage.

## Semantic-cardinality repair

The initial broad Claim was split before closeout:
- CLM-BR-003 = versioned validity/inheritance;
- CLM-BR-007 = provenance/dependency invalidation.

This removes an incorrect OR interpretation across two partial evidence routes.

## Boundary

Graph health validates structure.
It does not:
- infer phone SYSTEM_VALUE;
- convert synthetic model results into measurements;
- infer patent claims beyond reviewed scope;
- promote B-residual.
