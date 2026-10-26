# 18｜17页完整图片 v2 终版归档与本地 Work/SlidePoise 交接（2026-10-27）

> **最新有效版本：v2。原 v1 两个ZIP已被替代，不再用于新的 PPTX 重建。**
> 用户已视觉验收 S01–S17 全部17页；本轮针对上一版的 S12 与 S16 进行了真正的 Image2.5 定点修图，保留其余15页的图片、预览、原始图和备注字节不变。**尚未生成本轮最终 PPTX。**

## 一、最终二进制文件实际存放在哪里

**ChatGPT Library 中已保存并重新下载、验证 ZIP SHA-256 与 CRC 成功：**

`/Agentic-CPU-uArch/slidepoise/final17-v2-2026-10-27/`

| 文件 | 实际字节数 | SHA-256 | 用途 |
|---|---:|---|---|
| `Agentic_CPU_17Slides_PNG_Work_Input_v2_2026-10-27.zip` | 67,794,110 | `73a3549038f37aa143652d3a0054119db248119e47bbe52386782ac3bd5b3256` | **Work 优先附加这一包**；55文件，17正文+17预览+17备注+QA+总览 |
| `Agentic_CPU_17Slides_Full_Source_v2_2026-10-27.zip` | 88,886,731 | `b9a343d90460467631984cd590da13776523364d0cd46b0af3e78e8b2bca3c0b` | 全部内容 + 17原始画稿 + 归档处理脚本；77文件 |
| `17-slide-contact-sheet-v2.png` | 6,471,510 | 包内 manifest 另列图片完整SHA | 17页按 S01→S17 顺序的总览图 |

**两个 ZIP 完整性：PASS。** 已从 Library 实际 materialize 并比对本地原始文件 SHA-256；`testzip()` 均无错误。包含真实二进制 PNG，不是仅有文件路径或 JSON 清单。

GitHub 仓中归档的是**本交接合同与哈希/QA 元数据**。目前未通过 GitHub API 验证上述大 ZIP/PNG 字节已经提交本仓，因此 `GITHUB_BINARY_COMMITTED=false`；绝不能误报已存在于 GitHub。

## 二、页码与版本控制：仅两页修改

- S01–S11、S13–S15、S17：与上一版17页包相比，**正文 PNG、完整预览、原始画稿、Notes的 SHA-256 均相同**（15/15），版本冻结。
- **S12（新版）**：「跨层状态治理、低功耗准入与语义进度需要协同设计」：完整展现 F 执行/派生状态生命周期、P 感知事件→价值/意图判断→是否唤醒、V 语义进度→继续/切模型/核验结果→前台QoE。下半部映射 Agent/应用、Runtime/OS、CPU/LLVM 与 GPU/NPU/DRAM 的职责与接口；**不是三项专用硬件**。
- **S16（新版）**：「证据边界比论文数量更重要」：顶部投影明确区分**直接事实、跨来源推断、待证实假设、尚无足够证据支持的主张**四级，主体列出适用边界与不能从局部论文推出普适硬件结论的示例。
- 用户已明确认可新版 S12/S16 的视觉效果。新图审查认为已补足原合同两项内容缺口；仍不能声称对所有外部论文 Figure/Table 完成了重新现场全量核验，也不能把 Image2.5 版式作为科学测量来源。
- 旧 v1 `S12-content.png` 和 `S16-content.png` **一律禁用**；只允许从新 v2 ZIP 的同名路径取图。
- S16 Image2.5 源画面自带「16/17」小页号；v2 正文目标只遮除这个重复页号并保留原图备份，正式母版统一绘制页码。

## 三、Work 模式解包后应看到的目录结构

| ZIP 内路径 | 数量 | Work 用法 |
|---|---:|---|
| `01-substantive-2048x1070/S01-content.png` 至 `S17-content.png` | 17 | **正式 SlidePoise 正文视觉目标**，每张 2048×1070 |
| `02-full-16x9-2048x1152/S01-preview.png` 至 `S17-preview.png` | 17 | 全页 16:9 校对图；**不可**当 substantive image |
| `04-speaker-notes/S01-speaker-notes.md` 至 `S17-speaker-notes.md` | 17 | 需真正写入 PowerPoint 备注，再从最终 PPTX 读回核对 |
| `05-QA/manifest.json` + `17-slide-audit-and-work-handoff.md` | 2 | 逐页哈希、原图版本、QA、剩余证据边界 |
| `06-overview/17-slide-contact-sheet.png` | 1 | 17页顺序、风格、内容节奏总览 |
| `README.md` | 1 | 完整17页任务定义 |

全源包另有 `03-original-approved-source/`（17 张未修改的 Image2.5/混合原图）和 `07-scripts/`。**历史 v1 脚本已移到 `07-scripts/historical-v1-do-not-run/`，不能当 v2 重绘入口；Work 不应重新生成已经视觉验收的 PNG**。

## 四、Work 唯一正确的执行任务

1. 在 Work 对话附加来自 Library 的**一个** `Agentic_CPU_17Slides_PNG_Work_Input_v2_2026-10-27.zip`。若 Work 可浏览 Library 直接获取，仍必须验证实际 ZIP 字节/文件清单；否则请用户通过附件选择这一个ZIP，**不要**引用其他会话 `/mnt/data` 临时路径。
2. 加载本仓权威 `01-deck-outline.md`、`02-slide-contracts.md`、`03-evidence-map.md`、`04-risk-boundaries.md`、`05-visual-spec.md`、`09-frame-and-content-region-contract.md`、本 `18` 交接、`09-roadmap/current.md` 和 DEC-PORTFOLIO-002/DEC-A-008。
3. **按 S01→S17 严格固定页码**，封面/目录占01/02；没有新增分节页或跳页。17张全部使用 v2。
4. 使用既有 SlidePoise `academic-cpu-insight` Profile，标准16:9全页2048×1152，substantive 2048×1070，上下原生 header/footer 各41px。**正文使用 `01-substantive`，不要把全页 preview 当重建输入。**
5. 保留已验收 Image2.5 高级蓝白技术视觉；标题、正文、图表/数据、主要模块和关系箭头/矩阵尽量由 PowerPoint 原生可编辑对象重建。复杂的手机、芯片艺术或无法忠实原生重绘的特殊视觉素材允许作为独立可替换的图片对象，**不得整页 PNG 假充可编辑 PPT**。
6. 逐页将文字、来源限定、设备/模型/基线、箭头触发条件与原内容合同核对。已知红线：S06 的9.9–13.0%为NPU路径通信占比而非E2E收益；S08手机SqueezeSAM/SME2不是Agent基准；S10 OutcomeReceipt为建议接口；S14三项硬件残差均未证实；S16四证据等级必须清晰；S17三工程/三储备/零新硬件主押注。
7. 将**17份 Speaker Notes 真实写入最终 PPTX 并读回**；每份备注先讲本页结论与图形逻辑，再逐来源解释支持什么/不支持什么。原有旧版备注只能按技术主题参考，禁止按旧页码复制。
8. 每页实际渲染验收：Microsoft YaHei 中文字体与溢出、框与图标、箭头端点、16:9大小、页码连续、页眉/页脚边距、数据准确、与对应 v2 PNG 的可视保真，以及原生对象编辑性。
9. 只有在**真正**生成并 read-back 可编辑 PPTX/Notes、且验收通过后，才进行最终GitHub二进制归档并更新主README。发现失败要报告，不得直接跳过检查或换用旧 v1 素材。

## 五、真实完成状态

- `VISUAL`: 17/17 用户认可。
- `CONTRACT_COVERAGE`: 17/17 现行主题已核对，S12/S16 旧 P1 内容缺口已被本轮新图定点解决。
- `ARTIFACTS`: 两份含 PNG 实物的 ZIP + 单独总览已持久归档并通过真实回读。
- `GITHUB_BINARY`: 尚未完成，文档和哈希已可见。
- `PPTX`: 本轮未制作；由 Work/SlidePoise 完成。
