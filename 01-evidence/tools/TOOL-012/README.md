+++
id = "TOOL-012"
type = "SOURCE"
source_type = "tool"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "ExecuTorch + Arm SME2 phone measurements"
primary_url = "https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/"
priority = "UNSPECIFIED"
evidence_role = "real-phone CPU SME2 inference acceleration + bottleneck-shift engineering corroboration"
origin_paths = ["analysis/stage16a/public_evidence/README.md"]
origin_blobs = ["21c60cd65c7148b97792a62e7570100ff5657f1e"]
+++

# TOOL-012 — ExecuTorch + Arm SME2 phone measurements

## 30-second read
- **Why it matters:** Real vivo X300 measurements show substantial SME2 acceleration and ~40% post-SME2 data-movement share.
- **What it establishes:** Existing CPU matrix capability can materially improve real-phone AI latency and shift optimization pressure toward data movement/layout.
- **Boundary:** SqueezeSAM/ExecuTorch measurements; not CPU-vs-NPU and not Agent end-to-end evidence.
- **Primary source:** https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/

## Migration fidelity
- V1 baseline: `960abb4ef50a8f5b0bd357c067f08346025d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
