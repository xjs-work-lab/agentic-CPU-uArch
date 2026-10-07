# PAPER-013 — Speculative Interaction Agents — EDP v1 FULL_10Q

Re-reviewed: 2026-10-07

## Q1 — Problem + target mapping
Interactive Agents block on streaming user input and long tool calls. The paper asks whether reasoning and safe work can begin before all input arrives.

For A this directly tests whether executable/ready work can exist before it is certainly required.

## Q2 — Novelty / new-regime relevance
Mechanism:
- asynchronous user/environment updates;
- interruptible event-driven Agent loop;
- speculative tool issue;
- call modification/removal by ID;
- dependency cancellation;
- commit gating for unsafe state-changing tools.

Classification: Agent-native runtime semantics.

## Q3 — Falsifiable hypothesis
If future work can be safely started before full intent resolution, latency should fall without materially changing outcome quality, provided invalid speculative work can be cancelled/discarded and unsafe effects do not publish early.

## Q4 — Research lineage / competing route
Berkeley-led systems/ML group; independent from PARE / ProactiveAgent / ProAgentBench / TomasuLLM.

Competing/neighboring routes:
- ordinary synchronous ReAct;
- parallel tool dispatch;
- later runtime transaction/sandbox systems such as Cordon and TomasuLLM;
- Speculative Actions.

## Q5 — Mechanism / control point
Tools are manually divided into safe vs unsafe speculative execution classes.
Read-only/safe calls may execute before the user's final input.
Unsafe/state-changing tools may be planned but are held until a commit point.

A speculative call may be overwritten or removed.
If a completed speculative observation is invalidated before insertion, it is discarded; dependent calls are cancelled.

Commit occurs after final query arrival plus an indication that call edits are complete.

Important implication:
safe/unsafe, active/cancelled, dependency and commit state are **runtime-visible** in this design.

## Q6 — Experiment design + results
Benchmarks:
- HotpotQA;
- TinyAgent.

3B SI-SFT vs normal-SFT:

Qwen2.5-3B:
- HotpotQA: 68.6 accuracy / 2.7 s → 67.5 / 1.2 s (2.2×)
- TinyAgent: 65.6 / 4.1 s → 62.1 / 2.5 s (1.6×)

Llama-3.2-3B:
- HotpotQA: 70.4 / 2.3 s → 68.7 / 1.1 s (2.1×)
- TinyAgent: 66.8 / 5.0 s → 65.2 / 2.5 s (2.0×)

Cloud OpenAI Realtime results report 1.3–1.7× speedups with minor accuracy loss.

Negative transfer:
on Human Instructions,
- Qwen normal SFT: 22.0 accuracy / 9.3 s;
- Qwen SI-SFT: 13.6 / 14.3 s;
- Llama normal SFT: 19.2 / 5.6 s;
- Llama SI-SFT: 15.3 / 9.3 s.

The paper attributes this to degenerate/repeated-action behavior under more natural streaming input.

## Q7 — Artifact / reproducibility
Primary paper is public.
The method is sufficiently specified to reconstruct the task manager semantics.
Current audit does not establish a mature end-to-end production artifact.

Latency evaluation uses simulated arrival timing / benchmark tool delays, not smartphone system energy/thermal measurements.

## Q8 — Evidence vs alternatives
Demonstrated:
- ready/executable speculative work can exist before final user intent;
- runtime cancellation/discard/commit can preserve benchmark quality while hiding latency.

Also demonstrated:
- the strategy does not robustly transfer to harder naturalistic instructions.

Not demonstrated:
- explicit DemandState must be exported to OS/CPU;
- phone foreground QoE/energy benefit;
- hardware insufficiency.

## Q9 — Decision contribution
Supports CLM-AGENT-001.

But it narrows A:
the paper's own runtime already maintains much of the speculation/commit state.
Therefore A cannot claim differentiation from the mere existence of speculative/discardable work.

The surviving differentiated variable remains:
**RequiredProgress / DemandState information that the strongest runtime/history/topology baseline cannot reconstruct.**

## Q10 — Next action
KEEP as A structural evidence and B4-TX pressure.

EXP-A-001 must include:
- speculative/cancel/discard state in the baseline;
- hard naturalistic streaming cases;
- no credit for semantics already exposed by the Agent runtime.

## Decision footer
- Evidence maturity: STRUCTURAL_SIGNAL
- Decision impact: KEEP / NARROW A to residual DemandState
- Open questions: real-phone cost, naturalistic robustness, conditional information value beyond runtime state
- Primary source: https://arxiv.org/abs/2605.13360
