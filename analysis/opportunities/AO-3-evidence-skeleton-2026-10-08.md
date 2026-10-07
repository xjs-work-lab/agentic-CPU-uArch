# Round 15A — AO-3 Evidence Skeleton Audit

Date: 2026-10-08
Coverage: EVIDENCE_MAPPED (3 of 5)

## Question
Do persistent/reused/revised Agent state and heterogeneous SoC residency create a distinct mobile architecture opportunity after software-baseline and patent pressure?

## Primary sources and review depth
- PAPER-103 / MobiMem — existing FULL_10Q reused, primary HTML Sections 4–7 cross-checked: https://arxiv.org/html/2512.15784
- PAPER-104 / LOCAL — existing FULL_10Q reused; versioning, staged publication and cross-Agent pre-prefill: https://arxiv.org/abs/2608.15241
- PAPER-032 / Versioned Execution — previously FULL_10Q.
- PAPER-028 / PBKV, PAPER-031 / CacheScout, PAPER-034 / PLACEMEM, PAPER-035 / Invalidation Contracts — existing FULL_10Q software pressure set.
- VENDOR-022 / Oryon Flex Cache — **new official deep vendor card**, primary: https://www.qualcomm.com/news/onq/2026/08/oryon-cpu-5ghz-flexcache
- VENDOR-023 / Hexagon Agentic NPU — existing deep vendor card, primary: https://www.qualcomm.com/news/onq/2026/09/hexagon-npu-agentic-ai-architecture
- PATENT-024 / US9626295B2 and PATENT-032 / CN121960775A — **previous direct independent/dependent claim audits reused**, no new patent claim review claimed.

## Evidence role matrix
| Role | Canonical claim | Most important source / caveat |
|---|---|---|
| Problem | CLM-AO3-001 | MobiMem mobile memory; LOCAL single-GPU KV lifecycle |
| Mechanism | CLM-AO3-002 | LOCAL adapter-version validity; Versioned Execution; Invalidation Contracts |
| Product | CLM-AO3-004 | Qualcomm Flex Cache is **CPU-only shared pool**; Hexagon NPU pool is **NPU-local** |
| Strongest baseline | CLM-AO3-003 | MobiMem replay, PBKV, CacheScout, PLACEMEM, LOCAL, software invalidation |
| Prior art | CLM-AO3-005 | PATENT-024 cache-aware mobile cluster migration, PATENT-032 semantic/version Agent caches |
| Open gap | CLM-AO3-006 | Cross-engine physical derived-state lifecycle is plausible, unmeasured in phones |
| Architecture hypothesis | CLM-AO3-007 | OPEN: lightweight state descriptors/handles/residency/invalidation support |

## Cross-source result
MobiMem's strongest Snapdragon result is **CPU-only**, with highest 77.3% action reuse depending on human-crafted templates. LOCAL measures a **24GB discrete GPU**, not a smartphone SoC. Together they demonstrate persistent-state and version-lifecycle value without proving a specialized mobile cross-xPU hardware fabric.

Qualcomm's Oryon Flex Cache and Hexagon NPU disclosures demonstrate two different product trends. Their juxtaposition is an analyst observation, **not evidence that either vendor provides a coherent CPU↔NPU Agent state interface**.

## Direct technical inference and counterpressure
**Retain:** repeated Agent state reuse/revision across short-lived CPU/NPU/GPU phases may make residency, version propagation, (re)materialization and reclamation central to mobile QoE/bandwidth/energy.

**Undercut:** software version/provenance capsules and version-aware KV managers may carry the necessary information; cross-engine transport could be generic shared memory/coherent cache rather than a novel Agent-specific primitive.

**Kill broad novelty:** "Agent memory", generic shared cache, semantic cache-version tags, generic migration optimization or cache manager as standalone architecture bets.

**Do not kill:** bounded architectural investigation of physical state lifetime/handoff after strongest software capture.

## Decision
AO-3: **KEEP / EVIDENCE_MAPPED / PRODUCT-SIGNAL BACKED, SOFTWARE-PRESSURED CO-DESIGN OPPORTUNITY**.
No new Direction, score, uArch candidate or experiment demand.
Next: AO-4 — Always-On Proactive Front-End.
