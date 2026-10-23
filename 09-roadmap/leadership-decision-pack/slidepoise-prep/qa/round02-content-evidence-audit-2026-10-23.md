# Round 02｜17 页内容、证据与视觉关系独立审稿（2026-10-23）

> 状态：**REPO-CROSS-CHECK COMPLETE / IMAGE GATE NOT YET OPEN**  
> 审稿范围：逐页比对 [01 叙事大纲](../01-deck-outline.md)、[02 内容合同](../02-slide-contracts.md)、[03 证据映射](../03-evidence-map.md)、[04 风险边界](../04-risk-boundaries.md)与正式归档的原始资料深读卡、现行决策记录。  
> **独立性的含义**：本轮另起一个审稿视角检查内容，而非由独立人类、第三方 Agent 或全量外部原始文献重做独立复现；不得暗示已进行无关的现场第三方审计。  
> 前置决议：可进入**视觉概念方案设计**；未核 SlidePoise content canvas、具体原文 Figure/Table 与本地备注写入能力前，**不得宣称正式 accepted-slide 或完整 PPTX 已可交付**。

## 1. 审查结论

- **页数和结构**：S01–S17 均有逐页内容合同、图形形式、证据角色、备注任务和拒收项；封面/目录计入 17 页。章节顺序以 2026-10-20 全量综合稿第 17 章为基准。
- **技术组合**：已对照 [current.md](../../../current.md)、[DEC-PORTFOLIO-002](../../../../08-decisions/events/DEC-PORTFOLIO-002.md)、[DEC-A-008](../../../../08-decisions/events/DEC-A-008.md)；3 工程/平台 + 3 条件储备 + 0 独立 Agent 专用硬件主押注，不延用历史 82.5/Primary Bet。
- **主要实证**：重点比对 PAPER-009、PAPER-052、PAPER-057、PAPER-059、PAPER-098、PAPER-003、PAPER-119、PAPER-121、PAPER-044、TOOL-012 深读卡；不同设备、算子/阶段、平均/最高和独立性标注已进入 03。
- **官方/先前技术**：VENDOR-027/029/032 与 PATENT-024/032/033 的能力边界已写入 03/04；官方 API≠商品普及≠实测收益，专利申请≠已批准硬件。
- **图像重建**：保留高密度、主图与原生可编辑性要求；目前仍是**文字内容审稿**，不能代替未来对实际生成图、OpenCV overlay 或 PPTX 实际渲染的审查。

## 2. 逐页审稿清单

状态解释：
- **CONTENT-READY**：当前主张/内容方向和归档资料未发现实质冲突，可设计概念稿；不表示外部原文图已核完。
- **READY-WITH-CHECKPOINT**：在概念布局阶段可继续，但使用某数据/原图/平台接口的精确效果前必须完成列出的检查。
- **UNRELEASED**：未通过图像生成/可编辑重建/备注嵌入验收（所有页共同状态）。

| Slide | 内容审查 | 问题/处理 | 视觉或原始证据检查点 |
|---|---|---|---|
| S01 | CONTENT-READY | 标题限定 Agentic 手机 CPU/协同，非硅片项目启动 | 概念画面不冒充真实芯片布线 |
| S02 | CONTENT-READY | 17 页章节顺序与新稿一致；旧版备注页序不再作排序权威 | 目录与实际页码 01/17–17/17 一致 |
| S03 | CONTENT-READY | **已修文案**：「三项现有工程能力」改为「三项工程与平台能力」，强调 owner 不同 | 决策 3/3/0 不能以同色勾选模拟均已批准 |
| S04 | CONTENT-READY | Agent 生命周期是**概念结构**，不是每个手机的固定路径 | 失败/验证反馈有向，低功耗可跳过执行 |
| S05 | READY-WITH-CHECKPOINT | HeRo 工作流机制已映射，示意 DAG 不能冒充原论文唯一节点图 | 入图前冻结 node/edge 清单并检查每条端点与条件分支 |
| S06 | READY-WITH-CHECKPOINT | **已修文案**：「同一条件」改为「对应测试配置」；单算子与完整 Decode 不同 | 论文原图/绝对单位尚未逐图核，本轮只批准有条件的方向/区间数字文字 |
| S07 | READY-WITH-CHECKPOINT | 两篇 NPU 系统研究相关谱系；倍率可用但不得相乘或排名 | 若做数值图需单独附设备、基线、平均/最大 |
| S08 | READY-WITH-CHECKPOINT | vivo X300 的 CPU SqueezeSAM 与 SMEPilot 不同平台数据已拆开 | CPU 内 SME2 嵌套结构、手机与 M4 Pro 数值绝不合并 |
| S09 | READY-WITH-CHECKPOINT | HeRo 案例、SERENO 吞吐损失是不同指标 | 两例是消融案例，指标单位与基线不能误配 |
| S10 | READY-WITH-CHECKPOINT | **已修文案**：Android AppFunctions 的具体功能要补核官方文档；OutcomeReceipt 是提出的系统合同 | 不可在画面上宣称苹果/安卓已发布同名通用原语 |
| S11 | CONTENT-READY | LAS/ProgRouter/ProAgentBench 是软件强基线；A 假设依然开放 | 软件/云端数据不写成手机能耗测量 |
| S12 | CONTENT-READY | 执行状态/主动低功耗/进度 QoE 是主题，不是三个硅片项目 | 箭头语义区分控制、数据/状态、资源约束 |
| S13 | CONTENT-READY | C1–C3 编译/CPU，C4 跨 Runtime，C5 主属 C/Runtime/OS | 不能画成 CPU 组独立负责所有三项工程 |
| S14 | CONTENT-READY | A/B-residual/R2 为储备，R1/CG-07/CG-01/R3 保留准确状态 | 不使用已通过门槛的绿色勾、完成率/拟建硬件标签 |
| S15 | READY-WITH-CHECKPOINT | 年份属于建议，2029 均保持外部证据条件性 | 横纵层级、箭头条件、虚线研究选项要逐个检查 |
| S16 | CONTENT-READY | **已修文案**：「目前不成立」改为「尚无足够证据支持」，不暗示科学上已证伪 | 事实、推断、假设与证据缺口不能画成简单「从弱到强」可信分数 |
| S17 | CONTENT-READY | 与 S03 现行决策保持一致，研究重开仅限新公开原始证据 | 结尾行动不能写成已批准预算、实验或流片 |

**逐页审稿统计：** 10 页 CONTENT-READY（S01–S04、S11–S14、S16–S17），7 页 READY-WITH-CHECKPOINT（S05–S10、S15）。上述状态仅针对仓内材料和内容合同，17 页均未经过实际 image/PPT 验收。

## 3. 已修复的问题（代码和证据不变，仅明确表达）

| Finding | 原文风险 | 修复位置 | 核验结果 |
|---|---|---|---|
| F01（P1） | 「三项现有工程能力」易忽略 PT-A/C 的平台/系统责任 | 01 S03 及 02 S03 标题 | 已改为「三项工程与平台能力」 |
| F02（P1） | PAPER-009 不同配置数字被总称「同一条件」 | 02 S06 | 已改为「对应测试配置」；S06 仍需原图精确核验 |
| F03（P1） | Android AppFunctions 被直接视为已细核的能力链来源 | 02 S10、03 S10 | 已将具体功能设为**需要官方来源补核** |
| F04（P0） | S16 以「目前不成立的主张」暗示科学上已被证明不存在 | 02 S16 | 已改为「当前尚无足够证据支持的主张」 |
| F05（P1） | 旧版 17 页备注可能错页复用 | 01/02/03/04 统一备注合同 | 明确按新 S01–S17 映射，不按旧页码 |
| F06（P1） | 长期 PPT 制作中的箭头/框体错位可能使概念技术关系变化 | 02/04/05（视觉规范） | 增加 edge from/to/role、OpenCV overlay 与实际 PPT 渲染检查 |

## 4. 四个高风险样页的可执行「图形语义底稿」

以下只是**内容/关系合同**，不是直接交给 PptxGenJS 的坐标。正式设计先做草图再给每个节点/边建身份。

### 4.1 S05 动态 DAG — 先定义边再选择美术排布

**图形对象（建议）**：
- N1 用户目标及上下文（用户应用）
- N2 Agent 计划/调度器（Runtime）
- N3 可选查询重写/分解（条件性阶段）
- N4a/N4b 可并行检索（选择性并行子任务）
- N5 检索结果聚合/重排（依赖部分检索结果）
- N6 推理/生成（可 CPU/GPU/NPU 按算子与阶段调度）
- N7 工具操作（基于生成的已授权动作）
- N8 结果/外部效果验证（OS/应用/Agent Runtime）
- N9 状态记录与决定继续/结束（Runtime）
- CPU/GPU/NPU 作为**可选执行资源池**，不是 N3–N8 的硬编码归属。
- B1 共享 DRAM 带宽/前台 QoE 作为约束边，不是 DAG 任务节点。

**边集合**：
| 边 | 来源→目标 | 类型/含义 |
|---|---|---|
| E01 | N1→N2 | 用户控制请求 |
| E02 | N2→N3 | 条件性阶段展开 |
| E03 | N2→N4a/N4b | 未重写时直接检索的条件路径 |
| E04 | N3→N4a/N4b | 重写/分解后派发检索子任务 |
| E05 | N4a/N4b→N5 | 并行结果依赖，完成要求按具体任务而定 |
| E06 | N5→N6 | 生成/推理的输入数据依赖 |
| E07 | N6→N7 | 若需要工具操作且获授权的条件控制路径 |
| E08 | N6→N8 | 无外部工具操作时对答案/产物验证的条件路径 |
| E09 | N7→N8 | 实际外部效果回读/验证 |
| E10 | N8→N9 | 验证结果与下一步决策 |
| E11 | N9→N2 | 条件性修订/继续，而不是固定无限循环 |
| C01 | B1 - - > N2/资源池 | DRAM/前台 QoE 约束，不能伪装成任务数据流 |

**审图方式**：一名不了解原设计的检查者必须能从画面说出 E05 的汇聚、E07 与 E08 的分支，以及 E11 的有条件回环，否则不通过。

### 4.2 S06 CPU/NPU 比较 — 区间只讲它所测量的事

- 主图 A：**Prefill 阶段**，强调「该 Snapdragon 软件栈被测 NPU 路径更慢」与基线为 6 核 CPU；展示 `1.27–1.62× slower` 不能翻转方向。
- 主图 B：**Decode 中 MUL_MAT 单算子**，强调 NPU 更低延迟，`1.55–1.67× lower latency`；明确与**完整 Decode**分离。
- 右侧解释区：启动/同步/布局复制/CPU fallback/DRAM 争用可抵销局部算子改进，不把概念时间拆分强行做成一个由论文精确实测的瀑布图。
- 若有原论文图的精确图号/轴/单位和逐配置数据，可在下一轮升级为**原生可编辑精准图表**；当前只批准带文字/区间的概念对照图。

### 4.3 S08 CPU/SME2 — 嵌套而不是并列

```text
Mobile SoC
├── CPU cluster
│   └── AArch64 CPU core
│       ├── scalar / general-purpose
│       ├── SIMD / vector
│       └── SME / SME2 instruction-driven matrix capability
│            └── streaming mode / ZA (architectural state)
├── GPU
├── NPU
└── Shared DRAM
```

- SME/SME2 不是 standalone xPU；CPU 具体执行单元并行/复用等微架构细节如无正式来源，不画未证实内部 datapath。
- 面板 A（PAPER-052）：tile 划分、向量/softmax 与矩阵处理流水、离线 packing 的机制；最多展示指定论文最高 3.94×，明确 CPU 基线与不同平台。
- 面板 B（TOOL-012）：vivo X300/SqueezeSAM/单核 CPU：INT8 555.8→304.1 ms，FP16 1163.0→298.2 ms。40% 是具体路径数据移动占比。
- 若面板画不下，应减少面板 A 的数字，不许挤掉设备与模型标签。

### 4.4 S15 三年路线 — 每格是行动建议或研究条件

| 技术层 | 2027 | 2028 | 2029 |
|---|---|---|---|
| CPU / LLVM | 现有 SME2/AArch64 lowering、微内核与 packing/布局 | capability-aware CPU↔NPU 放置与 ABI 合同 | 继续可移植路径；新 ISA 需新公开证据 |
| 异构 Runtime / OS | 动态 DAG、DRAM 与前台 QoE 策略 | NPU load / cancel / reclaim 与跨层资源合同 | 新物理状态机制仅在隔离软件残差后评估 |
| 可信工具执行 | 权限、目标新鲜度、效果验证、失败恢复 | 跨应用安全与动作谱系 | 可移植生命周期/验证合同 |
| 内存与派生状态 | 版本/有效期、共享缓冲、缓存复用 | 跨模型/跨引擎状态失效与兼容性 | B/R2 只保留条件研究，不是硬件时间表 |
| 主动低功耗 | 跟踪 CHRE/AOP/Sensing Hub | 何时唤醒/不行动、隐私同意与帮助价值 | 专用低功耗域只有额外公开收益证据才评估 |

- **颜色+线型联动**：目前建议做的工程路径 = 实体主色；开放研究/尚未批准 = 虚线或空心；只跟进的技术 = 冷灰辅助区。需配图例，不仅靠颜色。
- 箭头只描述「建议随年份深化」或「只有证据成立才升级」；不能表示 2029 已批准流片。

## 5. 仍需解决的 QA 依赖（没有伪装成已完成）

| 依赖 | 目前状态 | 责任环节 | 不解决时的限制 |
|---|---|---|---|
| S05 HeRo 原论文 DAG 图号与端点逐图核 | NOT_DONE | 后续原图素材确认 | 可以做已明确概念身份的自绘 DAG；不能声称忠实复刻某原图 |
| S06 PAPER-009 每个原图柱/单位逐表核 | NOT_DONE | 精确科研图表制作前 | 只准带来源和方向的区间文本/概念对照 |
| S07/S09 多论文数字的同轴可比性 | NOT_COMPARABLE_BY_DEFAULT | 图表设计 | 只做机制并列，若数值单独面板各有基线/设备 |
| S08 正式半页构图数据面板与手机/非手机标注 | SPEC_READY / IMAGE_NOT_DONE | 样页生成 + 审图 | 不允许多平台混绘 |
| S10 Android AppFunctions 具体接口能力官方核 | NOT_DONE | 要使用该主张之前 | 仅可用已审核 Apple/专利与项目建议合同 |
| S15 三年技术层转场语义 | SPEC_READY / IMAGE_NOT_DONE | 样页生成 + 审图 | 不可生成误导性的确定路线 |
| SlidePoise 已安装版本、Profile、正文画布比例、字体 | USER_ENV_NOT_READ | 本地一次性 Preflight | 聊天图像只能 concept_only，非 reconstruction_ready |
| PPTX 中 Speaker Notes 写/读/导出与最终 PowerPoint 检验 | NOT_DONE | Work 模式独立实验 | 不能声称已完成 Notes |
| 原始实物 PNG/GitHub 哈希/Manifest | NOT_DONE | 后续生成与归档 | 不能把文本合同说成图片已经存档 |

## 6. 本轮通过/未通过的范围

**本轮已通过：**
- 17 页内容结构、现行技术组合一致性、归档来源逐页映射；
- 关键手机/软件研究的核心数字在归档深读卡内可以交叉定位；
- 高风险逻辑（SME 在 CPU 内、数值分母、动态 DAG/前台 QoE、2029 条件硬件）已转化为拒收条件；
- 需修订的高风险表达已在 01/02 文件中落实。

**本轮还未通过：**
- 原始论文所有 Figure/Table 的现场逐图核验；
- 正文画布/本地 Profile/真实字体能力；
- 概念图候选、actual accepted-slide、reconstruction、备注写入及 Windows PowerPoint 渲染。

**建议下一个 Gate：** 编制 `07-work-mode-handoff.md` 时，提供最低 token 的一次性 Preflight 检查清单；本地环境只导出配置事实，然后返回聊天窗口完成 S03/S05/S08/S15 的正式 substantive image 设计。若不读本地配置，也可以先生成 concept_only 图供选择视觉方向，但其后可能需要重新适配画布。
