# Final Goal and Question-State Tracker — Agentic Mobile CPU-uArch

Updated: 2026-10-08
Research authority: xjs-work-lab/agentic-CPU-uArch (V2.2 research SSOT / V2.4 graph)
Next: ROUND15C_PUBLIC_ARCHITECTURE_PRESSURE_AND_ROADMAP
Purpose: anti-drift one-page dashboard. Update at the **end of every meaningful research round** and summarize succinctly in user reply.

## Goal Lock (immutable in intent)
**By 2027–2029, what user/workload changes are induced by smartphone Agentic AI, and which compiler/LLVM, runtime, OS, CPU↔GPU↔NPU, memory/SoC and CPU-uArch technologies should a controllable team FOLLOW, BUILD, BET, RESERVE or KILL?**

Leadership deliverable = **3–5 structural workload changes + 3–5 architecture themes + vendor/academic mechanisms + explicit baselines/prior-art + software-vs-hardware split + ranked Primary Bets/Strategic Reserves/Kill list + year/layer roadmap + public-evidence confidence gates.**

**HARD CONSTRAINT — PUBLIC SOURCES ONLY, ZERO NEW EXPERIMENTS.** No local device testing, new benchmarks, simulations/replays, performance instrumentation, PoC execution or privately gathered test data. Rely on deep-read, traceable publicly available research papers, patents/claims, official vendor whitepapers/engineering publications, public product disclosures and published third-party experimental results. This applies through final delivery; lack of local experiments must **not delay** the evidence-based investment roadmap.

Gate-A public-evidence architecture discovery is the project's decision standard. Gate-B experimental product/silicon proof is **out of scope**, a descriptive caveat only.

## Seven final questions — progress audit
| ID | Must answer before closing | Status as of Round 15B | Current answer / unresolved gap |
|---|---|---|---|
| FQ1 | **What 3–5 workload/user-experience shifts matter in 2027–29?** | MAPPED, AWAITING 3–5 CONVERGENCE | T1..T8 product Trend map, Round14 complete; proactive, persistent context, revision/actuation, mixed-criticality heterogeneous pipeline recur. Need rank just 3–5 and year-scoped confidence. |
| FQ2 | **What do academic/industry leaders already implement, and what is mature prior art?** | MAPPED, DEEP COVERAGE STILL ITERATIVE | Round15A AO1–AO5 all EVIDENCE_MAPPED; Round15B deep ProgRouter closed. Authoritative LLM-routing, systems and vendor strands represented, source identity QA active; target-phone public disclosures still sparse. |
| FQ3 | **Where are 3–5 genuinely useful *cross-layer* architecture themes and overlaps?** | PROVISIONAL 3-THEME SYNTHESIS | Theme F AO1/2/3 execution-state; Theme P AO4 proactive admission; Theme V AO5 information/QoE policy. Cross-AO Claim/Evidence graph created; these are search themes, **not three new investment bets**. Need compare architectural mechanisms for distinctiveness. |
| FQ4 | **Which tensions survive strong software baselines; is any CPU/SoC/uArch lever justified from PUBLIC evidence?** | OPEN / NO SILICON COMMITMENT | Software control already powerful across all five AOs. Credible but publicly unmeasured residuals: cross-xPU lifetime/cancel/command, post-gating low-power domain, non-reconstructible NeededProgress. Rank plausibility and confidence without conducting a test. |
| FQ5 | **Which 2–3 PRIMARY BETs, 2–3 STRATEGIC RESERVES and Kill/Do-not-invest items should leadership choose?** | PROVISIONAL / DIFFERENTIATION REFRAME | A only PRIMARY_BET 82.5; second intentionally unfilled; PT-A+C enablers; CG-06 INVEST; CG-07 EXPLORE; CG-01 BENCHMARK; B-residual/R1/R2 reserves; R3 blocked. Generic utility, Agent transactions, semantic scheduling, generic cache novelty crowded. Need cross-theme re-rank without quota padding. |
| FQ6 | **What is the staged 2027 / 2028 / 2029 CPU–LLVM–OS–SoC roadmap?** | NEEDS RECONVERGENCE | Existing `09-roadmap/final-2027-2029.md` is an earlier provisional management snapshot, not yet refit to the new three themes. Need year×technical-layer milestones/what-to-follow and uncertainty bounds. |
| FQ7 | **Which PUBLIC evidence distinguishes competing hypotheses and warrants FOLLOW/BET/RESERVE/KILL?** | PUBLIC-EVIDENCE GATES IN PROGRESS | Prior EXP-* specifications are archival/future reference only, **not activities planned for this study**. Use original published ablations, cross-vendor disclosures, patent independent claims, counterevidence and scope limits. Missing direct proof is labelled clearly rather than converted to a testing request. |

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
