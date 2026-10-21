# 渲染接口与可复刻性

这些源码快照依赖原工程已有对象和未打包类型，**不是独立可运行包**。没有模型、纹理像素、场景/Prefab、UEOriginalActionPlayer或UEOriginalPersistentPresentation。本教程不通过重写动画、网格、骨骼或Bind Pose补齐依赖。

## 所需接口

| 消费方 | 类型/输入 | 当前用途 | 新工程应该如何准备 |
|---|---|---|---|
| 主体Shader | Renderer及正确submesh材质 | Forward/Outline/ShadowCaster | 使用已有角色，不批量替换贴花/发光槽 |
| RegionalShading | body、standingHead等SkinnedMeshRenderer | 分别写head=0/1与enable | 显式引用现有Renderer，保留已有MPB字段 |
| RegionalShading | 现有头Transform/只读矩阵 | 原点、横轴、宽度、有效位 | 只读现有头坐标，不重建Bind Pose |
| Profile | character、additional Renderer、root Transform | 原点、启用时高度与QualitySettings | 显式引用；了解生命周期恢复限制 |
| GeometryShadowMaps | UEOriginalActionPlayer及nativeRendering | 获取当前实际Renderer/可见状态 | 缺原桥接需单独渲染适配层，尚未验证 |
| GeometryShadowMaps | 现有骨盆/头坐标 | 深度图中心与回退 | 显式只读Transform，不改动画 |
| GeometryShadowMaps | 同场景Camera/Directional Light | 投影方向、调度与恢复主相机状态 | 显式引用、确认活动状态，不跨场景误选 |
| GeometryShadowMaps | Texture2D hairMask | 分类图R筛头发caster | 自己准备正确UV/线性R遮罩 |
| GeometryShadowMaps | Shader depthShader | GEOMETRY_DEPTH离屏RFloat | Built-in、设备支持、名称正确 |
| 主体及接收面Shader | 深度RT、矩阵、origin/range/forward/texel/enable | 投脸与Stage独立投影 | 成组发布，失败就禁用，不能只填一个常数 |
| 主体Shader | Base/Sss/ILM/Detail/OLM/区域/分类纹理、顶点合同 | 颜色/信号/域/线条 | 依[02章](../chapters/02.md)与[导入表](texture-imports.md)逐项连接 |

## 真实依赖与回退

[GGSTRegionalShading.cs:44–54](code/GGSTRegionalShading.cs.md#l44)通过GetComponent取得UEOriginalPersistentPresentation，遍历groups和现有头节点名字解析frame。缺组件不会凭空构造头坐标；frameValid为0时旧脸部及投脸门控受影响。该方法还查其他呈现分组，本教程只讲站立分支。

[GGSTGeometryShadowMaps.cs:82–112](code/GGSTGeometryShadowMaps.cs.md#l82)解析Player、presentation、骨盆、同场景主相机/方向光，depthShader回退Shader.Find。Ready检查p.nativeRendering、场景一致性、mask、shader与RFloat支持。Visible要求Renderer.enabled、activeInHierarchy、非forceRenderingOff、有sharedMesh且同场景；不是仅看enabled。

[159–168](code/GGSTGeometryShadowMaps.cs.md#l159)优先读取头Renderer MPB的有效脸原点；失败时退到已有骨盆+0.6米或Player+1.5米。回退值是代码行为，不能当准确头坐标。[255–269](code/GGSTGeometryShadowMaps.cs.md#l255)只绘制Shader名为GGST/BridgetToonStudy的submesh，并复制当前材质镜像开关和_MainTex_ST。

[BridgetImitateProfile.cs:25–26](code/BridgetImitateProfile.cs.md#l25)若character未填，会按名字bgt_body.001查找；rootBone缺失则用Renderer.transform。新工程应显式引用避免误选。additional的MPB还原限制见[覆盖附录](overrides.md)。

## 移植时可做与待做

可以在自己的Built-in场景阅读/练习Shader路径、制作自己的遮罩、显式连接已有Renderer/Transform/Light/Camera。通用适配器只应提供渲染输入和离屏绘制，不重写动画或网格。

本次没有新增examples可执行适配器，也没有Unity编译环境验证。完整通用适配器、MPB生命周期和新工程渲染对照均待补。不能承诺“复制三个脚本即可运行”。环境JSON里的包清单是原工程记录，不代表练习要安装所有MCP、Timeline等包。
