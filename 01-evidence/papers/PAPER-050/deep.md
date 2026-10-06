> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-050 — TomasuLLM: Out-of-Order Speculative Execution for LLM Agents

## Source
- Paper: https://arxiv.org/abs/2609.38201
- Authors: Jiangnan Yu, Ceyu Xu, Mengming Li, Shiyu Huang, Yiran Xia, Jian Weng, Hui Xue, Haohui Mai, Yuan Xie
- Venue/status: arXiv preprint, 2026-09-22
- Target: tool-using LLM Agent runtime
- Project relevance: A / C1 Effect-Commit baseline; PT-A speculative execution
- Priority: P0

## Q1 — Problem + target mapping
Long-running tool calls create large observation stalls. A runtime would like to execute future Agent actions early, but speculative work must not publish effects that diverge from serial committed execution.

This maps directly to Candidate A's Effect/Commit legality boundary.

## Q2 — Novelty / new-regime relevance
TomasuLLM applies out-of-order/speculative execution ideas to Agent tool trajectories:
- draft future actions;
- execute in private copy-on-write sandboxes;
- trace dependencies and effects;
- validate against committed state;
- commit only in trajectory order.

The Agent regime makes the mechanism relevant because actions can have stateful external consequences.

## Q3 — Falsifiable hypothesis
Dependency/effect-aware runtime validation can safely exploit tool-call latency without requiring speculative results to become visible before correctness is established.

## Q4 — Research lineage / competing route
Strong competing route for the project's previous assumption that Effect/Commit Safety must be an Agent-supplied semantic truth.

Related route:
- Cordon semantic transactions;
- speculative Agent action systems;
- sandbox/transaction runtimes.

## Q5 — Mechanism / control point
Inputs:
- current committed trajectory;
- drafted future action;
- tool schema/wrapper;
- read/version dependencies;
- produced observations;
- candidate effects.

Actuators:
- sandbox issue;
- hold;
- validate;
- discard;
- in-order commit.

Important boundary:
the predictor proposes work, but **runtime validation**, not prediction, authorizes publication.

## Q6 — Experiment
Reported:
- 100 SWE-bench Verified tasks: 1.31x;
- 28 Terminal-Bench 2.0 tasks: 1.35x;
- 18 SWE-Marathon sessions: 1.27x matched progress;
- 4,010 audited commit-validation records with zero false accepts.

## Q7 — Artifact / reproducibility
Public arXiv paper available.
Artifact/code availability was not established in this round.

## Q8 — Evidence vs hypothesis
**[FACT]** A runtime can derive and verify substantial effect/dependency legality from execution artifacts and wrappers without treating model rationale as the safety oracle.

**[BOUNDARY]**
Coding/tool Agents differ from phone proactive Agents, and the paper does not infer **DemandState** (required/optional/speculative goal value).

## Q9 — Decision contribution
Materially narrows Candidate A / C1.

Old differentiated framing:
> hard-to-infer DemandState + Effect/Commit legality.

Updated pressure:
- **DemandState remains Agent-native differentiated information.**
- Effect/Commit legality should be treated as a **strong runtime-derived safety baseline** wherever transaction/sandbox/lineage machinery can expose it.
- A may still consume Effect/Commit state, but should not claim that its existence must come from a new Agent semantic ABI.

This strengthens the B4 legality baseline and makes A more dependent on proving residual DemandState value.

## Q10 — Next action
- KEEP as P0 negative/constraint evidence.
- Add a B4-TX baseline with runtime-derived legality.
- Re-score A based on DemandState residual, not joint Demand+Effect semantics.
- Keep transactional speculation in PT-A/platform infrastructure, not as a new Primary Bet.

## Decision footer
- Evidence maturity: SYSTEM_VALUE for tool-Agent runtime; indirect for smartphone transfer
- Decision impact: NARROW A/C1; strengthen generic legality baseline
- Open questions: phone effect surfaces; cost of transactional containment; DemandState residual
- Primary source: https://arxiv.org/abs/2609.38201
