# Round 15A — AO-4 Evidence Skeleton and Deep-Source Audit

Date: 2026-10-08
Coverage: EVIDENCE_MAPPED (4 of 5)
Goal: decide what stays awake in a proactive personal Agent after software/model and mature low-power offload pressure.

## Deep source register / identity decision
| Canonical source | Type | Deep read and scope | Independent evidence caveat |
|---|---|---|---|
| PAPER-087 ProactiveMobile | CVPR 2026 | Prior FULL_10Q reused; official CVPR version and arXiv full HTML Sections 3–4 cross-checked | benchmark/task capability; no measured phone daily context |
| PAPER-088 PRPF | 2026 preprint | Prior FULL_10Q reused; arXiv v1 full HTML Sections 3, 4, Appendix B/C; v2 announced 2026-08-31 but version delta not fully checked | offline GPU compute/latency; 17.19% multimodal SR; no real-user traces |
| VENDOR-019 MediaTek | official product | Prior deep 10Q; 9600 Pro primary and launch release checked | architecture disclosed; always-on power comparison vendor-origin |
| VENDOR-024 AOSP CHRE | official platform documentation | New full 10Q; runtime, HAL, nanoapps, sensors/batching and trust limits | longstanding platform baseline, not Agent implementation |
| VENDOR-025 Qualcomm Sensing Hub | official product | New full 10Q; dual micro-NPUs and always-sensing ISPs | vendor dynamic page; no normalized phone Agent energy |
| VENDOR-026 Apple AOP Siri | official engineering note, 2017 | New full 10Q; two-stage tiny/large DNN wake, error thresholds and field evaluation | narrow voice trigger, not general multi-intent Agent |

Source identity: no new PAPER ID for PRPF v2 or CVPR-vs-arXiv ProactiveMobile. New VENDOR-024/025/026 have distinct original URLs from existing VENDOR source records. No patent claims are newly asserted or directly audited.

## Seven-role evidence matrix
| Role | Claim | Support / pressure |
|---|---|---|
| Problem | CLM-AO4-001 | PAPER-087; EC-AO4-001-B benchmark-to-phone limit |
| Product | CLM-AO4-002 | independent vendor official announcements VENDOR-019/025, not independent benchmarks |
| Mechanism | CLM-AO4-003 | PRPF staged gate; CHRE event bridge; Apple two-stage hardware wake |
| Strong baseline | CLM-AO4-004 | PRPF+CHRE+CPU/shared-NPU alternative; no stitched device result |
| Prior art | CLM-AO4-005 | 2017 Apple AOP and AOSP CHRE. Patent-family/direct claim scope not claimed |
| Open gap | CLM-AO4-006 | context-intent handoff and wake correctness/battery/permission tension; EC-AO4-006-B undercuts necessity |
| Architecture hypothesis | CLM-AO4-007 OPEN | event→intent→reason with budgeted escalation, not asserted silicon bet |

## Core cross-source insight
**[FACT]** The proactive workload adds a learned 'whether to intervene' decision beyond keyword spotting. **[FACT]** Dedicated low-power sensing/AI execution is productized and its generic AP wake mechanism has longstanding history. **[FACT]** PRPF reports 20.82→41.15% overall SR, 13.76→7.21% overall FTR, 69.3% expected inference compute reduction, 60.1% latency reduction and 12% peak GPU memory increase versus its 7B baseline in GPU benchmark; text-only vs screenshot results diverge sharply (65.15% vs 17.19% SR). **[INFERENCE]** Most false workload volume should be removed before comparing dedicated AI silicon economics. **[HYPOTHESIS]** A trust-aware context handoff/escalation policy may remain valuable after learned software gate plus CHRE, but its silicon dependence is unknown.

## Hardware economics questions (no fabricated numbers)
E_total = E_sense + E_encode + E_gate + P_idle·T + N_wake·E_wake + E_handoff + E_reason + E_retry.
Compare on **matched utility / SR / FTR / consent/privacy** rather than raw energy alone. Distinguish always-on sensing from always-on heavy Agent reasoning; high FNR may deceptively lower joules/day.

## New-regime differentiation
- Native/Amplified: latent multi-intent no-action calibration across changing app/state/user context, permission-limited availability and intermittent multi-model escalation.
- Generic enabling / crowded: sensor hub, tiny wake detector, two-stage wake, generic NPU placement, batching, AP power gating.
- Surviving structural tension: event/intent/workload distribution uncertainty, context validity and permission-aware state handoff, wake cost versus helpfulness/foreground overhead.

## Decision
AO-4 **KEEP / EVIDENCE_MAPPED / FOLLOW + RESEARCH CROSS-LAYER SPLIT**. No new investment lane, uArch or CPU ISA claim. CG-07 remains EXPLORE. Next AO-5, then AO-1..5 interaction/synthesis.

## First-hand links
- ProactiveMobile peer-reviewed: https://openaccess.thecvf.com/content/CVPR2026/html/Kong_ProactiveMobile_A_Comprehensive_Benchmark_for_Boosting_Proactive_Intelligence_On_Mobile_CVPR_2026_paper.html
- PRPF preprint/v1 HTML: https://arxiv.org/html/2606.03236v1
- MediaTek: https://www.mediatek.com/products/smartphones/mediatek-dimensity-9600-pro
- AOSP CHRE: https://source.android.com/docs/core/interaction/contexthub
- Qualcomm Sensing Hub: https://www.qualcomm.com/snapdragon/smartphones/ai
- Apple AOP two-pass: https://machinelearning.apple.com/research/hey-siri
