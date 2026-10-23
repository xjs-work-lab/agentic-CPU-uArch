# Round06｜S05 受控文字与有向连线 PNG 正式尺寸候选（2026-10-23）

> 审查结果：**实物 PNG 已生成，并在当前聊天会话中以可下载文件提供；GitHub 已归档 manifest，本轮没有直接上传 GitHub 二进制 PNG。**  
> 状态：`CONTENT_SAFE / SVG_RENDER_INSPECTED / USER_VISUAL_APPROVAL_PENDING / SLIDEPOISE_ACCEPTED_NOT_YET`。  
> 这是以用户认可的 Image2.5 蓝白科技视觉为参考、按受控内容合同**重新排版与矢量渲染**的 PNG，不是对 Image2.5 原始图片简单涂掉数字。PNG 中的中文、框体与箭头都来自审定技术内容，而不是图片模型重新生成的数字。

## 1. 本轮真实产生的文件

| 实物 | 精确尺寸 | 内容 SHA-256 | 状态 |
|---|---|---|---|
| `S05-controlled-content-v04.png` | **2048×1070** | `289df22c044c3a74e82f767fe9f52d0deaabb926b4b9bb7026b883e9f1e6547c` | 当前聊天附件已生成，GitHub 二进制尚未提交 |
| `S05-16x9-frame-preview-v04.png` | **2048×1152（16:9）** | `b4c04de83c084f4b48e52ead5dcedc74c12f112a2d7934fa3c7e4012684fc39a` | 当前聊天附件已生成，GitHub 二进制尚未提交 |
| `S05-controlled-content-v04.svg` | **2048×1070** | `a4897c92d621c46d4b0e340a502ae073c9b1d2efc898a776a871fe5f5ff1e87f` | 真实 SVG 已生成于聊天执行环境；GitHub 源码尚未提交 |
| `S05-controlled-source-and-PNG-v04.zip` | 四源文件+QA | 见当前聊天附件 | 可直接作为本地重建/归档输入包 |

内容哈希与状态已机器可读归档：[S05 PNG manifest](../generated-images/formal-content-v02/S05-controlled-png-v04.manifest.json)。

## 2. 视觉和技术内容审查（已执行）

| Gate | 检查 | 实际结果 |
|---|---|---|
| G2 技术主张 | 不再把 S05 写成「将全部 Decode、MLP、Attention 送 NPU 加速」 | PASS |
| G2 未验证数字 | 3.3×/2.5×/40–60% 等图片模型自加测量 | **出现 0 项** |
| G2 DAG 节点 | 用户目标→任务规划→可选查询重写→A/B 检索→聚合/重排→推理/生成→可选工具→验证→状态更新 | **10 个逻辑节点** |
| G2 DAG 语义边 | 13 条源/目标确定的控制与数据连接，旁路、条件工具执行、结果验证、反馈 | **13 条** |
| G2 来源与边界 | HeRo=动态 DAG；SERENO=共享内存 QoE；明确非定量实测 | PASS |
| G2 图像尺寸 | 2048×1070 正文、2048×1152 母版示意 | PASS |
| G2 渲染 | 真实 SVG→PNG，实际打开查看整体版式及主要文字/箭头路径 | PASS（本轮检查范围） |
| G2 文本边界 | 根据已安装 Noto Sans CJK 字体真实字宽估算裁切 | 0 处越界 |
| G3 真 PPTX | SlidePoise packaged PNG→native editable PPTX/Notes | **未执行** |

**特别说明**：本机验证字体为 Noto Sans CJK SC，用户 Windows 上的目标字体为 Microsoft YaHei，视觉字宽可能有小差异。正式 native PPTX 必须重读实际 fonts 和 PowerPoint 渲染，不能把本次本地 PNG 看作 Windows PPT 渲染验收。

## 3. 人工视觉审查结果

- 最终 PNG 维持用户认可的蓝白科技感：上部结论式标题、中部 DAG+约束双栏、底部一排在线调度迭代。
- DAG 修正了两种并行、可选查询重写及无需工具可直接验证的控制路由，且反馈应仅发生在任务继续/需要修订时。
- 因为证据与模型难以支撑任何通用 S05 加速数据，右栏只保留 **四类条件**，不给伪造精确柱、百分比或倍数。
- 将「局部算子快 ≠ 端到端快」作为可解释的结论，不用确定增益替代系统级评价。
- 仍建议由最终汇报使用者在完整分辨率下冷读一遍 S05，以确认右栏标签和底部引文的密度符合投影观看要求。

## 4. 给 Work / SlidePoise 的交接

需要一起消费：
1. **本次实际 PNG（正文 2048×1070，不是整页 16:9 的预览 PNG）**；
2. [最终 S05 内容合同](../11-s05-approved-copy-and-reconstruction-contract.md)；
3. [机器可读 DAG 边](../generated-images/formal-content-v02/S05-edge-contract-v02.json)；
4. [真实母版画布合同](../09-frame-and-content-region-contract.md)；
5. 本轮 manifest 和审稿记录。

**绝不可从图片 OCR 判断哪个箭头应该连接哪一个节点、擅自更改控制语义或添数字。** PNG 负责视觉，正式文字/节点/箭头来自合同。整页的 header/footer/page number 应由原生母版填充，而非把全页预览当 substantive input。

## 5. 仍需完成的交付动作

- 用户视觉确认后，可将文件标成 **技术与视觉候选已认可**；但 `SlidePoise packaged accepted-slide.png` 还需满足本地生成包、frame 和 image acceptance 约束。
- GitHub 中**已经写入本 manifest 和本 QA 文档**；PNG 的二进制提交本次连接工具没有直接完成，不能在 README 中标为“GitHub PNG 已归档”。可下载的 zip 包包含 PNG、整页预览、SVG、生成器脚本和 QA JSON，可由本地 Work 复用/归档。
- 待 Work 生产后仍需对 PPTX 的母版页码、原生可编辑对象、连接线和 Speaker Notes 做真实读回与逐页视觉 QA。

**下一张应进入 S08**，继承这次解决的“Image2.5 风格参考 + 受控原始技术事实”的方式，但 S08 的公开数值 555.8→304.1ms / 1163.0→298.2ms 必须和 vivo X300、SqueezeSAM 单核 CPU 路径同页出现。
