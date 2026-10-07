# PATENT-005 — Dynamic Predictive Wake-up Techniques — US20170168853A1

## Source
- Publication: US20170168853A1
- Assignee: Qualcomm Inc.
- Primary source: https://patents.google.com/patent/US20170168853A1/en
- Project relevance: M2
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
A CPU sleeps while waiting for an external transfer/resource, but waking only after completion adds latency while never sleeping wastes power.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Direct CPU/mobile-power relevance; not Agent-specific.

## Q3 — How crowded is this prior-art space?
Predictive wake and low-power exit timing are mature. Broad “predict completion and wake just in time” novelty is highly crowded.

## Q4 — What is the control point of the independent claims?
**Partial claim review.** Project-relevant control point:
predicted completion time + CPU exit latency → pre-wake timing command.

## Q5 — What do dependent claims / embodiments add or narrow?
Not fully claim-charted. Embodiments cover transfer/resource timing and low-power-state wake coordination.

## Q6 — Is the disclosed mechanism technically implementable/productizable?
Yes; requires completion prediction and wake-control hooks.

## Q7 — What do inventor / assignee / patent-family signals tell us?
Qualcomm ownership is important for mobile SoC relevance.

## Q8 — How does it overlap with Huawei / competitor public capability and our candidate?
It overlaps with generic predictive wake, not our narrower **post-ready intentional release** question.

## Q9 — What is background IP vs residual / foreground opportunity?
Background:
- pre-completion predictive wake.

Residual M2:
- after dependency is physically complete, can Agent semantics justify intentional delay until LatestUsefulResume?

## Q10 — What should we do next?
- Keep as M2 Kill anchor for predictive-wake novelty.
- Preserve M2's post-ready definition.
- Complete direct claim review before final novelty statement.

## Decision footer
- Prior-art pressure: Very High
- Decision impact: KILL broad predictive wake; KEEP narrow M2
- Claim-review completeness: Partial
- Open questions: exact claim-family boundaries
- Primary patent source: link above


## 2026-10-07 claim audit completion
The prior V1 card marked claim review partial.

Current re-audit verifies claim 26 directly:
- initiate I/O transfer;
- determine/update transfer rate;
- predict time to completion;
- compare predicted remaining time with known exit latency;
- issue wake command once completion is close enough.

Claim-review status for the project-relevant predictive-wake proposition is now **DIRECT / VERIFIED**.

The narrow R1 post-ready semantic interval remains outside this claim.
