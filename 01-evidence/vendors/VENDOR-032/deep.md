# VENDOR-032 — First-party product/platform Deep 10Q

Original official source: https://developer.apple.com/documentation/FoundationModels/LanguageModelSession
Reviewed: 2026-10-08
Source maturity: PRODUCT_CAPABILITY_OR_API_DISCLOSURE, not independent performance verification.
Independence: APPLE_FIRST_PARTY_PLATFORM_API

## Q1 — Problem and mobile Agent target
AO3/AO5 strong software session-state + on-device tool-control benchmark. This targets the smartphone experience and underlying runtime/chip interplay, not proof of intrinsic hardware necessity.

## Q2 — What has actually been publicly disclosed?
1. Foundation Models publicly exposes LanguageModelSession to apps on eligible Apple Intelligence devices; session accumulates transcript context between requests.
2. Session can be initialized from a transcript, prewarmed using prewarm(promptPrefix:), and uses Tool objects for invoking app-provided functions; optional DynamicProfile and history-supported APIs are beta and need version caution.
3. Session accepts at most one concurrent respond per session; transcript can exceed context size and raise an error. Thus it is a concrete state-management interface, not an unlimited concurrent Agent fabric.
4. Apple WWDC25 video chapters explicitly discuss tool calling, stateful sessions, snapshot streaming and guided structured output. June2026 release notes discuss multimodal agentic app experiences.
5. No public docs guarantee cross CPU↔GPU↔NPU persistent KV-coherent handoff, private Need/RequiredProgress ABI, or phones' 24-hour Agent energy benefit.

## Q3 — Agent-native or generic?
Software model/session/tool or proactive product value can be Agent-AMPLIFIED/NATIVE at the user level, but generic persistent contexts, hardware acceleration and tool calling are not automatically Agent-specific uArch differentiation.

## Q4 — Prior-art / competing route
Relevant stronger baselines: Android NPU Manager VENDOR-027, AICore VENDOR-031, CHRE VENDOR-024, PAPER-119/120/121 software workflow policy, and existing patent scope. Compare independent product providers without treating same SoC/vendor announcement as independent measured mechanism.

## Q5 — Technical control points
A platform/runtime-managed transcript, lifecycle, prewarming and tool abstraction are already strong reconstructible progress/state baselines, reducing generic novelty of Agent session persistence.

## Q6 — Measurements and proper denominator
No original independent apples-to-apples phone Agent experiments are present here. Official metrics must retain their chipset/model/version, internal-testing and applicability boundaries. Do not sum cross-vendor claimed percentages.

## Q7 — Reproducibility and caveat
Vendor documentation of API; no new hardware implementation or benchmark; Apple model and private cloud capabilities have product-dependent constraints. Some 2026 beta APIs may change.

## Q8 — Evidence vs analyst inference
PUBLICLY_DISCLOSED: only the listed API/feature/product design. CROSS_SOURCE_INFERENCE: market trend towards persistent, proactive on-device assistants. ARCHITECTURE_HYPOTHESIS: cross-engine state or semantic controls may still have residual value. NOT_ESTABLISHED: new CPU uArch control need or phone system energy benefit beyond strong runtime.

## Q9 — Investment decision contribution
Reinforces platform FOLLOW / BUILD and strong software-side solutions. Does not create a new Primary Bet; strengthens portfolio competitor/product coverage.

## Q10 — Next public evidence
Look for manufacturer HAL/kernel/LLVM/SDK documents and independently published task success vs energy/QoE with comparable workloads; no experiments by this project.

## First-party supplementary links
- https://developer.apple.com/videos/play/wwdc2025/286/
- https://developer.apple.com/documentation/updates/foundationmodels
- https://developer.apple.com/documentation/FoundationModels/

## Decision footer
Evidence: PLATFORM/PRODUCT_SIGNAL. Review: full named primary page and linked functional specifications where indicated. Vendor claims are not independent measurements. No hardware feature approval or legal/FTO conclusion.
