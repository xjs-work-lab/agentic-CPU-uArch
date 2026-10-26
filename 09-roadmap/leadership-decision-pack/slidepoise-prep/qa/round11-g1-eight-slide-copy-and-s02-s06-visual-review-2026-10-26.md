# Round11｜首批八页文案修订 + S02/S06 正式尺寸 PNG 候选的内容审核（2026-10-26）

> **G1 技术内容：8/8 已逐页修订锁定；G2 新图：2/8（S02、S06）已生成并审查为候选，仍待用户视觉认可；G3 PPTX：没有执行。**
>
> 本轮仅围绕 S01、S02、S04、S06、S07、S09、S10、S11。此前 Image2.5 输出的8张技术错页/错数据图**继续隔离，不将其改名作正式输入**。
>
> SSOT：正式[17页大纲](../01-deck-outline.md)、[原内容合同](../02-slide-contracts.md)、[证据图谱](../03-evidence-map.md)、[风险边界](../04-risk-boundaries.md)、[current.md](../../../current.md)、[DEC-PORTFOLIO-002](../../../../08-decisions/events/DEC-PORTFOLIO-002.md)、[DEC-A-008](../../../../08-decisions/events/DEC-A-008.md)。全部旧版讲者备注只作主题参考，**逐页重新写 Notes**。

## 1. 已完成的八页 G1 锁定文案及备注

| Slide | G1 | 实际改动 | 进入绘图的权威文案 |
|---|---|---|---|
| S01 | PASS | 决策型封面缩为范围、主张及抽象 Agent/SoC，不堆十几项技术卡 | [S01](../content-lock-round11/S01-approved-projection-copy-2026-10-26.md) |
| S02 | PASS | 确认四章节与03–05、06–09、10–14、15–17的真实页码；不把章标题误写成问答题 | [S02](../content-lock-round11/S02-approved-projection-copy-2026-10-26.md) |
| S04 | PASS | 增补连续工具、反复异构交接、版本取消恢复、低功耗准入四类Agent工作负载，说明任务只属概念示例 | [S04](../content-lock-round11/S04-approved-projection-copy-2026-10-26.md) |
| S06 | PASS / FIGURE HOLD | 移除原图伪造绝对毫秒柱形，核定Prefill慢1.27–1.62×、Decode MUL_MAT单算子低延迟1.55–1.67×、完整Decode仅约1.05–1.20×、通信路径开销9.9–13% | [S06](../content-lock-round11/S06-approved-projection-copy-2026-10-26.md) |
| S07 | PASS | 用 llm.npu 与 ShadowNPU 两条实际机制链取代泛化CPU/NPU决策图，保留CPU/GPU高精残差和Prefill Attention局限 | [S07](../content-lock-round11/S07-approved-projection-copy-2026-10-26.md) |
| S09 | PASS | HeRo动态阶段DAG / Agent任务时间，与SERENO后台LLM/共享DRAM/前台QoE并列两问题 | [S09](../content-lock-round11/S09-approved-projection-copy-2026-10-26.md) |
| S10 | PASS（平台边界） | 将内存状态页纠正为授权、新鲜绑定、工具动作、实际效果回执、验证/有界恢复；OutcomeReceipt是建议接口 | [S10](../content-lock-round11/S10-approved-projection-copy-2026-10-26.md) |
| S11 | PASS | LAS/ProgRouter/ProAgentBench的可观察软件任务账本对比尚未证明的私有RequiredProgress；不借云端实验宣称手机收益 | [S11](../content-lock-round11/S11-approved-projection-copy-2026-10-26.md) |

以上8份独立文件都包含投影主标题/副标题、卡片短文、证据及不可外推内容，以及**按新页主题重新撰写**的讲者备注。并不是从旧版17页备注按编号复制。

## 2. S06 科学数据复核清单

| 论文原始主张 | 当前合规说法 | 不可变更的分母/边界 |
|---|---|---|
| 被测NPU Prefill | 比6核CPU慢 1.27–1.62× | 该 Snapdragon 8 Gen3/Hexagon v75/特定后端栈；不是NPU全行业表现 |
| Decode 的 MUL_MAT 单算子 | NPU局部延迟低约 1.55–1.67× | 单一算子，不是完整Decode |
| 论文摘要 Decode整条路径 | 仅加速约1.05–1.20× | 是单次Decode路径，不是Agent E2E |
| 通信开销 | 约占被测 NPU 路径 9.9–13.0% | **不是**时延改善9.9–13%，不是可以独立相减的性能增益 |

- 本轮对照仓内 PAPER-009 深读及 arXiv 2605.27435 官方摘要；后者直接印证Prefill最多约1.6×CPU更快、Decode总路径有限收益1.05–1.20×。单算子1.55–1.67×、通信9.9–13.0%来自仓内深读卡，原文所有表格编号和精确配置**尚未逐表对回**。因此不放该页原始 Image2.5 所编造的精确绝对延迟柱形。
- 运行模型不等于阶段拆分，SME/CPU/NPU是不同证据上下文。**S07优化后NPU性能是对S06‘原始特定软件栈’的反证/强基线**，不应两页分别推出CPU永久有利或NPU永久有利。

## 3. 已产出的两个 G2 真尺寸候选

- S02 **2048×1070 正文 PNG + 2048×1152 16:9 frame 预览**：四组章节和每一页码均与 01 大纲一致。原生正文范围 41/1070/41 分层；总页码02/17由预览母版示意，不在正式正文图里重复。
- S06 **2048×1070 正文 PNG + 2048×1152 16:9 frame 预览**：三块证据牌 + 五种可能重叠的非计算开销，通信9.9–13%标为路径成本而非收益。由于之前模型加入了精确假的绝对数据，本页**禁止用绝对柱状图**，直至完成原论文Figure/Table/模型/基线/单位审计。
- 两页 SVG→PNG 实际渲染并打开查看；利用 Noto Sans CJK SC 字体做文本范围估算。S02 **50个文本对象，越界0**；S06 **34个文本对象，越界0**。
- 两页**仅为内容受控/视觉待批的候选**：尚未在用户 Windows 的 Microsoft YaHei / SlidePoise packager 中渲染，未经用户对版式冷读签收。
- 详细文件 SHA-256：见 [本批manifest](round11-eight-slide-content-lock-and-two-png.manifest.json)。实际五份二进制（四 PNG+一 ZIP）已通过 ChatGPT Library 上传和重新 list 核实，路径 `/Agentic-CPU-uArch/slidepoise/round11-g1-content-corrections/`；**GitHub 只存审核记录与文件指纹，尚未直接提交二进制**。

## 4. 下一张图片 Gate

S07/S09/S10/S11 的旧版P0错主题图不能仅改名字；必须从各自新 G1 投影合同重构主图区关系。S01应缩为封面；S04应体现条件触发/工具可选，而非所有步骤串行必经。所有页面的Speaker Notes以源支持、不支持与边界为核心，不得凭Image2.5生成补出未经证实的加速/能耗或新ISA方案。

**未做的部分（明确保留）**：本轮没有完成S01/S04/S07/S09/S10/S11六页的修正版PNG，没有全17页总览；也没有任何新的PPTX。不得把G1文案锁定直接解读为13页所有PNG工作已完成。
