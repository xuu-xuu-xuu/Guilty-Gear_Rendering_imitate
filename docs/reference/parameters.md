# 材质参数参考

先在对应章节调整关键参数，再用本表查完整值。Shader默认值是新材质起点，材质设置是示例角色的保存配置；Renderer MPB和全局输入仍可能覆盖同名字段，见[参数层级](overrides.md)。Color和Vector按类型使用，数值不是最终屏幕取色。未保存不等于0。

## Base_Imitate

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | (0.92, 1, 0.45, 1) |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | (0.92, 1.1, 1.28, 0) |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | (0.82, 0.7, 0.82, 0) |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | (0.99, 1, 1.07, 0) |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | (0.9, 0.93, 1.02, 0) |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | (1, 1.08, 1.23, 0) |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | (1.03, 1.06, 1.19, 0) |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | (0.94, 0.97, 1, 1) |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | (1, 0.9, 0.65, 0.6) |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 1 |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | (1, 0.84, 0.84, 1) |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 1 |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0 |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 |
| _LineRefineEnabled | Float | 0.0 | 1 |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | (0.82, 0.95, 0.6, 0.72) |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | (0.72, 0.76, 0.58, 0.72) |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | (0.06, 0.032, 0.015, 1) |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | (0.023, 0.031, 0.042, 1) |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | (0.1, 0.045, 0.027, 1) |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | (0.04, 0.032, 0.022, 1) |
| _FourMaterialSpecMask | 2D | black | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | (1, 0.94, 0.78, 1) |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 |
| _ClothShinePower | Range(2,40) | 12.0 | 12 |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | (0.9, 0.95, 1, 1) |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 |
| _SkinShinePower | Range(4,80) | 28.0 | 28 |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | (1, 0.82, 0.68, 1) |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | (1, 0.97, 0.9, 1) |
| _MainTex | 2D | white | Assets/Bridget_Textures/BGT_base.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _ShadowMap | 2D | white | Assets/Bridget_Textures/BGT_Sss.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _LightMap | 2D | white | Assets/Bridget_Textures/BGT_ilm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _DetailMap | 2D | white | Assets/Bridget_Textures/BGT_detail.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _OutlineMap | 2D | black | Assets/Bridget_Textures/BGT_olm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalMask | 2D | black | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalEnabled | Float | 0.0 | 0 |
| _RegionalHead | Float | 0.0 | 0 |
| _FaceFrameValid | Float | 0.0 | 0 |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | (1, 0, 0, 0.083) |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | (1, 0.92, 0.91, 1) |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | (0.78, 0.49, 0.47, 1) |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | (0.53, 0.62, 0.7, 1) |
| _CullMode | Float | 2.0 | 2 |
| _UseMirroredUV | Float | 0.0 | 0 |
| _DepthOffsetFactor | Float | 0.0 | 0 |
| _DepthOffsetUnits | Float | 0.0 | 0 |
| _LightTreshold | Range(0,1) | 0.5 | 0.5 |
| _RampOffset | Range(-1,1) | 0.0 | 0 |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (1, 1, 1, 1) |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (0.55, 0.22, 0.28, 1) |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, -0.4, 0) |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, 0.2, 0) |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _CharacterHeight | Float | 1.65 | 1.65 |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 |
| _AOStrength | Range(0,1) | 1.0 | 1 |
| _DetailIntensity | Range(0,1) | 0.278 | 0.278 |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | (0.035, 0.028, 0.025, 1) |
| _RimWidth | Range(0,1) | 0.16 | 0.16 |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 |
| _SpecularPower | Range(1,100) | 24.0 | 15 |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 |
| _HairLayerMin | Range(0,255) | 65.0 | 65 |
| _HairLayerMax | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 |
| _OutlineWidth | Range(0,4) | 0.8 | 0.8 |
| _UseSmoothOutline | Float | 0.0 | 1 |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | (0.04, 0.03, 0.025, 1) |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 |
| _DebugMode | Range(0,24) | 0.0 | 0 |

## BaseSecondary_Imitate

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | (0.92, 1, 0.45, 1) |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | (0.92, 1.1, 1.28, 0) |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | (0.82, 0.7, 0.82, 0) |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | (0.99, 1, 1.07, 0) |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | (0.9, 0.93, 1.02, 0) |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | (1, 1.08, 1.23, 0) |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | (1.03, 1.06, 1.19, 0) |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | (0.94, 0.97, 1, 1) |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | (1, 0.9, 0.65, 0.6) |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 1 |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | (1, 0.84, 0.84, 1) |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 1 |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0 |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 |
| _LineRefineEnabled | Float | 0.0 | 1 |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | (0.82, 0.95, 0.6, 0.72) |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | (0.72, 0.76, 0.58, 0.72) |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | (0.06, 0.032, 0.015, 1) |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | (0.023, 0.031, 0.042, 1) |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | (0.1, 0.045, 0.027, 1) |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | (0.04, 0.032, 0.022, 1) |
| _FourMaterialSpecMask | 2D | black | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | (1, 0.94, 0.78, 1) |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 |
| _ClothShinePower | Range(2,40) | 12.0 | 12 |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | (0.9, 0.95, 1, 1) |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 |
| _SkinShinePower | Range(4,80) | 28.0 | 28 |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | (1, 0.82, 0.68, 1) |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | (1, 0.97, 0.9, 1) |
| _MainTex | 2D | white | Assets/Bridget_Textures/BGT_base.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _ShadowMap | 2D | white | Assets/Bridget_Textures/BGT_Sss.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _LightMap | 2D | white | Assets/Bridget_Textures/BGT_ilm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _DetailMap | 2D | white | Assets/Bridget_Textures/BGT_detail.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _OutlineMap | 2D | black | Assets/Bridget_Textures/BGT_olm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalMask | 2D | black | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalEnabled | Float | 0.0 | 0 |
| _RegionalHead | Float | 0.0 | 0 |
| _FaceFrameValid | Float | 0.0 | 0 |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | (1, 0, 0, 0.083) |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | (1, 0.92, 0.91, 1) |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | (0.78, 0.49, 0.47, 1) |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | (0.53, 0.62, 0.7, 1) |
| _CullMode | Float | 2.0 | 2 |
| _UseMirroredUV | Float | 0.0 | 0 |
| _DepthOffsetFactor | Float | 0.0 | 0 |
| _DepthOffsetUnits | Float | 0.0 | 0 |
| _LightTreshold | Range(0,1) | 0.5 | 0.5 |
| _RampOffset | Range(-1,1) | 0.0 | 0 |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (1, 1, 1, 1) |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (0.55, 0.22, 0.28, 1) |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, -0.4, 0) |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, 0.2, 0) |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _CharacterHeight | Float | 1.65 | 1.65 |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 |
| _AOStrength | Range(0,1) | 1.0 | 1 |
| _DetailIntensity | Range(0,1) | 0.278 | 0.278 |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | (0.035, 0.028, 0.025, 1) |
| _RimWidth | Range(0,1) | 0.16 | 0.16 |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 |
| _SpecularPower | Range(1,100) | 24.0 | 15 |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 |
| _HairLayerMin | Range(0,255) | 65.0 | 65 |
| _HairLayerMax | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 |
| _OutlineWidth | Range(0,4) | 0.8 | 0.8 |
| _UseSmoothOutline | Float | 0.0 | 1 |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | (0.04, 0.03, 0.025, 1) |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 |
| _DebugMode | Range(0,24) | 0.0 | 0 |

## BodyBaseFlip_Imitate

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | (0.92, 1, 0.45, 1) |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | (0.92, 1.1, 1.28, 0) |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | (0.82, 0.7, 0.82, 0) |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | (0.99, 1, 1.07, 0) |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | (0.9, 0.93, 1.02, 0) |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | (1, 1.08, 1.23, 0) |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | (1.03, 1.06, 1.19, 0) |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | (0.94, 0.97, 1, 1) |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | (1, 0.9, 0.65, 0.6) |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 0 |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | (1, 0.8399999, 0.8399999, 1) |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 0 |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0.75 |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 |
| _LineRefineEnabled | Float | 0.0 | 1 |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | (0.82, 0.95, 0.6, 0.72) |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | (0.72, 0.76, 0.58, 0.72) |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | (0.06, 0.032, 0.015, 1) |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | (0.023, 0.031, 0.042, 1) |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | (0.1, 0.045, 0.027, 1) |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | (0.04, 0.032, 0.022, 1) |
| _FourMaterialSpecMask | 2D | black | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | (1, 0.94, 0.78, 1) |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 |
| _ClothShinePower | Range(2,40) | 12.0 | 12 |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | (0.9, 0.95, 1, 1) |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 |
| _SkinShinePower | Range(4,80) | 28.0 | 28 |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | (1, 0.82, 0.68, 1) |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | (1, 0.97, 0.9, 1) |
| _MainTex | 2D | white | Assets/Bridget_Textures/BGT_base.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _ShadowMap | 2D | white | Assets/Bridget_Textures/BGT_Sss.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _LightMap | 2D | white | Assets/Bridget_Textures/BGT_ilm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _DetailMap | 2D | white | Assets/Bridget_Textures/BGT_detail.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _OutlineMap | 2D | black | Assets/Bridget_Textures/BGT_olm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalMask | 2D | black | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalEnabled | Float | 0.0 | 0 |
| _RegionalHead | Float | 0.0 | 0 |
| _FaceFrameValid | Float | 0.0 | 0 |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | (1, 0, 0, 0.083) |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | (1, 0.92, 0.91, 1) |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | (0.78, 0.49, 0.47, 1) |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | (0.53, 0.62, 0.7, 1) |
| _CullMode | Float | 2.0 | 2 |
| _UseMirroredUV | Float | 0.0 | 0 |
| _DepthOffsetFactor | Float | 0.0 | 0 |
| _DepthOffsetUnits | Float | 0.0 | 0 |
| _LightTreshold | Range(0,1) | 0.5 | 0.624 |
| _RampOffset | Range(-1,1) | 0.0 | 0 |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (1, 1, 1, 1) |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (0.55, 0.22, 0.28, 1) |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, -0.4, 0) |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, 0.2, 0) |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _CharacterHeight | Float | 1.65 | 1.65 |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 |
| _AOStrength | Range(0,1) | 1.0 | 1 |
| _DetailIntensity | Range(0,1) | 0.278 | 0.278 |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | (0.035, 0.028, 0.025, 1) |
| _RimWidth | Range(0,1) | 0.16 | 0.16 |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 |
| _SpecularPower | Range(1,100) | 24.0 | 15 |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 |
| _HairLayerMin | Range(0,255) | 65.0 | 65 |
| _HairLayerMax | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 |
| _OutlineWidth | Range(0,4) | 0.8 | 0 |
| _UseSmoothOutline | Float | 0.0 | 1 |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | (0.04, 0.03, 0.025, 1) |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 |
| _DebugMode | Range(0,24) | 0.0 | 0 |

## CoatExterior_Imitate

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _ThighLobeEnabled | Range(0,1) | 0.0 | 1 |
| _ThighLobeStrength | Range(0,0.4) | 0.16 | 0.16 |
| _ThighLobeTint | Color | [0.92, 1.0, 0.45, 1.0] | (0.92, 1, 0.45, 1) |
| _FocusedShadeEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedSpecEnabled | Range(0,1) | 0.0 | 1 |
| _FocusedTunicThreshold | Range(0.2,0.7) | 0.4 | 0.4 |
| _FocusedThighThreshold | Range(0.3,0.8) | 0.57 | 0.57 |
| _FocusedCalfThreshold | Range(0.3,0.8) | 0.59 | 0.59 |
| _FocusedKneeThreshold | Range(0.3,0.8) | 0.62 | 0.62 |
| _FocusedSkinStrength | Range(0,0.4) | 0.14 | 0.14 |
| _FocusedSkinWidth | Range(0.02,0.4) | 0.22 | 0.22 |
| _FocusedHairGain | Range(0,2) | 1.25 | 1.25 |
| _FocusedClothGain | Range(0,2) | 1.2 | 1.2 |
| _FocusedMetalGain | Range(0,2) | 1.05 | 1.05 |
| _CleanShadeEnabled | Range(0,1) | 0.0 | 1 |
| _CleanClothMaskWeight | Range(0,1) | 0.4 | 0.4 |
| _CleanClothAOWeight | Range(0,1) | 0.25 | 0.25 |
| _CleanClothSoftness | Range(0.005,0.06) | 0.018 | 0.018 |
| _CleanFaceUnderStart | Range(-1,0) | -0.7 | -0.7 |
| _CleanFaceUnderEnd | Range(-1,0.2) | -0.45 | -0.45 |
| _PaletteEnabled | Range(0,1) | 0.0 | 1 |
| _PaletteSkinLight | Vector | [0.92, 1.1, 1.28, 0.0] | (0.92, 1.1, 1.28, 0) |
| _PaletteSkinDark | Vector | [0.82, 0.7, 0.82, 0.0] | (0.82, 0.7, 0.82, 0) |
| _PaletteSleeveLight | Vector | [0.99, 1.0, 1.07, 0.0] | (0.99, 1, 1.07, 0) |
| _PaletteSleeveDark | Vector | [0.9, 0.93, 1.02, 0.0] | (0.9, 0.93, 1.02, 0) |
| _PaletteTunicLight | Vector | [1.0, 1.08, 1.23, 0.0] | (1, 1.08, 1.23, 0) |
| _PaletteTunicDark | Vector | [1.03, 1.06, 1.19, 0.0] | (1.03, 1.06, 1.19, 0) |
| _ReferenceRimEnabled | Range(0,1) | 0.0 | 1 |
| _ReferenceRimWidth | Range(0.02,0.4) | 0.19 | 0.24 |
| _ReferenceRimStrength | Range(0,1) | 0.38 | 0.5 |
| _ReferenceRimShadowFloor | Range(0,1) | 0.45 | 0.55 |
| _ReferenceRimTint | Color | [0.94, 0.97, 1.0, 1.0] | (0.94, 0.97, 1, 1) |
| _ReferenceRimTintMix | Range(0,1) | 0.65 | 0.75 |
| _ReferenceRimMaterial | Vector | [1.0, 0.9, 0.65, 0.6] | (1, 0.9, 0.65, 0.6) |
| _ReferenceRimFaceScale | Range(0,1) | 0.15 | 0.15 |
| _FaceDiffuseRefine | Range(0,1) | 0.0 | 0 |
| _FaceDiffuseBoundary | Range(0.25,0.85) | 0.54 | 0.54 |
| _FaceDiffuseEdge | Range(0.015,0.12) | 0.045 | 0.045 |
| _FaceDiffuseSide | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseDepth | Range(0,1) | 0.9 | 0.9 |
| _FaceDiffuseTint | Color | [1.0, 0.84, 0.84, 1.0] | (1, 0.8399999, 0.8399999, 1) |
| _EyeRefineEnabled | Range(0,1) | 0.0 | 0 |
| _EyeIrisUpperDepth | Range(0,0.5) | 0.18 | 0.18 |
| _EyeIrisLowerLift | Range(0,0.4) | 0.1 | 0.1 |
| _EyeIrisEdgeDepth | Range(0,0.3) | 0.08 | 0.08 |
| _EyeCatchlightLift | Range(0,0.5) | 0.25 | 0.25 |
| _EyeScleraShade | Range(0,0.2) | 0.06 | 0.06 |
| _HairFaceShadowStrength | Range(0,1) | 0.0 | 0.75 |
| _HairFaceShadowBias | Range(0,0.01) | 0.0006 | 0.0006 |
| _HairFaceShadowFilter | Range(0,3) | 1.1 | 1.1 |
| _LineRefineEnabled | Float | 0.0 | 1 |
| _LineContourWidths | Vector | [0.82, 0.95, 0.6, 0.72] | (0.82, 0.95, 0.6, 0.72) |
| _LineContourTintMix | Range(0,1) | 0.55 | 0.55 |
| _LineInnerStrengths | Vector | [0.72, 0.76, 0.58, 0.72] | (0.72, 0.76, 0.58, 0.72) |
| _LineInnerFilter | Range(0,1) | 0.6 | 0.6 |
| _LineInnerTintMix | Range(0,1) | 0.45 | 0.45 |
| _LineHairInk | Color | [0.06, 0.032, 0.015, 1.0] | (0.06, 0.032, 0.015, 1) |
| _LineClothInk | Color | [0.023, 0.031, 0.042, 1.0] | (0.023, 0.031, 0.042, 1) |
| _LineSkinInk | Color | [0.1, 0.045, 0.027, 1.0] | (0.1, 0.045, 0.027, 1) |
| _LineMetalInk | Color | [0.04, 0.032, 0.022, 1.0] | (0.04, 0.032, 0.022, 1) |
| _FourMaterialSpecMask | 2D | black | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _FourMaterialSpecEnabled | Range(0,1) | 0.0 | 1 |
| _HairShineStrength | Range(0,0.5) | 0.12 | 0.12 |
| _HairShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _HairShineTint | Color | [1.0, 0.94, 0.78, 1.0] | (1, 0.94, 0.78, 1) |
| _ClothShineStrength | Range(0,0.2) | 0.035 | 0.035 |
| _ClothShinePower | Range(2,40) | 12.0 | 12 |
| _ClothShineTint | Color | [0.9, 0.95, 1.0, 1.0] | (0.9, 0.95, 1, 1) |
| _SkinShineStrength | Range(0,0.2) | 0.028 | 0.028 |
| _SkinShinePower | Range(4,80) | 28.0 | 28 |
| _SkinShineTint | Color | [1.0, 0.82, 0.68, 1.0] | (1, 0.82, 0.68, 1) |
| _MetalShineStrength | Range(0,1) | 0.38 | 0.38 |
| _MetalShineWidth | Range(0.02,0.3) | 0.1 | 0.1 |
| _MetalShineTint | Color | [1.0, 0.97, 0.9, 1.0] | (1, 0.97, 0.9, 1) |
| _MainTex | 2D | white | Assets/Bridget_Textures/BGT_base.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _ShadowMap | 2D | white | Assets/Bridget_Textures/BGT_Sss.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _LightMap | 2D | white | Assets/Bridget_Textures/BGT_ilm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _DetailMap | 2D | white | Assets/Bridget_Textures/BGT_detail.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _OutlineMap | 2D | black | Assets/Bridget_Textures/BGT_olm.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalMask | 2D | black | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _RegionalEnabled | Float | 0.0 | 0 |
| _RegionalHead | Float | 0.0 | 0 |
| _FaceFrameValid | Float | 0.0 | 0 |
| _FaceOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _FaceRightWS | Vector | [1.0, 0.0, 0.0, 0.083] | (1, 0, 0, 0.083) |
| _FaceSideStrength | Range(0,1) | 0.85 | 0.85 |
| _FaceShadeThreshold | Range(0,1) | 0.8 | 0.8 |
| _SkinShadeThreshold | Range(0,1) | 0.69 | 0.69 |
| _SleeveShadeThreshold | Range(0,1) | 0.68 | 0.68 |
| _RegionalSoftness | Range(0.001,0.08) | 0.018 | 0.018 |
| _FaceShadeStrength | Range(0,1) | 0.78 | 0.78 |
| _SkinShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _SleeveShadeStrength | Range(0,1) | 0.72 | 0.72 |
| _FaceShadeTint | Color | [1.0, 0.92, 0.91, 1.0] | (1, 0.92, 0.91, 1) |
| _SkinShadeTint | Color | [0.78, 0.49, 0.47, 1.0] | (0.78, 0.49, 0.47, 1) |
| _SleeveShadeTint | Color | [0.53, 0.62, 0.7, 1.0] | (0.53, 0.62, 0.7, 1) |
| _CullMode | Float | 2.0 | 2 |
| _UseMirroredUV | Float | 0.0 | 0 |
| _DepthOffsetFactor | Float | 0.0 | 0 |
| _DepthOffsetUnits | Float | 0.0 | 0 |
| _LightTreshold | Range(0,1) | 0.5 | 0.5 |
| _RampOffset | Range(-1,1) | 0.0 | 0 |
| _RampMaskCenter | Range(0,1) | 0.4980392 | 0.49803922 |
| _RampMaskStrength | Range(0,2) | 1.0 | 1 |
| _ShadowSoftness | Range(0,0.1) | 0.008 | 0.008 |
| _ShadowIntensity | Range(0,1) | 0.65 | 0.65 |
| _ShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (1, 1, 1, 1) |
| _SkinShadowOffset | Range(-0.5,0.5) | 0.06 | 0.06 |
| _SecondShadowThreshold | Range(-1,1) | 0.1 | 0.1 |
| _SecondShadowStrength | Range(0,1) | 0.0 | 0.9 |
| _SecondShadowTint | Color | [1.0, 1.0, 1.0, 1.0] | (0.55, 0.22, 0.28, 1) |
| _LowerRegionUpper | Range(0,1) | 0.52 | 0.52 |
| _LowerRegionFeather | Range(0.01,0.3) | 0.08 | 0.08 |
| _LowerLightBlend | Range(0,1) | 0.0 | 0.8 |
| _LowerLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, -0.4, 0) |
| _LowerLightDynamic | Range(0,1) | 0.0 | 1 |
| _LowerSkinColorGate | Range(0,1) | 1.0 | 1 |
| _TasteRatePow | Range(0.1,4) | 1.0 | 1 |
| _TasteHeightStart | Range(-1,2) | 0.0 | 0 |
| _TasteHeightEnd | Range(-1,2) | 0.65 | 0.65 |
| _TasteNormalWeight | Range(0,1) | 0.5 | 0.5 |
| _RegionLightBlend | Range(0,1) | 0.0 | 0 |
| _RegionLightDirection | Vector | [0.8, 0.5, 0.2, 0.0] | (0.8, 0.5, 0.2, 0) |
| _CharacterOriginWS | Vector | [0.0, 0.0, 0.0, 0.0] | (0, 0, 0, 0) |
| _CharacterHeight | Float | 1.65 | 1.65 |
| _LightIntensity | Range(0,2) | 0.9 | 0.9 |
| _AmbientStrength | Range(0,1) | 0.2 | 0.2 |
| _AOStrength | Range(0,1) | 1.0 | 1 |
| _DetailIntensity | Range(0,1) | 0.278 | 0 |
| _InnerLineStrength | Range(0,1) | 0.65 | 0.65 |
| _InnerLineColor | Color | [0.035, 0.028, 0.025, 1.0] | (0.035, 0.028, 0.025, 1) |
| _RimWidth | Range(0,1) | 0.16 | 0.16 |
| _RimIntensity | Range(0,1) | 0.16 | 0.16 |
| _SpecularPower | Range(1,100) | 24.0 | 15 |
| _SpecularIntensity | Range(0,2) | 0.12 | 0.12 |
| _LayerMaskStep | Range(0,255) | 60.0 | 60 |
| _BodySpecularWidth | Range(0,1) | 0.18 | 0.18 |
| _BodySpecularIntensity | Range(0,1) | 0.15 | 0.15 |
| _HeadSpecularWidth | Range(0,1) | 0.14 | 0.14 |
| _HeadSpecularIntensity | Range(0,1) | 0.22 | 0.22 |
| _HairLayerMin | Range(0,255) | 65.0 | 65 |
| _HairLayerMax | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMin | Range(0,255) | 90.0 | 90 |
| _LeatherLayerMax | Range(0,255) | 125.0 | 125 |
| _MetalLayerMin | Range(0,255) | 145.0 | 145 |
| _MetalLayerMax | Range(0,255) | 200.0 | 200 |
| _MetallicStepSpecularWidth | Range(0,1) | 0.2 | 0.2 |
| _MetallicStepSpecularIntensity | Range(0,1) | 0.25 | 0.25 |
| _ReceiveShadowStrength | Range(0,1) | 0.7 | 0.7 |
| _OutlineWidth | Range(0,4) | 0.8 | 0.8 |
| _UseSmoothOutline | Float | 0.0 | 1 |
| _OutlineSkinScale | Range(0,1) | 0.35 | 0.35 |
| _OutlineColor | Color | [0.04, 0.03, 0.025, 1.0] | (0.04, 0.03, 0.025, 1) |
| _OutlineMapStrength | Range(0,1) | 0.6 | 0.6 |
| _DebugMode | Range(0,24) | 0.0 | 0 |

## StageFloorReceiver

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _GeometryShadowFloor | Range(0,1) | 0.1 | 0.08 |
| _GeometryShadowBias | Range(0,0.02) | 0.001 | 0.0007 |
| _GeometryShadowFilter | Range(0,4) | 0.8 | 0.65 |
| _GeometryShadowFade | Range(0,0.5) | 0.08 | 0.12 |
| _Color | Color | [0.702, 0.702, 0.702, 1.0] | (0.74509805, 0.74509805, 0.74509805, 1) |
| _GradientStrength | Range(0, 1) | 0.134 | 0 |

## StageWallReceiver

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _GeometryShadowFloor | Range(0,1) | 0.1 | 0.1 |
| _GeometryShadowBias | Range(0,0.02) | 0.001 | 0.001 |
| _GeometryShadowFilter | Range(0,4) | 0.8 | 0.8 |
| _GeometryShadowFade | Range(0,0.5) | 0.08 | 0.08 |
| _Color | Color | [0.702, 0.702, 0.702, 1.0] | (0.7019608, 0.7019608, 0.7019608, 1) |
| _GradientStrength | Range(0, 1) | 0.134 | 0.31 |

## BodyDecal_Imitate

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _MainTex | 2D | gray | Assets/Bridget_Textures/BGT_decal.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _Strength | Range(0,1) | 1.0 | 1 |

## HeadDecal_Imitate

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _MainTex | 2D | gray | Assets/Bridget_Textures/BGT_decal.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _Strength | Range(0,1) | 1.0 | 1 |

## HeadGlow_Imitate

| 属性 | 类型 | Shader默认 | 材质设置 |
|---|---|---|---|
| _MainTex | 2D | white | Assets/Bridget_Textures/BGT_base.png；Tiling={'x': 1, 'y': 1}；Offset={'x': 0, 'y': 0} |
| _GlowMultiplier | Float | 2.0 | 2 |
