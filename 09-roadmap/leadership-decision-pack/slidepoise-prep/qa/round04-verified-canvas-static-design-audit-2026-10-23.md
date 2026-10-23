# Round04｜经真实本地 Profile 核验的 16:9 页壳 + 正文 SVG 审计（2026-10-23）

> **审计结果：FULL_SLIDE_16_9_CONFIRMED / CONTENT_CANVAS_CONFIRMED / STATIC_SVG_PASS / VISUAL_RENDER_NOT_YET_TESTED**。  
> 用户在 GitHub 新上传 `slidepoise-preflight-export.json`，本轮已通过 GitHub connector 真实读取并核查其字段；S03/S05/S08/S15 已按正确正文区域生成全新独立 SVG，并提供 16:9 母版组合参考预览（不等于本机 PowerPoint 的实际渲染）。

## 1. 上传的真实配置确认

| 属性 | 真实值 | 结论 |
|---|---|---|
| Profile | `academic-cpu-insight`，revision `c330fa78476cd5d74298edb608b3fcedde4b90c6f8175905316588b95ea779d6` | 蓝色科研风与中文字体配置生效 |
| 完整 PPT | `[2048,1152]` | **16:9** |
| header | enabled=true，height=41 | 母版上 41 px |
| footer | enabled=true，height=41 | 母版下 41 px |
| 生成区 | `[2048,1070]`，offset_y=41，ratio 1.914019 | 正文区，不是 PPT 纸张宽高比 |
| 字体/基础色 | Microsoft YaHei；#102C55/#174478/#2473B6 | 配置层可见，但 PowerPoint 字体回退还未实测 |
| header/footer 文案 | 原文件空字符串 | 10 号 manifest 中的母版标签是**建议/示意** |
| 原生页码 | `{slide_number}` | 实际渲染 `03/17` 格式未验证 |
| Speaker Notes | `NOT_TESTED` | 尚不可声称内嵌演讲者备注已实现 |

数据直接来自：[真实 JSON](../../slidepoise-config/slidepoise-preflight-export.json)。

## 2. 完整样页资源审计

| 视觉对象 | 数量 | 要求 | 当前结果 |
|---|---:|---|---|
| 独立纯正文 SVG | 4 | 每张 **2048×1070** | 已通过静态尺寸检查 |
| 16:9 整页母版 SVG 示意 | 4 | 每张 **2048×1152** | 已通过静态尺寸检查 |
| 正文图中母版重复文本/页码 | 0 | 只能在 frame mockup 出现 | 符合 |
| SVG 标签/属性/转义结构异常 | 0（8 文件） | XML 格式和关键属性正确 | 静态检查通过 |
| 估算超出画布的文本坐标 | 0（8 文件） | 基于字符估算而非字体排版引擎 | 未发现明显越界 |
| 实际渲染后的碰撞/字号验证 | 未做 | 必须在 SVG→PNG / 本地 PPT 真图检查 | **未通过验收门槛** |

源图片及哈希入口：[10-formal-content-region-samples.md](../10-formal-content-region-samples.md)。四页旧版 1600×900 只存历史参考，不曾强行变形。

## 3. 技术事实与视觉规则的第二轮核对

| Slide | 必要技术内容 | 已知关键错误的规避 | 还需实际看到画面的检查 |
|---|---|---|---|
| S03 | 三工程/平台、三条件研究储备、0 项独立 Agent 新硬件主押注；CPU/Runtime/NPU/DRAM 关系 | 未再把 PIM/独立加速器当三正式储备；储备没有“已完成”标志 | 左侧层级是否可冷读；每条箭头是否真实落在对应框体 |
| S05 | 10 个逻辑节点、13 条边（含条件和验证反馈），另有资源/DRAM 约束 | 查询重写不是强制；工具操作不是必经，真实效果验证独立于 API success | 修复的顶部 bypass 边到节点的间距，所有箭头连接实际落点与条件线视觉区分 |
| S08 | SME/SME2 **在 CPU 核内**；vivo X300 SqueezeSAM 单 CPU 核 INT8 555.8→304.1 ms，FP16 1163.0→298.2 ms | Apple M4 Pro 能耗**不**写作手机电池；两组 bar **各自在组内**按“优化前”归一化，不是跨精度同量尺 | 原始 PyTorch 官方数值读回；两组条形长度视觉上准确且单位可读 |
| S15 | 五个技术层 × 三年，不把“持续工程”和“待证据硬件”混成已批准项目 | 改掉 2029 全格虚线导致持续软件工程也被误写成条件研究的问题；保留逐行“持续/条件”标签 | 2027–29 的阅读顺序、网格排版与虚线/文字意义一致性 |

S05 机器可读关系合同：[S05-edge-contract-v02.json](../generated-images/formal-content-v02/S05-edge-contract-v02.json)。这不是可擅改的美术连线清单，而是下一阶段必须映射为原生 PowerPoint connectors 的语义合同。

S08 比例计算（不改变原数据）：
- INT8 `304.1/555.8=0.54713`；柱长建议 264 vs 482；
- FP16 `298.2/1163.0=0.25641`；柱长建议 124 vs 482；
- 两组的 `482` 像素 **分别**代表本组原始基线 100%，不允许观众拿两个优化前柱直接比较 555.8 与 1163.0 的绝对差别。
- 这些值沿用已核仓内来源，没有本轮重新逐张下载全部原始 PDF 与独立实测；别把它说成新的现场手机测试。

## 4. 实际 native SlidePoise 管线仍未进行

| Gate | 现在状态 | 需要的下一证据 |
|---|---|---|
| G1 内容/来源合同 | 仓内核对通过，有原图精确表待核项 | 若变动数字需回溯原文；不要静默替换 |
| G2 视觉草图/正确尺寸 | **静态通过，渲染/人工目视未完成** | 真实 SVG/PNG 全分辨率查看，重点 S05 箭头交叉 |
| G2 正式 ImageGen request | **尚未执行** | 使用实际 Profile、canvas 和 `prepare_generation.py` 编译的请求 |
| G2 accepted-slide.png | **没有** | 来源/文字/样式/边界通过后才能冻结 |
| G3 native PPT 真实重建/可编辑性 | **没有** | semantic-map、OpenCV 证据、package renderer、native object verification |
| G3 master/页码 | **没有** | 真正应用 run session overrides，验证 inherited frame |
| G3 Speaker Notes | **没有** | PPTX 真实写/读/逐页核 |
| G3 全页与跨页 QA | **没有** | PowerPoint 渲染、contact sheet、文字提取与 16:9 核验 |

## 5. 后续建议

当前 GitHub 里已经有足够详细的**实质内容区**与**完整 16:9 母版样页参考**。接下来最有价值的不是再产一批泛化图，而是在本地 SlidePoise 或可靠的浏览器中**真实渲染/核箭头/核中文字体**，用 S05 作首个语义高风险 G2 样页。可使用 [Work Handoff](../07-work-mode-handoff.md)，只执行四页试制，**不准越过用户关口一次直接生成全部 17 页**。

没有真机 CPU 实测与真正 PowerPoint 编辑验证，必须继续在结论与交付层面如实标注对应约束。
