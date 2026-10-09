# Round15Y｜17 页正式汇报底部引用安全留白修订

日期：2026-10-09。**状态：可编辑 PPTX / 同源 PDF / 17 张高清 PNG 已实际制作，通过 LibreOffice 与 OOXML 基础 QA；仍待用户与 Windows Microsoft PowerPoint 终验。**

## 用户意见与修改目标

上一版 17 页合并后，用户指出“每页最下面的引用链接太靠下了，很难看到，所以最下方最好留点空白，整体内容往上挪一挪”，并批准进入修订。

**设计固定约束**：保持已认可的内容、结论、论文数据、来源链接、演讲者逐来源备注、配色、封面和目录；只调整正文页下部的纵向分布及引用区的页底安全距离。不能粗暴把整页变成图片，也不能使正文图表覆盖标题或页码。

## Round15Y 实际实施

- 以 [Round15X 完整17页集成版](round15x-full-17-slide-integration-qa-2026-10-09.md)为唯一修改输入（保留已认可每页版本）。
- 对物理页 3–17（正文 01–15）将页顶标题、说明及正文页码固定，正文内容沿其上沿轻微纵向收紧，约 **94.2%–94.5%**。下方总结框、引用链接因此自然上移约 0.3 英寸，不改变横向布局与对象层次。
- 第 06 页 SME2、第 08 页 HeRo 采用较高正文锚点以避开不同高度的标题带。
- 物理页 1–2（封面、目录）未改变。
- 来源文字、技术论点、字体属性、图片、超链接目标、演讲者备注**均未修改**。

## 验收结果

| 检查 | 结果 |
|---|---|
| PowerPoint 幻灯片数 | 17，16:9 |
| 形状 | 1,042（1,025 个原生文字/形状 + 17 张独立装饰图），数量与原版逐页一致 |
| 可见文字 | **17 页逐字完全一致**，没有改写或漏字 |
| Speaker Notes | **17 页逐字完全一致**，保留逐来源“已证明／未证明／本页对应” |
| PPTX 外链 | **34 条，原 URL 与数量保持一致** |
| PDF 文本 | 重新渲染后 17 页与原 PDF 逐页文本完全一致 |
| 引用距离页底 | 典型页从原来约 **0.00–0.04 英寸**提高到 **0.33–0.50 英寸**（8–13 毫米）；新版本按页核算 |
| 文件 / 渲染 | ZIP 完整；LibreOffice 导出 17 页 PDF；17 张约 1920×1080 PNG 渲染；总览图已检查 |
| 用户验收 | **待用户查看优化版**；不能因程序验证通过而写成最终 Office 验收 |

**重要解释**：此次采用微小的纵向几何压缩，所以在原生可编辑对象中改善安全空白，但没有扩大引用字号。实际 1080p 投影的引用字号仍需在使用环境中审阅；若依然太小，应局部提高文字大小，而不是再无限抬高正文。

## 可编辑文件与再生产

当前会话附件（**二进制未入 GitHub**）：

- `/mnt/data/round15y_footer_safe_v2/Agentic_CPU_uArch_2027-2029_17slides_footer_safe_editable.pptx`
- `/mnt/data/round15y_footer_safe_v2/Agentic_CPU_uArch_2027-2029_17slides_footer_safe_editable.pdf`
- `/mnt/data/round15y_footer_safe_v2/Agentic_CPU_uArch_17slides_footer_safe_contact_sheet.png`
- `/mnt/data/round15y_footer_safe_v2/Agentic_CPU_uArch_17slides_footer_safe_PNG.zip`
- `/mnt/data/round15y_footer_safe_v2/FOOTER_SAFE_QA_2026-10-09.md`
- `/mnt/data/round15y_footer_safe_v2/reflow_footer.py`、`qa_footer_revision.py` 与 `qa_footer_revision.json`.

## 下一步

用户审阅优化后整套投影版，主要关注底部链接是否看得见、是否有文字挤压、整体页面密度是否舒适。Windows PowerPoint 的实际字体、链接点击、演讲者备注与会议室投影最后确认后才标为终稿。之后任何重新合并不得退回 Round15X 的页底参考位置。
