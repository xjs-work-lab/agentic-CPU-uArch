# PAPER-035 — Invalidation Contracts for Cross-Episode Agent Memory — FULL_10Q

## Q1 — Problem
Agents may reuse recovery suggestions learned in prior episodes, but server-side schema/data drift can silently make those memories stale.

## Q2 — New-regime relevance
Persistent cross-episode Agent memory needs explicit validity semantics when external dependencies evolve.

## Q3 — Hypothesis
Version and dependency contracts can invalidate only stale memories while preserving valid reuse.

## Q4 — Baseline
Re-derive on every episode, broad/table-level invalidation, or reuse without fine-grained validity metadata.

## Q5 — Mechanism
Protocol attaches:
- version stamps;
- cacheability hints;
- dependency vectors/scopes;
- fine-grained invalidation information.

The paper separates:
- validity — whether cached information remains correct;
- compliance — whether the planner applies it.

## Q6 — Experiment
Across seven models, three serving paths, two domains and ~9,400 episodes:
- row-level invalidation raises compliance by 0–66.7 percentage points depending on model;
- gains of 55.6–66.7 points appear on three models;
- 29–33% of baseline token cost is recovered on four of seven models;
- table-level invalidation can destroy useful co-located entries;
- row-level oracle eviction precision is 1.00;
- contract payload adds 15%;
- version-stamp validity is deterministic and reports zero contract failures across the evaluation.

## Q7 — Limitations
Application/protocol memory, not smartphone physical artifacts.
No phone KV/NPU/DRAM/UFS experiment.
Planner compliance varies strongly by model, so protocol correctness does not guarantee behavioral adoption.

## Q8 — Evidence
FACT: version/dependency validity can be made deterministic in a software protocol.
FACT: finer invalidation can preserve useful reuse versus broad eviction.
INFERENCE: broad semantic/version invalidation is not B-residual novelty.
NOT ESTABLISHED: phone-derived artifacts are fully expressible by this protocol state.

## Q9 — Project decision
Raises B4-safe-generic for correctness/validity and further narrows B-residual.

## Q10 — Next
Only target-phone evidence for unmodeled physical-artifact lineage can justify keeping/promoting the residual.

## Decision footer
- strong protocol-level validity evidence
- no target-phone SYSTEM_VALUE
- no score or maturity promotion
