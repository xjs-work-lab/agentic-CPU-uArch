> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# PAPER-032 — Serving a Revisable World: Versioned Execution for Interruptible Agents

## Source
- Paper: https://arxiv.org/abs/2610.01160
- Authors: Yanxin Zhang, Rahul Sharma, Nitin Vegesna, Zheyu Fu, Chang Liu, Trivikram Krishnamurthy
- Venue/status: arXiv preprint, 2026-10-01
- Target: Agent serving / vLLM
- Project relevance: Candidate B validity/inheritance; Candidate A authority/commit boundary
- Priority: P0

## Q1 — Problem
Agent plans are revised while work is in flight. Obsolete execution must lose authority, but completed state that is still valid should not be thrown away.

## Q2 — Novelty / relevance
The paper introduces versioned execution:
- requests own resources;
- execution versions own authority;
- obsolete versions are revoked;
- compatible completed state may be inherited by the successor.

This is directly Agentic.

## Q3 — Falsifiable hypothesis
Coordinated invalidation + certified state inheritance beats native abort-and-cold-restart while preserving correctness.

## Q4 — Competing route
Strong direct pressure against a broad Candidate B claim that Agent revisions require a new generic versioned-state fabric.

## Q5 — Mechanism
Version authority is enforced across:
- output publication;
- GPU execution;
- KV installation/handoff;
- tiered recovery;
- reclamation.

The runtime decides the replacement; the server enforces authority and valid-state inheritance.

## Q6 — Experiment
Reported controlled paired experiment:
- native+cold TTFT ~1127 ms;
- combined invalidation + inheritance ~951 ms;
- median paired reduction **17.1%**;
- 4096 certified tokens inherited in every trial.

The paper also reports correctness tests preventing obsolete output.

## Q7 — Artifact
Implementation is described in vLLM; artifact availability should be verified before reproduction.

## Q8 — Evidence vs hypothesis
**[FACT]** Versioned validity + selective inheritance is implementable and useful in a real serving stack.

**Boundary:** server/GPU serving, not smartphone NPU/DRAM/UFS.

## Q9 — Project contribution
This kills broad novelty of semantic revision → invalidate obsolete state + preserve valid state.

Candidate B must now be mobile-specific and prove a cross-tier physical-state problem not captured by server versioned execution.

## Q10 — Next action
- KEEP as P0 negative/constraint evidence.
- Reframe B away from generic versioned execution.
- Test smartphone S0/S1→S2/S3 coherence specifically.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for server Agent versioned execution; STRUCTURAL_SIGNAL for mobile transfer
- Decision impact: NARROW / DOWNGRADE broad B
- Open questions: phone/NPU transfer; artifact
- Primary source: https://arxiv.org/abs/2610.01160
