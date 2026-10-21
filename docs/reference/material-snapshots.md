# 12份材质保存原貌

来自 materials_saved.json，完整保留保存字段、历史冗余属性、纹理引用和未知Shader。793行声明属性账本只含10个可对应材质；不要把历史保存字段误当Shader当前仍读取的属性。StageShadowReceiver的shader=null，不能自动当作同名StageShadowReceiver Shader已解析。

## Base_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/Base_Imitate.mat",
  "shader": "Assets/GGST_Imitate/Shaders/BridgetToon.shader",
  "savedValues": {
    "_AOStrength": 1,
    "_AmbientStrength": 0.2,
    "_BodySpecularIntensity": 0.15,
    "_BodySpecularWidth": 0.18,
    "_BumpScale": 1,
    "_CharacterHeight": 1.65,
    "_CleanClothAOWeight": 0.25,
    "_CleanClothMaskWeight": 0.4,
    "_CleanClothSoftness": 0.018,
    "_CleanFaceUnderEnd": -0.45,
    "_CleanFaceUnderStart": -0.7,
    "_CleanShadeEnabled": 1,
    "_ClothShinePower": 12,
    "_ClothShineStrength": 0.035,
    "_CullMode": 2,
    "_Cutoff": 0.5,
    "_DebugMode": 0,
    "_DepthOffsetFactor": 0,
    "_DepthOffsetUnits": 0,
    "_DetailIntensity": 0.278,
    "_DetailNormalMapScale": 1,
    "_DstBlend": 0,
    "_EyeCatchlightLift": 0.25,
    "_EyeIrisEdgeDepth": 0.08,
    "_EyeIrisLowerLift": 0.1,
    "_EyeIrisUpperDepth": 0.18,
    "_EyeRefineEnabled": 1,
    "_EyeScleraShade": 0.06,
    "_FaceDiffuseBoundary": 0.54,
    "_FaceDiffuseDepth": 0.9,
    "_FaceDiffuseEdge": 0.045,
    "_FaceDiffuseRefine": 1,
    "_FaceDiffuseSide": 0.9,
    "_FaceFrameValid": 0,
    "_FaceShadeStrength": 0.78,
    "_FaceShadeThreshold": 0.8,
    "_FaceSideStrength": 0.85,
    "_FocusedCalfThreshold": 0.59,
    "_FocusedClothGain": 1.2,
    "_FocusedHairGain": 1.25,
    "_FocusedKneeThreshold": 0.62,
    "_FocusedMetalGain": 1.05,
    "_FocusedShadeEnabled": 1,
    "_FocusedSkinStrength": 0.14,
    "_FocusedSkinWidth": 0.22,
    "_FocusedSpecEnabled": 1,
    "_FocusedThighThreshold": 0.57,
    "_FocusedTunicThreshold": 0.4,
    "_FourMaterialSpecEnabled": 1,
    "_GlossMapScale": 1,
    "_Glossiness": 0.5,
    "_GlossyReflections": 1,
    "_HairFaceShadowBias": 0.0006,
    "_HairFaceShadowFilter": 1.1,
    "_HairFaceShadowStrength": 0,
    "_HairLayerMax": 90,
    "_HairLayerMin": 65,
    "_HairShineStrength": 0.12,
    "_HairShineWidth": 0.1,
    "_HeadSpecularIntensity": 0.22,
    "_HeadSpecularWidth": 0.14,
    "_InnerLineStrength": 0.65,
    "_LayerMaskStep": 60,
    "_LeatherLayerMax": 125,
    "_LeatherLayerMin": 90,
    "_LightIntensity": 0.9,
    "_LightTreshold": 0.5,
    "_LineContourTintMix": 0.55,
    "_LineInnerFilter": 0.6,
    "_LineInnerTintMix": 0.45,
    "_LineRefineEnabled": 1,
    "_LowerLightBlend": 0.8,
    "_LowerLightDynamic": 1,
    "_LowerRegionFeather": 0.08,
    "_LowerRegionUpper": 0.52,
    "_LowerSkinColorGate": 1,
    "_MetalLayerMax": 200,
    "_MetalLayerMin": 145,
    "_MetalShineStrength": 0.38,
    "_MetalShineWidth": 0.1,
    "_Metallic": 0,
    "_MetallicStepSpecularIntensity": 0.25,
    "_MetallicStepSpecularWidth": 0.2,
    "_Mode": 0,
    "_OcclusionStrength": 1,
    "_OutlineMapStrength": 0.6,
    "_OutlineSkinScale": 0.35,
    "_OutlineWidth": 0.8,
    "_PaletteEnabled": 1,
    "_Parallax": 0.02,
    "_RampMaskCenter": 0.49803922,
    "_RampMaskStrength": 1,
    "_RampOffset": 0,
    "_ReceiveShadowStrength": 0.7,
    "_ReferenceRimEnabled": 1,
    "_ReferenceRimFaceScale": 0.15,
    "_ReferenceRimShadowFloor": 0.55,
    "_ReferenceRimStrength": 0.5,
    "_ReferenceRimTintMix": 0.75,
    "_ReferenceRimWidth": 0.24,
    "_RegionLightBlend": 0,
    "_RegionalEnabled": 0,
    "_RegionalHead": 0,
    "_RegionalSoftness": 0.018,
    "_RimIntensity": 0.16,
    "_RimWidth": 0.16,
    "_SecondShadowStrength": 0.9,
    "_SecondShadowThreshold": 0.1,
    "_ShadowIntensity": 0.65,
    "_ShadowSoftness": 0.008,
    "_SkinShadeStrength": 0.72,
    "_SkinShadeThreshold": 0.69,
    "_SkinShadowOffset": 0.06,
    "_SkinShinePower": 28,
    "_SkinShineStrength": 0.028,
    "_SleeveShadeStrength": 0.72,
    "_SleeveShadeThreshold": 0.68,
    "_SmoothnessTextureChannel": 0,
    "_SpecularHighlights": 1,
    "_SpecularIntensity": 0.12,
    "_SpecularPower": 15,
    "_SrcBlend": 1,
    "_TasteHeightEnd": 0.65,
    "_TasteHeightStart": 0,
    "_TasteNormalWeight": 0.5,
    "_TasteRatePow": 1,
    "_ThighLobeEnabled": 1,
    "_ThighLobeStrength": 0.16,
    "_UVSec": 0,
    "_UseMirroredUV": 0,
    "_UseSmoothOutline": 1,
    "_ZWrite": 1,
    "_CharacterOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_ClothShineTint": {
      "r": 0.9,
      "g": 0.95,
      "b": 1,
      "a": 1
    },
    "_Color": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_EmissionColor": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 1
    },
    "_FaceDiffuseTint": {
      "r": 1,
      "g": 0.84,
      "b": 0.84,
      "a": 1
    },
    "_FaceOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_FaceRightWS": {
      "r": 1,
      "g": 0,
      "b": 0,
      "a": 0.083
    },
    "_FaceShadeTint": {
      "r": 1,
      "g": 0.92,
      "b": 0.91,
      "a": 1
    },
    "_HairShineTint": {
      "r": 1,
      "g": 0.94,
      "b": 0.78,
      "a": 1
    },
    "_InnerLineColor": {
      "r": 0.035,
      "g": 0.028,
      "b": 0.025,
      "a": 1
    },
    "_LineClothInk": {
      "r": 0.023,
      "g": 0.031,
      "b": 0.042,
      "a": 1
    },
    "_LineContourWidths": {
      "r": 0.82,
      "g": 0.95,
      "b": 0.6,
      "a": 0.72
    },
    "_LineHairInk": {
      "r": 0.06,
      "g": 0.032,
      "b": 0.015,
      "a": 1
    },
    "_LineInnerStrengths": {
      "r": 0.72,
      "g": 0.76,
      "b": 0.58,
      "a": 0.72
    },
    "_LineMetalInk": {
      "r": 0.04,
      "g": 0.032,
      "b": 0.022,
      "a": 1
    },
    "_LineSkinInk": {
      "r": 0.1,
      "g": 0.045,
      "b": 0.027,
      "a": 1
    },
    "_LowerLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": -0.4,
      "a": 0
    },
    "_MetalShineTint": {
      "r": 1,
      "g": 0.97,
      "b": 0.9,
      "a": 1
    },
    "_OutlineColor": {
      "r": 0.04,
      "g": 0.03,
      "b": 0.025,
      "a": 1
    },
    "_PaletteSkinDark": {
      "r": 0.82,
      "g": 0.7,
      "b": 0.82,
      "a": 0
    },
    "_PaletteSkinLight": {
      "r": 0.92,
      "g": 1.1,
      "b": 1.28,
      "a": 0
    },
    "_PaletteSleeveDark": {
      "r": 0.9,
      "g": 0.93,
      "b": 1.02,
      "a": 0
    },
    "_PaletteSleeveLight": {
      "r": 0.99,
      "g": 1,
      "b": 1.07,
      "a": 0
    },
    "_PaletteTunicDark": {
      "r": 1.03,
      "g": 1.06,
      "b": 1.19,
      "a": 0
    },
    "_PaletteTunicLight": {
      "r": 1,
      "g": 1.08,
      "b": 1.23,
      "a": 0
    },
    "_ReferenceRimMaterial": {
      "r": 1,
      "g": 0.9,
      "b": 0.65,
      "a": 0.6
    },
    "_ReferenceRimTint": {
      "r": 0.94,
      "g": 0.97,
      "b": 1,
      "a": 1
    },
    "_RegionLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": 0.2,
      "a": 0
    },
    "_SecondShadowTint": {
      "r": 0.55,
      "g": 0.22,
      "b": 0.28,
      "a": 1
    },
    "_ShadowTint": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_SkinShadeTint": {
      "r": 0.78,
      "g": 0.49,
      "b": 0.47,
      "a": 1
    },
    "_SkinShineTint": {
      "r": 1,
      "g": 0.82,
      "b": 0.68,
      "a": 1
    },
    "_SleeveShadeTint": {
      "r": 0.53,
      "g": 0.62,
      "b": 0.7,
      "a": 1
    },
    "_ThighLobeTint": {
      "r": 0.92,
      "g": 1,
      "b": 0.45,
      "a": 1
    }
  },
  "textures": {
    "_BumpMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailAlbedoMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMap": {
      "path": "Assets/Bridget_Textures/BGT_detail.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMask": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailNormalMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_EmissionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_FourMaterialSpecMask": {
      "path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_LightMap": {
      "path": "Assets/Bridget_Textures/BGT_ilm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGT_base.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MetallicGlossMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OcclusionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OutlineMap": {
      "path": "Assets/Bridget_Textures/BGT_olm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ParallaxMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_RegionalMask": {
      "path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ShadowMap": {
      "path": "Assets/Bridget_Textures/BGT_Sss.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## BaseSecondary_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/BaseSecondary_Imitate.mat",
  "shader": "Assets/GGST_Imitate/Shaders/BridgetToon.shader",
  "savedValues": {
    "_AOStrength": 1,
    "_AmbientStrength": 0.2,
    "_BodySpecularIntensity": 0.15,
    "_BodySpecularWidth": 0.18,
    "_BumpScale": 1,
    "_CharacterHeight": 1.65,
    "_CleanClothAOWeight": 0.25,
    "_CleanClothMaskWeight": 0.4,
    "_CleanClothSoftness": 0.018,
    "_CleanFaceUnderEnd": -0.45,
    "_CleanFaceUnderStart": -0.7,
    "_CleanShadeEnabled": 1,
    "_ClothShinePower": 12,
    "_ClothShineStrength": 0.035,
    "_CullMode": 2,
    "_Cutoff": 0.5,
    "_DebugMode": 0,
    "_DepthOffsetFactor": 0,
    "_DepthOffsetUnits": 0,
    "_DetailIntensity": 0.278,
    "_DetailNormalMapScale": 1,
    "_DstBlend": 0,
    "_EyeCatchlightLift": 0.25,
    "_EyeIrisEdgeDepth": 0.08,
    "_EyeIrisLowerLift": 0.1,
    "_EyeIrisUpperDepth": 0.18,
    "_EyeRefineEnabled": 1,
    "_EyeScleraShade": 0.06,
    "_FaceDiffuseBoundary": 0.54,
    "_FaceDiffuseDepth": 0.9,
    "_FaceDiffuseEdge": 0.045,
    "_FaceDiffuseRefine": 1,
    "_FaceDiffuseSide": 0.9,
    "_FaceFrameValid": 0,
    "_FaceShadeStrength": 0.78,
    "_FaceShadeThreshold": 0.8,
    "_FaceSideStrength": 0.85,
    "_FocusedCalfThreshold": 0.59,
    "_FocusedClothGain": 1.2,
    "_FocusedHairGain": 1.25,
    "_FocusedKneeThreshold": 0.62,
    "_FocusedMetalGain": 1.05,
    "_FocusedShadeEnabled": 1,
    "_FocusedSkinStrength": 0.14,
    "_FocusedSkinWidth": 0.22,
    "_FocusedSpecEnabled": 1,
    "_FocusedThighThreshold": 0.57,
    "_FocusedTunicThreshold": 0.4,
    "_FourMaterialSpecEnabled": 1,
    "_GlossMapScale": 1,
    "_Glossiness": 0.5,
    "_GlossyReflections": 1,
    "_HairFaceShadowBias": 0.0006,
    "_HairFaceShadowFilter": 1.1,
    "_HairFaceShadowStrength": 0,
    "_HairLayerMax": 90,
    "_HairLayerMin": 65,
    "_HairShineStrength": 0.12,
    "_HairShineWidth": 0.1,
    "_HeadSpecularIntensity": 0.22,
    "_HeadSpecularWidth": 0.14,
    "_InnerLineStrength": 0.65,
    "_LayerMaskStep": 60,
    "_LeatherLayerMax": 125,
    "_LeatherLayerMin": 90,
    "_LightIntensity": 0.9,
    "_LightTreshold": 0.5,
    "_LineContourTintMix": 0.55,
    "_LineInnerFilter": 0.6,
    "_LineInnerTintMix": 0.45,
    "_LineRefineEnabled": 1,
    "_LowerLightBlend": 0.8,
    "_LowerLightDynamic": 1,
    "_LowerRegionFeather": 0.08,
    "_LowerRegionUpper": 0.52,
    "_LowerSkinColorGate": 1,
    "_MetalLayerMax": 200,
    "_MetalLayerMin": 145,
    "_MetalShineStrength": 0.38,
    "_MetalShineWidth": 0.1,
    "_Metallic": 0,
    "_MetallicStepSpecularIntensity": 0.25,
    "_MetallicStepSpecularWidth": 0.2,
    "_Mode": 0,
    "_OcclusionStrength": 1,
    "_OutlineMapStrength": 0.6,
    "_OutlineSkinScale": 0.35,
    "_OutlineWidth": 0.8,
    "_PaletteEnabled": 1,
    "_Parallax": 0.02,
    "_RampMaskCenter": 0.49803922,
    "_RampMaskStrength": 1,
    "_RampOffset": 0,
    "_ReceiveShadowStrength": 0.7,
    "_ReferenceRimEnabled": 1,
    "_ReferenceRimFaceScale": 0.15,
    "_ReferenceRimShadowFloor": 0.55,
    "_ReferenceRimStrength": 0.5,
    "_ReferenceRimTintMix": 0.75,
    "_ReferenceRimWidth": 0.24,
    "_RegionLightBlend": 0,
    "_RegionalEnabled": 0,
    "_RegionalHead": 0,
    "_RegionalSoftness": 0.018,
    "_RimIntensity": 0.16,
    "_RimWidth": 0.16,
    "_SecondShadowStrength": 0.9,
    "_SecondShadowThreshold": 0.1,
    "_ShadowIntensity": 0.65,
    "_ShadowSoftness": 0.008,
    "_SkinShadeStrength": 0.72,
    "_SkinShadeThreshold": 0.69,
    "_SkinShadowOffset": 0.06,
    "_SkinShinePower": 28,
    "_SkinShineStrength": 0.028,
    "_SleeveShadeStrength": 0.72,
    "_SleeveShadeThreshold": 0.68,
    "_SmoothnessTextureChannel": 0,
    "_SpecularHighlights": 1,
    "_SpecularIntensity": 0.12,
    "_SpecularPower": 15,
    "_SrcBlend": 1,
    "_TasteHeightEnd": 0.65,
    "_TasteHeightStart": 0,
    "_TasteNormalWeight": 0.5,
    "_TasteRatePow": 1,
    "_ThighLobeEnabled": 1,
    "_ThighLobeStrength": 0.16,
    "_UVSec": 0,
    "_UseMirroredUV": 0,
    "_UseSmoothOutline": 1,
    "_ZWrite": 1,
    "_CharacterOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_ClothShineTint": {
      "r": 0.9,
      "g": 0.95,
      "b": 1,
      "a": 1
    },
    "_Color": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_EmissionColor": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 1
    },
    "_FaceDiffuseTint": {
      "r": 1,
      "g": 0.84,
      "b": 0.84,
      "a": 1
    },
    "_FaceOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_FaceRightWS": {
      "r": 1,
      "g": 0,
      "b": 0,
      "a": 0.083
    },
    "_FaceShadeTint": {
      "r": 1,
      "g": 0.92,
      "b": 0.91,
      "a": 1
    },
    "_HairShineTint": {
      "r": 1,
      "g": 0.94,
      "b": 0.78,
      "a": 1
    },
    "_InnerLineColor": {
      "r": 0.035,
      "g": 0.028,
      "b": 0.025,
      "a": 1
    },
    "_LineClothInk": {
      "r": 0.023,
      "g": 0.031,
      "b": 0.042,
      "a": 1
    },
    "_LineContourWidths": {
      "r": 0.82,
      "g": 0.95,
      "b": 0.6,
      "a": 0.72
    },
    "_LineHairInk": {
      "r": 0.06,
      "g": 0.032,
      "b": 0.015,
      "a": 1
    },
    "_LineInnerStrengths": {
      "r": 0.72,
      "g": 0.76,
      "b": 0.58,
      "a": 0.72
    },
    "_LineMetalInk": {
      "r": 0.04,
      "g": 0.032,
      "b": 0.022,
      "a": 1
    },
    "_LineSkinInk": {
      "r": 0.1,
      "g": 0.045,
      "b": 0.027,
      "a": 1
    },
    "_LowerLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": -0.4,
      "a": 0
    },
    "_MetalShineTint": {
      "r": 1,
      "g": 0.97,
      "b": 0.9,
      "a": 1
    },
    "_OutlineColor": {
      "r": 0.04,
      "g": 0.03,
      "b": 0.025,
      "a": 1
    },
    "_PaletteSkinDark": {
      "r": 0.82,
      "g": 0.7,
      "b": 0.82,
      "a": 0
    },
    "_PaletteSkinLight": {
      "r": 0.92,
      "g": 1.1,
      "b": 1.28,
      "a": 0
    },
    "_PaletteSleeveDark": {
      "r": 0.9,
      "g": 0.93,
      "b": 1.02,
      "a": 0
    },
    "_PaletteSleeveLight": {
      "r": 0.99,
      "g": 1,
      "b": 1.07,
      "a": 0
    },
    "_PaletteTunicDark": {
      "r": 1.03,
      "g": 1.06,
      "b": 1.19,
      "a": 0
    },
    "_PaletteTunicLight": {
      "r": 1,
      "g": 1.08,
      "b": 1.23,
      "a": 0
    },
    "_ReferenceRimMaterial": {
      "r": 1,
      "g": 0.9,
      "b": 0.65,
      "a": 0.6
    },
    "_ReferenceRimTint": {
      "r": 0.94,
      "g": 0.97,
      "b": 1,
      "a": 1
    },
    "_RegionLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": 0.2,
      "a": 0
    },
    "_SecondShadowTint": {
      "r": 0.55,
      "g": 0.22,
      "b": 0.28,
      "a": 1
    },
    "_ShadowTint": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_SkinShadeTint": {
      "r": 0.78,
      "g": 0.49,
      "b": 0.47,
      "a": 1
    },
    "_SkinShineTint": {
      "r": 1,
      "g": 0.82,
      "b": 0.68,
      "a": 1
    },
    "_SleeveShadeTint": {
      "r": 0.53,
      "g": 0.62,
      "b": 0.7,
      "a": 1
    },
    "_ThighLobeTint": {
      "r": 0.92,
      "g": 1,
      "b": 0.45,
      "a": 1
    }
  },
  "textures": {
    "_BumpMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailAlbedoMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMap": {
      "path": "Assets/Bridget_Textures/BGT_detail.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMask": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailNormalMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_EmissionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_FourMaterialSpecMask": {
      "path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_LightMap": {
      "path": "Assets/Bridget_Textures/BGT_ilm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGT_base.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MetallicGlossMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OcclusionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OutlineMap": {
      "path": "Assets/Bridget_Textures/BGT_olm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ParallaxMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_RegionalMask": {
      "path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ShadowMap": {
      "path": "Assets/Bridget_Textures/BGT_Sss.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## BodyBaseFlip_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/BodyBaseFlip_Imitate.mat",
  "shader": "Assets/GGST_Imitate/Shaders/BridgetToon.shader",
  "savedValues": {
    "_AOStrength": 1,
    "_AmbientStrength": 0.2,
    "_BodySpecularIntensity": 0.15,
    "_BodySpecularWidth": 0.18,
    "_BumpScale": 1,
    "_CharacterHeight": 1.65,
    "_CleanClothAOWeight": 0.25,
    "_CleanClothMaskWeight": 0.4,
    "_CleanClothSoftness": 0.018,
    "_CleanFaceUnderEnd": -0.45,
    "_CleanFaceUnderStart": -0.7,
    "_CleanShadeEnabled": 1,
    "_ClothShinePower": 12,
    "_ClothShineStrength": 0.035,
    "_CullMode": 2,
    "_Cutoff": 0.5,
    "_DebugMode": 0,
    "_DepthOffsetFactor": 0,
    "_DepthOffsetUnits": 0,
    "_DetailIntensity": 0.278,
    "_DetailNormalMapScale": 1,
    "_DstBlend": 0,
    "_EyeCatchlightLift": 0.25,
    "_EyeIrisEdgeDepth": 0.08,
    "_EyeIrisLowerLift": 0.1,
    "_EyeIrisUpperDepth": 0.18,
    "_EyeRefineEnabled": 0,
    "_EyeScleraShade": 0.06,
    "_FaceDiffuseBoundary": 0.54,
    "_FaceDiffuseDepth": 0.9,
    "_FaceDiffuseEdge": 0.045,
    "_FaceDiffuseRefine": 0,
    "_FaceDiffuseSide": 0.9,
    "_FaceFrameValid": 0,
    "_FaceShadeStrength": 0.78,
    "_FaceShadeThreshold": 0.8,
    "_FaceSideStrength": 0.85,
    "_FocusedCalfThreshold": 0.59,
    "_FocusedClothGain": 1.2,
    "_FocusedHairGain": 1.25,
    "_FocusedKneeThreshold": 0.62,
    "_FocusedMetalGain": 1.05,
    "_FocusedShadeEnabled": 1,
    "_FocusedSkinStrength": 0.14,
    "_FocusedSkinWidth": 0.22,
    "_FocusedSpecEnabled": 1,
    "_FocusedThighThreshold": 0.57,
    "_FocusedTunicThreshold": 0.4,
    "_FourMaterialSpecEnabled": 1,
    "_GlossMapScale": 1,
    "_Glossiness": 0.5,
    "_GlossyReflections": 1,
    "_HairFaceShadowBias": 0.0006,
    "_HairFaceShadowFilter": 1.1,
    "_HairFaceShadowStrength": 0.75,
    "_HairLayerMax": 90,
    "_HairLayerMin": 65,
    "_HairShineStrength": 0.12,
    "_HairShineWidth": 0.1,
    "_HeadSpecularIntensity": 0.22,
    "_HeadSpecularWidth": 0.14,
    "_InnerLineStrength": 0.65,
    "_LayerMaskStep": 60,
    "_LeatherLayerMax": 125,
    "_LeatherLayerMin": 90,
    "_LightIntensity": 0.9,
    "_LightTreshold": 0.624,
    "_LineContourTintMix": 0.55,
    "_LineInnerFilter": 0.6,
    "_LineInnerTintMix": 0.45,
    "_LineRefineEnabled": 1,
    "_LowerLightBlend": 0.8,
    "_LowerLightDynamic": 1,
    "_LowerRegionFeather": 0.08,
    "_LowerRegionUpper": 0.52,
    "_LowerSkinColorGate": 1,
    "_MetalLayerMax": 200,
    "_MetalLayerMin": 145,
    "_MetalShineStrength": 0.38,
    "_MetalShineWidth": 0.1,
    "_Metallic": 0,
    "_MetallicStepSpecularIntensity": 0.25,
    "_MetallicStepSpecularWidth": 0.2,
    "_Mode": 0,
    "_OcclusionStrength": 1,
    "_OutlineMapStrength": 0.6,
    "_OutlineSkinScale": 0.35,
    "_OutlineWidth": 0,
    "_PaletteEnabled": 1,
    "_Parallax": 0.02,
    "_RampMaskCenter": 0.49803922,
    "_RampMaskStrength": 1,
    "_RampOffset": 0,
    "_ReceiveShadowStrength": 0.7,
    "_ReferenceRimEnabled": 1,
    "_ReferenceRimFaceScale": 0.15,
    "_ReferenceRimShadowFloor": 0.55,
    "_ReferenceRimStrength": 0.5,
    "_ReferenceRimTintMix": 0.75,
    "_ReferenceRimWidth": 0.24,
    "_RegionLightBlend": 0,
    "_RegionalEnabled": 0,
    "_RegionalHead": 0,
    "_RegionalSoftness": 0.018,
    "_RimIntensity": 0.16,
    "_RimWidth": 0.16,
    "_SecondShadowStrength": 0.9,
    "_SecondShadowThreshold": 0.1,
    "_ShadowIntensity": 0.65,
    "_ShadowSoftness": 0.008,
    "_SkinShadeStrength": 0.72,
    "_SkinShadeThreshold": 0.69,
    "_SkinShadowOffset": 0.06,
    "_SkinShinePower": 28,
    "_SkinShineStrength": 0.028,
    "_SleeveShadeStrength": 0.72,
    "_SleeveShadeThreshold": 0.68,
    "_SmoothnessTextureChannel": 0,
    "_SpecularHighlights": 1,
    "_SpecularIntensity": 0.12,
    "_SpecularPower": 15,
    "_SrcBlend": 1,
    "_TasteHeightEnd": 0.65,
    "_TasteHeightStart": 0,
    "_TasteNormalWeight": 0.5,
    "_TasteRatePow": 1,
    "_ThighLobeEnabled": 1,
    "_ThighLobeStrength": 0.16,
    "_UVSec": 0,
    "_UseMirroredUV": 0,
    "_UseSmoothOutline": 1,
    "_ZWrite": 1,
    "_CharacterOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_ClothShineTint": {
      "r": 0.9,
      "g": 0.95,
      "b": 1,
      "a": 1
    },
    "_Color": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_EmissionColor": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 1
    },
    "_FaceDiffuseTint": {
      "r": 1,
      "g": 0.8399999,
      "b": 0.8399999,
      "a": 1
    },
    "_FaceOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_FaceRightWS": {
      "r": 1,
      "g": 0,
      "b": 0,
      "a": 0.083
    },
    "_FaceShadeTint": {
      "r": 1,
      "g": 0.92,
      "b": 0.91,
      "a": 1
    },
    "_HairShineTint": {
      "r": 1,
      "g": 0.94,
      "b": 0.78,
      "a": 1
    },
    "_InnerLineColor": {
      "r": 0.035,
      "g": 0.028,
      "b": 0.025,
      "a": 1
    },
    "_LineClothInk": {
      "r": 0.023,
      "g": 0.031,
      "b": 0.042,
      "a": 1
    },
    "_LineContourWidths": {
      "r": 0.82,
      "g": 0.95,
      "b": 0.6,
      "a": 0.72
    },
    "_LineHairInk": {
      "r": 0.06,
      "g": 0.032,
      "b": 0.015,
      "a": 1
    },
    "_LineInnerStrengths": {
      "r": 0.72,
      "g": 0.76,
      "b": 0.58,
      "a": 0.72
    },
    "_LineMetalInk": {
      "r": 0.04,
      "g": 0.032,
      "b": 0.022,
      "a": 1
    },
    "_LineSkinInk": {
      "r": 0.1,
      "g": 0.045,
      "b": 0.027,
      "a": 1
    },
    "_LowerLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": -0.4,
      "a": 0
    },
    "_MetalShineTint": {
      "r": 1,
      "g": 0.97,
      "b": 0.9,
      "a": 1
    },
    "_OutlineColor": {
      "r": 0.04,
      "g": 0.03,
      "b": 0.025,
      "a": 1
    },
    "_PaletteSkinDark": {
      "r": 0.82,
      "g": 0.7,
      "b": 0.82,
      "a": 0
    },
    "_PaletteSkinLight": {
      "r": 0.92,
      "g": 1.1,
      "b": 1.28,
      "a": 0
    },
    "_PaletteSleeveDark": {
      "r": 0.9,
      "g": 0.93,
      "b": 1.02,
      "a": 0
    },
    "_PaletteSleeveLight": {
      "r": 0.99,
      "g": 1,
      "b": 1.07,
      "a": 0
    },
    "_PaletteTunicDark": {
      "r": 1.03,
      "g": 1.06,
      "b": 1.19,
      "a": 0
    },
    "_PaletteTunicLight": {
      "r": 1,
      "g": 1.08,
      "b": 1.23,
      "a": 0
    },
    "_ReferenceRimMaterial": {
      "r": 1,
      "g": 0.9,
      "b": 0.65,
      "a": 0.6
    },
    "_ReferenceRimTint": {
      "r": 0.94,
      "g": 0.97,
      "b": 1,
      "a": 1
    },
    "_RegionLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": 0.2,
      "a": 0
    },
    "_SecondShadowTint": {
      "r": 0.55,
      "g": 0.22,
      "b": 0.28,
      "a": 1
    },
    "_ShadowTint": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_SkinShadeTint": {
      "r": 0.78,
      "g": 0.49,
      "b": 0.47,
      "a": 1
    },
    "_SkinShineTint": {
      "r": 1,
      "g": 0.82,
      "b": 0.68,
      "a": 1
    },
    "_SleeveShadeTint": {
      "r": 0.53,
      "g": 0.62,
      "b": 0.7,
      "a": 1
    },
    "_ThighLobeTint": {
      "r": 0.92,
      "g": 1,
      "b": 0.45,
      "a": 1
    }
  },
  "textures": {
    "_BumpMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailAlbedoMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMap": {
      "path": "Assets/Bridget_Textures/BGT_detail.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMask": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailNormalMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_EmissionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_FourMaterialSpecMask": {
      "path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_LightMap": {
      "path": "Assets/Bridget_Textures/BGT_ilm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGT_base.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MetallicGlossMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OcclusionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OutlineMap": {
      "path": "Assets/Bridget_Textures/BGT_olm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ParallaxMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_RegionalMask": {
      "path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ShadowMap": {
      "path": "Assets/Bridget_Textures/BGT_Sss.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## BodyDecal_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/BodyDecal_Imitate.mat",
  "shader": "Assets/GGST_RenderFix/GgstDecal.shader",
  "savedValues": {
    "_Strength": 1
  },
  "textures": {
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGT_decal.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## CoatExterior_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/CoatExterior_Imitate.mat",
  "shader": "Assets/GGST_Imitate/Shaders/BridgetToon.shader",
  "savedValues": {
    "_AOStrength": 1,
    "_AmbientStrength": 0.2,
    "_BodySpecularIntensity": 0.15,
    "_BodySpecularWidth": 0.18,
    "_BumpScale": 1,
    "_CharacterHeight": 1.65,
    "_CleanClothAOWeight": 0.25,
    "_CleanClothMaskWeight": 0.4,
    "_CleanClothSoftness": 0.018,
    "_CleanFaceUnderEnd": -0.45,
    "_CleanFaceUnderStart": -0.7,
    "_CleanShadeEnabled": 1,
    "_ClothShinePower": 12,
    "_ClothShineStrength": 0.035,
    "_CullMode": 2,
    "_Cutoff": 0.5,
    "_DebugMode": 0,
    "_DepthOffsetFactor": 0,
    "_DepthOffsetUnits": 0,
    "_DetailIntensity": 0,
    "_DetailNormalMapScale": 1,
    "_DstBlend": 0,
    "_EyeCatchlightLift": 0.25,
    "_EyeIrisEdgeDepth": 0.08,
    "_EyeIrisLowerLift": 0.1,
    "_EyeIrisUpperDepth": 0.18,
    "_EyeRefineEnabled": 0,
    "_EyeScleraShade": 0.06,
    "_FaceDiffuseBoundary": 0.54,
    "_FaceDiffuseDepth": 0.9,
    "_FaceDiffuseEdge": 0.045,
    "_FaceDiffuseRefine": 0,
    "_FaceDiffuseSide": 0.9,
    "_FaceFrameValid": 0,
    "_FaceShadeStrength": 0.78,
    "_FaceShadeThreshold": 0.8,
    "_FaceSideStrength": 0.85,
    "_FocusedCalfThreshold": 0.59,
    "_FocusedClothGain": 1.2,
    "_FocusedHairGain": 1.25,
    "_FocusedKneeThreshold": 0.62,
    "_FocusedMetalGain": 1.05,
    "_FocusedShadeEnabled": 1,
    "_FocusedSkinStrength": 0.14,
    "_FocusedSkinWidth": 0.22,
    "_FocusedSpecEnabled": 1,
    "_FocusedThighThreshold": 0.57,
    "_FocusedTunicThreshold": 0.4,
    "_FourMaterialSpecEnabled": 1,
    "_GlossMapScale": 1,
    "_Glossiness": 0.5,
    "_GlossyReflections": 1,
    "_HairFaceShadowBias": 0.0006,
    "_HairFaceShadowFilter": 1.1,
    "_HairFaceShadowStrength": 0.75,
    "_HairLayerMax": 90,
    "_HairLayerMin": 65,
    "_HairShineStrength": 0.12,
    "_HairShineWidth": 0.1,
    "_HeadSpecularIntensity": 0.22,
    "_HeadSpecularWidth": 0.14,
    "_InnerLineStrength": 0.65,
    "_LayerMaskStep": 60,
    "_LeatherLayerMax": 125,
    "_LeatherLayerMin": 90,
    "_LightIntensity": 0.9,
    "_LightTreshold": 0.5,
    "_LineContourTintMix": 0.55,
    "_LineInnerFilter": 0.6,
    "_LineInnerTintMix": 0.45,
    "_LineRefineEnabled": 1,
    "_LowerLightBlend": 0.8,
    "_LowerLightDynamic": 1,
    "_LowerRegionFeather": 0.08,
    "_LowerRegionUpper": 0.52,
    "_LowerSkinColorGate": 1,
    "_MetalLayerMax": 200,
    "_MetalLayerMin": 145,
    "_MetalShineStrength": 0.38,
    "_MetalShineWidth": 0.1,
    "_Metallic": 0,
    "_MetallicStepSpecularIntensity": 0.25,
    "_MetallicStepSpecularWidth": 0.2,
    "_Mode": 0,
    "_OcclusionStrength": 1,
    "_OutlineMapStrength": 0.6,
    "_OutlineSkinScale": 0.35,
    "_OutlineWidth": 0.8,
    "_PaletteEnabled": 1,
    "_Parallax": 0.02,
    "_RampMaskCenter": 0.49803922,
    "_RampMaskStrength": 1,
    "_RampOffset": 0,
    "_ReceiveShadowStrength": 0.7,
    "_ReferenceRimEnabled": 1,
    "_ReferenceRimFaceScale": 0.15,
    "_ReferenceRimShadowFloor": 0.55,
    "_ReferenceRimStrength": 0.5,
    "_ReferenceRimTintMix": 0.75,
    "_ReferenceRimWidth": 0.24,
    "_RegionLightBlend": 0,
    "_RegionalEnabled": 0,
    "_RegionalHead": 0,
    "_RegionalSoftness": 0.018,
    "_RimIntensity": 0.16,
    "_RimWidth": 0.16,
    "_SecondShadowStrength": 0.9,
    "_SecondShadowThreshold": 0.1,
    "_ShadowIntensity": 0.65,
    "_ShadowSoftness": 0.008,
    "_SkinShadeStrength": 0.72,
    "_SkinShadeThreshold": 0.69,
    "_SkinShadowOffset": 0.06,
    "_SkinShinePower": 28,
    "_SkinShineStrength": 0.028,
    "_SleeveShadeStrength": 0.72,
    "_SleeveShadeThreshold": 0.68,
    "_SmoothnessTextureChannel": 0,
    "_SpecularHighlights": 1,
    "_SpecularIntensity": 0.12,
    "_SpecularPower": 15,
    "_SrcBlend": 1,
    "_TasteHeightEnd": 0.65,
    "_TasteHeightStart": 0,
    "_TasteNormalWeight": 0.5,
    "_TasteRatePow": 1,
    "_ThighLobeEnabled": 1,
    "_ThighLobeStrength": 0.16,
    "_UVSec": 0,
    "_UseMirroredUV": 0,
    "_UseSmoothOutline": 1,
    "_ZWrite": 1,
    "_CharacterOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_ClothShineTint": {
      "r": 0.9,
      "g": 0.95,
      "b": 1,
      "a": 1
    },
    "_Color": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_EmissionColor": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 1
    },
    "_FaceDiffuseTint": {
      "r": 1,
      "g": 0.8399999,
      "b": 0.8399999,
      "a": 1
    },
    "_FaceOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_FaceRightWS": {
      "r": 1,
      "g": 0,
      "b": 0,
      "a": 0.083
    },
    "_FaceShadeTint": {
      "r": 1,
      "g": 0.92,
      "b": 0.91,
      "a": 1
    },
    "_HairShineTint": {
      "r": 1,
      "g": 0.94,
      "b": 0.78,
      "a": 1
    },
    "_InnerLineColor": {
      "r": 0.035,
      "g": 0.028,
      "b": 0.025,
      "a": 1
    },
    "_LineClothInk": {
      "r": 0.023,
      "g": 0.031,
      "b": 0.042,
      "a": 1
    },
    "_LineContourWidths": {
      "r": 0.82,
      "g": 0.95,
      "b": 0.6,
      "a": 0.72
    },
    "_LineHairInk": {
      "r": 0.06,
      "g": 0.032,
      "b": 0.015,
      "a": 1
    },
    "_LineInnerStrengths": {
      "r": 0.72,
      "g": 0.76,
      "b": 0.58,
      "a": 0.72
    },
    "_LineMetalInk": {
      "r": 0.04,
      "g": 0.032,
      "b": 0.022,
      "a": 1
    },
    "_LineSkinInk": {
      "r": 0.1,
      "g": 0.045,
      "b": 0.027,
      "a": 1
    },
    "_LowerLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": -0.4,
      "a": 0
    },
    "_MetalShineTint": {
      "r": 1,
      "g": 0.97,
      "b": 0.9,
      "a": 1
    },
    "_OutlineColor": {
      "r": 0.04,
      "g": 0.03,
      "b": 0.025,
      "a": 1
    },
    "_PaletteSkinDark": {
      "r": 0.82,
      "g": 0.7,
      "b": 0.82,
      "a": 0
    },
    "_PaletteSkinLight": {
      "r": 0.92,
      "g": 1.1,
      "b": 1.28,
      "a": 0
    },
    "_PaletteSleeveDark": {
      "r": 0.9,
      "g": 0.93,
      "b": 1.02,
      "a": 0
    },
    "_PaletteSleeveLight": {
      "r": 0.99,
      "g": 1,
      "b": 1.07,
      "a": 0
    },
    "_PaletteTunicDark": {
      "r": 1.03,
      "g": 1.06,
      "b": 1.19,
      "a": 0
    },
    "_PaletteTunicLight": {
      "r": 1,
      "g": 1.08,
      "b": 1.23,
      "a": 0
    },
    "_ReferenceRimMaterial": {
      "r": 1,
      "g": 0.9,
      "b": 0.65,
      "a": 0.6
    },
    "_ReferenceRimTint": {
      "r": 0.94,
      "g": 0.97,
      "b": 1,
      "a": 1
    },
    "_RegionLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": 0.2,
      "a": 0
    },
    "_SecondShadowTint": {
      "r": 0.55,
      "g": 0.22,
      "b": 0.28,
      "a": 1
    },
    "_ShadowTint": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_SkinShadeTint": {
      "r": 0.78,
      "g": 0.49,
      "b": 0.47,
      "a": 1
    },
    "_SkinShineTint": {
      "r": 1,
      "g": 0.82,
      "b": 0.68,
      "a": 1
    },
    "_SleeveShadeTint": {
      "r": 0.53,
      "g": 0.62,
      "b": 0.7,
      "a": 1
    },
    "_ThighLobeTint": {
      "r": 0.92,
      "g": 1,
      "b": 0.45,
      "a": 1
    }
  },
  "textures": {
    "_BumpMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailAlbedoMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMap": {
      "path": "Assets/Bridget_Textures/BGT_detail.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailMask": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_DetailNormalMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_EmissionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_FourMaterialSpecMask": {
      "path": "Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_LightMap": {
      "path": "Assets/Bridget_Textures/BGT_ilm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGT_base.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MetallicGlossMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OcclusionMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OutlineMap": {
      "path": "Assets/Bridget_Textures/BGT_olm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ParallaxMap": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_RegionalMask": {
      "path": "Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ShadowMap": {
      "path": "Assets/Bridget_Textures/BGT_Sss.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## HeadDecal_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/HeadDecal_Imitate.mat",
  "shader": "Assets/GGST_RenderFix/GgstDecal.shader",
  "savedValues": {
    "_Strength": 1
  },
  "textures": {
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGT_decal.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## HeadGlow_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/HeadGlow_Imitate.mat",
  "shader": "Assets/GGST_RenderFix/GgstGlow.shader",
  "savedValues": {
    "_GlowMultiplier": 2
  },
  "textures": {
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGT_base.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## ShadowGeometryParked_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/ShadowGeometryParked_Imitate.mat",
  "shader": "Assets/GGST_RenderFix/GgstShadowParked.shader",
  "savedValues": {},
  "textures": {},
  "renderQueue": -1,
  "keywords": []
}
```

## StageFloorReceiver

```json
{
  "source": "Assets/GGST_Imitate/Materials/StageFloorReceiver.mat",
  "shader": "Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader",
  "savedValues": {
    "_GeometryShadowBias": 0.0007,
    "_GeometryShadowFade": 0.12,
    "_GeometryShadowFilter": 0.65,
    "_GeometryShadowFloor": 0.08,
    "_GradientStrength": 0,
    "_Color": {
      "r": 0.74509805,
      "g": 0.74509805,
      "b": 0.74509805,
      "a": 1
    }
  },
  "textures": {},
  "renderQueue": -1,
  "keywords": []
}
```

## StageShadowReceiver

```json
{
  "source": "Assets/GGST_Imitate/Materials/StageShadowReceiver.mat",
  "shader": null,
  "savedValues": {
    "_Color": {
      "r": 0.5,
      "g": 0.5,
      "b": 0.5,
      "a": 1
    }
  },
  "textures": {
    "_MainTex": {
      "path": null,
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```

## StageWallReceiver

```json
{
  "source": "Assets/GGST_Imitate/Materials/StageWallReceiver.mat",
  "shader": "Assets/GGST_Imitate/Shaders/StageShadowReceiver.shader",
  "savedValues": {
    "_GeometryShadowBias": 0.001,
    "_GeometryShadowFade": 0.08,
    "_GeometryShadowFilter": 0.8,
    "_GeometryShadowFloor": 0.1,
    "_GradientStrength": 0.31,
    "_Color": {
      "r": 0.7019608,
      "g": 0.7019608,
      "b": 0.7019608,
      "a": 1
    }
  },
  "textures": {},
  "renderQueue": -1,
  "keywords": []
}
```

## Weapon_Imitate

```json
{
  "source": "Assets/GGST_Imitate/Materials/Weapon_Imitate.mat",
  "shader": "Assets/GGST_Imitate/Shaders/BridgetToon.shader",
  "savedValues": {
    "_AOStrength": 1,
    "_AmbientStrength": 0.2,
    "_BodySpecularIntensity": 0.15,
    "_BodySpecularWidth": 0.18,
    "_CharacterHeight": 1.65,
    "_CullMode": 2,
    "_DebugMode": 0,
    "_DepthOffsetFactor": 0,
    "_DepthOffsetUnits": 0,
    "_DetailIntensity": 0.278,
    "_HairLayerMax": 90,
    "_HairLayerMin": 65,
    "_HeadSpecularIntensity": 0.22,
    "_HeadSpecularWidth": 0.14,
    "_InnerLineStrength": 0.65,
    "_LayerMaskStep": 60,
    "_LeatherLayerMax": 125,
    "_LeatherLayerMin": 90,
    "_LightIntensity": 0.9,
    "_LightTreshold": 0.5,
    "_LowerLightBlend": 0,
    "_LowerRegionFeather": 0.08,
    "_LowerRegionUpper": 0.52,
    "_LowerSkinColorGate": 1,
    "_MetalLayerMax": 200,
    "_MetalLayerMin": 145,
    "_MetallicStepSpecularIntensity": 0.25,
    "_MetallicStepSpecularWidth": 0.2,
    "_OutlineMapStrength": 0.6,
    "_OutlineSkinScale": 0.35,
    "_OutlineWidth": 0.8,
    "_RampMaskCenter": 0.49803922,
    "_RampMaskStrength": 1,
    "_RampOffset": 0,
    "_ReceiveShadowStrength": 0.7,
    "_RimIntensity": 0.16,
    "_RimWidth": 0.16,
    "_SecondShadowStrength": 0,
    "_SecondShadowThreshold": 0.1,
    "_ShadowIntensity": 0.65,
    "_ShadowSoftness": 0.008,
    "_SkinShadowOffset": 0.06,
    "_SpecularIntensity": 0.12,
    "_SpecularPower": 24,
    "_UseMirroredUV": 0,
    "_UseSmoothOutline": 0,
    "_CharacterOriginWS": {
      "r": 0,
      "g": 0,
      "b": 0,
      "a": 0
    },
    "_InnerLineColor": {
      "r": 0.035,
      "g": 0.028,
      "b": 0.025,
      "a": 1
    },
    "_LowerLightDirection": {
      "r": 0.8,
      "g": 0.5,
      "b": 0.2,
      "a": 0
    },
    "_OutlineColor": {
      "r": 0.04,
      "g": 0.03,
      "b": 0.025,
      "a": 1
    },
    "_SecondShadowTint": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    },
    "_ShadowTint": {
      "r": 1,
      "g": 1,
      "b": 1,
      "a": 1
    }
  },
  "textures": {
    "_DetailMap": {
      "path": "Assets/Bridget_Textures/BGT_detail.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_LightMap": {
      "path": "Assets/Bridget_Textures/BGTW_ilm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_MainTex": {
      "path": "Assets/Bridget_Textures/BGTW_base.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_OutlineMap": {
      "path": "Assets/Bridget_Textures/BGT_olm.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    },
    "_ShadowMap": {
      "path": "Assets/Bridget_Textures/BGTW_Sss.png",
      "scale": {
        "x": 1,
        "y": 1
      },
      "offset": {
        "x": 0,
        "y": 0
      }
    }
  },
  "renderQueue": -1,
  "keywords": []
}
```
