+++
id = "PAPER-107"
type = "SOURCE"
source_type = "paper"
record_state = "CURRENT"
review_depth = "FULL_10Q"
deep_review_protocol = "EDP_V1"
deep_review_date = "2026-10-07"
decision_critical = true
decision_use = "T6_SANDBOX_SECURITY_AND_WASI_BOUNDARY"
independence_assessment = "INDEPENDENT_UNIVERSITY_RESEARCH"
title = "MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools"
primary_url = "https://arxiv.org/abs/2601.01241"
priority = "P0"
evidence_role = "Agent-tool runtime security/containment baseline; negative pressure on standalone T6 CPU residual"
authors = ["Zhuoran Tan", "Run Hao", "Jeremy Singer", "Yutian Tang", "Christos Anagnostopoulos"]
venue = "arXiv preprint v2, revised 2026-06-22"
artifact_urls = ["https://anonymous.4open.science/r/MCP-SandboxScan-FFFB"]
+++

# PAPER-107 — MCP-SandboxScan / SandScope

## 30-second read
- v2 expands the original seed to 30 controlled subjects plus a 100-repository MCP corpus.
- SandScope supports WASI-backed portable tools and native stdio MCP execution.
- The paper explicitly separates its runtime-audit contribution from “WASM instead of OS sandboxing.”
- Native untrusted tools still require strong OS containment.
- No smartphone, JIT, code-cache, energy or thermal experiment.
- T6 impact: strengthen PT-A/platform security baseline; narrow standalone T6 differentiation.

See [deep.md](deep.md).
