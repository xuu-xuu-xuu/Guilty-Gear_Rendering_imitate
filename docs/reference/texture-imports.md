# 贴图连接与导入设置

先按[通道用途](channels.md)判断颜色纹理与数据纹理，再设置Inspector。Filter Mode数值1为Bilinear，Wrap数值0为Repeat、1为Clamp；null表示没有可用字段，不能据此设置成0。

平台overridden=0时，该条不是生效的覆盖；textureFormat=-1也不直接说明最终GPU格式。保留MipMap和Alpha数据，随后在目标平台查看实际导入结果。

| 纹理 | 尺寸 | sRGB | MipMap | Filter / Aniso | Wrap U/V/W | Alpha Is Transparency | Max Size |
|---|---|---|---|---|---|---|---|
| BGT_detail.png | 1024×1024 | 0 | 1 | 1 / 1 | 0/0/0 | 0 | 2048 |
| BGT_SpecularClassMask.png | 2048×2048 | 0 | 0 | 1 / 1 | 1/1/1 | 0 | 2048 |
| BGT_ilm.png | 2048×2048 | 0 | 1 | 1 / 1 | 0/0/0 | 0 | 2048 |
| BGT_base.png | 2048×2048 | 1 | 1 | 1 / 1 | 1/1/0 | 0 | 2048 |
| BGT_olm.png | 2048×2048 | 1 | 1 | 1 / 1 | 0/0/0 | 0 | 2048 |
| BGT_RegionalMask.png | 2048×2048 | 0 | 0 | 1 / 1 | 1/1/1 | 0 | 2048 |
| BGT_Sss.png | 2048×2048 | 1 | 1 | 1 / 1 | 0/0/0 | 0 | 2048 |
| BGT_decal.png | 1024×1024 | 0 | 1 | 1 / 1 | 0/0/0 | 0 | 2048 |

## BGT_detail.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 0 |
| wrapV | 0 |
| wrapW | 0 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 1 |
| sRGBTexture | 0 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## BGT_SpecularClassMask.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 0 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 1 |
| wrapV | 1 |
| wrapW | 1 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 0 |
| sRGBTexture | 0 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## BGT_ilm.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 0 |
| wrapV | 0 |
| wrapW | 0 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 1 |
| sRGBTexture | 0 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## BGT_base.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 1 |
| wrapV | 1 |
| wrapW | 0 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 1 |
| sRGBTexture | 1 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## BGT_olm.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 0 |
| wrapV | 0 |
| wrapW | 0 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 1 |
| sRGBTexture | 1 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## BGT_RegionalMask.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 0 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 1 |
| wrapV | 1 |
| wrapW | 1 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 0 |
| sRGBTexture | 0 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## BGT_Sss.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 0 |
| wrapV | 0 |
| wrapW | 0 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 1 |
| sRGBTexture | 1 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## BGT_decal.png

| 平台 | 启用覆盖 | Max Size | 格式枚举 | 压缩枚举 | 质量 | Crunch | Alpha Split |
|---|---|---|---|---|---|---|---|
| DefaultTexturePlatform | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |
| Standalone | 0 | 2048 | -1 | 1 | 50 | 0 | 0 |

| 采样设置 | 值 |
|---|---|
| filterMode | 1 |
| aniso | 1 |
| mipBias | 0 |
| wrapU | 0 |
| wrapV | 0 |
| wrapW | 0 |
| alphaSource | None |
| alphaIsTransparency | 0 |
| mipMapMode | 0 |
| enableMipMap | 1 |
| sRGBTexture | 0 |
| linearTexture | 0 |
| fadeOut | 0 |
| borderMipMap | 0 |
| mipMapsPreserveCoverage | 0 |
| alphaTestReferenceValue | 0.5 |
| mipMapFadeDistanceStart | 1 |
| mipMapFadeDistanceEnd | 3 |

## 材质连接

| 材质 | Shader纹理槽 | 资源引用 | Tiling | Offset |
|---|---|---|---|---|
| Base_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| Base_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| Base_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| Base_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| Base_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| Base_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| Base_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BaseSecondary_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BaseSecondary_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BaseSecondary_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BaseSecondary_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BaseSecondary_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BaseSecondary_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BaseSecondary_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyBaseFlip_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyBaseFlip_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyBaseFlip_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyBaseFlip_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyBaseFlip_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyBaseFlip_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyBaseFlip_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| BodyDecal_Imitate | _MainTex | Assets/Bridget_Textures/BGT_decal.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| CoatExterior_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| CoatExterior_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| CoatExterior_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| CoatExterior_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| CoatExterior_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| CoatExterior_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| CoatExterior_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| HeadDecal_Imitate | _MainTex | Assets/Bridget_Textures/BGT_decal.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
| HeadGlow_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} |
