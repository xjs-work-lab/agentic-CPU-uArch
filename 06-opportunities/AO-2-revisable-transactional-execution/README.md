+++
id = "AO-2"
type = "ARCHITECTURE_OPPORTUNITY"
record_state = "CURRENT"
title = "Revisable / Transactional Agent Execution"
opportunity_stage = "DISCOVERY"
coverage_state = "EVIDENCE_MAPPED"
priority_rank = 2
research_question = "Do revision, speculation, cancellation and effect authority create a new cross-layer execution/state-management problem for mobile Agent systems?"
claim_links = [
  { claim_id = "CLM-AO2-001", role = "PROBLEM_SIGNAL" },
  { claim_id = "CLM-AO2-002", role = "MECHANISM" },
  { claim_id = "CLM-AO2-003", role = "STRONG_BASELINE" },
  { claim_id = "CLM-AO2-004", role = "PRIOR_ART_BOUNDARY" },
  { claim_id = "CLM-AO2-005", role = "STRONG_BASELINE" },
  { claim_id = "CLM-AO2-006", role = "OPEN_GAP" },
  { claim_id = "CLM-AO2-007", role = "ARCH_HYPOTHESIS" }
]
related_trends = ["T3", "T5"]
related_directions = ["PT-A", "B-residual"]
related_capabilities = []
related_actors = []
+++

# AO-2 — Revisable / Transactional Agent Execution

## Current judgment
**KEEP / HIGH-INTEREST ACADEMIC-LEAD OPPORTUNITY — EVIDENCE_MAPPED.**

The core opportunity is not to invent transactions for Agents. That space is already active in runtime research and prior art.

The research question is narrower: if speculative/revised work increasingly occupies local accelerator queues and derived state, does the cost of revocation, selective inheritance and reclamation become a cross-layer mobile architecture issue?

## Evidence skeleton

### Problem Signal
CLM-AO2-001: useful work may execute before final authority is resolved; actions can later be revised, cancelled or discarded.

Primary full-text anchors:
- PAPER-013 — speculative interaction with runtime cancellation/commit gating;
- PAPER-116 — Speculative Actions with branch validation, commit/discard and reversibility requirements.

### Mechanism
CLM-AO2-002: Agent systems are explicitly developing task-level transaction/version abstractions.

Primary full-text anchors:
- PAPER-117 Cordon — intent/result lineage, shadow state, effect outbox, delegated authority, commit/abort;
- PAPER-118 Atomix — epochs, resource scopes/frontiers, effect classes, settle/abort;
- PAPER-032 Versioned Execution — version authority and compatible-state inheritance.

### Strongest Baseline
CLM-AO2-003 and CLM-AO2-005: much of the problem is already software-capturable.

Strong software can provide:
- speculative branch control;
- versioned authority;
- task-level transaction boundaries;
- rollback/compensation;
- progress-aware settlement;
- compatible-state inheritance.

Current load-bearing limits remain software mediation, metadata correctness, opaque external effects, distributed progress and multi-endpoint irreversibility.

### Prior-Art Boundary
CLM-AO2-004: broad multi-Agent prepare/commit/rollback/snapshot/failover is already claimed prior art.

Direct-claim anchors:
- PATENT-033 CN120704926A;
- PATENT-032 version-aware Agent cache validity.

### Product Signal
**Currently insufficient as a distinct AO-2 role.**

No reviewed public mobile vendor source yet exposes a standardized Agent transaction/version/cancel architecture comparable to the academic abstractions above.

This absence is not proof that products lack internal mechanisms; it is a public-evidence gap.

### Open Gap
CLM-AO2-006: the only coherent architecture residual is below the already-strong runtime abstraction.

Question:
when revision/speculation creates local NPU/GPU/CPU queue work and derived state, does revocation/selective inheritance/resource reclamation become materially expensive or too late when mediated only by software?

Public evidence does not yet answer that question for smartphones.

### Architecture Hypothesis
CLM-AO2-007 remains OPEN.

Candidate hypotheses include:
- lightweight execution-version/epoch identifiers;
- cancellable accelerator work;
- rapid state/resource reclamation;
- selective state retirement/inheritance;
- low-overhead shadow/checkpoint assistance.

These are not silicon recommendations.

## Important negative evidence
- Cordon and Atomix solve substantial correctness semantics entirely in runtime software.
- Versioned Execution handles authority revocation and compatible KV/state inheritance in software.
- PATENT-033 crowds broad transaction/rollback/failover novelty.
- current limitations mostly point to mediation/metadata/distributed/external-effect boundaries, not CPU microarchitecture.

## Round 15A conclusion
AO-2 survives as a high-interest academic-leading Architecture Opportunity, but it is less product-validated than AO-1.

Do not promote it to a hardware Bet until public evidence shows that local execution/state revocation cost is becoming structurally important in mobile Agent workloads.

## Remaining gaps
1. mobile product signals for revision/speculation/transaction semantics;
2. measurements or architecture disclosures for accelerator cancellation and state reclamation;
3. frequency/cost of revision and speculative work in persistent personal Agents;
4. interaction with AO-3 persistent state fabric;
5. whether the same version/epoch metadata can unify AO-2 transaction semantics and AO-3 state lifecycle.