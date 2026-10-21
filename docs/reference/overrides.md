# 参数层级与最终覆盖

同名属性必须连同来源和最后写入位置一起阅读。完整[保存账本](parameters.md)逐列列出类型、Shader默认、保存值和字段是否存在；不是当前Play内存转储。

| 层级 | 例子 | 证据与注意事项 |
|---|---|---|
| Shader Properties默认 | _ReferenceRimWidth=0.19 | 声明不是现有材质最终值；[属性索引](property-declarations.md) |
| .mat保存 | 同属性=0.24 | material_parameters.csv；Color和Vector分开解释 |
| Renderer MPB | _RegionalEnabled=Clamp01(strength) | strength保存1，材质保存0；源码规则推断，非本次采样 |
| Shader全局 | _HairShadowDepth/VP/OriginRange/Forward/Texel/Enabled，Stage同类 | CommandBuffer按Ready/可见性/draw开关发布；不写成固定材质数值 |
| 姿态动态/启用时数据 | _FaceOriginWS/_FaceRightWS、_CharacterOriginWS/_CharacterHeight | 现有只读矩阵、root与初始化bounds；没有任意帧数值 |
| 内部替换 | CleanShade/Focused/ThighLobe/ReferenceRim | 输入值仍存在，不保证早期结果进入最后颜色 |

## MPB和动态坐标

- [GGSTRegionalShading.cs:23–42](code/GGSTRegionalShading.cs.md#l23)读取现有frame矩阵：头部原点、归一化横轴，宽度=max(axis.magnitude×0.083084,0.001)。有效frame才置 _FaceFrameValid=1，不写骨骼。
- [56–66](code/GGSTRegionalShading.cs.md#l56) GetPropertyBlock后设置enable/head/face字段；body=0、standingHead=1。OnDisable还原已记录的相关字段。
- [BridgetImitateProfile.cs:25–42](code/BridgetImitateProfile.cs.md#l25)启用时记录bounds高度与相对root的底部偏移，随后root位置+偏移写MPB；height不是每帧重新测量的动画高度。
- [GGSTGeometryShadowMaps.cs:273–280](code/GGSTGeometryShadowMaps.cs.md#l273)按CommandBuffer发布深度图/矩阵等；关闭时enable=0。没有纹理不能只写enable=1。

Profile在OnDisable恢复主character的旧整块MPB，不逐一恢复additional；Regional只恢复自己记录的字段。多组件写同一Renderer时，不能假定禁用顺序完全独立，需要在自己的适配层验证。

## 内部覆盖关系

| 分支 | 写入/替换 | 当前如何读参数 |
|---|---|---|
| 旧band/侧脸/投脸 | 基础band、dark、diffuse与早期差值 | Debug10/32/35/36只是对应中间量 |
| Palette | 早期diffuse乘区域向量 | 不改albedo/spec/rim/ink；CleanShade会重新包含Palette |
| CleanShade，479–501 | 覆盖脸、身体皮肤、袖、胸前及其他布料diffuse | cleanCoverage内重建；脸主要按世界n.y下暗面；不写回band |
| FocusedShade，507–518 | 腿/胸前diffuse的差值修正 | 依赖CleanShade覆盖与图集域，不是全图额外一层阴影 |
| FourMaterialSpec，548–567 | 分类内高光 | 未分类保留后备；26–29仅这一层 |
| FocusedSpec，572–609 | 分类高光以新受光带替换，脸皮肤排除 | 13才是最后spec；旧_SpecularPower仍作用于未分类后备 |
| ThighLobe，583–603 | 先替换focusedSkinShine的腿域 | 最终需FocusedSpec及分类皮肤；域外或head门控不满足就不会照搬亮形 |
| ReferenceRim，616–623 | 分类内rim替换 | 主要用_ReferenceRimWidth；旧_RimWidth保留未分类后备 |
| 内线/眼睛白点，630–657 | 完成光照合成后覆盖 | 先墨线，再保留原白点清晰度；不生成运动点 |

完整控制流见[04章](../chapters/04.md)。_LowerLightDynamic=1时lowerLight被混回主光；Taste/RegionalLight诊断变量没有接入最终颜色。旧侧脸、旧高光和旧rim参数有保存值，不代表是最终主要旋钮。

## 运行写入原始数据

[runtime_overrides.csv](https://github.com/xuu-xuu-xuu/Guilty-Gear_Rendering_imitate/blob/f8980fad7a742d76cf8b941843234cd292c7ae82/rendering-tutorial-source-pack/data/runtime_overrides.csv) 与 [runtime_write_sites.csv](https://github.com/xuu-xuu-xuu/Guilty-Gear_Rendering_imitate/blob/f8980fad7a742d76cf8b941843234cd292c7ae82/rendering-tutorial-source-pack/data/runtime_write_sites.csv)提供覆盖规则和写入行。链接固定到原始资料提交，正文源码逐行索引可在站内相对跳转。
