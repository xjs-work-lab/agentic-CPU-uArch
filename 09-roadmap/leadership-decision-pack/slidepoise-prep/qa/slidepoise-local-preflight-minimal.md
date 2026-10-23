# SlidePoise 本地一次性最小预检（尽量不消耗 Work token）

> 2026-10-23｜本文件是后续画布和 native PowerPoint 重建的输入采集清单，**不代表当前本地已执行检查**。  
> 目标：让聊天窗口先把图像设计所需的真实画布/字体/框架设置锁定，避免拿整页 16:9 PNG 错误地重建到 SlidePoise 实质内容区。

## 1. 不进入 Work 模式也能执行的命令

在你已经安装 SlidePoise 的本地终端执行。CLI 已在 PATH 时：

```powershell
slidepoise doctor
slidepoise profile show
```

如果已从仓库安装但本地 PATH 未注册，优先用实际安装目录的程序或官方文档中的 npx doctor 命令，不需要重新 setup。不要为了出示检查结果而重装软件。

**尚不能由上两条命令直接判断正文画布时：** 可让本地 CLI 建立一个仅用于预检的空 run，再执行对应的 `slidepoise run resolve <run-path>`，只导出实际解析配置。不需要运行图像生成或 PowerPoint 重建，不用在 Work 中完整制作一页。

## 2. 请保留/回传以下非敏感配置（其他信息可删）

```yaml
slidepoise:
  cli_version_or_commit: TO_BE_CAPTURED
  doctor_summary: TO_BE_CAPTURED
  active_profile_id: TO_BE_CAPTURED
  profile_reference_libraries: TO_BE_CAPTURED
  slide_width_height: TO_BE_CAPTURED
  inherited_header_enabled_and_height: TO_BE_CAPTURED
  inherited_footer_enabled_and_height: TO_BE_CAPTURED
  substantive_content_width_height_or_ratio: TO_BE_CAPTURED
  dynamic_title_and_footer_ownership: TO_BE_CAPTURED
  available_zh_and_latin_fonts: TO_BE_CAPTURED
  image_provider_or_manual_mode: TO_BE_CAPTURED
  local_preview_libreoffice_poppler: TO_BE_CAPTURED
  power_point_speaker_notes_writing: UNVERIFIED_REQUIRES_ONE_PAGE_TEST
```

**无需上传**登录密钥、模型 API token、私人路径、账号凭据或具体设备序列号。可以只分享影响画布/字体/能力的字段。

## 3. 我们为何需要这些

1. **真实正文画布**：SlidePoise 的 image-generation 区域通常须扣除启用的 inherited header/footer；完整幻灯片 16:9 不等于生成内容图也应 16:9。
2. **Profile**：确定蓝色学术型风格与图标/参考素材已选，防止聊天阶段和本地阶段各用不同风格。
3. **图像输入方式**：以后由聊天窗口生成候选并归档 GitHub；本地是否支持直接用已选图作为 accepted target，仍需符合安装版本的 packaged workflow。
4. **Speaker Notes**：只是底层 PowerPoint 工具支持，不等于当前 SlidePoise 的 packaged renderer 已自动实现。需用一页 PPTX 写入、打开并读回验证后再声称支持。

## 4. 与图片阶段的状态对应

| 状态 | 能做什么 | 不得声称什么 |
|---|---|---|
| 未获得上述配置 | 在聊天窗口完成文字合同、版式参考和 concept_only 草图 | 不能声称正式 accepted-slide 的画布已合规 |
| 配置已核对，尚未走真实 SlidePoise 生成请求 | 可以明确生成目标尺寸，制作视觉候选，审箭头/数据 | 不能声称已执行 packaged generation/reconstruction |
| 图片与 manifest 均审核，且 runtime 接受 | 才能在 Work 中走 semantic-map → OpenCV → native scene → 实际 render | 不能把图片审核当 PPTX 编辑/备注/渲染验收 |

## 5. 退出准则

- [ ] 精确记录 SlidePoise Profile ID、正文 canvas 尺寸/比例、页眉页脚配置。
- [ ] 明确标题归属：PowerPoint 框架/原生标题 vs 图像正文占位，不能重复。
- [ ] 确认字体与 LibreOffice/Poppler 状态。
- [ ] 记录 Speaker Notes 仍待一页实际验证或已完成的**真实证据**，而不是猜测。

完成该最小预检后，将审核信息归档到同目录新的 `slidepoise-preflight-snapshot-*.md`；下一轮就可以生成 S03/S05/S08/S15 四页正式比例的高质量可审计候选图。
