+++
id = "PAPER-029"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "An Efficient Context Management System for On-Device LLMaaS"
primary_url = "https://doi.org/10.1145/3774906.3800479"
priority = "P1"
evidence_role = "direct mobile persistent-context/KV generic runtime-memory baseline"
origin_paths = ["03-academic/paper-briefs/PAPER-021-040.md"]
origin_blobs = ["e2af40f95a08c39744c46ae121f469647c435363"]
authors = ["Wangsong Yin", "Mengwei Xu", "Yuanchun Li", "Xuanzhe Liu"]
venue = "SenSys 2026"
+++

# PAPER-029 — An Efficient Context Management System for On-Device LLMaaS

## 30-second read
- **Why it matters:** Shows persistent model/context state is a real mobile cost but large value can be captured by generic runtime/memory/storage management.
- **What it establishes:** Mobile S2/KV persistence and restoration cost is real; generic context management is a strong baseline.
- **Boundary:** Not Agent-specific semantic lineage and not CPU-uArch proof.

## Migration fidelity
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
- detailed V1 interpretation is preserved in [deep.md](deep.md).
- source independence remains `UNKNOWN`.
