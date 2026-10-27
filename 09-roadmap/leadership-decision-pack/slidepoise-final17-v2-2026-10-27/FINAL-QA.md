# Agentic CPU µArch Insight — 17 页可编辑 PPTX QA

日期：2026-10-27。页序固定 S01–S17。使用本地 SlidePoise 与 `academic-cpu-insight` Profile 重建。

## 输入与版本

- v2 Work 输入 ZIP 的 17 张正文 PNG、17 张全页预览、17 份备注、QA 与 manifest 已校验。完整源包 `Agentic_CPU_17Slides_Full_Source_v2_2026-10-27.zip` 也已读取，CRC 无错误，SHA-256 为 `b9a343d90460467631984cd590da13776523364d0cd46b0af3e78e8b2bca3c0b`，与仓库交接文档一致。
- 完整源包中的 17 张正文 PNG 与 Work 输入 ZIP 逐页 SHA-256 一致。`03-original-approved-source/` 是原始 PNG 备份，并非分层 PowerPoint 工程；所有正式重建仍以 v2 正文 PNG 为目标。S12、S16 均来自 v2。

## 结构与备注

- 17/17 页，标准 16:9。母版为全页 2048×1152 的对应比例，正文目标 2048×1070，上下页眉页脚各 41px。
- 17/17 份 Speaker Notes 已写入最终 PPTX，并从 PPTX 逐页读回，与 v2 备注原文匹配。
- 共 1,200 个原生文字对象、2,140 个非图片对象、42 个被结构检查识别的连接对象。共 16 个独立图片对象，单张图片最大覆盖页面 19.17%；无整页 PNG 铺底。封面手机/芯片等复杂装饰仍为可替换图片。
- 17/17 页已由 PowerPoint 文件渲染为独立 PNG 预览，并生成总览图。SlidePoise 文本审计 0 项结构性发现。

## 逐页视觉复核

- 已对 17 页总览、S01、S04、S07、S12、S14 关键页做人工视觉核查。封面主要关系图、S02 论证阶段、S04 生命周期与旁路、S07 热图、S09 任务 DAG、S10 验证结果、S12 层间反馈、S14 基线及证据路径等已用原生对象表达。
- 页面保持已确认的蓝白技术视觉和信息顺序。密集信息页保留了参考 PNG 的较小字号，正式投屏前建议按实际显示设备再看一次可读性。预览由 LibreOffice 渲染；不同 PowerPoint 字体环境可能有轻微换行差异。
- 来源与技术判断沿用 v2 文本和 Speaker Notes；本轮没有重新做全部外部论文实验或原始数据核验。图像原稿本身含少量 Image2.5 文字细节，复杂装饰图中的这些文字并非逐字可编辑。

## 交付文件

- `Agentic-CPU-17-slide-editable-v2-final.pptx` — 可编辑 PPTX，SHA-256 `1be3059bd5b54c7186f4f7cf4249954b1b340e4f2ecddf5201ce9339d4e67262`。
- `preview/slide-001.png` 至 `slide-017.png` 和 `preview/contact-sheet.png` — 17 页渲染预览。
- `editability-and-notes-check.json` — 逐页编辑性、图片面积及备注回读记录。
- `text-audit.json` — SlidePoise 文本结构审计原始结果。
