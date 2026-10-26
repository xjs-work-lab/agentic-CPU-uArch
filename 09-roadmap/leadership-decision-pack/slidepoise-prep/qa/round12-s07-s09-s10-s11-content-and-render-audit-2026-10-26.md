# Round12｜S07 / S09 / S10 / S11 受控目标 PNG 与逐页技术/视觉审计（2026-10-26）

> **已完成：4/4 G1 技术内容合同复核；4/4 PNG + 完整 16:9 预览真实生成、打开并检查。**
> **尚未完成：用户视觉签收；正式 SlidePoise packaged accepted-slide.png；原生可编辑 PPTX；Windows PowerPoint Notes 写读回。**
> 旧版错页 Image2.5 图继续隔离，本轮绝不偷换旧图名。S02、S06 上轮已获用户视觉批准，S03、S05、S08、S15 的试制结果不变。

## 1. 四页的主张与防错审计

| Slide | 源事实应支撑的主张 | 本轮图形核对 | 绝不外推 | 状态 |
|---|---|---|---|---|
| **S07** | PAPER-059 llm.npu：Prompt 分块 / 静态图复用 / INT8 NPU 核心 + CPU/GPU outlier；PAPER-057 ShadowNPU：低精重要 token 估计 + CPU/GPU 高精 top-k 稀疏残差，主要 Prefill Attention | 两栏并列机制链，CPU/GPU 与 NPU 均存在；Decode 仍保留 CPU/GPU 完整 Attention | “所有Attention与Decode被NPU取代”；“两篇独立重复验证”；跨论文速度/能耗倍数相乘 | G1 PASS；G2 视觉候选 |
| **S09** | PAPER-098 HeRo：动态 Agentic RAG DAG、阶段放置、任务完成时间；PAPER-003 SERENO：后台 LLM 与前台 App 共享 DRAM/QoE 争用 | 左右两条不同因果关系，并分别指向底部 Runtime/OS 的调度和带宽责任；非产品实际部署架构图 | 把HeRo两个消融案例作为全局平均；把SERENO的 jank 指标当算子加速；两成果相加 | G1 PASS；G2 视觉候选 |
| **S10** | VENDOR-032 软件工具能力 + PATENT-033 软件事务先例 + PT-A 工程合同 | 五阶段：授权→目标新鲜绑定→受限执行→外部状态回读→目标效果核验；成功与恢复分支仅从独立核验分出 | API 200 等于外部目标达成；OutcomeReceipt是已发布的跨平台标准；推导CPU语义ISA | G1 PASS WITH PLATFORM BOUNDARY；G2 视觉候选 |
| **S11** | PAPER-119 LAS、PAPER-121 ProgRouter、PAPER-044 ProAgentBench 是可观察软件状态的强基线；DEC-A-008 条件降级 | 实线软件账本、语义摘要、路由/恢复；三源卡片；右侧独立虚线“私有进度信息”未证实假说 | 软件基准等于手机 SoC 能耗实测；CPU 已发现 RequiredProgress 私有寄存器；旧82.5是现行评分 | G1 PASS；G2 视觉候选 |

## 2. 渲染与视觉工程检查

- 逐页原始**正文图精确 2048×1070**，四张全页预览为 **2048×1152（16:9）**，上/下母版区各41px。内容 PNG 不包含页码、共享页眉/页脚；整页预览的项目名和页码只是 mother/frame 视觉示意。
- 生成的是独立受控 SVG → CairoSVG PNG，**不是 Image2.5 错误技术全文图**。ImageGen 的一张蒙太奇只用于确认蓝色、卡片圆角与技术报告视觉语言；其中文文案/页码与具体图形没有进入交付文件。
- 使用 Noto Sans CJK SC 字体 + Pillow 计算每个文本对象的近似横向范围：S07 **28** 个、S09 **27** 个、S10 **23** 个、S11 **25** 个，**共103个**，未检出画布边界溢出。文字测量不等于可视碰撞零问题，已另外对四张实物预览进行冷读/连线目视检查。
- 箭头语义检查：S07 两种优化路径不能画成单一 CPU→NPU 固定流程；S09 两类 OS 系统目标互补而非论文数据直接因果；S10 必须有独立结果核验分支；S11 虚线框表达未知假设而非已发现的信号。
- 受控页面**不展示任何未充分绑定的算子速度、能耗或手机整体性能收益百分比**。相关原文数字及测试设备说明留在 Notes，方便领导被追问时追溯。
- **未做**：Windows Microsoft YaHei 与 Noto Sans CJK 的实际 PPT 字体差异测试、真实 SlidePoise accepted target 及 PowerPoint native-object/Notes 验证。本轮不生成 PPTX。

## 3. 交付、存储和身份

- 四张正文 PNG、四张整页预览 PNG + 完整 ZIP 真正保存到 ChatGPT Library: `/Agentic-CPU-uArch/slidepoise/round12-four-visual-candidates`，上传后重新 list 为 **9/9**。
- 单个包 `Agentic_CPU_Round12_S07_S09_S10_S11_Review.zip` 含 **21 项**：四张正文 PNG、四张全页预览、四张 SVG、四页详细 Notes、脚本、QA Manifest、预览拼图和交接说明等。ZIP 由 Library 实际 materialize/read-back，经 SHA-256 校验一致且 CRC 无损。
- [SHA-256、文件大小、精确尺寸与 G2 状态 JSON](round12-four-slide-controlled-png.manifest.json)。
- **GitHub 本轮上传的是 Notes、QA、Manifest 文本，尚未直接写入 PNG/ZIP 的二进制字节**。Work 应从 Library 按唯一 ZIP 文件名获取或由用户从 Library 附加，不能使用其他执行会话的 `/mnt/data` 路径，不能把 GitHub manifest 当 PNG 实体。
- 正式用户视觉签收前状态统一 `G2_RENDERED_VISUAL_CANDIDATE`，不得命名为 `accepted-slide.png`。

## 4. 接下来的门槛

请用户对这四张真实 16:9 预览检查中文字体、主张独立可读性、框图比例、箭头落点和单页信息密度。若确认这四张，则这一批 S07/S09/S10/S11 更新至“用户视觉通过”，再制作第一批剩余的 S01 与 S04。已验收四页 pilot 不重做；后续整套17页总览须等所有 PNG 实物齐备再制作。
