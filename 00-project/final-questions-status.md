# Final Goal and Question-State Tracker — Agentic Mobile CPU-uArch

Updated: 2026-10-08
Research authority: xjs-work-lab/agentic-CPU-uArch (V2.2 research SSOT / V2.4 graph)
Next: ROUND15G_FINAL_SOURCE_AUDIT_AND_REPORT_CLOSURE
Purpose: anti-drift one-page dashboard. Update at the **end of every meaningful research round** and summarize succinctly in user reply.

## Goal Lock (immutable in intent)
**By 2027–2029, what user/workload changes are induced by smartphone Agentic AI, and which compiler/LLVM, runtime, OS, CPU↔GPU↔NPU, memory/SoC and CPU-uArch technologies should a controllable team FOLLOW, BUILD, BET, RESERVE or KILL?**

Leadership deliverable = **3–5 structural workload changes + 3–5 architecture themes + vendor/academic mechanisms + explicit baselines/prior-art + software-vs-hardware split + ranked Primary Bets/Strategic Reserves/Kill list + year/layer roadmap + public-evidence confidence gates.**

**HARD CONSTRAINT — PUBLIC SOURCES ONLY, ZERO NEW EXPERIMENTS.** No local device testing, new benchmarks, simulations/replays, performance instrumentation, PoC execution or privately gathered test data. Rely on deep-read, traceable publicly available research papers, patents/claims, official vendor whitepapers/engineering publications, public product disclosures and published third-party experimental results. This applies through final delivery; lack of local experiments must **not delay** the evidence-based investment roadmap.

Gate-A public-evidence architecture discovery is the project's decision standard. Gate-B experimental product/silicon proof is **out of scope**, a descriptive caveat only.

## Seven final questions — progress audit
| ID | Must answer before closing | Status as of Round 15F | Current answer / unresolved gap |
|---|---|---|---|
| FQ1 | **What 3–5 workload/user-experience shifts matter in 2027–29?** | ADEQUATE — RANKED FOUR SHIFTS | Ranked persistent safe workflows, repeated CPU↔NPU stages, revisable state and proactive LP admission; cross-OEM product evidence and published phone/system sources. 2027–29 prevalence and specific SoC economics remain conditional. |
| FQ2 | **What do academic/industry leaders already implement, and what is mature prior art?** | ADEQUATE FOR BOUNDED STRATEGY | 5/5 AO evidence mapped; three direct patent claim audits; Apple, Google, Samsung official products; ProgRouter/LAS full deep reads, Android NPU Manager/QNN. Direct multi-vendor Agent system energy evidence remains incomplete. |
| FQ3 | **Where are 3–5 genuinely useful *cross-layer* architecture themes and overlaps?** | ADEQUATE — 3 THEMES WITH OWNERSHIP | F execution/state, P proactive LP admission, V progress/QoE software information; user-effect authority separate from memory validity. Not three hardware Bets. |
| FQ4 | **Which tensions survive strong software baselines; is any CPU/SoC/uArch lever justified from PUBLIC evidence?** | COMPILER ADEQUATE / HARDWARE GAP | Existing AArch64 SME ABI, MLIR ArmSME/Linalg, vectorization and KleidiAI plus vivo phone SME2 reveal concrete compiler/microkernel paths; optimized NPU/mobile Agent runtime software baseline remains strong. Novel Agent CPU hardware causal value unestablished. |
| FQ5 | **Which 2–3 PRIMARY BETs, 2–3 STRATEGIC RESERVES and Kill/Do-not-invest items should leadership choose?** | CLOSED FOR 2026-10-08 PUBLIC EVIDENCE PORTFOLIO | DEC-PORTFOLIO-002 formally commits 3 P0 technology investments CG-06/PT-A/C, **0 independent differentiated Primary Bets**, core reserves A/B-residual/R2; R1 WATCH, CG-07 Explore, CG-01 external benchmark, R3 Blocked. A 82.5 retired historical (DEC-A-008), no new score. |
| FQ6 | **What is the staged 2027 / 2028 / 2029 CPU–LLVM–OS–SoC roadmap?** | ADEQUATE + OWNER-SPECIFIC CG06 LEVERS | 15E year/layer roadmap now complemented by 15F technical brief and C1–C5 compiler/ABI/kernel/CPU-NPU partition/runtime ownership. Management source link audit still to close. |
| FQ7 | **Which PUBLIC evidence distinguishes competing hypotheses and warrants FOLLOW/BET/RESERVE/KILL?** | ADEQUATE PUBLIC DECISION RULES | Formal reserve/downgrade from deep original software progress paper ablations and official NPU/API/prior art, with SUPPORT+SCOPE_LIMIT. A private info and cross-xPU physical value remain explicitly unknown; no experiment needed or proposed. |

## Persistent portfolio invariants — Round15E formal cutover
- **CG-06 INVEST, PT-A PLATFORM_TRACK, C STRATEGIC_ENABLER** = three actionable priority engineering/platform investments with original published phone/product evidence, not differentiated CPU-ISA Primary Bets.
- **0 evidence-qualified new independent differentiated PRIMARY_BETs** at this as-of date. Never fill to 2–3 by renaming existing enabling/platform work.
- **A formally downgraded PRIMARY_BET→CONDITIONAL_RESERVE**, historical 82.5 retired from current allocation ranking, `HYPOTHESIS_OPEN`; prior A Decision Events preserved as historic.
- Three core strategic reserves = **A, B-residual, R2**. **R1 WATCH**, not core reserve; **CG-07 EXPLORE**, **CG-01 BENCHMARK**, **R3 BLOCKED**.
- Product Trends T1–T8 may remain important despite lack of standalone differentiated novel processor mechanisms; 3 F/P/V research themes are not 3 financial bets.
- No experiment, phone instrumentation, simulation or PoC in this public-evidence-only project.

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

## Round15E formal closeout status and technology coverage (2026-10-08)
- FQ1 ADEQUATE in scope: ranked four shifts; dates not vendor product promises.
- FQ2 ADEQUATE for literature/vendor/patent prior-art baseline, remaining phone long-agent multi-vendor quantitative limitations.
- FQ3 ADEQUATE: F/P/V three architecture study themes, separated from core investments.
- FQ4 PARTIAL / GAP: strongest software/OS sufficiency clear for generic primitives; no publicly demonstrated distinctive CPU/SoC Agent-specific state primitive.
- FQ5 CLOSED at 2026-10-08 public-evidence level: three core engineering investments; zero new differentiated Primary Bets; three core Reserves; R1 WATCH; explicit Kill.
- FQ6 ADEQUATE integrated 2027/28/29 public-only year/layer draft, leadership narrative refinement next.
- FQ7 ADEQUATE for public-sources strategic decision rules, with explicit knowledge boundaries and no experiment obligation.
- Technical coverage: UX/Agent workloads ADEQUATE; LLVM/AArch64 PARTIAL (more original compiler/backend implementation literature comparison); CPU core/uArch PARTIAL (no Agent-specific published mobile benefit); runtime/actuation ADEQUATE; OS resource control ADEQUATE (API not universal retail deployment); CPU–NPU/shared-state PARTIAL; low-power admission PARTIAL (daily-energy+helpfulness tradeoff absent).
- Next Round15F: review decision-critical CPU+LLVM portable fast-path original technical detail, finalize management-facing integrated roadmap, audit links and contradictions; strictly public sources only.

## Round15F cumulative progress and coverage (2026-10-08)
- FQ1 ADEQUATE — four ranked workload/UX shifts; not asserted universal rollout.
- FQ2 ADEQUATE — 5 AO mapped plus direct original CPU/NPU papers and five new official compiler/kernel documentation sources (TOOL-014..018).
- FQ3 ADEQUATE — themes F/P/V separated from three priority investments.
- FQ4 **COMPILER/RUNTIME ADEQUATE; new CPU/uArch silicon GAP** — CPU SME2 on smartphone beneficial in a non-Agent vision task, MLIR/LLVM ABI/kernel implementation levers mapped, optimized NPU competes strongly.
- FQ5 CLOSED within dated public evidence — CG-06/PT-A/C investment, zero differentiated Primary Bets, A/B/R2 reserves, R1 Watch and R3 Blocked; **no lane/score change this round**.
- FQ6 ADEQUATE, more concrete CPU/LLVM C1–C5 component-and-year ownership and leadership brief.
- FQ7 ADEQUATE bounded sourcing, original academic and vendor lineages not counted as independent replications.
- Technology coverage: Agent UX ADEQUATE; LLVM/AArch64 compiler **ADEQUATE for technical mechanism map**; CPU uArch **PARTIAL (no novel hardware proof)**; PT-A/runtime ADEQUATE; OS/QoE ADEQUATE; shared CPU/NPU states PARTIAL; always-on low power PARTIAL.
- Round15G: original source link and decision claim consistency audit, leadership-ready final report, **not experiments**.
