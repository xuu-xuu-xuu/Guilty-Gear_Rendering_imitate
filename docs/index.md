# Unity 罪恶装备风格角色渲染复刻

从基础明暗到材质高光与线条。本文解释当前 Unity 项目已经实现的风格化方案：为什么需要这些处理、在独立练习项目如何操作、用什么证据判断是否正确。

[![原工程历史最终渲染](assets/images/project/final.png)](assets/images/project/final.png)

原工程2026-10-20历史最终验收图，非Debug，含角色投影；来源 `thigh_highlight_20261020/verified_play_2.png`。它是历史展示，不能与独立副本作单变量比较。[本轮新Unity静态实验](reference/experiments-20261021.md)单独收录，不将历史图冒充新图；后续[站立验收](reference/standing-stability-20261021.md)已真实进入Play，结论独立列出。完整来源见[图片索引](reference/images.md)。

## 从哪里开始

默认你会用Unity材质与贴图，已有能正常播放站立动画的模型。先建立输入和观察基准，再按视觉问题学习各效果。源码快照不是独立可运行工程；模型、原始/自制纹理、动画、场景和桥接组件未提供。无需下载或补入原游戏资源。

| 路线 | 章节 | 你应能回答的问题 |
|---|---|---|
| 建立基准 | [00 范围](chapters/00.md)、[01 环境](chapters/01.md)、[02 输入](chapters/02.md)、[03 材质覆盖](chapters/03.md) | 图从哪里来？实际数值来自哪一层？ |
| 理解计算 | [04 执行顺序](chapters/04.md)、[05 两段式](chapters/05.md)、[06 分区明暗](chapters/06.md)、[07 配色](chapters/07.md) | 为什么旧明暗结果会被重建？ |
| 组织质感 | [08 阴影路径](chapters/08.md)、[09 材质高光](chapters/09.md)、[10 大腿高光](chapters/10.md) | 如何控制范围、形状与颜色？ |
| 完成表现 | [11 线条](chapters/11.md)、[12 眼睛](chapters/12.md)、[13 边缘光](chapters/13.md) | 为什么某些细节必须晚于光照合成？ |
| 检查结果 | [14 站立验收与排错](chapters/14.md) | 怎样区分输入、覆盖和时序问题？ |

教程顺序不等于Shader执行顺序。[04](chapters/04.md)单独列出FORWARD内的真实计算顺序与独立Pass调度。

## 如何核查

先看[章节—源码—参数—效果图—验证证据表](reference/evidence-map.md)。每章给出来源行号、连续原文摘录、默认值/四主体材质保存值与独立练习步骤。参数、Debug、通道、导入及依赖都有完整附录。

源码决定当前计算，data决定保存起点和覆盖规则，images_manifest决定图片用途；历史报告只说明原来的验证范围。本教程没有将历史结果写成本次新验证，也没有为凑齐截图改写源码或原资源。

## 完成状态与边界

00–14章正文完整；[新实测附录](reference/experiments-20261021.md)已补墙/地接收单属性投影A/B、最终眼睛开关近景、重复帧及恢复证据，采集器和原Shader已在完整工程隔离副本编译/渲染。[站立循环新增验收](reference/standing-stability-20261021.md)已覆盖三个受控周期和122条正常Play帧；网格TANGENT语义、通用适配、新模型/UV与跨环境时序仍待补，见[证据表](reference/evidence.md)。不宣称原游戏内部算法还原。

站点已于2026-10-21通过GitHub Pages发布，PR #1已合并。本站使用项目子路径，正文与仓库Markdown共用。发布记录、检查范围与后续部署方法见[构建与Pages](reference/deployment.md)。

## 附录入口

- [参数账本](reference/parameters.md) · [属性声明](reference/property-declarations.md) · [运行覆盖](reference/overrides.md)
- [通道与模型契约](reference/channels.md) · [导入及绑定](reference/texture-imports.md) · [Debug](reference/debug.md)
- [依赖与可复刻性](reference/dependencies.md) · [图片来源](reference/images.md) · [许可说明](reference/credits.md)

所有公式使用普通文本/代码表示，GitHub与网页共用同一Markdown；图片可点击查看原尺寸。没有自动播放媒体或动画。
