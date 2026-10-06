+++
id = "TOOL-013"
type = "SOURCE"
source_type = "tool"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Arm SME2 ExecuTorch Profiling Kit"
primary_url = "https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling"
priority = "UNSPECIFIED"
evidence_role = "public SME2 on/off profiling + ETDump operator-breakdown workflow"
origin_paths = ["analysis/stage16a/harness/README.md"]
origin_blobs = ["5a721b9875ff526e1144a71d8081edd91f6a66be"]
+++

# TOOL-013 — Arm SME2 ExecuTorch Profiling Kit

## 30-second read
- **Why it matters:** Provides a reproducible public measurement path for existing CPU matrix capability.
- **What it establishes:** The CG-06 measurement path can be implemented with public profiling tooling on supported platforms.
- **Boundary:** Measurement/reproducibility artifact, not evidence that CPU wins a particular production workload.
- **Primary source:** https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
