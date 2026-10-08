# Public-Source-Only Agentic Mobile CPU/SoC Roadmap — 2027–2029 (Round 15C)

Status: **CURRENT PROVISIONAL PUBLIC-EVIDENCE ROADMAP**, dated 2026-10-08.
Authority: [research goal lock](../00-project/research-goal-lock-agentic-mobile.md) and [7-question anti-drift tracker](../00-project/final-questions-status.md).
This document supersedes the experiment-dependent **execution instructions** in the legacy [final-2027-2029.md](final-2027-2029.md), while preserving legacy historical results.

## Strategic target and strict boundary

Guide 2027–2029 **smartphone Agentic AI** CPU/uArch, LLVM/compiler, runtime, OS, NPU/GPU cooperation, memory/subsystems, low-power SoC choices, using **ONLY public original papers, patent claims, vendor white papers, platform standards and published measurements. No experiments, simulations, PoC execution or tests are part of this project.**

End state: most important workload shifts, mature baselines, differentiated architecture hypotheses, ranked BET/FOLLOW/RESERVE/KILL, confidence and year×layer roadmap. Product silicon feasibility is explicitly an inference confidence ceiling, **not** a prerequisite to deliver.

## High-signal official mobile architecture pressure in Round 15C

| Source | Specific observed implementation | Why it changes architecture novelty and software baseline | Confidence / boundary |
|---|---|---|---|
| [Android NPU Manager VENDOR-027](../01-evidence/vendors/VENDOR-027/deep.md) | Android 17+ model-load admission, NPU app priorities, OS model-unload requests, work requested/started/resumed/ended/cancelled/paused HAL lifecycle | Strong direct OS-level baseline for AO1 mixed-criticality and AO2 task cancellation; AO3 NPU model residency | **Official platform API**, not deployment on all phones and not transactional Agent KV/version coherence |
| [Android burst HAL VENDOR-028](../01-evidence/vendors/VENDOR-028/deep.md) | Burst context caches memory mapping/driver state, FMQ low-overhead dispatch | Generic persistent execution context/memory-map reuse predates Agent era | Historical HAL mechanism, deprecated NNAPI NDK app API, no target-Agent measurements |
| [Qualcomm QNN HTP VENDOR-029](../01-evidence/vendors/VENDOR-029/deep.md) | Shared host/HTP buffers, tensor offset descriptors and conditional external weight/spill/VTCM memory | Generic CPU-NPU shared buffer and context memory are SDK primitives; focus on restrictions/cross-model validity | **SECTION_REVIEW**, official indexed tables/limitations; not blanket zero-copy or universal compatibility |
| [Android NNAPI migration VENDOR-030](../01-evidence/vendors/VENDOR-030/deep.md) | NNAPI NDK deprecated Android 15; updated TFLite/AICore recommended | Do not commit 2027 interfaces to legacy NNAPI; prefer portable, updateable runtime contracts | Official OS lifecycle, not evidence Android NN HAL removed |
| [Android AICore VENDOR-031](../01-evidence/vendors/VENDOR-031/deep.md) | On-device Gemini Nano model/runtime updates with privacy/safety, restricted packages | On-device foundation model service is existing product baseline; semantic hints must preserve permission/trust and software ownership | Official product documentation, not arbitrary agent-state access |
| [PAPER-009](../01-evidence/papers/PAPER-009/deep.md) | Real Snapdragon8Gen3 CPU↔NPU phase/operator crossover, fallbacks and dispatch cost | Strong *current stack* structural and energy signal, **also** backend/operator maturity counterpressure | Single 2026 phone/backend and LLM, not future inherent CPU advantage nor Agent-only cause |

**New finding:** Android 17 NPU Manager publicly formalizes model reservations, app priority and work lifecycle. A proposed 'Agent NPU manager', system scheduling priority, model unload, pause/resume or cancel event **without a clearly different information/control gap is crowded**. QNN/NN HAL make generic buffer passing, fast dispatch and context retention crowded too.

## Four likely high-impact workload shifts (FQ1 provisional shortlist)
1. **Persistent multi-turn personal context + cross-app task chains:** CPU control and state maintenance repeatedly interleave with heterogeneous model/tool phases (confidence: MULTI-SOURCE).
2. **Mixed reactive and proactive demand:** long low-duty-cycle sensing and occasional intervention meet tight foreground and battery budgets (confidence: product + benchmark; full-day phone prevalence uncertain).
3. **Revisable/interruptible action loops:** need safe effect authority, versioned state and selective continuation rather than simple FIFO task execution (confidence: strong academic runtime, weaker phone product data).
4. **Model/engine and memory specialization:** stages are not one monolithic inference; task quality, power, privacy, residency and CPU↔xPU backend support drive dynamic placement (confidence: real phone plus vendor/OS capabilities; economics evolving).

These are not predictions that every smartphone will run a fully autonomous long-horizon Agent by 2029.

## Three themes / three technical ownership levels (FQ3/FQ4)

### Theme F — Execution–State Lifecycle (AO1+AO2+AO3)
- **Foundation / FOLLOW→BUILD:** OS model admission/preemption/unload (Android17), QNN shared handles, HAL burst, generic scheduling, LLVM operator fusion and device-target lowering, runtime versioned KV/state capsules.
- **Architectural hypothesis / RESERVE:** a cross-model/engine *execution epoch + derived-state validity* boundary when user intent is revised; separate authorization/effect semantics from safe physical buffer release. Lower-layer implementation **not publicly justified**.
- **Kill broad novelty:** NPU priority arbiter, task-cancel callback, zero-copy I/O, generic persistent memory mapping, generic KV reuse.
- **Track evidence:** new Android/Vendor driver/HAL release, public memory/queue residency docs, independent phone phase-level performance with optimized NPU baselines. Do **not** propose or perform internal tests.
- **CPU-uArch:** focus on CPU orchestration and latency-critical software path / flexible cache reuse as competitor-follow; no new ISA, execution epoch tag or cache protocol commitment.

### Theme P — Low-Power Proactive Admission (AO4)
- **Foundation / FOLLOW:** CHRE sensing hub VENDOR-024, Qualcomm VENDOR-025, MediaTek VENDOR-019, Apple AOP VENDOR-026, PRPF PAPER-088.
- **Architecture hypothesis:** selective, consent-aware event→intent→reason wake tiers with useful-assistance versus wake/battery budgets; new dedicated Agent low-power hardware is **not** publicly necessary.
- **Kill broad novelty:** two-stage always-on wake, lightweight classifier, generic separate LP NPU. Distinguish actual assist/no-action accuracy from marketing power percentages.
- **Track evidence:** official releases with low-power context capabilities; published 24-hour false-trigger/battery studies, not proposed local device tests.

### Theme V — Agent Semantic Progress / QoE Information Contract (AO5)
- **Foundation / BUILD runtime-first:** PAPER-119 LAS, PAPER-120 SMetric, PAPER-121 ProgRouter; user history, DAG/verification/utility, cost-aware progress estimates in B4-TX.
- **Narrow differentiated A hypothesis:** only **Agent-internal RequiredProgress** that remains non-reconstructible once *all* history, OS work info, session, verifier, stage, SLO/utility and permission data are included.
- **Kill broad novelty:** adding "semantic priority" integer to OS/NPU manager, generic progress-aware model router, task time-utility functions; none alone merits new CPU/uArch work.
- **Track evidence:** published ablation with matched observability and user outcome; honest gap label if none available. No custom EXP-A execution.

## Staged 2027–2029 roadmap (public-evidence recommendations, not an experimental schedule)

| Year | User / industry signal | LLVM / software / runtime direction | OS / CPU–NPU–memory / SoC architecture watch | Investment gate (public sources only) |
|---|---|---|---|---|
| **2027: baseline consolidation** | Compare public recurring mobile Agent contexts, action success, proactive no-action prevalence; track cross-vendor capability divergence | Favor CPU stage fusion and portable LLVM AArch64 dispatch, optimized NPU backend coverage, model-stage-aware runtime control, versioned state reuse, permission-safe orchestration | **FOLLOW/BENCHMARK PUBLICLY:** Android17 NPU Manager model priorities and wake/preempt; QNN shared buffer restrictions; AICore and CHRE ecosystems; CPU-side warm state under stage churn | Keep strong *existing* A/CG06/PT-A/C lanes provisional; explicitly reject unqualified zero-copy and new scheduler novelty; use external published data to update confidence |
| **2028: selective co-design differentiation** | Track whether long-lived multimodal Agent tasks actually shift on-device, expand low-duty-cycle and revised-state occurrence | Cross-model state capsule/epoch manifests and CPU↔xPU stage metadata as **software/API concepts**, with LLVM reuse/fusion and public standards compatibility | **RESERVE research:** hardware-visible cancellation/retire only if published vendor/academic source shows an irreducible local queue/state problem; track multi-vendor memory tiers and duty-cycle LP domains | Do not promote hardware just because a paper has a speedup; prefer more direct published phone system value than server/desktop extrapolation |
| **2029: architecture option positioning** | Conditional ecosystem: proactive personal AI and local small-model collaboration could be mainstream in premium devices; market path uncertain | Favor stable cross-platform control-plane contracts, model/state compatibility and compiler portability; avoid proprietary Agent semantic ABI lock-in without standard signals | **ARCHITECTURE OPTIONS ONLY:** low-cost cross-engine handoff/state lifetime, secure event-to-intent escalation, flexible CPU locality/coherence — all conditional, not implementation commitments | Issue leadership FOLLOW/BET/RESERVE/KILL according to public product uptake, patent boundaries, software insufficiency arguments and missing-phone-data confidence ceiling |

**Years are roadmap analysis horizons, not asserted release dates or a promise to implement features.**

## Portfolio snapshot and do-not-invest list

**As of Round15C, carry forward existing canonical investment decisions without numeric/priority mutation:** A PRIMARY_BET 82.5 provisional (non-reconstructible need signal not proven), CG-06 INVEST 86.5 CPU competitive execution, PT-A PLATFORM_TRACK 80 and C ENABLER 72, CG-07 EXPLORE 75, CG-01 BENCHMARK 71; strategic reserves B-residual/R1/R2; R3 blocked. Second/third differentiated Primary Bet unfilled; no CPU-uArch Primary Bet. A's prior numeric confidence should not be confused with hardware maturity.

**DO NOT INVEST / KILL novelty:** generic Agent scheduling, priority tags, utility curves, generic multi-agent transactions, generic zero-copy/shared memory, AOSP NPU Manager reimplementation as an Agent-only silicon bet, blind always-on dual NPU, speculative state retirement ISA without specific public evidence.

## Four unresolved public-evidence ceilings and decisions
1. **Phone subsystem economics:** current sources show isolated devices and SDK APIs, not one multi-vendor comparable Agent QoE/battery/thermal cohort. Verdict: architectural mechanism credible, hardware specificity open.
2. **OS-level lifecycle versus Agent private authority:** Android NPU Manager supplies preemption/cancel/status, not legally authorized external side-effect commit nor version-compatible KV semantics. Verdict: runtime contract first; not proof new silicon.
3. **CPU/NPU 2027–29 crossover:** one Snapdragon study confirms implementation-dependent crossover; backend maturity may erase it. Verdict: CPU efficient execution strategically important, no intrinsic CPU superiority claim.
4. **Low-power dedicated Agent domain:** vendor products exist; calibrated no-action/falsenegative versus whole-day power missing. Verdict: track product convergence, no automatic uArch promotion.

## Next research priority
**Round 15D** should test *public-document sufficiency*, not run tests: update patent independent-claim pressure only for shortlisted residuals; compare additional mobile OEM CPU/NPU disclosures and publish a leadership-ready **3–5 Trend / 3 Theme / Portfolio** shortlist with explicit confidence grades and stable refs.
