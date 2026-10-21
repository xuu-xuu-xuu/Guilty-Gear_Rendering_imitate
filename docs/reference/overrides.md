# 参数层级与最终覆盖

材质面板上的值不是全部输入。调参没有反应时，先判断该字段从哪里来，再找最后使用它的分支。

| 来源 | 例子 | 应该怎样操作 |
|---|---|---|
| Shader Properties默认值 | _ReferenceRimWidth=0.19 | 只决定新材质起点，不能代替示例配置 |
| 材质设置 | 同属性为0.24 | 按对应材质填写，Color和Vector分开解释 |
| Renderer MPB | _RegionalEnabled、_RegionalHead | 共享材质的头/体分别写入；先Get再Set，保留其他字段 |
| Shader全局 | _HairShadowDepth/VP/OriginRange/Forward/Texel/Enabled，Stage同类 | 由深度渲染成组发布，不能只开enable |
| 动态坐标 | _FaceOriginWS/_FaceRightWS、_CharacterOriginWS/_CharacterHeight | 从已有头部/root及启用时bounds读取，不能固定在世界原点 |
| Shader内部替换 | CleanShade、Focused、ThighLobe、ReferenceRim | 修改最终路径的参数，基础结果可能已被覆盖 |

## MPB怎么接

1. 为每个目标Renderer保留已有材质槽。
2. 写自己的字段前调用GetPropertyBlock，写完调用SetPropertyBlock，不要用空MPB清掉其他组件的数据。
3. Regional的strength=1时，_RegionalEnabled被写为1；body的head=0，standingHead的head=1。材质保存的0不能用来判断运行分区关闭。
4. 从已有头Transform获得原点、横轴和宽度；有效时才写_FaceFrameValid=1。MPB没有覆盖某字段时使用材质值，GetFloat对缺失字段返回0不等于实际着色输入为0。

[GGSTRegionalShading.cs:23–66](code/GGSTRegionalShading.cs.md#l23)给出了读坐标和写字段的位置。横轴宽度为max(axis.magnitude×0.083084,0.001)。[Profile:25–42](code/BridgetImitateProfile.cs.md#l25)在启用时计算bounds高度和相对root的底部偏移，之后更新原点；height不是每帧变化的动画高度。

Profile禁用时恢复主character的整块旧MPB，additional没有逐个备份；Regional只恢复自己的字段。组件开关后数据消失时，先检查多写入者的覆盖顺序。

## 调哪个分支

| 效果 | 最后主要控制位置 | 避免误判 |
|---|---|---|
| 脸/皮肤/衣料漫反射 | CleanShade 479–501，FocusedShade 507–518 | 基础侧脸/投脸的中间贡献不一定保留 |
| 亮暗配色 | Palette 461–476，CleanShade内重新纳入 | 不改albedo/spec/rim/ink，不额外乘两遍 |
| 分类高光 | FourMaterial 548–567，FocusedSpec 572–609 | 26–29只看基础分类，最终看13 |
| 大腿亮块 | 583–603先替换focusedSkinShine，再经605–609合并 | 还依赖分类皮肤、head、UV域和FocusedSpec |
| 分类边缘光 | ReferenceRim 616–623 | _RimWidth主要是未分类后备，分类区调_ReferenceRimWidth |
| 内线与原眼睛白点 | 630–657 | 先内线覆盖，再恢复原白点；不生成运动点 |

完整控制流见[Shader执行顺序](../chapters/04.md)。_LowerLightDynamic=1时下半身光向混回主光；Taste/RegionalLight诊断变量未接入最终颜色。保留这些判断有助于解释“基础参数变了，最终画面却没变”。
