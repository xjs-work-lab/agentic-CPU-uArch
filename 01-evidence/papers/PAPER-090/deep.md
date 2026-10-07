# PAPER-090 — FBLayout: Optimizing Memory Layout for Efficient LLM Finetuning on Mobile GPUs

## Source
- MobiSys 2026
- DOI: 10.1145/3745756.3809214
- arXiv:2607.21624
- real mobile phones with ARM Mali and Qualcomm Adreno GPUs
- Priority: P0 strongest generic mobile-training baseline

## Q1 — Problem + target mapping
Transformer fine-tuning on mobile GPUs performs forward and backward computation with conflicting tensor-access patterns.
Layouts efficient for one phase can become inefficient for the other, causing transformations, poor locality and memory pressure.

Target mapping:
> how much of mobile training cost is already removable by software/layout co-design before claiming a new system or hardware control point?

## Q2 — Novelty / new-regime relevance
FBLayout introduces:
- R-Tile unified layout;
- tile-level index transformation;
- activation-guided global layout selection.

New-regime classification:
**GENERIC ENABLING** for mobile training.
It is highly relevant to an Agent-learning frontier, but the mechanism is not Agent-specific.

## Q3 — Falsifiable hypothesis
If layout conflict is a major bottleneck in mobile transformer training, a unified texture-aware layout plus logical index remapping should materially improve training throughput and memory behavior.

Falsifiers:
- compute dominates regardless of layout;
- layout gains vanish across GPU families;
- conversion overhead is negligible;
- benefits disappear on larger LLM fine-tuning.

The reported multi-device results support the hypothesis.

## Q4 — Research lineage / competing route
Competing routes:
- MNN / TFLite / TVM training paths;
- explicit layout transformations;
- one-layout reuse;
- CPU training;
- LoRA / recomputation / checkpointing;
- NPU or heterogeneous training.

## Q5 — Key mechanism / control point
The core control point is **tensor layout and data movement across forward/backward phases**.

R-Tile is tailored to mobile GPU texture memory.
Index transforms replace physical reshape/transpose movement where possible.
Global layout selection propagates choices through the graph.

## Q6 — Experiment design
Evaluation spans seven transformer models on multiple mobile phones using ARM Mali and Qualcomm Adreno GPUs.

Reported aggregate speedup:
**2.2–5.7×** over MNN, TFLite and TVM, with improved cache efficiency and lower memory pressure.

The paper also reports that mobile-GPU inference advantage can collapse during fine-tuning because backward/layout behavior differs sharply.

## Q7 — Data / artifact / reproducibility
Strengths:
- peer reviewed at MobiSys;
- real mobile devices;
- cross-GPU-family evaluation;
- multiple model families;
- clear root-cause mechanism.

Limitations:
- not a continual-Agent workload;
- primarily GPU-centric;
- no mixed foreground inference + background training Agent loop;
- architecture portability to NPU/CPU paths is open.

## Q8 — Evidence vs hypothesis
### [FACT]
Mobile fine-tuning can suffer substantial layout/data-movement inefficiency absent in inference-oriented optimization.

### [FACT]
FBLayout reports large speedups through software/layout co-design.

### [OBSERVATION]
A training bottleneck that looks architectural can be heavily reduced by representation/layout changes.

### [INFERENCE — project]
Generic mobile-training inefficiency cannot be used as evidence for a differentiated Agent CPU/uArch Bet.

## Q9 — Real contribution to project decision
FBLayout is a **strongest-baseline pressure source** for H-CAL.

It narrows:
- “training needs new hardware”;
- “backward memory pressure is intrinsically architectural”;
- “mobile GPU cannot train efficiently.”

It does not address:
- Agent-driven update timing;
- versioned KV validity;
- mixed live inference/training control.

## Q10 — Next action
1. KEEP as P0 generic mobile-training baseline.
2. Use it to subtract generic layout/data-movement cost from any Agent-specific residual.
3. Search for target-phone concurrent inference + training evidence.
4. No portfolio score change by itself.

## Decision footer
- **Evidence maturity:** SYSTEM_VALUE for generic mobile training
- **Decision impact:** raises H-CAL strongest baseline
- **Open questions:** mixed workload, NPU/CPU transfer, thermal interaction with live Agent use
- **Primary source:** https://arxiv.org/abs/2607.21624
