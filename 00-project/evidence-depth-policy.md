# Evidence Depth Policy — EDP v1

Updated: 2026-10-07

## Purpose
Prevent shallow source reading from propagating into claims, strongest baselines, Keep/Kill decisions, portfolio scores or CPU/uArch conclusions.

This policy is part of the active research method. It applies to papers, patents, vendor evidence, tools/artifacts and other sources according to their source type.

## Decision-critical source rule
A source is **decision-critical** if any of the following is true:
1. it materially supports an active Direction / reserve / competitive-gap lane;
2. it is named as part of a strongest baseline;
3. it materially triggers Keep / Upgrade / Downgrade / Narrow / Kill;
4. it is used to pass or block SYSTEM_VALUE, SOFTWARE_INSUFFICIENCY, hardware-specific cause or UARCH_CANDIDATE;
5. it materially supports a public capability-gap or prior-art boundary.

Decision-critical papers must reach **FULL_10Q under EDP v1** before they may newly drive a portfolio decision.

## EDP v1 deep-read contract
A FULL_10Q review is not satisfied by an abstract-level ten-question summary.

The deep-read must reconstruct:
> workload/input → internal state → mechanism → control variable → resource behavior → measured outcome → limitation

It must also record:
- strongest competing baseline actually evaluated;
- ablations / causal evidence;
- target hardware and software stack;
- direct vs inferred mechanism;
- alternative explanations;
- external-validity boundary;
- artifact/reproducibility status;
- research lineage / independence where material;
- exact decision impact and whether the source changes, narrows or merely supports an existing conclusion.

Unknown values remain Unknown / Not yet verified.

## Strongest-baseline gate
A source may not Kill/Narrow a candidate merely because it appears to cover the same idea.

Before a source materially acts as a strongest baseline:
- the relevant mechanism must be FULL_10Q;
- the baseline comparator must be understood at the same control-point granularity as the candidate;
- evaluated platform/workload differences must be explicit;
- software capture must not be converted into universal software sufficiency without a residual test.

## Kill gate
Future standalone Direction / hypothesis Kill decisions require, at minimum:
- workload premise deep-read;
- strongest positive source deep-read;
- strongest opposing/software baseline deep-read;
- direct target-system evidence deep-read when available;
- alternative explanation / negative-evidence review;
- explicit statement of what is killed: novelty, mechanism, architecture necessity, product need or wording.

## Backtrace gate
For every major current conclusion, the audit path is:
> roadmap conclusion → decision event → claim → evidence case → source → mechanism/experiment

If the source does not support the exact wording, the claim must be narrowed even if the overall lane remains unchanged.

## Review metadata
Decision-critical paper Source objects should use:
- `review_depth = "FULL_10Q"`
- `deep_review_protocol = "EDP_V1"`
- `deep_review_date = "YYYY-MM-DD"`
- `decision_critical = true`

## Enforcement rollout
### Phase 1 — Rescue mode
Current historical debt produces **Graph QA warnings**, not hard failures.

### Phase 2 — Hard gate
After current-portfolio decision-critical paper debt reaches zero:
- a new decision-critical paper without FULL_10Q becomes a hard error for Primary-Bet promotion, Direction Kill, evidence-maturity promotion or uArch promotion;
- other active-lane gaps remain warnings until explicitly closed.

## Scope boundary
This policy does not require every background paper in the repository to receive FULL_10Q.

Depth follows decision importance, not source count.
