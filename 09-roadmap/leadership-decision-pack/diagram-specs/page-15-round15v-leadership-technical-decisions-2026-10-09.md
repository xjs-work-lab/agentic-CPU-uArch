# 正文第 15 页：技术路线的管理讨论事项（Round15V）

**2026-10-09；状态：可编辑 PPTX/PNG 已制作、通过基础 QA，待用户审阅。**

## 已制作的正文主张
**现阶段应明确技术优先级、跨团队责任与新硬件重审条件；资源安排和产品时间表需另行评审。**

管理层可实际回答的三个问题：
1. 是否将现有 CPU/LLVM 高效执行、Agent 工具可信效果与 Runtime/OS 跨引擎协作排在优先位置？
2. Compiler/CPU、Runtime/NPU、Agent/App、OS 之间由谁承担执行代码、路径选择、授权和真实效果确认？**只提出技术责任域，不虚构组织负责人。**
3. 哪类**新的独立公开手机证据**可以重新触发新硬件方向的研究？软件基线应足够强、硬件残余需物理可定位、收益须可与面积/能耗/风险比较。

三条边界：不把不同设备/模型的论文结果拼成通用收益；不把软件工具、优先级、共享缓冲等已有能力包装成独有硬件；不将专利/概念图替代手机性能和组织审批。

最终结论：**优先已有 CPU/LLVM 与软件协作；三项研究问题有界保留；当前缺足够证据支持新 Agent 专用 CPU ISA。**

## 逐来源演讲者备注
1. [现行技术路线](https://github.com/xjs-work-lab/agentic-CPU-uArch/blob/main/09-roadmap/current.md)：正式综合研究判断的依据；**不是**团队批准和资源分配记录。
2. [2027–2029 年×层公开研究路线](https://github.com/xjs-work-lab/agentic-CPU-uArch/blob/main/09-roadmap/round15e-integrated-public-roadmap-2027-2029.md)：技术先后与跨层依赖，**不构成**量产时间表。
3. [HeRo](https://arxiv.org/abs/2603.01661)：软件调度路线强基线，**不能**证明每种 Agent 都有相同比例的提升。
4. [LLVM AArch64SME](https://llvm.org/docs/AArch64SME.html)：已有 CPU 编译/调用能力，**不能**推出新 Agent ISA 必需。
5. [Apple Tool Calling](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling)：已有工具调用能力，**不能**推出目标完成或可靠性完全由 CPU 提供。

以上五份**逐条独立写入可编辑 PPTX 的讲者备注**；各说明证明范围、非证明范围、与本页的对应点，并列出研究综合推断、尚需证据及公开资料研究的边界。

## 交付及 QA
三页合并 PPTX、`page-3.png`、JS 源和装饰图位于 `/mnt/data/round15v_slides13_15/`；第 15 页 51 个原生可编辑元素与一幅可移动的装饰图片、4 条可点击可视来源链接；同源 1920×1080 PNG，`15 / 15` 页码，无禁用词。**用户审阅/全17页整合/Microsoft PowerPoint 兼容性仍未完成**。
