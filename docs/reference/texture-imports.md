# 贴图导入与绑定完整表

本页只有接口元数据，没有纹理像素。数据来自 texture_import_settings.json 与 texture_bindings.csv。filterMode=1 是 Bilinear；wrap=0 是 Repeat、1 是 Clamp；null 代表未采到字段，不能推断实际值。平台条目 overridden=0 时不是启用的平台覆盖。保留压缩枚举数值，不凭记录推断最终 GPU 压缩格式。

| 纹理路径 | 尺寸 | sRGB | MipMap | filter/aniso | wrap U/V/W | alphaIsTransparency | maxTextureSize |
|---|---|---|---|---|---|---|---|
| Assets/Bridget_Textures/BGT_detail.png | 1024×1024 | 0 | 1 | 1/1 | 0/0/0 | 0 | 2048 |
| Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | 2048×2048 | 0 | 0 | 1/1 | 1/1/1 | 0 | 2048 |
| Assets/Bridget_Textures/BGT_ilm.png | 2048×2048 | 0 | 1 | 1/1 | 0/0/0 | 0 | 2048 |
| Assets/Bridget_Textures/BGT_base.png | 2048×2048 | 1 | 1 | 1/1 | 1/1/0 | 0 | 2048 |
| Assets/Bridget_Textures/BGT_olm.png | 2048×2048 | 1 | 1 | 1/1 | 0/0/0 | 0 | 2048 |
| Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | 2048×2048 | 0 | 0 | 1/1 | 1/1/1 | 0 | 2048 |
| Assets/Bridget_Textures/BGT_Sss.png | 2048×2048 | 1 | 1 | 1/1 | 0/0/0 | 0 | 2048 |
| Assets/Bridget_Textures/BGT_decal.png | 1024×1024 | 0 | 1 | 1/1 | 0/0/0 | 0 | 2048 |
| Assets/Bridget_Textures/BGTW_ilm.png | 1024×1024 | 1 | 1 | 1/1 | 0/0/0 | 0 | 2048 |
| Assets/Bridget_Textures/BGTW_base.png | 1024×1024 | 1 | 1 | 1/1 | 0/0/0 | 0 | 2048 |
| Assets/Bridget_Textures/BGTW_Sss.png | 1024×1024 | 1 | 1 | 1/1 | 0/0/0 | 0 | 2048 |

## BGT_detail.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    1024,
    1024
  ],
  "mode": "RGB",
  "sha256": "dd39f741223c2f1545b69d80da2e75b31bc27de4eebcdb5848fc5a4987e5668e",
  "included": false,
  "sRGB": 0,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 0,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGT_SpecularClassMask.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 0 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    2048,
    2048
  ],
  "mode": "RGBA",
  "sha256": "c2d055455f57a2de3ba1a1de16ecd93821ba7099a47b9e1e42912395b953b583",
  "included": false,
  "sRGB": 0,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 0,
    "sRGBTexture": 0,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 1,
    "wrapV": 1,
    "wrapW": 1
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGT_ilm.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    2048,
    2048
  ],
  "mode": "RGBA",
  "sha256": "fd818feef44a54b02f9e750b89ee8294cbc0ae26044e344d03c85bcce9ec15b7",
  "included": false,
  "sRGB": 0,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 0,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGT_base.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    2048,
    2048
  ],
  "mode": "RGBA",
  "sha256": "8c5e10750c16efe5280492ada7aa1245f63b515ebf005205f6c403674dfe6a08",
  "included": false,
  "sRGB": 1,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 1,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 1,
    "wrapV": 1,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGT_olm.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    2048,
    2048
  ],
  "mode": "RGB",
  "sha256": "136cf2d45a29cc866bb044f555a795d6b2cfd63a6f1b67826ed25fd0fd905c61",
  "included": false,
  "sRGB": 1,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 1,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGT_RegionalMask.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 0 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    2048,
    2048
  ],
  "mode": "RGBA",
  "sha256": "369b43a7d701dc55517fc1200721f8e0b0824e96586f49ffe92e533c096380df",
  "included": false,
  "sRGB": 0,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 0,
    "sRGBTexture": 0,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 1,
    "wrapV": 1,
    "wrapW": 1
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGT_Sss.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    2048,
    2048
  ],
  "mode": "RGBA",
  "sha256": "6e6ce9a0c6b151c536fd2ffd91eae44ded971afbab0b523665a06ad39c05461a",
  "included": false,
  "sRGB": 1,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 1,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGT_decal.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    1024,
    1024
  ],
  "mode": "RGB",
  "sha256": "095529a84c4b3f52edd4762e02a216f70df3e6f9a4ff2c70cc1cf9dbf82b1b98",
  "included": false,
  "sRGB": 0,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 0,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGTW_ilm.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    1024,
    1024
  ],
  "mode": "RGBA",
  "sha256": "4aae6cf82b55e46ac0b5a16bc1eaccc21c739dea6d211cee1afcab2900e119ba",
  "included": false,
  "sRGB": 1,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 1,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGTW_base.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    1024,
    1024
  ],
  "mode": "RGB",
  "sha256": "56eab578b738caa55c27e6c593c1f10d502c9e10f6c4e6a98bfd4de4f5af1bd7",
  "included": false,
  "sRGB": 1,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 1,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## BGTW_Sss.png

| serializedVersion | buildTarget | maxTextureSize | resizeAlgorithm | textureFormat | textureCompression | compressionQuality | crunchedCompression | allowsAlphaSplitting | overridden | ignorePlatformSupport | androidETC2FallbackOverride | forceMaximumCompressionQuality_BC6H_BC7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | DefaultTexturePlatform | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | Standalone | 2048 | 0 | -1 | 1 | 50 | 0 | 0 | 0 | 0 | 0 | 0 |

完整采样及 Alpha 元数据：

```json
{
  "size": [
    1024,
    1024
  ],
  "mode": "RGBA",
  "sha256": "aab971d8a61c2a86fd6df77371b6f413597eb090e1a18976aa20ff2cf848dc34",
  "included": false,
  "sRGB": 1,
  "mipmaps": {
    "mipMapMode": 0,
    "enableMipMap": 1,
    "sRGBTexture": 1,
    "linearTexture": 0,
    "fadeOut": 0,
    "borderMipMap": 0,
    "mipMapsPreserveCoverage": 0,
    "alphaTestReferenceValue": 0.5,
    "mipMapFadeDistanceStart": 1,
    "mipMapFadeDistanceEnd": 3
  },
  "textureSettings": {
    "serializedVersion": 2,
    "filterMode": 1,
    "aniso": 1,
    "mipBias": 0,
    "wrapU": 0,
    "wrapV": 0,
    "wrapW": 0
  },
  "maxTextureSize": 2048,
  "alphaSource": null,
  "alphaIsTransparency": 0
}
```

## 材质纹理绑定

| material | slot | texture | tiling | offset | included |
|---|---|---|---|---|---|
| Base_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Base_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Base_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Base_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Base_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Base_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Base_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BaseSecondary_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BaseSecondary_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BaseSecondary_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BaseSecondary_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BaseSecondary_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BaseSecondary_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BaseSecondary_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyBaseFlip_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyBaseFlip_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyBaseFlip_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyBaseFlip_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyBaseFlip_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyBaseFlip_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyBaseFlip_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| BodyDecal_Imitate | _MainTex | Assets/Bridget_Textures/BGT_decal.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| CoatExterior_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| CoatExterior_Imitate | _FourMaterialSpecMask | Assets/GGST_Imitate/SpecularRefinement/BGT_SpecularClassMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| CoatExterior_Imitate | _LightMap | Assets/Bridget_Textures/BGT_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| CoatExterior_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| CoatExterior_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| CoatExterior_Imitate | _RegionalMask | Assets/GGST_Imitate/RegionalShading/BGT_RegionalMask.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| CoatExterior_Imitate | _ShadowMap | Assets/Bridget_Textures/BGT_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| HeadDecal_Imitate | _MainTex | Assets/Bridget_Textures/BGT_decal.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| HeadGlow_Imitate | _MainTex | Assets/Bridget_Textures/BGT_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Weapon_Imitate | _DetailMap | Assets/Bridget_Textures/BGT_detail.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Weapon_Imitate | _LightMap | Assets/Bridget_Textures/BGTW_ilm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Weapon_Imitate | _MainTex | Assets/Bridget_Textures/BGTW_base.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Weapon_Imitate | _OutlineMap | Assets/Bridget_Textures/BGT_olm.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
| Weapon_Imitate | _ShadowMap | Assets/Bridget_Textures/BGTW_Sss.png | {"x": 1, "y": 1} | {"x": 0, "y": 0} | False |
