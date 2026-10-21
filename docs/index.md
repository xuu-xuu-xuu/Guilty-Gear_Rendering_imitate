# Unity 罪恶装备风格角色渲染实操教程

从两段式明暗开始，把脸、皮肤和衣料的明暗整理成大块，再加入材质高光、大腿亮形、眼睛、边缘光和线条。每一步都给出修改位置、关键参数、预期画面和排错方法。

[![完整角色效果，Debug0](assets/images/project/final.png)](assets/images/project/final.png)

图中同时包含主体着色和墙地投影，用来认识最终目标，不与其他构图或画质设置的图片直接做单变量比较。

## 开始前

你需要会使用Unity材质和贴图，已有模型及正常播放的站立动画。配置基准是Unity **2022.3.62f3c1、Built-in、Linear**。源码不包含模型、纹理像素、动画、场景和完整呈现组件；使用自己的模型时，要按[通道与UV契约](reference/channels.md)准备输入，并按[渲染接口](reference/dependencies.md)连接已有Renderer和Transform。

## 按实现顺序学习

| 步骤 | 要做什么 | 从哪里开始 |
|---|---|---|
| 准备 | 固定相机、主光、贴图和材质槽 | [最终效果与准备](chapters/00.md) → [环境](chapters/01.md) → [贴图](chapters/02.md) → [Renderer参数](chapters/03.md) |
| 输入与结构 | 理解Pass，先提供投影所需深度输入 | [执行顺序](chapters/04.md) → [投影](chapters/08.md) |
| 漫反射 | 建立两段式，再分区和配色 | [两段式](chapters/05.md) → [分区明暗](chapters/06.md) → [亮暗配色](chapters/07.md) |
| 局部着色 | 细化眼睛，再区分材质并塑造大腿 | [眼睛](chapters/12.md) → [材质高光](chapters/09.md) → [大腿亮块](chapters/10.md) |
| 合成与线条 | 加边缘光，再整理内部线和外轮廓 | [边缘光](chapters/13.md) → [线条](chapters/11.md) |
| 排查 | 暂停同一姿态定位问题，再观察整个站立循环 | [画面排错](chapters/14.md) |

教程的搭建顺序服务于操作；FORWARD里的逐像素执行顺序与独立Pass调度见[Shader结构](chapters/04.md)。

## 调参时随手查

- [从画面问题找控制项](reference/evidence-map.md)
- [材质参数](reference/parameters.md)与[默认值、MPB和内部覆盖](reference/overrides.md)
- [纹理通道](reference/channels.md)、[导入设置](reference/texture-imports.md)与[Debug选择](reference/debug.md)
- [投影与眼睛的同条件对照](reference/experiments-20261021.md)
- [站立姿态图集与问题定位](reference/standing-stability-20261021.md)

图片可以点击查看原尺寸。先固定姿态和其他参数，再只改一个因素；累计效果示意、诊断分量和独立开关对照的区别见[读图条件](reference/images.md)。
