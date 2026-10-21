# 属性名称与类型

按原属性名赋值，区分Float、Range、Vector、Color和纹理。点击行号查看声明；_LightTreshold保留源码拼写。

| Shader | 属性 | 面板名称 | 类型 | 默认值 | 声明 |
|---|---|---|---|---|---|
| BridgetToon.shader | _ThighLobeEnabled | 大腿局部收尖高光 | Range(0,1) | 0.0 | [第6行](code/BridgetToon.shader.md#l6) |
| BridgetToon.shader | _ThighLobeStrength | 大腿独立亮块强度 | Range(0,0.4) | 0.16 | [第7行](code/BridgetToon.shader.md#l7) |
| BridgetToon.shader | _ThighLobeTint | 大腿浅金色高光 | Color | [0.92, 1.0, 0.45, 1.0] | [第8行](code/BridgetToon.shader.md#l8) |
| BridgetToon.shader | _FocusedShadeEnabled | 腹部与腿部阴面收窄 | Range(0,1) | 0.0 | [第12行](code/BridgetToon.shader.md#l12) |
| BridgetToon.shader | _FocusedSpecEnabled | 整理后独立材质高光 | Range(0,1) | 0.0 | [第13行](code/BridgetToon.shader.md#l13) |
| BridgetToon.shader | _FocusedTunicThreshold | 腹部明暗阈值 | Range(0.2,0.7) | 0.4 | [第14行](code/BridgetToon.shader.md#l14) |
| BridgetToon.shader | _FocusedThighThreshold | 大腿明暗阈值 | Range(0.3,0.8) | 0.57 | [第15行](code/BridgetToon.shader.md#l15) |
| BridgetToon.shader | _FocusedCalfThreshold | 小腿明暗阈值 | Range(0.3,0.8) | 0.59 | [第16行](code/BridgetToon.shader.md#l16) |
| BridgetToon.shader | _FocusedKneeThreshold | 膝部明暗阈值 | Range(0.3,0.8) | 0.62 | [第17行](code/BridgetToon.shader.md#l17) |
| BridgetToon.shader | _FocusedSkinStrength | 皮肤浅暖亮块强度 | Range(0,0.4) | 0.14 | [第18行](code/BridgetToon.shader.md#l18) |
| BridgetToon.shader | _FocusedSkinWidth | 皮肤亮块宽度 | Range(0.02,0.4) | 0.22 | [第19行](code/BridgetToon.shader.md#l19) |
| BridgetToon.shader | _FocusedHairGain | 发丝亮带倍率 | Range(0,2) | 1.25 | [第20行](code/BridgetToon.shader.md#l20) |
| BridgetToon.shader | _FocusedClothGain | 布料柔光倍率 | Range(0,2) | 1.2 | [第21行](code/BridgetToon.shader.md#l21) |
| BridgetToon.shader | _FocusedMetalGain | 金属亮芯倍率 | Range(0,2) | 1.05 | [第22行](code/BridgetToon.shader.md#l22) |
| BridgetToon.shader | _CleanShadeEnabled | 角色简洁漫反射明暗 | Range(0,1) | 0.0 | [第26行](code/BridgetToon.shader.md#l26) |
| BridgetToon.shader | _CleanClothMaskWeight | 衣料明暗遮罩参与 | Range(0,1) | 0.4 | [第27行](code/BridgetToon.shader.md#l27) |
| BridgetToon.shader | _CleanClothAOWeight | 衣料顶点暗部参与 | Range(0,1) | 0.25 | [第28行](code/BridgetToon.shader.md#l28) |
| BridgetToon.shader | _CleanClothSoftness | 衣料色块边界宽度 | Range(0.005,0.06) | 0.018 | [第29行](code/BridgetToon.shader.md#l29) |
| BridgetToon.shader | _CleanFaceUnderStart | 下颌暗面起点 | Range(-1,0) | -0.7 | [第30行](code/BridgetToon.shader.md#l30) |
| BridgetToon.shader | _CleanFaceUnderEnd | 下颌亮面起点 | Range(-1,0.2) | -0.45 | [第31行](code/BridgetToon.shader.md#l31) |
| BridgetToon.shader | _PaletteEnabled | 皮肤与浅色衣料漫反射配色 | Range(0,1) | 0.0 | [第35行](code/BridgetToon.shader.md#l35) |
| BridgetToon.shader | _PaletteSkinLight | 皮肤亮面乘色 | Vector | [0.92, 1.1, 1.28, 0.0] | [第36行](code/BridgetToon.shader.md#l36) |
| BridgetToon.shader | _PaletteSkinDark | 皮肤暖阴面乘色 | Vector | [0.82, 0.7, 0.82, 0.0] | [第37行](code/BridgetToon.shader.md#l37) |
| BridgetToon.shader | _PaletteSleeveLight | 白袖亮面乘色 | Vector | [0.99, 1.0, 1.07, 0.0] | [第38行](code/BridgetToon.shader.md#l38) |
| BridgetToon.shader | _PaletteSleeveDark | 白袖冷灰阴面乘色 | Vector | [0.9, 0.93, 1.02, 0.0] | [第39行](code/BridgetToon.shader.md#l39) |
| BridgetToon.shader | _PaletteTunicLight | 胸前衣料亮面乘色 | Vector | [1.0, 1.08, 1.23, 0.0] | [第40行](code/BridgetToon.shader.md#l40) |
| BridgetToon.shader | _PaletteTunicDark | 胸前衣料阴面乘色 | Vector | [1.03, 1.06, 1.19, 0.0] | [第41行](code/BridgetToon.shader.md#l41) |
| BridgetToon.shader | _ReferenceRimEnabled | 参考风格边缘光启用 | Range(0,1) | 0.0 | [第45行](code/BridgetToon.shader.md#l45) |
| BridgetToon.shader | _ReferenceRimWidth | 参考边缘光宽度 | Range(0.02,0.4) | 0.19 | [第46行](code/BridgetToon.shader.md#l46) |
| BridgetToon.shader | _ReferenceRimStrength | 参考边缘光强度 | Range(0,1) | 0.38 | [第47行](code/BridgetToon.shader.md#l47) |
| BridgetToon.shader | _ReferenceRimShadowFloor | 暗面边缘光保留 | Range(0,1) | 0.45 | [第48行](code/BridgetToon.shader.md#l48) |
| BridgetToon.shader | _ReferenceRimTint | 参考边缘光浅色 | Color | [0.94, 0.97, 1.0, 1.0] | [第49行](code/BridgetToon.shader.md#l49) |
| BridgetToon.shader | _ReferenceRimTintMix | 边缘光浅色混合 | Range(0,1) | 0.65 | [第50行](code/BridgetToon.shader.md#l50) |
| BridgetToon.shader | _ReferenceRimMaterial | 边缘光 发/布/肤/金属 | Vector | [1.0, 0.9, 0.65, 0.6] | [第51行](code/BridgetToon.shader.md#l51) |
| BridgetToon.shader | _ReferenceRimFaceScale | 脸部边缘光比例 | Range(0,1) | 0.15 | [第52行](code/BridgetToon.shader.md#l52) |
| BridgetToon.shader | _FaceDiffuseRefine | 脸部漫反射造型启用 | Range(0,1) | 0.0 | [第56行](code/BridgetToon.shader.md#l56) |
| BridgetToon.shader | _FaceDiffuseBoundary | 侧脸暗面边界 | Range(0.25,0.85) | 0.54 | [第57行](code/BridgetToon.shader.md#l57) |
| BridgetToon.shader | _FaceDiffuseEdge | 侧脸边界过渡 | Range(0.015,0.12) | 0.045 | [第58行](code/BridgetToon.shader.md#l58) |
| BridgetToon.shader | _FaceDiffuseSide | 侧脸阴面覆盖 | Range(0,1) | 0.9 | [第59行](code/BridgetToon.shader.md#l59) |
| BridgetToon.shader | _FaceDiffuseDepth | 脸部原Sss暗色混合 | Range(0,1) | 0.9 | [第60行](code/BridgetToon.shader.md#l60) |
| BridgetToon.shader | _FaceDiffuseTint | 脸部漫反射暖暗乘色 | Color | [1.0, 0.84, 0.84, 1.0] | [第61行](code/BridgetToon.shader.md#l61) |
| BridgetToon.shader | _EyeRefineEnabled | 眼睛分区层次启用 | Range(0,1) | 0.0 | [第65行](code/BridgetToon.shader.md#l65) |
| BridgetToon.shader | _EyeIrisUpperDepth | 虹膜上层深色 | Range(0,0.5) | 0.18 | [第66行](code/BridgetToon.shader.md#l66) |
| BridgetToon.shader | _EyeIrisLowerLift | 虹膜下层透亮 | Range(0,0.4) | 0.1 | [第67行](code/BridgetToon.shader.md#l67) |
| BridgetToon.shader | _EyeIrisEdgeDepth | 虹膜外缘层次 | Range(0,0.3) | 0.08 | [第68行](code/BridgetToon.shader.md#l68) |
| BridgetToon.shader | _EyeCatchlightLift | 原白色高光清晰度 | Range(0,0.5) | 0.25 | [第69行](code/BridgetToon.shader.md#l69) |
| BridgetToon.shader | _EyeScleraShade | 眼白克制冷色 | Range(0,0.2) | 0.06 | [第70行](code/BridgetToon.shader.md#l70) |
| BridgetToon.shader | _HairFaceShadowStrength | 真实头发投脸强度 | Range(0,1) | 0.0 | [第74行](code/BridgetToon.shader.md#l74) |
| BridgetToon.shader | _HairFaceShadowBias | 头发阴影深度偏移/米 | Range(0,0.01) | 0.0006 | [第75行](code/BridgetToon.shader.md#l75) |
| BridgetToon.shader | _HairFaceShadowFilter | 头发阴影过滤/贴素 | Range(0,3) | 1.1 | [第76行](code/BridgetToon.shader.md#l76) |
| BridgetToon.shader | _LineRefineEnabled | 材质分区线条启用 | Float | 0.0 | [第79行](code/BridgetToon.shader.md#l79) |
| BridgetToon.shader | _LineContourWidths | 轮廓像素宽度 发/布/肤/金属 | Vector | [0.82, 0.95, 0.6, 0.72] | [第80行](code/BridgetToon.shader.md#l80) |
| BridgetToon.shader | _LineContourTintMix | 轮廓材质色混合 | Range(0,1) | 0.55 | [第81行](code/BridgetToon.shader.md#l81) |
| BridgetToon.shader | _LineInnerStrengths | 内部线强度 发/布/肤/金属 | Vector | [0.72, 0.76, 0.58, 0.72] | [第82行](code/BridgetToon.shader.md#l82) |
| BridgetToon.shader | _LineInnerFilter | 内部线覆盖率过滤 | Range(0,1) | 0.6 | [第83行](code/BridgetToon.shader.md#l83) |
| BridgetToon.shader | _LineInnerTintMix | 内部线材质色混合 | Range(0,1) | 0.45 | [第84行](code/BridgetToon.shader.md#l84) |
| BridgetToon.shader | _LineHairInk | 发线暖棕 | Color | [0.06, 0.032, 0.015, 1.0] | [第85行](code/BridgetToon.shader.md#l85) |
| BridgetToon.shader | _LineClothInk | 布线蓝炭 | Color | [0.023, 0.031, 0.042, 1.0] | [第86行](code/BridgetToon.shader.md#l86) |
| BridgetToon.shader | _LineSkinInk | 肤线暖棕 | Color | [0.1, 0.045, 0.027, 1.0] | [第87行](code/BridgetToon.shader.md#l87) |
| BridgetToon.shader | _LineMetalInk | 金属线深棕 | Color | [0.04, 0.032, 0.022, 1.0] | [第88行](code/BridgetToon.shader.md#l88) |
| BridgetToon.shader | _FourMaterialSpecMask | 高光分类 RGBA发/布/肤/金属 | 2D | black | [第91行](code/BridgetToon.shader.md#l91) |
| BridgetToon.shader | _FourMaterialSpecEnabled | 独立材质高光启用 | Range(0,1) | 0.0 | [第92行](code/BridgetToon.shader.md#l92) |
| BridgetToon.shader | _HairShineStrength | 头发亮带强度 | Range(0,0.5) | 0.12 | [第93行](code/BridgetToon.shader.md#l93) |
| BridgetToon.shader | _HairShineWidth | 头发亮带宽度 | Range(0.02,0.3) | 0.1 | [第94行](code/BridgetToon.shader.md#l94) |
| BridgetToon.shader | _HairShineTint | 头发亮带色 | Color | [1.0, 0.94, 0.78, 1.0] | [第95行](code/BridgetToon.shader.md#l95) |
| BridgetToon.shader | _ClothShineStrength | 布料柔光强度 | Range(0,0.2) | 0.035 | [第96行](code/BridgetToon.shader.md#l96) |
| BridgetToon.shader | _ClothShinePower | 布料柔光指数 | Range(2,40) | 12.0 | [第97行](code/BridgetToon.shader.md#l97) |
| BridgetToon.shader | _ClothShineTint | 布料柔光色 | Color | [0.9, 0.95, 1.0, 1.0] | [第98行](code/BridgetToon.shader.md#l98) |
| BridgetToon.shader | _SkinShineStrength | 皮肤微光强度 | Range(0,0.2) | 0.028 | [第99行](code/BridgetToon.shader.md#l99) |
| BridgetToon.shader | _SkinShinePower | 皮肤微光指数 | Range(4,80) | 28.0 | [第100行](code/BridgetToon.shader.md#l100) |
| BridgetToon.shader | _SkinShineTint | 皮肤微光色 | Color | [1.0, 0.82, 0.68, 1.0] | [第101行](code/BridgetToon.shader.md#l101) |
| BridgetToon.shader | _MetalShineStrength | 金属窄亮芯强度 | Range(0,1) | 0.38 | [第102行](code/BridgetToon.shader.md#l102) |
| BridgetToon.shader | _MetalShineWidth | 金属亮芯宽度 | Range(0.02,0.3) | 0.1 | [第103行](code/BridgetToon.shader.md#l103) |
| BridgetToon.shader | _MetalShineTint | 金属亮芯色 | Color | [1.0, 0.97, 0.9, 1.0] | [第104行](code/BridgetToon.shader.md#l104) |
| BridgetToon.shader | _MainTex | 基础色 | 2D | white | [第106行](code/BridgetToon.shader.md#l106) |
| BridgetToon.shader | _ShadowMap | 原 Sss 颜色图 | 2D | white | [第107行](code/BridgetToon.shader.md#l107) |
| BridgetToon.shader | _LightMap | ilm 数据 | 2D | white | [第108行](code/BridgetToon.shader.md#l108) |
| BridgetToon.shader | _DetailMap | detail / UV1 | 2D | white | [第109行](code/BridgetToon.shader.md#l109) |
| BridgetToon.shader | _OutlineMap | olm 轮廓颜色 | 2D | black | [第110行](code/BridgetToon.shader.md#l110) |
| BridgetToon.shader | _RegionalMask | 独立分区 R皮肤 G白袖 | 2D | black | [第111行](code/BridgetToon.shader.md#l111) |
| BridgetToon.shader | _RegionalEnabled | 分区明暗启用 | Float | 0.0 | [第112行](code/BridgetToon.shader.md#l112) |
| BridgetToon.shader | _RegionalHead | 头部 Renderer 分区 | Float | 0.0 | [第113行](code/BridgetToon.shader.md#l113) |
| BridgetToon.shader | _FaceFrameValid | 只读脸部坐标有效 | Float | 0.0 | [第114行](code/BridgetToon.shader.md#l114) |
| BridgetToon.shader | _FaceOriginWS | 只读头部原点 | Vector | [0.0, 0.0, 0.0, 0.0] | [第115行](code/BridgetToon.shader.md#l115) |
| BridgetToon.shader | _FaceRightWS | 只读头部横向与半宽 | Vector | [1.0, 0.0, 0.0, 0.083] | [第116行](code/BridgetToon.shader.md#l116) |
| BridgetToon.shader | _FaceSideStrength | 侧脸受控阴影 | Range(0,1) | 0.85 | [第117行](code/BridgetToon.shader.md#l117) |
| BridgetToon.shader | _FaceShadeThreshold | 脸部明暗阈值 | Range(0,1) | 0.8 | [第118行](code/BridgetToon.shader.md#l118) |
| BridgetToon.shader | _SkinShadeThreshold | 身体皮肤明暗阈值 | Range(0,1) | 0.69 | [第119行](code/BridgetToon.shader.md#l119) |
| BridgetToon.shader | _SleeveShadeThreshold | 白袖明暗阈值 | Range(0,1) | 0.68 | [第120行](code/BridgetToon.shader.md#l120) |
| BridgetToon.shader | _RegionalSoftness | 分区边界宽度 | Range(0.001,0.08) | 0.018 | [第121行](code/BridgetToon.shader.md#l121) |
| BridgetToon.shader | _FaceShadeStrength | 脸部暖暗色强度 | Range(0,1) | 0.78 | [第122行](code/BridgetToon.shader.md#l122) |
| BridgetToon.shader | _SkinShadeStrength | 皮肤暖暗色强度 | Range(0,1) | 0.72 | [第123行](code/BridgetToon.shader.md#l123) |
| BridgetToon.shader | _SleeveShadeStrength | 白袖冷暗色强度 | Range(0,1) | 0.72 | [第124行](code/BridgetToon.shader.md#l124) |
| BridgetToon.shader | _FaceShadeTint | 脸部暗面乘色 | Color | [1.0, 0.92, 0.91, 1.0] | [第125行](code/BridgetToon.shader.md#l125) |
| BridgetToon.shader | _SkinShadeTint | 皮肤暗面乘色 | Color | [0.78, 0.49, 0.47, 1.0] | [第126行](code/BridgetToon.shader.md#l126) |
| BridgetToon.shader | _SleeveShadeTint | 白袖暗面乘色 | Color | [0.53, 0.62, 0.7, 1.0] | [第127行](code/BridgetToon.shader.md#l127) |
| BridgetToon.shader | _CullMode | 面剔除 | Float | 2.0 | [第129行](code/BridgetToon.shader.md#l129) |
| BridgetToon.shader | _UseMirroredUV | 读取第三套 UV | Float | 0.0 | [第130行](code/BridgetToon.shader.md#l130) |
| BridgetToon.shader | _DepthOffsetFactor | 深度偏移因子 | Float | 0.0 | [第131行](code/BridgetToon.shader.md#l131) |
| BridgetToon.shader | _DepthOffsetUnits | 深度偏移单位 | Float | 0.0 | [第132行](code/BridgetToon.shader.md#l132) |
| BridgetToon.shader | _LightTreshold | 明暗分界 | Range(0,1) | 0.5 | [第133行](code/BridgetToon.shader.md#l133) |
| BridgetToon.shader | _RampOffset | 区域明暗偏移 | Range(-1,1) | 0.0 | [第134行](code/BridgetToon.shader.md#l134) |
| BridgetToon.shader | _RampMaskCenter | ilm G 中性值（实验参数） | Range(0,1) | 0.4980392 | [第135行](code/BridgetToon.shader.md#l135) |
| BridgetToon.shader | _RampMaskStrength | ilm G 偏移强度 | Range(0,2) | 1.0 | [第136行](code/BridgetToon.shader.md#l136) |
| BridgetToon.shader | _ShadowSoftness | 明暗边界宽度 | Range(0,0.1) | 0.008 | [第137行](code/BridgetToon.shader.md#l137) |
| BridgetToon.shader | _ShadowIntensity | Sss 暗部混合 | Range(0,1) | 0.65 | [第138行](code/BridgetToon.shader.md#l138) |
| BridgetToon.shader | _ShadowTint | 暗部色调 | Color | [1.0, 1.0, 1.0, 1.0] | [第139行](code/BridgetToon.shader.md#l139) |
| BridgetToon.shader | _SkinShadowOffset | 低 R 分区明暗偏移 | Range(-0.5,0.5) | 0.06 | [第140行](code/BridgetToon.shader.md#l140) |
| BridgetToon.shader | _SecondShadowThreshold | 第二暗部阈值 / NdotL | Range(-1,1) | 0.1 | [第141行](code/BridgetToon.shader.md#l141) |
| BridgetToon.shader | _SecondShadowStrength | 下半身第二暗部强度 | Range(0,1) | 0.0 | [第142行](code/BridgetToon.shader.md#l142) |
| BridgetToon.shader | _SecondShadowTint | 第二暗部乘色 | Color | [1.0, 1.0, 1.0, 1.0] | [第143行](code/BridgetToon.shader.md#l143) |
| BridgetToon.shader | _LowerRegionUpper | 下半身区域上界 / 相对身高 | Range(0,1) | 0.52 | [第144行](code/BridgetToon.shader.md#l144) |
| BridgetToon.shader | _LowerRegionFeather | 区域过渡宽度 | Range(0.01,0.3) | 0.08 | [第145行](code/BridgetToon.shader.md#l145) |
| BridgetToon.shader | _LowerLightBlend | 下半身独立光向混合 | Range(0,1) | 0.0 | [第146行](code/BridgetToon.shader.md#l146) |
| BridgetToon.shader | _LowerLightDirection | 下半身独立光向 / 世界空间 | Vector | [0.8, 0.5, 0.2, 0.0] | [第147行](code/BridgetToon.shader.md#l147) |
| BridgetToon.shader | _LowerLightDynamic | 下半身跟随主光（移动光源 A/B） | Range(0,1) | 0.0 | [第148行](code/BridgetToon.shader.md#l148) |
| BridgetToon.shader | _LowerSkinColorGate | 用基础色排除低R白色材质（当前配色实验） | Range(0,1) | 1.0 | [第149行](code/BridgetToon.shader.md#l149) |
| BridgetToon.shader | _TasteRatePow | 下半身渐变指数（实验） | Range(0.1,4) | 1.0 | [第150行](code/BridgetToon.shader.md#l150) |
| BridgetToon.shader | _TasteHeightStart | 渐变高度下界（诊断） | Range(-1,2) | 0.0 | [第151行](code/BridgetToon.shader.md#l151) |
| BridgetToon.shader | _TasteHeightEnd | 渐变高度上界（诊断） | Range(-1,2) | 0.65 | [第152行](code/BridgetToon.shader.md#l152) |
| BridgetToon.shader | _TasteNormalWeight | 水平法线参与度（诊断） | Range(0,1) | 0.5 | [第153行](code/BridgetToon.shader.md#l153) |
| BridgetToon.shader | _RegionLightBlend | 部位光向混合（诊断） | Range(0,1) | 0.0 | [第154行](code/BridgetToon.shader.md#l154) |
| BridgetToon.shader | _RegionLightDirection | 部位候选光向（诊断） | Vector | [0.8, 0.5, 0.2, 0.0] | [第155行](code/BridgetToon.shader.md#l155) |
| BridgetToon.shader | _CharacterOriginWS | 角色脚下参考原点 | Vector | [0.0, 0.0, 0.0, 0.0] | [第156行](code/BridgetToon.shader.md#l156) |
| BridgetToon.shader | _CharacterHeight | 角色参考身高 | Float | 1.65 | [第157行](code/BridgetToon.shader.md#l157) |
| BridgetToon.shader | _LightIntensity | 主光贡献 | Range(0,2) | 0.9 | [第158行](code/BridgetToon.shader.md#l158) |
| BridgetToon.shader | _AmbientStrength | 环境光贡献 | Range(0,1) | 0.2 | [第159行](code/BridgetToon.shader.md#l159) |
| BridgetToon.shader | _AOStrength | 顶点 R 明暗控制 | Range(0,1) | 1.0 | [第160行](code/BridgetToon.shader.md#l160) |
| BridgetToon.shader | _DetailIntensity | Detail 强度 | Range(0,1) | 0.278 | [第161行](code/BridgetToon.shader.md#l161) |
| BridgetToon.shader | _InnerLineStrength | ilm Alpha 内部线条 | Range(0,1) | 0.65 | [第162行](code/BridgetToon.shader.md#l162) |
| BridgetToon.shader | _InnerLineColor | 内部线条颜色 | Color | [0.035, 0.028, 0.025, 1.0] | [第163行](code/BridgetToon.shader.md#l163) |
| BridgetToon.shader | _RimWidth | 边缘光宽度 | Range(0,1) | 0.16 | [第164行](code/BridgetToon.shader.md#l164) |
| BridgetToon.shader | _RimIntensity | 边缘光强度 | Range(0,1) | 0.16 | [第165行](code/BridgetToon.shader.md#l165) |
| BridgetToon.shader | _SpecularPower | 通用高光指数 | Range(1,100) | 24.0 | [第166行](code/BridgetToon.shader.md#l166) |
| BridgetToon.shader | _SpecularIntensity | 通用高光强度 | Range(0,2) | 0.12 | [第167行](code/BridgetToon.shader.md#l167) |
| BridgetToon.shader | _LayerMaskStep | 皮肤分区上界（实验分类） | Range(0,255) | 60.0 | [第168行](code/BridgetToon.shader.md#l168) |
| BridgetToon.shader | _BodySpecularWidth | 皮肤高光宽度 | Range(0,1) | 0.18 | [第169行](code/BridgetToon.shader.md#l169) |
| BridgetToon.shader | _BodySpecularIntensity | 皮肤高光强度 | Range(0,1) | 0.15 | [第170行](code/BridgetToon.shader.md#l170) |
| BridgetToon.shader | _HeadSpecularWidth | 头发高光宽度 | Range(0,1) | 0.14 | [第171行](code/BridgetToon.shader.md#l171) |
| BridgetToon.shader | _HeadSpecularIntensity | 头发高光强度 | Range(0,1) | 0.22 | [第172行](code/BridgetToon.shader.md#l172) |
| BridgetToon.shader | _HairLayerMin | 头发/布料共享分区下界 | Range(0,255) | 65.0 | [第173行](code/BridgetToon.shader.md#l173) |
| BridgetToon.shader | _HairLayerMax | 头发/布料共享分区上界 | Range(0,255) | 90.0 | [第174行](code/BridgetToon.shader.md#l174) |
| BridgetToon.shader | _LeatherLayerMin | 手套/裙子分区下界 | Range(0,255) | 90.0 | [第175行](code/BridgetToon.shader.md#l175) |
| BridgetToon.shader | _LeatherLayerMax | 手套/裙子分区上界 | Range(0,255) | 125.0 | [第176行](code/BridgetToon.shader.md#l176) |
| BridgetToon.shader | _MetalLayerMin | 金属分区下界 | Range(0,255) | 145.0 | [第177行](code/BridgetToon.shader.md#l177) |
| BridgetToon.shader | _MetalLayerMax | 金属分区上界 | Range(0,255) | 200.0 | [第178行](code/BridgetToon.shader.md#l178) |
| BridgetToon.shader | _MetallicStepSpecularWidth | 金属高光宽度 | Range(0,1) | 0.2 | [第179行](code/BridgetToon.shader.md#l179) |
| BridgetToon.shader | _MetallicStepSpecularIntensity | 金属高光强度 | Range(0,1) | 0.25 | [第180行](code/BridgetToon.shader.md#l180) |
| BridgetToon.shader | _ReceiveShadowStrength | 接收投影强度 | Range(0,1) | 0.7 | [第181行](code/BridgetToon.shader.md#l181) |
| BridgetToon.shader | _OutlineWidth | 轮廓宽度 / 输出像素 | Range(0,4) | 0.8 | [第182行](code/BridgetToon.shader.md#l182) |
| BridgetToon.shader | _UseSmoothOutline | 使用蒙皮平滑描边法线（需专用网格） | Float | 0.0 | [第183行](code/BridgetToon.shader.md#l183) |
| BridgetToon.shader | _OutlineSkinScale | 皮肤轮廓宽度比例 | Range(0,1) | 0.35 | [第184行](code/BridgetToon.shader.md#l184) |
| BridgetToon.shader | _OutlineColor | 轮廓颜色 | Color | [0.04, 0.03, 0.025, 1.0] | [第185行](code/BridgetToon.shader.md#l185) |
| BridgetToon.shader | _OutlineMapStrength | olm 颜色参与 | Range(0,1) | 0.6 | [第186行](code/BridgetToon.shader.md#l186) |
| BridgetToon.shader | _DebugMode | 调试输出 0～24（编号见修改文档） | Range(0,24) | 0.0 | [第187行](code/BridgetToon.shader.md#l187) |
| StageShadowReceiver.shader | _GeometryShadowFloor | 投影最低可见率 | Range(0,1) | 0.1 | [第6行](code/StageShadowReceiver.shader.md#l6) |
| StageShadowReceiver.shader | _GeometryShadowBias | 投影深度偏移/米 | Range(0,0.02) | 0.001 | [第7行](code/StageShadowReceiver.shader.md#l7) |
| StageShadowReceiver.shader | _GeometryShadowFilter | 投影边缘过滤/贴素 | Range(0,4) | 0.8 | [第8行](code/StageShadowReceiver.shader.md#l8) |
| StageShadowReceiver.shader | _GeometryShadowFade | 离接收面距离衰减 | Range(0,0.5) | 0.08 | [第9行](code/StageShadowReceiver.shader.md#l9) |
| StageShadowReceiver.shader | _Color | Backdrop Color | Color | [0.702, 0.702, 0.702, 1.0] | [第12行](code/StageShadowReceiver.shader.md#l12) |
| StageShadowReceiver.shader | _GradientStrength | Horizontal Falloff | Range(0, 1) | 0.134 | [第14行](code/StageShadowReceiver.shader.md#l14) |
| GgstDecal.shader | _MainTex | 原版贴花（线性数据） | 2D | gray | [第2行](code/GgstDecal.shader.md#l2) |
| GgstDecal.shader | _Strength | 贴花强度 | Range(0,1) | 1.0 | [第2行](code/GgstDecal.shader.md#l2) |
| GgstGlow.shader | _MainTex | 原版发光基础色 | 2D | white | [第2行](code/GgstGlow.shader.md#l2) |
| GgstGlow.shader | _GlowMultiplier | 发光倍率 | Float | 2.0 | [第2行](code/GgstGlow.shader.md#l2) |
