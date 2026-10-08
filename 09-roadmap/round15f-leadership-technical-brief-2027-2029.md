# Round15F Leadership Brief — CPU/uArch and LLVM 2027–2029

**One-slide answer:** Agentic phone CPU should host flexible orchestration plus selective inference stages through existing AArch64 SIMD/SME2 and optimized LLVM/MLIR microkernels. Direct public phone data support value for CPU inference, but no new Agent CPU instruction or hardware silicon mechanism is justified.

## Decisions
- **Invest CG-06**: C1 graph/shape/precision lowering, C2 ABI state/lifetime, C3 microkernels/layout reuse, C4 CPU↔NPU split, C5 runtime/OS foreground QoE. Full [technical evidence and caveats](../analysis/engineering/round15f-cpu-llvm-compiler-pressure-2026-10-08.md).
- **Build PT-A/C**: authorized safe tool actions, QoE-aware resource scheduling and NPU admission are OS/software concerns.
- **No novel hardware Bet**: 0 independent differentiated Primary Bets on current public evidence; reserves A/B-residual/R2; R1 Watch, R3 Blocked.

## Three-year technical perspective
| Domain | 2027 | 2028 | 2029 |
|---|---|---|---|
| LLVM/CPU | Existing-ISA SME2, ABI, packing, vector/matrix kernel selection | Shape/precision-aware portable lowering and codegen capability contract | Conditional CPU-locality/handoff options; no Agent ISA |
| OS/CPU↔xPU | Best optimized NPU placement and Android NPU Manager priority | Workflow criticality and safe cross-model state contracts | Hardware only if independently published gap beyond software/OS |
| Agent quality | PT-A verified actions and stateful sessions | Trusted cross-app state/OutcomeReceipt + QoE | Portable local Agent system contracts |
| Low-power | CHRE/sensing hub and measured external published no-action | Context privacy and useful-assist energy analysis | Special LP block only if evidence exceeds generic hub |

## Explicit limits
No new experiments. TOOL-012 vivo result covers SqueezeSAM, not Agent. PAPER-052 desktop energy not phone. llm.npu/ShadowNPU and Agent.xpu/HeRo shared author lineages. Research conclusion is bounded but actionable.

## Links
- [Formal canonical portfolio](current.md)
- [Prior year/layer integrated roadmap](round15e-integrated-public-roadmap-2027-2029.md)
- [Seven final questions](../00-project/final-questions-status.md)
