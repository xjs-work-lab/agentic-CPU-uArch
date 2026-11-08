# Agentic CPU µArch Research Refresh — 2026-11-09

本目录是 2026-11-09 对既有 Agentic CPU µArch 公开证据研究的定向更新。**不修改旧决策快照、不修改任何 PPT/PPTX。**

## 文件
- [Phase 1 仓库质量与当前性审计](repository-quality-audit-2026-11-09.md)
- [PAPER-122 EdgePace 深读卡](PAPER-122-EdgePace-2026-10-27.md)
- [PAPER-123 Tandem 深读卡](PAPER-123-Tandem-2026-10-19.md)

## 当前阶段判断（尚非正式决策）
- C：STRENGTHEN — 新增 OnePlus 13 直接手机证据，支持 deadline/freshness/memory-pressure 联合 Runtime 控制。
- CG-06：STRENGTHEN — CPU counter 反馈、NPU suspension、state reuse 与 power vote 管理使 CPU/LLVM/backend/Runtime 协同更具体；不是新增 ISA 证据。
- B-residual：NARROW — 一些状态复用和活跃功耗管理可由软件实现；跨引擎物理状态残差仍未证实。
- A：KEEP CONDITIONAL — 新软件状态可提供丰富进度信息，但没有匹配可观察性对照来证明私有 RequiredProgress 的独立信息价值。
- PT-A：NO DIRECT CHANGE — 本轮两篇论文不直接测权限、目标绑定、外部真实效果核验和恢复。
- R2：NO DIRECT CHANGE — 没有新增手机 CPU continuation microstate/cache locality 证据。

下一步：完成 EdgePace/Tandem 全部图表与消融核验；补齐 2026-10-09 后官方 Android/Arm/LLVM/Qualcomm/MediaTek/Apple/Samsung 资料；做独立工作与反证搜索；再形成方向影响矩阵。不能把本页的初步判断当成正式 portfolio 决策。
