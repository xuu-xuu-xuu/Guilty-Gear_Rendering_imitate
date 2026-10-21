Unity 风格化角色渲染教程：GitHub GPT 资料包
采集日期：2026-10-21（北京时间）

这是教程写作输入，不是教程成稿，也不是可直接运行的 Unity 工程。
当前只完成只读检查、资料整理和章节规划；没有创建仓库、上传 GitHub 或修改 Unity 工程。

建议阅读顺序：
1. notes/01_inventory.txt —— 收录资料与用途。
2. notes/02_chapter_outline.txt —— 拟定章节、源码、配图与验收点。
3. notes/03_texture_channels.txt —— 当前 Shader 对通道的解释及导入设置。
4. notes/04_actual_parameters.txt —— 参数快照与覆盖关系。
5. notes/05_portability_and_gaps.txt —— 待补资料及不能直接移植的部分。
6. notes/06_gpt_handoff.txt —— 可直接交给 GitHub GPT 的写作要求。
index.html 提供离线导航和真实效果图预览。

证据边界：
- sources 和 data 的参数、导入设置、场景配置来自本次磁盘只读读取。
- 运行时覆盖规则来自源码分析，不是本次启动 Play 后抓取的数据。
- images 和 evidence 中播放记录为 2026-10-20 已有验证产物，明确区分原工程和独立演示副本。
- 428 个 Assets/Packages/ProjectSettings 文件与原教程采集快照一致。
- 本次未连接 Unity MCP、未进入 Play、未重新验证动画或 900cs；未核实编辑器未保存的内存状态。

不含模型、贴图像素（包括自制 UV 遮罩）、动画、骨骼数据、Bind Pose、控制器、Unity 场景/Prefab、AssetBundle、PAK、音乐或视频。
图片仅为已生成的角色渲染截图，不包含参考视频截图或原始贴图。
保留贴图文件名、尺寸、导入参数及哈希作为接口说明；它们不是贴图文件。
没有为项目源码或第三方角色形象自动授予许可证；源码保留原文和来源，公开仓库许可需另外确定。
