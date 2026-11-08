# PAPER-125 — Mitigating Compiler Fusion-Induced Power Bursts in Mobile NPU Inference as the Battery Depletes

- **Primary source:** https://arxiv.org/abs/2607.16555
- **Full text:** https://arxiv.org/html/2607.16555
- **Submitted:** 2026-07-17 (arXiv preprint)
- **Authors:** Ryoga Yuzawa (UC Berkeley; Sony visiting researcher), Masayoshi Tomizuka (UC Berkeley)
- **Target:** Snapdragon 8 Gen 3 commercial smartphone; Qualcomm HTP NPU
- **Review date:** 2026-11-09
- **Status:** FULL_TEXT_REVIEWED / SINGLE_SOC_PREPRINT / PRIOR_ART_MISSED_BY_OCTOBER_REPOSITORY
- **Decision relevance:** CG-06 compiler/energy boundary; C power/thermal stability; not direct CPU-uArch evidence.

## Q1 — Problem

Aggressive NPU compiler operator fusion can concentrate execution into large superlayers and create high peak-current bursts. At low battery voltage, transient PDN droop can trigger DVFS or shutdown-like protection, increasing latency. The paper studies voltage stability, not average inference energy alone.

## Q2 — Mechanism

A measurement-guided offline graph rewrite inserts Quantize–Dequantize (Q–DQ) barriers at selected compiler-fusion boundaries. Candidate boundaries are profiled for PAPR and tested for vendor-compiler feasibility for each model/resolution/compiler configuration. This is a software graph transformation before the proprietary NPU compiler; it does not modify CPU ISA or silicon.

## Q3 — Results and baselines

On Snapdragon 8 Gen 3 with MobileNetV4 at 768×768, the paper reports peak current falling from 3.12 A to 1.94 A (37.8%) with 3.76% latency overhead, and an inferred DVFS-margin improvement of approximately 173 mV. PAPR-ranked splitting outperforms equal-interval and random splitting. Combining the method with sustained frequency capping yields a larger peak reduction in the tested setup.

The benefit is highly conditional:
- When baseline PAPR is high (≥2.0 in the paper's tested configurations), splitting reduces peak current by 17–40% with 2–14% latency overhead.
- When PAPR is lower, peak reduction is only 0–23% while latency rises 25–36%; forcing barriers can be counterproductive.

## Q4 — Limits

- One SoC family and two vision backbones; not a language-model or Agent benchmark.
- The 147 mV/A voltage-onset regression and derived 173 mV estimate are exploratory; the paper reports no confidence interval or hypothesis test.
- PAPR profiles and compile-feasible boundaries are model/resolution/compiler-specific and require offline characterization.
- The paper is an arXiv preprint; no independent replication or public artifact was confirmed in this review.

## Q5 — Decision impact

**No change to the CPU hardware portfolio.** This is a useful missed prior-art item for cross-layer compiler/power reasoning: compiler decisions can affect transient current and low-voltage stability, and graph-level controls may mitigate it without new hardware. It may inform a broader CG-06/C power-aware compiler/runtime subtopic, but its target is NPU graph fusion, not LLVM/AArch64 CPU optimization.

## Evidence footer

Original arXiv full text reviewed. Confidence: medium for the measured single-device result; low-to-medium for transfer to other NPU compilers, models or SoCs.
