+++
id = "PAPER-003"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with SERENO"
primary_url = "https://www.usenix.org/system/files/osdi26-xin.pdf"
priority = "P0"
evidence_role = "direct smartphone foreground/background interference + strong generic foreground-protection baseline"
origin_paths = ["03-academic/paper-10q/PAPER-003.md"]
origin_blobs = ["6ce5cd2a0955c0076d00d87c087e40df39936a02"]
authors = ["Tong Xin", "Xinrui Shi", "Mingkai Dong", "Zeyu Mi"]
venue = "OSDI 2026"
+++

# PAPER-003 — Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with SERENO

## 30-second read
- **Why it matters:** Direct commercial-phone evidence that background AI can materially hurt foreground QoE and that strong generic resource control already captures much of the problem.
- **What it establishes:** The mixed-criticality smartphone interference problem is real and generic foreground protection is a strong baseline.
- **Boundary:** Mobile LLM interference, not a full Agent workload; does not establish incremental DemandState value.
- **Primary source:** https://www.usenix.org/system/files/osdi26-xin.pdf

## Migration fidelity
- V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- Transform: `STRUCTURAL_REPACK`
- Detailed V1 interpretation is preserved in [deep.md](deep.md).
- Source independence remains `UNKNOWN` unless explicitly assessed later.
