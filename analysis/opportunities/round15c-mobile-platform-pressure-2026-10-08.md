# Round15C — Android17 NPU Manager and Qualcomm HTP pressure audit

Research date 2026-10-08. **PUBLIC ORIGINAL SOURCES ONLY, NO EXPERIMENTS.**

## Deep first-party anchor
- [Android17 NPU Manager](../../01-evidence/vendors/VENDOR-027/deep.md): explicit system arbitration for model load/unload, priority, driver/HAL work lifecycle; strongest new counterpressure to AO1/2 'new OS scheduler/cancel events'. Source provides interfaces, no universal retail deployment measurement.
- [AOSP burst](../../01-evidence/vendors/VENDOR-028/deep.md): same-model high-performance context, mapping cache, FMQ fast dispatch and burst lifetime; software/driver prior art for AO1/3.
- [Qualcomm QNN shared](../../01-evidence/vendors/VENDOR-029/deep.md): multiple tensor buffers, FastRPC/NPU shared memory; external spill/VTCM contexts and restrictions; reviewed indexed official technical sections (not complete SDK doc).
- [Android NNAPI migration](../../01-evidence/vendors/VENDOR-030/deep.md): NDK NNAPI deprecated Android15; vendor HAL supported; avoid mixing historical HAL prior art with future app-level recommended API.
- [AICore](../../01-evidence/vendors/VENDOR-031/deep.md): on-device models, hardware acceleration, privileged privacy/safety/request isolation, not arbitrary trusted Agent-state sharing.
- [PAPER-009 mobile CPU-NPU](../../01-evidence/papers/PAPER-009/deep.md): existing independent **actual Snapdragon8Gen3 / Hexagon v75 measurement** of backend/operator-dependent crossover and dispatch tax, plus software maturity counterargument.

## Claim / evidence
- CLM-R15C-001 OS NPU lifecycle: EC-R15C-001-A SUPPORT, 001-B SCOPE_LIMIT.
- CLM-R15C-002 shared/burst baseline: EC-R15C-002-A SUPPORT, 002-B SCOPE_LIMIT.
- CLM-R15C-003 runtime/privacy evolution: EC-R15C-003-A SUPPORT.
- CLM-R15C-004 residual Agent lifecycle: EC-R15C-004-A SUPPORT question; 004-B UNDERCUTS its inferential bridge; 004-C SCOPE_LIMIT.
- No newly fabricated CPU/uArch mechanism. AO1/2/3 remain distinct scope owners under combined Theme F.

## Technical insight
The user-visible end goal is stable: 2027–29 strategic recommendations from published literature. The new Android17 NPU Manager is not a CPU ISA or proof of independent private Agent uArch: it explicitly standardizes **model admission, foreground/background preemption, release and work start/resume/cancel status**. A future differentiator, if any, must sit *beyond* that strong public baseline in correctness-aware cross-model/engine **version/need/lifetime contract** and true physical queue/memory costs.

AOSP burst and QNN shared handles show the primitives for messaging and no-copy buffer transfers already exist with mode/format/lifetime restrictions. Their existence supports software-first system design and raises the novelty bar; it does **not** prove zero copying for every Agent state path.

AICore and CHRE emphasize trusted service boundaries; do not hand sensitive goal or private context labels to lower layers merely because a performance abstraction is attractive.

## Decision
**KEEP 3 Gate-A themes F/P/V; NARROW generic hardware story; software/platform-first; no change to A/CG-06/PT-A/C/CG-07/CG-01/R1/R2/B/R3 portfolio.** 2027–29 public-only provisional year-layer roadmap written. Full final strategic rank and patent residual claims wait next public-source round, **not any experiment**.
