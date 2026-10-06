# PATENT-021 — Mechanism to Save and Restore Cache and Translation Trace for Fast Context Switch — US7634642B2

## Source
- Publication: US7634642B2
- Assignee: IBM
- Primary source: https://patents.google.com/patent/US7634642B2/en
- Project relevance: M3
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
A resumed context suffers cold TLB/cache/page-table state after context switching.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Direct CPU locality/context-switch relevance; generic, not Agent-specific.

## Q3 — How crowded is this prior-art space?
Very high. Warm-state restore/prefetch is long-standing architecture prior art.

## Q4 — What is the control point of the independent claims?
**Partial claim review.** Verified mechanism:
record execution/cache/translation footprint before switch → preload/restore relevant state when context returns.

## Q5 — What do dependent claims / embodiments add or narrow?
Not fully claim-mapped; cache/TLB/translation-trace variants require direct review.

## Q6 — Is the disclosed mechanism technically implementable/productizable?
Possible but incurs footprint recording/storage/prefetch overhead and requires OS/uArch cooperation.

## Q7 — What do inventor / assignee / patent-family signals tell us?
IBM architecture lineage strengthens this as foundational prior art.

## Q8 — How does it overlap with Huawei / competitor public capability and our candidate?
Kills generic “restore Agent cache/TLB footprint on resume” novelty.

## Q9 — What is background IP vs residual / foreground opportunity?
Background:
- generic fast context warm-state restore.

Residual:
- Agent future-reuse semantics may improve selection, retention horizon or placement policy.

## Q10 — What should we do next?
- Keep as P0 M3 boundary.
- Do not propose generic state restore.
- Test whether StateAffinity adds value beyond history/MPKI/task identity.

## Decision footer
- Prior-art pressure: Very High
- Decision impact: KILL broad M3 restore primitive
- Claim-review completeness: Partial
- Open questions: exact claims; benefit/overhead on mobile
- Primary patent source: link above
