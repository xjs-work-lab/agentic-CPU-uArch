# 15 页正文：按内容选择绘图语言与最终素材（v1）

> 2026-10-08。**这是制图工具决策表，不修改原先 15 页战略结论。** 制图规范见 [多语言制图政策](diagram-authoring-policy-v1-2026-10-08.md)，研究依据见 [内容蓝图](../content-storyboard-v1-2026-10-08.md)。本表中的工具为推荐，不代表已完成该语言的解析或素材制作。

| 页 | 最主要的图/问题 | 逻辑设计首选 | 最终呈现建议 | 必须警惕 |
|---|---|---|---|---|
| 1 | Agent 到 Runtime 再到 CPU/NPU 的任务和反馈 | Mermaid / DOT（少节点、并列层级） | Direct SVG 或 PPT connectors + Image Generator 图标 | LLVM 不在硬件执行器列；不是 CPU 统管 NPU |
| 2 | Agent 跨层工具时序、验证与恢复 | **PlantUML sequence**，另用 Mermaid 标记结果状态分支 | SVG/PPT 分层泳道、横向时间轴 | 回执 ≠ 用户目标完成；失败与取消不同终态 |
| 3 | 哪种处理器能降低完整阶段成本？ | 简单 Mermaid 决策流程 + 文字成本定义 | PPT 路径选择决策树和三列解释表 | 五种成本可能重叠，不画伪比例 |
| 4 | Snapdragon CPU/NPU 多口径时延证据 | 论文数值表、轴和对照规范 | 真数据柱图/原文图（核权属后） | `call-usec` ≠ NPU 纯 kernel；Stage aggregated ≠ 完整 Agent E2E |
| 5 | llm.npu 与 ShadowNPU 不同的软件增强路径 | 分开的 Mermaid/PlantUML component 方法摘要；需要时 Direct SVG | 双 panel 技术图 + 原文关键 Fig | 两篇不能拼成一条方法流水 |
| 6 | vivo X300 单 CPU 核 SME2 on/off | 锁定数据表、比较单位与尺度 | 可编辑 PPT 数据条 + 小型 layout SVG | 不属于 Agent/NPU 对比 |
| 7 | SMEPilot roofline、tile、phase pipeline 与 layout | **Direct SVG**，需要时 DOT 表示分支与依赖 | 核对 Methods 的结构图 + 真实 Ablation | SME 与 CPU 核并非两个独立 SoC 处理器 |
| 8 | HeRo 部分 DAG/关键性、异构执行、带宽 | **Graphviz DOT** 的 cluster+DAG | 基于 DOT 的层次骨架 + 论文证据图 | DAG 不固定；PU 可选分配；实验条件分开 |
| 9 | LLVM/编译、CPU 内核、Runtime/OS 技术责任 | **PlantUML component** 或 DOT cluster | Direct SVG/PPT 分层架构 + owner 说明 | 编译期和运行期关系不能混画 |
| 10 | 工具执行合法性 vs 派生状态有效性 | **PlantUML sequence/state**，分开两张 | 双泳道 SVG / 两种不同状态图 | 不虚构已存在统一硬件状态协议 |
| 11 | 主动事件是否触发 CPU/NPU 唤醒 | Mermaid decision flow / PlantUML activity | 可编辑 PPT 决策树 | 无动作也是合法终态，需遵守隐私 |
| 12 | 新 Agent 专用 CPU 硬件是否过证据门 | Mermaid / PlantUML activity | 4 道清晰决策门 + 结论说明 | “证据不足” ≠ “物理证明无价值” |
| 13 | 工程、研究储备、Watch、暂不立项 | 结构化 Markdown 数据合同 | **PPT 原生表格/少量 SmartArt** | 工程 3、条件储备 3、差异化 Bet 0 |
| 14 | 2027–2029 分层技术路线 | Markdown 年份×层矩阵 | PPT 可编辑矩阵/时间轴 | 非正式人力、预算、流片时间表 |
| 15 | 从可公开证据到技术管理决策 | Markdown 三列表 | PPT 原生矩阵 + 清晰决策句 | 不把技术建议写成已获批承诺 |

## 生产原则

- 主体内容是一张真实数据图时：**数据合同优先，不强加任何流程语言**。
- 关系分支复杂时：**先完成可机器/人工检查的源拓扑**，再用 Image Generator 做统一视觉美化。
- 需要严格时序与同步语义时：优先 PlantUML sequence；交叉 DAG 且要可控层级时优先 Graphviz；机制中 CPU/NPU 具体分区和资料自带关键图时优先 Direct SVG。
- 所有 SVG/Graphviz/PlantUML 视觉只是表达层；技术真值属于 Markdown + 原始文献，不由图的风格决定。
- 绘图代码不强迫一个文件同时有 3–4 种语言；只保留能清晰表达该图的**最小必要源**与一份清楚的对应说明。

## 下一轮三页代表性试制选择

- **第 5 页**：双论文 NPU 优化对比，检查严谨方法图与视觉创新能否兼得。
- **第 6 页**：真实数量化图，检验文字和数值不能被 Image Generator 改写。
- **第 8 页**：较复杂的 Agent DAG，使用 DOT 布局骨架检验箭头的准确率。

三页先通过各自的原始论文/数据/结构审查，再设计 Image Generator 的背景、图标、卡片与高保真色彩；最终用 PPT 精确叠字和可点击来源。其余页根据结果复制制作规范，不复制未经审查的图片内容。
