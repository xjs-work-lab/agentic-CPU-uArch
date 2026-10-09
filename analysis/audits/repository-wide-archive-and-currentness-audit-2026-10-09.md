# 全仓目录、链接、当前性与成品归档深度验收 — 2026-10-09

**本次范围：** 已读取 GitHub main 的**未截断完整 Git tree**，随后新增并实际执行 [read-only全仓文件/Markdown相对链接扫描器](../graph/repository_archive_audit.py)，在 GitHub Actions 完整 checkout 上运行，无实验、无设备、无改写研究事实。与 2026-10-09 早先只读11个入口的阶段不同，本轮对**所有文件的存在性、路径分类及全部Markdown中的本地链接**完成扫描。**没有**声称逐字人工重审1042篇Markdown中的科学事实，也未重新在线核对所有外部URL。

## 1. 本轮扫描真实结果

| 指标 | 第一次扫描 | 修复后 |
|---|---:|---:|
| 文件 | 1,053 | **1,055**（增加审计/索引文件） |
| Markdown | 1,040 | **1,042** |
| 目录 | 232 | **232** |
| Markdown中检查的仓内相对链接 | 524 | **615** |
| 失效仓内链接 | **29** | **0** |
| 工具明确标记的主要入口过时项 | **4** | **0** |
| 结题必需路径缺失 | 0 | 0 |

第二轮执行结果：[Complete Repository Archive Audit #37950895274](https://github.com/xjs-work-lab/agentic-CPU-uArch/actions/runs/37950895274) — **SUCCESS**。相关 Artifact 名为 `complete-repository-archive-audit`，其中包含 `archive-tree-audit.json` / `archive-tree-audit.md`，可下载复核。当前主仓另外一次 [V2.4 Graph + Source Identity QA #37950895122](https://github.com/xjs-work-lab/agentic-CPU-uArch/actions/runs/37950895122) — **SUCCESS**。两种检查互补，前者核验文件路径和当前入口，后者核验图谱/来源身份；均不代替科学事实或外部网址实时再审核。

**29处链接的处理：**
- AO-3/AO-4/AO-5 的25条论文/厂商原始资料链接多退一级，已机械更正至确有原文的 `01-evidence/...`。
- R1、R2、B-residual 的历史Stage15实验链接指向不存在的 `07-experiments`；已指向现存 `07-validation/**/EXP-*/deep.md` 并注明这是 V1 历史对象、非当前实验任务。
- 个别Stage14和A设备Trace历史附件不在本仓：**明确标注原文件不存在**，只给出现行组合/结题证据入口，不伪造历史原始记录。
- PPT第04页V3→V2制作规格路径错误已纠正为同目录正确地址。

**其它陈旧索引修复：** `01-evidence/README.md`、`07-validation/README.md` 原“Wave0空仓”说明与实际内容相反；`02-claims`、`03-evidence-cases`、`04-actors`、`05-capabilities`、`06-directions`、`08-decisions` 类似误导性Wave0说明也已归一为现行证据对象职责；新增缺失的 `06-trends/README.md`；修复 `09-roadmap/README.md` 和 `leadership-decision-pack/README.md` 顶部过时“latest pilot”提示；`reports/README.md` / `prototype/README.md` 已澄清空目录/历史原型边界。

## 2. 全仓分类和文件位置合理性

| 现行目录 | 主要职责 | 本轮位置验收 |
|---|---|---|
| `00-project/` | 目标、当前状态、七问结题、数据模型与治理；混有旧迁移审批文件 | **合理但历史噪声大**。新增 `00-project/README.md` 将活跃治理与历史MIGRATION/WAVE0资料分开。不批量移动旧档避免断链 |
| `01-evidence/` | 学术论文、专利、官方厂商/工具资料和发现轮次 | **合理**；修复README非空仓信息；来源身份仍归此处 |
| `02-claims/` | 可证伪/可限定命题 | **合理**；对象存在但不可自动当事实 |
| `03-evidence-cases/` | Evidence-to-Claim支持、削弱与限定 | **合理**；属于证据逻辑，不是论文目录 |
| `04-actors/`、`05-capabilities/` | 机构/人员身份与已有可复用能力 | **合理**；身份排名不作为实验论据 |
| `06-trends/` / `06-opportunities/` / `06-directions/` | 趋势→机会→方向的决策对象层 | **合理**；AO链接已修复，当前状态仍以 `09-roadmap/current.md` 为唯一组合权威 |
| `07-validation/` | 历史V1实验/验证假设与论证 | **位置可保留但性质必须显式标历史**；已更新README，禁止把历史EXP当当前待执行任务 |
| `08-decisions/` | 不可覆写的Decision Event | **合理**；历史决策留档，不覆盖DEC-PORTFOLIO-002与A降级 |
| `09-roadmap/` | 正式管理报告、current组合、领导决策包与历次制图合同 | **合理但制作历史密集**。已更新入口；原始迭代记录仍按历史存放在 `diagram-specs/`，正式材料在 `leadership-decision-pack/archive/` |
| `analysis/` | 机制研究、反证审计、图谱工具/审核脚本 | **合理**；本全仓检查器位于 `analysis/graph/`，当前报告位于 `analysis/audits/` |
| `views/` | 衍生机器图谱，不能覆盖规范化SSOT | **合理**；现有Graph+Identity CI成功 |
| `history/` | 迁移/研究交易历史 | **合理**；与现行决策区分明确 |
| `reports/`、`prototype/` | 空派生报告目录和历史原型索引 | **低优先级历史占位**，保留但README已澄清，不再当当前研究成果 |

**不建议此时大规模搬移** `00-project/MIGRATION-*` 或 `09-roadmap/leadership-decision-pack/diagram-specs/round15*` 文件：内容为历史有效事实，频繁改动相对链接、事务对象、EvidenceCase与DecisionEvent可能引入新的证据漂移。以后确需整理，可做独立“路径重定向+引用全量校验”任务，而不是本次结题必需项。

## 3. “文件是最新”的严格解释

**当前入口与决策状态：PASS。** [CONTINUE-HERE](../../CONTINUE-HERE.md)→[最终结题](../../00-project/final-research-archive-acceptance-2026-10-09.md)→[current.md](../../09-roadmap/current.md)→[最终管理报告](../../09-roadmap/management-final-public-evidence-2027-2029.md)→[PPT成品归档索引](../../09-roadmap/leadership-decision-pack/archive/README.md)为权威链；3项工程方向、3项条件储备、0项充分公开证据支持的新 Agent-only uArch硬件保持一致。历史文件不会被自动重写为新决定。

**逐份科学资料在2026-10-09仍“实时最新”：NOT VERIFIED，不可假称PASS。** 1042份Markdown已作语法层本地链接扫描，不等于人工重读其每篇论文的所有数值/专利法律状态。Round15G审计只覆盖决策关键原始文献，已明确访问受限和独立性边界。当前是公开证据条件下的**有边界结题**；只有关键新证据影响决策时才开展定向更新。

**External URL liveness：NOT VERIFIED**；本轮只区分GitHub相对引用和外部URL，不逐一访问实时网页。**PDF/PPT Windows演示：NOT TESTED**。

## 4. 最终 PPT 是否真的在 GitHub？

**答案：仍然没有。** 全仓主分支Git tree中 `pptx / pdf / zip` **文件数均为0**。此前归档到的，是：
- GitHub的 [17页备注全文](../../09-roadmap/leadership-decision-pack/archive/round16c-17-page-speaker-notes-2026-10-09.md) + [最终文件位置、SHA-256](../../09-roadmap/leadership-decision-pack/archive/README.md) + 页级制作与QA文字；
- ChatGPT Library `/Research-Archives/Agentic-CPU-uArch/2026-10-09/`中的完整PPTX/ZIP/备注/manifest。

**建议真正完成GitHub二进制交付的路径**：创建版本化GitHub Release `uarch-insight-2026-10-09`，将 `Agentic_CPU_uArch_2027-2029_17slides_explanation_first_notes_editable.pptx`、对应PDF和 `Agentic_CPU_uArch_2026-10-09_FINAL_HANDOFF.zip` 添加为 Release Assets，并在上述archive/README补入真实Release链接。这样比向git历史永久写入22MB/31MB文件更适合固定交付包，并可核对SHA-256。也可将单份22MB PPTX提交到 `09-roadmap/leadership-decision-pack/archive/releases/2026-10-09/`，但会增大git仓库，Release更推荐。

**本轮未上传GitHub二进制。原因是当前连接的GitHub工具没有从本地22MB附件直接上传Release Asset的动作，也无法将容器里的字节流安全地传给Git对象API。不能因此写“GitHub PPTX已归档完成”。** 持久Library副本真实存在；GitHub Release/二进制副本属于**明确开放的归档项**，需要经能上传Release资产的GitHub UI或Cloud Browser完成。

PPTX复验 SHA-256：`6d7bb7a19d62c0353f2cbebd9651fed4cb19e874543b39b7063e42cf63f187d5`；ZIP：`02431e8295cf8f7faa4178d02f399553dc2007bb20e8c62d5456f390f891a493`。

## 5. 判定、后续与自动回归

- **PASS**：全仓文件存在/分区清单、1042份Markdown相对链接零失效、有效当前入口、历史/活跃职责标注、Graph与Identity CI、研究决策正式结题。
- **OPEN（仅归档发布，不是研究任务）**：最终 PPTX/PDF/ZIP 尚未上传到GitHub Release，GitHub完整自存档未完成。
- **OPEN / NOT CLAIMED**：逐份原始来源全文“当日最新”、全球专利FTO、外部URL逐个在线可访问、Windows PowerPoint和投影实测。
- [repository_archive_audit.py](../graph/repository_archive_audit.py)和[GitHub Actions自动扫描](../../.github/workflows/repository-archive-audit.yml)已入库，后续涉及关键文件/目录的提交可再次执行全树扫描，并留存机器结果。**本次自动检查不在后台反复搜索新论文**。

**最终声明：科学研究在公开资料限定范围内已结题；研究文档的结构性归档此次实际补强；GitHub上的PPT二进制归档仍待补一项，不能把Library存储说成Github原文件。**
