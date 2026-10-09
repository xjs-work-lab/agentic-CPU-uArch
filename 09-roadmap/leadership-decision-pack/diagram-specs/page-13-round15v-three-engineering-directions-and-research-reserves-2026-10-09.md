# 正文第 13 页：工程方向与条件研究分层（Round15V）

**2026-10-09；状态：纯蓝色可编辑 PPTX/PNG 已制作，通过基础 QA，待用户审阅。**

## 已制作的正文主张
**现阶段优先推进三类现有技术能力；三项硬件相关研究问题先保留研究，不直接启动 Agent 专用设计。**

- **CPU/LLVM**：SME2/Neon 等现有 CPU 执行路径、微内核、编译生成和布局复用，解决适合 CPU 的模型阶段开销。主要责任是 CPU/Compiler，不假称 CPU 对所有模型更快。
- **Agent/App + OS**：工具目标/权限绑定和实际效果核验。解决“工具返回成功不等于用户目标完成”，属于平台而非新增 CPU 指令。
- **Runtime/OS**：根据阶段、前台 QoE、同步、回退和共享带宽优化 CPU/GPU/NPU 放置。
- **三个具体开放问题（不是三项芯片方案）**：任务进度中不能由完整日志重建的新增信息；跨引擎派生数据的物理有效性残余；CPU 恢复后的缓存/微状态局部性残余。
- **持续观察**：主动 Agent 的低功耗实现、通用共享缓存和恢复时序；不因已有任务优先级、取消、缓冲管理等功能就提出“Agent 专用” ISA。

## 来源对照 / 逐来源备注
1. [When NPUs Are Not Always Faster](https://arxiv.org/abs/2605.27435)：支撑 CPU/NPU stage、fallback 和后端成本需要同条件考虑；**不能**证明 CPU 永远更快或新增 Agent ISA。
2. [HeRo](https://arxiv.org/abs/2603.01661)：支持多阶段 Agentic RAG 存在软件调度与争用管理空间；**不能**证明新硬件必要性。
3. [LLVM AArch64SME](https://llvm.org/docs/AArch64SME.html)：支持已有 SME ABI 和编译规则；**不能**推出任意 Agent 端到端收益。
4. [Apple Tool Calling](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling)：支持外部工具与副作用能力的存在；**不能**将回执当目标已完成证据。
5. [项目当前权威路线](https://github.com/xjs-work-lab/agentic-CPU-uArch/blob/main/09-roadmap/current.md)：研究综合结论为三类工程/平台方向、三项条件研究、无已证实的独立新 Agent CPU 电路方案；不是正式项目批准。

**所有五项在 PPTX 演讲者备注中各有独立条目：来源/已证明/未证明/本页对应，并明确研究综合推断。** 不使用历史方向代号或商业化标签。

## 实物与当前限制
位于同一对话运行时目录 `/mnt/data/round15v_slides13_15/`：三页合并 PPTX、`page-1.png`、`make_slides13_15.js`、装饰图。二进制文件**尚未提交 GitHub**。本页 55 个原生可编辑对象 + 1 张独立装饰图、4 条页面可点击来源链接，备注解释了 5 项来源。页码 `13 / 15`；同源 PNG 为 1920×1080；无禁用词。最终 Microsoft PowerPoint 和全17页一致性待验。
