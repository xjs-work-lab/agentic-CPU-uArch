> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

## TOOL-013 input contract

The public SME2 profiling kit emits all-runs timeline CSV with fields including:

- model_id
- name
- type
- delegate_backend
- start_us
- end_us
- duration_ms
- pct_total
- node_id
- run_index
- block

The adapter does not parse binary ETDump directly.
ETDump remains the source artifact; the public tool's CSV is the normalized ingestion point.
