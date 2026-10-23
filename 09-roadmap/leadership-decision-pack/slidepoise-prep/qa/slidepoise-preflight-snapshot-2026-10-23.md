# SlidePoise 本地配置核验快照（2026-10-23）

> **读取状态：已从 GitHub 读取本机上传的 doctor.json 与 profile-show.json**；未在本机运行命令、未读取本机 `resolved-config.json`，也未使用真实 PowerPoint 测试 Speaker Notes。  
> **结论：安装依赖基本就绪；激活的 Consulting Profile 与本项目蓝色中文技术学术风冲突；正式正文画布仍未确定。正式 SlidePoise image target 仍阻断。**

## 1. 用户上传的原始结果与出处

- [doctor.json](../../slidepoise-config/doctor.json)，Git blob SHA：`8545b63d080bc56181869bac210968f9e0e090bf`。
- [profile-show.json](../../slidepoise-config/profile-show.json)，Git blob SHA：`21d34bae1dc651e9337edd65792c0576a7fc852c`。
- 技术实现依据：[SlidePoise workflow](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/references/workflow.md)、[canvas.py](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/runtime/src/slidepoise/canvas.py)、[resolve_config.py](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/scripts/resolve_config.py)、[Profile authoring](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/references/profile-authoring.md)。

## 2. 可从上传文件直接确认的事实

| 项目 | 实际读到的值 | 质量判断 |
|---|---|---|
| Python | 3.12.14 | 依赖可见，**未另行测试运行兼容性** |
| Node/npm | Windows 安装路径已检测到 | 可见，版本号未在此次文件中列出 |
| Codex | detected=true | 已配置执行环境 |
| PptxGenJS | true | PowerPoint 重建依赖可见 |
| LibreOffice、Poppler pdftoppm | 两者有工具路径 | 可支持 PPT 预览，**但尚未实测 render** |
| SlidePoise Framework | 已有本地 framework home | 说明安装存在 |
| Profile count | 4 | 已存在四个 Profile |
| **Active Profile** | **consulting** | 与项目蓝色学术技术风不一致 |
| Profile schema | 1.0.0 | 已读 `profile-show.json` |
| Profile 资源 | remix-icon、mdi、wikimedia-identity；consulting-core；consulting-references | 不能把该资源列表直接等同全部已下载或可重绘许可 |
| style_agency | palette/typography/density=specified | 表明这些是**配置约束**，不应只靠出图 prompt 强行覆盖 |
| 配色 | #FD5108、#FE7C39 等橙色 + 黑白 | 冲突：当前研究目标是深/中/浅蓝统一层级 |
| 文字 | 标题 Georgia、正文 Arial；默认文本规则 Arial | 冲突：中文无衬线与科研说明文字优先，Georgia 不适合中文结论标题 |
| hard_rules | orange-led、Georgia/Arial、橙色图表/标注等多层规则 | 只改 `palette` 字段不够；硬规则、text policies、chart tokens、connectors 都可能漂移 |
| 本机 resolved config | **未上传** | 不能从 doctor/profile 文件确定全画布和正文画布尺寸 |
| Speaker Notes | 未看到测试/回读结果 | 不得声明 Notes 可写入 PPTX |
| image generation | “Discovered by Agent from tools…” | 不能据此认定本机已选好生成模型、接口或已完成一次合法出图 |

## 3. 画布信息为什么尚未确定

SlidePoise 官方 `canvas.py` 中：

```text
substantive_width  = design.full_slide_px[0]
substantive_height = design.full_slide_px[1]
                   - (header.enabled ? header.height_px : 0)
                   - (footer.enabled ? footer.height_px : 0)
generation_aspect_ratio = substantive_width / substantive_height
```

`profile-show.json` 的 `design_overrides.frame` **只列字体/颜色和规则等字段，没有有效的 full_slide_px 和 header/footer 高度实测值**。这些来自默认配置叠加 Profile 再叠加 run/session overrides，只有 `resolved-config.json` 是最终依据。

**仅供理解的官方仓库默认配置示例**（`framework/defaults/slidepoise-config.json`，**不是本机实测**）：
- full_slide_px = 2048×1152；
- header.enabled=true、height_px=41；
- footer.enabled=true、height_px=41；
- 如果完全使用这些值，则 substantive region = 2048×1070、宽高比约 1.914；真实 run 可覆盖这些数值。

上述参考值**绝不可作为本项目正式出图尺寸**，除非本地 resolved config 显示一致。

## 4. 下一步最省 token 的实际操作

不需要进入本地 Work 模式。直接在已安装 SlidePoise 的**普通本地终端**解析一个用于本次研究的 presentation/run 配置。

官方 CLI 的命令形态经过 [framework/cli.py](https://github.com/henryhyw/slidepoise/blob/main/framework/cli.py) 核对：

```powershell
# 使用新的临时 run，不覆盖现有演示项目；首次创建
slidepoise run create agentic-cpu-preflight --profile consulting

# 上条命令会输出实际 run 根目录。以该输出路径替换下面的 <RUN_ROOT>。
slidepoise run resolve "<RUN_ROOT>" --output "<RUN_ROOT>\work\resolved-config.json"
```

将 `resolved-config.json` 上传至 GitHub 的 `09-roadmap/leadership-decision-pack/slidepoise-config/`。推荐只保留视觉相关字段或上传前检查是否含本地敏感路径、模型凭据。已有 run 可直接 `slidepoise run resolve`，不需要新建。

**更合理的最终步骤**：先按 [08-profile-adaptation-contract.md](../08-profile-adaptation-contract.md) 创建独立的蓝色 Profile，再创建正式 run 并解析它的配置，避免只为临时 Consulting 生成一个即将被废弃的目标画布快照。可以先复用这个临时结果确认 CLI 环境，但最终须以采用新 Profile 的 `resolved-config.json` 为准。

## 5. Profile 冲突及处理决定

**不要直接修改内置 Consulting Profile。** 它本身的橙色和 serif 风格是其产品硬规则，强行在 page prompt 中要求蓝色会导致图像、重建与跨页规则互相冲突。

建议建立独立的 `academic-cpu-insight` Profile，形成「蓝色同色系 + 中文可读的 Sans + 科研/技术领导叙事 + 可编辑科学图表 + 客观证据界限」，配置细则见 [08-profile-adaptation-contract.md](../08-profile-adaptation-contract.md)。

需要完整审阅并统一修改的字段：
- `design_overrides.frame.header/footer`、`title`、`style`
- `design_overrides.text_reconstruction.text_style_policies`
- `semantic_style_tokens`、`connectors`、`data_visualization`
- `hard_rules` 的 `color_system`、`typography`、`data_visualization` 与主色/图标资产约束
- `style_agency`、`review_questions`、`anti_patterns`

配完之后跑 `profile show academic-cpu-insight` 和正式 `run resolve`，要求无橙色硬约束残留、字体角色无互相冲突。配置更新必须记录当前 revision，不直接覆盖用户现有 Profile。

## 6. 正式图片 gate

| 检查 | 状态 |
|---|---|
| GitHub doctor 原始文件读取 | PASS |
| GitHub profile-show 原始文件读取 | PASS |
| 安装依赖列表可见 | REPORTED_OK（未运行 smoke test） |
| 蓝色科研风 Profile 与实际 runtime 兼容 | **BLOCKED / 尚未创建** |
| full-slide 与 substantive canvas | **BLOCKED / 未取得 resolved config** |
| 4 张 SVG 概念图 | `concept_only`，仍可作为视觉参考 |
| 正式 image-generation 请求 | NOT_STARTED |
| `accepted-slide.png` 与重建 | NOT_STARTED |
| Speaker Notes 写入、回读 | NOT_TESTED |

**结论**：本轮的真正进展是确认安装情况、找出 Profile 的系统性视觉冲突和明确还差什么配置。不能将它写成「图像正式生产就绪」。
