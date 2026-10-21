# 选择Debug分量排查画面

先选能隔离问题的分量，检查完恢复0。面板范围是0–24，frag支持1–44；高编号通过材质或MPB的SetFloat赋值。下面是API调用示意，不是完整组件：

```csharp
material.SetFloat("_DebugMode", 44f);
// 查看后恢复最终画面
material.SetFloat("_DebugMode", 0f);
```

| 要看什么 | 编号 | 注意 |
|---|---|---|
| 纹理和顶点输入 | 1–9 | 7是ILM.A，8是顶点R |
| 头体区域/材质类别 | 22 / 25 | 38是CleanShade覆盖，不能代替22 |
| 最终漫反射 | 16 | 10仍是基础band，不是最终diffuse |
| 最终高光 | 13 | 26–29不含Focused/Thigh的最后替换 |
| 边缘光 | 12 | 与正面高光分开看 |
| 内部线 | 30 / 31 | Debug会裁掉外轮廓，外壳回0看 |
| 眼睛区域/贡献 | 33 / 34 | 34不是最终显示颜色的增亮量 |
| 大腿替换域/形状 | 43 / 44 | 没乘_ThighLobeEnabled，不能证明开关打开 |

19/20的变量未接入最终颜色；32、35、36是后续可能被CleanShade替换的基础脸部贡献。不要用它们代替16判断最终脸色。

## 输出表达式

| 编号 | 源码返回值 | 位置 |
|---|---|---|
| 1 | half4(base,1) | [BridgetToon.shader:678](code/BridgetToon.shader.md#l678) |
| 2 | half4(sss,1) | [BridgetToon.shader:679](code/BridgetToon.shader.md#l679) |
| 3 | half4(detail,1) | [BridgetToon.shader:680](code/BridgetToon.shader.md#l680) |
| 4 | half4(ilm.rrr,1) | [BridgetToon.shader:681](code/BridgetToon.shader.md#l681) |
| 5 | half4(ilm.ggg,1) | [BridgetToon.shader:682](code/BridgetToon.shader.md#l682) |
| 6 | half4(ilm.bbb,1) | [BridgetToon.shader:683](code/BridgetToon.shader.md#l683) |
| 7 | half4(ilm.aaa,1) | [BridgetToon.shader:684](code/BridgetToon.shader.md#l684) |
| 8 | half4(i.color.rrr,1) | [BridgetToon.shader:685](code/BridgetToon.shader.md#l685) |
| 9 | half4(n*0.5+0.5,1) | [BridgetToon.shader:686](code/BridgetToon.shader.md#l686) |
| 10 | half4(band.xxx,1) | [BridgetToon.shader:687](code/BridgetToon.shader.md#l687) |
| 11 | half4(rawShadow.xxx,1) | [BridgetToon.shader:688](code/BridgetToon.shader.md#l688) |
| 12 | half4(rim,1) | [BridgetToon.shader:689](code/BridgetToon.shader.md#l689) |
| 13 | half4(spec,1) | [BridgetToon.shader:690](code/BridgetToon.shader.md#l690) |
| 14 | half4(skin*half3(1,0.35,0.2)+hair*half3(0.2,0.4,1)+leather*half3(0.8,0.2,1)+metal*half3(0.2,1,0.8),1) | [BridgetToon.shader:691](code/BridgetToon.shader.md#l691) |
| 15 | half4(tex2D(_OutlineMap,i.uv.xy).rgb,1) | [BridgetToon.shader:692](code/BridgetToon.shader.md#l692) |
| 16 | half4(diffuse,1) | [BridgetToon.shader:693](code/BridgetToon.shader.md#l693) |
| 17 | half4(step(1.0,max(color.r,max(color.g,color.b)))*half3(1,0,0),1) | [BridgetToon.shader:694](code/BridgetToon.shader.md#l694) |
| 18 | half4(secondShade.xxx,1) | [BridgetToon.shader:695](code/BridgetToon.shader.md#l695) |
| 19 | half4(tasteHeight,tasteHorizontalNormal,tasteGradient,1) | [BridgetToon.shader:696](code/BridgetToon.shader.md#l696) |
| 20 | half4((faceRegion*float3(1,0.2,0.1)+legRegion*float3(0.1,1,0.2)+hair*float3(0.2,0.4,1)+coatRegion*float3(0.8,0.2,1))*regionalNl,1) | [BridgetToon.shader:697](code/BridgetToon.shader.md#l697) |
| 21 | half4(i.color.gba,1) | [BridgetToon.shader:698](code/BridgetToon.shader.md#l698) |
| 22 | half4(faceRegionMask,bodySkinRegion,sleeveRegion,1) | [BridgetToon.shader:699](code/BridgetToon.shader.md#l699) |
| 23 | half4(lerp(band,regionalSignal,regionTotal).xxx,1) | [BridgetToon.shader:716](code/BridgetToon.shader.md#l716) |
| 24 | half4(lerp(albedo,dark,regionTotal),1) | [BridgetToon.shader:717](code/BridgetToon.shader.md#l717) |
| 25 | half4(specClass.r+specClass.a,specClass.g+specClass.a,specClass.b+specClass.a,1) | [BridgetToon.shader:719](code/BridgetToon.shader.md#l719) |
| 26 | half4(shineHair*specClass.r*_LightColor0.rgb*band,1) | [BridgetToon.shader:720](code/BridgetToon.shader.md#l720) |
| 27 | half4(shineCloth*specClass.g*_LightColor0.rgb*band,1) | [BridgetToon.shader:721](code/BridgetToon.shader.md#l721) |
| 28 | half4(shineSkin*specClass.b*_LightColor0.rgb*band,1) | [BridgetToon.shader:722](code/BridgetToon.shader.md#l722) |
| 29 | half4(shineMetal*specClass.a*_LightColor0.rgb*band,1) | [BridgetToon.shader:723](code/BridgetToon.shader.md#l723) |
| 30 | half4((refinedInk*inkCoverage).xxx,1) | [BridgetToon.shader:672](code/BridgetToon.shader.md#l672) |
| 31 | half4(styledInk*refinedInk*inkCoverage,1) | [BridgetToon.shader:673](code/BridgetToon.shader.md#l673) |
| 32 | half4(hairFaceOcclusion.xxx,1) | [BridgetToon.shader:676](code/BridgetToon.shader.md#l676) |
| 33 | half4(eyeIrisMask,eyeScleraMask,eyeCatchMask,1) | [BridgetToon.shader:667](code/BridgetToon.shader.md#l667) |
| 34 | half4(abs(eyeDiffuseDelta)+abs(color-eyeBeforeCatch),1) | [BridgetToon.shader:668](code/BridgetToon.shader.md#l668) |
| 35 | half4(faceRefineGate.xxx,1) | [BridgetToon.shader:662](code/BridgetToon.shader.md#l662) |
| 36 | half4(abs(faceDiffuseDelta),1) | [BridgetToon.shader:663](code/BridgetToon.shader.md#l663) |
| 37 | half4(paletteGate,1) | [BridgetToon.shader:701](code/BridgetToon.shader.md#l701) |
| 38 | half4(cleanGate,1) | [BridgetToon.shader:704](code/BridgetToon.shader.md#l704) |
| 39 | half4(float3(saturate(focusedLegRegion+tunicRegion),focusedSpecCoverage,0),1) | [BridgetToon.shader:711](code/BridgetToon.shader.md#l711) |
| 40 | half4(focusedLegRegion.xxx,1) | [BridgetToon.shader:712](code/BridgetToon.shader.md#l712) |
| 41 | half4(lerp(cleanSkinBand,focusedSkinBand,saturate(_FocusedShadeEnabled)).xxx*focusedLegRegion,1) | [BridgetToon.shader:713](code/BridgetToon.shader.md#l713) |
| 42 | half4(lerp(cleanTunicBand,focusedTunicBand,saturate(_FocusedShadeEnabled)).xxx*tunicRegion,1) | [BridgetToon.shader:714](code/BridgetToon.shader.md#l714) |
| 43 | half4((thighReplace*bodySkinRegion).xxx,1) | [BridgetToon.shader:708](code/BridgetToon.shader.md#l708) |
| 44 | half4((thighLobe*thighFacing*thighReplace*bodySkinRegion).xxx,1) | [BridgetToon.shader:709](code/BridgetToon.shader.md#l709) |
