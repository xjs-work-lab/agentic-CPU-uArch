# Round15D — Claims-level Patent Boundaries × Apple/Google/Samsung Product Uptake × Portfolio

Date: 2026-10-08
Study method: **public original patents, vendor documents and prior deep-read published results only; NO experiment/PoC.**
Status: **PRE-DECISION PORTFOLIO SYNTHESIS**, canonical investment lanes and numbers remain unchanged this round.

## One-page finding
1. Multiple device ecosystems publicly expose **stateful personal models, proactive assistance and tool/context flows** (Apple Foundation Models VENDOR-032, Google Pixel10 VENDOR-033, Samsung Galaxy S26 VENDOR-034).
2. Claims-level prior art covers generic scheduling based on cache load (PATENT-024), Agent **demand-satisfaction+business-version** memory validity (PATENT-032), and Agent prepare/commit/snapshot/rollback/replacement (PATENT-033). See each canonical patent's [claims-round15d.md](../../01-evidence/patents/PATENT-032/claims-round15d.md) addendum.
3. This increases evidence that CPU/runtime/LLVM heterogeneous orchestration and trusted platform actuation are valuable; it **does not** show a distinct processor semantic ISA, private NeedStatus interface or unified CPU↔GPU↔NPU Agent coherence hardware.
4. Source independence: Google Pixel Tensor and Apple framework represent two independent ecosystems; Samsung OEM Galaxy S26 Ultra uses Snapdragon 8 Elite Gen5, **not** a third independent chip architecture. Samsung+Qualcomm are not two independent silicon confirmations. No percentage gains combined.

## Direct patent claim audit / three nonidentical scopes
| Existing canonical ID | Claim scope checked (2026-10-08) | Broad novelty crowded | Deliberate non-overlap / public-evidence gap |
|---|---|---|---|
| [PATENT-024](../../01-evidence/patents/PATENT-024/claims-round15d.md) US9626295B2 | Independent 1/6/12/17 weighted CPU load+cache demand→cluster migration; dependent 23 smartphone/tablet | Generic cache-aware mobile heterogeneous CPU-cluster migration; shared cache-demand metrics | Does not directly claim Agent semantic release/commit or cross CPU↔NPU version-coherent KV. Google Patents lists expired-fee-related status (not legal/FTO opinion) |
| [PATENT-032](../../01-evidence/patents/PATENT-032/claims-round15d.md) CN121960775A | Independent 1+8/10; dependent 2–5 semantic two-layer caching, identity/time/service version, demand fulfillment, intent chain | Broad Agent semantic history/reasoning cache validity and current-demand grading | 'Demand satisfied by cached response' ≠ private internal RequiredProgress for OS. Application pending, not granted |
| [PATENT-033](../../01-evidence/patents/PATENT-033/claims-round15d.md) CN120704926A | Independent 1, dependent 2,4,5,6,7; master coordinator atomic tasks→prepare/rollback/snapshots/handoffs | Broad multi-Agent transaction rollback, recovery, failover state migration | No direct claim to reclaim physical NPU work queues or CPU microarchitectural state. Pending application |

**Patent methodological limit:** three publications are targeted prior-art examples, **not exhaustive patent landscaping or legal/FTO clearance**. Claims are not necessarily enforced or representative of shipped silicon.

## Vendor source truth table
| First party | Public feature/APIs | Agent work/load signal | Why NOT an independent new silicon proof |
|---|---|---|---|
| [Apple VENDOR-032](../../01-evidence/vendors/VENDOR-032/deep.md) | LanguageModelSession accumulated transcript, prewarm, Tool calls and transcript restoration; WWDC2025; June2026 optional dynamic profiles | Stateful local sessions/tools in real mobile app ecosystem | Mostly an **app/runtime API**, no physical cross-NPU version-coherent cache contract |
| [Google VENDOR-033](../../01-evidence/vendors/VENDOR-033/deep.md) | Pixel10 Tensor G5/Gemini Nano, Magic Cue, Voice Translate, Call Notes actions | On-device proactive assistance and model/SoC codevelopment are product real | Internal Google claimed TPU/CPU/model percent deltas; target agent end-user energy not isolated |
| [Samsung VENDOR-034](../../01-evidence/vendors/VENDOR-034/deep.md) | Galaxy S26 Agentic experience + Gemini integration; S26 Ultra Snapdragon SoC | Multiple OEMs pushing Agent use cases | Samsung device vendor plus Qualcomm silicon is not two independent implementations; no Agent-ISA claim |

## Differentiation/portfolio pressure matrix — NOT a hidden rescore

| Control hypothesis / existing direction | Product value | Agent native vs generic | Stronger public baseline / prior art | Current Gate-A public-source verdict |
|---|---|---|---|---|
| **PT-A** verified Agent actions and authority | **HIGH** — tool/phone workflows, app permissions | Native correct action & user intent | Apple Tools + Android AppFunctions VENDOR-020, Cordon/PAPER-117 | **PLATFORM_BUILD / priority 1**, strong system correctness; differentiation at trust/outcome contract, not silicon |
| **CG-06** latency-critical CPU fast path + LLVM/AArch64 | **HIGH** CPU remains orchestration and fallback path | Agent-amplified | PAPER-009 actual phone but optimized NPU/kernel maturity alternative; Android NPU manager | **ENGINEERING_INVEST / priority 1**, work on portable compilation/operator/placement; do not claim NPU inherently inferior |
| **C** QoE-aware heterogeneous runtime/OS control | **HIGH** multi model/task QoE/foreground | Generic enabling but Agent-amplified | Android NPU manager, ProgRouter, LAS, SMetric, HeRo | **PLATFORM_BUILD / priority 1**, not a second differentiated Bet |
| **A** private Goal/Need RequiredProgress over B4-TX | Potentially high, conditional | Possibly native *if* private state exists | Apple session transcript, runtime ledger, ProgRouter, ReUA/utility and PATENT-032 demand assessment | **CONDITIONAL DIFFERENTIATION WATCH**. Existing canonical PRIMARY_BET/82.5 remains a historical provisional lane; **not yet public-proof-validated Bet / not a hardware investment** |
| **Theme F AO1/2/3 / B-residual R2** | MEDIUM–HIGH potential | Amplified via short frequent resume/cancel | Android17 NPU manager, QNN buffers, AOSP burst, patents 024/032/033, LOCAL | **STRATEGIC_RESERVE** — only cross-version derived-state physical lifecycle residual survives |
| **CG-07 / Theme P AO4** | HIGH prospective proactive UX | Native/adaptive event intake | Apple AOP, CHRE, PRPF, Qualcomm/MediaTek; Google Pixel + Samsung proactive launches | **FOLLOW/EXPLORE**, hardware differentiation LOW CONFIDENCE; do not rebrand always-on NPU |
| **CG-01** Flex Cache | MEDIUM CPU continuity | Generic CPU locality | Qualcomm official Flex Cache VENDOR-001; PATENT-024 generic cache migration | **BENCHMARK_PUBLICLY/FOLLOW** and competitor-adapt; not independent Agent cache silicon novelty |
| **R1** semantic release timing | CONDITIONAL | Agent-amplified | Older utility models, ready/release scheduling + ProgRouter | **RESERVE** after strongest software QoE and knowledge of user need |
| **R3** Agent semantic ISA hints | LOW demonstrated | Unproven | Existing framework/OS control and 2004 utility prior art | **KILL/BLOCKED** until independently published hardware-specific advantage; none currently |

## Strategic conclusions
- **BET/BUILD:** platform and CPU/compiler heterogeneous execution direction, with clear technical ownership, is highest-confidence action from public primary evidence.
- **Primary differentiated novelty:** A is still the leading **research hypothesis**, but is NOT equivalent to a proven, budget-ready new hardware feature; preserve canonical lane pending a transparent formal rescore/cutover to avoid SSOT conflict.
- **RESERVE:** versioned cross-engine physical state/rollback and special timing value survive as hypotheses, not generic transaction/cache control.
- **KILL broad novelty:** NPU-work priority/cancellation callbacks, zero-copy buffer, generic cache-demand migration, 'Agent demand satisfaction cache', coordinator transaction rollback, semantic task utility/dynamic routing, extra always-on domain by itself.
- **Do not fill a 2–3 Primary-Bets quota artificially**, and do not count vendor press release uplift as end-to-end Agent CPU-uArch benefit.

## 2027–2029 portfolio interpretation
2027: **portable LLVM/CPU execution, OS/NPU runtime interfaces, safe tool/Agent actuation and stateful session access**, based on public vendor APIs and mobile published measurements.
2028: **selective reuse and version/effect-authority interop, user-QoE-aware workflow policies, product privacy and context escalation**. Inspect OEM product API uptake and evidence published to date; no experiments.
2029: **architecture option positioning** for cross-xPU derived-state lifetime and secure semantic progress only if public literature/vendor convergence supports more than generic software. No specific ISA/queue block promised.

## Gap to leadership-ready final
1. Formal reconciliation of **existing A=82.5 PRIMARY_BET** versus strongly conditioned public evidence; do not silently reinterpret the SSOT score as empirical probability.
2. Stronger independent mobile power/performance/QoE evidence of product follow-up; software baselines and patents clearly tabulated now.
3. Evidence-weighted final **3–5 trends, 3 themes, 1–2 supported primary bets (if justified), reserves and Kill**; reframe work by technical ownership and public-evidence confidence, not fabricated data.
4. Refresh `09-roadmap/current.md` and canonical direction frontmatter **only when final public portfolio cutover approved**, never change scores via an analysis note alone.
