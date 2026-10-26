# S09｜讲者备注：动态工作流调度与前台 QoE 是两个互补系统问题

**本页观点。** HeRo 与 SERENO 解决不同系统目标，因而不能把两项实验结果拼成一条加速率。它们共同表明端侧 Runtime/OS 需要同时理解任务依赖和共享资源约束。

**左侧 HeRo（PAPER-098）**：针对商业手机上的 Agentic RAG 多阶段任务，在线阶段 DAG 只有部分未来节点可知，因此调度要考虑关键路径、并行性、CPU/GPU/NPU 亲和、算子形状与共享 DRAM。原论文 Redmi K80/OnePlus 13 的消融示例 5.79→3.82s 与 17.23→5.38s 是两个不同案例，不能当做平均提速1.52–3.20×。本页流程图为解释性抽象，不是原论文逐节点复刻。

**右侧 SERENO（PAPER-003，USENIX OSDI 2026）**：在 OnePlus 商用手机研究后台 LLM 与前台交互应用对共享内存带宽的争用，重点在前台 jank/QoE 与后台推理吞吐之间的取舍。指定配置中的 Prefill / Decode 吞吐变化约 1.01% / 1.64%，不能解读为 Agent E2E 性能提升，也不能当成 HeRo 的测试结果。

**来源与不能推出什么。** HeRo https://arxiv.org/abs/2603.01661；SERENO https://www.usenix.org/conference/osdi26/presentation/xin。结合二者得出的 Runtime/OS 协同责任是跨来源的系统推断，不是公开证据已证明专用硬件调度器必要。
