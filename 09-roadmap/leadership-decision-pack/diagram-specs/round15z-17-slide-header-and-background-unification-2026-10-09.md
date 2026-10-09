# Round15Z｜17 页领导汇报：顶部标题栏及背景统一

日期：2026-10-09。**状态：17 页可编辑 PPTX、同源 PDF、17 张高分辨率 PNG 和新旧对比已实际制作，基础 OOXML/PDF/渲染检查通过；待用户审阅与 Windows PowerPoint 终验。**

## 触发原因与设计基准

用户指出上一轮合并版“**每页最上边标题栏的格式和背景也都不一致，你好好检查下，建议向最后四页对齐**”。

实际检查确认：原来正文前 11 页确实混用 1.22–1.77 英寸标题栏、不同蓝底、竖向蓝线高度、芯片图宽度和约 19–25.5pt 标题；正文还有 **5 种页面底色**，且 SME2 与 HeRo 使用旧式右上角白色页码浮框。本轮使用**最后四张正文页 12–15（物理页 14–17）**作为唯一格式基准，而不是凭肉眼调整。

## Round15Z 实际版式变更

- 正文 01–15 采用**统一底色** #F7FBFE；统一页眉 #EAF5FD，x=0, y=0, w=13.333in, h=1.28in。
- 左侧竖向蓝线 #1674D1，统一 x=0.34,y=0.16,w=0.07,h=0.84in；右侧仍是**原始独立芯片图片对象**，统一 x=10.48,y=0,w=2.853,h=1.28in。
- 标题统一字体 Noto Sans CJK SC、**23.5pt、加粗、#0A2B62**；副标题**11.4pt、#506D8D**。正文页码统一 x=12.41,y=1.32。其他正文技术图表、标签、数值、来源链接及讲者备注保持。
- 对正文前 7 页少数主卡片起点在 1.44in 而贴近新页码的情况，做低幅度垂直坐标整理，主卡片起点归一至约1.51in，不改变技术因果节点、箭头语义或原始数据。
- **SME2（正文06）**原特殊 1.77in 高页眉改为统一 1.28in，正文垂直布局适度重排以避免大块空白，图表横向定量条、设备和模型标签保持。其原两行标题合成一个原生文本形状，原英文 Evidence 字段移到统一副标题层。
- **HeRo（正文08）**原单行标题自然换行为双行，移除右上角页码浮框，页码移至统一位置。
- **目录**：统一顶栏底色、插图尺寸与左竖线、深蓝标题、副标题；保留四章介绍卡、范围和“阅读路径”，移除旧页眉边界处多余分隔线。
- **封面是特意保留的独立版式**，不应该和正文一样加页码或限制图像尺寸。

## 强制保证的不变内容及 QA

1. PPTX 完整，LibreOffice 可导出 **17 页 PDF，16:9**；全部 **17 张 1920×1080 PNG** 已重新渲染和制作总览。
2. **原生 PowerPoint 形状和文字保持可编辑**，不是把 PNG 拼回幻灯片。原对象数 1042→1038，差 4 个是旧目录分隔线及 SME2/HeRo 的页码浮框、重复文字形状改造所需的装饰对象清理，不是技术内容删除。
3. 比较上一版逐页可见字符，**忽略空格和换行后，17 页字符集合完全一致**，正文第13页 V2 三个正式方向名保留。
4. **17 页演讲者备注文本逐页完全一致**，包含用户认可的逐来源“已证明/未证明/对应本页/推断与限制”。
5. **34 条 PPT 外部超链接完整不变**；原有独立芯片图片均保留。
6. 全部正文页页眉背景颜色、位置、标题及副标题字号通过同一模板强校验；底色由 5 种归一为 1 种。页码 01/15–15/15 连续，未检出禁用的“投资”。
7. PDF 文本块外缘边界扫描正常，未发现超页内容。预览已人工检查正文01、04、05、06、08及全套联系图；不能把此当作 Windows Office 实机或投影验收。

## 实际交付文件（当前对话运行环境，非 GitHub 二进制仓）

- `/mnt/data/round15z_header_unified/Agentic_CPU_uArch_2027-2029_17slides_unified_headers_editable.pptx`
- `/mnt/data/round15z_header_unified/Agentic_CPU_uArch_2027-2029_17slides_unified_headers_editable.pdf`
- `/mnt/data/round15z_header_unified/Agentic_CPU_uArch_17slides_unified_headers_contact_sheet.png`
- `/mnt/data/round15z_header_unified/Agentic_CPU_uArch_header_before_after.png`
- `/mnt/data/round15z_header_unified/Agentic_CPU_uArch_17slides_unified_headers_PNG.zip`
- `/mnt/data/round15z_header_unified/HEADER_UNIFICATION_QA_2026-10-09.md`
- `/mnt/data/round15z_header_unified/unify_headers.py`、`qa_unified_headers.py`、`qa_unified_headers.json`

此版 **Round15Z 取代 Round15Y 成为当前最新整合候选**。后续如果再按页改动，应从本版出发，确保模板严格继承正文12–15的标题栏规范；不得用旧版中的 SME2/HeRo 非标准页眉回滚。Windows Microsoft PowerPoint 中文字体、备注显示、链接点击和会议室投影可读性仍需用户最后确认。