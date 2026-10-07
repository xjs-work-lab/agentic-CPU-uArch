# PAPER-107 — MCP-SandboxScan / SandScope — FULL_10Q

## Q1 — Problem
Audit untrusted MCP/Agent tools at runtime and capture source-to-sink exposure into LLM-visible outputs.

## Q2 — Why it matters
Agent tools create real authority/provenance risk, but this is a security/runtime contract before it is a CPU mechanism.

## Q3 — Hypothesis
Controlled execution can expose runtime evidence missed by static scanning. A separate T6 hypothesis — phone-specific WASM/JIT/code-cache cost — is not tested.

## Q4 — Baselines
Direct WASM, WASM shim and native stdio MCP coexist. Strong native containment can use Docker/Bubblewrap.

## Q5 — Mechanism
Canary sources + controlled execution + MCP-aware sink extraction + semantic capability profiling.

## Q6 — Evaluation
30 controlled subjects across Go/Python/Rust/TypeScript; v2 also studies 100 MCP repositories. Real-world shallow dynamic scans succeed on 35 repositories; semantic profiling recovers 1,127 tools across 71 repositories; targeted exploration re-executes 33/35 and observes witnesses in 12. Controlled precision/recall/F1 are 1.000/0.889/0.941.

The reported scan latency includes build/startup/scanner work and is not normal WASM execution overhead.

## Q7 — Limitations
No smartphone, phone power/thermal/QoE, JIT/interpreter, code-cache or Android baseline.

## Q8 — Fact vs inference
FACT: WASI is useful containment for portable artifacts.
FACT: native MCP execution remains necessary in broad real-world coverage.
INFERENCE: authority/provenance belongs primarily to PT-A/platform security.

## Q9 — Project decision
No standalone T6 CPU/uArch residual is established.

## Q10 — Action
Use as strongest containment/security pressure baseline; do not promote a WASM/code-cache Direction.

Primary: https://arxiv.org/abs/2601.01241
