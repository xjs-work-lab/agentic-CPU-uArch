> V1 semantic source copied/repacked from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.
> Do not reinterpret this page as V2.2 metadata authority; the compact README owns the Source object.

# PAPER-015 — Proactive Agent Research Environment (PARE)

## Source
- Paper: https://arxiv.org/abs/2604.00842
- Authors: Deepak Nathani, Cheng Zhang, Chang Huan, Jiaming Shan, Yinfei Yang, Alkesh Patel, Zhe Gan, William Yang Wang, Michael Saxon, Xin Eric Wang
- Venue/status: arXiv preprint, 2026
- Artifact: https://github.com/deepakn97/pare
- Project relevance: W5 / M4 / C1 semantic ground truth
- Priority: P0

## Q1 — What problem is the paper solving, and how does it map to smartphones?
Proactive assistants must decide when to observe, intervene and execute without explicit user prompts. PARE creates a controlled environment to evaluate such behavior.

It is a simulated stateful mobile-phone environment, not real phone CPU execution.

## Q2 — Is the problem/new mechanism actually new?
Proactive user assistance and intervention timing are **Agentic-native** compared with ordinary request-response inference.

## Q3 — What falsifiable hypothesis is being tested?
The benchmark enables testing whether Agents can correctly infer when action is warranted and whether proposed interventions are useful/safe.

For our project, a derived hypothesis is:
Agent runtime can expose useful proactive/speculative/discardable labels unavailable to CPU traces alone.

## Q4 — What is the research lineage / competing route?
Related to proactive assistants, contextual agents, user simulation and event-driven agents.

## Q5 — What is the key technical mechanism / control point?
Observe → decide/confirm → execute semantics with explicit proactive labels in a stateful environment.

## Q6 — How is the experiment designed?
143 benchmark scenarios in a simulated mobile-phone environment with stateful interactions and proactive actions.

The main experiment uses:
- GPT-5-mini as user simulator;
- maximum 10 turns;
- 1 user iteration / turn;
- up to 5 Observe iterations and 10 Execute iterations;
- same model for Observe and Execute.

The paper reports Proposal Rate, Acceptance Rate and read-only actions, and Appendix analysis further splits proposal outcomes into:
- direct accept;
- reject;
- gather more context;
- truncated.

For frontier models, direct proposal outcome examples are:
- Claude 4.5 Sonnet: 72.1% accept / 7.8% reject / 17.8% gather / 2.3% truncated;
- GPT-5: 64.1% accept / 7.4% reject / 23.4% gather / 5.1% truncated.

These are model-behavior statistics under PARE, not workload invariants.

## Q7 — What data/artifact/reproducibility support exists?
Strong for offline analysis: official public repository and benchmark environment.

## Q8 — Do the results actually support the hypothesis?
PARE strongly supports the **semantic existence** of:
- Observe / read-only state;
- AwaitingConfirmation / not-yet-authorized state;
- Execute / state-changing authorized state.

A Stage12E derived replay using paper-reported proposal/outcome rates finds that frontier-model proposals which are not immediately accepted occupy only about **3.6–10.1% of total turns**.

**[INFERENCE]** This is enough to validate the semantic distinction, but not enough by itself to prove large cross-layer system value.

Boundary: PARE does not speculatively execute the effectful branch before approval and cannot establish mobile CPU timing, energy, jank or uArch effects.

## Q9 — What is the real contribution / technology control point for us?
PARE is a strong source for **semantic ground truth**:
- proactive vs reactive;
- read-only vs state-changing effects;
- not-yet-authorized vs demanded execution;
- explicit confirmation/commit boundary;
- premature intervention / gather-context state.

This materially strengthens **DemandState + Effect/Commit Safety** as ASEC semantic candidates.

However it also narrows the system claim:
the semantic boundary is already enforced inside the Agent runtime in PARE. A phone-wide ASEC only adds value if lower layers have useful release/cancel/defer/progress actuators that cannot act safely without this information.

## Q10 — What should we do next?
- Keep as Stage12 W5 / C1 P0.
- Use its mode/proposal outcomes as semantic ground truth, not timing ground truth.
- Include proposal-rate × outcome-rate bands in device-free replay.
- Test whether affected work is expensive/frequent enough to clear C1 break-even.
- Never promote simulated timing to SYSTEM_VALUE.

## Decision footer
- Evidence maturity: STRUCTURAL_SIGNAL
- Decision impact: KEEP as semantic/workload source
- Open questions: mapping to real-device timing
- Primary source: paper above
- Artifact: official repo above
