+++
id = "PAPER-032"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
independence_assessment = "UNKNOWN"
title = "Serving a Revisable World: Versioned Execution for Interruptible Agents"
primary_url = "https://arxiv.org/abs/2610.01160"
priority = "P0"
evidence_role = "versioned execution + certified compatible-state inheritance baseline"
origin_paths = ["03-academic/paper-10q/PAPER-032.md"]
origin_blobs = ["4b976c9612c587f9369f2a6d2ea29f4c1366cddb"]
authors = ["Yanxin Zhang", "Rahul Sharma", "Nitin Vegesna", "Zheyu Fu", "Chang Liu", "Trivikram Krishnamurthy"]
venue = "arXiv preprint · 2026-10-01"
+++

# PAPER-032 — Serving a Revisable World: Versioned Execution for Interruptible Agents

## 30-second read
- **Why it matters:** Directly demonstrates invalidating obsolete authority while preserving compatible completed state.
- **What it establishes:** Generic versioned Agent execution plus selective compatible-state inheritance is already implementable and useful.
- **Boundary:** Server/vLLM, not smartphone NPU/DRAM/UFS.

## Migration fidelity
- frozen V1 baseline: `960abb4ef50f050da3c6784d30826053d42e5c5d`
- transform: `STRUCTURAL_REPACK`
- detailed V1 interpretation is preserved in [deep.md](deep.md).
- source independence remains `UNKNOWN`.
