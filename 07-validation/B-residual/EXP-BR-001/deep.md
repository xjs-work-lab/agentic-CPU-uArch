> Exact V1 B-residual experiment specification and pass-1 result from frozen baseline `960abb4ef50f050da3c6784d30826053d42e5c5d`.

# Stage 15 — B-residual Strong-Baseline Break-even / Kill Test

Updated: 2026-10-05

## Goal

Attack the remaining B-residual:

> **Mobile Agent Semantic-to-Physical State Coherence**

Question:

> After strong generic safe version/hash/provenance handling, does explicit Agent semantic/workflow lineage still preserve enough smartphone S2/S3 state to improve a meaningful end outcome by >=~5%?

## Why the baseline changed

The previous first-pass B model compared:
- safe full invalidation/rebuild;
- dependency-aware selective preservation.

That is now too weak.

Recent Agent systems already demonstrate:
- versioned execution with certified compatible-state inheritance;
- dependency-scoped validation;
- dependency-guided rollback and selective replay;
- version/dependency-based Agent-memory invalidation.

Therefore **dependency-aware selective invalidation is not itself project whitespace**.

## Policies

### B4-safe-full
Known semantic/workflow revision -> invalidate all derived state in scope -> rebuild.

Use only as a lower baseline / historical reference.

### B4-safe-generic — required strong baseline
- revision/version event known;
- artifact identity includes available version/content hashes;
- dependency/provenance scopes are used where available;
- unchanged/proven-compatible artifacts are preserved;
- unknown validity fails closed;
- stale reuse = 0.

### B6-cross-tier-lineage
Adds only the residual information:
- explicit S0/S1 semantic/workflow lineage to S2/S3 phone artifacts;
- conservative invalidation of affected artifacts;
- certified preservation of additional compatible artifacts;
- stale reuse = 0.

B6 must not receive credit for preservation already achievable by B4-safe-generic.

## Key quantities

1. **RevisionEventFraction**
2. **RevisionWeightedReconstructionShare**
3. **AffectedStateFraction**
4. **GenericSafePreservationCapture**
   - fraction of otherwise-preservable state already kept safely by generic version/hash/provenance machinery.
5. **LineageCapture**
   - fraction of the remaining avoidable invalidation recovered by explicit Agent cross-tier lineage.
6. **RetentionSurvival**
   - fraction of preserved state still resident/actionable under realistic phone memory pressure.
7. metadata / graph-maintenance overhead
8. stale reuse / correctness failures

## Pass-1 model

```
Gain =
RevisionWeightedReconstructionShare
× (1 - AffectedStateFraction)
× (1 - GenericSafePreservationCapture)
× LineageCapture
× RetentionSurvival
- MetadataOverhead
```

Safety:
unknown dependency / validity -> invalidate, never reuse.

This makes incomplete lineage a performance loss, not a correctness shortcut.

## Promotion gate

Promote B-residual above Strategic Reserve only if target-phone evidence shows all:

1. Agent semantic/workflow revisions create material S2/S3 stale-state events;
2. revision-weighted S2/S3 rebuild cost is substantial;
3. strong B4-safe-generic leaves a large avoidable residual;
4. B6 produces >=~5% meaningful outcome gain;
5. stale reuse = 0;
6. benefit survives realistic memory pressure and eviction;
7. value is specifically cross-tier S0/S1 -> S2/S3, not only S0/S1 memory repair.

## Kill / further downgrade

Further downgrade if any:
- revisions are rare;
- rebuild is cheap;
- most state is actually affected;
- GenericSafePreservationCapture is high;
- preserved state does not survive memory pressure;
- dependency/provenance maintenance cost erases the gain;
- benefit remains entirely at Agent memory/plan/runtime layer.

## Pass-1 result

See:
`analysis/stage15_b_residual/results/b-residual-kill-pass1.md`

Decision:
**NARROW / DOWNGRADE.**

B-residual remains a conditional measurement hypothesis, not an active second-Bet challenger.

## Future phone trace additions

Only when target-device work resumes, add the minimum fields needed to estimate:
- revision/version ID;
- artifact ID/type (S2/S3);
- provenance/dependency root;
- rebuild/restoration cost;
- invalidated vs preserved;
- B4-safe-generic decision;
- B6 decision;
- pressure/eviction state;
- stale-reuse correctness result.

Do not add CPU PMU/uArch fields for B-residual at this stage.


---

# Stage 15 B-residual — Strong-Baseline Kill Test, Pass 1

Date: 2026-10-05

## Question

Does **Mobile Agent Semantic-to-Physical State Coherence** retain a plausible >=5% incremental region after a strong safe generic version/hash/provenance baseline?

This is not a full-flush-vs-selective comparison anymore.

The stronger comparison is:

- **B4-safe-generic:** revision is known; generic versions/hashes/scoped provenance safely preserve some unaffected state; unknown validity fails closed.
- **B6-cross-tier-lineage:** explicit Agent S0/S1 -> S2/S3 lineage preserves additional compatible state not already captured by B4.

Safety constraint:
**stale reuse = 0** for both.

## Model

Normalized incremental gain:

```
revision_weighted_reconstruction_share
× (1 - affected_state_fraction)
× (1 - generic_safe_preservation_capture)
× lineage_capture
× retention_survival
- metadata_overhead
```

Pass-1 defaults:
- target gain: 5%
- lineage capture: 90%
- metadata overhead: 0.2%
- reference retention survival under pressure: 75%

All values except the target/overhead are sensitivity assumptions, not phone measurements.

## Reference break-even at 5% revision frequency

### 25% of derived state truly affected per revision

| Generic safe preservation already captured | Required revision-weighted rebuild share | Required rebuild cost / revision vs average event |
|---:|---:|---:|
| 0% | 10.27% | 2.29x |
| 25% | 13.70% | 3.17x |
| 50% | 20.54% | 5.17x |
| 75% | 41.09% | 13.95x |

### 50% of derived state truly affected per revision

| Generic safe preservation already captured | Required revision-weighted rebuild share | Required rebuild cost / revision vs average event |
|---:|---:|---:|
| 0% | 15.41% | 3.64x |
| 25% | 20.54% | 5.17x |
| 50% | 30.81% | 8.91x |
| 75% | 61.63% | 32.12x |

Interpretation:
once a strong generic baseline safely preserves ~50–75% of the otherwise-preservable state, B6 requires a very expensive revision/rebuild regime to clear 5%.

## Coarse grid

Sweep:
- revision frequency: 2%, 5%, 10%
- reconstruction cost multiplier: 1x, 2x, 4x, 8x
- affected state: 25%, 50%, 75%
- generic safe preservation capture: 25%, 50%, 75%
- retention survival: 50%, 75%, 100%
- lineage capture: 90%
- metadata overhead: 0.2%

108 cells per generic-capture band.

5% passing cells:
- generic capture 25%: **26/108**
- generic capture 50%: **13/108**
- generic capture 75%: **2/108**

At 75% generic capture the only passing cells are the extreme:
- 10% revision frequency
- 8x reconstruction cost
- only 25% state affected
- retention survival 75–100%

## Decision

**NARROW / DOWNGRADE B-residual.**

The broad full-flush-vs-selective model was too optimistic because it credited B6 for preservation that mature version/hash/provenance mechanisms may already achieve.

B-residual is no longer an active second-Bet challenger in the device-free portfolio.

It remains a **conditional Strategic Reserve / measurement hypothesis** only if future phone evidence shows all of:
1. S0/S1 revisions frequently invalidate expensive S2/S3 state;
2. the revision-weighted rebuild share is large;
3. strong generic safe version/hash/provenance preserves materially less than ~50% of the avoidable rebuild;
4. preserved state survives realistic phone memory pressure;
5. explicit cross-tier Agent lineage adds >=5% matched-outcome value with zero stale reuse.

## Strongest next measurement

Do not build a special coherence mechanism first.

Measure:
- revision frequency;
- S2/S3 artifact rebuild cost;
- true affected-state fraction;
- **GenericSafePreservationCapture**;
- **RetentionSurvival** under memory pressure;
- stale-reuse/correctness.

If generic safe preservation reaches ~75% in realistic regimes, this pass suggests B-residual is unlikely to justify an independent architecture program unless revision/rebuild cost is extreme.

