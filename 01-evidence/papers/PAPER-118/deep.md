# PAPER-118 — Atomix — FULL_10Q

## Q1 — Problem + target mapping
Tool return is often treated as if the operation is safe to settle immediately. Under faults, contention or speculative branches, this can leak partial effects, stale writes or irreversible actions.

AO-2 mapping: progress-aware authority to make effects final.

## Q2 — New-regime relevance
Agent-native / Agent-amplified. The runtime must know both which effects belong together and whether earlier conflicting work can still arrive.

## Q3 — Falsifiable hypothesis
Separating execute from settle, then gating commit by per-resource progress frontiers, should improve clean recovery and isolation without large tool-path overhead.

## Q4 — Strongest baselines
The paper compares or discusses no transaction, Saga/compensation, checkpoint/replay, mutex/workflow locking and TCC-style transaction coordination. Several strong baselines tie Atomix in selected correctness regimes but differ in integration burden, waiting/rejection or irreversible-effect behavior.

## Q5 — Mechanism / control point
Core objects: Epoch, Scope, Effect metadata, per-resource Frontier and Transaction.
Lifecycle: execute, seal footprint, frontier-check, commit/abort, settle.
Effect classes: bufferable, reversible-eager and irreversible-gated.
Under speculation each branch is a transaction; chosen branch commits and losers abort.

## Q6 — Experiment design + results
Workloads include tau-bench retail, WebArena, OSWorld, multi-Agent tau-bench and controlled contention/fault stress.

Reported anchors include strong clean-recovery improvements, zero leaked correctly classified irreversible sends in a 500-trial test for full Atomix, and microsecond-scale wrapper overhead relative to tool latency.

A critical negative result is that under-specified scopes/metadata can violate invariants, while wrong effect classification can leak effects.

## Q7 — Artifact / limitations
Single-process Python runtime plus adapters and public artifacts. Adapter bypass escapes the boundary. Correctness depends on accurate metadata. Frontier advancement is an orchestrator/runtime contract. No full distributed crash-safe exactly-once deployment. Multiple unrelated irreversible endpoints may need tool-side transaction support. No mobile SoC evaluation.

## Q8 — Evidence vs hypothesis
FACT: progress-aware effect settlement is implementable in software.
FACT: epoch/frontier semantics matter under speculation and contention.
FACT: runtime metadata quality is load-bearing.
NOT ESTABLISHED: hardware epoch/version support, accelerator cancellation cost, or mobile system value.

## Q9 — Decision contribution
Very strong AO-2 MECHANISM and STRONG_BASELINE evidence. Atomix shows epoch/frontier/commit semantics can live entirely in the Agent runtime.

## Q10 — Next action
Use with Cordon and Versioned Execution to define the strongest software transaction baseline before proposing hardware assistance.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for evaluated Agent runtime
- Decision impact: KEEP AO-2 but narrow hardware hypothesis
- Open questions: lower-layer state, accelerator cancellation, mobile effect economics
- Primary source: https://arxiv.org/abs/2602.14849