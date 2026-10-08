# 技术领导汇报《逐页内容—逻辑—证据—视觉设计蓝图》v1.0

日期：2026-10-08 · 设计阶段，不是 PPT、PNG 或新增技术研究。基于已完成的 Round15G 公开证据报告、Round15H 决策包、Round15F CPU/LLVM 原始机制卡。

> **最重要的制作纪律：先把技术故事讲完整，再决定图是什么样；先让页内证据与因果关系成立，再画图和排版；最后才考虑配色、图标和动画。**
>
> 受众：有 CPU/uArch、OS、编译技术背景，但不参与研究日常的技术管理层。**正文不显示研究仓库中 CG-06 / PT-A / A / B-residual / R2、PAPER-009 等内部代号**。内部 ID 只用在制作表、讲者备注和附录引用索引；正文使用完整的人能读懂的技术名称。
>
> 正式投资状态以 [当前组合](../current.md) 为准；事实以 [Round15G 管理报告](../management-final-public-evidence-2027-2029.md)、[原始来源审计](../../analysis/audits/round15g-final-source-and-ssot-audit-2026-10-08.md) 和原始论文为准。本蓝图不改变任何投资判断。

## 0. 先设计「故事」，而不是先设计「页面」

**目标问题**：2027–2029 年端侧 Agent 将怎样改变手机工作负载？什么有别于现有 CPU/NPU/Runtime/OS 优化？技术团队应当投向哪里，不该投向哪里？

**核心回答 / 结论先行**：Agent 把手机 AI 从一次模型请求变成可中断、可恢复、跨应用、跨 CPU/GPU/NPU 的动态执行系统。这提高了可编程控制、软件编译适配、阶段分工、内存状态和前台 QoE 的重要性；**但最强已公开软件/既有 ISA 基线很强，暂不足以证明必须创造专用 Agent CPU-uArch 硬件**。

**叙事弧（给作者使用，严禁写成幻灯片标题）**

- ① **为什么问题正在改变**：完整手机 Agent 事务而不是单次 LLM kernel；一个真实可说明的业务场景将问题显性化。
- ② **真正的技术矛盾是什么**：计算能力更强的 NPU 不代表所有阶段的端到端时延更低；异构卸载/同步/回退与流动的中间数据支配阶段收益。
- ③ **公开论文证据一正一反**：指定 Snapdragon 栈 CPU/NPU crossover；vivo X300 / SMEPilot 的 CPU+SME2 能力；llm.npu/ShadowNPU 强化 NPU；HeRo 证明 software-Agent scheduler 已具强收益。
- ④ **把证据转换为可控技术内容**：LLVM、SME ABI、微内核与布局、CPU-NPU partition、Runtime/OS QoE；以及可信动作、状态生命周期和低功耗 admission。
- ⑤ **回答“哪些不是我们应该赌的 CPU 硬件创新”**：严格区分通用缓存、已有优先级、现有 CHRE、软件进度控制与真正独特的新物理因果链。
- ⑥ **形成技术管理决策**：优先建设三项工程/平台能力、保留三项极窄条件研究问题、不在现有证据下立 Agent 专用 CPU ISA/uArch Bet，规划 2027/28/29 技术路线。

**说服逻辑的充分性：** 每个页面至少有【背景/问题】→【机制或原始证据】→【推理】→【本页结论】四环，且不能把【未由论文证明】的推理写成论文实测。

## 1. 统一的逐页信息与图形规范

每页采用**完整判断句标题**（通常 28–50 个汉字；按视觉空间做合理断行，不用“金字塔”“证据第 X 页”之类方法学/项目文件名当标题）。

每页从上往下：**顶层高密度结论**（一句告诉决策含义）→ **占页面最大面积的主图/主证据**（能够自洽地表达机制/数据）→ **相邻解释块**（说明为什么出现、怎么读、有什么制约）→ **底部“因此建议/不应该得出的结论”** → **原始来源、设备/模型/版本小字**。每个视觉对象必须有可读的标题、图例或标注；不允许只有“小胶囊词语”。

视觉功能分类：
- **A 原论文原图**：只有在完整核对 PDF 图号、方法与使用许可/署名后才考虑按原样局部嵌入；保留期刊/作者/出处、实验条件，不能裁掉会影响结论的图例。不因用户想要论文图就未经核对编造截屏。
- **B 机制重绘**：结构复杂但可从 Methods 重建的，做准确的可编辑矢量流程；标明“依据作者方法重绘（非论文原图）”，不伪造真实系统 trace。
- **C 原始数据重画**：同原论文条件的柱图、比值图、方差或实验表格，数据值保持原始分母与方向，页脚按来源标注；PowerPoint 原生形状/图表优先。
- **D 概念场景图**：作者自制的*说明性例子*，明确写“示意/非实测”而不是伪装成论文实测过程。
- **E 外部绘图插件或 SVG**：适合复杂 DAG、SoC 层次/跨引擎生命周期等图。先编审节点和边清单、布局草图，再由 Figma/Canva/矢量绘制工具生成；导入 PNG/SVG 时同时提供可编辑版本或替代图层。**插件只是绘图执行，不代替机制正确性审查**。
- **F 纯文字块**：只承担定义、因果说明、局限和管理决策；每段用完整主谓宾句，不做大面积“关键词瓷砖”。

**版面密度目标**：让技术专家在一分钟内完成一次“读图—看证据—得出结果”的阅读，而不是盲目把字号缩到看不清；长论文方法可进入备份页。重要证据最好有独立的“实验条件/结果/反例/含义”模块。

**制作前的两个质检关口**：
1. **逻辑验收**：不依赖讲解，仅看页面能否说清背景→因果→来源条件→投资含义？项目内部编号是否全部外移？
2. **视觉验收**：每一条箭头两端准确指向对象、方向和 label 都正确，避免跨越无法辨认的线；任何数值与图形尺度一致，文字不碰撞、未隐藏。PDF/PNG 放大看正文与页脚，缩略图看总结构。

---

## 第 1 页｜先给有技术根据的战略答案，而不是只列代号和 03/03/00

**结论式标题**：**未来三年，手机 Agent 的 CPU 机会主要是灵活控制、现有 ISA 上的选择性推理和异构协同，而不是立即增加专用语义指令。**

**这页必须解释的三个事实**：
1. 一个 Agent 任务会连续执行 LLM 推理、App/工具动作、状态核验、模型/精度切换、后台恢复；这是 CPU/LLVM/OS 都能接触到的技术链，而不只是 NPU TOPS。
2. **第一类：值得建设的工程/平台能力**：CPU/LLVM 现有 ISA fast path；可信 Agent 工具动作和结果确认；OS/Runtime 对 CPU/NPU 资源和 QoE 的协调。每个方向必须写出**所解决的问题、技术负责层、最终改善的用户体验**，不能只写方向编号。
3. **第二类：有条件的研究储备**：真正不可重建的 Agent 语义进度信息、跨引擎派生物理状态有效性、CPU 任务续执行局部性。都需标“尚无足够独立公开证据证明值得新做硅片”。

**页面视觉草图**：
- 左侧 60%：**端侧 Agent 执行体系结构图**。App/Agent 工作流（发生事件、形成子任务、获授权、执行业务动作、验证效果）→ Runtime/OS（任务 DAG、deadline、QoE 与 NPU 资源）→ CPU/LLVM（控制＋小阶段、SME2/Neon 微内核）↔ GPU/NPU（适合的吞吐密集算子）→ Memory/state（版本化数据与派生缓存）。**每个大层至少 2–3 句用途+数据流解释**。连线分“调用/数据/反馈”，要有图例。
- 右侧 40%：标题为“投资建议（截至 2026-10-08）”，用三个**语义标题**的模块，不画仿序号的巨大“03”：“优先建设的工程能力（3类）”“保留判断空间的研究问题（3类）”“暂不支持立项的专用硬件（0项）”。每模块写出完整名称及本质原因，**不放研究 ID**。
- 底部横贯：一句边界“工程价值 ≠ 新芯片独特性；现行公开证据不证明 Agent 需要新 CPU ISA”。

**文字不能省略**：每一类必须回答“技术机制—现有基线—为什么投/不投”；例如不能只写“持续目标 / 可信动作”。

**素材与来源**：[正式投资组合](../current.md)、[完整报告](../management-final-public-evidence-2027-2029.md)。这一页是跨来源策略推断，不放无意义论文插图。

**承接下一页**：“为什么一个传统 LLM 性能优化问题会演变成跨层系统问题？”

## 第 2 页｜用完整业务机制证明 Agent 工作负载与单次推理根本不同

**结论式标题**：**Agent 从“输入一次、推理一次、输出一次”演变为可中断、跨应用、可修订的长链执行，CPU/OS 开始承担更多控制与状态责任。**

**需要写明的背景**：传统任务边界明确，模型的 I/O 生命周期短；Agent 的工具调用可能真实修改日历、支付或设备设置，模型输出不是“已成功执行”的证明；前台任务与后台主动事件竞争资源。

**核心执行例子（明确写概念示意，非任一论文完整真实 trace）**：
- 用户请求“出行前重新安排日程” → Agent 解析目标、读取允许访问的日程 → 判断是否需要发起多次检索/推理 → 按权限选择工具并在执行前确认具体目标 → App 返回可核验效果 → 校验是否完成目标 → 更新会话与派生缓存的版本 → 如被打断则安全恢复/放弃旧结果。
- 标记每个步骤的**异构处理器可能归属和已知不确定性**，例如 CPU 执行控制/权限、NPU/GPU 承担适合的模型算子、OS 分配/回收资源。

**主视觉**：
- 左 25%：传统模型链，带完整说明“可预先固定路径、少数执行边界、低状态复杂度”。
- 中 55%：**泳道图**：Agent/App | Runtime/OS | CPU/LLVM | NPU/GPU | 外部工具/状态；每个节点写出触发条件与结果，回环必须有明确起止点（重新规划、校验失败、暂停恢复）。
- 右 20%：四项**新问题的因果链**：动态 shape→放置成本；tool action→可信结果；上下文版本→缓存有效性；事件触发→帮助质量×电量。
- 图下用 3 句话解释“其中哪些是已经被标准 Runtime/OS 覆盖的能力，哪些仍是研究问题”。

**图形生产**：泳道多分支可用矢量插件/SVG 制作，或 PowerPoint 分组可编辑线/块；**不允许跨泳道线段脱离端点**。允许概念图，无须造论文截图。

**来源**：[HeRo](https://arxiv.org/abs/2603.01661)、[Apple Foundation Models 官方 session API](https://developer.apple.com/documentation/FoundationModels/LanguageModelSession)、[Android CHRE](https://source.android.com/docs/core/interaction/contexthub)。官方材料证明现有接口，概念例子不冒充其中任何用户实测。

**承接**：“复杂流程为何不是更大的 NPU 就能解决？”

## 第 3 页｜分解端到端 CPU/NPU 阶段耗时，说明真正的成本来自哪里

**结论式标题**：**阶段最优处理器取决于计算时间与图准备、精度转换、数据移动、同步和回退的总和，不能按 NPU TOPS 一次性决定。**

**证据层逻辑**：
1. 端到端阶段时间包括：模型/子图准备、数据类型和布局调整、Kernel 执行、同步/拷贝、CPU fallback；这是软件/系统总和而非架构单指标。
2. Prefill 和 Decode 的 GEMV/attention、短工具调用、短多模型 stage 的密度/重复性完全不同。
3. 需要先选最强优化 NPU baseline 才能判断 CPU 是否真有长久竞争优势。

**主视觉**：四条横向**阶段成本堆叠图**（注意是概念比例，不允许装作数据；如无可比真实比例，就统一绘制等长分段并标“非定量结构示意”），覆盖 long prefill、short decode、precision-sensitive attention、Agent scheduler/control。每条右侧对应处理器权衡“为何可能 CPU/NPU/混合”。
- 顶部左：“决定归属的 5 个成本分量”概念分类；
- 右部：一张“逐阶段判定树”：NPU 支持吗 → shape 可复用吗 → copy/sync 是否抵消 Kernel 收益 → 是否有前台 QoE 约束？
- 底部：**这不是实测归属图**，具体论据在下一页的 Snapdragon 论文与后续优化 NPU 论文。

**文本层**：解释“Kernel latency ≠ end-to-end latency”“算子被 NPU 支持 ≠ 整图可高效 offload”“CPU fast path 角色随软件栈演进”。

**素材方式**：原创机制信息图（SVG/可编辑），不使用伪定量色块长度。

**承接**：“公开同机数据到底证明了什么？”

## 第 4 页｜一篇 Snapdragon 实机论文提供了 CPU/NPU crossover 的直接但有限证据

**结论式标题**：**Snapdragon 8 Gen 3 实测中，NPU 的 Decode GEMV 内核虽快，但 Prefill 和端到端收益受软件回退与通信显著制约。**

**背景和实验条件必须完整出现**：PAPER-009 *When NPUs Are Not Always Faster*；Snapdragon 8 Gen 3、Hexagon v75；指定 Android/llama.cpp 后端、论文中测试的模型/运行条件。比值的**分子分母分别是什么**必须在图题处标明。
- Prefill：NPU 路径 **1.27–1.62 倍于 6 核 CPU 的执行时间**（较慢）。
- Decode 核心 MUL_MAT：NPU Kernel **1.55–1.67× 较低时延/更快**（比值要按论文原表定义，制作时再次逐项核对原文）。
- Decode 端到端：CPU/NPU 优势比仅约 **1.05–1.20×**，通信约占 NPU 路径 **9.9–13.0%**（按论文定义）。

**主图（占 55%）**：三个原始数据对比 panel：Prefill、Decode Kernel、Decode End-to-end；**不能共用一根没有标明方向的速度条**。每 panel 的副标题是“谁作为基线/优化对象、设备/模型/测试栈”。若能取得原文准确图号与许可，优先嵌入论文原图局部并标示；否则以原数据重绘三个小倍数图和细化的背景分解图。

**辅图（25%）**：从 prefill/decode stage → NPU graph → fallback/copy/sync → measured E2E 的带注释流程；这页绝不声称该论文是未来最优 NPU 后端。

**右侧解释（20%）**：“为何 Kernel 比整体快得多？”“哪些限制随 NPU 编译软件优化而改变？”“当年某栈的 CPU 优势不能外推 2029”。

**底部结论**：**投资 CPU/LLVM 的跨阶段可选执行，不投资‘所有 Agent Prefill 永远该上 CPU’的固化硬件判断。**

**原始链接**：[PAPER-009](https://arxiv.org/abs/2605.27435)；[深读卡](../../01-evidence/papers/PAPER-009/deep.md)。来源是已发表论文作者结果，非本项目测量。

**承接**：“NPU 软件改进会怎样改变这张图？”

## 第 5 页｜强 NPU 软件论文提供决定性反证：CPU 胜出范围不是常数

**结论式标题**：**llm.npu 与 ShadowNPU 通过图重构、低精度重要性估计和稀疏高精度残差，把原本留在 CPU/GPU 的工作重新交给 NPU。**

**论证链**：
1. 现有 NPU 图/量化/动态形状限制会让某些 stage CPU/GPU fallback；但限制一部分属于编译软件栈，而不是硬件必然。
2. ASPLOS 2025 llm.npu 的图/分块/调度软件优化降低某些 fallback 和 graph overhead。
3. MobiSys 2026 ShadowNPU 将 Prefill attention 分为 NPU 低精度重要性估计和 CPU/GPU 稀疏高精度残差，再利用流水重叠；**Decode attention 仍有 CPU/GPU 部分**。
4. 两项研究同一学术研究链条，**不能当两次独立可重复实验**。定量性能与质量指标必须局限在各论文特定 workload，且不能横向相乘。

**主视觉**：**Before/After 双泳道技术机制**；左为整段 CPU/GPU fallback；右为 NPU quantized graph / importance → selected sparse residual on CPU/GPU → merge/overlap。每条边写清传的数据类型或 token/head subset；**在右侧特别标出 Decode 不被完整覆盖**。

**证据模块**：可采用论文实际 architecture figure（核对许可、图号和原图注后局部嵌入）＋根据实际 Methods 重绘的简化分工图。必须在图区明确区分“论文原图”“依据方法重绘”。

**解释文字**：过去 CPU 算子快不说明以后仍优；CPU 团队应投的是可选角色/精度/布局接口，与 NPU 软件共同演进。

**出处**：[llm.npu](https://doi.org/10.1145/3669940.3707239)、[ShadowNPU](https://doi.org/10.1145/3745756.3809205)、[其深读](../../01-evidence/papers/PAPER-057/deep.md)。

**承接**：“在 NPU 越来越强的情况下，CPU 是否仍有具体实证价值？”

## 第 6 页｜用同机同任务的 CPU 实测，证明现有 ISA 值得投入（但不冒充 CPU/NPU 对比）

**结论式标题**：**vivo X300 单核 CPU 实测显示 SME2 使特定视觉模型显著加速，但优化后约 40% 时间仍在数据搬运，布局与微内核同样关键。**

**绝对必须保持的实验条件**：PyTorch/ExecuTorch + Arm 官方共同发布的 vivo X300、SqueezeSAM、Normal mode、单 CPU 核；比较 CPU 上 SME2 disabled/enabled；不是 Agent 工作流也不是 NPU 优劣实验。
- INT8：**555.8 → 304.1 ms**。
- FP16：**1163.0 → 298.2 ms**。
- 加速后作者报告的 Data Movement 占时：INT8 **41.4%**，FP16 **39.9%**。
- 作者含 Arm 人员，不应把同工具链公开 blog 与厂商自述当第三方多次证据。

**主视觉（55%）**：原始数据**成对水平柱图**，同一精度显示 SME2 OFF 与 ON，以 ms 为同一数轴，不复用 V3 中易产生尺度歧义的宽度处理；再加两个分割条说明 post-optimization 时间中的数据移动分数。
**辅图（25%）**：数据路径 CPU L1/L2 ↔ packed-layout ↔ SME kernel 的简化瓶颈示意，清楚表达为何“矩阵核更快”不代表 end-to-end 同比例快。
**解释（20%）**：“这项证据支持现有 ISA + packing/layout 的工程方向；不支持 CPU 全面超越优化 NPU；且不证明 Agent 总任务耗时下降。”

**图形方式**：原生 PPT 横向实数轴或图表＋可编辑数据路径。原文相关性能表可以作为来源核对缩图，但不代替重绘数据。

**出处**：[TOOL-012 官方原始表](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/)、[source card](../../01-evidence/tools/TOOL-012/deep.md)。

**承接**：“在已有 SME2 指令下，系统性的软件编排还能有什么增量？”

## 第 7 页｜SMEPilot 将能力从指令级加速推进到整个 CPU 算子执行计划

**结论式标题**：**SMEPilot 的收益来自算子角色规划、CPU/SME 并行、tile 划分和 layout 重用，证明现有硬件仍有大量编译与运行时优化空间。**

**逐项证据**：[SMEPilot](https://arxiv.org/abs/2606.16332) 的 Methods/ablation 表明：
- 公开测试含 **Dimensity 9500**、Apple M4 Pro 和服务器等平台；“最高 **3.94×**”是受测配置中的 up to，不可用作所有手机。
- 不做 Tile Partition，指定 GEMM latency **×1.46**；不做 Attention Pipeline，指定 prefill attention **×2.07**。
- 错误地在线 packing，可使 cited decode GEMV **0.52 → 1.71 ms**。
- 功耗/能量在 Apple M4 Pro 平台报告，**不是手机整机能耗证据**。

**核心图（60%）**：按论文 Methods 准确重绘 **Profile / shape characterization → online planning → CPU-only / SME-only / pipelined parallel paths → packed KV/weight layout reuse**。建议让机制设计师输出可编辑 SVG，必要时对照论文原始系统图，不要省略数据格式和 lifetime。
**右侧（40%）**：三组真实 ablation 数据小图，每组旁边一整句“去掉什么→损失什么→说明哪个成本最关键”；再标设备和分母。
**页脚推论**：将现有 ISA 的编译/runtime/packing 组合做精，比起没有专属 Agent 工作负载证据就新建 ISA，更符合当前公开研究。

**出处**：[原论文](https://arxiv.org/abs/2606.16332)；[深读卡](../../01-evidence/papers/PAPER-052/deep.md)。

**承接**：“除了单个算子与 CPU 流水，Agent 全任务还能从纯软件调度获益多少？”

## 第 8 页｜真实手机 Agentic RAG 说明 DAG 与带宽软件调度已经很强

**结论式标题**：**HeRo 在商业 Snapdragon 手机上利用任务 DAG、动态阶段分区和共享 DRAM 约束提高端到端效率，软件已可获取大部分关键调度信息。**

**必要实验环境**：Redmi K80 / OnePlus 13；Agentic RAG 工作流；论文报告 up to **10.94× 相对 GPU-only 特定基线**，相对 Ayo-like 静态 mapping 约 **1.5×**，必须同时报对照对象，不能只写“10.94× Agent 加速”。
- 作者 ablation C1：**5.79 s → 3.82 s**（约 1.52×）。
- 作者 ablation C2：**17.23 s → 5.38 s**（约 3.20×）。
- 仍不是全部通用调度策略的穷尽比较；同 Agent.xpu 学术研究血统，不多次算独立验证。

**主机制图（60%）**：用户 Agent RAG：query rewrite / retrieval / rerank / generate 的部分可观察 DAG → stage profiling / shape partition → online scheduler（criticality + future edge + shared bandwidth）→ CPU/GPU/NPU。箭头必须标出控制、数据与争用反馈，不能把 DAG 画成绝对固定顺序。
**辅图（40%）**：原论文两组有同一基线的 ablation 秒数；与 10.94× headline 各放不同条件格，**避免误以为属于一条实验**。

**原图策略**：优先审阅论文架构 Figure 是否确能展示 DAG 与调度器；若原图过于密集，截图只作缩小后的“原论文依据”，主图另作清晰矢量重绘。不要仅贴一张无法读懂的论文截图。

**出处**：[HeRo 原论文](https://arxiv.org/abs/2603.01661)、[深读卡](../../01-evidence/papers/PAPER-098/deep.md)。

**底部判断**：跨引擎 Agent DAG 的软件调度值得做，但该论文**不是新增专用 CPU/uArch 控制原语的直接因果证明**。

**承接**：“以上五组机制怎样形成真正可控的 CPU/LLVM 技术路线？”

## 第 9 页｜从论文抽象出五个真正可交付的技术控制点，而不是五个研究标签

**结论式标题**：**最具可执行性的投资链条，是 LLVM 编译降低、SME 状态 ABI、CPU 微内核布局、异构阶段分工以及 OS 前台 QoE 控制。**

**主图**：技术层级及数据/控制闭环，而不是横着排五个小卡片：
- 上层 **模型/算子要求**：shape、量化精度、动态 DAG、deadline/foreground priority。
- 编译层 **LLVM/MLIR**：Linalg tiling/fusion、vectorizer、ArmSME lowering、CPU subtarget selection。
- CPU 执行层 **SM/ZA ABI + KleidiAI µkernels**：直播状态/调用边界、GEMM/GEMV、packed tensor 重用。
- Runtime **CPU-NPU 分工**：graph specialization、precision role、fallback/copy/sync。
- OS **QoE/admission**：Agent DAG criticality、DRAM 资源、NPU work scheduling。
- 关键**反馈边**：模型 shape/性能条件从 Runtime 返回编译/runtime selector；版本失效导致 packed tensor/Kernel 调整。没有已公开支持时，不画不存在的专属硬件 signal。

**文字（相邻五条）**：每一项一整段“技术问题／已有什么／团队能做什么／不能主张什么”。示例：LLVM SME 调用约定已存在，团队工作是保证函数边界的正确性与组合性能，**不能宣称已经测到手机 PSTATE.SM 微秒切换开销**。

**图表类型**：**系统依赖架构图**可编辑 SVG，5 个 technical owner 色块（CPU/Compiler/Runtime/OS/Agent platform）须明确，避免看起来 CPU 团队独立拥有全部平台。

**出处**：[LLVM SME](https://llvm.org/docs/AArch64SME.html)、[MLIR ArmSME](https://mlir.llvm.org/docs/Dialects/ArmSME/)、[KleidiAI](https://github.com/ARM-software/kleidiai)、[Round15F 综合](../../analysis/engineering/round15f-cpu-llvm-compiler-pressure-2026-10-08.md)。

**承接**：“CPU kernel 之外，Agent state 和安全执行在物理层是否形成新的设计空间？”

## 第 10 页｜必须把 Agent 工具行为和 CPU-NPU 派生状态分成不同问题

**结论式标题**：**安全的 Agent 操作需要授权目标与结果验证；高效的跨引擎复用需要版本化派生状态，但两者都不自动要求专用 CPU 硬件。**

**要解释的两个不同状态层级**：
1. **用户可见的动作合法性**：目标 App/对象必须在当前权限上下文中绑定；工具返回结果必须能验证真实效果；失败后不能简单重放造成重复副作用。这个问题的主责层是 App/Agent Framework/OS。
2. **物理可复用状态有效性**：Agent 任务版本改变后，CPU/NPU/GPU 的 KV/layout/compiled graph/缓存 derived state 是否仍与本次目标、模型版本和可见权限一致。这个问题含 Runtime/驱动/内存；通用版本化/共享缓冲已是强基线。

**主视觉**：**双泳道版本关联图**：上泳道 Intent/Authority/ToolEffect/OutcomeReceipt，下一泳道 CPU packed weights / NPU graph / memory state，二者通过 version/provenance ID 有条件关联。**注意图例要说明 S0/S1/S2/S3 是内部设计抽象，不能直接用这几个研究编号给领导看**。
**辅图**：已存在的 Android NPU Manager 生命周期、QNN shared buffers、Apple session API 和多 Agent 事务回退专利的“已支持/有限覆盖/未证明 Agent-only 硬件”对照表。

**相关资料与限制**：[AOSP NPU Manager](https://source.android.com/docs/core/perf/npu-manager)、[QNN shared buffer](https://docs.qualcomm.com/nav/home/htp_shared_buffer_tutorial.html?product=924033590759186372)、[Apple session](https://developer.apple.com/documentation/FoundationModels/LanguageModelSession)、[CN120704926A](https://patents.google.com/patent/CN120704926A/en)。部分官方文档直访受限，措辞限定为已归档技术审阅，不作全机型部署宣称。

**承接**：“低功耗主动 Agent 是不是需要一个新硬件域？”

## 第 11 页｜主动 Agent 的价值函数不是随时唤醒，而是“值得帮助时才行动”

**结论式标题**：**端侧主动 Agent 的核心是帮助效果、误触发、隐私和整机电量之间的取舍；现有低功耗感知体系已构成强基线。**

**要讲明的因果链**：
- 持续监听不等于持续调用完整 LLM；sensor/audio/event 可能先进入低功耗监测/轻量过滤，之后才决定是否唤醒 CPU/NPU。
- 用户真正重视的是“是否有帮助／是否打扰／耗电多少／隐私是否越界”，单一 LP block 峰值能效不足以支撑新硅片投资。
- Android CHRE、Qualcomm Sensing Hub、部分 OEM AI 公开披露已提供这些机制的一部分；不存在匹配全 Agent 成功率和手机 24h 电量的独立同口径数据可直接证明另一个新 LP 域。

**主图**：**多级 admission 判定树**：Event → privacy/permission filter → cheap screening → usefulness decision → CPU/NPU wake or no-action；沿图标出资源/延时成本和误触发风险。右侧成本函数示意只写符号与定义，不人为填数。
**辅助信息**：一张“厂商已有能力 vs 仍缺的独立公开条件”矩阵，分别为低功耗监听、NPU 唤醒、可信主动行为、帮助率调整后总能耗。

**图形方式**：可编辑流程 SVG／原生 PPT 节点；不需要找泛化的手机渲染照片。

**原始资料**：[CHRE](https://source.android.com/docs/core/interaction/contexthub)、[Snapdragon AI Sensing Hub](https://www.qualcomm.com/snapdragon/smartphones/ai)、[Pixel Tensor G5](https://blog.google/products-and-platforms/devices/pixel/tensor-g5-pixel-10/)。

**承接**：“为什么这些值得跟进的主题还不是独立硬件 Bet？”

## 第 12 页｜真正的 CPU 新硬件需要越过四重证据门，而不是多一条专利或概念图

**结论式标题**：**公开研究证明“需要优化”不等于证明“需要新硬件”；独立 Agent-uArch 投资必须同时越过软件可替代性、物理因果和手机收益门槛。**

**四重门（每门均有完整解释）**：
1. **手机/Agent 相关性**：负载是否真的发生在手机的长时 Agent 情境？泛化数据中心调度不够。
2. **最强软件基线仍不充分**：现有 LLVM/SME、KleidiAI、LLM NPU 图量化、HeRo/Android priority/cache/LP sensors 是否已能解决？不能靠用弱 baseline 证明硬件空白。
3. **无法由通用软件重建的物理状态/控制点**：例如私有语义状态、跨引擎派生对象有效性、CPU 微状态 continuation 中究竟有什么新增信息？
4. **公开可解释的手机收益与风险**：是否有具体能耗/QoE/延时/成本边界；未知时只能给有界研究假设，不能虚构数字。

**主视觉**：上下对照的“错误捷径 vs 完整因果链”，右侧注明三项精确仍开放的问题（不显示 A/B/R2 内部编号）：Agent private progress、derived physical state versioning、CPU continuation locality。每项列出现有通用技术为何是强反证。
**解释模块**：一个明确结论：“今天可以批准工程建设，但无法从现有公开证据证明特有 Agent ISA 的新颖物理收益。”

**素材**：机制决策树＋已有专利/论文元数据。任何专利只证明某技术主张**已公开/权利要求存在**，不是产品性能与 FTO 结论。

**承接**：“因此具体的投资组合应如何分类？”

## 第 13 页｜用领导听得懂的完整技术名称说明 Build、Reserve、Watch、Kill

**结论式标题**：**建议优先建设 CPU/LLVM 异构执行、可信工具操作与系统 QoE 三类能力；其余特有硬件问题保留研究而不立项。**

**主图是一张高密度技术投资矩阵（非“大号 03/03/00”卡片）**，列：投资类型／技术方案全名／解决的结构性问题／已有公开证据／责任层／主要未知／当前结论。
- 工程投入 1：CPU+LLVM 现有 SIMD/SME2/µkernel 和异构执行 fast path；现有手机 CPU 与 NPU stage 论文、优化 NPU 反证。
- 工程投入 2：具备权限、目标绑定、可验证效果/有限恢复的 Agent 工具平台；不能当 CPU uArch 自己的项目。
- 工程投入 3：Agent DAG / NPU admission / shared bandwidth / 前台 QoE 的 Runtime/OS 软件底座。
- 条件储备：Agent 私有语义进度额外信息；跨引擎派生状态的物理有效性；CPU continuation cache/TLB/branch 微状态。
- Watch / Follow：post-ready 时序、Flex Cache、低功耗主动 AI。
- Kill／暂不批准：仅给通用 priority/hint/cache/zero-copy/transaction 贴“Agent 专用”标签的 ISA/硬件预算。

**每一行写完整的技术因果**，不出现内部研究方向代号或历史数字 86.5/82.5 等。历史评分已失去现行预算含义。

**可视化方式**：长表需足够行高；每条方向用双行单元格“动作＋理由”，下端单独一块解释“Build ≠ silicon Primary Bet”。

**出处**：[正式组合](../current.md)、[决策事件](../../08-decisions/events/DEC-PORTFOLIO-002.md)。

**承接**：“这些能力在 2027 到 2029 年如何分层推进？”

## 第 14 页｜按照技术层×年份说明逐步演进，而不是不可靠的 OEM 发布时间表

**结论式标题**：**2027 年应形成现有 ISA 的 CPU/LLVM 快路径，2028 年打通跨引擎执行与状态合同，2029 年只保留有公开证据的新硬件选项。**

**主图**：X 轴 2027（BUILD）、2028（CONNECT）、2029（CONDITIONAL）；Y 轴 CPU/LLVM、Runtime/NPU、Agent Trust、OS/Memory、Low Power。每个格子至少回答：
- 技术能力/对象；
- 所属团队控制点（技术建议，非实际组织授权）；
- 与上一年相比新增的接口/条件；
- 与成熟外部技术的边界。

**技术叙事（示意）**：
- CPU/LLVM：2027 SME ABI、KleidiAI kernel/packing、shape/precision → 2028 跨设备能力合同及 ABI/layout reuse → 2029 只有已被公开证明的软件无法解决的 CPU 局部状态问题，才考虑硬件。
- Runtime/OS：2027 NPU 优化基线下的 stage placement + QoE → 2028 DAG、模型/资源版本和可撤销工作合同 → 2029 条件性物理/系统接口研究。
- Agent Trust：2027 权限/结果契约 → 2028 跨 App/跨引擎可信执行 → 2029 通用端侧 Agent 可信软件平台。
- LP/Memory：用已有 CHRE、QNN/cache/版本管理；条件研究不等于专用 IP 排期。

**旁文**：“这是技术战略建议，既不是芯片量产时间表，也不承诺内部预算或测试计划”。

**素材**：原生表格 + 少量每层技术示意，避免大量小胶囊断章取义。

**出处**：[15G 年×层路线](../management-final-public-evidence-2027-2029.md)。

**承接**：“领导现在需要批准什么，哪些内容不能由研究直接批准？”

## 第 15 页｜用清晰的决策请求收束，而不是用‘研究完成’一类空话收尾

**结论式标题**：**现阶段需要决定的是技术优先级、跨团队所有权和硬件止损边界；具体预算、人员与产品时间表必须由组织另行评审。**

**三项明确领导讨论问题**：
1. 是否认可重点建设**现有 ISA CPU/LLVM＋异构 Runtime 快路径**、**可信 Agent 工具动作合同**、**OS/QoE 资源协调**，并暂不批准 Agent 专用 ISA/硅片 Bet？
2. 哪支团队实际承担 Compiler/Cpu ABI/kernel、Runtime stage placement、OS admission、App/Agent trust？现阶段报告只给技术所有权建议，不虚构内部组织负责人。
3. 什么外部新原始证据可以触发对三项硬件研究储备的重新评估？没有这样的证据前是 Watch，不是 PoC 或内部实验。

**视觉**：从“已经可公开证实”→“建议的工程/平台建设”→“需要领导确认的组织事项”的三列表，每列要有因果叙述。右侧补充“不会做的事”：不夸大厂商数字、不对不同设备拼性能、不把专利当 FTO、不承诺本项目实验。

**结果和承接**：本页可以结束。后续附录让技术专家深入检查原始来源，不必继续堆正文。

---

## 附录 A｜原始定量证据总表（建议单独一页）

按**来源／论文名称／设备和运行环境／模型及任务／被比较的两个版本／定量结果与单位／统计口径／该数据支持的结论／不能外推的内容**九列展示，允许分为两页保证可读。

最低包含：
- *When NPUs Are Not Always Faster*：Snapdragon 8 Gen 3/Hexagon v75；Prefill NPU 1.27–1.62× slower than 6-core CPU，decode kernel 1.55–1.67× advantage for NPU，E2E about 1.05–1.20×，按原论文确认分母；
- *SMEPilot*：最多 3.94×，tile/attention/packing ablation 和准确平台；
- PyTorch/Arm vivo X300：INT8 555.8→304.1ms，FP16 1163→298.2ms，data movement 41.4/39.9%，任务为 SqueezeSAM；
- *HeRo*：最高 10.94× 指定 GPU-only baseline；C1 5.79→3.82s，C2 17.23→5.38s，**分开三种实验条件**；
- *ShadowNPU*：质量/精度 tradeoff、Prefill scope；论文原始结果必须核对，不与 llm.npu 同团队证据相乘。

不进行跨模型、跨手机、跨精度的速度收益运算。

## 附录 B｜论文原图和原创图的制作资产清单

| 想用的图 | 原始文献/资料 | 主要科学信息 | 第一选择 | 原图不能直接用时 |
|---|---|---|---|---|
| CPU-NPU crossover 数据图 | [PAPER-009](https://arxiv.org/abs/2605.27435) | Prefill / Decode Kernel / E2E 比较及 stack overhead | 核对论文 figure/table 与图例许可，保留作者出处 | 用原数重绘三 panel 条形/比值图 |
| SMEPilot Profiler/Planner 架构 | [PAPER-052](https://arxiv.org/abs/2606.16332) | CPU-only / SME-only / mixed + packing layout | 论文原方法图局部插图（许可、图号核对后） | 制作 Methods-faithful 可编辑 SVG 系统图 |
| vivo SME2 数据表 | [TOOL-012](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/) | 同机 SqueezeSAM CPU on/off SME2 | 原数与设备说明重绘图表 | 原始表格小图作出处旁证 |
| ShadowNPU 重要性估计/残差 | [PAPER-057](https://arxiv.org/abs/2508.16703) | Low precision NPU selection + sparse high-precision CPU/GPU refinement | 对照作者方法图准确重画，标“依据方法重绘” | 复杂图用 Figma/矢量工具排版并附可编辑源 |
| HeRo Agent DAG Scheduler | [PAPER-098](https://arxiv.org/abs/2603.01661) | Online partial DAG/shape/criticality/DRAM QoE | 依据论文真实架构图重绘，再核对所有路径 | 原 PDF 细图仅放补充“来自论文”小视窗 |
| LLVM/SME toolchain | [LLVM SME](https://llvm.org/docs/AArch64SME.html)、[MLIR ArmSME](https://mlir.llvm.org/docs/Dialects/ArmSME/) | 已公开 ABI/lowering/状态边界 | 原生可编辑 PPT 体系结构图 | SVG 可编辑分组 |
| 可信状态/工具事件双泳道 | 多份官方技术+专利机制 | 权限、真实工具效果、派生缓存是不同生命周期 | 原创概念泳道（醒目标“示意”） | 矢量图插件完成节点、连线，仍需校审 |

**素材清点 Gate**：每一张候选论文原图，先有原 PDF 链接、图号、图注、作者/venue、图片许可或适用引用条件、放入幻灯片的精确作用、必要的局限说明。没有这些信息不直接截图。正式制作前才进行素材下载/原图版权确认；本轮仅设计，不假称原始图片已取得或许可证已核准。

## 附录 C｜反证/既有产业能力矩阵

将 LLVM/MLIR ArmSME、KleidiAI、llm.npu/ShadowNPU、HeRo、Android NPU Manager、Qualcomm QNN shared buffers、CHRE/Sensing Hub、LAS/ProgRouter 与版本化和 Agent 事务专利作为**已公开强基线**。列“能力是什么 → 覆盖的 Agent 问题 → 尚未证明的特有硬件残差 → 对当前投资决策的影响”。同团队/厂商宣传必须分组，不能当独立验证。

## 附录 D｜仍保留的三个硬件问题必须有明确的不成立条件

**私有语义进度信息**：如果 complete observable ledger/history/SLO/permission/validator 已达到同等可用控制，便不能单独做语义硬件。

**跨引擎派生状态**：如果 version/provenance/cache validity/QNN shared buffer 已解决映射、隔离、复用，那么无法从“有状态”推导出新物理 coherent primitive。

**CPU continuation locality**：如果普通 affinity/cache/prefetch/context-state 机制已覆盖增量，就不能为 Agent 定制独立 predictor/cache/TLB 保存原语。

仅接受**新发表的公开研究与可访问厂商技术资料**作为后续是否改变判断的依据。**本研究绝不开展或规划自有实验、仿真、PoC。**

---

## 2. 如何审稿：内容蓝图 → 精细 wireframe → 小样 PNG → 全量 PPT

**Gate 1：领导独立可读性**。把每页标题、文字、图注和证据给没参与项目的技术负责人看：他们不需要知道任何研究代码或内部标签，能否回答“现象是什么、机制是什么、证据是什么、跟 CPU 有什么关系”？

**Gate 2：页间递进**。第 n 页明确接上 n−1 页留下的问题，不能出现“上页说 NPU，下一页突然说投资框架”这样的跳跃。前半段以证据建立问题，后半段将证据转换为所有权、投资与边界；**写作原则隐藏在幕后**。

**Gate 3：媒体责任**。每个图都要有指定：为什么用图不用文字、谁作为源、哪些元素必须可编辑、箭头含义、事实/示意标签、替代视觉方式。复杂图可交由矢量绘图插件，但出图结果必须逐线比对设计蓝图。

**Gate 4：密度与清晰度共同达标**。完整论证以“图 + 实验条件 + 指标 + 因果解释 + 结论/限制”组合承载；缩略图检查大结构、单页全分辨率检查正文；不能以 7pt 字号来凑内容量，也不能用三个空卡片占据半页。

**Gate 5：独立来源与投资纪律**。论文原文/厂商材料/概念推断的标签清晰；llm.npu+ShadowNPU 和 Agent.xpu+HeRo 不算多次独立复现；Vendor SDK/Android NPU Manager 部分页面当次访问受限需注明；现行组合 **3 类工程平台投入、3 项条件储备、0 个已证实的独立 Agent CPU 硅片 Bet** 保持不变。

**正式制作顺序**：①先审批这份蓝图；②完成每页可审读的文字稿与含说明的低保真 wireframe；③只做 2–3 张代表性高保真 PNG（工作流、论文数据、系统机制）检查视觉语言；④逐页批量制作可编辑 PPT；⑤最后做整套 PNG 渲染、文字溢出和线段端点审查。

**当前阶段结论**：尚未开始下一套 PNG 或 PPT；需要先确认整套内容/逻辑/媒体蓝图的可读性。
