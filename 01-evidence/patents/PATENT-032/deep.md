> Exact V1 patent 10Q copied from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# PATENT-032 — Agent Interaction Based on Dialogue-History Self-Deposition — CN121960775A

## Source
- Publication: CN121960775A
- Assignee: Zhongdian Cloud Computing Technology Co., Ltd.
- Priority: 2026-01-20
- Publication date: 2026-05-01
- Primary source: https://patents.google.com/patent/CN121960775A/en
- Project relevance: Candidate B semantic validity / cache invalidation
- Priority: P0

## Q1 — What engineering problem is the patent trying to solve?
Agent dialogue/result/reasoning caches can become stale when business knowledge or rules change. Generic TTL/LRU cannot determine semantic validity.

## Q2 — How relevant is it to smartphones / CPU / Agentic workloads?
Directly Agentic at the application/memory layer.

It is platform-general and does not specifically target smartphone NPU/DRAM/UFS physical state.

## Q3 — How crowded is this prior-art space?
Stage 14 evidence shows rapidly increasing crowding around:
- versioned Agent memory;
- semantic cache invalidation;
- dependency-aware invalidation;
- versioned execution and valid-state inheritance.

## Q4 — What is the control point of the independent claims?
**Direct claim review.**

Independent claim 1 recites an Agent interaction method that:
- retrieves semantically similar records from a two-layer cache containing historical-result and reasoning-process caches;
- performs multi-factor cache-validity arbitration including identity, time window and **service-version consistency**;
- evaluates whether a valid historical answer fully/partially/does not satisfy current demand;
- if needed, retrieves structured memory including entity relations, intent-evolution paths and user-profile data;
- invokes an LLM with the constructed context and reuses/corrects historical reasoning;
- updates structured memory and caches after the new answer.

This is a direct Agent-specific claim-level anchor for semantic/version-aware cache validity.

## Q5 — What do dependent claims / embodiments add or narrow?
**Direct dependent-claim review.**

Relevant claims add:
- claim 2: cached metadata includes user/session/intent and reasoning cache stores intent labels, entity paths, reasoning logic and dependent data;
- claim 3: validity is the conjunction of identity, time-window and version matching;
- claim 4: major/minor service-version changes trigger invalidation;
- claim 5: semantic demand-satisfaction grading controls whether cached answers can be reused.

The claims are focused on dialogue/result/reasoning memory and knowledge-version changes.

They do **not** directly claim:
- invalidating derived NPU/DRAM/UFS KV/compiled/runtime artifacts from an Agent plan/fact revision;
- certified partial physical-state inheritance across smartphone tiers.

## Q6 — Is the disclosed mechanism implementable/productizable?
Yes at Agent/runtime/application memory layers.

## Q7 — What do assignee/family signals tell us?
The assignee is a cloud-computing technology company. This is technically relevant prior art but not evidence of mobile-SoC productization.

## Q8 — How does it overlap with our Candidate B?
Strong overlap with the broad reframe:
> Agent semantic/version change → invalidate stale cached memory.

Less direct overlap with the narrower residual:
> S0/S1 semantic revision → dependency-tracked invalidation/preservation of derived S2/S3 physical state on a smartphone.

## Q9 — Background IP vs residual opportunity
Background / crowded:
- Agent semantic-aware cache invalidation;
- version-stamped Agent memory;
- structured intent/entity/reasoning cache validity.

Residual:
- cross-tier derived-state lineage from semantic/workflow state into model/runtime physical artifacts;
- smartphone-specific NPU/DRAM/UFS coherence;
- selective preservation of compatible physical state under tight mobile memory/energy constraints.

## Q10 — Next action
- Keep as P0 Candidate-B boundary.
- Kill broad novelty wording around “semantic/version-aware Agent cache invalidation.”
- Only preserve a narrower phone cross-tier coherence hypothesis if its incremental value can be measured.
- No legal/FTO conclusion.

## Decision footer
- Evidence role: **DIRECT_AGENTIC**
- Prior-art pressure: High
- Decision impact: NARROW / DOWNGRADE Candidate B
- Claim-review completeness: **Direct**
- Open questions: family/prosecution evolution; mobile physical-state lineage prior art
- Primary patent source: https://patents.google.com/patent/CN121960775A/en
