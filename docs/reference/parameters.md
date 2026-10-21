# 完整材质与属性账本

由 material_parameters.csv 自动转录，共 793 行、10 个材质。材质名、类型、默认值、保存值及保存字段是否存在逐列保留；没有保存字段时不能把空值当成 0。Color 与 Vector 即使以 r/g/b/a 序列化，也必须按类型解释。运行写入和内部覆盖另见[覆盖规则](overrides.md)。数值不是屏幕取色。

## BaseSecondary_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 | True |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 | True |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | {"r": 0.92, "g": 1, "b": 0.45, "a": 1} | True |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 | True |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 | True |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 | True |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 | True |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 | True |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 | True |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 | True |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 | True |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 | True |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 | True |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 | True |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 | True |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 | True |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 | True |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 | True |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | {"r": 0.92, "g": 1.1, "b": 1.28, "a": 0} | True |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | {"r": 0.82, "g": 0.7, "b": 0.82, "a": 0} | True |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | {"r": 0.99, "g": 1, "b": 1.07, "a": 0} | True |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | {"r": 0.9, "g": 0.93, "b": 1.02, "a": 0} | True |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | {"r": 1, "g": 1.08, "b": 1.23, "a": 0} | True |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | {"r": 1.03, "g": 1.06, "b": 1.19, "a": 0} | True |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 | True |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 | True |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 | True |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 | True |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | {"r": 0.94, "g": 0.97, "b": 1, "a": 1} | True |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 | True |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | {"r": 1, "g": 0.9, "b": 0.65, "a": 0.6} | True |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 | True |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 1 | True |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 | True |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 | True |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | {"r": 1, "g": 0.84, "b": 0.84, "a": 1} | True |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 1 | True |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 | True |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 | True |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 | True |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 | True |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 | True |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0 | True |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 | True |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 | True |
| _LineRefineEnabled | Float | 0.0 | 1 | True |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | {"r": 0.82, "g": 0.95, "b": 0.6, "a": 0.72} | True |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 | True |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | {"r": 0.72, "g": 0.76, "b": 0.58, "a": 0.72} | True |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 | True |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 | True |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | {"r": 0.06, "g": 0.032, "b": 0.015, "a": 1} | True |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | {"r": 0.023, "g": 0.031, "b": 0.042, "a": 1} | True |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | {"r": 0.1, "g": 0.045, "b": 0.027, "a": 1} | True |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | {"r": 0.04, "g": 0.032, "b": 0.022, "a": 1} | True |
| _FourMaterialSpecMask | 2D | "black" | {"path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 | True |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | {"r": 1, "g": 0.94, "b": 0.78, "a": 1} | True |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 | True |
| _ClothShinePower | Range(2,40) | 12.0 | 12 | True |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | {"r": 0.9, "g": 0.95, "b": 1, "a": 1} | True |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 | True |
| _SkinShinePower | Range(4,80) | 28.0 | 28 | True |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | {"r": 1, "g": 0.82, "b": 0.68, "a": 1} | True |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 | True |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | {"r": 1, "g": 0.97, "b": 0.9, "a": 1} | True |
| _MainTex | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_base.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _ShadowMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_Sss.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _LightMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_ilm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _DetailMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_detail.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _OutlineMap | 2D | "black" | {"path": "Assets/Bridget_Textures/BGT_olm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalMask | 2D | "black" | {"path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalEnabled | Float | 0.0 | 0 | True |
| _RegionalHead | Float | 0.0 | 0 | True |
| _FaceFrameValid | Float | 0.0 | 0 | True |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | {"r": 1, "g": 0, "b": 0, "a": 0.083} | True |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 | True |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 | True |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 | True |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 | True |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 | True |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 | True |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | {"r": 1, "g": 0.92, "b": 0.91, "a": 1} | True |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | {"r": 0.78, "g": 0.49, "b": 0.47, "a": 1} | True |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | {"r": 0.53, "g": 0.62, "b": 0.7, "a": 1} | True |
| _CullMode | Float | 2.0 | 2 | True |
| _UseMirroredUV | Float | 0.0 | 0 | True |
| _DepthOffsetFactor | Float | 0.0 | 0 | True |
| _DepthOffsetUnits | Float | 0.0 | 0 | True |
| _LightTreshold | Range(0,1) | 0.5 | 0.5 | True |
| _RampOffset | Range(-1,1) | 0.0 | 0 | True |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 | True |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 | True |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 | True |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 | True |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 1, "g": 1, "b": 1, "a": 1} | True |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 | True |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 | True |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 | True |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 0.55, "g": 0.22, "b": 0.28, "a": 1} | True |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 | True |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 | True |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 | True |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": -0.4, "a": 0} | True |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 | True |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 | True |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 | True |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 | True |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 | True |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 | True |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 | True |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": 0.2, "a": 0} | True |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _CharacterHeight | Float | 1.65 | 1.65 | True |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 | True |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 | True |
| _AOStrength | Range(0,1) | 1.0 | 1 | True |
| _DetailIntensity | Range(0,1) | 0.278 | 0.278 | True |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 | True |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | {"r": 0.035, "g": 0.028, "b": 0.025, "a": 1} | True |
| _RimWidth | Range(0,1) | 0.16 | 0.16 | True |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 | True |
| _SpecularPower | Range(1,100) | 24.0 | 15 | True |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 | True |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 | True |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 | True |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 | True |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 | True |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 | True |
| _HairLayerMin | Range(0,255) | 65.0 | 65 | True |
| _HairLayerMax | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 | True |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 | True |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 | True |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 | True |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 | True |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 | True |
| _OutlineWidth | Range(0,4) | 0.8 | 0.8 | True |
| _UseSmoothOutline | Float | 0.0 | 1 | True |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 | True |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | {"r": 0.04, "g": 0.03, "b": 0.025, "a": 1} | True |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 | True |
| _DebugMode | Range(0,24) | 0.0 | 0 | True |

## Base_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 | True |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 | True |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | {"r": 0.92, "g": 1, "b": 0.45, "a": 1} | True |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 | True |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 | True |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 | True |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 | True |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 | True |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 | True |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 | True |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 | True |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 | True |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 | True |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 | True |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 | True |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 | True |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 | True |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 | True |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | {"r": 0.92, "g": 1.1, "b": 1.28, "a": 0} | True |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | {"r": 0.82, "g": 0.7, "b": 0.82, "a": 0} | True |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | {"r": 0.99, "g": 1, "b": 1.07, "a": 0} | True |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | {"r": 0.9, "g": 0.93, "b": 1.02, "a": 0} | True |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | {"r": 1, "g": 1.08, "b": 1.23, "a": 0} | True |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | {"r": 1.03, "g": 1.06, "b": 1.19, "a": 0} | True |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 | True |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 | True |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 | True |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 | True |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | {"r": 0.94, "g": 0.97, "b": 1, "a": 1} | True |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 | True |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | {"r": 1, "g": 0.9, "b": 0.65, "a": 0.6} | True |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 | True |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 1 | True |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 | True |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 | True |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | {"r": 1, "g": 0.84, "b": 0.84, "a": 1} | True |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 1 | True |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 | True |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 | True |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 | True |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 | True |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 | True |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0 | True |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 | True |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 | True |
| _LineRefineEnabled | Float | 0.0 | 1 | True |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | {"r": 0.82, "g": 0.95, "b": 0.6, "a": 0.72} | True |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 | True |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | {"r": 0.72, "g": 0.76, "b": 0.58, "a": 0.72} | True |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 | True |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 | True |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | {"r": 0.06, "g": 0.032, "b": 0.015, "a": 1} | True |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | {"r": 0.023, "g": 0.031, "b": 0.042, "a": 1} | True |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | {"r": 0.1, "g": 0.045, "b": 0.027, "a": 1} | True |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | {"r": 0.04, "g": 0.032, "b": 0.022, "a": 1} | True |
| _FourMaterialSpecMask | 2D | "black" | {"path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 | True |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | {"r": 1, "g": 0.94, "b": 0.78, "a": 1} | True |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 | True |
| _ClothShinePower | Range(2,40) | 12.0 | 12 | True |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | {"r": 0.9, "g": 0.95, "b": 1, "a": 1} | True |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 | True |
| _SkinShinePower | Range(4,80) | 28.0 | 28 | True |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | {"r": 1, "g": 0.82, "b": 0.68, "a": 1} | True |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 | True |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | {"r": 1, "g": 0.97, "b": 0.9, "a": 1} | True |
| _MainTex | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_base.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _ShadowMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_Sss.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _LightMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_ilm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _DetailMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_detail.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _OutlineMap | 2D | "black" | {"path": "Assets/Bridget_Textures/BGT_olm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalMask | 2D | "black" | {"path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalEnabled | Float | 0.0 | 0 | True |
| _RegionalHead | Float | 0.0 | 0 | True |
| _FaceFrameValid | Float | 0.0 | 0 | True |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | {"r": 1, "g": 0, "b": 0, "a": 0.083} | True |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 | True |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 | True |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 | True |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 | True |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 | True |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 | True |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | {"r": 1, "g": 0.92, "b": 0.91, "a": 1} | True |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | {"r": 0.78, "g": 0.49, "b": 0.47, "a": 1} | True |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | {"r": 0.53, "g": 0.62, "b": 0.7, "a": 1} | True |
| _CullMode | Float | 2.0 | 2 | True |
| _UseMirroredUV | Float | 0.0 | 0 | True |
| _DepthOffsetFactor | Float | 0.0 | 0 | True |
| _DepthOffsetUnits | Float | 0.0 | 0 | True |
| _LightTreshold | Range(0,1) | 0.5 | 0.5 | True |
| _RampOffset | Range(-1,1) | 0.0 | 0 | True |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 | True |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 | True |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 | True |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 | True |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 1, "g": 1, "b": 1, "a": 1} | True |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 | True |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 | True |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 | True |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 0.55, "g": 0.22, "b": 0.28, "a": 1} | True |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 | True |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 | True |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 | True |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": -0.4, "a": 0} | True |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 | True |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 | True |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 | True |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 | True |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 | True |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 | True |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 | True |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": 0.2, "a": 0} | True |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _CharacterHeight | Float | 1.65 | 1.65 | True |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 | True |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 | True |
| _AOStrength | Range(0,1) | 1.0 | 1 | True |
| _DetailIntensity | Range(0,1) | 0.278 | 0.278 | True |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 | True |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | {"r": 0.035, "g": 0.028, "b": 0.025, "a": 1} | True |
| _RimWidth | Range(0,1) | 0.16 | 0.16 | True |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 | True |
| _SpecularPower | Range(1,100) | 24.0 | 15 | True |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 | True |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 | True |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 | True |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 | True |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 | True |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 | True |
| _HairLayerMin | Range(0,255) | 65.0 | 65 | True |
| _HairLayerMax | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 | True |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 | True |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 | True |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 | True |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 | True |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 | True |
| _OutlineWidth | Range(0,4) | 0.8 | 0.8 | True |
| _UseSmoothOutline | Float | 0.0 | 1 | True |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 | True |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | {"r": 0.04, "g": 0.03, "b": 0.025, "a": 1} | True |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 | True |
| _DebugMode | Range(0,24) | 0.0 | 0 | True |

## BodyBaseFlip_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 | True |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 | True |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | {"r": 0.92, "g": 1, "b": 0.45, "a": 1} | True |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 | True |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 | True |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 | True |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 | True |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 | True |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 | True |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 | True |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 | True |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 | True |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 | True |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 | True |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 | True |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 | True |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 | True |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 | True |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | {"r": 0.92, "g": 1.1, "b": 1.28, "a": 0} | True |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | {"r": 0.82, "g": 0.7, "b": 0.82, "a": 0} | True |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | {"r": 0.99, "g": 1, "b": 1.07, "a": 0} | True |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | {"r": 0.9, "g": 0.93, "b": 1.02, "a": 0} | True |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | {"r": 1, "g": 1.08, "b": 1.23, "a": 0} | True |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | {"r": 1.03, "g": 1.06, "b": 1.19, "a": 0} | True |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 | True |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 | True |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 | True |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 | True |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | {"r": 0.94, "g": 0.97, "b": 1, "a": 1} | True |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 | True |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | {"r": 1, "g": 0.9, "b": 0.65, "a": 0.6} | True |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 | True |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 0 | True |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 | True |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 | True |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | {"r": 1, "g": 0.8399999, "b": 0.8399999, "a": 1} | True |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 0 | True |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 | True |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 | True |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 | True |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 | True |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 | True |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0.75 | True |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 | True |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 | True |
| _LineRefineEnabled | Float | 0.0 | 1 | True |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | {"r": 0.82, "g": 0.95, "b": 0.6, "a": 0.72} | True |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 | True |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | {"r": 0.72, "g": 0.76, "b": 0.58, "a": 0.72} | True |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 | True |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 | True |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | {"r": 0.06, "g": 0.032, "b": 0.015, "a": 1} | True |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | {"r": 0.023, "g": 0.031, "b": 0.042, "a": 1} | True |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | {"r": 0.1, "g": 0.045, "b": 0.027, "a": 1} | True |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | {"r": 0.04, "g": 0.032, "b": 0.022, "a": 1} | True |
| _FourMaterialSpecMask | 2D | "black" | {"path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 | True |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | {"r": 1, "g": 0.94, "b": 0.78, "a": 1} | True |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 | True |
| _ClothShinePower | Range(2,40) | 12.0 | 12 | True |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | {"r": 0.9, "g": 0.95, "b": 1, "a": 1} | True |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 | True |
| _SkinShinePower | Range(4,80) | 28.0 | 28 | True |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | {"r": 1, "g": 0.82, "b": 0.68, "a": 1} | True |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 | True |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | {"r": 1, "g": 0.97, "b": 0.9, "a": 1} | True |
| _MainTex | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_base.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _ShadowMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_Sss.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _LightMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_ilm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _DetailMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_detail.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _OutlineMap | 2D | "black" | {"path": "Assets/Bridget_Textures/BGT_olm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalMask | 2D | "black" | {"path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalEnabled | Float | 0.0 | 0 | True |
| _RegionalHead | Float | 0.0 | 0 | True |
| _FaceFrameValid | Float | 0.0 | 0 | True |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | {"r": 1, "g": 0, "b": 0, "a": 0.083} | True |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 | True |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 | True |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 | True |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 | True |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 | True |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 | True |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | {"r": 1, "g": 0.92, "b": 0.91, "a": 1} | True |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | {"r": 0.78, "g": 0.49, "b": 0.47, "a": 1} | True |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | {"r": 0.53, "g": 0.62, "b": 0.7, "a": 1} | True |
| _CullMode | Float | 2.0 | 2 | True |
| _UseMirroredUV | Float | 0.0 | 0 | True |
| _DepthOffsetFactor | Float | 0.0 | 0 | True |
| _DepthOffsetUnits | Float | 0.0 | 0 | True |
| _LightTreshold | Range(0,1) | 0.5 | 0.624 | True |
| _RampOffset | Range(-1,1) | 0.0 | 0 | True |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 | True |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 | True |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 | True |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 | True |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 1, "g": 1, "b": 1, "a": 1} | True |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 | True |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 | True |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 | True |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 0.55, "g": 0.22, "b": 0.28, "a": 1} | True |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 | True |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 | True |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 | True |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": -0.4, "a": 0} | True |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 | True |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 | True |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 | True |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 | True |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 | True |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 | True |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 | True |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": 0.2, "a": 0} | True |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _CharacterHeight | Float | 1.65 | 1.65 | True |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 | True |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 | True |
| _AOStrength | Range(0,1) | 1.0 | 1 | True |
| _DetailIntensity | Range(0,1) | 0.278 | 0.278 | True |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 | True |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | {"r": 0.035, "g": 0.028, "b": 0.025, "a": 1} | True |
| _RimWidth | Range(0,1) | 0.16 | 0.16 | True |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 | True |
| _SpecularPower | Range(1,100) | 24.0 | 15 | True |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 | True |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 | True |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 | True |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 | True |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 | True |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 | True |
| _HairLayerMin | Range(0,255) | 65.0 | 65 | True |
| _HairLayerMax | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 | True |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 | True |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 | True |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 | True |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 | True |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 | True |
| _OutlineWidth | Range(0,4) | 0.8 | 0 | True |
| _UseSmoothOutline | Float | 0.0 | 1 | True |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 | True |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | {"r": 0.04, "g": 0.03, "b": 0.025, "a": 1} | True |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 | True |
| _DebugMode | Range(0,24) | 0.0 | 0 | True |

## BodyDecal_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _MainTex | 2D | "gray" | {"path": "Assets/Bridget_Textures/BGT_decal.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _Strength | Range(0,1) | 1.0 | 1 | True |

## CoatExterior_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 | True |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 | True |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | {"r": 0.92, "g": 1, "b": 0.45, "a": 1} | True |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 | True |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 | True |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 | True |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 | True |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 | True |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 | True |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 | True |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 | True |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 | True |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 | True |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 | True |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 | True |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 | True |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 | True |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 | True |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 | True |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | {"r": 0.92, "g": 1.1, "b": 1.28, "a": 0} | True |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | {"r": 0.82, "g": 0.7, "b": 0.82, "a": 0} | True |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | {"r": 0.99, "g": 1, "b": 1.07, "a": 0} | True |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | {"r": 0.9, "g": 0.93, "b": 1.02, "a": 0} | True |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | {"r": 1, "g": 1.08, "b": 1.23, "a": 0} | True |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | {"r": 1.03, "g": 1.06, "b": 1.19, "a": 0} | True |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 | True |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 | True |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 | True |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 | True |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | {"r": 0.94, "g": 0.97, "b": 1, "a": 1} | True |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 | True |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | {"r": 1, "g": 0.9, "b": 0.65, "a": 0.6} | True |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 | True |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 0 | True |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 | True |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 | True |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 | True |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | {"r": 1, "g": 0.8399999, "b": 0.8399999, "a": 1} | True |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 0 | True |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 | True |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 | True |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 | True |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 | True |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 | True |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0.75 | True |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 | True |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 | True |
| _LineRefineEnabled | Float | 0.0 | 1 | True |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | {"r": 0.82, "g": 0.95, "b": 0.6, "a": 0.72} | True |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 | True |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | {"r": 0.72, "g": 0.76, "b": 0.58, "a": 0.72} | True |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 | True |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 | True |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | {"r": 0.06, "g": 0.032, "b": 0.015, "a": 1} | True |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | {"r": 0.023, "g": 0.031, "b": 0.042, "a": 1} | True |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | {"r": 0.1, "g": 0.045, "b": 0.027, "a": 1} | True |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | {"r": 0.04, "g": 0.032, "b": 0.022, "a": 1} | True |
| _FourMaterialSpecMask | 2D | "black" | {"path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 | True |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 | True |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | {"r": 1, "g": 0.94, "b": 0.78, "a": 1} | True |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 | True |
| _ClothShinePower | Range(2,40) | 12.0 | 12 | True |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | {"r": 0.9, "g": 0.95, "b": 1, "a": 1} | True |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 | True |
| _SkinShinePower | Range(4,80) | 28.0 | 28 | True |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | {"r": 1, "g": 0.82, "b": 0.68, "a": 1} | True |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 | True |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 | True |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | {"r": 1, "g": 0.97, "b": 0.9, "a": 1} | True |
| _MainTex | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_base.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _ShadowMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_Sss.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _LightMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_ilm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _DetailMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_detail.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _OutlineMap | 2D | "black" | {"path": "Assets/Bridget_Textures/BGT_olm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalMask | 2D | "black" | {"path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalEnabled | Float | 0.0 | 0 | True |
| _RegionalHead | Float | 0.0 | 0 | True |
| _FaceFrameValid | Float | 0.0 | 0 | True |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | {"r": 1, "g": 0, "b": 0, "a": 0.083} | True |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 | True |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 | True |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 | True |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 | True |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 | True |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 | True |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 | True |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | {"r": 1, "g": 0.92, "b": 0.91, "a": 1} | True |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | {"r": 0.78, "g": 0.49, "b": 0.47, "a": 1} | True |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | {"r": 0.53, "g": 0.62, "b": 0.7, "a": 1} | True |
| _CullMode | Float | 2.0 | 2 | True |
| _UseMirroredUV | Float | 0.0 | 0 | True |
| _DepthOffsetFactor | Float | 0.0 | 0 | True |
| _DepthOffsetUnits | Float | 0.0 | 0 | True |
| _LightTreshold | Range(0,1) | 0.5 | 0.5 | True |
| _RampOffset | Range(-1,1) | 0.0 | 0 | True |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 | True |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 | True |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 | True |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 | True |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 1, "g": 1, "b": 1, "a": 1} | True |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 | True |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 | True |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 | True |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 0.55, "g": 0.22, "b": 0.28, "a": 1} | True |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 | True |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 | True |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 | True |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": -0.4, "a": 0} | True |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 | True |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 | True |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 | True |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 | True |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 | True |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 | True |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 | True |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": 0.2, "a": 0} | True |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _CharacterHeight | Float | 1.65 | 1.65 | True |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 | True |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 | True |
| _AOStrength | Range(0,1) | 1.0 | 1 | True |
| _DetailIntensity | Range(0,1) | 0.278 | 0 | True |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 | True |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | {"r": 0.035, "g": 0.028, "b": 0.025, "a": 1} | True |
| _RimWidth | Range(0,1) | 0.16 | 0.16 | True |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 | True |
| _SpecularPower | Range(1,100) | 24.0 | 15 | True |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 | True |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 | True |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 | True |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 | True |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 | True |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 | True |
| _HairLayerMin | Range(0,255) | 65.0 | 65 | True |
| _HairLayerMax | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 | True |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 | True |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 | True |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 | True |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 | True |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 | True |
| _OutlineWidth | Range(0,4) | 0.8 | 0.8 | True |
| _UseSmoothOutline | Float | 0.0 | 1 | True |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 | True |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | {"r": 0.04, "g": 0.03, "b": 0.025, "a": 1} | True |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 | True |
| _DebugMode | Range(0,24) | 0.0 | 0 | True |

## HeadDecal_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _MainTex | 2D | "gray" | {"path": "Assets/Bridget_Textures/BGT_decal.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _Strength | Range(0,1) | 1.0 | 1 | True |

## HeadGlow_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _MainTex | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_base.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _GlowMultiplier | Float | 2.0 | 2 | True |

## StageFloorReceiver

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _GeometryShadowFloor | Range(0,1) | 0.1 | 0.08 | True |
| _GeometryShadowBias | Range(0,0.02) | 0.001 | 0.0007 | True |
| _GeometryShadowFilter | Range(0,4) | 0.8 | 0.65 | True |
| _GeometryShadowFade | Range(0,0.5) | 0.08 | 0.12 | True |
| _Color | Color | [0.702, 0.702, 0.702, 1.0] | {"r": 0.74509805, "g": 0.74509805, "b": 0.74509805, "a": 1} | True |
| _GradientStrength | Range(0, 1) | 0.134 | 0 | True |

## StageWallReceiver

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _GeometryShadowFloor | Range(0,1) | 0.1 | 0.1 | True |
| _GeometryShadowBias | Range(0,0.02) | 0.001 | 0.001 | True |
| _GeometryShadowFilter | Range(0,4) | 0.8 | 0.8 | True |
| _GeometryShadowFade | Range(0,0.5) | 0.08 | 0.08 | True |
| _Color | Color | [0.702, 0.702, 0.702, 1.0] | {"r": 0.7019608, "g": 0.7019608, "b": 0.7019608, "a": 1} | True |
| _GradientStrength | Range(0, 1) | 0.134 | 0.31 | True |

## Weapon_Imitate

| 属性 | 类型 | Shader 默认 | 材质保存 | savedPresent |
|---|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | null | False |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | null | False |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | null | False |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | null | False |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | null | False |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | null | False |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | null | False |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | null | False |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | null | False |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | null | False |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | null | False |
| _FocusedHairGain | Range(0,2) | 1.25 | null | False |
| _FocusedClothGain | Range(0,2) | 1.2 | null | False |
| _FocusedMetalGain | Range(0,2) | 1.05 | null | False |
| _CleanShadeEnabled | Range(0,1) | 0.0 | null | False |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | null | False |
| _CleanClothAOWeight | Range(0,1) | 0.25 | null | False |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | null | False |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | null | False |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | null | False |
| _PaletteEnabled | Range(0,1) | 0.0 | null | False |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | null | False |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | null | False |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | null | False |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | null | False |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | null | False |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | null | False |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | null | False |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | null | False |
| _ReferenceRimStrength | Range(0,1) | 0.38 | null | False |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | null | False |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | null | False |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | null | False |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | null | False |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | null | False |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | null | False |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | null | False |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | null | False |
| _FaceDiffuseSide | Range(0,1) | 0.9 | null | False |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | null | False |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | null | False |
| _EyeRefineEnabled | Range(0,1) | 0.0 | null | False |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | null | False |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | null | False |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | null | False |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | null | False |
| _EyeScleraShade | Range(0,0.2) | 0.06 | null | False |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | null | False |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | null | False |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | null | False |
| _LineRefineEnabled | Float | 0.0 | null | False |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | null | False |
| _LineContourTintMix | Range(0,1) | 0.55 | null | False |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | null | False |
| _LineInnerFilter | Range(0,1) | 0.6 | null | False |
| _LineInnerTintMix | Range(0,1) | 0.45 | null | False |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | null | False |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | null | False |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | null | False |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | null | False |
| _FourMaterialSpecMask | 2D | "black" | null | False |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | null | False |
| _HairShineStrength | Range(0,0.5) | 0.12 | null | False |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | null | False |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | null | False |
| _ClothShineStrength | Range(0,0.2) | 0.035 | null | False |
| _ClothShinePower | Range(2,40) | 12.0 | null | False |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | null | False |
| _SkinShineStrength | Range(0,0.2) | 0.028 | null | False |
| _SkinShinePower | Range(4,80) | 28.0 | null | False |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | null | False |
| _MetalShineStrength | Range(0,1) | 0.38 | null | False |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | null | False |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | null | False |
| _MainTex | 2D | "white" | {"path": "Assets/Bridget_Textures/BGTW_base.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _ShadowMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGTW_Sss.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _LightMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGTW_ilm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _DetailMap | 2D | "white" | {"path": "Assets/Bridget_Textures/BGT_detail.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _OutlineMap | 2D | "black" | {"path": "Assets/Bridget_Textures/BGT_olm.png", "scale": {"x": 1, "y": 1}, "offset": {"x": 0, "y": 0}} | True |
| _RegionalMask | 2D | "black" | null | False |
| _RegionalEnabled | Float | 0.0 | null | False |
| _RegionalHead | Float | 0.0 | null | False |
| _FaceFrameValid | Float | 0.0 | null | False |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | null | False |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | null | False |
| _FaceSideStrength | Range(0,1) | 0.85 | null | False |
| _FaceShadeThreshold | Range(0,1) | 0.8 | null | False |
| _SkinShadeThreshold | Range(0,1) | 0.69 | null | False |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | null | False |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | null | False |
| _FaceShadeStrength | Range(0,1) | 0.78 | null | False |
| _SkinShadeStrength | Range(0,1) | 0.72 | null | False |
| _SleeveShadeStrength | Range(0,1) | 0.72 | null | False |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | null | False |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | null | False |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | null | False |
| _CullMode | Float | 2.0 | 2 | True |
| _UseMirroredUV | Float | 0.0 | 0 | True |
| _DepthOffsetFactor | Float | 0.0 | 0 | True |
| _DepthOffsetUnits | Float | 0.0 | 0 | True |
| _LightTreshold | Range(0,1) | 0.5 | 0.5 | True |
| _RampOffset | Range(-1,1) | 0.0 | 0 | True |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 | True |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 | True |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 | True |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 | True |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 1, "g": 1, "b": 1, "a": 1} | True |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 | True |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 | True |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0 | True |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | {"r": 1, "g": 1, "b": 1, "a": 1} | True |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 | True |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 | True |
| _LowerLightBlend | Range(0,1) | 0.0 | 0 | True |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | {"r": 0.8, "g": 0.5, "b": 0.2, "a": 0} | True |
| _LowerLightDynamic | Range(0,1) | 0.0 | null | False |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 | True |
| _TasteRatePow | Range(0.1,4) | 1.0 | null | False |
| _TasteHeightStart | Range(-1,2) | 0.0 | null | False |
| _TasteHeightEnd | Range(-1,2) | 0.65 | null | False |
| _TasteNormalWeight | Range(0,1) | 0.5 | null | False |
| _RegionLightBlend | Range(0,1) | 0.0 | null | False |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | null | False |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | {"r": 0, "g": 0, "b": 0, "a": 0} | True |
| _CharacterHeight | Float | 1.65 | 1.65 | True |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 | True |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 | True |
| _AOStrength | Range(0,1) | 1.0 | 1 | True |
| _DetailIntensity | Range(0,1) | 0.278 | 0.278 | True |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 | True |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | {"r": 0.035, "g": 0.028, "b": 0.025, "a": 1} | True |
| _RimWidth | Range(0,1) | 0.16 | 0.16 | True |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 | True |
| _SpecularPower | Range(1,100) | 24.0 | 24 | True |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 | True |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 | True |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 | True |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 | True |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 | True |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 | True |
| _HairLayerMin | Range(0,255) | 65.0 | 65 | True |
| _HairLayerMax | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 | True |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 | True |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 | True |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 | True |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 | True |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 | True |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 | True |
| _OutlineWidth | Range(0,4) | 0.8 | 0.8 | True |
| _UseSmoothOutline | Float | 0.0 | 0 | True |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 | True |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | {"r": 0.04, "g": 0.03, "b": 0.025, "a": 1} | True |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 | True |
| _DebugMode | Range(0,24) | 0.0 | 0 | True |
