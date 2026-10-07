+++
id = "CLM-MEM-003"
type = "CLAIM"
record_state = "CURRENT"
claim_kind = "OBSERVATION"
status = "SUPPORTED"
scope = "dense long-horizon personal-memory workload on evaluated NVIDIA Spark GB10 edge platform"
supersedes = []
+++

# CLM-MEM-003

## Proposition
In the evaluated dense personal-memory workload, memory search is usually a modest fixed addition to TTFT relative to reader inference, while structured-memory ingest can incur much larger cumulative energy because it invokes extractor-model computation.

## Evidence
PAPER-077 / MemArena.

## Quantitative anchors
- search: ~87 ms BM25-RAG, ~7 ms Memobase, ~48 ms MemSearch;
- only the smallest-reader + slowest-backend case makes search ~54% of TTFT;
- 15-day structured Memobase ingest: ~52–1,222 kJ across evaluated extractor/model scales.

## Boundary
Edge-node result, not smartphone SYSTEM_VALUE.
The energy range is implementation/model dependent.