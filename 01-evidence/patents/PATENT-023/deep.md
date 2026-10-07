# PATENT-023 — Cache-Aware Task Migration — US9483321B2 / EP2894565B1

## Source
- Publication/family: US9483321B2 / EP2894565B1
- Assignee: Huawei Technologies Co., Ltd.
- Primary source: https://patents.google.com/patent/US9483321B2/en
- Project relevance: M3
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
Load balancing through task migration can destroy useful cache locality and reduce performance.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Direct CPU scheduling/cache relevance and especially important because it is Huawei prior art. Not Agent-specific.

## Q3 — How crowded is this prior-art space?
Cache-aware migration is mature and highly crowded.

## Q4 — What is the control point of the independent claims?
**Direct claim review — VERIFIED.** Project-relevant mechanism:
cache-miss/instruction/cache-behavior information + source/destination load/state → choose migration candidate/target.

## Q5 — What do dependent claims / embodiments add or narrow?
Not yet fully claim-charted; likely variants in cache metrics, load thresholds and migration selection.

## Q6 — Is the disclosed mechanism technically implementable/productizable?
Yes at OS/runtime scheduling layer with PMU/cache metrics.

## Q7 — What do inventor / assignee / patent-family signals tell us?
Huawei ownership strongly constrains any proposal framed as “cache-aware Agent migration.”

## Q8 — How does it overlap with Huawei / competitor public capability and our candidate?
Strong overlap with history/PMU-based cache-aware placement.
M3 must beat this with future-state semantics, not repeat it.

## Q9 — What is background IP vs residual / foreground opportunity?
Background:
- cache/MPKI/load-aware migration.

Residual:
- future Agent StateAffinity/reuse horizon as predictive information beyond observed history.

## Q10 — What should we do next?
- Keep as P0 M3 baseline/kill anchor.
- Compare StateAffinity oracle against history/PMU affinity.
- Claim-chart before final novelty wording.

## Decision footer
- Prior-art pressure: Very High
- Decision impact: KILL broad cache-aware migration; KEEP semantic-selection hypothesis
- Claim-review completeness: Direct / VERIFIED
- Open questions: exact independent-claim scope
- Primary patent source: link above
