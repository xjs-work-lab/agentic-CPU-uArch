# 17页视觉获认可版本｜最终 PNG 归并、真文件存储及 Work 交接（2026-10-27）

> **历史版本 v1，已经废止。** 2026-10-27 新版 S12、S16 Image2.5 图已获用户视觉认可，并已制作更新的17页ZIP。请优先阅读 [v2 唯一有效交接](18-final17-v2-image-assets-and-work-handoff-2026-10-27.md) 和 [v2 manifest](qa/final17-v2-library-binary-manifest-2026-10-27.json)。本页下方的 S12/S16 P1 阻断与 v1 文件哈希仅代表历史，不再描述当前版本。**不得拿 v1 ZIP 作为 Work 输入。**


> 本轮完成 **17/17 页正确顺序的真实图片归并**：17 张 substantive **2048×1070 PNG** + 17 张 16:9 **2048×1152 预览** + 17 张用户认可的原始图片备份 + 17 篇当前页序 Speaker Notes + 17页顺序总览 + QA/每项 SHA-256 机器清单。
>
> **严格状态区分：17/17 用户视觉认可；15/17 达到当前内容合同基本输入标准（部分带解释边界）；S12 技术内容P1缺口，S16 投影证据等级 P1不足。两页必须修订或明确豁免，才可宣布17/17技术审定。尚无本轮 PowerPoint。**
>
> 本文档按最终真实文件校验情况编写，2026-10-27 生效；覆盖任何历史“17页全部已经进入 Work”之类的推断，不撤销历史审计记录。

## 1. 持久存储（真实二进制，不是临时 /mnt/data 路径）

实际完整上传、重新列出并从 ChatGPT Library 取回校验通过的路径：

`/Agentic-CPU-uArch/slidepoise/final17-2026-10-27/`

| 实物 | 文件字节 | SHA-256（完整） | 具体内容 |
|---|---:|---|---|
| `Agentic_CPU_17Slides_PNG_Work_Input_2026-10-27.zip` | 67,100,508 | `c123cce034d4d8d2eb7d8c76ae5948abc1b0cbaea8f1b25a7ef124da1f4b347f` | 17正文、17整页预览、17 Notes、总览、逐页QA与manifest（55个条目） |
| `Agentic_CPU_17Slides_Full_Source_2026-10-27.zip` | 89,604,648 | `9d53ec064be0af0f3510903413408e067bb45113e464a5fe4baab2f0b92692fa` | 上面全部＋17源图片备份＋3个处理/审计脚本（75个条目） |
| `17-slide-contact-sheet.png` | 6,383,927 | ZIP 内 `manifest.json` 另有自身SHA-256 | 17页顺序图，4列×5行，按页码S01至S17 |

两个 ZIP **均已从 Library materialize 回读，源字节 SHA-256 完全一致且 testzip() CRC 检查全部通过**；所有17页 PNG 和 notes 在 ZIP 内逐路径验证无缺项。

## 2. 冻结的页序与所采用的真正原图版本

| 页码 | 技术主题 | 本次实际采用的原图片文件 | 内容审计 |
|---|---|---|---|
| S01 | 封面：Agentic AI 与手机异构系统 | `agentic_ai驱动手机异构协作.png` | PASS |
| S02 | 目录 | `Round11/S02-round11-v01-content.png` | PASS |
| S03 | 总体判断 3/3/0 | `S03-controlled-content-v01.png` | PASS |
| S04 | Agent 负载四类变化 | `手机智能体任务负载全景图.png` | PASS |
| S05 | 动态 Agent DAG | `S05-controlled-content-v04.png` | PASS |
| S06 | CPU/NPU 阶段交叉点 | `Round11/S06-round11-v01-content.png` | PASS |
| S07 | llm.npu / ShadowNPU | `npu优化与异构协同技术全景图.png` | REVIEW_NOTE |
| S08 | CPU SME2 / 手机实证 | `S08-controlled-content-v01.png` | PASS |
| S09 | HeRo / SERENO | `runtime_os_协同调度架构.png` | REVIEW_NOTE |
| S10 | 可信工具真实效果验证 | `可信智能体真实效果验证流程.png` | PASS |
| S11 | 软件账本强基线 | `软件任务账本与语义进度控制机制.png` | REVIEW_NOTE |
| S12 | 跨层状态/低功耗/语义进度 | `跨层状态治理与agent生命周期管理.png` | CONTENT_P1_BLOCK |
| S13 | 三优先工程责任 | `软件工程优先的系统能力路线图.png` | REVIEW_NOTE |
| S14 | 三条件研究/证据门槛 | `强软件基线下的硬件研究边界.png` | PASS |
| S15 | 2027–29 三年建议 | `S15-controlled-content-v01.png` | PASS |
| S16 | 证据等级与不能外推 | `证据边界与硬件重审路径.png` | CONTENT_P1_REVIEW |
| S17 | 当前技术决策 | `软件优先与证据驱动的三年路线.png` | REVIEW_NOTE |

**特殊检查**：
- S02/S06：用用户认可的 Round11 受控修订版；旧 Image2.5 错目录/伪性能柱形不得再流入。
- S03/S05/S08/S15：沿用用户先前通过的四页试制目标图，不重做。
- S07/S09/S10/S11：用后来由 Image2.5 真正独立完成、用户认可的完整版设计，**不使用 Round12 用户视觉拒收的机械 SVG 流水线**。
- S12–S14、S16、S17：用最近用户视觉认可的 Image2.5 页图，保留原图字节备份。
- 新统一尺寸生成原则：原长宽约1.914比的图只做等比缩放；原始 16:9 的 Image2.5 图等比放入 **2048×1070** 后左右各约 73px 白边，**不裁切文字，也不横向拉伸**。全页框是 header 41 + substantive 1070 + footer 41 = **2048×1152**。
- S16/S17 Image2.5 原图自己带右上角16/17、17/17，为避免与真实全页原生页脚页码重复，生成统一 substantive 时仅在空白上角遮除原内嵌页码；原图备份保持不变。

## 3. 两个 Work 前内容 Gate（不可遗漏）

1. **S12：CONTENT_P1_BLOCK**。画面深入讲状态生命周期、账本、缓存与隐私，但不足以完整交代当前 [S12合同](02-slide-contracts.md) 的另外两条主题：`主动低功耗准入（感知事件→价值→是否唤醒）`、`语义进度/QoE（继续、换模型、验证与前台体验）`。仅在 Notes 提到不算解决；建议用 Image2.5 保留版式整体修订这一页，再让用户复审。
2. **S16：CONTENT_P1_REVIEW**。画面按“支持/不能外推/何时重审”三栏展开，方向正确，但 [S16合同](02-slide-contracts.md) 要求屏幕明确区分四种证据级别：「直接事实／跨来源推断／待证实假设／尚无足够证据支持的主张」。建议补一个四级图例并冷读确认。

非阻断但须 Notes 解释：S07 的 CPU/GPU 分工箭头不能当固定序列，S09 CPU/NPU 执行泳道属示意放置，S11 未证实的私有任务进度不是发现的新CPU寄存器，S17 “季度复审”是一条建议而非现有承诺。

## 4. Work / SlidePoise 后续操作规则

1. 本轮 **不生产 PPTX**。在 S12/S16 内容门槛完成并得到用户视觉认可后，才可迁入真正 native 编辑 PPTX。
2. Work 的可靠文件入口是上述 Library 文件夹。若 Work 无法检索 Library，请用户在 Work 附件菜单选择一个 `Agentic_CPU_17Slides_PNG_Work_Input_2026-10-27.zip` 并附加，**不要引用另一个会话的 /mnt/data**。
3. 只使用 ZIP 内 `01-substantive-2048x1070/Sxx-content.png` 作为 packaged reconstruction 的正文目标，`02-full-16x9-2048x1152/Sxx-preview.png` 用来检查完整母版效果；来源/文字/箭头语义以 `02-slide-contracts.md`、`03-evidence-map.md`、`04-risk-boundaries.md` 和 ZIP 内 Speaker Notes 为准。
4. 真 PPT 16:9，header/footer 各41px由 PPT 原生 Master 构成；高密度蓝白学术技术汇报；标题/数字/大部分框图/箭头/表格 native 可编辑，复杂图形可独立图资产；禁止整页 PNG 假装可编辑。
5. 逐页渲染比对 PNG，检查字体/中文、引用边距、箭头、页码与来源，Speaker Notes 必须写入 PowerPoint 并从 .pptx 真实读回。
6. ZIP 与源图二进制已在 Library 持久归档，但 **GitHub 主仓本轮尚未真实上传 ZIP/PNG 的二进制字节**；仓库内仅 QA/索引/现有合同。Work 如要求 GitHub 也保存，须在本地以 git/LFS或其它合法路径上传后 read-back 按 SHA 校验，才可升级 `GITHUB_BINARY_COMMITTED` 状态。

## 5. 与现有项目权威一致

研究结论依 [current.md](../../current.md) 和正式 DEC-PORTFOLIO-002、DEC-A-008 生效：三类软件/平台工程重点、三项条件研究储备、零独立新增 Agent CPU 硬件主押注；没有新增实际手机测量，也没有批准硬件开发。

**本次的完成标准**：17页图片、页序、备注、QA、压缩包与可迁移持久地址都已经真正建立；剩余 S12/S16 **是内容审核收尾问题，不是图片遗失或图像生成缺页**。
