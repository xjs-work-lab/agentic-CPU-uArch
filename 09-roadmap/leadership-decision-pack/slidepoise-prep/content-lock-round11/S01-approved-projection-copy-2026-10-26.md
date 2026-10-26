# S01｜Agentic AI 将改变手机 CPU 与异构系统的协作方式

> 修订状态：G1_PASS_REVISED｜2026-10-26｜权威内容：02/03/04合同 + current.md + DEC-PORTFOLIO-002/DEC-A-008。此文件为 Image2.5 生成前的**受控投影文案**，没有授予任何旧图 G2 通过资格。

## 投影主标题（逐字）
**Agentic AI 将改变手机 CPU 与异构系统的协作方式**

## 可见副标题
2027—2029 手机 CPU/uArch、LLVM、Runtime/OS 技术洞察

## 投影框图 / 卡片的受控文案
1. **单句判断**：从一次性推理，延伸到多阶段任务、可信工具执行与可修订状态。
2. **画面任务**：左：用户目标 → 计划 / 计算与工具（条件） → 实际效果核验。右：SoC 概念框，CPU / GPU / NPU / 共享 DRAM，由 Runtime/OS 协同。
3. **范围标签**：公开证据 · 技术路线建议 · 手机 AArch64 优先

## 来源映射（Notes 与图中短引按实际主题关联）
- 09-roadmap/current.md
- 09-roadmap/agentic-cpu-uarch-detailed-research-summary-cn-2026-10-20.md
- VENDOR-032 (Apple Session/Tools API as capability example)

## 必须写入画面或讲者备注的边界
- 封面只解释对象与范围，不展示定量实验与假想芯片互连。
- 2027–2029 是规划时间窗，不代表厂商实际产品发布日期/公司批准的研发排期。
- 不在封面上陈列 3/3/0 详细策略卡，该论证由 S03 承担。

## Speaker Notes（按本页主题重新撰写，非旧版同页码复制）
1. 先解释手机 Agent 不只在终端运行一个 LLM，可能包含计划、跨模型推理、工具调用、目标验证和状态迭代。
2. CPU 角色是通用控制与部分计算；NPU/GPU 是按能力与成本使用的资源，不是 CPU 内含的指令部件。
3. 本报告基于公开论文、厂商/框架文档、专利与开源项目，对未来三年提出建议；未做真机测量，没有确定新 CPU 指令或 silicon 项目。

## 画面关系审核
- 封面只用最少抽象关系图，不能出现假想芯片互联硬件结构。 

## G1/G2 Gate
- G1 内容与证据：G1_PASS_REVISED; 
- G2 新 PNG 是否生成：NOT_STARTED; 旧8张 Image2.5 候选仍处于 REJECTED/HOLD 隔离状态。
- 不得把本文件的 G1 通过解释为原有 PNG 可以交给 Work。
