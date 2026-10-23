# 03｜17 页 PPT 主张—论文—实验数据—证据边界映射（Evidence Map v0.1）

> **状态：DRAFT/SECONDARY_REPO_AUDIT，2026-10-23**。依据 GitHub 中已归档的研究终稿、现行决策及原始来源深读卡逐项核对；**本轮不是重新下载所有论文 PDF、重复原始表格逐格验算或重新检查全部外部网站**。不能将 REPO-CHECKED 写成 LIVE-PRIMARY-REVERIFIED。  
> 对应制作合同：[01 叙事大纲](01-deck-outline.md) / [02 逐页合同](02-slide-contracts.md) / [05 视觉规范](05-visual-spec.md)。  
> 唯一完整内容基线：[2026-10-20 综合终稿](../../agentic-cpu-uarch-detailed-research-summary-cn-2026-10-20.md)，源文件 blob SHA `4fd19b49353bd927472df08c0cb76de65d5b81ea`。  
> 正式技术路线权威：[current.md](../../current.md)、[DEC-PORTFOLIO-002](../../../08-decisions/events/DEC-PORTFOLIO-002.md)、[DEC-A-008](../../../08-decisions/events/DEC-A-008.md)。研究审计截点 2026-10-09。  
> **禁止**将「研究内部已核对来源卡」误称为「2026-10-23 今日重新核对原始图的所有坐标/数字」。

## 0. 通用证据使用规范

| 标签 | 严格含义 | 对投影的约束 |
|---|---|---|
| F-DIRECT | 当前归档的原始论文深读卡列出的论文实验数据 | 必须带设备、工作负载、指标、基线、平均/最高等真实限定 |
| P-OFFICIAL | 官方 SDK/OS/编译器接口或厂商第一方披露 | 只能证明披露的 API/机制，不等于所有手机已实现，也不是第三方测量 |
| C-PRIORART | 已审阅的专利独立/从属权利要求 | 先前方案边界，不是产品落地证据、专利法律意见或 FTO |
| I-SYNTH | 由多个来源与项目决策综合形成的技术判断 | 展示「推断/建议」身份，不能升级为论文的直接结论 |
| H-OPEN | 可证伪但缺乏足够直接证据的残余假说 | 标为条件性研究，不能写成硬件获批或已验证 |
| E-GAP | 缺少可匹配原始实证/来源独立性/外部核验 | 不填充估算值、不用美化图像掩盖边界 |

### 固化事实的单位与比较合同

- 区分 **手机/SoC**、**Apple M4 Pro 非手机平台**、**云端/服务器软件 Agent 基准**、**官方 API 说明**。这些不是一个测量样本池。
- 区分 Prefill、Decode、单个 MUL_MAT/GEMV/GEMM 算子、完整模型、Agent 端到端工作流、前台 QoE、能耗、吞吐。
- 标注某个值是「最大」「平均」「某配置消融案例」；不同实验的 `×` 不能相乘、加总或做无条件横向排名。
- 只在设备/模型/基线可比且完全核对原始数据时构造定量交叉论文图；否则做机制对照，用明确的定性箭头。
- PPT 页底采用人类可读的来源短引（论文名称、作者/机构、年份、URL/DOI 视版式）；内部 `PAPER-XXX` 等编号保存在本表/备注，不应强迫领导猜标签。
- 旧版 17 页备注只作主题素材，**新 S01–S17 的讲者备注必须按此映射重编**；不得按旧页码粘贴。

## 1. 可复用关键原始资料的精确锚点

| 证据 ID | 来源与类型 | 直接可引用的限定事实（依据归档深读） | 主要不能推出的结论 |
|---|---|---|---|
| [PAPER-009](../../../01-evidence/papers/PAPER-009/deep.md) | [When NPUs Are Not Always Faster](https://arxiv.org/abs/2605.27435)，手机原始实证 | Snapdragon 8 Gen 3 / Hexagon v75；被测 NPU Prefill 较 6 核 CPU 慢 1.27–1.62×；单个 Decode MUL_MAT 算子 NPU 延迟低 1.55–1.67×；通信约占 NPU 路径 9.9–13.0% | CPU 总是快、完整 Decode 获同样倍数、下一代 NPU 也一样 |
| [PAPER-052](../../../01-evidence/papers/PAPER-052/deep.md) | [SMEPilot](https://arxiv.org/abs/2606.16332)，现有 ISA/CPU 方法 | 混合 CPU/SME、tile、流水化、packing；最高端到端加速 3.94×，基线 llama.cpp CPU；Apple M4 Pro 某配置能耗 482.813→233.931 J，其他平台含 Dimensity 9500 与 KunPeng | Apple M4 Pro 焦耳值是手机电池；SME 独立于 CPU；相对优化 NPU 获同样收益 |
| [TOOL-012](../../../01-evidence/tools/TOOL-012/README.md) | [PyTorch ExecuTorch + Arm SME2](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/)，第一方手机报告 | vivo X300 / SqueezeSAM / 单 CPU 核，INT8 555.8→304.1 ms，FP16 1163.0→298.2 ms；SME2 路径数据搬运约 40% | Agent 完整任务/CPU vs NPU 比较；全部工作负载通用加速；独立第三方复现实验 |
| [PAPER-059](../../../01-evidence/papers/PAPER-059/deep.md) | [llm.npu](https://arxiv.org/abs/2407.05858)，ASPLOS 2025 手机系统研究 | 对其论文设备与基线：平均 Prefill 22.4×，平均节能 30.7×，最高端到端应用加速 32.8×；采用 prompt 图分桶、INT8+稀疏 outlier、异构子图 | 所有场景恒定倍数；所有算子均可搬上 NPU |
| [PAPER-057](../../../01-evidence/papers/PAPER-057/deep.md) | [ShadowNPU](https://arxiv.org/abs/2508.16703)，MobiSys 2026 手机系统研究 | NPU 用 INT8 重要性估计，CPU/GPU 处理 top-k/高精稀疏残差；研究主要针对 Prefill Attention；报告部分配置最高延迟降低约 3.0×、能耗降低约 7.66× | 所有 Attention 在 NPU 上；完全没有 CPU 工作；与 llm.npu 相互独立复现 |
| [PAPER-098](../../../01-evidence/papers/PAPER-098/deep.md) | [HeRo](https://arxiv.org/abs/2603.01661)，Agentic RAG 手机调度 | 商用 Snapdragon 手机 Redmi K80/OnePlus 13；动态 Stage DAG、资源亲和性、部分未来依赖/DRAM；独立消融案例 5.79→3.82 s（1.52×）、17.23→5.38 s（3.20×） | 两例是平均加速；已超越所有通用动态调度器；需要硬件调度器 |
| [PAPER-003](../../../01-evidence/papers/PAPER-003/deep.md) | [SERENO](https://www.usenix.org/system/files/osdi26-xin.pdf)，OSDI 2026 手机前台 QoE | OnePlus 13/12；后台 LLM 对共享带宽造成前台争用；论文相应保护设置下报告后台 Prefill 吞吐变化约 1.01%、Decode 约 1.64% | 所有手机固定吞吐代价；Agent 专用 CPU ISA 的因果证据 |
| [PAPER-119](../../../01-evidence/papers/PAPER-119/deep.md) | [LAS](https://aclanthology.org/2026.acl-long.581/)，ACL 2026 多 Agent 软件 | MBPP AFlow 94.2%/6643.2 token/134.28 s 对 LAS 93.7%/2430.2 token/77.99 s；利用可观察产物、验证与调度 | 真实手机 QoE/电池或私有 RequiredProgress 的独立芯片价值 |
| [PAPER-121](../../../01-evidence/papers/PAPER-121/deep.md) | [ProgRouter](https://arxiv.org/abs/2608.25992)，多 Agent 软件研究 | 可观察任务 ledger、语义摘要、模型收益预测和预算约束；2026-08-30 v2，作者称获 Findings of EMNLP 2026 接收，发表状态仍有当时的独立核实边界 | 语义进度是 CPU 硬件专有信息；所有能耗实验来自手机 |
| [PAPER-044](../../../01-evidence/papers/PAPER-044/deep.md) | ProAgentBench，用户历史/主动帮助研究 | When-to-Assist：zero-shot 57.3% accuracy/66.7% F1，对真实历史微调 74.0%/78.5%（归档具体测试配置） | 手机 SoC benchmark，或非观察态的私有 CPU oracle |
| [VENDOR-027](../../../01-evidence/vendors/VENDOR-027/deep.md) | [Android NPU Manager](https://source.android.com/docs/core/perf/npu-manager)，官方平台 | Android 17+ 规格，模型准入、优先级、load/unload、工作状态/取消信号等 | 全部零售设备部署、硬件跨引擎状态一致性、实际电池或延迟收益 |
| [VENDOR-029](../../../01-evidence/vendors/VENDOR-029/deep.md) | [Qualcomm QNN HTP Shared Buffer](https://docs.qualcomm.com/nav/home/htp_shared_buffer_tutorial.html?product=924033590759186372)，官方 SDK | 共享缓冲、上下文与执行模式限制；**当时仅 SECTION_REVIEW**，官方动态手册正文访问受限 | 一切 CPU/NPU 交接零拷贝、各机型任意场景无成本 |
| [VENDOR-032](../../../01-evidence/vendors/VENDOR-032/deep.md) | [Apple LanguageModelSession](https://developer.apple.com/documentation/FoundationModels/LanguageModelSession)，官方 API | transcript、prewarm、Tool 对象、会话状态，且存在 concurrent respond 与上下文限制 | CPU/NPU 物理 KV 一致性、Agent 专用 CPU ISA、全天省电可量化收益 |
| [PATENT-024](../../../01-evidence/patents/PATENT-024/claims-round15d.md) | [US9626295B2](https://patents.google.com/patent/US9626295B2/en)，独立权利要求 | 异构 CPU cluster、共享 cache、缓存需求驱动的任务迁移先例 | Agent 私有语义硬件、NPU 状态一致性、法律 FTO |
| [PATENT-032](../../../01-evidence/patents/PATENT-032/claims-round15d.md) | [CN121960775A](https://patents.google.com/patent/CN121960775A/en)，公开申请 | 语义/推理缓存与身份/版本有效性、覆盖度判定的申请权利要求；核查时 pending | 其「问题覆盖度」等价于假设的 Agent 私有 RequiredProgress；已有获准专用硬件 |
| [PATENT-033](../../../01-evidence/patents/PATENT-033/claims-round15d.md) | [CN120704926A](https://patents.google.com/patent/CN120704926A/en)，公开申请 | 多 Agent 软件协调、失败回滚、快照/状态迁移的申请权利要求 | 证明 NPU 物理队列取消、硬件回收或硬件缓存一致性 |

> **来源独立性**：PAPER-059 与 PAPER-057 属相连研究谱系；HeRo 与 Agent.xpu 研究线有关；官方厂商技术披露不能当独立第三方实测；LAS/ProgRouter 的多 Agent 软件数据不能映射成手机芯片数据。

## 2. 按页映射（S01–S17）

### S01 封面：Agentic AI 将改变手机 CPU 与异构系统的协作方式
- **主张级别** I-SYNTH（技术范围与趋势说明）。
- **投影需要**：智能手机 / AArch64 CPU / LLVM / CPU↔GPU↔NPU / Runtime / 共享内存，2027–2029 路线；可选概念性手机工作流/SoC 抽象，不贴未经验证的芯片 die photo。
- **证据角色**：综合终稿第 1–3、13–14 章；current.md 支撑研究结论，Apple VENDOR-032 仅支撑已有会话/工具 API 能力。
- **不能推出**：已批准新 Agent CPU 微架构项目；已验证未来某年的手机产业量化路线。
- **备注责任**：总问题、研究边界和公开资料属性，结尾映射到正式决策。

### S02 目录：本报告从工作负载变化出发，用公开证据收敛技术路线
- **主张级别** I-SYNTH（编辑结构，不是数据证据）。
- **投影需要**：S03–05、S06–09、S10–14、S15–17 四组章节与物理页码，封面和目录也计数。
- **证据角色**：01-deck-outline.md 提供页序；这里不需要用某论文证明「目录」。
- **不能推出**：目录链条本身是科学因果证明。
- **备注责任**：解释先结论、再反证/正证、再跨层分工与三年路线的必要性。

### S03 当前技术组合：三项工程、三项储备、零项新增硬件主押注
- **主张级别** I-SYNTH + H-OPEN。
- **直接权威**：current.md、DEC-PORTFOLIO-002、DEC-A-008：CG-06 / PT-A / C 为工程/平台优先；A / B-residual / R2 为条件研究；新增独立 Agent 硬件 Primary Bet = **0（公开证据不足）**。
- **可见图形职责**：三层按状态分组，明确三项工程属于不同技术 owner；面向领导使用自然语言。
- **不能推出**：三个新硅片设计、已批准预算、A 仍为现行硬件 Bet 或未来永无新硬件价值。
- **备注责任**：逐项解释现行优先级和旧版 A 降级的生效逻辑。

### S04 四种 Agent 负载变化与生命周期
- **主张级别** P-OFFICIAL + F-DIRECT + I-SYNTH。
- **直接来源**：VENDOR-032（会话/Tool API）；PAPER-098（动态 Agentic RAG 工作流）；PAPER-044（主动帮助/历史）；第 3 章概念 Agent 任务阶段。
- **可见图形职责**：用户意图→计划→检索/推理→执行工具→效果验证→状态修订；「何时触发」作为条件分支。**概念示例**，非某论文唯一标准流水线。
- **不能推出**：每个 Agent/手机均执行全部环节、所有系统实现了硬件级持久状态。
- **备注责任**：四项变化分别如何压到 CPU/Runtime/OS/DRAM/低功耗。

### S05 动态有向阶段图（高风险样页）
- **主张级别** F-DIRECT（HeRo 动态依赖问题）+ I-SYNTH（抽象图）。
- **来源**：PAPER-098 的 Agentic RAG 任务重写、分解、检索/重排、阶段亲和与部分未来依赖；PAPER-003 佐证 DRAM 影响前台体验。
- **建议图关系**：`intent → planner → {rewrite? / parallel retrieval} → rerank → generate/tool → verify → update`；其中 `{...}` 为可选/并行示意；箭头 role 必须写为 data_dependency / control_request / conditional_feedback 中的一个。
- **实测数据**：不必在此页放 HeRo 消融值（留给 S09）；如出现，注明 Redmi K80/OnePlus 13、论文案例与非通用平均值。
- **不能推出**：示意 DAG 是 HeRo 原始实现所有节点的精确副本；每一资源亲和性固定或由 CPU 硅片直接决定。
- **备注责任**：走通关键路径与分支，解释调度粒度为何从算子扩展到工作流阶段。

### S06 CPU/NPU 阶段交叉点（高风险定量页）
- **主张级别** F-DIRECT + I-SYNTH。
- **来源**：PAPER-009 手机原始实证（Snapdragon 8 Gen 3 / Hexagon v75）。
- **数据锁定**：
  - Prefill **被测 NPU 路径较 6 核 CPU 慢约 1.27–1.62×**；该 `×` 的主谓方向必须保留，不可写成「NPU 快 1.27×」。
  - Decode 的 **MUL_MAT 单算子**由 NPU 执行时 **延迟低约 1.55–1.67×**；不等于 Decode 总时间或完整 Agent 工作流加速。
  - 通信 **约占其 NPU 路径 9.9–13.0%**；是总路径分母相关结果，不是把 9.9% 直接从某个值减掉。
- **概念公式**：阶段成本 = 计算/启动/同步/搬运/回退/争用等分项，仅为分析框架，实际成本可重叠，不是纸上按项相加的实测。
- **不能推出**：CPU 永久胜过 NPU，所有型号有同交叉点。
- **图表准入**：若画柱状图，先查论文对应的 Figure/Table、测试配置与绝对单位；当前合同允许定性对照 + 文本数字，不允许凭区间捏造两根精确柱。
- **备注责任**：解释 Prefill 与 Decode、单算子与总任务、基线与数据的差别。

### S07 NPU 软件前沿
- **主张级别** F-DIRECT（两篇分别测量）+ I-SYNTH（共同对 CPU 空间的影响）。
- **来源**：PAPER-059 llm.npu（ASPLOS 2025）、PAPER-057 ShadowNPU（MobiSys 2026）。
- **数据锁定（如果放数字）**：llm.npu 被测平台/基线 **平均 Prefill 22.4×**、**平均能耗节省 30.7×**、**最高端到端应用 32.8×**；ShadowNPU 指定实验设置下 **最高约 3.0× 降低延迟、最高约 7.66× 降低能耗**。不得把最高、平均和不同论文纵轴合并。
- **机制关系**：llm.npu 图分块/INT8+outlier+异构子图；ShadowNPU NPU 粗粒度排序估计 + CPU/GPU 精确稀疏残差（主要 Prefill Attention）。
- **不能推出**：所有 Decode Attention 完全 NPU 执行；论文结果是互相独立复现。
- **备注责任**：两项研究谱系、受测机型、模型和软件栈，不滥用倍率。

### S08 CPU 内部 SME2 与布局（高风险样页）
- **主张级别** F-DIRECT + P-OFFICIAL + I-SYNTH。
- **来源**：PAPER-052、TOOL-012、LLVM AArch64 SME / MLIR ArmSME 官方工具资料。
- **数据锁定**：
  - **vivo X300 手机 / SqueezeSAM 视觉分割 / 单 CPU 核 / ExecuTorch + XNNPACK + KleidiAI**：INT8 555.8 → 304.1 ms；FP16 1163.0 → 298.2 ms。来源为第一方官方报告，不是 Agent 推理，也不是 CPU/NPU 直接对照。
  - 数据搬运约占 SME2 特定单核 INT8/FP16 路径 **41.4% / 39.9%**，如图中概括「约 40%」须保留模型/路径限定。
  - **SMEPilot**：最高端到端加速 3.94×（llama.cpp CPU 基线，跨多评估平台）；Apple M4 Pro 某配置 482.813→233.931 J **属于非手机平台**，不要在手机能耗页引用。
- **结构不可变规则**：`SoC ├ CPU(core: scalar/SIMD + SME/SME2) └ NPU/GPU`；不允许 `CPU / SME / NPU` 三处理器平级。
- **图表准入**：允许两个独立、注明平台的研究面板；数字源自 PDF/官方文档，不是图像生成产物。
- **备注责任**：CPU 内的 SME 指令、ZA/PSTATE.SM/ABI、tile/pipeline、packing、现有 ISA 工程价值与可移植边界。

### S09 DAG 调度 vs DRAM 争用
- **主张级别** F-DIRECT + I-SYNTH。
- **来源**：PAPER-098 HeRo（Redmi K80/OnePlus 13）、PAPER-003 SERENO（OnePlus 13/12）。
- **数据锁定（可选）**：HeRo **案例 1** 5.79→3.82 s（1.52×）；**案例 2** 17.23→5.38 s（3.20×）；不能写为「平均提升 1.52–3.20×」。SERENO 指定配置后台 Prefill **约 1.01%**、Decode **约 1.64%** 的吞吐下降，不能外推所有后台任务或称为前台提升比例。
- **机制关系**：HeRo 处理动态任务/阶段 DAG 和 XPU 放置；SERENO 管共享带宽压力和前台体验；共同支持 Runtime/OS 系统责任，不能叠加两论文的加速数。
- **备注责任**：两个技术控制点互补，为什么不是 Agent 专用硬件调度器已获证实。

### S10 可信工具动作结果链
- **主张级别** P-OFFICIAL + C-PRIORART + I-SYNTH（PT-A 是跨来源工程合同）。
- **来源**：VENDOR-032 Apple Tool/Session 软件能力；PATENT-033 多 Agent 事务回滚申请；研究终稿 12.2；Android AppFunctions 在终稿中作为平台先例提及，但本轮**未定位到独立的 AppFunctions 深读卡**。
- **图形必须有**：授权与目标新鲜绑定 → 受限动作 → **独立的可观察效果回执** → 验证成功或有界恢复；「API 调用返回成功」不等于「用户期望已完成」。
- **证据细分**：各平台已具有部分工具/会话/事务能力属于直接文档范围；上面的一体化 OutcomeReceipt 合同属于**研究建议的系统接口**，不是苹果/安卓已经同名完整提供的现成标准。
- **图表准入/待核**：如要画「Android AppFunctions API 已具备某项具体结果确认能力」，必须先找到官方文档并核版本/接口；当前只能作为待进一步查证的示例，不能作为该页定量/完备证据。
- **备注责任**：清晰区分现存接口与项目建议的 PT-A 合同，避免把专利申请说成已落地。

### S11 软件进度基线
- **主张级别** F-DIRECT（软件研究）+ H-OPEN（私有 RequiredProgress）。
- **来源**：PAPER-119 LAS、PAPER-121 ProgRouter、PAPER-044 ProAgentBench、DEC-A-008。
- **数据锁定（非必须上屏）**：LAS MBPP AFlow 94.2%/6643.2 output token/134.28s vs LAS 93.7%/2430.2/77.99s；ProAgentBench 某 When-to-Assist 实验 zero-shot 57.3% accuracy/66.7% F1 vs 历史微调 74.0%/78.5%。都是各论文测试，不能拼成统一手机结论。
- **关系**：可观察 ledger、产物、验证、历史可完成部分动态路由；**私有 RequiredProgress 还未证明不可重建、也未证明独立手机收益**。
- **备注责任**：解释 A 从 Primary Bet 正式降级条件储备，不隐含假设已被否证。

### S12 三主题跨层架构
- **主张级别** I-SYNTH。
- **来源**：综合终稿第 11 章及 VENDOR-027、VENDOR-029、VENDOR-032、PAPER-003/098/119/121。
- **图形职责**：执行与派生状态生命周期（F）、低功耗准入（P）、语义进度/QoE（V）是跨层**主题**；需映射 Agent、Runtime/OS、CPU/LLVM、NPU/GPU/DRAM 的工作角色，而非三颗新处理器。
- **证据限制**：平台接口说明不能保证跨引擎物理生命周期无开销；OS API 能力不是已经完成手机系统一致性评测。
- **备注责任**：给出每条接口的输入、输出和负责层，解释组织协作含义。

### S13 三优先工程与责任边界
- **主张级别** I-SYNTH（正式方向）+ F-DIRECT/P-OFFICIAL（可用工程基线）。
- **来源**：current.md、DEC-PORTFOLIO-002 与 PAPER-009/052、TOOL-012、PAPER-098/003、VENDOR-027/029/032。
- **内容映射**：① CPU/LLVM/AArch64 + 微内核、packing、C1–C3 主要由 CPU/编译负责；C4 operator placement 需 Runtime 协作；C5 前台 QoE/DRAM 主要由 Runtime/OS 方向 C 负责。② PT-A 可信动作主要 Agent 平台/应用/OS。③ C 异构 DAG、NPU admission、DRAM、前台 QoE 主要 Runtime/OS。
- **关键技术断言**：优先「已有 ISA/系统接口的能力建设」，**不是三项独立专有 CPU 硬件方案**。
- **备注责任**：分别解释每项方向的输入、输出、基线与为什么组织责任不同；没有真实批准的团队排班或预算数据。

### S14 三研究储备与外部证据门槛
- **主张级别** H-OPEN + I-SYNTH。
- **直接决策**：DEC-A-008 和 DEC-PORTFOLIO-002；其他 R1 WATCH、CG-07 FOLLOW/EXPLORE、CG-01 BENCHMARK/FOLLOW、R3 BLOCKED。
- **储备 1**：可观察 ledger/history/权限/验证等软件基线之后，A 的私有 RequiredProgress 是否仍改变正确执行决策？强基线 LAS、ProgRouter、ProAgentBench、PATENT-032。
- **储备 2**：B-residual 跨引擎派生状态有效性在版本/缓存/共享缓冲/NPU 管理以后是否有独立物理成本？强基线 VENDOR-027/029、PATENT-033 软件恢复。
- **储备 3**：R2 continuation locality 在共享缓存/亲和性/迁移策略后是否有手机级不可替代残差？强基线 PATENT-024 与公开 CPU/cache。
- **不得写**：三项「待投入硬件」或已经完成差异化验证；不能用历史 A=82.5 分评分做现实推荐。
- **备注责任**：每项对应一个可证伪问题、一个最强替代解释、一条公开证据升级条件。

### S15 2027–2029 分技术层路线（高风险样页）
- **主张级别** I-SYNTH（规划建议，不是已批准 roadmap）。
- **正式来源**：综合终稿第 13 章、current.md、正式 2027–2029 技术管理报告。
- **2027**：现有 CPU ISA 的编译/微内核/布局，工作流 DAG 与前台 QoE 基础、可信动作/验证、软件状态/共享缓冲、低功耗现有平台跟进。
- **2028**：跨 CPU/NPU capability-aware 放置与 ABI/接口，模型驻留/取消/恢复、跨应用可信合同、跨引擎状态版本兼容、唤醒/隐私/帮助率等低功耗决策。
- **2029**：保持可移植跨层能力；新缓存/硬件状态/低功耗域/语义 ISA 只在**出现可复核外部原始证据且超出强软件基线**时重新评估。
- **横向/纵向边语义**：时间分段属于研究者建议，不是完成率；连线表示接口或研究条件的演进，而不是厂商承诺量产。
- **备注责任**：按年度、技术层解释为什么先做软件/通用 ISA 再研究条件残差。

### S16 证据等级与不能外推的主张
- **主张级别** F-DIRECT + P-OFFICIAL + I-SYNTH + E-GAP。
- **来源**：综合终稿第 14–15 章、证据独立性审计、PAPER-009/052/057/059/098/003。
- **页面事实→推断关系**：「手机特定配置 CPU/NPU crossover」≠「所有手机 CPU 更快」；「SME2 当前 CPU 路径可加速」≠「新 Agent ISA 必要」；「软件进度调度有效」≠「存在不可观察 CPU 语义信号」。
- **四标签**：直接事实、跨来源推断、待核验假设、**尚无足够证据支持的主张**（不是「已被科学证明不存在」）。
- **备注责任**：设备、模型、基线、独立性、URL 核查边界，不能以文献数量当因果强度。

### S17 当前管理技术决策与重开条件
- **主张级别** I-SYNTH + H-OPEN。
- **直接权威**：current.md、DEC-PORTFOLIO-002、DEC-A-008、2026-10-09 结题验收。
- **投影需要**：三工程/平台优先、三储备开放、零个独立新硬件主押注；新的同设备/同任务 CPU vs 优化 NPU 公开研究、独立真实手机系统测量或新官方 ABI/OS 证据可触发窄问题重审。
- **边界**：不是终止所有 CPU 技术研究；无授权真机自测、合作或芯片实施承诺。
- **备注责任**：解释每个管理讨论点如何与具体来源对应，并点明可复查的外部证据门槛。

## 3. 定量内容入画面的分级清单

| Slide | 已有仓内核对的数字 | 投影建议 | 进入精确图表前还必须做 |
|---|---|---|---|
| S03 | 3 工程 / 3 储备 / 0 新硬件主押注 | 可以直接用决策计数 | 与 current.md 当前生效状态一致 |
| S06 | 1.27–1.62×、1.55–1.67×、9.9–13.0% | 可用带设备/分母的文本或有界区间条 | 想画严格柱图需按原文 Figure/Table 核每个配置/单位 |
| S07 | 22.4×、30.7×、最高 32.8×；最高 3.0×/7.66× | 机制主图，选择少数代表数字 | 不同论文条件不能混排为可排序的同轴柱图 |
| S08 | vivo X300 555.8→304.1、1163.0→298.2 ms；数据移动约 40%；SMEPilot 最高 3.94× | vivo 数据独立对照，SMEPilot 放机制而非同图 | 查官方原图条件；不同平台不合并 |
| S09 | HeRo 两个消融案例 5.79→3.82 / 17.23→5.38 s；SERENO 后台吞吐变化 | 可用两个独立的差异块，或不放数字 | 案例、对照与论文图表精确一致 |
| S11 | LAS MBPP / ProAgentBench 软件数据 | 大部分放备注 | 不能假装是 SoC 或设备端电池数据 |
| S15 | 2027/28/29 | 使用年份作为**规划窗口** | 不图示为已获批准项目/流片日期 |
| S16 | 来源覆盖数/审核数非科学机制 | 一般不放数量 | 仅作为审计属性，不能替代实验证明 |

## 4. 原图/原表使用的尚待解除事项（Image Gate）

- **IMG-01 S05**：如要使用 HeRo 原始 DAG，请定位论文图号并对照原文箭头；当前只批准绘制「带概念标签的本项目自制 DAG」。
- **IMG-02 S06**：若直接复刻 PAPER-009 Figure 的数值柱状图，先核每一条具体设备/后端/阶段/模型与原图比例；未核前只可排「区间及方向标注」。
- **IMG-03 S07**：两篇相关研究不可合并成一张「独立证据票数图」；仅可并列阐明机制。
- **IMG-04 S08**：优先使用由原数据形成的可编辑 PPT 数字面板；若粘贴官方 SqueezeSAM 图像，另作原图/版权/分辨率检查。
- **IMG-05 S09**：HeRo 两个消融案例独立，SERENO 指标不同，不可混纵轴；可采用自绘双机制架构示意。
- **IMG-06 S10**：OutcomeReceipt 是本项目建议的接口表达，不能标注为 Apple/Android 已公开统一对象类型；Android AppFunctions 的具体 API 主张尚需补查官方卡。
- **IMG-07 S15**：画路线前核每一技术层年度位置，条件性项不得采用实体已落地样式。

**进入精确制图的规则**：`numeric_text_checked` ≠ `source_figure_verified`；二者分别记录状态。不能把生成图模型自带的文字/数字作为数据来源。

## 5. 来源变更和审计记录

- 本版为**对仓内公开证据卡的第二层内容核对**，没有得到新的独立实验或样本；保留相关论文的审计日期和来源独立性。
- 如发现需要更正数值、来源/年份/设备，先修改正式证据对象或给出纠错 issue，再按权威顺序同步改本文件和 02 合同，不允许孤立改变 PPT。
- 下一轮要做的是 04 风险边界和 17 页独立审稿；通过后才可冻结设计文本。图片出图前还需要验证本地 SlidePoise Profile、实际 content canvas 和 Speaker Notes 支持方式。
