# Shader 属性声明

从 shader_properties.csv 转录；保留原列名与声明行号。

| shader | property | label | type | default | line |
|---|---|---|---|---|---|
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ThighLobeEnabled | 大腿局部收尖高光 | Range(0,1) | 0.0 | 6 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ThighLobeStrength | 大腿独立亮块强度 | Range(0,0.4) | 0.16 | 7 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ThighLobeTint | 大腿浅金色高光 | Color | [0.92, 1.0, 0.45, 1.0] | 8 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedShadeEnabled | 腹部与腿部阴面收窄 | Range(0,1) | 0.0 | 12 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedSpecEnabled | 整理后独立材质高光 | Range(0,1) | 0.0 | 13 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedTunicThreshold | 腹部明暗阈值 | Range(0.2,0.7) | 0.4 | 14 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedThighThreshold | 大腿明暗阈值 | Range(0.3,0.8) | 0.57 | 15 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedCalfThreshold | 小腿明暗阈值 | Range(0.3,0.8) | 0.59 | 16 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedKneeThreshold | 膝部明暗阈值 | Range(0.3,0.8) | 0.62 | 17 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedSkinStrength | 皮肤浅暖亮块强度 | Range(0,0.4) | 0.14 | 18 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedSkinWidth | 皮肤亮块宽度 | Range(0.02,0.4) | 0.22 | 19 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedHairGain | 发丝亮带倍率 | Range(0,2) | 1.25 | 20 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedClothGain | 布料柔光倍率 | Range(0,2) | 1.2 | 21 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FocusedMetalGain | 金属亮芯倍率 | Range(0,2) | 1.05 | 22 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CleanShadeEnabled | 角色简洁漫反射明暗 | Range(0,1) | 0.0 | 26 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CleanClothMaskWeight | 衣料明暗遮罩参与 | Range(0,1) | 0.4 | 27 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CleanClothAOWeight | 衣料顶点暗部参与 | Range(0,1) | 0.25 | 28 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CleanClothSoftness | 衣料色块边界宽度 | Range(0.005,0.06) | 0.018 | 29 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CleanFaceUnderStart | 下颌暗面起点 | Range(-1,0) | -0.7 | 30 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CleanFaceUnderEnd | 下颌亮面起点 | Range(-1,0.2) | -0.45 | 31 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _PaletteEnabled | 皮肤与浅色衣料漫反射配色 | Range(0,1) | 0.0 | 35 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _PaletteSkinLight | 皮肤亮面乘色 | Vector | [0.92, 1.1, 1.28, 0.0] | 36 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _PaletteSkinDark | 皮肤暖阴面乘色 | Vector | [0.82, 0.7, 0.82, 0.0] | 37 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _PaletteSleeveLight | 白袖亮面乘色 | Vector | [0.99, 1.0, 1.07, 0.0] | 38 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _PaletteSleeveDark | 白袖冷灰阴面乘色 | Vector | [0.9, 0.93, 1.02, 0.0] | 39 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _PaletteTunicLight | 胸前衣料亮面乘色 | Vector | [1.0, 1.08, 1.23, 0.0] | 40 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _PaletteTunicDark | 胸前衣料阴面乘色 | Vector | [1.03, 1.06, 1.19, 0.0] | 41 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimEnabled | 参考风格边缘光启用 | Range(0,1) | 0.0 | 45 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimWidth | 参考边缘光宽度 | Range(0.02,0.4) | 0.19 | 46 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimStrength | 参考边缘光强度 | Range(0,1) | 0.38 | 47 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimShadowFloor | 暗面边缘光保留 | Range(0,1) | 0.45 | 48 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimTint | 参考边缘光浅色 | Color | [0.94, 0.97, 1.0, 1.0] | 49 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimTintMix | 边缘光浅色混合 | Range(0,1) | 0.65 | 50 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimMaterial | 边缘光 发/布/肤/金属 | Vector | [1.0, 0.9, 0.65, 0.6] | 51 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReferenceRimFaceScale | 脸部边缘光比例 | Range(0,1) | 0.15 | 52 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceDiffuseRefine | 脸部漫反射造型启用 | Range(0,1) | 0.0 | 56 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceDiffuseBoundary | 侧脸暗面边界 | Range(0.25,0.85) | 0.54 | 57 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceDiffuseEdge | 侧脸边界过渡 | Range(0.015,0.12) | 0.045 | 58 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceDiffuseSide | 侧脸阴面覆盖 | Range(0,1) | 0.9 | 59 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceDiffuseDepth | 脸部原Sss暗色混合 | Range(0,1) | 0.9 | 60 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceDiffuseTint | 脸部漫反射暖暗乘色 | Color | [1.0, 0.84, 0.84, 1.0] | 61 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _EyeRefineEnabled | 眼睛分区层次启用 | Range(0,1) | 0.0 | 65 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _EyeIrisUpperDepth | 虹膜上层深色 | Range(0,0.5) | 0.18 | 66 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _EyeIrisLowerLift | 虹膜下层透亮 | Range(0,0.4) | 0.1 | 67 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _EyeIrisEdgeDepth | 虹膜外缘层次 | Range(0,0.3) | 0.08 | 68 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _EyeCatchlightLift | 原白色高光清晰度 | Range(0,0.5) | 0.25 | 69 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _EyeScleraShade | 眼白克制冷色 | Range(0,0.2) | 0.06 | 70 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairFaceShadowStrength | 真实头发投脸强度 | Range(0,1) | 0.0 | 74 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairFaceShadowBias | 头发阴影深度偏移/米 | Range(0,0.01) | 0.0006 | 75 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairFaceShadowFilter | 头发阴影过滤/贴素 | Range(0,3) | 1.1 | 76 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineRefineEnabled | 材质分区线条启用 | Float | 0.0 | 79 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineContourWidths | 轮廓像素宽度 发/布/肤/金属 | Vector | [0.82, 0.95, 0.6, 0.72] | 80 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineContourTintMix | 轮廓材质色混合 | Range(0,1) | 0.55 | 81 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineInnerStrengths | 内部线强度 发/布/肤/金属 | Vector | [0.72, 0.76, 0.58, 0.72] | 82 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineInnerFilter | 内部线覆盖率过滤 | Range(0,1) | 0.6 | 83 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineInnerTintMix | 内部线材质色混合 | Range(0,1) | 0.45 | 84 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineHairInk | 发线暖棕 | Color | [0.06, 0.032, 0.015, 1.0] | 85 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineClothInk | 布线蓝炭 | Color | [0.023, 0.031, 0.042, 1.0] | 86 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineSkinInk | 肤线暖棕 | Color | [0.1, 0.045, 0.027, 1.0] | 87 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LineMetalInk | 金属线深棕 | Color | [0.04, 0.032, 0.022, 1.0] | 88 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FourMaterialSpecMask | 高光分类 RGBA发/布/肤/金属 | 2D | "black" | 91 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FourMaterialSpecEnabled | 独立材质高光启用 | Range(0,1) | 0.0 | 92 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairShineStrength | 头发亮带强度 | Range(0,0.5) | 0.12 | 93 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairShineWidth | 头发亮带宽度 | Range(0.02,0.3) | 0.1 | 94 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairShineTint | 头发亮带色 | Color | [1.0, 0.94, 0.78, 1.0] | 95 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ClothShineStrength | 布料柔光强度 | Range(0,0.2) | 0.035 | 96 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ClothShinePower | 布料柔光指数 | Range(2,40) | 12.0 | 97 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ClothShineTint | 布料柔光色 | Color | [0.9, 0.95, 1.0, 1.0] | 98 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SkinShineStrength | 皮肤微光强度 | Range(0,0.2) | 0.028 | 99 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SkinShinePower | 皮肤微光指数 | Range(4,80) | 28.0 | 100 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SkinShineTint | 皮肤微光色 | Color | [1.0, 0.82, 0.68, 1.0] | 101 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MetalShineStrength | 金属窄亮芯强度 | Range(0,1) | 0.38 | 102 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MetalShineWidth | 金属亮芯宽度 | Range(0.02,0.3) | 0.1 | 103 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MetalShineTint | 金属亮芯色 | Color | [1.0, 0.97, 0.9, 1.0] | 104 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MainTex | 基础色 | 2D | "white" | 106 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ShadowMap | 原 Sss 颜色图 | 2D | "white" | 107 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LightMap | ilm 数据 | 2D | "white" | 108 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _DetailMap | detail / UV1 | 2D | "white" | 109 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _OutlineMap | olm 轮廓颜色 | 2D | "black" | 110 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RegionalMask | 独立分区 R皮肤 G白袖 | 2D | "black" | 111 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RegionalEnabled | 分区明暗启用 | Float | 0.0 | 112 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RegionalHead | 头部 Renderer 分区 | Float | 0.0 | 113 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceFrameValid | 只读脸部坐标有效 | Float | 0.0 | 114 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceOriginWS | 只读头部原点 | Vector | [0.0, 0.0, 0.0, 0.0] | 115 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceRightWS | 只读头部横向与半宽 | Vector | [1.0, 0.0, 0.0, 0.083] | 116 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceSideStrength | 侧脸受控阴影 | Range(0,1) | 0.85 | 117 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceShadeThreshold | 脸部明暗阈值 | Range(0,1) | 0.8 | 118 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SkinShadeThreshold | 身体皮肤明暗阈值 | Range(0,1) | 0.69 | 119 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SleeveShadeThreshold | 白袖明暗阈值 | Range(0,1) | 0.68 | 120 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RegionalSoftness | 分区边界宽度 | Range(0.001,0.08) | 0.018 | 121 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceShadeStrength | 脸部暖暗色强度 | Range(0,1) | 0.78 | 122 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SkinShadeStrength | 皮肤暖暗色强度 | Range(0,1) | 0.72 | 123 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SleeveShadeStrength | 白袖冷暗色强度 | Range(0,1) | 0.72 | 124 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _FaceShadeTint | 脸部暗面乘色 | Color | [1.0, 0.92, 0.91, 1.0] | 125 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SkinShadeTint | 皮肤暗面乘色 | Color | [0.78, 0.49, 0.47, 1.0] | 126 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SleeveShadeTint | 白袖暗面乘色 | Color | [0.53, 0.62, 0.7, 1.0] | 127 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CullMode | 面剔除 | Float | 2.0 | 129 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _UseMirroredUV | 读取第三套 UV | Float | 0.0 | 130 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _DepthOffsetFactor | 深度偏移因子 | Float | 0.0 | 131 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _DepthOffsetUnits | 深度偏移单位 | Float | 0.0 | 132 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LightTreshold | 明暗分界 | Range(0,1) | 0.5 | 133 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RampOffset | 区域明暗偏移 | Range(-1,1) | 0.0 | 134 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RampMaskCenter | ilm G 中性值（实验参数） | Range(0,1) | 0.4980392 | 135 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RampMaskStrength | ilm G 偏移强度 | Range(0,2) | 1.0 | 136 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ShadowSoftness | 明暗边界宽度 | Range(0,0.1) | 0.008 | 137 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ShadowIntensity | Sss 暗部混合 | Range(0,1) | 0.65 | 138 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ShadowTint | 暗部色调 | Color | [1.0, 1.0, 1.0, 1.0] | 139 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SkinShadowOffset | 低 R 分区明暗偏移 | Range(-0.5,0.5) | 0.06 | 140 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SecondShadowThreshold | 第二暗部阈值 / NdotL | Range(-1,1) | 0.1 | 141 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SecondShadowStrength | 下半身第二暗部强度 | Range(0,1) | 0.0 | 142 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SecondShadowTint | 第二暗部乘色 | Color | [1.0, 1.0, 1.0, 1.0] | 143 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LowerRegionUpper | 下半身区域上界 / 相对身高 | Range(0,1) | 0.52 | 144 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LowerRegionFeather | 区域过渡宽度 | Range(0.01,0.3) | 0.08 | 145 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LowerLightBlend | 下半身独立光向混合 | Range(0,1) | 0.0 | 146 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LowerLightDirection | 下半身独立光向 / 世界空间 | Vector | [0.8, 0.5, 0.2, 0.0] | 147 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LowerLightDynamic | 下半身跟随主光（移动光源 A/B） | Range(0,1) | 0.0 | 148 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LowerSkinColorGate | 用基础色排除低R白色材质（当前配色实验） | Range(0,1) | 1.0 | 149 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _TasteRatePow | 下半身渐变指数（实验） | Range(0.1,4) | 1.0 | 150 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _TasteHeightStart | 渐变高度下界（诊断） | Range(-1,2) | 0.0 | 151 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _TasteHeightEnd | 渐变高度上界（诊断） | Range(-1,2) | 0.65 | 152 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _TasteNormalWeight | 水平法线参与度（诊断） | Range(0,1) | 0.5 | 153 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RegionLightBlend | 部位光向混合（诊断） | Range(0,1) | 0.0 | 154 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RegionLightDirection | 部位候选光向（诊断） | Vector | [0.8, 0.5, 0.2, 0.0] | 155 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CharacterOriginWS | 角色脚下参考原点 | Vector | [0.0, 0.0, 0.0, 0.0] | 156 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _CharacterHeight | 角色参考身高 | Float | 1.65 | 157 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LightIntensity | 主光贡献 | Range(0,2) | 0.9 | 158 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _AmbientStrength | 环境光贡献 | Range(0,1) | 0.2 | 159 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _AOStrength | 顶点 R 明暗控制 | Range(0,1) | 1.0 | 160 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _DetailIntensity | Detail 强度 | Range(0,1) | 0.278 | 161 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _InnerLineStrength | ilm Alpha 内部线条 | Range(0,1) | 0.65 | 162 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _InnerLineColor | 内部线条颜色 | Color | [0.035, 0.028, 0.025, 1.0] | 163 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RimWidth | 边缘光宽度 | Range(0,1) | 0.16 | 164 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _RimIntensity | 边缘光强度 | Range(0,1) | 0.16 | 165 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SpecularPower | 通用高光指数 | Range(1,100) | 24.0 | 166 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _SpecularIntensity | 通用高光强度 | Range(0,2) | 0.12 | 167 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LayerMaskStep | 皮肤分区上界（实验分类） | Range(0,255) | 60.0 | 168 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _BodySpecularWidth | 皮肤高光宽度 | Range(0,1) | 0.18 | 169 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _BodySpecularIntensity | 皮肤高光强度 | Range(0,1) | 0.15 | 170 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HeadSpecularWidth | 头发高光宽度 | Range(0,1) | 0.14 | 171 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HeadSpecularIntensity | 头发高光强度 | Range(0,1) | 0.22 | 172 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairLayerMin | 头发/布料共享分区下界 | Range(0,255) | 65.0 | 173 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _HairLayerMax | 头发/布料共享分区上界 | Range(0,255) | 90.0 | 174 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LeatherLayerMin | 手套/裙子分区下界 | Range(0,255) | 90.0 | 175 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _LeatherLayerMax | 手套/裙子分区上界 | Range(0,255) | 125.0 | 176 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MetalLayerMin | 金属分区下界 | Range(0,255) | 145.0 | 177 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MetalLayerMax | 金属分区上界 | Range(0,255) | 200.0 | 178 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MetallicStepSpecularWidth | 金属高光宽度 | Range(0,1) | 0.2 | 179 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _MetallicStepSpecularIntensity | 金属高光强度 | Range(0,1) | 0.25 | 180 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _ReceiveShadowStrength | 接收投影强度 | Range(0,1) | 0.7 | 181 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _OutlineWidth | 轮廓宽度 / 输出像素 | Range(0,4) | 0.8 | 182 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _UseSmoothOutline | 使用蒙皮平滑描边法线（需专用网格） | Float | 0.0 | 183 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _OutlineSkinScale | 皮肤轮廓宽度比例 | Range(0,1) | 0.35 | 184 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _OutlineColor | 轮廓颜色 | Color | [0.04, 0.03, 0.025, 1.0] | 185 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _OutlineMapStrength | olm 颜色参与 | Range(0,1) | 0.6 | 186 |
| Assets/GGST_Imitate/Shaders/BridgetToon.shader | _DebugMode | 调试输出 0～24（编号见修改文档） | Range(0,24) | 0.0 | 187 |
| Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader | _GeometryShadowFloor | 投影最低可见率 | Range(0,1) | 0.1 | 6 |
| Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader | _GeometryShadowBias | 投影深度偏移/米 | Range(0,0.02) | 0.001 | 7 |
| Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader | _GeometryShadowFilter | 投影边缘过滤/贴素 | Range(0,4) | 0.8 | 8 |
| Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader | _GeometryShadowFade | 离接收面距离衰减 | Range(0,0.5) | 0.08 | 9 |
| Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader | _Color | Backdrop Color | Color | [0.702, 0.702, 0.702, 1.0] | 12 |
| Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader | _GradientStrength | Horizontal Falloff | Range(0, 1) | 0.134 | 14 |
| Assets/GGST_RenderFix/GgstDecal.shader | _MainTex | 原版贴花（线性数据） | 2D | "gray" | 2 |
| Assets/GGST_RenderFix/GgstDecal.shader | _Strength | 贴花强度 | Range(0,1) | 1.0 | 2 |
| Assets/GGST_RenderFix/GgstGlow.shader | _MainTex | 原版发光基础色 | 2D | "white" | 2 |
| Assets/GGST_RenderFix/GgstGlow.shader | _GlowMultiplier | 发光倍率 | Float | 2.0 | 2 |
