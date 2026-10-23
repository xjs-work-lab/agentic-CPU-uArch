# 08｜SlidePoise Academic CPU Insight 蓝色中文技术 Profile 适配合同

> 状态：**方案与机器可读配置补丁已存 GitHub；尚未在本地创建/激活/验证**。  
> 资料来源：本地 [doctor.json](../slidepoise-config/doctor.json)、[profile-show.json](../slidepoise-config/profile-show.json)（请注意实际相对路径见下方），[本轮预检快照](qa/slidepoise-preflight-snapshot-2026-10-23.md)。  
> 配置 JSON：[profile-blue/academic-cpu-insight.profile-update.json](profile-blue/academic-cpu-insight.profile-update.json)，它是 **profile update 的字段 payload**，不是完整版带 ID/schema 的 \`profile.json\`，不能直接替换本地已安装 Profile 文件。

## 1. 为什么必须独立 Profile

当前用户安装的 active Profile 为 \`consulting\`，而其 \`style_agency.palette/typography/density = specified\`。它通过多个地方同时指定橙色、Georgia/Arial 字体以及橙色箭头、数据可视化和图标：
- \`design_overrides.style.accent_colors\`
- \`design_overrides.title\` 和 \`text_reconstruction.text_style_policies\`
- \`design_overrides.frame.header/footer\`
- \`semantic_style_tokens\`、\`connectors\` 和 \`data_visualization\`
- \`hard_rules.color_system\`、\`hard_rules.typography\`、\`hard_rules.data_visualization\` 和 \`hard_rules.icons\`

若仅在图片 prompt 强调「使用蓝色科技风」，后续 native PPT 重建仍可能强行应用橙色 Consulting 规则，产生视觉漂移。**不修改或覆盖内置 Consulting**；创建专用 \`academic-cpu-insight\`。

## 2. 蓝色科研风配置原则

| 类别 | 目标 | 机器可读字段 |
|---|---|---|
| 主色 | 深海军蓝 \`#102C55\`、中蓝 \`#2473B6\`、浅蓝 \`#E7F2FD\`，中性白/冷灰配合 | \`style.accent_colors/neutral_colors\`、\`hard_rules.color_system\` |
| 文本 | 优先 \`Microsoft YaHei\` 作中文 UI 和结论主标题（Windows 本机**是否可用未核实**） | \`title\`、\`frame\`、\`text_reconstruction\`、\`hard_rules.typography\` |
| 图形关系 | 箭头和线型表达方向/条件/数据依赖；CPU/SME2 嵌套正确 | \`connectors\`、\`hard_rules.geometry\` |
| 科研数据 | 指定设备/指标/最高或平均值、原始来源，科学图表无捏造数据 | \`data_visualization\`、\`review_questions\` |
| 视觉材料 | SVG/线性通用图标，以 native 结构为主；不携带内置 Consulting 的橙色组件或参考 | \`library_sets\`、\`hard_rules.icons\` |
| 模板职责 | 静态 header/footer 归共享 frame；结论主标题归内容区 PowerPoint 原生标题角色 | \`design_overrides.frame\` + \`work/deck-design.json\` |
| 图像 | 在实际 \`resolved-config.json\` 指示的 substantive canvas 生成，不包含页码、页眉 | \`derived.generation_region_px\` |

自定义 Profile 使用完整的设计字段覆盖和自定义硬规则；样页可临时偏离卡片数量，但**不得偏离上述跨页技术语义**。

## 3. 可执行的本地普通终端步骤

以下命令经过 SlidePoise 官方 \`framework/cli.py\` 的参数接口核对，假设你已经将本 GitHub 仓拉取/同步到本地，并在仓库根目录启动 PowerShell。**不需要 Work 模式、不需要安装或重新 setup**。

\`\`\`powershell
# 仅首次创建；若已存在，不重复创建
slidepoise profile create "Academic CPU Insight" --id academic-cpu-insight --based-on consulting

# 读取 create 后的新 Profile revision；update 要求 expected revision
$profile = slidepoise profile show academic-cpu-insight | ConvertFrom-Json
$patchPath = "09-roadmap/leadership-decision-pack/slidepoise-prep/profile-blue/academic-cpu-insight.profile-update.json"
$patch = Get-Content -Raw -Encoding UTF8 $patchPath
slidepoise profile update academic-cpu-insight --json $patch --expected $profile.revision

# 核验更新后的 Profile
slidepoise profile show academic-cpu-insight
\`\`\`

**兼容性提醒**：PowerShell/Windows 对长 JSON native-command 传参有时会产生转义问题；若 CLI 报 JSON parse/length 错，应采用 Python \`subprocess.run([...,"--json", json.dumps(payload),...])\` 传递单个 JSON 参数，并重新获取 revision，**不要直接替换 \`~/.slidepoise/profiles/consulting/profile.json\`**。若本地某个内置库不接受 \`library_sets.components=[]\`，报告真实 CLI 错误后再定向修复；没有实际执行前不得声称补丁验证成功。

准备一份正式 presentation run（上面的 Profile ID 必须用于本次 run）：

\`\`\`powershell
slidepoise run create agentic-cpu-sample --profile academic-cpu-insight
# 将 create 输出的真实 run 根目录复制到这里（不要猜路径）
slidepoise run resolve "<RUN_ROOT>" --output "<RUN_ROOT>\work\resolved-config.json"
\`\`\`

把不含敏感凭据的 \`resolved-config.json\` 上传到 GitHub 的 \`09-roadmap/leadership-decision-pack/slidepoise-config/\`。若你更希望先确认从现有 Consulting 派生的默认尺寸，也可用旧 run resolve 一次，但 **最终必须以 academic-cpu-insight 正式 run 的结果为准**。

## 4. 别忽略正文画布与标题的所有权

根据官方 [canvas.py](https://github.com/henryhyw/slidepoise/blob/main/slidepoise/runtime/src/slidepoise/canvas.py)：

\`W_content = W_full\`，\`H_content = H_full - H_header(enabled) - H_footer(enabled)\`。

- \`profile show\` 是视觉风格对象，不包含完整运行时所有配置；\`doctor\` 是依赖检查，也不计算正文画布。
- **图像生成须只包含实质正文内容区**，但**结论式主标题可以是实质内容区中的原生文字角色**。如果启用 inherited header，那应只放章节/研究标签等静态共享信息；不把每页动态标题挤进一个全套相同的 header 字段。
- 已存四张 \`1600×900\` 全页蓝色 SVG 含标题/页脚，它们仍为 \`concept_only\`；不会通过拉伸变成 \`accepted-slide.png\`。拿到实际画布后重新布局图中的主标题、图表与边界条。
- 真正的 PPTX 配色要对 \`profile show\` 的渲染规则、\`resolved-config\` 的原生 text/chart/connector style、生成目标图三方审计，不能靠 prompt 自称一致。

## 5. 机器可读 JSON 的验证边界

GitHub 的 \`academic-cpu-insight.profile-update.json\` 是从用户上传的 Consulting Profile 中的**现有受支持字段结构**派生，更新了色彩、字体、卡片、线条、图表与自定义 hard rules，消除了橙色的正向视觉约束。

**已检查**：
- JSON 对象具备 CLI \`apply_profile_values\` 所要求的可替换 top-level 字段；不包含不可修改的 \`profile_id\` 与 \`schema_version\`。
- 所有关键 \`design_overrides\`、\`hard_rules\`、\`review_questions\` 均统一为蓝色研究主题。
- 字体设为 \`Microsoft YaHei\` 是**设计选择**而非本机检测结论。

**未检查/尚待本地验证**：
- Profile 更新命令在用户具体安装版本的 JSON 解析/资源选择校验；
- Microsoft YaHei、候选英文字符与数学符号在 PowerPoint 和 LibreOffice 中的实际字体覆盖；
- 已选资源 \`remix-icon\` 和 \`mdi\` 是否按本地情况全部可检索；
- 实际 header/footer、full_slide_px/substantive canvas 比例；
- Speaker Notes 写入与读回通道。

## 6. 成功后如何升级四张样页

1. 更新 [本轮预检快照](qa/slidepoise-preflight-snapshot-2026-10-23.md) 为真实 Profile+resolved config 结果（或者新增 post-profile 快照，保留本快照）。
2. 把 S03/S05/S08/S15 的概念图分解成**动态标题原生文本 + substantive diagram/table region + inherited header/footer**，根据真实尺寸编译正式生成请求。
3. 图片生成后逐页 Blind Read 与 Source/Fidelity Read，特别审 S05 箭头、S08 CPU/SME/实测数据和 S15 2029 条件方向。
4. 将正式被选图像、签名、候选理由和审计记录入 GitHub，标为 \`reconstruction_ready\`，再进入 Work 用 packaged SlidePoise 重建。

当前阻断未解除，不应为了赶进度把四张现有 SVG 直接当可编辑 PPTX。
