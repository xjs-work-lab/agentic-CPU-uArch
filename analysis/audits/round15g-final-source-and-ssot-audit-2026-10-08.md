# Round15G — Final Source URL / Independence / Decision Fidelity / SSOT Audit

Date: **2026-10-08**. Scope: final leadership report's **decision-critical** sources and repository entrypoints. Not an exhaustive crawl of every file, external URL, patent family or legal FTO. **No owned test, benchmark, PoC or simulation.**

## A. Audit method and reconciliation

- **Source-to-decision evidence:** leadership sentence → canonical Source ID / Deep 10Q or official section card → existing Claim + EvidenceCase (support, scope limit, undercut) → Direction / Decision Event. No new SOURCE aliases minted merely to compile reports.
- **Source identity:** DOI, arXiv number (versions unified), patent publication number and family, normalized original URL; distinct vendor product claims and academic peer-reviewed experiments must not be conflated. Existing full source identity/duplicate CI is the global baseline.
- **Internal links tested:** **22 priority MD documents** (9 entrypoints + 13 technical/decision source cards), **84 relative Markdown links**, **0 missing repository file paths** when compared to GitHub main tree at parent commit 4834609e601944f9be3fcfc440efa546a1ad99c5. This only checks link **targets in the repo**, not external HTTP.
- **SSOT drift detected and fixed:** root README had stale “A PRIMARY_BET / 82.5”, stale 515 nodes; archived “final” roadmap pointer mistakenly led to superseded Round15C. README and archive pointers corrected; historical STATUS log marked historical. Current authority remains [DEC-PORTFOLIO-002](../../08-decisions/events/DEC-PORTFOLIO-002.md), with 0 qualified new differentiated Primary Bets.
- **Public availability categories:** OPEN ORIGINAL PAGE, ORIGINAL FULL 10Q FROM PRIOR ROUND, OFFICIAL INDEXED SECTION/CLAIM, OFFICIAL PAGE DIRECT-FETCH RESTRICTED, NOT independently phone-benchmarked. Restricted != disproven or link broken.

## B. Original decision-critical academic/phone source matrix

| Source & paper | Original URL; original-method depth | Direct support | Transferability and independence ceiling |
|---|---|---|---|
| [PAPER-009, When NPUs Are Not Always Faster](../../01-evidence/papers/PAPER-009/deep.md) | https://arxiv.org/abs/2605.27435 — archived FULL_10Q; abs page opened this round | Snapdragon8Gen3 current CPU/NPU prefill/decode/dispatch stage dependence | 1 backend generation, not permanent CPU superiority |
| [PAPER-052, SMEPilot](../../01-evidence/papers/PAPER-052/deep.md) | https://arxiv.org/abs/2606.16332 — FULL_10Q | CPU SME tiled pipelines and packing on Apple/Dimensity/server platforms | M4 Pro Joules are not phone Joules; no same-phone optimized NPU |
| [PAPER-059, llm.npu, ASPLOS 2025](../../01-evidence/papers/PAPER-059/deep.md) | https://doi.org/10.1145/3669940.3707239 ; https://arxiv.org/abs/2407.05858 — FULL_10Q | Snapdragon NPU graph/quantization/task/precision partition | Shared PKU/BUPT research author lineage with ShadowNPU; **not two independent replications** |
| [PAPER-057, ShadowNPU, MobiSys 2026](../../01-evidence/papers/PAPER-057/deep.md) | https://doi.org/10.1145/3745756.3809205 ; https://arxiv.org/abs/2508.16703 — FULL_10Q | Mobile NPU-low-precision attention importance, sparse CPU/GPU high-precision residual | Prefill attention not all decode; shared author group with llm.npu |
| [PAPER-098, HeRo, arXiv author DAC2026 listing](../../01-evidence/papers/PAPER-098/deep.md) | https://arxiv.org/abs/2603.01661 — FULL_10Q | Snapdragon phones Agentic RAG partial DAG/shape affinity/DRAM dynamic scheduling | Same PKU lineage as Agent.xpu, incomplete strongest generic scheduling comparison |
| [PAPER-003, SERENO OSDI 2026](../../01-evidence/papers/PAPER-003/deep.md) | https://www.usenix.org/system/files/osdi26-xin.pdf — archived FULL_10Q | Phone foreground QoE/memory-bandwidth NPU contention | Generic issue, not evidence new Agent HW. Direct PDF not reanalysed in this round |
| [PAPER-119, LLM-as-Scheduler, ACL 2026](../../01-evidence/papers/PAPER-119/deep.md) | https://aclanthology.org/2026.acl-long.581/ — FULL_10Q | Runtime-artifact validation/cheap gate/Agent workflow cost-quality improvement | Cloud benchmarks, software-only, no special private Agent CPU info |
| [PAPER-121, ProgRouter, arXiv v2](../../01-evidence/papers/PAPER-121/deep.md) | https://arxiv.org/abs/2608.25992 — FULL_10Q | Observable coordinator ledger, software semantic scoring/model selection | GPU joules exclude CPU/memory/network, not smartphone battery; publisher venue claim not independently reconfirmed |
| [TOOL-012, PyTorch/Arm SME2 phone](../../01-evidence/tools/TOOL-012/deep.md) | https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/ — original results table **directly reopened** | Vivo X300 SqueezeSAM CPU one core: INT8 555.8→304.1ms, FP16 1163.0→298.2ms; data movement 41.4/39.9% | Coauthored Arm/framework blog, no separate independent Agent or NPU comparator |

The papers are not automatically statistically comparable; paper/model/device/sampling/battery denominators remain local to each source. Report uses no cross-paper numerical speedup arithmetic.

## C. Official code/toolchain/OEM and patent original-URL audit

| Canonical | Authoritative link and current access result | Evidence ceiling |
|---|---|---|
| [TOOL-014 LLVM AArch64 SME](../../01-evidence/tools/TOOL-014/deep.md) | https://llvm.org/docs/AArch64SME.html — **OPEN ORIGINAL** | ABI function attributes, PSTATE.SM and ZA constraints; not measured mobile switching latency |
| [TOOL-015 MLIR ArmSME](../../01-evidence/tools/TOOL-015/deep.md) | https://mlir.llvm.org/docs/Dialects/ArmSME/ — **OPEN ORIGINAL** | Linalg matmul → SME FMOPA is already available |
| [TOOL-016 Arm KleidiAI](../../01-evidence/tools/TOOL-016/deep.md) | https://github.com/ARM-software/kleidiai — **OPEN ORIGINAL GITHUB MIRROR** | Arm GitLab is upstream, GitHub is **same code**, not second independent evidence |
| [TOOL-017 MLIR Linalg](../../01-evidence/tools/TOOL-017/deep.md) | https://mlir.llvm.org/docs/Dialects/Linalg/ — **OPEN ORIGINAL** | Tiling/fusion/vectorization general primitives |
| [TOOL-018 LLVM vectorizers](../../01-evidence/tools/TOOL-018/deep.md) | https://llvm.org/docs/Vectorizers.html — **OPEN ORIGINAL** | CPU cost-model baseline, not Agent-only vectorizer |
| [VENDOR-027 Android17 NPU Manager](../../01-evidence/vendors/VENDOR-027/deep.md) | https://source.android.com/docs/core/perf/npu-manager — **DIRECT WEB FETCH FAILED THIS ROUND** | Earlier Round15C technical review retained; don't imply retail Android phones all ship identical capabilities |
| [VENDOR-029 Qualcomm QNN HTP buffer](../../01-evidence/vendors/VENDOR-029/deep.md) | https://docs.qualcomm.com/nav/home/htp_shared_buffer_tutorial.html?product=924033590759186372 — **OFFICIAL INDEXED TECHNICAL SECTION + TABLE**, full interactive manual access restricted | Buffer type and sequential/concurrent constraints, not universal zero-copy or cross-engine Agent coherent state |
| [VENDOR-032 Apple Foundation Models](../../01-evidence/vendors/VENDOR-032/deep.md) | https://developer.apple.com/documentation/FoundationModels/LanguageModelSession — **OFFICIAL URL JS-REQUIRED**, prior official API/WWDC review retained | App session/tool interface, not silicon execution insight |
| [VENDOR-033 Google Pixel10](../../01-evidence/vendors/VENDOR-033/deep.md) | https://blog.google/products-and-platforms/devices/pixel/tensor-g5-pixel-10/ — **OPEN ORIGINAL** | Tensor G5+Gemini Nano product, vendor in-house comparison only |
| [VENDOR-034 Samsung S26](../../01-evidence/vendors/VENDOR-034/deep.md) | https://news.samsung.com/global/galaxy-unpacked-2026-highlights-from-galaxy-unpacked-the-beginning-of-truly-agentic-ai — **OPEN ORIGINAL** | OEM Agent marketing, Snapdragon S26 Ultra silicon **not a new independent Samsung-designed chip evidence line** |
| [PATENT-024 US9626295B2](../../01-evidence/patents/PATENT-024/claims-round15d.md) | https://patents.google.com/patent/US9626295B2/en — **OPEN indexed original claims** | Cache-demand CPU heterocluster migration, not Agent xPU coherence |
| [PATENT-032 CN121960775A](../../01-evidence/patents/PATENT-032/claims-round15d.md) | https://patents.google.com/patent/CN121960775A/en — **ORIGINAL CLAIM 1 / METADATA VIA INDEXED SEARCH; DIRECT PAGE FAILED** | Agent dialogue cache version and demand-satisfaction, distinct from private future RequiredProgress; pending application |
| [PATENT-033 CN120704926A](../../01-evidence/patents/PATENT-033/claims-round15d.md) | https://patents.google.com/patent/CN120704926A/en — **OPEN indexed original claims** | Multi-Agent software transaction rollback not physical NPU queue cancel |

**Patent legal boundary:** patent-family separation, Google Patents translations and current-status badges are not official legal validity, infringement, licensing or FTO opinions; no comprehensive patent search was performed.

## D. Contradiction/quality and residual risk register

| Key | Potential error | Round15G disposition |
|---|---|---|
| **S-01** | Root README retained old A Primary Bet/82.5 and 515 nodes | **FIXED** to 2026-10-08 current decisions and 632 nodes |
| **S-02** | Historic “final” 2027–2029 report archived but redirected readers to 15C instead of current 15G | **FIXED** with newest management authority |
| **S-03** | STATUS contains long chronology of now-superseded Bet/EXP statements | **MARKED HISTORY**; latest current decision, goal policy and report linked before chronology |
| **S-04** | llm.npu and ShadowNPU same author-lineage; Agent.xpu and HeRo overlap | **GROUP LINEAGE**; cannot count as independent multiple confirmations |
| **S-05** | TOOL-012 Arm authors; official KleidiAI code also Arm | **NOT INDEPENDENT REPLICATION** (different kinds of evidence, same vendor involvement) |
| **S-06** | NPU Manager direct error, Apple page JS, QNN partial manual, CN patent direct error | **BOUNDED ACCESS LABELS**; no blanket 'all sources live verified' |
| **S-07** | Old A/B/R1/R2 EXP gates described in archived documents | **NOT ACTIVE**, not part of this public-only study; do not commission experiments |
| **S-08** | Four workload trends, three architecture themes and three P0 investments confused with 3 independent CPU silicon Bets | **SEPARATED**; zero current evidence-qualified hardware Primary Bets |
| **S-09** | Published smartphone CPU speedup turned into Agent end-to-end CPU-over-NPU conclusion | **REJECTED**; vivo test is SqueezeSAM, Apple joules not phone and default NPU baselines may be weak |

## E. Closure statement

**Bounded management decision supported:** YES, FQ1/2/3/5/6/7 sufficiently answered by scoped primary material and FQ4 explicitly states **existing-ISA compiler/runtime investable, distinct Agent silicon proof absent**. This is a genuine *decision under uncertainty*, not a claim all questions are empirically resolved.

**What is not claimed:** exhaustive Web health check of all sources, patent FTO, all-phone universal claims, original measurements by this project. New original papers or officially published product mechanisms may change future strategic confidence; no ongoing monitoring/task has been created.
