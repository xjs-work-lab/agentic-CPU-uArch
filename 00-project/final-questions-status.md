# Final Goal and Question-State Tracker — Agentic Mobile CPU-uArch

Updated: 2026-10-08
Research authority: xjs-work-lab/agentic-CPU-uArch (V2.2 research SSOT / V2.4 graph)
Next: ROUND15D_PUBLIC_EVIDENCE_STRATEGIC_CONVERGENCE
Purpose: anti-drift one-page dashboard. Update at the **end of every meaningful research round** and summarize succinctly in user reply.

## Goal Lock (immutable in intent)
**By 2027–2029, what user/workload changes are induced by smartphone Agentic AI, and which compiler/LLVM, runtime, OS, CPU↔GPU↔NPU, memory/SoC and CPU-uArch technologies should a controllable team FOLLOW, BUILD, BET, RESERVE or KILL?**

Leadership deliverable = **3–5 structural workload changes + 3–5 architecture themes + vendor/academic mechanisms + explicit baselines/prior-art + software-vs-hardware split + ranked Primary Bets/Strategic Reserves/Kill list + year/layer roadmap + public-evidence confidence gates.**

**HARD CONSTRAINT — PUBLIC SOURCES ONLY, ZERO NEW EXPERIMENTS.** No local device testing, new benchmarks, simulations/replays, performance instrumentation, PoC execution or privately gathered test data. Rely on deep-read, traceable publicly available research papers, patents/claims, official vendor whitepapers/engineering publications, public product disclosures and published third-party experimental results. This applies through final delivery; lack of local experiments must **not delay** the evidence-based investment roadmap.

Gate-A public-evidence architecture discovery is the project's decision standard. Gate-B experimental product/silicon proof is **out of scope**, a descriptive caveat only.

## Seven final questions — progress audit
| ID | Must answer before closing | Status as of Round 15C | Current answer / unresolved gap |
|---|---|---|---|
| FQ1 | **What 3–5 workload/user-experience shifts matter in 2027–29?** | PROVISIONAL FOUR-SHIFT SHORTLIST | Four public-evidence themes now selected: persistent action/context, reactive+proactive, revisable/interruptible, heterogeneous model/SoC. Rank and 2027–29 uptake confidence still to converge. |
| FQ2 | **What do academic/industry leaders already implement, and what is mature prior art?** | MAPPED + OFFICIAL OS/SDK PRESSURE ADDED | Added Android17 NPU Manager, AOSP HAL burst, Qualcomm QNN HTP shared memory, NNAPI NDK migration, AICore; QNN page excerpt audit not full manual; platform deployment and target phone economics remain scope limits. |
| FQ3 | **Where are 3–5 genuinely useful *cross-layer* architecture themes and overlaps?** | PROVISIONAL THREE THEMES RE-STRESSED | Theme F AO1/2/3 execution-state, P AO4 proactive LP admission, V AO5 QoE/info. AOSP NPU Manager directly crowds several formerly tempting AO1/AO2 generic control points. Three themes remain not three investment bets. |
| FQ4 | **Which tensions survive strong software baselines; is any CPU/SoC/uArch lever justified from PUBLIC evidence?** | NARROWED / NO SILICON COMMITMENT | Android17 model admission, work cancel/preempt/pausing and QNN/AOSP memory+burst controls are documented generic baseline. Only Agent-specific version/permission/need/lifetime residuals are architecture hypotheses; published per-phone causal evidence still missing. |
| FQ5 | **Which 2–3 PRIMARY BETs, 2–3 STRATEGIC RESERVES and Kill/Do-not-invest items should leadership choose?** | PROVISIONAL / DIFFERENTIATION REFRAME | A only PRIMARY_BET 82.5; second intentionally unfilled; PT-A+C enablers; CG-06 INVEST; CG-07 EXPLORE; CG-01 BENCHMARK; B-residual/R1/R2 reserves; R3 blocked. Generic utility, Agent transactions, semantic scheduling, generic cache novelty crowded. Need cross-theme re-rank without quota padding. |
| FQ6 | **What is the staged 2027 / 2028 / 2029 CPU–LLVM–OS–SoC roadmap?** | PROVISIONAL PUBLIC-ONLY ROADMAP DRAFTED | `09-roadmap/round15c-public-source-roadmap-2027-2029.md` now maps 2027/28/29 and LLVM/runtime/OS/CPU-NPU/low-power themes; old `final-2027-2029.md` explicitly marked archived (contains forbidden EXP tasks). Leadership-ready year milestones still need final ranking. |
| FQ7 | **Which PUBLIC evidence distinguishes competing hypotheses and warrants FOLLOW/BET/RESERVE/KILL?** | PUBLIC-EVIDENCE GATES SET FOR F/P/V | No experiments. AOSP official interfaces vs vendor implementation disclosures; original phone experimental papers vs optimized software; patented control scope; multiple vendor uptake; Agent-private info vs ledger-visible progress. Missing phone proof labelled confidence ceiling. |

## Persistent portfolio invariants
- A PRIMARY_BET 82.5 / SIMULATION_SUPPORT: **unproven** hidden DemandState/RequiredProgress residual, not generic progress scheduler.
- PT-A PLATFORM_TRACK; C STRATEGIC_ENABLER; CG-06 INVEST; CG-07 EXPLORE; CG-01 BENCHMARK.
- B-residual, R1, R2 conditional reserves; R3 BLOCKED; second differentiated Primary Bet UNFILLED; no uArch Primary Bet.
- AOs remain opportunity *research objects*; 5/5 EVIDENCE_MAPPED ≠ 5 investments; three themes ≠ three Primary Bets.

## Round-end reporting contract (every future round)
1. **This round:** exact source-deepread, graph/QA and conclusion delta.
2. **Goal check:** final goal in one sentence + FQ1…FQ7 statuses (compact table).
3. **Portfolio:** which keep/upgrade/downgrade/kill changes; or explicitly none.
4. **What's missing and next smallest round:** public-literature/patent/whitepaper gap only. **Never schedule or suggest conducting a new experiment or PoC** as part of this project.
5. **SSOT commit / QA:** exact SHA, validation result, unresolved blockers.

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
