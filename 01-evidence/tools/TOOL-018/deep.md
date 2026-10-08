# TOOL-018 — Original official source eight-question technical review

- Original: https://llvm.org/docs/Vectorizers.html
- Review date: 2026-10-08
- Depth: named original technical sections; not complete source-code audit

## 1. Technical problem
How to exploit existing AArch64 CPU/MLIR features efficiently and correctly in changing inference shapes, data layouts and calling modes.

## 2. Source-proven mechanism
LLVM LoopVectorizer widens loops, SLP packs scalar operations; cost decisions involve vector factor, instruction mapping, unroll, register pressure and code size.

## 3. Existing vs new
These are existing documented platform/compiler/library capabilities. They do not establish a new Agent-only ISA or processor structure.

## 4. Ownership
LLVM/MLIR owns representation and codegen; CPU kernel library owns microkernel; runtime owns state, dispatch and memory; OS controls accelerator admission.

## 5. Relevant reported result
This document itself is not a smartphone benchmark. Pair with previously archived TOOL-012 actual vivo X300 SME2 SqueezeSAM results and PAPER-052 SMEPilot CPU-engine study.

## 6. Best competing approach
Use a mature NPU backend, shape-specialized quantization and staged heterogeneous mapping from PAPER-059/057/098 before declaring a permanent CPU win.

## 7. Decision impact
Short scalar/control AI phases could require careful cost tuning; the documentation does not establish Agent-specific vectorization gain.

## 8. Limits and next public evidence
No measured Agent-specific ABI entry cost, private RequiredProgress uplift, same-phone optimized NPU comparison or new hardware necessity. No original tests/PoCs in this project.
