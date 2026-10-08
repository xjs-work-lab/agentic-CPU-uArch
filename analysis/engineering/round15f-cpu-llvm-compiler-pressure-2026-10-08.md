# Round15F — CPU/LLVM Compiler, Microkernel and Heterogeneous NPU Pressure

Date: 2026-10-08. Public evidence only; no own experiments/benchmark/PoC.

## Main answer
CPU should be treated as a dual-role programmable control host and selective existing-ISA AI endpoint, not a universal alternative to NPU. Scope-based capability/shape/precision, layout and dataflow economics determine the choice.

## Normalized original evidence
| Canonical source | What was actually reported | Non-transferable inference |
|---|---|---|
| [TOOL-012](../../01-evidence/tools/TOOL-012/deep.md) | vivo X300 1-core SqueezeSAM ExecuTorch/XNNPACK/KleidiAI INT8 556→304ms, FP16 1163→298ms; ~40% data movement | Not an Agent workload or CPU-vs-NPU benchmark; coauthored vendor report |
| [PAPER-052](../../01-evidence/papers/PAPER-052/deep.md) | SMEPilot CPU/SME tile partition, attention overlap and packed layout reuse on phone/Apple/server | Apple M4 Pro energy cannot be called phone energy; no optimized phone NPU comparison |
| [PAPER-009](../../01-evidence/papers/PAPER-009/deep.md) | Snapdragon 8 Gen 3 NPU prefill/decode stack crossover | Does not establish universal CPU prefill advantage |
| [PAPER-059](../../01-evidence/papers/PAPER-059/deep.md) | llm.npu NPU graph/shape quantization outlier CPU/GPU residual and subgraph overlap | Strong software alternative, not all models/years |
| [PAPER-057](../../01-evidence/papers/PAPER-057/deep.md) | ShadowNPU attention low-precision ranking + precise sparse residual on Snapdragon | Prefill attention focus; decode still uses CPU/GPU |
| [PAPER-098](../../01-evidence/papers/PAPER-098/deep.md) | HeRo commercial-phone dynamic Agentic-RAG partial DAG scheduling/DRAM-affinity | Strong OS/runtime baseline, not new physical instruction proof |

## Five independently owned technology levers
| Lever | Compiler/microkernel/runtime responsibility | Prior-art ceiling |
|---|---|---|
| C1 Shape and precision lowering | MLIR Linalg tile/fuse/vectorize→ArmSME and LLVM AArch64 target codegen | TOOL-015/017/018 already provide primitives |
| C2 SME stream and ZA ABI | LLVM PSTATE.SM/ZA function/callsite transitions and live-state compatibility | TOOL-014 already supports ABI. Switching latency on phone **not measured here** |
| C3 CPU µkernel and layout lifetime | KleidiAI CPU GEMM/GEMV/packing variants; runtime owns reuse of packed data and tensors | TOOL-016 exists, TOOL-012 shows ~40% data movement |
| C4 CPU-NPU stage/precision partition | Runtime/graph compiler NPU graph bucketing, CPU precision residual and fallback, bounded copies/dispatch | PAPER-059/057 moving frontier |
| C5 Agent workflow and QoE | Runtime partial DAG, criticality and bandwidth; OS resource admission and priority | PAPER-098 and Android NPU Manager already provide control |

### Key source distinctions
- LLVM streaming/ZA documentation supplies correctness/ABI mechanisms; **not** an Agent-specific context-switch cycle measurement.
- LLVM/MLIR and Arm KleidiAI are capability/codebase anchors rather than independent academic performance replications.
- TOOL-012 is a first-party coauthored performance disclosure; PAPER-052 is an independent research source with a different model, methods and platforms.
- PAPER-059 and PAPER-057 share research group lineage. PAPER-097 and PAPER-098 also have shared research authors; do not count as independent paired replications.

## Strategic judgment
**CG-06 INVEST unchanged** (existing-ISA CPU/compiler/kernel/runtime competency); C and PT-A maintain platform priority. No differentiated new Agent CPU-uArch/ISA Bet; A/B-residual/R2 remain reserves.

## 2027–2029 schedule, not an experimental program
- 2027: shape-specialized LLVM/MLIR/SME2 lowering, kernel dispatch + packed layout lifecycle; compare **published** optimized NPU CPU/NPU stage roles.
- 2028: capability-versioned portable heterogeneous stage descriptors, co-design runtime scheduling and OS NPU manager, maintain strong precision constraints.
- 2029: reserve architectural response only for publicly documented cross-engine retirement/coherence gaps; do not commit Agent ISA based on inference.

## Remaining decision gap
There is no strong matched multi-vendor end-to-end phone Agent battery/QoE comparison of fully optimized CPU and NPU backends; absent phone results set an evidence confidence ceiling rather than a requirement for tests.
