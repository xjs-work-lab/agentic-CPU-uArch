# PATENT-028 — Compiler-Based Scheduling Optimization Hints for User-Level Threads — US20070124732A1 / US8205200B2

## Source
- Publication/family: US20070124732A1 / US8205200B2
- Assignee: Intel Corp.
- Earliest priority: 2005-11-29
- Primary source: https://patents.google.com/patent/US20070124732A1/en
- Project relevance: C1
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
A compiler can know independence, locality, fusion and work characteristics that a runtime scheduler may not infer cheaply.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Not Agent-specific, but directly relevant to the broad C1 pattern of compiler-derived semantics driving runtime scheduling.

## Q3 — How crowded is this prior-art space?
Very high. This is a strong historical anchor showing compiler→runtime scheduling hints are old.

## Q4 — What is the control point of the independent claims?
**Direct claim review.**

Independent claim 1 recites:
- receiving scheduling-hint information for a user-level thread from a compiler;
- taking that information into account for dynamic runtime scheduling;
- scheduling performed by a user-space scheduler.

This directly claims the broad `compiler → scheduling hint → runtime scheduler` pattern.

## Q5 — What do dependent claims / embodiments add or narrow?
**Direct dependent-claim review.**

Relevant dependents explicitly claim:
- API/interface transfer (claim 2);
- independent-unit and fusion/dependence hints (claims 4–5);
- locality degree (claim 6);
- computation amount / hotspot (claims 7–8);
- compiler generation without user input (claim 11);
- scheduler may disregard a hint if no performance benefit (claim 12);
- locality-based same-core / nearby-core / shared-cache co-location (claims 13–16).

This is a very strong direct prior-art boundary for generic compiler/runtime hints and locality metadata.

It still does not directly claim Agent goal-demand truth or effect/commit legality.

## Q6 — Is the disclosed mechanism technically implementable/productizable?
Yes and conceptually straightforward: compiler metadata plus runtime consumption.

## Q7 — What do inventor / assignee / patent-family signals tell us?
Intel ownership and age make it foundational CPU/compiler prior art.

## Q8 — How does it overlap with Huawei / competitor public capability and our candidate?
It kills broad novelty of:
`compiler understands program → emits scheduling/locality metadata → runtime acts`.

ASEC must therefore differentiate through **Agent-native semantics and mobile value**, not the existence of the interface.

## Q9 — What is background IP vs residual / foreground opportunity?
Background:
- compiler/runtime scheduling contract;
- locality/independence/fusion hints.

Residual:
- demanded vs ready;
- commit/discardability;
- future state affinity;
- runtime-updated semantics;
- phone-specific FFRT/kernel/NPU lowering.

## Q10 — What should we do next?
- Keep as foundational C1 Kill anchor.
- Make it mandatory citation whenever C1 novelty is discussed.
- Complete direct claim chart before Stage14.

## Decision footer
- Evidence role: **BOUNDARY_BASELINE**
- Prior-art pressure: Very High
- Decision impact: KILL broad compiler→scheduler novelty; NARROW C1
- Claim-review completeness: **Direct**
- Open questions: prosecution/family evolution; no legal/FTO conclusion
- Primary patent source: link above
