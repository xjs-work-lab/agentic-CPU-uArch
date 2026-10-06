# PATENT-020 — Swapping and Restoring Context-Specific Branch Predictor States on Context Switches — WO2021045811A1

## Source
- Publication/family: WO2021045811A1 / EP4025998B1
- Assignee: Microsoft Technology Licensing LLC
- Primary source: https://patents.google.com/patent/WO2021045811A1/en
- Project relevance: M3
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
Context switches can destroy or isolate trained branch-predictor state, hurting resumed-context performance.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Direct CPU microarchitectural-state relevance; not Agent-specific.

## Q3 — How crowded is this prior-art space?
State preservation across context switches is mature. This family specifically covers predictor-state retention/restore.

## Q4 — What is the control point of the independent claims?
**Partial claim review.** Verified mechanism:
context-specific branch predictor state → swap/store on context switch → restore on return.

## Q5 — What do dependent claims / embodiments add or narrow?
Not fully claim-charted; storage location/restore behavior/context handling variants need direct review.

## Q6 — Is the disclosed mechanism technically implementable/productizable?
Yes, but requires predictor-state storage/indexing and context-switch integration.

## Q7 — What do inventor / assignee / patent-family signals tell us?
Microsoft ownership signals serious systems/architecture prior art; not mobile-specific.

## Q8 — How does it overlap with Huawei / competitor public capability and our candidate?
Kills generic “preserve Agent predictor state” novelty.

## Q9 — What is background IP vs residual / foreground opportunity?
Background:
- predictor-state save/restore.

Residual:
- Agent semantics may choose **which state/context is worth preserving** better than generic task/process identity.

## Q10 — What should we do next?
- Keep as M3 Kill anchor.
- Shift M3 novelty toward selection/policy/information value.
- Require PMU/real-device evidence before any uArch recommendation.

## Decision footer
- Prior-art pressure: Very High
- Decision impact: KILL broad predictor-retention idea
- Claim-review completeness: Partial
- Open questions: exact claim variants; phone cost
- Primary patent source: link above
