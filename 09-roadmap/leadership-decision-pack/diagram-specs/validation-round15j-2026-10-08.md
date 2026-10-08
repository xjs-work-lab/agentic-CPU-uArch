# Round15J — 技术机制核对与 Mermaid 静态结构验证报告

日期：2026-10-08。范围：第 1–12 页的 11 段流程/架构 Mermaid（第 10 页 2 段）；第 4、6 页数值/统计口径的原文核对。第 13–15 页采用投资/路线/决策矩阵，不属于本轮 Mermaid 验证对象。

## 1. 检查方法和准确边界

**已实际运行**自编写的离线静态结构检查：扫描所有 Mermaid 源码，检查节点注册、边源/目标引用、重复节点、孤立节点、未解析的文本行，以及所有判断框是否拥有 2 条以上带标签的出口；改进后支持 Mermaid 的行内目标节点定义。用于本轮的是前三页旧图 + 第 5/7/8/9 页修订图 + 第 10/11/12 页旧图。

**结果**：11 段图、89 个注册节点、115 条关系边；**0 条未定义端点、0 个重复注册、0 个孤立节点、0 条不能识别的语句**。所有 12 个条件判断节点（见各图）至少有 2 条具名出口。该测试为**结构闭合性检查，不是 Mermaid 官方语法引擎/CLI 渲染**。本环境没有预装 Mermaid CLI，外部包仓库 DNS 无法访问，尚不能宣称 11 张图已通过真正的 Mermaid parser/render 测试。

**已阅读** arXiv 提供的四篇原论文 PDF 文本及方法/图注（SMEPilot、HeRo、ShadowNPU、When NPUs Are Not Always Faster），并核对 PyTorch/Arm 官方博客。由于 PDF 页面截图服务返回 cache miss，**原图像素级逐图复核和版权/许可证检查尚未完成**；不应将这批图称为“与所有原始图精确一致”。

## 2. 验证矩阵

| 页 | 静态结构 | 原始来源核查 | 处理 |
|---|---|---|---|
| 1 | 6 节点 / 11 边 | 跨来源系统层级分析，非单论文图 | 已复核 node-edge 闭合；LLVM 不算执行器 |
| 2 | 12 / 16 | 说明性日历任务，非真机 trace | 成功、取消分叉有标签；需视觉检查回环布局 |
| 3 | 7 / 8 | 机制选路，不是实测 | NPU 否分支允许图重写及候选比较 |
| 4 | 不适用 | arXiv 2605.27435 Table II–V | **纠正 Table III 的 NPU call-usec 与 Table V 的 aggregated operator 口径** |
| 5 | 9 / 10 | ShadowNPU §3.1–3.4 / Fig. 5；llm.npu 单独保留 | 图中加入离线 profiling/graph bucketing、top-k 和 CPU/GPU QKV；不把两篇画为同一流程 |
| 6 | 不适用 | PyTorch/Arm Fig.1 Table 1/2 | 一位小数取 Table 2；data movement 的百分比不是全 Agent 数据 |
| 7 | 10 / 14 | SMEPilot §3–4 / Fig. 2/5 | 加入 roofline、在线规划、tile 划分/phase 流水/layout 复用 |
| 8 | 11 / 17 | HeRo §3–4 / Fig. 4/Table 3 | 明确离线 profile、动态 DAG、shape/criticality/带宽三类机制；C1/C2 分开 |
| 9 | 7 / 11 | LLVM/MLIR/KleidiAI 文档与 HeRo | Runtime 下 CPU 和 GPU/NPU 并列；LLVM 是编译支撑 |
| 10（动作） | 7 / 6 | 公开软件/事务基线 | 与物理状态有效性图分离 |
| 10（状态） | 6 / 5 | 通用版本管理/共享内存基线 | 不推定特定硬件协议 |
| 11 | 6 / 6 | Android CHRE 等公开背景 | 隐私与帮助性选择为说明性判定树 |
| 12 | 8 / 11 | 投资决策推理 | 缺失证据与明确不成立被区分 |

## 3. 高优先级修正发现

**第 4 页统计口径**：[论文 Table III](https://arxiv.org/pdf/2605.27435#page=3) 标题明确 `PER-INVOCATION MUL_MAT LATENCY`，且 NPU 的值包含 `call-usec` 的通信开销；所以先前设计称其为“纯 NPU Kernel latency”是错误标签。Table V 是 `DECODE-STAGE AGGREGATED OPERATOR LATENCY`，不能直接写“完整 Agent E2E latency”。详细数据已记录在 [page-04-stage-benchmark-data.md](page-04-stage-benchmark-data.md)。

**第 5 页论文机制**：[ShadowNPU §3.1 Figure 5](https://arxiv.org/pdf/2508.16703#page=5) 将离线 profile、图桶、NPU INT8 QK 估计、CPU/GPU top-k/稀疏 QKV、head-wise pipeline 分开；初版图遗漏了前两项及 top-k。已建 [page-05-npu-software-path.md](page-05-npu-software-path.md)。llm.npu 的详细实施方式仍需和本篇分开核实，防止拼接成虚假综合系统。

**第 6 页同机实验**：[PyTorch/Arm](https://pytorch.org/blog/accelerating-on-device-ml-inference-with-executorch-and-arm-sme2/) Table 2 数值 INT8 555.8→304.1ms、FP16 1163.0→298.2ms；后优化的 Data Movement 占时分别为 41.4% 和 39.9%。这只能用于 SqueezeSAM 同机单核 SME2 开关对照。数据已入 [page-06-sme2-x300-data.md](page-06-sme2-x300-data.md)。

**第 7 页执行机制**：[SMEPilot §3.3–4.4](https://arxiv.org/pdf/2606.16332#page=5) 明确 shape-aware online plan，mixed 的 tile-level partition 与 phase-aware pipeline 处理不同执行空隙，并且 layout-aware runtime 避免反复打包。先前 Mermaid 三分支无法承载必要技术内容。已建 [page-07-smepilot-method.md](page-07-smepilot-method.md)。

**第 8 页 DAG 调度**：[HeRo Figure 4/Table 3](https://arxiv.org/pdf/2603.01661#page=4) 支持“在线部分 DAG、shape 分片、关键性、共享带宽并发控制”；C1 5.79→3.82s，C2 17.23→5.38s，均来自 8Gen4 指定配置的消融而非 10.94× 的同一测量。已建 [page-08-hero-runtime.md](page-08-hero-runtime.md)。

**第 9 页所有权**：CPU 编译生成路径与 Runtime/OS 资源控制的边界明确，已建 [page-09-compiler-runtime-ownership.md](page-09-compiler-runtime-ownership.md)。

## 4. 尚未通过的 Gate

1. Mermaid 官方语法解析/实际矢量渲染（由于执行环境没有 Mermaid CLI）；静态结构无错误不等于可以宣称正式渲染成功。
2. 对照原论文截图逐张核验布局与全部组件，尤其 ShadowNPU Fig. 5、HeRo Fig. 4、SMEPilot Fig. 2/5；**PDF 截图获取失败**，仍须在实际制图关口处理。
3. 第 5 页 llm.npu 左侧详细机制；当前右侧 ShadowNPU 已做深入核对，但两者不能不经原文就在一张图里合成一条流水线。
4. 第 10–12 页虽然结构闭合，尚需在正式排版时审查：图形是否暗示了某个现实 SDK 已提供的完整功能；不能从投资建议推导出已具证据的新硬件接口。
5. 前三页与后续新版机制图的**视觉一致性、真实点击链接、中文叠排和箭头位置验收**尚未完成。

## 5. 后续制作指引

- **Markdown** 继续作为标题、结论、精确数字和媒体合同的权威。
- **Mermaid** 作为结构骨架，适合定义节点、分支与连线，但不代替原始论文图的科学核对。
- **Image Generator** 负责 16:9 学术浅蓝配色和视觉创意，不得改写归属、实测口径与机制。
- **正式 PPT** 将文案和链接精确叠加；数值图用可编辑图表，图形化机制不允许擅自增加论文中不存在的 CPU→NPU 控制通道。
- 当新 Markdown 与旧版 04–15 设计文件存在冲突，以本目录经过核对的 page 文件为当前制作输入；旧文件保留历史但须提示“被局部修订”。

**审计状态**：结构性离线检查完成，原文文本/表格抽查完成，针对六页已形成修订输入；原图像素比对、原生 Mermaid 渲染及 PPT 视觉验收仍开放。
