# Final Goal and Question-State Tracker — Agentic Mobile CPU-uArch

Updated: 2026-10-08
Research authority: xjs-work-lab/agentic-CPU-uArch (V2.2 research SSOT / V2.4 graph)
Next: ROUND15E_PORTFOLIO_FORMAL_RECONCILIATION
Purpose: anti-drift one-page dashboard. Update at the **end of every meaningful research round** and summarize succinctly in user reply.

## Goal Lock (immutable in intent)
**By 2027–2029, what user/workload changes are induced by smartphone Agentic AI, and which compiler/LLVM, runtime, OS, CPU↔GPU↔NPU, memory/SoC and CPU-uArch technologies should a controllable team FOLLOW, BUILD, BET, RESERVE or KILL?**

Leadership deliverable = **3–5 structural workload changes + 3–5 architecture themes + vendor/academic mechanisms + explicit baselines/prior-art + software-vs-hardware split + ranked Primary Bets/Strategic Reserves/Kill list + year/layer roadmap + public-evidence confidence gates.**

**HARD CONSTRAINT — PUBLIC SOURCES ONLY, ZERO NEW EXPERIMENTS.** No local device testing, new benchmarks, simulations/replays, performance instrumentation, PoC execution or privately gathered test data. Rely on deep-read, traceable publicly available research papers, patents/claims, official vendor whitepapers/engineering publications, public product disclosures and published third-party experimental results. This applies through final delivery; lack of local experiments must **not delay** the evidence-based investment roadmap.

Gate-A public-evidence architecture discovery is the project's decision standard. Gate-B experimental product/silicon proof is **out of scope**, a descriptive caveat only.

## Seven final questions — progress audit
| ID | Must answer before closing | Status as of Round 15D | Current answer / unresolved gap |
|---|---|---|---|
| FQ1 | **What 3–5 workload/user-experience shifts matter in 2027–29?** | FOUR SHIFTS + CROSS-OEM SUPPORT | Persistent sessions/tool use (Apple), proactive local help (Google), Agent UI/action evolution (Samsung), heterogeneous CPU/NPU (Google/Samsung) publicly reported; 2027–29 penetration remains conditional. |
| FQ2 | **What do academic/industry leaders already implement, and what is mature prior art?** | MAPPED + 3 PATENT CLAIM RE-AUDITS + 3 OEM SOURCES | Independent/dependent claims PATENT-024/032/033 re-read, Apple Foundation Models VENDOR-032, Pixel10 VENDOR-033, Samsung S26 VENDOR-034 reviewed; vendor launch is not independent benchmark and Snapdragon S26 not separate Samsung silicon. |
| FQ3 | **Where are 3–5 genuinely useful *cross-layer* architecture themes and overlaps?** | PROVISIONAL THREE THEMES RE-STRESSED | Theme F AO1/2/3 execution-state, P AO4 proactive LP admission, V AO5 QoE/info. AOSP NPU Manager directly crowds several formerly tempting AO1/AO2 generic control points. Three themes remain not three investment bets. |
| FQ4 | **Which tensions survive strong software baselines; is any CPU/SoC/uArch lever justified from PUBLIC evidence?** | NARROWED BY PATENT+OS+FRAMEWORK / NO SILICON COMMITMENT | Old CPU-cluster cache-demand migration, current-demand Agent reasoning cache validity and Agent transaction rollback patents directly crowd broad novelty; Android17, Apple sessions and QNN already cover resource/state interfaces. Agent-private cross-xPU lifetime hypothetical only. |
| FQ5 | **Which 2–3 PRIMARY BETs, 2–3 STRATEGIC RESERVES and Kill/Do-not-invest items should leadership choose?** | PRE-DECISION LEADERSHIP PRIORITY MATRIX READY | PT-A / CG-06 / C highest confidence engineering/platform; A remains canonical provisional PRIMARY_BET/82.5 but only CONDITIONAL differentiation in public evidence; CG-07 follow, B/R1/R2 reserve, R3 blocked. Second Bet unfilled; no silent score cutover. |
| FQ6 | **What is the staged 2027 / 2028 / 2029 CPU–LLVM–OS–SoC roadmap?** | PUBLIC YEAR-LAYER ROADMAP + PRIORITY MATRIX | Public-only 15C year×LLVM/runtime/OS/CPU-NPU/LP roadmap plus `09-roadmap/round15d-leadership-portfolio-provisional-2027-2029.md`. Main remaining: reconcile canonical A Bet/score evidence and finalize management wording. |
| FQ7 | **Which PUBLIC evidence distinguishes competing hypotheses and warrants FOLLOW/BET/RESERVE/KILL?** | CLAIMS-LEVEL + SOURCE-INDEPENDENCE AUDITED | Independent/dependent patent claims and Apple/Google/Samsung official disclosure checks plus negative/undercut Cases. Remaining A hidden-info and cross-xPU cost issues labelled NOT_PUBLICLY_ESTABLISHED; no experiment proposed. |

## Persistent portfolio invariants
- A PRIMARY_BET 82.5 / SIMULATION_SUPPORT: **unproven** hidden DemandState/RequiredProgress residual, not generic progress scheduler.
- PT-A PLATFORM_TRACK; C STRATEGIC_ENABLER; CG-06 INVEST; CG-07 EXPLORE; CG-01 BENCHMARK.
- B-residual, R1, R2 conditional reserves; R3 BLOCKED; second differentiated Primary Bet UNFILLED; no uArch Primary Bet.
- AOs remain opportunity *research objects*; 5/5 EVIDENCE_MAPPED ≠ 5 investments; three themes ≠ three Primary Bets.

## Round-end reporting contract (every future round)
**Adopt the companion compiler-optimization insight project's cumulative goal-review sequence; retain CPU-uArch's own seven questions.** Exact template and status semantics: [round-end-reporting-contract.md](round-end-reporting-contract.md).

In every user-visible research-round closing use this fixed order:
1. **最终项目目标** — 2027–2029 smartphone Agentic workload → LLVM/CPU/OS/SoC strategy; public sources only; no new tests or experiments.
2. **最终必须回答的七个问题** — one **累计进展** table with FQ1–FQ7, progress/results so far, ADEQUATE/PARTIAL/GAP/CLOSED (and PROVISIONAL when needed), outstanding public-source/decision gaps.
3. **主要技术领域累计覆盖** — workload/UX, LLVM/AArch64, CPU core/cache/uArch, agent/runtime/permissions, OS/CPU↔NPU/GPU/memory, always-on low-power; each area has a status and one important evidence gap.
4. **防跑偏检查** — original decision goal, target phone, software-vs-hardware split, product relevance/novelty, no-experiment constraint, unfilled Bet quota and canonical-portfolio fidelity.
5. **下一步及其必要性** — the next smallest *public-research-only* stage, linked to the specific unanswered FQ and potential investment conclusion.
6. **本轮实际增量与仓库/QA** — concise primary sources deeply checked, inference/portfolio delta, identity dedup and latest commit/CI. May appear briefly before the fixed recap, but must not replace it.

Critical: Round-end reporting tracks **cumulative research progress toward the final management answer**, not merely the number of files or papers added. Never describe an unexecuted experiment as an intended task.
## Public-only decision rule (persistent)
- Progress means **new primary-source verification, original-method deep reading, patent claim checks, source identity dedup, counterevidence and reasoned synthesis** — not equipment trials.
- Each final claim should declare **published fact / cross-source inference / hypothesis / unsupported-by-public-evidence**; vendor claims do not become verified phone-system results merely by citation.
- Existing EXP-* files are historic contingency designs; their existence does not override this user research constraint.
- If a key value cannot be established publicly, give a conditional recommendation and confidence ceiling instead of keeping the project open until hypothetical testing occurs.

## Round15C public-source-only delta (2026-10-08)
- FQ1: four prioritized *candidate* workload shifts, still not 2027–29 inevitabilities.
- FQ2: official Android 17 NPU Manager is the most important new OS-level prior-art pressure: model admission/unload, NPU app priority and work paused/resumed/cancelled; AOSP burst and QNN shared buffers pressure generic context/zero-copy novelty.
- FQ3/FQ4: three themes retained but Theme F is narrower after strong OS/SDK baseline; no demonstrated private Agent uArch reason.
- FQ5: portfolio state unchanged, broad scheduler/zero-copy/transaction novelty more firmly crowded.
- FQ6: active public-only year × layer roadmap now drafted; legacy EXP-dependent roadmap explicitly historic/nonoperative.
- FQ7: public document validation only; no device tests, simulation, new benchmark or PoC.
- Next round: public-evidence portfolio/rank and patented residual control pressure, management shortlist.

## Round15D anti-drift state (2026-10-08)
- FQ1 four workload shifts now include Apple stateful sessions, Pixel on-device proactive features, Samsung Galaxy S26 Agentic app vision as independent OEM *product* scope.
- FQ2 primary patent 024 / 032 / 033 claim re-audits archived; 3 new first-party OEM/platform cards VENDOR-032/033/034. Same Snapdragon S26-Ultra chip is not independent Samsung semiconductor evidence.
- FQ3 the 3 F/P/V themes remain; 3-way vendor signals are **not** 3 unique uArch bets.
- FQ4 strong software/scheduler and patent baseline; no direct proprietary or Agent-specific hardware contract benefit inferred.
- FQ5 pre-decision public portfolio matrix: PT-A/CG-06/C P0 actionable; A conditional differentiated research; CG-07 follow; B/R1/R2 reserves; R3 blocked. Existing 82.5 score/lane is historical provisional and **must be explicitly reconciled**, not silently reinterpreted.
- FQ6 2027–2029 public roadmap and initial leadership portfolio pre-decision created.
- FQ7 claim-vs-product-vs-phone measurement classes separate. No tests/experiments.
- Next Round15E formal SSOT portfolio reconciliation and management-ready final 7 questions; still only public sources.
