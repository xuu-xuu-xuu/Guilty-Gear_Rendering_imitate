# 连接现有渲染输入

Shader可以阅读和逐层练习，但三个C#渲染组件还依赖现有呈现类型。代码未包含完整场景、模型和UEOriginalActionPlayer/UEOriginalPersistentPresentation，不能把文件直接拖进空工程就开始调参。先让现有角色系统提供以下输入；适配层只负责渲染引用和参数，不改动画或网格。

## 需要连接什么

| 接入位置 | 类型或字段 | 应提供的现有对象 |
|---|---|---|
| 主体材质 | Renderer / submesh | 保留头体与辅助材质槽的角色Renderer |
| GGSTRegionalShading | body / standingHead等 | 身体与站立头SkinnedMeshRenderer，逐个写head标志 |
| GGSTRegionalShading | 只读头Transform / 矩阵 | 头原点、横轴、宽度；缺失时不能伪造有效位 |
| BridgetImitateProfile | character / additional / root | 显式连接Renderer，计算原点和启用时高度 |
| GGSTGeometryShadowMaps | p / nativeRendering | 当前实际Renderer和可见状态的提供方 |
| GGSTGeometryShadowMaps | 只读头/骨盆坐标 | 为深度图提供正确中心，不改变Transform |
| GGSTGeometryShadowMaps | mainCamera / lightSource | 同场景活动主相机与Directional Light |
| GGSTGeometryShadowMaps | hairMask | 与角色UV匹配、线性采样的头发类别R通道 |
| GGSTGeometryShadowMaps | depthShader | 支持RFloat设备上的GGSTGeometryDepth |
| 主体/接收面Shader | 全局深度RT、VP、origin/range、forward、texel、enable | 成组发布；输入无效则禁用该自定义路径 |

## 组件在哪里读取引用

- [Regional:44–54](code/GGSTRegionalShading.cs.md#l44)通过GetComponent取得已有呈现组件，并从groups的头节点解析frame。你自己的适配层需要提供等价的只读坐标；缺坐标时frameValid保持0。
- [GeometryShadowMaps:82–112](code/GGSTGeometryShadowMaps.cs.md#l82)解析Player、骨盆、同场景Camera/Light，depthShader可回退Shader.Find。Ready还检查nativeRendering、mask、shader和RFloat支持。
- [159–168](code/GGSTGeometryShadowMaps.cs.md#l159)优先读取头MPB的有效原点，否则回退骨盆+0.6米或Player+1.5米。若投影中心不对，先检查输入，不把回退值当准确头坐标。
- [255–269](code/GGSTGeometryShadowMaps.cs.md#l255)只画GGST/BridgetToonStudy的submesh，并传入材质的镜像与_MainTex_ST。
- [Profile:25–26](code/BridgetImitateProfile.cs.md#l25)在character空时按bgt_body.001查找，rootBone空时使用Renderer.transform；自己的场景应显式连接，避免误选。

Visible不只看Renderer.enabled，还要求activeInHierarchy、非forceRenderingOff、有sharedMesh且属于正确场景。深度路径没有draw时，先排查这些条件。

## 接好以后怎么确认

先用Debug22/25确认区域和类别，再看16/13/12的着色分量，最后回0看外轮廓。逐Renderer与全局参数的区分见[参数层级](overrides.md)，投影步骤见[接入投影](../chapters/08.md)。

缺少上述原有类型时，需要先完成自己的渲染接口适配；仓库中的采集工具也依赖完整工程，不能作为通用适配器复制使用。环境包清单不表示必须安装MCP、Timeline等与着色无关的工具。
