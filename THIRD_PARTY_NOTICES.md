# 来源、第三方内容与许可边界

本仓库不自动采用覆盖全部文件的MIT或其他开源许可证。没有LICENSE文件不表示任何人可以任意复制、商用或再分发全部内容。

| 内容 | 来源 | 许可/用途边界 |
|---|---|---|
| rendering-tutorial-source-pack中的9份渲染源码 | 用户提供的2026-10-21资料包，source_index.csv记录原工程路径与哈希 | 原文保留；本次未独立确立全部源码的开源授权 |
| 21张渲染截图及其文档副本 | images_manifest.json白名单，原工程历史验收/独立副本历史渲染 | 包含既有角色形象，仅作技术说明；不因此获得角色/游戏资源再分发许可 |
| 角色/游戏名称 | 《罪恶装备：奋战》及Bridget等现有名称 | 权利归各自权利人；本教程不是官方教程或内部算法公开 |
| 新编教程、核查工具与站点配置 | 本次根据用户要求新增 | 单独的许可方案尚未决定；不将第三方内容纳入擅定统一许可 |
| MkDocs / Material for MkDocs及Python依赖 | 构建时从包索引安装，requirements-docs.txt固定直接依赖 | 依赖保留各自许可；不改写第三方授权，不将主题许可扩大到教程素材 |

没有附入或下载模型、原始纹理、自制遮罩像素、动画、骨骼、Bind Pose、控制器、AssetBundle、PAK、音乐、视频或参考视频帧。图片副本逐字节核对，来源映射在docs/assets/image-provenance.json。

本轮另增14张真实Unity实验图（12张去重原生截图与2张无修饰裁切），来源为合法现有完整工程的隔离副本，登记在evidence/rendering-ab-20261021/images.json。新增Editor采集工具位于examples/capture，不冒充原资料包源码。角色形象和既有源码的上述许可边界同样适用；没有因此授予统一开源许可。

技术栈使用说明参照[ MkDocs配置文档](https://www.mkdocs.org/user-guide/configuration/)、[Material设置文档](https://squidfunk.github.io/mkdocs-material/setup/)与[GitHub Pages自定义工作流文档](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。它们用于站点配置，不作为当前Unity算法的证据。

后续站立验收另增91张原生Unity截图及13张精确眼区裁切，来自相同完整工程隔离副本，来源/姿态/Debug/哈希登记在evidence/standing-render-20261021/images.json。仅公开渲染图和接口/哈希记录，不分发模型、贴图像素或动画。新增采集器位于examples/capture/StandingRenderStabilityCapture.cs，实际执行版本另存证据TXT；既有角色及资源权利边界继续适用，不因此授予整体开源许可证。
