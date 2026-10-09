# 07-validation — 历史验证设计与局限记录（非当前实验指令）

**当前：2026-10-09 公开资料研究已结题；没有授权，也不允许在本轮研究中自行进行实验、仿真、设备trace或PoC。**

此目录保留从历史V1迁移的 Experiment/Validation 文档及其中的假设、基线、可能的验证条件、历史论证和失败边界。它们是**历史可追溯研究对象**，不是当前研究“待运行清单”。过去写的 `simulations/results` 等历史文字不能升级成新实验授权。

现存主要子目录：

- [A/](A/)：Agent-private RequiredProgress 条件研究的历史验证论证；
- [B-residual/](B-residual/)：跨引擎派生状态/物理有效性研究问题；
- [R1/](R1/) 与 [R2/](R2/)：post-ready release timing 和 CPU continuation locality 历史假设；
- [CG-06/](CG-06/) 与 [CG-07/](CG-07/)：CPU快路径和低功耗主动Agent历史验证思路；
- [C/](C/)、[PT-A/](PT-A/)、[CG-01/](CG-01/)、[R3/](R3/)：异构调度、可信工具、通用缓存、语义ISA相关历史设计。

应先阅读[现行技术组合](../09-roadmap/current.md)以及[正式结题及证据限制](../00-project/final-research-archive-acceptance-2026-10-09.md)，不能从这些文档中直接恢复已经停用的2027“实验计划”。

关于研究方法，可根据未来**新的公开发表材料**重开限定问题；该动作不同于执行这里的旧实验。
