# Agentic CPU-uArch — 2027–2029 手机 Agentic AI 技术洞察 SSOT

> 研究权威：xjs-work-lab/agentic-CPU-uArch · V2.2 Research SSOT / Graph V2.4 · 2026-10-08 · **Round15G 公开资料研究交付版本**。
>
> **硬性约束：仅研究公开论文、专利、厂商技术资料和已发表第三方实验结果。没有项目自有实验、手机测试、仿真、PoC，也不以其作为结论完成门槛。**

## 当前有效入口（按推荐阅读顺序）

1. **[管理层技术洞察与 2027–2029 路线图](09-roadmap/management-final-public-evidence-2027-2029.md)** — 4 个负载变化、F/P/V 主线、投资/储备/Kill、逐年架构路线。
2. **[当前正式投资组合](09-roadmap/current.md)** — 唯一有效的 Direction 投资 SSOT；决策事件 [DEC-PORTFOLIO-002](08-decisions/events/DEC-PORTFOLIO-002.md)。
3. **[最终七问与技术覆盖累计状态](00-project/final-questions-status.md)** — 每轮回顾目标与进度的权威文件。
4. **[最终原始链接、独立性和冲突审计](analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md)** — 审查分级和不可迁移边界。
5. **[CPU/LLVM/SME2 技术机制深读与强 NPU 反证](analysis/engineering/round15f-cpu-llvm-compiler-pressure-2026-10-08.md)**。
6. [项目当前状态与历史记录](00-project/STATUS.md) · [研究目标约束](00-project/research-goal-lock-agentic-mobile.md) · [当前研究图谱](views/graph/current.json)。

## 正式投资快照 — 截至 2026-10-08

| 决策类型 | 当前方向 | 重要限制 |
|---|---|---|
| **优先工程 / 平台投入 3 项** | CG-06 CPU/LLVM 异构快路径；PT-A 可信 Agent 动作；C 异构资源/QoE 软件系统 | 不能算成 3 个原创 CPU 硬件 Primary Bets |
| **独立差异化 Primary Bets：0** | 不强行填足期望的 2–3 个名额 | 没有足够独立公开证据证明 Agent 专用 CPU-uArch 新增价值 |
| **核心战略研究储备 3 项** | A 私有 RequiredProgress；B-residual 派生物理状态有效性；R2 CPU continuation locality | 机会仍是假设，不等于新硅片项目 |
| **Follow / Explore / Watch** | CG-07 低功耗 Agent、CG-01 Flex Cache、R1 post-ready timing | 已有通用技术/产品路径 |
| **Kill / Blocked** | R3 Agent 语义 ISA；普通缓存/调度/事务/零拷贝机制的新颖性主张 | Kill 精确投资主张，不否认相关平台功能有价值 |

**决策修正已正式完成：** A 在 2026-10-07 旧方案中列为 PRIMARY_BET/82.5，已由 [DEC-A-008](08-decisions/events/DEC-A-008.md) 更改为 **CONDITIONAL_RESERVE / HYPOTHESIS_OPEN**。82.5 仅历史评分，不是当前项目成功概率或预算排名。历史 [旧“最终路线图”](09-roadmap/final-2027-2029.md) 和 [2027 实验规划](09-roadmap/2027-execution-plan.md) 完全归档，所有 EXP 指令不再生效。

## 研究领域和数据管理

范围：手机优先，2027–2029，Agent 体验、LLVM/AArch64、Runtime/OS、CPU↔GPU↔NPU、Cache/内存/SoC、低功耗。结论区分公开直接事实、交叉来源推断、尚未确证的架构假设。

**上轮已验证图谱基数（Round15F）：632 规范节点、1,202 正向语义边、1,202 反向边、1,148 依赖边。** Round15G 只完成报告与一致性审计，没有人为添加无价值证据节点。

原始 SOURCE 按 DOI/arXiv/专利公开号/同族/原始 URL 去重，不能把同组论文或 OEM 对相同 SoC 的宣传当成独立复现。重要 Direction 变更必须有 Decision Event。轮末汇报遵循 [固定研究轮末协议](00-project/round-end-reporting-contract.md)。

历史 V1 冻结版本：xiejinsen/agentic-CPU-uArch@960abb4ef50f050da3c6784d30826053d42e5c5d；迁移 MIG-20261006-02、批准日期 2026-10-06；主分支为唯一长期权威。
