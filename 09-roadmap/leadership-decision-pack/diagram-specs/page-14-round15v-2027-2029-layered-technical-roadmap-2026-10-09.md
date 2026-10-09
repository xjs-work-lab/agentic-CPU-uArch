# 正文第 14 页：2027–2029 分层技术路线（Round15V）

**2026-10-09；状态：纯蓝色可编辑 PPTX/PNG 已制作，通过基础 QA，待用户审阅。**

## 已制作的正文主张
**2027 年先完善现有 CPU 能力，2028 年深化跨层协作；2029 年的新硬件研究取决于新增证据。**

采用 PPT 原生可编辑的 **四行技术层 × 三列年份**矩阵，不使用虚构定量柱图，也不让非证据性技术愿景看起来像厂商新品发布时间。

| 技术层 | 2027 打牢基础 | 2028 跨层联动 | 2029 条件评估 |
|---|---|---|---|
| CPU/LLVM | SME2/Neon、微内核、ABI、布局复用 | 按阶段/精度选择代码并减少重复 packing | 若优化软件仍有不可替代物理瓶颈才研究 |
| Runtime/OS | 强 NPU 后端对照，观察 fallback/sync/QoE | 任务依赖、数据版本、资源争用参与放置 | 证据仍不足时不设新跨引擎硬件接口排期 |
| Agent/App | 目标权限、真实工具效果和受控恢复 | 跨应用任务修订与权限/结果追踪 | 优先可移植软件规则，不默默认定需专用语义指令 |
| 低功耗/内存 | CHRE、共享缓冲、通用缓存基础 | 关联唤醒、数据版本、整机 QoE/隐私 | 只跟踪存在明确剩余缺口的候选 |

**特别边界**：这是基于公开信息的技术先后顺序建议，**不是**团队已授权的资源、芯片量产、发布或测试日程；本研究不会自发开展 PoC、真机实验、仿真。

## 证据及逐来源讲者备注
1. [项目 2027–2029 权威分层路线](https://github.com/xjs-work-lab/agentic-CPU-uArch/blob/main/09-roadmap/round15e-integrated-public-roadmap-2027-2029.md)：说明分年/层研究建议，非内部已批准排期。
2. [LLVM SME](https://llvm.org/docs/AArch64SME.html)：已知 CPU ABI/streaming/ZA 支撑，非所有平台都有 SME2。
3. [MLIR ArmSME](https://mlir.llvm.org/docs/Dialects/ArmSME/)：证明 linalg.matmul 可 lower 到 SME FMOPA 的示例，不保证所有模型最优。
4. [HeRo](https://arxiv.org/abs/2603.01661)：支持动态跨引擎软件编排研究，不支持新硬件必需结论。
5. [Android CHRE](https://source.android.com/docs/core/interaction/contexthub)：支持低功耗处理器环境与部分 AP offload，非完整 Agent 平台。
6. [Apple Tool Calling](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling)：支持工具调用机制，不直接保证跨应用目标完成。

**六份来源的身份、已证明、未证明、对应技术单元均写入本页 PowerPoint 演讲者备注**，并独立标明“研究综合推断”和待观察证据。

## 实物与质量
三页合并 PPTX 与当前页 PNG `page-2.png` 位于 `/mnt/data/round15v_slides13_15/`；有 58 个原生可编辑图形/文字、1 张独立芯片插图和4个正文可点击来源链接，页码 `14 / 15`。已检查 1920×1080 渲染、无禁用商业化用词。尚待用户验收和17页合并。
