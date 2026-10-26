# S07｜NPU 软件优化正在缩小传统 CPU/GPU 回退工作的范围

> 修订状态：G1_PASS_REVISED｜2026-10-26｜权威内容：02/03/04合同 + current.md + DEC-PORTFOLIO-002/DEC-A-008。此文件为 Image2.5 生成前的**受控投影文案**，没有授予任何旧图 G2 通过资格。

## 投影主标题（逐字）
**NPU 软件优化正在缩小传统 CPU/GPU 回退工作的范围**

## 可见副标题
必须与优化后的异构 NPU 软件栈竞争，不能把未经优化的NPU路径当永久基线。

## 投影框图 / 卡片的受控文案
1. **llm.npu｜优化 NPU Prefill 执行**：Prompt 分块使动态长度映射到静态计算图；INT8 核心 MatMul在NPU；CPU/GPU并行处理 outlier/敏感子图；模型块按后端亲和度放置。
2. **ShadowNPU｜Prefill Attention 异构分解**：NPU 低精估计重要 token / 注意力分布；CPU/GPU 执行重要位置 top-k 和高精度稀疏残差；Decode 全 Attention 并未据此全部搬至 NPU。
3. **两者共同的判断**：NPU 软件持续改进，CPU机会空间被更强基线压缩，但 CPU控制/必要精确残差与fallback 仍重要。
4. **研究关系**：同一/相近研究谱系，不应把两篇视为独立重复验证或相乘收益。

## 来源映射（Notes 与图中短引按实际主题关联）
- PAPER-059 llm.npu https://arxiv.org/abs/2407.05858 (ASPLOS 2025)
- PAPER-057 ShadowNPU https://arxiv.org/abs/2508.16703 (MobiSys 2026)

## 必须写入画面或讲者备注的边界
- 当前投影不显示22.4×/30.7×/3×/7.66×，避免未展示完整实验条件与基线时误比。
- 不能把ShadowNPU称为‘所有 Attention/Decode 均由NPU执行’。
- llm.npu的CPU/GPU outlier执行不可删，ShadowNPU本身是跨NPU和CPU/GPU的分工。

## Speaker Notes（按本页主题重新撰写，非旧版同页码复制）
1. 解释 Prefill NPU 图构建和低精度精度问题是软件/算子图问题，不是单纯CPU/NPU谁更强。
2. llm.npu在真实Snapdragon设备上通过prompt、tensor、block三级改造获得特定基线上的高收益；官方摘要给出平均Prefill 22.4×及平均能耗节省30.7×，但本页不将其与其他研究组合。
3. ShadowNPU进一步让NPU做低精排序估计，CPU/GPU做高精稀疏重要项，主要针对Prefill Attention；Decode仍有CPU/GPU路径。两项研究谱系相关，不能算两次完全独立证明。
4. 这些强软件基线意味着新CPU硬件研究必须证明软件无法吸收的残差，而不只是和朴素NPU做对比。

## 画面关系审核
- 两条并列技术机制链必须标出NPU与CPU/GPU协作分工，不能只画通用资源调度。 

## G1/G2 Gate
- G1 内容与证据：G1_PASS_REVISED; 
- G2 新 PNG 是否生成：NOT_STARTED; 旧8张 Image2.5 候选仍处于 REJECTED/HOLD 隔离状态。
- 不得把本文件的 G1 通过解释为原有 PNG 可以交给 Work。
