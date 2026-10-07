# PAPER-032 — Serving a Revisable World — FULL_10Q

## Source
- Primary: https://arxiv.org/abs/2610.01160
- Submitted: 2026-10-01
- Review: FULL_10Q / EDP v1
- Priority: P0

## Q1 — Problem
Agent revisions must stop obsolete work from affecting the result while retaining already-computed state that is still valid.

## Q2 — Relevance
Versioned execution separates resource ownership from execution-version authority; obsolete versions are revoked and compatible completed state may be inherited.

## Q3 — Hypothesis
Coordinated invalidation + compatible-state inheritance should beat abort-and-cold-restart while preserving correctness.

## Q4 — Strongest baseline
Abort old request, submit replacement and rebuild state.

For B-residual, version/authority/provenance handling is now a strong generic baseline.

## Q5 — Mechanism
Version authority spans output publication, GPU execution, KV handoff/installation, tiered recovery, distributed/multi-tenant paths and asynchronous reclamation.

## Q6 — Experiment
Reported:
- correctness tests preventing obsolete output and preserving valid state;
- median 17.1% reduction in revision-to-successor TTFT with combined invalidation + inheritance;
- repeated interruption replay with no obsolete output and continued progress of final versions.

## Q7 — Limitations
Implemented in vLLM/server GPU setting; no smartphone NPU/DRAM/UFS, battery, thermal or foreground-QoE evaluation.

## Q8 — Evidence
FACT: versioned Agent execution can revoke obsolete authority while preserving compatible state.
FACT: mechanism includes KV/state installation.
INFERENCE: version/authority/inheritance alone are not B-residual novelty.
NOT ESTABLISHED: generic version/provenance is always sufficient for phone S2/S3 artifact validity.

## Q9 — Project decision
Raises B4-safe-generic materially. B-residual survives only if semantic/workflow lineage adds target-phone information beyond compatibility/version certification.

## Q10 — Next
EXP-BR-001 should test that narrow residual.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for server Agent versioned execution
- Phone transfer: STRUCTURAL_SIGNAL
- Primary source: https://arxiv.org/abs/2610.01160
