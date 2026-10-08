# Round15K 第 8 页 HeRo 重新试制 V2：算法主线与可编辑 PPT 验收

日期：2026-10-08。**v1 用户明确退回**（箭头乱、逻辑不易理解）；本次 V2 为待用户审阅的新作品，不自动宣布视觉通过。旧样仍保留为失败案例：[问题定位与修正合同](page-08-hero-design-correction-v2-2026-10-08.md)、[v1 QA](page-08-round15k-visual-pilot-status.md)。

## 主要修改

- **论文锚点**：[HeRo, Algorithm 1（第 5 页）](https://arxiv.org/pdf/2603.01661)、§4.2 和 Figure 4(a)–(d) 的图注/方法文字。V2 是**依据论文算法的方法简化重绘**，而不是 Figure 4 原图或原系统部署截图。已核对原文 Methods/Algorithm；因外部 PDF 图像截图服务失败，未宣称 Figure 4 原图逐元素视觉对照完成。
- 原来将 DAG、profile、priority、DRAM 与三处理器 fanout 一次性混画；这次将**在线调度主语义锁定为五个单向模块**：
  1. 当前部分 DAG 更新/已就绪阶段；
  2. 估计 observed+future criticality，选最关键 ready node；
  3. 对该节点枚举可执行 PU × shape-aware configuration；
  4. 过滤带宽软限额，按预测完成与关键路径争用成本评分；
  5. 选最优**单个** PU 配置并派发。
- **四根水平箭头**只连接主链相邻节点，没有巨型回环或物理 CPU→NPU 直接控制线。离线 profiling（第三/四步的共同依据）与完成后继续迭代以说明条表达。No feasible config → 尝试其他就绪阶段/等待，在右侧辅助条注明，不把异常画成越线反馈。
- 中文锁定文案、形状、柱图、链接由 PptxGenJS 的原生 PPT 图层制作；Image Generator 只提供第 6 页认可的装饰芯片素材，且没有直接修改技术结构。
- 页面“图：Algorithm 1 方法简化，非 Figure 4 原图”明确写在页脚；内部 Speaker Notes 更详细给出算法、分支、实验依据。

## 真实原论文消融数据，不得跨场景拼比

[HeRo Table 3: SpeedUp Breakdown of Proposed Techniques](https://arxiv.org/pdf/2603.01661)：

| 实验 | 场景 | Baseline（Ayo-like 静态映射） | 完整 HeRo | 同组加速 |
|---|---|---:|---:|---:|
| C1 | Snapdragon 8 Gen 4；Qwen3；Workflow 2；FinqaBench | 5.79 s | 3.82 s | 1.52× |
| C2 | Snapdragon 8 Gen 4；BGE；Workflow 3；2WikiQA | 17.23 s | 5.38 s | 3.20× |

数据分别采用同组归一化的柱状图，**不以两组柱子的等长来表示跨场景绝对耗时可比**。原论文其他 `up to 10.94×` 的 GPU-only benchmark 与这两组消融不能合并。

## 实物与检查结果

实际生成文件放在当前会话资产文件夹 `round15k_hero_v2/`（GitHub **尚未托管二进制 PPTX/PNG**）：
- `round15k_slide08_hero_v2_editable.pptx` — 16:9，可编辑文字、四根单向箭头、卡片、两组数据柱、可点击论文源链接。
- `round15k_slide08_hero_v2_preview.png` — 对同一个 PPTX 经 LibreOffice/PDF 转出的 16:9 PNG 预览。
- `make_slide8_v2.js` — PptxGenJS 生成源码（存在于当前会话文件）。
- `slide08_traceability.json` — 图形拓扑核验源记录。

**实际执行的 QA**：ZIP 包校验成功；PPTX 有 **73 个原生 `p:sp` 形状**、1 个 Image Generator 装饰图；PPT 原生箭头末端元素 **4 个**；论文链接存在；所有五个主节点标签、C1/C2 数值和“无可行候选”的注释在 PPTX 文本中检出；PNG 为 **1921×1080（约 16:9）**；拓扑跟踪 JSON 中四条边均有合法节点端点，且水平坐标严格向右。

**局限**：
- 静态 QA ≠ 已由用户确认视觉效果或真实 Microsoft PowerPoint 字体/链接功能；二者还需用户检查。
- 当前 5 步图省略了 Algorithm 1 中 idle-PU 循环、活跃节点集合更新和部分显式 No-candidate 内循环，简化边界已在辅助条与备注注明，不可作为可执行伪代码或逐行算法流程图。
- PDF 第 4 页 Figure 4 视觉截图获取失败，只完成 Figure/Methods/Algorithm 原始文字审读。本图标明“方法简化”而非“原图缩绘”。
- v1 的 DOT 仍作失败例保留，V2 直接采用精确 PPT 单向可编辑 connector，不代表 Graphviz 自动布局在复杂反馈中已被修复。

## 下一步

先让用户审阅 V2 左侧的阅读清晰度及整页的图文密度。如果通过，则保留这套“算法级主线抽取→最少可编辑连接线→视觉风格统一→箭头逐条 QA”的方法，再进入第 5 页 ShadowNPU/llm.npu 技术架构试制。若仍有误解，先改本页结构合同/节点描述后再出新样，不再次对 v1 做手工拉线修补。

**当前状态：V2 生成与基础 QA 通过，技术论文原文的算法主要步骤核对完成，待用户视觉确认与 Office 验收。**
