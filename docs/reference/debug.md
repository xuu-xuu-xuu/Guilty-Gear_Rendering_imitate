# Debug 输出索引

面板 Range(0,24)，frag 实现 1–44；0 返回最终颜色。独立练习副本中可通过 Material.SetFloat("_DebugMode", 44f) 设置，使用后恢复 0。该调用仅示意 API，不是完整脚本，也未在 Unity 验证。Debug 会裁掉 OUTLINE Pass。

10 是旧 band，16 是经过重建后的 diffuse；19/20 的诊断项未接入最终颜色。26–29 不包含最后 Focused/Thigh 修正，要看 13。32 是早期 hairFaceOcclusion，不能证明最终 CleanShade 漫反射仍含投脸。35/36 也是替换前的旧脸部贡献。43 为替换域，44 为域内形状与朝向门控，两者均没有乘 _ThighLobeEnabled，不能仅凭其非黑判断最终开关。

| mode | expression | source | line |
|---|---|---|---|
| 1 | half4(base,1) | sources/BridgetToon.shader | 678 |
| 2 | half4(sss,1) | sources/BridgetToon.shader | 679 |
| 3 | half4(detail,1) | sources/BridgetToon.shader | 680 |
| 4 | half4(ilm.rrr,1) | sources/BridgetToon.shader | 681 |
| 5 | half4(ilm.ggg,1) | sources/BridgetToon.shader | 682 |
| 6 | half4(ilm.bbb,1) | sources/BridgetToon.shader | 683 |
| 7 | half4(ilm.aaa,1) | sources/BridgetToon.shader | 684 |
| 8 | half4(i.color.rrr,1) | sources/BridgetToon.shader | 685 |
| 9 | half4(n*0.5+0.5,1) | sources/BridgetToon.shader | 686 |
| 10 | half4(band.xxx,1) | sources/BridgetToon.shader | 687 |
| 11 | half4(rawShadow.xxx,1) | sources/BridgetToon.shader | 688 |
| 12 | half4(rim,1) | sources/BridgetToon.shader | 689 |
| 13 | half4(spec,1) | sources/BridgetToon.shader | 690 |
| 14 | half4(skin*half3(1,0.35,0.2)+hair*half3(0.2,0.4,1)+leather*half3(0.8,0.2,1)+metal*half3(0.2,1,0.8),1) | sources/BridgetToon.shader | 691 |
| 15 | half4(tex2D(_OutlineMap,i.uv.xy).rgb,1) | sources/BridgetToon.shader | 692 |
| 16 | half4(diffuse,1) | sources/BridgetToon.shader | 693 |
| 17 | half4(step(1.0,max(color.r,max(color.g,color.b)))*half3(1,0,0),1) | sources/BridgetToon.shader | 694 |
| 18 | half4(secondShade.xxx,1) | sources/BridgetToon.shader | 695 |
| 19 | half4(tasteHeight,tasteHorizontalNormal,tasteGradient,1) | sources/BridgetToon.shader | 696 |
| 20 | half4((faceRegion*float3(1,0.2,0.1)+legRegion*float3(0.1,1,0.2)+hair*float3(0.2,0.4,1)+coatRegion*float3(0.8,0.2,1))*regionalNl,1) | sources/BridgetToon.shader | 697 |
| 21 | half4(i.color.gba,1) | sources/BridgetToon.shader | 698 |
| 22 | half4(faceRegionMask,bodySkinRegion,sleeveRegion,1) | sources/BridgetToon.shader | 699 |
| 23 | half4(lerp(band,regionalSignal,regionTotal).xxx,1) | sources/BridgetToon.shader | 716 |
| 24 | half4(lerp(albedo,dark,regionTotal),1) | sources/BridgetToon.shader | 717 |
| 25 | half4(specClass.r+specClass.a,specClass.g+specClass.a,specClass.b+specClass.a,1) | sources/BridgetToon.shader | 719 |
| 26 | half4(shineHair*specClass.r*_LightColor0.rgb*band,1) | sources/BridgetToon.shader | 720 |
| 27 | half4(shineCloth*specClass.g*_LightColor0.rgb*band,1) | sources/BridgetToon.shader | 721 |
| 28 | half4(shineSkin*specClass.b*_LightColor0.rgb*band,1) | sources/BridgetToon.shader | 722 |
| 29 | half4(shineMetal*specClass.a*_LightColor0.rgb*band,1) | sources/BridgetToon.shader | 723 |
| 30 | half4((refinedInk*inkCoverage).xxx,1) | sources/BridgetToon.shader | 672 |
| 31 | half4(styledInk*refinedInk*inkCoverage,1) | sources/BridgetToon.shader | 673 |
| 32 | half4(hairFaceOcclusion.xxx,1) | sources/BridgetToon.shader | 676 |
| 33 | half4(eyeIrisMask,eyeScleraMask,eyeCatchMask,1) | sources/BridgetToon.shader | 667 |
| 34 | half4(abs(eyeDiffuseDelta)+abs(color-eyeBeforeCatch),1) | sources/BridgetToon.shader | 668 |
| 35 | half4(faceRefineGate.xxx,1) | sources/BridgetToon.shader | 662 |
| 36 | half4(abs(faceDiffuseDelta),1) | sources/BridgetToon.shader | 663 |
| 37 | half4(paletteGate,1) | sources/BridgetToon.shader | 701 |
| 38 | half4(cleanGate,1) | sources/BridgetToon.shader | 704 |
| 39 | half4(float3(saturate(focusedLegRegion+tunicRegion),focusedSpecCoverage,0),1) | sources/BridgetToon.shader | 711 |
| 40 | half4(focusedLegRegion.xxx,1) | sources/BridgetToon.shader | 712 |
| 41 | half4(lerp(cleanSkinBand,focusedSkinBand,saturate(_FocusedShadeEnabled)).xxx*focusedLegRegion,1) | sources/BridgetToon.shader | 713 |
| 42 | half4(lerp(cleanTunicBand,focusedTunicBand,saturate(_FocusedShadeEnabled)).xxx*tunicRegion,1) | sources/BridgetToon.shader | 714 |
| 43 | half4((thighReplace*bodySkinRegion).xxx,1) | sources/BridgetToon.shader | 708 |
| 44 | half4((thighLobe*thighFacing*thighReplace*bodySkinRegion).xxx,1) | sources/BridgetToon.shader | 709 |
