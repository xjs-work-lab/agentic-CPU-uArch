# S09｜Agent 工作流调度与前台内存争用应由 Runtime/OS 协同管理

> 修订状态：G1_PASS_REVISED｜2026-10-26｜权威内容：02/03/04合同 + current.md + DEC-PORTFOLIO-002/DEC-A-008。此文件为 Image2.5 生成前的**受控投影文案**，没有授予任何旧图 G2 通过资格。

## 投影主标题（逐字）
**Agent 工作流调度与前台内存争用应由 Runtime/OS 协同管理**

## 可见副标题
HeRo 优化任务依赖与资源放置；SERENO 约束后台计算对前台交互的影响。

## 投影框图 / 卡片的受控文案
1. **HeRo｜Agentic RAG 阶段 DAG**：动态可见阶段、异构资源亲和性、形状感知与并行/带宽限制 → 优化任务完成时间。
2. **SERENO｜前台 QoE 与共享带宽**：背景 LLM 占用共享 DRAM 带宽会导致前台卡顿；用可让步机制/带宽控制保护前台体验。
3. **共同归属｜Runtime/OS**：任务阶段调度、NPU CPU/GPU放置、共享DRAM带宽、前后台公平/回收以及QoE观测。
4. **不混淆**：HeRo 控制的对象是 Agent 阶段 / 任务延迟；SERENO 控制的是后台 LLM 与前台 App 的带宽冲突 / 体验。

## 来源映射（Notes 与图中短引按实际主题关联）
- PAPER-098 HeRo https://arxiv.org/abs/2603.01661
- PAPER-003 SERENO OSDI 2026 https://www.usenix.org/conference/osdi26/presentation/xin

## 必须写入画面或讲者备注的边界
- 不把HeRo两个消融案例1.52×/3.20×当作全局平均。
- SERENO摘要对前台jank与后台吞吐的研究结果不能写成GPU/NPU某算子的加速，且两篇数据不能相加或相乘。
- 两篇证明系统软件价值，但不是Agent专用硬件调度器已必要。

## Speaker Notes（按本页主题重新撰写，非旧版同页码复制）
1. HeRo: Redmi K80/OnePlus13商用机上的动态Agentic RAG，在线调度利用关键路径、算子形状、资源亲和、共享DRAM争用。仓内两个消融案例5.79→3.82s与17.23→5.38s相互独立，不是‘平均1.52–3.20×’。
2. SERENO: OnePlus13/12等商业手机研究前台应用与后台LLM争用，共享带宽与NPU交通优先级影响前台jank。USENIX官方摘要报告背景LLM使前台综合jank上升153%，在其配置背景吞吐减少约1.01%/1.64%；引述时需明确其基线与实验阶段。
3. 两项机制互补却不同：任务完成时间vs前台交互质量。将其放同一页是Runtime/OS协同责任的研究推断，不是共享硬件架构已实现。

## 画面关系审核
- HeRo和SERENO平行两条因果链，底部汇到Runtime/OS责任，不做论文数字相加。 

## G1/G2 Gate
- G1 内容与证据：G1_PASS_REVISED; 
- G2 新 PNG 是否生成：NOT_STARTED; 旧8张 Image2.5 候选仍处于 REJECTED/HOLD 隔离状态。
- 不得把本文件的 G1 通过解释为原有 PNG 可以交给 Work。
