+++
id = "AO-3"
type = "ARCHITECTURE_OPPORTUNITY"
record_state = "CURRENT"
title = "Persistent Agent State / Context Fabric"
opportunity_stage = "DISCOVERY"
coverage_state = "EVIDENCE_MAPPED"
priority_rank = 3
research_question = "Does long-lived, repeatedly reused and revised Agent state require a more explicit cross-engine/mobile state lifecycle than conventional cache management?"
claim_links = [
  { claim_id = "CLM-AO3-001", role = "PROBLEM_SIGNAL" },
  { claim_id = "CLM-AO3-002", role = "MECHANISM" },
  { claim_id = "CLM-AO3-003", role = "STRONG_BASELINE" },
  { claim_id = "CLM-AO3-004", role = "PRODUCT_SIGNAL" },
  { claim_id = "CLM-AO3-005", role = "PRIOR_ART_BOUNDARY" },
  { claim_id = "CLM-AO3-006", role = "OPEN_GAP" },
  { claim_id = "CLM-AO3-007", role = "ARCH_HYPOTHESIS" }
]
related_trends = ["T5", "T8"]
related_directions = ["B-residual", "R2", "CG-01", "C"]
related_capabilities = ["CAP-QUALCOMM-ORYON-FLEX-CACHE"]
related_actors = ["ACT-QUALCOMM"]
+++

# AO-3 — Persistent Agent State / Context Fabric

## Round 15A judgment
**KEEP / PRODUCT-SIGNAL BACKED, SOFTWARE-PRESSURED CO-DESIGN OPPORTUNITY — EVIDENCE_MAPPED.**

Not a standalone new-cache thesis and **not** a silicon candidate. The surviving question is whether logical Agent state and derived physical state need a more economical, version-aware, cross-engine *lifetime and handoff* contract than existing generic cache + runtime policies.

### Problem and mechanism
- **CLM-AO3-001**: [MobiMem / PAPER-103](../../../01-evidence/papers/PAPER-103/deep.md) shows profile/experience/action persistence, valid replay and CPU-only Snapdragon software benefits. [LOCAL / PAPER-104](../../../01-evidence/papers/PAPER-104/deep.md) exposes KV/adapter/version lifecycle and future-consumer demand on one 24 GB GPU.
- **CLM-AO3-002**: LOCAL, Versioned Execution and Invalidation Contracts support explicit version/provenance/dependency validity and selective reuse.

### Product signal
- **CLM-AO3-004**: [Qualcomm Oryon Flex Cache / VENDOR-022](../../../01-evidence/vendors/VENDOR-022/deep.md) is heterogeneous **CPU-core** cache sharing. [Hexagon Agentic NPU / VENDOR-023](../../../01-evidence/vendors/VENDOR-023/deep.md) increases **NPU-local** shared-memory capacity. They are separate pools, **not** public proof of a unified CPU↔NPU Agent-state coherence design.

### Software / prior-art pressure
- **CLM-AO3-003**: MobiMem validated replay; PBKV/CacheScout software reuse prediction; PLACEMEM state capsules; Invalidation Contracts and LOCAL version checks comprise the strong baseline. The sources span non-comparable setups and do not form a single implementation.
- **CLM-AO3-005**: PATENT-024 (US9626295B2) and PATENT-032 (CN121960775A) directly crowd generic cache-aware mobile migration and Agent version-aware semantic cache validity. These are prior-art boundaries, not FTO findings.

### Open gap and architecture hypothesis
- **CLM-AO3-006**: Cross-engine lifetimes, validity propagation and handoff/rebuild overhead under repeated short resume/revision remain a **credible inferential gap**, not a measured phone bottleneck.
- **CLM-AO3-007 (OPEN)**: candidate state lifetime/version descriptors, context handles, tier residency and selective preservation are hypotheses competing with stronger software-only designs.

### Negative and limiting evidence
- EC-AO3-001-B / EC-AO3-002-B limit mobile transfer;
- EC-AO3-004-B and EC-AO3-006-C prevent Qualcomm CPU-cache and NPU-shared-memory disclosures being misread as a unified cross-xPU fabric;
- **EC-AO3-006-B UNDERCUTS** EC-AO3-006-A: software capsule/version-aware managers may already provide sufficient explicit lifetime signals;
- no reviewed source establishes phone battery/thermal/end-user QoE gain or a hardware-specific unsolved cause.

## Position versus adjacent opportunities
- **AO-1:** owns *execution dispatch/synchronization/CPU↔xPU handoff*; AO-3 owns *persistent state lifetime/validity/residency economics*. They may converge; do not double-count product evidence.
- **AO-2:** owns *revision/transaction authority*. It can produce invalidation events, but AO-3 evaluates what derived state to retain/release.
- **T5 / B-residual:** established software state lifecycle and cross-tier residual research; AO-3 is a bounded architecture-opportunity synthesis object, not a new Direction.

## Outstanding public-evidence questions
1. Public CPU↔NPU/GPU state ownership/coherence details, and whether physical state must be serialized/recreated during repeated Agent phase switches.
2. Whether software version/provenance metadata plus generic shared memory/cache adequately handles fine-grained invalidation and continuation.
3. Comparable end-to-end Agent QoE, energy/bandwidth and residency data for mobile multi-engine workloads.
4. Whether AO-1/AO-2/AO-3 describe one shared execution-state fabric, rather than three separate mechanisms.

## Decision
Retain for architecture foresight as **KEEP / EVIDENCE_MAPPED**, without new Direction, score, silicon or ISA commitment. Proceed to **AO-4**.
