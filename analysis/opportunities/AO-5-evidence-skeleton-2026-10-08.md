# Round 15A — AO-5 Evidence Skeleton

Date: 2026-10-08
Outcome: **EVIDENCE_MAPPED (5/5 AO opportunities) / KEEP-NARROW only / no portfolio repricing**.

## Field-map and deep-read route
- ACL / EMNLP / ICLR: agent reasoning, confidence and adaptive workflow control; direct ACL 2026 LAS PAPER-119 FULL_10Q; ICLR 2025 Proactive Agent PAPER-043 already FULL_10Q.
- MLSys / ASPLOS / OSDI / SOSP / EuroSys / USENIX ATC: agent-serving/scheduling, runtime legality, OS/SoC co-design adjacent field; SMetric PAPER-120 FULL_10Q server systems anchor; PAPER-047 and PAPER-050 previous FULL_10Q.
- RTSS / EMSOFT / ACM TECS: utility/deadline/energy scheduling ancestry; ReUA PAPER-068 previous FULL_10Q.
- Consumer mobile product/platform: Huawei FFRT / kernel, MediaTek agentic AI, Qualcomm NPU are product surfaces only; no documented Agent private RequiredProgress-to-silicon binding.
- Next expansion debt: EMNLP Findings-reported ProgRouter PAPER-121 currently screened abstract only, full PDF unavailable; do not count as deep-reviewed evidence. Search mechanism lineage after deep-read.

## Primary-source review table
| ID | Primary link | Depth | Evidence role and hard boundary |
|---|---|---|---|
| PAPER-119 | https://aclanthology.org/2026.acl-long.581.pdf | NEW FULL_10Q, ACL final camera-ready PDF pages 1–9 including Section 4/5, Tables 2–6, limitations | Gate + LLM routing of verified intermediate artifacts; code/math API benchmark, not target phone. Website abstract says 43% token savings; paper final abstract average 50.5%, Table 2 varies 37.4–63.4%. Use final PDF and dataset-specific numbers. |
| PAPER-120 | https://arxiv.org/html/2607.08565 | NEW FULL_10Q, original HTML Sections 2–5 with trace methodology, system baselines and sensitivity | Session turn inferred from messages; 10–16% good TPS gains with global tier; no-agent-logic router, no phone. |
| PAPER-068 | https://doi.org/10.1145/1017753.1017768 | REUSED FULL_10Q | TUF/utility accrual mobile embedded prior art; simulation, no Agent direct value. |
| PAPER-047 | https://arxiv.org/abs/2609.10964 | REUSED FULL_10Q | Ready/release tail under queue pressure, server Agent only. |
| PAPER-043/044 | https://arxiv.org/abs/2410.12361 ; https://arxiv.org/abs/2602.04482 | REUSED FULL_10Q | Behavior-based learned demand proxy, not oracle Agent RequiredProgress. |
| PAPER-013/015/050 | https://arxiv.org/abs/2605.13360 ; https://arxiv.org/abs/2604.00842 ; https://arxiv.org/abs/2609.38201 | REUSED FULL_10Q | Speculate, propose/accept, effect/commit are runtime-visible or runtime-derivable in part. |
| PAPER-048 | https://arxiv.org/abs/2605.07937 | REUSED FULL_10Q | Long-trajectory clarification value windows, not CPU scheduler timing. |
| PAPER-121 | https://arxiv.org/abs/2608.25992 | METADATA_ONLY, queued FULL_10Q | High-priority progress-aware routing competing paper, **not** used as decision-grade premises. |

## Evidence roles and relations
- Problem CLM-AO5-001: EC-AO5-001-A SUPPORT; EC-AO5-001-B SCOPE_LIMIT.
- Product CLM-AO5-002: EC-AO5-002-A SUPPORT; EC-AO5-002-B SCOPE_LIMIT.
- Mechanism CLM-AO5-003: EC-AO5-003-A/B SUPPORT.
- Strongest baseline CLM-AO5-004: EC-AO5-004-A/B SUPPORT.
- Prior art CLM-AO5-005: EC-AO5-005-A/B SUPPORT.
- Open gap CLM-AO5-006: EC-AO5-006-A SUPPORT a bounded *question*, -B UNDERCUTS that inferential bridge, -C SCOPE_LIMIT.
- Hypothesis CLM-AO5-007: EC-AO5-007-A SCOPE_LIMIT, -B SUPPORT its bounded *research motivation*, not truth.

## Source-claim-inference hierarchy
**[FACT]** LAS benefits from quality/artifact/validator/routing state and suffers quality loss when naive gating; **[FACT]** SMetric extracts meaningful session-stage information from existing messages and its server performance depends on KV architecture; **[FACT]** generic utility-under-deadline is old prior art; **[OBSERVATION]** semantic-like *observable* information already influences software decisions; **[INFERENCE]** private DemandState has a possible conditional-information residual; **[HYPOTHESIS]** only after independent value should an interface be proposed.

## Decision
**KEEP / NARROW AO-5**; seven role-backed claims; no unmeasured improvement, no new portfolio investment. AO-1..5 now have EVIDENCE_MAPPED coverage but not final cross-AO assessment.

## Next
Round15B with ProgRouter full read prioritized; compare AO1 execution, AO2 revisions, AO3 state, AO4 proactive gates and AO5 policy/semantic value without duplicate product evidence and without inventing a second Primary Bet.
