# PAPER-064 — Sherlock: Reliable and Efficient Agentic Workflow Execution

## Source
- arXiv preprint, 2025
- https://arxiv.org/abs/2511.00330
- Authors include Microsoft Azure Research / UT Austin collaborators
- Hardware: 8× NVIDIA A100 80GB server environment
- Serving: vLLM
- Executor: Llama-3.1-Instruct-8B in the reported setup
- Benchmarks: CoTCollection, OMEGA, LiveCodeBench
- Priority: P1 because publication/peer-review status was not established in this review

## Q1 — Problem + target mapping
Agentic workflows can amplify errors: one bad intermediate result may corrupt many downstream nodes.

Verifying every node is expensive, so Sherlock asks:
- which nodes actually deserve verification;
- which verifier is cost-effective;
- how verification latency can be hidden.

Project mapping:
verification status changes whether downstream work is provisional, committable, discardable or rollback-dependent—directly relevant to PT-A effect/outcome contracts and A's B4-TX.

## Q2 — Novelty / new-regime relevance
Sherlock combines:
- counterfactual workflow analysis for vulnerability;
- selective verifier assignment;
- speculative downstream execution during verification;
- rollback/discard on verifier failure.

This is **Agent-native workflow reliability/performance co-design**, but the primitives remain software-level verification, speculation and rollback.

## Q3 — Falsifiable hypothesis
If only a subset of nodes dominate error propagation and verifier latency can overlap useful downstream work, selective verification + bounded speculation can improve reliability without paying full verification latency/cost.

Falsifiers:
- vulnerability ranking is unstable;
- verifier cost/accuracy choices transfer poorly;
- speculation frequently rolls back and wastes compute;
- downstream side effects cannot be safely undone;
- semantic similarity cannot reliably identify unaffected downstream work.

Results support the hypothesis within the evaluated server workflows.

## Q4 — Research lineage / competing route
Competing routes:
- verify every node;
- self-reflection/debate/LLM-as-judge;
- Monte-Carlo verifier selection;
- speculative actions;
- transactional workflow engines.

Compared with Speculative Actions, Sherlock focuses more on **verification-induced provisional execution** and workflow rollback than next-action prediction.

## Q5 — Key mechanism / control point
### Counterfactual vulnerability analysis
Fault injection estimates which nodes materially affect final workflow accuracy.

### Verifier selection
Nodes receive cost/accuracy-appropriate verifiers rather than uniform verification.

### Speculative downstream execution
Dependent work begins while the verifier runs.

### Rollback/discard
On verification failure:
- failed node is corrected/re-executed;
- dependent speculative results are discarded/rescheduled;
- task-specific semantic-similarity logic may preserve unaffected work where reliable.

### Budget
Speculation is bounded by verifier latency and an explicit resource/speculation budget.

## Q6 — Experiment design
Server setup:
- 8× A100 80GB;
- vLLM;
- multiple executor/verifier model choices.

Benchmarks:
- CoTCollection;
- OMEGA;
- LiveCodeBench.

Reported headline:
- +18.3% average accuracy over non-verifying baseline;
- up to 48.7% reduction in verification-related execution time depending comparison;
- 26.0% lower verification cost than compared Monte-Carlo selection method.

Detailed workflow execution-time reductions vary by benchmark and configuration; the important project fact is that speculative work/rollback is measured as an explicit system tradeoff.

## Q7 — Data / artifact / reproducibility
Strengths:
- detailed workflow and fault-injection methodology;
- multiple benchmark/task families;
- explicit executor/verifier setup;
- explicit rollback and speculation budget.

Limitations:
- preprint status;
- server GPU environment;
- no smartphone energy/QoE;
- semantic similarity is task-dependent; code/math preservation is difficult and may require full rollback.

## Q8 — Evidence vs hypothesis
### [FACT]
Sherlock treats downstream results as provisional during verification and discards/re-executes dependent work on verification failure.

### [FACT]
Verification vulnerability and speculation budget are explicitly profiled/controlled.

### [OBSERVATION]
Agent workflow state already contains enough correctness/lineage information for sophisticated software scheduling of provisional work.

### [INFERENCE — project]
Cancel/discard legality and rollback scope are strong B4-TX/PT-A baseline facts rather than unexplored lower-layer semantics.

### Not established
- mobile SYSTEM_VALUE;
- direct CPU/NPU resource management benefit;
- hardware insufficiency;
- universal verifier/rollback policy.

## Q9 — Real contribution to project decision
### PT-A
Strengthens the case for explicit OutcomeReceipt / verification state / dependency lineage / rollback scope in the platform contract.

### A
B4-TX must include:
- verifier-pending vs verified state;
- dependency/lineage-derived rollback scope;
- provisional work discardability;
- verification vulnerability/criticality where reconstructible.

### Second Bet
No new Bet. The paper further narrows cancel/discard legality as an independent direction.

## Q10 — Next action
1. KEEP as P1 strong preprint evidence.
2. Use as supporting premise for the legality/rollback Claim, but do not count it as peer-reviewed corroboration.
3. Strengthen PT-A/A baselines.
4. Preserve mobile-transfer gap.

## Decision footer
- **New-regime relevance:** Agent-native
- **Evidence maturity:** SYSTEM_VALUE in evaluated server Agent workflows; not mobile
- **Decision impact:** supports legality/rollback baseline; no portfolio promotion
- **Publication boundary:** preprint in current review
- **Open questions:** phone transfer, energy cost of rejected speculation, safe external side effects
- **Primary source:** https://arxiv.org/abs/2511.00330