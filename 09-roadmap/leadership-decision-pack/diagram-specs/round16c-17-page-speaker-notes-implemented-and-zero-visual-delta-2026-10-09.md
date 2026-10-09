# Round16C — 17 页演讲者备注已全部改写并通过零视觉变化 QA

日期：2026-10-09。**状态：17页新备注已确实写入可编辑PPTX，已执行二进制/OXML、讲者备注读取与同源 PDF 不变性检查；待用户实际审阅内容及 Microsoft PowerPoint 终验。**

## 用户要求和本次交付

用户要求“每页的备注首先是ppt实际内容的更详细的解释，然后才是相关来源的逐条说明，来自哪儿，主要观点、论据，支撑了什么结论等等”。完整规范参见[Round16C 讲者备注合同](round16c-speaker-notes-explanation-first-and-source-evidence-contract-2026-10-09.md)。

**本轮已实际完成**：
- 以 [Round16B 箭头已修复完整17页](round16b-native-horizontal-arrow-alignment-no-text-change-2026-10-09.md) 为唯一修改输入；
- 17页 Notes 正文全部改为 **“一、页面内容详细讲解”在前→“二、来源逐条解读”在后**；
- 第一部分按实际视觉元素逐一解释图表、操作路径、指向与异常分支、真实统计口径、技术因果及CPU/LLVM、Agent/App、Runtime/OS责任域；
- 第二部分对**47条来源条目**独立解释机构/论文及原始URL、问题和主要观点、技术方法/数据论据、支撑哪幅图/结论、不能证明及不得外推的结论；
- 原先封面、目录备注错误说“前两页无编号”已纠正为**封面01/17、目录02/17、正文03–17/17**。目录按四章的实际物理页序介绍。

这轮没有重做幻灯片、没有添加虚构论文/测试，也没有改标题/数据/箭头或对比关系。备注中的研究归纳明确标注跨来源推断，不伪称任何论文已证明新Agent-only ISA。

## 基础结构验收（已实测）

- PPTX包含17页，全部17页notes_text_frame可被读取并与导出审核稿逐字匹配；
- **30,143 个备注字符、47条逐份来源解读**，每页都有独立第一、第二部分；
- 从原Round16B PPTX的**103个 OOXML ZIP 文件**来看，**只改动17个 `ppt/notesSlides/notesSlide1.xml` … `notesSlide17.xml`**，剩余**86个成员字节完全相同**，包括17页投影原始XML、超链接关系、媒体、母版、图形和页码；
- 旧新版逐页 PowerPoint文本 shape 按内容顺序完全一致；
- LibreOffice成功将新版打开导出为17页16:9 PDF；新版PDF与原Round16B PDF**17/17页提取文本完全一致**；
- 备注首部分最短仍有636字符，不再用“一句结论＋来源链接”代替页面讲解；全部来源说明均含原始 URL、论据/依据、支撑该页和不能证明/局限；
- Microsoft Windows PowerPoint备注页可读性/滚动显示**仍待实机确认**，不能把库解析成功冒称用户已最终验收。

## 关键科学边界（本轮保留/强化）

- Snapdragon数据区分单次MUL_MAT的Prefill/Decode微秒与Decode累计算子耗时毫秒，NPU call-usec不可称纯算子内核时延；CPU回退与通信是具体软件路径而非故障；
- ShadowNPU 与 llm.npu是有关联但方法不同的研究；MI14端到端、K60单kernel能耗、任务平均准确率不能混成同一测试；
- SME是CPU ISA扩展，不是同CPU并列的独立SoC处理器；SMEPilot的Apple M4 Pro ablation非手机专有实验；
- HeRo的五步任务图是根据论文解释性简化重绘，不是论文原图或量产硬件电路；
- 工具回执成功与用户真实意图达成不同；共享缓冲与派生计算状态语义有效性不同；
- 主动Agent的低功耗筛选不是官方已推出的统一跨平台语义协议；软件与低功耗硬件已有很强基线；
- **三类工程平台优先≠三项已验证Agent CPU新硬件**，三项条件研究仍待新公开证据，2027–2029只是技术顺序建议，不代表内部资源、芯片排期或实验批准。

## 当前文件（在对话附件空间，未将二进制提交GitHub）

- `/mnt/data/round16c_notes_upgrade/Agentic_CPU_uArch_2027-2029_17slides_explanation_first_notes_editable.pptx`：**当前最新完整17页可编辑演讲版**；
- `/mnt/data/round16c_notes_upgrade/SPEAKER_NOTES_17SLIDES_REVIEW.md`：新17页备注文字的直接导出审核稿；
- `/mnt/data/round16c_notes_upgrade/NOTES_UPGRADE_QA_2026-10-09.md`、`NOTES_QA.json`：逐页来源数量、文字保真和文件结构验收；
- `notes_01_08.py`、`notes_09_17.py`、`patch_and_qa.py`：Notes-only生产源码与检查脚本。
- 17页可见PDF版式同Round16B，备注不会自动显示在普通PDF投影片中，故最终交付重点是PPTX＋备注审核稿。

**Round16C（Notes-only）为最新的17页交付候选；需用户审阅技术说明是否完整后才能宣称最终通过。**