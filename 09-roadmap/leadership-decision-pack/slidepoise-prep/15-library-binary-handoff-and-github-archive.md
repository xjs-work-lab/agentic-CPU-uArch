# 四页 SlidePoise 试制：真实图片的持久存储及交接修复（2026-10-23）

> **当前事实：12 个实际二进制文件已在用户 ChatGPT Library 持久保存，并在上传后重新 list 核实。GitHub 本仓仅存本清单；PNG/ZIP 二进制尚未真正提交到 GitHub。**  
> 此记录修复此前错误地让 Work 读取其他会话 `/mnt/data/` 临时路径的交接缺陷。**用户已确认 S03、S05、S08、S15 四张预览的视觉方向，Work 应立即推进四页原生 PPTX 试制，而非重新设计。**

## 唯一可靠的当前二进制来源

ChatGPT Library 目录：

`/Agentic-CPU-uArch/slidepoise/four-slide-pilot/`

已确认 12/12 文件有独立持久 `file_id` 和 `libfile` 标识（鉴于此仓可公开，具体个人 Library 标识**不复制到 GitHub**），包含每页的正文 PNG、16:9 全页参考预览和源代码素材 ZIP。机器可核对的全部文件名/字节数/SHA-256 见 [四页文件清单](binary-assets/four-slide-pilot/library-assets-manifest.json)。

| 页面 | Work 必需的 2048×1070 正文 PNG | 完整 16:9 视觉对照 | 附带重建源码 ZIP |
|---|---|---|---|
| S03 | `S03-controlled-content-v01.png` | `S03-16x9-frame-preview-v01.png` | `S03-controlled-source-and-PNG-v01.zip` |
| S05 | `S05-controlled-content-v04.png` | `S05-16x9-frame-preview-v04.png` | `S05-controlled-source-and-PNG-v04.zip` |
| S08 | `S08-controlled-content-v01.png` | `S08-16x9-frame-preview-v01.png` | `S08-controlled-source-and-PNG-v01.zip` |
| S15 | `S15-controlled-content-v01.png` | `S15-16x9-frame-preview-v01.png` | `S15-controlled-source-and-PNG-v01.zip` |

## Work 应如何取得文件（不要再尝试其他会话的 sandbox 绝对路径）

1. 在有权限的 ChatGPT Work 会话通过 **Library** 查找 `Agentic-CPU-uArch/slidepoise/four-slide-pilot`；优先把四份 `*-controlled-source-and-PNG-*.zip` 下载/导入本地 Work 工作目录，或者直接取得四张 `*-controlled-content-*.png`。**在继续前先确认读取到真实图像字节。**
2. 若 Work 无法自动浏览 Library，**用户可以从文件附加入口选择 Library 中的这四份 ZIP 或四张正文 PNG 并附加至 Work**。这是一项文件附加动作，不需要重新生成图片，也不必使用无法打开的 sandbox 链接。
3. 从 ZIP 中取得可复用脚本、SVG、PNG 和 QA 数据；将图片校验值与本文件关联的 [manifest](binary-assets/four-slide-pilot/library-assets-manifest.json) 对照；不得从 GitHub 的纯文本 `manifest.json` 误判 PNG 二进制已经存在。
4. 真正把四页完整素材 ZIP 与 PNG **提交到 GitHub 的固定目标路径**：
   `09-roadmap/leadership-decision-pack/slidepoise-prep/binary-assets/four-slide-pilot/`。更新 README 的“GitHub 二进制”状态之前，**必须通过 GitHub API/read-back 确认实际 PNG 文件路径存在且字节 SHA-256 相同**。
5. 按 [07 Work 交接](07-work-mode-handoff.md)构建四页原生 PowerPoint：页面 16:9，完整 `2048×1152`；正文 `2048×1070`；frame 上下各 41px；标题、DAG 框和边、实验图表、矩阵、年份及结果数字 native 可编辑；备注真实写入后回读；完成渲染检查。
6. **只试制四页**，不要直接扩展全部17页或重新打开无关研究。

## 四页来源合同（优先级高于 PNG 的 OCR 文本）

- S03：[14-S03 内容合同](14-s03-approved-copy-and-reconstruction-contract.md)及 [Speaker Notes](notes/S03-speaker-notes-2026-10-23.md)。
- S05：[11-S05 内容合同](11-s05-approved-copy-and-reconstruction-contract.md)及 [DAG 连接合同](generated-images/formal-content-v02/S05-edge-contract-v02.json)。
- S08：[12-S08 内容合同](12-s08-approved-copy-and-reconstruction-contract.md)；PyTorch/Arm vivo X300 数据不得变更。
- S15：[13-S15 内容合同](13-s15-roadmap-content-and-reconstruction-contract.md)；2029“条件研究”不得画成流片/量产承诺。

## 这次保存解决了什么，尚有哪些未解决

- **已解决**：四张用户认可的内容 PNG **真实文件被可靠持久保存**；原来仅有临时 sandbox 存储的缺口已经修复。
- **仍未解决**：12 个二进制当前只在 ChatGPT Library，**GitHub 还未收到图片字节**；待 Work 从 Library 读取之后推送并实际验收。不得在本仓状态栏写“GitHub 图片已归档”。
- **下一交付 Gate**：四页 PPTX 文件实际存在、PowerPoint 原生对象可编辑、真实截图与 PNG 对照、Notes 嵌入与回读、GitHub 二进制真正入库。
