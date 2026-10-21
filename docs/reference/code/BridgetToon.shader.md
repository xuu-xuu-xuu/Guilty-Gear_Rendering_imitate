# BridgetToon.shader 逐行索引

原文件：`sources/BridgetToon.shader`；原工程路径：`Assets/GGST_Imitate/Shaders/BridgetToon.shader`。

SHA256：`9a5e64e1c8515efcb7662908d612fd62cf7dd45dd11c0b09e99738899641cdd5`。以下由原文生成，未修正拼写或分支。每行锚点用于正文核查；这是源码摘录索引，不是可直接运行工程。

| 行 | 原文 |
|---|---|
| <a id="l1"></a>1 | <code>Shader "GGST/BridgetToonStudy"</code> |
| <a id="l2"></a>2 | <code>{</code> |
| <a id="l3"></a>3 | <code>    Properties</code> |
| <a id="l4"></a>4 | <code>    {</code> |
| <a id="l5"></a>5 | <code>// BEGIN GGST THIGH LOBE properties</code> |
| <a id="l6"></a>6 | <code>        _ThighLobeEnabled("大腿局部收尖高光",Range(0,1))=0</code> |
| <a id="l7"></a>7 | <code>        _ThighLobeStrength("大腿独立亮块强度",Range(0,0.4))=0.16</code> |
| <a id="l8"></a>8 | <code>        _ThighLobeTint("大腿浅金色高光",Color)=(0.92,1,0.45,1)</code> |
| <a id="l9"></a>9 | <code>// END GGST THIGH LOBE properties</code> |
| <a id="l10"></a>10 | <code></code> |
| <a id="l11"></a>11 | <code>// BEGIN GGST FOCUSED LIGHT properties</code> |
| <a id="l12"></a>12 | <code>        _FocusedShadeEnabled("腹部与腿部阴面收窄",Range(0,1))=0</code> |
| <a id="l13"></a>13 | <code>        _FocusedSpecEnabled("整理后独立材质高光",Range(0,1))=0</code> |
| <a id="l14"></a>14 | <code>        _FocusedTunicThreshold("腹部明暗阈值",Range(0.2,0.7))=0.4</code> |
| <a id="l15"></a>15 | <code>        _FocusedThighThreshold("大腿明暗阈值",Range(0.3,0.8))=0.57</code> |
| <a id="l16"></a>16 | <code>        _FocusedCalfThreshold("小腿明暗阈值",Range(0.3,0.8))=0.59</code> |
| <a id="l17"></a>17 | <code>        _FocusedKneeThreshold("膝部明暗阈值",Range(0.3,0.8))=0.62</code> |
| <a id="l18"></a>18 | <code>        _FocusedSkinStrength("皮肤浅暖亮块强度",Range(0,0.4))=0.14</code> |
| <a id="l19"></a>19 | <code>        _FocusedSkinWidth("皮肤亮块宽度",Range(0.02,0.4))=0.22</code> |
| <a id="l20"></a>20 | <code>        _FocusedHairGain("发丝亮带倍率",Range(0,2))=1.25</code> |
| <a id="l21"></a>21 | <code>        _FocusedClothGain("布料柔光倍率",Range(0,2))=1.2</code> |
| <a id="l22"></a>22 | <code>        _FocusedMetalGain("金属亮芯倍率",Range(0,2))=1.05</code> |
| <a id="l23"></a>23 | <code>// END GGST FOCUSED LIGHT properties</code> |
| <a id="l24"></a>24 | <code></code> |
| <a id="l25"></a>25 | <code>// BEGIN GGST CLEAN SHADE properties</code> |
| <a id="l26"></a>26 | <code>        _CleanShadeEnabled("角色简洁漫反射明暗",Range(0,1))=0</code> |
| <a id="l27"></a>27 | <code>        _CleanClothMaskWeight("衣料明暗遮罩参与",Range(0,1))=0.4</code> |
| <a id="l28"></a>28 | <code>        _CleanClothAOWeight("衣料顶点暗部参与",Range(0,1))=0.25</code> |
| <a id="l29"></a>29 | <code>        _CleanClothSoftness("衣料色块边界宽度",Range(0.005,0.06))=0.018</code> |
| <a id="l30"></a>30 | <code>        _CleanFaceUnderStart("下颌暗面起点",Range(-1,0))=-0.7</code> |
| <a id="l31"></a>31 | <code>        _CleanFaceUnderEnd("下颌亮面起点",Range(-1,0.2))=-0.45</code> |
| <a id="l32"></a>32 | <code>// END GGST CLEAN SHADE properties</code> |
| <a id="l33"></a>33 | <code></code> |
| <a id="l34"></a>34 | <code>// BEGIN GGST PALETTE properties</code> |
| <a id="l35"></a>35 | <code>        _PaletteEnabled("皮肤与浅色衣料漫反射配色",Range(0,1))=0</code> |
| <a id="l36"></a>36 | <code>        _PaletteSkinLight("皮肤亮面乘色",Vector)=(0.92,1.10,1.28,0)</code> |
| <a id="l37"></a>37 | <code>        _PaletteSkinDark("皮肤暖阴面乘色",Vector)=(0.82,0.70,0.82,0)</code> |
| <a id="l38"></a>38 | <code>        _PaletteSleeveLight("白袖亮面乘色",Vector)=(0.99,1,1.07,0)</code> |
| <a id="l39"></a>39 | <code>        _PaletteSleeveDark("白袖冷灰阴面乘色",Vector)=(0.90,0.93,1.02,0)</code> |
| <a id="l40"></a>40 | <code>        _PaletteTunicLight("胸前衣料亮面乘色",Vector)=(1,1.08,1.23,0)</code> |
| <a id="l41"></a>41 | <code>        _PaletteTunicDark("胸前衣料阴面乘色",Vector)=(1.03,1.06,1.19,0)</code> |
| <a id="l42"></a>42 | <code>// END GGST PALETTE properties</code> |
| <a id="l43"></a>43 | <code></code> |
| <a id="l44"></a>44 | <code>// BEGIN GGST RIM REFINE properties</code> |
| <a id="l45"></a>45 | <code>        _ReferenceRimEnabled("参考风格边缘光启用",Range(0,1))=0</code> |
| <a id="l46"></a>46 | <code>        _ReferenceRimWidth("参考边缘光宽度",Range(0.02,0.4))=0.19</code> |
| <a id="l47"></a>47 | <code>        _ReferenceRimStrength("参考边缘光强度",Range(0,1))=0.38</code> |
| <a id="l48"></a>48 | <code>        _ReferenceRimShadowFloor("暗面边缘光保留",Range(0,1))=0.45</code> |
| <a id="l49"></a>49 | <code>        _ReferenceRimTint("参考边缘光浅色",Color)=(0.94,0.97,1,1)</code> |
| <a id="l50"></a>50 | <code>        _ReferenceRimTintMix("边缘光浅色混合",Range(0,1))=0.65</code> |
| <a id="l51"></a>51 | <code>        _ReferenceRimMaterial("边缘光 发/布/肤/金属",Vector)=(1,0.9,0.65,0.6)</code> |
| <a id="l52"></a>52 | <code>        _ReferenceRimFaceScale("脸部边缘光比例",Range(0,1))=0.15</code> |
| <a id="l53"></a>53 | <code>// END GGST RIM REFINE properties</code> |
| <a id="l54"></a>54 | <code></code> |
| <a id="l55"></a>55 | <code>// BEGIN GGST FACE DIFFUSE properties</code> |
| <a id="l56"></a>56 | <code>_FaceDiffuseRefine("脸部漫反射造型启用",Range(0,1))=0</code> |
| <a id="l57"></a>57 | <code>        _FaceDiffuseBoundary("侧脸暗面边界",Range(0.25,0.85))=0.54</code> |
| <a id="l58"></a>58 | <code>        _FaceDiffuseEdge("侧脸边界过渡",Range(0.015,0.12))=0.045</code> |
| <a id="l59"></a>59 | <code>        _FaceDiffuseSide("侧脸阴面覆盖",Range(0,1))=0.90</code> |
| <a id="l60"></a>60 | <code>        _FaceDiffuseDepth("脸部原Sss暗色混合",Range(0,1))=0.90</code> |
| <a id="l61"></a>61 | <code>        _FaceDiffuseTint("脸部漫反射暖暗乘色",Color)=(1,0.84,0.84,1)</code> |
| <a id="l62"></a>62 | <code>// END GGST FACE DIFFUSE properties</code> |
| <a id="l63"></a>63 | <code></code> |
| <a id="l64"></a>64 | <code>// BEGIN GGST EYE REFINEMENT properties</code> |
| <a id="l65"></a>65 | <code>        _EyeRefineEnabled("眼睛分区层次启用",Range(0,1))=0</code> |
| <a id="l66"></a>66 | <code>        _EyeIrisUpperDepth("虹膜上层深色",Range(0,0.5))=0.18</code> |
| <a id="l67"></a>67 | <code>        _EyeIrisLowerLift("虹膜下层透亮",Range(0,0.4))=0.10</code> |
| <a id="l68"></a>68 | <code>        _EyeIrisEdgeDepth("虹膜外缘层次",Range(0,0.3))=0.08</code> |
| <a id="l69"></a>69 | <code>        _EyeCatchlightLift("原白色高光清晰度",Range(0,0.5))=0.25</code> |
| <a id="l70"></a>70 | <code>        _EyeScleraShade("眼白克制冷色",Range(0,0.2))=0.06</code> |
| <a id="l71"></a>71 | <code>// END GGST EYE REFINEMENT properties</code> |
| <a id="l72"></a>72 | <code></code> |
| <a id="l73"></a>73 | <code>// BEGIN GGST SHADOW REFINEMENT properties</code> |
| <a id="l74"></a>74 | <code>        _HairFaceShadowStrength("真实头发投脸强度",Range(0,1))=0</code> |
| <a id="l75"></a>75 | <code>        _HairFaceShadowBias("头发阴影深度偏移/米",Range(0,0.01))=0.0006</code> |
| <a id="l76"></a>76 | <code>        _HairFaceShadowFilter("头发阴影过滤/贴素",Range(0,3))=1.1</code> |
| <a id="l77"></a>77 | <code>// END GGST SHADOW REFINEMENT properties</code> |
| <a id="l78"></a>78 | <code>// BEGIN GGST LINE REFINEMENT properties</code> |
| <a id="l79"></a>79 | <code>        _LineRefineEnabled("材质分区线条启用",Float)=0</code> |
| <a id="l80"></a>80 | <code>        _LineContourWidths("轮廓像素宽度 发/布/肤/金属",Vector)=(0.82,0.95,0.60,0.72)</code> |
| <a id="l81"></a>81 | <code>        _LineContourTintMix("轮廓材质色混合",Range(0,1))=0.55</code> |
| <a id="l82"></a>82 | <code>        _LineInnerStrengths("内部线强度 发/布/肤/金属",Vector)=(0.72,0.76,0.58,0.72)</code> |
| <a id="l83"></a>83 | <code>        _LineInnerFilter("内部线覆盖率过滤",Range(0,1))=0.60</code> |
| <a id="l84"></a>84 | <code>        _LineInnerTintMix("内部线材质色混合",Range(0,1))=0.45</code> |
| <a id="l85"></a>85 | <code>        _LineHairInk("发线暖棕",Color)=(0.06,0.032,0.015,1)</code> |
| <a id="l86"></a>86 | <code>        _LineClothInk("布线蓝炭",Color)=(0.023,0.031,0.042,1)</code> |
| <a id="l87"></a>87 | <code>        _LineSkinInk("肤线暖棕",Color)=(0.10,0.045,0.027,1)</code> |
| <a id="l88"></a>88 | <code>        _LineMetalInk("金属线深棕",Color)=(0.04,0.032,0.022,1)</code> |
| <a id="l89"></a>89 | <code>// END GGST LINE REFINEMENT properties</code> |
| <a id="l90"></a>90 | <code>        // BEGIN GGST SPECULAR REFINEMENT properties</code> |
| <a id="l91"></a>91 | <code>        _FourMaterialSpecMask("高光分类 RGBA发/布/肤/金属",2D)="black"{}</code> |
| <a id="l92"></a>92 | <code>        _FourMaterialSpecEnabled("独立材质高光启用",Range(0,1))=0</code> |
| <a id="l93"></a>93 | <code>        _HairShineStrength("头发亮带强度",Range(0,0.5))=0.12</code> |
| <a id="l94"></a>94 | <code>        _HairShineWidth("头发亮带宽度",Range(0.02,0.3))=0.10</code> |
| <a id="l95"></a>95 | <code>        _HairShineTint("头发亮带色",Color)=(1,0.94,0.78,1)</code> |
| <a id="l96"></a>96 | <code>        _ClothShineStrength("布料柔光强度",Range(0,0.2))=0.035</code> |
| <a id="l97"></a>97 | <code>        _ClothShinePower("布料柔光指数",Range(2,40))=12</code> |
| <a id="l98"></a>98 | <code>        _ClothShineTint("布料柔光色",Color)=(0.90,0.95,1,1)</code> |
| <a id="l99"></a>99 | <code>        _SkinShineStrength("皮肤微光强度",Range(0,0.2))=0.028</code> |
| <a id="l100"></a>100 | <code>        _SkinShinePower("皮肤微光指数",Range(4,80))=28</code> |
| <a id="l101"></a>101 | <code>        _SkinShineTint("皮肤微光色",Color)=(1,0.82,0.68,1)</code> |
| <a id="l102"></a>102 | <code>        _MetalShineStrength("金属窄亮芯强度",Range(0,1))=0.38</code> |
| <a id="l103"></a>103 | <code>        _MetalShineWidth("金属亮芯宽度",Range(0.02,0.3))=0.10</code> |
| <a id="l104"></a>104 | <code>        _MetalShineTint("金属亮芯色",Color)=(1,0.97,0.90,1)</code> |
| <a id="l105"></a>105 | <code>        // END GGST SPECULAR REFINEMENT properties</code> |
| <a id="l106"></a>106 | <code>        _MainTex("基础色",2D)="white"{}</code> |
| <a id="l107"></a>107 | <code>        _ShadowMap("原 Sss 颜色图",2D)="white"{}</code> |
| <a id="l108"></a>108 | <code>        _LightMap("ilm 数据",2D)="white"{}</code> |
| <a id="l109"></a>109 | <code>        _DetailMap("detail / UV1",2D)="white"{}</code> |
| <a id="l110"></a>110 | <code>        _OutlineMap("olm 轮廓颜色",2D)="black"{}</code> |
| <a id="l111"></a>111 | <code>        _RegionalMask("独立分区 R皮肤 G白袖",2D)="black"{}</code> |
| <a id="l112"></a>112 | <code>        [HideInInspector] _RegionalEnabled("分区明暗启用",Float)=0</code> |
| <a id="l113"></a>113 | <code>        [HideInInspector] _RegionalHead("头部 Renderer 分区",Float)=0</code> |
| <a id="l114"></a>114 | <code>        [HideInInspector] _FaceFrameValid("只读脸部坐标有效",Float)=0</code> |
| <a id="l115"></a>115 | <code>        [HideInInspector] _FaceOriginWS("只读头部原点",Vector)=(0,0,0,0)</code> |
| <a id="l116"></a>116 | <code>        [HideInInspector] _FaceRightWS("只读头部横向与半宽",Vector)=(1,0,0,0.083)</code> |
| <a id="l117"></a>117 | <code>        _FaceSideStrength("侧脸受控阴影",Range(0,1))=0.85</code> |
| <a id="l118"></a>118 | <code>        _FaceShadeThreshold("脸部明暗阈值",Range(0,1))=0.80</code> |
| <a id="l119"></a>119 | <code>        _SkinShadeThreshold("身体皮肤明暗阈值",Range(0,1))=0.69</code> |
| <a id="l120"></a>120 | <code>        _SleeveShadeThreshold("白袖明暗阈值",Range(0,1))=0.68</code> |
| <a id="l121"></a>121 | <code>        _RegionalSoftness("分区边界宽度",Range(0.001,0.08))=0.018</code> |
| <a id="l122"></a>122 | <code>        _FaceShadeStrength("脸部暖暗色强度",Range(0,1))=0.78</code> |
| <a id="l123"></a>123 | <code>        _SkinShadeStrength("皮肤暖暗色强度",Range(0,1))=0.72</code> |
| <a id="l124"></a>124 | <code>        _SleeveShadeStrength("白袖冷暗色强度",Range(0,1))=0.72</code> |
| <a id="l125"></a>125 | <code>        _FaceShadeTint("脸部暗面乘色",Color)=(1,0.92,0.91,1)</code> |
| <a id="l126"></a>126 | <code>        _SkinShadeTint("皮肤暗面乘色",Color)=(0.78,0.49,0.47,1)</code> |
| <a id="l127"></a>127 | <code>        _SleeveShadeTint("白袖暗面乘色",Color)=(0.53,0.62,0.70,1)</code> |
| <a id="l128"></a>128 | <code></code> |
| <a id="l129"></a>129 | <code>        [Enum(UnityEngine.Rendering.CullMode)] _CullMode("面剔除",Float)=2</code> |
| <a id="l130"></a>130 | <code>        [Toggle] _UseMirroredUV("读取第三套 UV",Float)=0</code> |
| <a id="l131"></a>131 | <code>        _DepthOffsetFactor("深度偏移因子",Float)=0</code> |
| <a id="l132"></a>132 | <code>        _DepthOffsetUnits("深度偏移单位",Float)=0</code> |
| <a id="l133"></a>133 | <code>        _LightTreshold("明暗分界",Range(0,1))=0.5</code> |
| <a id="l134"></a>134 | <code>        _RampOffset("区域明暗偏移",Range(-1,1))=0</code> |
| <a id="l135"></a>135 | <code>        _RampMaskCenter("ilm G 中性值（实验参数）",Range(0,1))=0.4980392</code> |
| <a id="l136"></a>136 | <code>        _RampMaskStrength("ilm G 偏移强度",Range(0,2))=1</code> |
| <a id="l137"></a>137 | <code>        _ShadowSoftness("明暗边界宽度",Range(0,0.1))=0.008</code> |
| <a id="l138"></a>138 | <code>        _ShadowIntensity("Sss 暗部混合",Range(0,1))=0.65</code> |
| <a id="l139"></a>139 | <code>        _ShadowTint("暗部色调",Color)=(1,1,1,1)</code> |
| <a id="l140"></a>140 | <code>        _SkinShadowOffset("低 R 分区明暗偏移",Range(-0.5,0.5))=0.06</code> |
| <a id="l141"></a>141 | <code>        _SecondShadowThreshold("第二暗部阈值 / NdotL",Range(-1,1))=0.1</code> |
| <a id="l142"></a>142 | <code>        _SecondShadowStrength("下半身第二暗部强度",Range(0,1))=0</code> |
| <a id="l143"></a>143 | <code>        _SecondShadowTint("第二暗部乘色",Color)=(1,1,1,1)</code> |
| <a id="l144"></a>144 | <code>        _LowerRegionUpper("下半身区域上界 / 相对身高",Range(0,1))=0.52</code> |
| <a id="l145"></a>145 | <code>        _LowerRegionFeather("区域过渡宽度",Range(0.01,0.3))=0.08</code> |
| <a id="l146"></a>146 | <code>        _LowerLightBlend("下半身独立光向混合",Range(0,1))=0</code> |
| <a id="l147"></a>147 | <code>        _LowerLightDirection("下半身独立光向 / 世界空间",Vector)=(0.8,0.5,0.2,0)</code> |
| <a id="l148"></a>148 | <code>        _LowerLightDynamic("下半身跟随主光（移动光源 A/B）",Range(0,1))=0</code> |
| <a id="l149"></a>149 | <code>        _LowerSkinColorGate("用基础色排除低R白色材质（当前配色实验）",Range(0,1))=1</code> |
| <a id="l150"></a>150 | <code>        _TasteRatePow("下半身渐变指数（实验）",Range(0.1,4))=1</code> |
| <a id="l151"></a>151 | <code>        _TasteHeightStart("渐变高度下界（诊断）",Range(-1,2))=0</code> |
| <a id="l152"></a>152 | <code>        _TasteHeightEnd("渐变高度上界（诊断）",Range(-1,2))=0.65</code> |
| <a id="l153"></a>153 | <code>        _TasteNormalWeight("水平法线参与度（诊断）",Range(0,1))=0.5</code> |
| <a id="l154"></a>154 | <code>        _RegionLightBlend("部位光向混合（诊断）",Range(0,1))=0</code> |
| <a id="l155"></a>155 | <code>        _RegionLightDirection("部位候选光向（诊断）",Vector)=(0.8,0.5,0.2,0)</code> |
| <a id="l156"></a>156 | <code>        [HideInInspector] _CharacterOriginWS("角色脚下参考原点",Vector)=(0,0,0,0)</code> |
| <a id="l157"></a>157 | <code>        [HideInInspector] _CharacterHeight("角色参考身高",Float)=1.65</code> |
| <a id="l158"></a>158 | <code>        _LightIntensity("主光贡献",Range(0,2))=0.9</code> |
| <a id="l159"></a>159 | <code>        _AmbientStrength("环境光贡献",Range(0,1))=0.2</code> |
| <a id="l160"></a>160 | <code>        _AOStrength("顶点 R 明暗控制",Range(0,1))=1</code> |
| <a id="l161"></a>161 | <code>        _DetailIntensity("Detail 强度",Range(0,1))=0.278</code> |
| <a id="l162"></a>162 | <code>        _InnerLineStrength("ilm Alpha 内部线条",Range(0,1))=0.65</code> |
| <a id="l163"></a>163 | <code>        _InnerLineColor("内部线条颜色",Color)=(0.035,0.028,0.025,1)</code> |
| <a id="l164"></a>164 | <code>        _RimWidth("边缘光宽度",Range(0,1))=0.16</code> |
| <a id="l165"></a>165 | <code>        _RimIntensity("边缘光强度",Range(0,1))=0.16</code> |
| <a id="l166"></a>166 | <code>        _SpecularPower("通用高光指数",Range(1,100))=24</code> |
| <a id="l167"></a>167 | <code>        _SpecularIntensity("通用高光强度",Range(0,2))=0.12</code> |
| <a id="l168"></a>168 | <code>        _LayerMaskStep("皮肤分区上界（实验分类）",Range(0,255))=60</code> |
| <a id="l169"></a>169 | <code>        _BodySpecularWidth("皮肤高光宽度",Range(0,1))=0.18</code> |
| <a id="l170"></a>170 | <code>        _BodySpecularIntensity("皮肤高光强度",Range(0,1))=0.15</code> |
| <a id="l171"></a>171 | <code>        _HeadSpecularWidth("头发高光宽度",Range(0,1))=0.14</code> |
| <a id="l172"></a>172 | <code>        _HeadSpecularIntensity("头发高光强度",Range(0,1))=0.22</code> |
| <a id="l173"></a>173 | <code>        _HairLayerMin("头发/布料共享分区下界",Range(0,255))=65</code> |
| <a id="l174"></a>174 | <code>        _HairLayerMax("头发/布料共享分区上界",Range(0,255))=90</code> |
| <a id="l175"></a>175 | <code>        _LeatherLayerMin("手套/裙子分区下界",Range(0,255))=90</code> |
| <a id="l176"></a>176 | <code>        _LeatherLayerMax("手套/裙子分区上界",Range(0,255))=125</code> |
| <a id="l177"></a>177 | <code>        _MetalLayerMin("金属分区下界",Range(0,255))=145</code> |
| <a id="l178"></a>178 | <code>        _MetalLayerMax("金属分区上界",Range(0,255))=200</code> |
| <a id="l179"></a>179 | <code>        _MetallicStepSpecularWidth("金属高光宽度",Range(0,1))=0.2</code> |
| <a id="l180"></a>180 | <code>        _MetallicStepSpecularIntensity("金属高光强度",Range(0,1))=0.25</code> |
| <a id="l181"></a>181 | <code>        _ReceiveShadowStrength("接收投影强度",Range(0,1))=0.7</code> |
| <a id="l182"></a>182 | <code>        _OutlineWidth("轮廓宽度 / 输出像素",Range(0,4))=0.8</code> |
| <a id="l183"></a>183 | <code>        [Toggle] _UseSmoothOutline("使用蒙皮平滑描边法线（需专用网格）",Float)=0</code> |
| <a id="l184"></a>184 | <code>        _OutlineSkinScale("皮肤轮廓宽度比例",Range(0,1))=0.35</code> |
| <a id="l185"></a>185 | <code>        _OutlineColor("轮廓颜色",Color)=(0.04,0.03,0.025,1)</code> |
| <a id="l186"></a>186 | <code>        _OutlineMapStrength("olm 颜色参与",Range(0,1))=0.6</code> |
| <a id="l187"></a>187 | <code>        [IntRange] _DebugMode("调试输出 0～24（编号见修改文档）",Range(0,24))=0</code> |
| <a id="l188"></a>188 | <code>    }</code> |
| <a id="l189"></a>189 | <code>    SubShader</code> |
| <a id="l190"></a>190 | <code>    {</code> |
| <a id="l191"></a>191 | <code>        Tags {"RenderType"="Opaque" "Queue"="Geometry"}</code> |
| <a id="l192"></a>192 | <code>        LOD 200</code> |
| <a id="l193"></a>193 | <code>        Pass</code> |
| <a id="l194"></a>194 | <code>        {</code> |
| <a id="l195"></a>195 | <code>            Name "FORWARD"</code> |
| <a id="l196"></a>196 | <code>            Tags {"LightMode"="ForwardBase"}</code> |
| <a id="l197"></a>197 | <code>            Cull [_CullMode] ZWrite On</code> |
| <a id="l198"></a>198 | <code>            Offset [_DepthOffsetFactor], [_DepthOffsetUnits]</code> |
| <a id="l199"></a>199 | <code>            CGPROGRAM</code> |
| <a id="l200"></a>200 | <code>            #pragma target 3.0</code> |
| <a id="l201"></a>201 | <code>            #pragma vertex vert</code> |
| <a id="l202"></a>202 | <code>            #pragma fragment frag</code> |
| <a id="l203"></a>203 | <code>            #pragma multi_compile_fwdbase nolightmap nodirlightmap nodynlightmap novertexlight</code> |
| <a id="l204"></a>204 | <code>            #include "UnityCG.cginc"</code> |
| <a id="l205"></a>205 | <code>            #include "Lighting.cginc"</code> |
| <a id="l206"></a>206 | <code>            #include "AutoLight.cginc"</code> |
| <a id="l207"></a>207 | <code>            // BEGIN GGST SPECULAR REFINEMENT declarations</code> |
| <a id="l208"></a>208 | <code>// BEGIN GGST RIM REFINE declarations</code> |
| <a id="l209"></a>209 | <code>            float _ReferenceRimEnabled,_ReferenceRimWidth,_ReferenceRimStrength;</code> |
| <a id="l210"></a>210 | <code>            float _ReferenceRimShadowFloor,_ReferenceRimTintMix,_ReferenceRimFaceScale;</code> |
| <a id="l211"></a>211 | <code>            half4 _ReferenceRimTint;</code> |
| <a id="l212"></a>212 | <code>            float4 _ReferenceRimMaterial;</code> |
| <a id="l213"></a>213 | <code>// END GGST RIM REFINE declarations</code> |
| <a id="l214"></a>214 | <code>// BEGIN GGST PALETTE declarations</code> |
| <a id="l215"></a>215 | <code>            float _PaletteEnabled;</code> |
| <a id="l216"></a>216 | <code>            float4 _PaletteSkinLight,_PaletteSkinDark,_PaletteSleeveLight,_PaletteSleeveDark,_PaletteTunicLight,_PaletteTunicDark;</code> |
| <a id="l217"></a>217 | <code>// END GGST PALETTE declarations</code> |
| <a id="l218"></a>218 | <code>// BEGIN GGST CLEAN SHADE declarations</code> |
| <a id="l219"></a>219 | <code>            float _CleanShadeEnabled,_CleanClothMaskWeight,_CleanClothAOWeight,_CleanClothSoftness;</code> |
| <a id="l220"></a>220 | <code>            float _CleanFaceUnderStart,_CleanFaceUnderEnd;</code> |
| <a id="l221"></a>221 | <code>// END GGST CLEAN SHADE declarations</code> |
| <a id="l222"></a>222 | <code>// BEGIN GGST FOCUSED LIGHT declarations</code> |
| <a id="l223"></a>223 | <code>// BEGIN GGST THIGH LOBE declarations</code> |
| <a id="l224"></a>224 | <code>            float _ThighLobeEnabled,_ThighLobeStrength;</code> |
| <a id="l225"></a>225 | <code>            half4 _ThighLobeTint;</code> |
| <a id="l226"></a>226 | <code>// END GGST THIGH LOBE declarations</code> |
| <a id="l227"></a>227 | <code>            float _FocusedShadeEnabled,_FocusedSpecEnabled,_FocusedTunicThreshold;</code> |
| <a id="l228"></a>228 | <code>            float _FocusedThighThreshold,_FocusedCalfThreshold,_FocusedKneeThreshold;</code> |
| <a id="l229"></a>229 | <code>            float _FocusedSkinStrength,_FocusedSkinWidth,_FocusedHairGain,_FocusedClothGain,_FocusedMetalGain;</code> |
| <a id="l230"></a>230 | <code>// END GGST FOCUSED LIGHT declarations</code> |
| <a id="l231"></a>231 | <code>            sampler2D _FourMaterialSpecMask;</code> |
| <a id="l232"></a>232 | <code>            float _FourMaterialSpecEnabled,_HairShineStrength,_HairShineWidth;</code> |
| <a id="l233"></a>233 | <code>            float _ClothShineStrength,_ClothShinePower,_SkinShineStrength,_SkinShinePower;</code> |
| <a id="l234"></a>234 | <code>            float _MetalShineStrength,_MetalShineWidth;</code> |
| <a id="l235"></a>235 | <code>            half4 _HairShineTint,_ClothShineTint,_SkinShineTint,_MetalShineTint;</code> |
| <a id="l236"></a>236 | <code>            // END GGST SPECULAR REFINEMENT declarations</code> |
| <a id="l237"></a>237 | <code>// BEGIN GGST LINE REFINEMENT forward declarations</code> |
| <a id="l238"></a>238 | <code>            float _LineRefineEnabled,_LineContourTintMix,_LineInnerFilter,_LineInnerTintMix;</code> |
| <a id="l239"></a>239 | <code>            float4 _LineContourWidths,_LineInnerStrengths;</code> |
| <a id="l240"></a>240 | <code>            half4 _LineHairInk,_LineClothInk,_LineSkinInk,_LineMetalInk;</code> |
| <a id="l241"></a>241 | <code>// END GGST LINE REFINEMENT forward declarations</code> |
| <a id="l242"></a>242 | <code>// BEGIN GGST SHADOW REFINEMENT face receiver declarations</code> |
| <a id="l243"></a>243 | <code>            sampler2D _HairShadowDepth;</code> |
| <a id="l244"></a>244 | <code>            float4x4 _HairShadowVP;</code> |
| <a id="l245"></a>245 | <code>            float4 _HairShadowOriginRange,_HairShadowForward,_HairShadowTexel;</code> |
| <a id="l246"></a>246 | <code>            float _HairShadowEnabled,_HairFaceShadowStrength,_HairFaceShadowBias,_HairFaceShadowFilter;</code> |
| <a id="l247"></a>247 | <code>            float ReadHairVisibility(float3 world)</code> |
| <a id="l248"></a>248 | <code>            {</code> |
| <a id="l249"></a>249 | <code>                float4 clipSpace=mul(_HairShadowVP,float4(world,1));</code> |
| <a id="l250"></a>250 | <code>                float2 uv=clipSpace.xy/max(clipSpace.w,0.00001)*0.5+0.5;</code> |
| <a id="l251"></a>251 | <code>                float depth=dot(world-_HairShadowOriginRange.xyz,_HairShadowForward.xyz)/max(_HairShadowOriginRange.w,0.00001);</code> |
| <a id="l252"></a>252 | <code>                float inside=step(0,uv.x)*step(uv.x,1)*step(0,uv.y)*step(uv.y,1)*step(0,depth)*step(depth,1);</code> |
| <a id="l253"></a>253 | <code>                float bias=_HairFaceShadowBias/max(_HairShadowOriginRange.w,0.00001);</code> |
| <a id="l254"></a>254 | <code>                float visibility=0;</code> |
| <a id="l255"></a>255 | <code>                [unroll] for(int x=-1;x&lt;=1;x++)</code> |
| <a id="l256"></a>256 | <code>                [unroll] for(int y=-1;y&lt;=1;y++)</code> |
| <a id="l257"></a>257 | <code>                {</code> |
| <a id="l258"></a>258 | <code>                    float stored=tex2D(_HairShadowDepth,uv+float2(x,y)*_HairShadowTexel.xy*_HairFaceShadowFilter).r;</code> |
| <a id="l259"></a>259 | <code>                    visibility+=step(depth-bias,stored);</code> |
| <a id="l260"></a>260 | <code>                }</code> |
| <a id="l261"></a>261 | <code>                return lerp(1.0,visibility/9.0,inside*saturate(_HairShadowEnabled));</code> |
| <a id="l262"></a>262 | <code>            }</code> |
| <a id="l263"></a>263 | <code>// END GGST SHADOW REFINEMENT face receiver declarations</code> |
| <a id="l264"></a>264 | <code>            sampler2D _MainTex,_ShadowMap,_LightMap,_DetailMap,_OutlineMap,_RegionalMask;</code> |
| <a id="l265"></a>265 | <code>// BEGIN GGST EYE REFINEMENT declarations</code> |
| <a id="l266"></a>266 | <code>            float _EyeRefineEnabled,_EyeIrisUpperDepth,_EyeIrisLowerLift;</code> |
| <a id="l267"></a>267 | <code>            float _EyeIrisEdgeDepth,_EyeCatchlightLift,_EyeScleraShade;</code> |
| <a id="l268"></a>268 | <code>            float EyeDisk(float2 q)</code> |
| <a id="l269"></a>269 | <code>            {</code> |
| <a id="l270"></a>270 | <code>                float radius=length(q);</code> |
| <a id="l271"></a>271 | <code>                float aa=clamp(fwidth(radius)*0.55,0.01,0.08);</code> |
| <a id="l272"></a>272 | <code>                return 1.0-smoothstep(1.0-aa,1.0+aa,radius);</code> |
| <a id="l273"></a>273 | <code>            }</code> |
| <a id="l274"></a>274 | <code>// END GGST EYE REFINEMENT declarations</code> |
| <a id="l275"></a>275 | <code></code> |
| <a id="l276"></a>276 | <code>            float _RegionalEnabled,_RegionalHead,_FaceShadeThreshold,_SkinShadeThreshold,_SleeveShadeThreshold,_RegionalSoftness;</code> |
| <a id="l277"></a>277 | <code>            float _FaceShadeStrength,_SkinShadeStrength,_SleeveShadeStrength,_FaceSideStrength,_FaceFrameValid;</code> |
| <a id="l278"></a>278 | <code>            float4 _FaceOriginWS,_FaceRightWS;</code> |
| <a id="l279"></a>279 | <code>            half4 _FaceShadeTint,_SkinShadeTint,_SleeveShadeTint;</code> |
| <a id="l280"></a>280 | <code>// BEGIN GGST FACE DIFFUSE declarations</code> |
| <a id="l281"></a>281 | <code>float _FaceDiffuseRefine,_FaceDiffuseBoundary,_FaceDiffuseEdge,_FaceDiffuseSide,_FaceDiffuseDepth;</code> |
| <a id="l282"></a>282 | <code>            half4 _FaceDiffuseTint;</code> |
| <a id="l283"></a>283 | <code>// END GGST FACE DIFFUSE declarations</code> |
| <a id="l284"></a>284 | <code></code> |
| <a id="l285"></a>285 | <code>            float4 _MainTex_ST;</code> |
| <a id="l286"></a>286 | <code>            float _UseMirroredUV,_LightTreshold,_RampOffset,_RampMaskCenter,_RampMaskStrength,_ShadowSoftness;</code> |
| <a id="l287"></a>287 | <code>            float _ShadowIntensity,_SkinShadowOffset,_LightIntensity,_AmbientStrength,_AOStrength,_DetailIntensity;</code> |
| <a id="l288"></a>288 | <code>            float _InnerLineStrength,_RimWidth,_RimIntensity,_SpecularPower,_SpecularIntensity,_LayerMaskStep;</code> |
| <a id="l289"></a>289 | <code>            float _BodySpecularWidth,_BodySpecularIntensity,_HeadSpecularWidth,_HeadSpecularIntensity;</code> |
| <a id="l290"></a>290 | <code>            float _HairLayerMin,_HairLayerMax,_LeatherLayerMin,_LeatherLayerMax;</code> |
| <a id="l291"></a>291 | <code>            float _MetalLayerMin,_MetalLayerMax,_MetallicStepSpecularWidth,_MetallicStepSpecularIntensity;</code> |
| <a id="l292"></a>292 | <code>            float _ReceiveShadowStrength,_DebugMode;</code> |
| <a id="l293"></a>293 | <code>            float _SecondShadowThreshold,_SecondShadowStrength,_LowerRegionUpper,_LowerRegionFeather,_LowerLightBlend,_LowerLightDynamic,_CharacterHeight;</code> |
| <a id="l294"></a>294 | <code>            float _LowerSkinColorGate,_TasteRatePow,_TasteHeightStart,_TasteHeightEnd,_TasteNormalWeight,_RegionLightBlend;</code> |
| <a id="l295"></a>295 | <code>            float4 _CharacterOriginWS,_LowerLightDirection,_RegionLightDirection;</code> |
| <a id="l296"></a>296 | <code>            half4 _SecondShadowTint;</code> |
| <a id="l297"></a>297 | <code>            half4 _ShadowTint,_InnerLineColor;</code> |
| <a id="l298"></a>298 | <code>            struct appdata</code> |
| <a id="l299"></a>299 | <code>            {</code> |
| <a id="l300"></a>300 | <code>                float4 vertex:POSITION; float3 normal:NORMAL;</code> |
| <a id="l301"></a>301 | <code>                float2 uv:TEXCOORD0; float2 uv1:TEXCOORD1; float2 uvMirror:TEXCOORD2;</code> |
| <a id="l302"></a>302 | <code>                float4 color:COLOR;</code> |
| <a id="l303"></a>303 | <code>            };</code> |
| <a id="l304"></a>304 | <code>            struct v2f</code> |
| <a id="l305"></a>305 | <code>            {</code> |
| <a id="l306"></a>306 | <code>                float4 pos:SV_POSITION; float4 uv:TEXCOORD0;</code> |
| <a id="l307"></a>307 | <code>                float3 worldPos:TEXCOORD1; float3 normal:TEXCOORD2;</code> |
| <a id="l308"></a>308 | <code>                float4 color:COLOR; SHADOW_COORDS(3)</code> |
| <a id="l309"></a>309 | <code>            };</code> |
| <a id="l310"></a>310 | <code>            v2f vert(appdata v)</code> |
| <a id="l311"></a>311 | <code>            {</code> |
| <a id="l312"></a>312 | <code>                v2f o;</code> |
| <a id="l313"></a>313 | <code>                o.pos=UnityObjectToClipPos(v.vertex);</code> |
| <a id="l314"></a>314 | <code>                o.worldPos=mul(unity_ObjectToWorld,v.vertex).xyz;</code> |
| <a id="l315"></a>315 | <code>                o.normal=UnityObjectToWorldNormal(v.normal);</code> |
| <a id="l316"></a>316 | <code>                o.uv.xy=TRANSFORM_TEX(lerp(v.uv,v.uvMirror,step(0.5,_UseMirroredUV)),_MainTex);</code> |
| <a id="l317"></a>317 | <code>                o.uv.zw=v.uv1; o.color=v.color;</code> |
| <a id="l318"></a>318 | <code>                TRANSFER_SHADOW(o);</code> |
| <a id="l319"></a>319 | <code>                return o;</code> |
| <a id="l320"></a>320 | <code>            }</code> |
| <a id="l321"></a>321 | <code>            half4 frag(v2f i, float facing:VFACE):SV_Target</code> |
| <a id="l322"></a>322 | <code>            {</code> |
| <a id="l323"></a>323 | <code>                float3 n=normalize(i.normal)*(facing&gt;=0?1:-1);</code> |
| <a id="l324"></a>324 | <code>                float3 l=normalize(UnityWorldSpaceLightDir(i.worldPos));</code> |
| <a id="l325"></a>325 | <code>                float3 v=normalize(UnityWorldSpaceViewDir(i.worldPos));</code> |
| <a id="l326"></a>326 | <code>                float nl=dot(n,l)*0.5+0.5, nv=saturate(dot(n,v));</code> |
| <a id="l327"></a>327 | <code>                half3 base=tex2D(_MainTex,i.uv.xy).rgb;</code> |
| <a id="l328"></a>328 | <code>                half3 sss=tex2D(_ShadowMap,i.uv.xy).rgb;</code> |
| <a id="l329"></a>329 | <code>                float4 ilm=tex2D(_LightMap,i.uv.xy);</code> |
| <a id="l330"></a>330 | <code>                half3 detail=tex2D(_DetailMap,i.uv.zw).rgb;</code> |
| <a id="l331"></a>331 | <code>                half3 albedo=base*lerp(half3(1,1,1),detail,_DetailIntensity);</code> |
| <a id="l332"></a>332 | <code>// BEGIN GGST EYE REFINEMENT audited atlas gates</code> |
| <a id="l333"></a>333 | <code>                // Pixel-space values are measured in the immutable 2048 atlas.</code> |
| <a id="l334"></a>334 | <code>                // The original small eye and high-detail eye use different UV</code> |
| <a id="l335"></a>335 | <code>                // islands. Current head MPBs cover lowHead and cinematicHair;</code> |
| <a id="l336"></a>336 | <code>                // body material/hood UVs cannot enter this branch.</code> |
| <a id="l337"></a>337 | <code>                float2 eyePixel=float2(i.uv.x*2048.0,(1.0-i.uv.y)*2048.0);</code> |
| <a id="l338"></a>338 | <code>                float eyeHead=saturate(_EyeRefineEnabled)*saturate(_RegionalHead);</code> |
| <a id="l339"></a>339 | <code>                float2 eyeSmallQ=(eyePixel-float2(960.0,64.0))/float2(34.0,34.0);</code> |
| <a id="l340"></a>340 | <code>                float2 eyeLargeQ=(eyePixel-float2(1152.0,130.0))/float2(104.0,100.0);</code> |
| <a id="l341"></a>341 | <code>                float eyeSmallDisk=EyeDisk(eyeSmallQ);</code> |
| <a id="l342"></a>342 | <code>                float eyeLargeDisk=EyeDisk(eyeLargeQ);</code> |
| <a id="l343"></a>343 | <code>                float eyeSmallPupil=smoothstep(1.10,1.24,length((eyePixel-float2(960.0,64.0))/float2(13.0,13.0)));</code> |
| <a id="l344"></a>344 | <code>                float eyeLargePupil=smoothstep(1.10,1.24,length((eyePixel-float2(1152.0,129.0))/float2(29.0,35.0)));</code> |
| <a id="l345"></a>345 | <code>                // Bounded original teal chroma protects black pupils/ink and</code> |
| <a id="l346"></a>346 | <code>                // authored white glints, including compressed texture edges.</code> |
| <a id="l347"></a>347 | <code>                float eyeChroma=smoothstep(0.015,0.055,min(base.g,base.b)-base.r);</code> |
| <a id="l348"></a>348 | <code>                float eyeIrisMask=saturate(eyeSmallDisk+eyeLargeDisk)*eyeSmallPupil*eyeLargePupil*eyeChroma*eyeHead;</code> |
| <a id="l349"></a>349 | <code>                float2 eyeQ=lerp(eyeSmallQ,eyeLargeQ,step(1020.0,eyePixel.x));</code> |
| <a id="l350"></a>350 | <code>                float eyeUp=-eyeQ.y; // PNG y increases downwards.</code> |
| <a id="l351"></a>351 | <code>                float eyeUpper=smoothstep(-0.20,0.55,eyeUp);</code> |
| <a id="l352"></a>352 | <code>                float eyeLower=(1.0-smoothstep(-0.35,0.40,eyeUp))*(1.0-smoothstep(0.75,1.0,length(eyeQ)));</code> |
| <a id="l353"></a>353 | <code>                float eyeEdge=smoothstep(0.56,0.94,length(eyeQ));</code> |
| <a id="l354"></a>354 | <code>                float eyeDomain=step(896.0,eyePixel.x)*step(eyePixel.x,1280.0)*step(0.0,eyePixel.y)*step(eyePixel.y,256.0);</code> |
| <a id="l355"></a>355 | <code>                float3 eyeWhiteDistance=abs(base-half3(0.8388,0.8308,0.9301));</code> |
| <a id="l356"></a>356 | <code>                float eyeNeutral=1.0-smoothstep(0.025,0.065,max(eyeWhiteDistance.r,max(eyeWhiteDistance.g,eyeWhiteDistance.b)));</code> |
| <a id="l357"></a>357 | <code>                float eyeScleraMask=eyeDomain*eyeNeutral*(1.0-saturate(eyeSmallDisk+eyeLargeDisk))*eyeHead;</code> |
| <a id="l358"></a>358 | <code>                // The two small-eye glints already exist in the original base.</code> |
| <a id="l359"></a>359 | <code>                // Do not generate a new moving point. The high-detail eye's</code> |
| <a id="l360"></a>360 | <code>                // separate original HeadGlow/HeadDecal passes stay untouched.</code> |
| <a id="l361"></a>361 | <code>                float eyeAuthoredGlint=saturate(EyeDisk((eyePixel-float2(938.7075,48.0896))/float2(12.0,12.0))+EyeDisk((eyePixel-float2(983.5789,85.5))/float2(8.5,8.5)));</code> |
| <a id="l362"></a>362 | <code>                float eyeCatchMask=eyeAuthoredGlint*smoothstep(0.85,0.97,min(base.r,min(base.g,base.b)))*eyeHead;</code> |
| <a id="l363"></a>363 | <code>// END GGST EYE REFINEMENT audited atlas gates</code> |
| <a id="l364"></a>364 | <code></code> |
| <a id="l365"></a>365 | <code>                float layer=ilm.r*255.0;</code> |
| <a id="l366"></a>366 | <code>                float skin=step(10.0,layer)*(1.0-step(_LayerMaskStep,layer));</code> |
| <a id="l367"></a>367 | <code>                float hair=step(_HairLayerMin,layer)*(1.0-step(_HairLayerMax,layer));</code> |
| <a id="l368"></a>368 | <code>                float leather=step(_LeatherLayerMin,layer)*(1.0-step(_LeatherLayerMax,layer));</code> |
| <a id="l369"></a>369 | <code>                float metal=step(_MetalLayerMin,layer)*(1.0-step(_MetalLayerMax,layer));</code> |
| <a id="l370"></a>370 | <code>                float relativeHeight=(i.worldPos.y-_CharacterOriginWS.y)/max(_CharacterHeight,0.01);</code> |
| <a id="l371"></a>371 | <code>                float lowerHeight=pow(saturate(1.0-smoothstep(_LowerRegionUpper-_LowerRegionFeather,_LowerRegionUpper+_LowerRegionFeather,relativeHeight)),max(_TasteRatePow,0.01));</code> |
| <a id="l372"></a>372 | <code>                float lowerRegion=skin*lowerHeight;</code> |
| <a id="l373"></a>373 | <code>                // Diagnostic-only independent height / horizontal-normal gradient. It is not wired into final color.</code> |
| <a id="l374"></a>374 | <code>                float tasteHeight=saturate(1.0-smoothstep(_TasteHeightStart,_TasteHeightEnd,relativeHeight));</code> |
| <a id="l375"></a>375 | <code>                float tasteHorizontalNormal=saturate(length(n.xz));</code> |
| <a id="l376"></a>376 | <code>                float tasteGradient=pow(saturate(tasteHeight*lerp(1.0,tasteHorizontalNormal,saturate(_TasteNormalWeight))),max(_TasteRatePow,0.01));</code> |
| <a id="l377"></a>377 | <code>                // Diagnostic-only regional light response; it is not wired into final color.</code> |
| <a id="l378"></a>378 | <code>                float3 regionalLight=normalize(_RegionLightDirection.xyz+float3(0,0.00001,0));</code> |
| <a id="l379"></a>379 | <code>                float regionalNl=dot(n,lerp(l,regionalLight,saturate(_RegionLightBlend)))*0.5+0.5;</code> |
| <a id="l380"></a>380 | <code>                float faceRegion=skin*smoothstep(0.58,0.80,relativeHeight);</code> |
| <a id="l381"></a>381 | <code>                float legRegion=skin*(1.0-smoothstep(0.35,0.55,relativeHeight));</code> |
| <a id="l382"></a>382 | <code>                float coatRegion=leather*(1.0-faceRegion);</code> |
| <a id="l383"></a>383 | <code>                // Low-R also contains white material. This color gate is a default-palette hypothesis.</code> |
| <a id="l384"></a>384 | <code>                float warmSkin=smoothstep(0.06,0.10,base.r-base.b)*smoothstep(0.02,0.04,base.r-base.g);</code> |
| <a id="l385"></a>385 | <code>                lowerRegion*=lerp(1.0,warmSkin,saturate(_LowerSkinColorGate));</code> |
| <a id="l386"></a>386 | <code>                float3 lowerLight=normalize(_LowerLightDirection.xyz+float3(0,0.00001,0));</code> |
| <a id="l387"></a>387 | <code>                lowerLight=normalize(lerp(lowerLight,l,saturate(_LowerLightDynamic)));</code> |
| <a id="l388"></a>388 | <code>                l=normalize(lerp(l,lowerLight,saturate(_LowerLightBlend*lowerRegion)));</code> |
| <a id="l389"></a>389 | <code>                nl=dot(n,l)*0.5+0.5;</code> |
| <a id="l390"></a>390 | <code>                // These are configurable reconstruction hypotheses, not the original GPU equations.</code> |
| <a id="l391"></a>391 | <code>                float ao=lerp(1.0,saturate(i.color.r),_AOStrength);</code> |
| <a id="l392"></a>392 | <code>                float signal=(nl+_RampOffset+(ilm.g-_RampMaskCenter)*_RampMaskStrength+skin*_SkinShadowOffset)*ao;</code> |
| <a id="l393"></a>393 | <code>                float soft=max(_ShadowSoftness,0.00001);</code> |
| <a id="l394"></a>394 | <code>                float band=smoothstep(_LightTreshold-soft,_LightTreshold+soft,signal);</code> |
| <a id="l395"></a>395 | <code>                float rawShadow=SHADOW_ATTENUATION(i);</code> |
| <a id="l396"></a>396 | <code>                float projected=lerp(1.0,rawShadow,_ReceiveShadowStrength);</code> |
| <a id="l397"></a>397 | <code>                band*=projected;</code> |
| <a id="l398"></a>398 | <code>                half3 dark=lerp(albedo,sss*_ShadowTint.rgb,_ShadowIntensity);</code> |
| <a id="l399"></a>399 | <code>                // Reconstructed regional second shade; not the stripped native shader expression.</code> |
| <a id="l400"></a>400 | <code>                float secondShade=lowerRegion*(1.0-band)*(1.0-smoothstep(_SecondShadowThreshold-0.06,_SecondShadowThreshold+0.06,dot(n,l)));</code> |
| <a id="l401"></a>401 | <code>                dark*=lerp(half3(1,1,1),_SecondShadowTint.rgb,secondShade*_SecondShadowStrength);</code> |
| <a id="l402"></a>402 | <code>                // Independent atlas masks keep face/skin/sleeve changes out of hair,</code> |
| <a id="l403"></a>403 | <code>                // eye whites, the hood band, socks, blue coat and metal. No mesh data</code> |
| <a id="l404"></a>404 | <code>                // or skinning equations are changed by this rendering-only branch.</code> |
| <a id="l405"></a>405 | <code>                float2 region=saturate(tex2D(_RegionalMask,i.uv.xy).rg)*saturate(_RegionalEnabled);</code> |
| <a id="l406"></a>406 | <code>                float head=saturate(_RegionalHead);</code> |
| <a id="l407"></a>407 | <code>                float faceRegionMask=region.r*head;</code> |
| <a id="l408"></a>408 | <code>                float bodySkinRegion=region.r*(1.0-head);</code> |
| <a id="l409"></a>409 | <code>                float sleeveRegion=region.g*(1.0-head);</code> |
| <a id="l410"></a>410 | <code>                float regionTotal=saturate(faceRegionMask+bodySkinRegion+sleeveRegion);</code> |
| <a id="l411"></a>411 | <code>                float regionalSignal=(nl+_RampOffset+(ilm.g-_RampMaskCenter)*_RampMaskStrength)*ao;</code> |
| <a id="l412"></a>412 | <code>                float regionSoft=max(_RegionalSoftness,0.001);</code> |
| <a id="l413"></a>413 | <code>                float faceBand=smoothstep(_FaceShadeThreshold-regionSoft,_FaceShadeThreshold+regionSoft,regionalSignal);</code> |
| <a id="l414"></a>414 | <code>                // Artist-controlled lateral face shading in a read-only head frame.</code> |
| <a id="l415"></a>415 | <code>                // Main light selects the far cheek. It follows the existing Step</code> |
| <a id="l416"></a>416 | <code>                // pose directly; no temporal interpolation or bone writes.</code> |
| <a id="l417"></a>417 | <code>                float3 faceRight=normalize(_FaceRightWS.xyz+float3(0.000001,0,0));</code> |
| <a id="l418"></a>418 | <code>                float faceX=dot(i.worldPos-_FaceOriginWS.xyz,faceRight)/max(_FaceRightWS.w,0.001);</code> |
| <a id="l419"></a>419 | <code>                float lightSide=dot(l,faceRight);</code> |
| <a id="l420"></a>420 | <code>                float lateral=smoothstep(0.12,0.48,abs(lightSide));</code> |
| <a id="l421"></a>421 | <code>                float sideBoundary=lerp(0.92,0.30,lateral);</code> |
| <a id="l422"></a>422 | <code>                float farCheek=-faceX*(lightSide&gt;=0?1.0:-1.0);</code> |
| <a id="l423"></a>423 | <code>                float cheekShade=smoothstep(sideBoundary-0.07,sideBoundary+0.07,farCheek)*smoothstep(0.04,0.18,abs(lightSide));</code> |
| <a id="l424"></a>424 | <code>                faceBand=min(faceBand,1.0-cheekShade*_FaceSideStrength*saturate(_FaceFrameValid));</code> |
| <a id="l425"></a>425 | <code>                float skinBand=smoothstep(_SkinShadeThreshold-regionSoft,_SkinShadeThreshold+regionSoft,regionalSignal);</code> |
| <a id="l426"></a>426 | <code>                float sleeveBand=smoothstep(_SleeveShadeThreshold-regionSoft,_SleeveShadeThreshold+regionSoft,regionalSignal);</code> |
| <a id="l427"></a>427 | <code>                float regionalBand=faceBand*faceRegionMask+skinBand*bodySkinRegion+sleeveBand*sleeveRegion;</code> |
| <a id="l428"></a>428 | <code>                half3 faceDark=lerp(albedo,sss*_FaceShadeTint.rgb,saturate(_FaceShadeStrength));</code> |
| <a id="l429"></a>429 | <code>                half3 skinDark=lerp(albedo,albedo*_SkinShadeTint.rgb,saturate(_SkinShadeStrength));</code> |
| <a id="l430"></a>430 | <code>                half3 sleeveDark=lerp(albedo,albedo*_SleeveShadeTint.rgb,saturate(_SleeveShadeStrength));</code> |
| <a id="l431"></a>431 | <code>                half3 regionalDark=faceDark*faceRegionMask+skinDark*bodySkinRegion+sleeveDark*sleeveRegion;</code> |
| <a id="l432"></a>432 | <code>                // Weighted replacement, not a second layer of the old empirical red</code> |
| <a id="l433"></a>433 | <code>                // height tint. Preserve unmasked material lighting exactly.</code> |
| <a id="l434"></a>434 | <code>                float safeRegion=max(regionTotal,0.0001);</code> |
| <a id="l435"></a>435 | <code>                band=lerp(band,(regionalBand/safeRegion)*projected,regionTotal);</code> |
| <a id="l436"></a>436 | <code>                dark=lerp(dark,regionalDark/safeRegion,regionTotal);</code> |
| <a id="l437"></a>437 | <code>                half3 diffuse=lerp(dark,albedo,band)*_LightColor0.rgb*_LightIntensity;</code> |
| <a id="l438"></a>438 | <code>// BEGIN GGST SHADOW REFINEMENT true hair occlusion only in face diffuse</code> |
| <a id="l439"></a>439 | <code>                float hairVisibility=ReadHairVisibility(i.worldPos);</code> |
| <a id="l440"></a>440 | <code>                float hairFaceOcclusion=(1.0-hairVisibility)*faceRegionMask*saturate(_FaceFrameValid)*saturate(_HairFaceShadowStrength);</code> |
| <a id="l441"></a>441 | <code>                // Reuse the approved face dark tone. Its union with an existing</code> |
| <a id="l442"></a>442 | <code>                // dark face region does not multiply the same shade twice.</code> |
| <a id="l443"></a>443 | <code>                diffuse=lerp(diffuse,faceDark*_LightColor0.rgb*_LightIntensity,hairFaceOcclusion);</code> |
| <a id="l444"></a>444 | <code>// END GGST SHADOW REFINEMENT true hair occlusion only in face diffuse</code> |
| <a id="l445"></a>445 | <code>// BEGIN GGST FACE DIFFUSE replacement</code> |
| <a id="l446"></a>446 | <code>// Refine diffuse only. Keep the established band intact for</code> |
| <a id="l447"></a>447 | <code>                // highlights/rim/eyes, and retain the original hair visibility.</code> |
| <a id="l448"></a>448 | <code>                // The existing atlas gate excludes hair, clothing and eye UVs.</code> |
| <a id="l449"></a>449 | <code>                float faceRefineGate=faceRegionMask*saturate(_FaceFrameValid)*saturate(_FaceDiffuseRefine);</code> |
| <a id="l450"></a>450 | <code>                float faceBoundary=lerp(0.92,_FaceDiffuseBoundary,lateral);</code> |
| <a id="l451"></a>451 | <code>                float faceEdge=max(_FaceDiffuseEdge,fwidth(farCheek)*0.55);</code> |
| <a id="l452"></a>452 | <code>                float faceSideShade=smoothstep(faceBoundary-faceEdge,faceBoundary+faceEdge,farCheek)*smoothstep(0.04,0.18,abs(lightSide));</code> |
| <a id="l453"></a>453 | <code>                float faceDiffuseBand=min(smoothstep(_FaceShadeThreshold-regionSoft,_FaceShadeThreshold+regionSoft,regionalSignal),1.0-faceSideShade*_FaceDiffuseSide);</code> |
| <a id="l454"></a>454 | <code>                half3 faceDiffuseDark=lerp(albedo,sss*_FaceDiffuseTint.rgb,saturate(_FaceDiffuseDepth));</code> |
| <a id="l455"></a>455 | <code>                half3 faceDiffuseOld=lerp(faceDark,albedo,faceBand*projected)*_LightColor0.rgb*_LightIntensity;</code> |
| <a id="l456"></a>456 | <code>                half3 faceDiffuseNew=lerp(faceDiffuseDark,albedo,faceDiffuseBand*projected)*_LightColor0.rgb*_LightIntensity;</code> |
| <a id="l457"></a>457 | <code>                half3 faceDiffuseDelta=(faceDiffuseNew-faceDiffuseOld)*faceRefineGate*(1.0-hairFaceOcclusion);</code> |
| <a id="l458"></a>458 | <code>                diffuse+=faceDiffuseDelta;</code> |
| <a id="l459"></a>459 | <code>// END GGST FACE DIFFUSE replacement</code> |
| <a id="l460"></a>460 | <code></code> |
| <a id="l461"></a>461 | <code>// BEGIN GGST PALETTE diffuse only</code> |
| <a id="l462"></a>462 | <code>                // Immutable atlas cream swatch, verified against original body</code> |
| <a id="l463"></a>463 | <code>                // UVs. Exclude hood, socks, hair and other head renderers.</code> |
| <a id="l464"></a>464 | <code>                float2 palettePixel=float2(i.uv.x*2048.0,(1.0-i.uv.y)*2048.0);</code> |
| <a id="l465"></a>465 | <code>                float tunicUpper=step(768.5,palettePixel.x)*step(palettePixel.x,895.5)*step(640.5,palettePixel.y)*step(palettePixel.y,895.5);</code> |
| <a id="l466"></a>466 | <code>                float tunicLower=step(512.5,palettePixel.x)*step(palettePixel.x,895.5)*step(895.5,palettePixel.y)*step(palettePixel.y,1343.5);</code> |
| <a id="l467"></a>467 | <code>                float tunicRegion=saturate(tunicUpper+tunicLower)*(1.0-head)*saturate(_RegionalEnabled);</code> |
| <a id="l468"></a>468 | <code>                float paletteSkin=faceRegionMask+bodySkinRegion;</code> |
| <a id="l469"></a>469 | <code>                float paletteSkinBand=lerp(saturate(skinBand*projected),saturate(lerp(faceBand,faceDiffuseBand,saturate(_FaceDiffuseRefine))*projected),head);</code> |
| <a id="l470"></a>470 | <code>                float3 paletteSkinMultiplier=lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,paletteSkinBand);</code> |
| <a id="l471"></a>471 | <code>                float3 paletteSleeveMultiplier=lerp(_PaletteSleeveDark.rgb,_PaletteSleeveLight.rgb,saturate(sleeveBand*projected));</code> |
| <a id="l472"></a>472 | <code>                float3 paletteTunicMultiplier=lerp(_PaletteTunicDark.rgb,_PaletteTunicLight.rgb,saturate(band));</code> |
| <a id="l473"></a>473 | <code>                float3 paletteMultiplier=1.0+(paletteSkinMultiplier-1.0)*paletteSkin+(paletteSleeveMultiplier-1.0)*sleeveRegion+(paletteTunicMultiplier-1.0)*tunicRegion;</code> |
| <a id="l474"></a>474 | <code>                float3 paletteGate=float3(paletteSkin,sleeveRegion,tunicRegion);</code> |
| <a id="l475"></a>475 | <code>                // Do not recolor albedo, band, ambient, specular, rim or ink.</code> |
| <a id="l476"></a>476 | <code>                diffuse*=lerp(float3(1,1,1),paletteMultiplier,saturate(_PaletteEnabled));</code> |
| <a id="l477"></a>477 | <code>// END GGST PALETTE diffuse only</code> |
| <a id="l478"></a>478 | <code></code> |
| <a id="l479"></a>479 | <code>// BEGIN GGST CLEAN SHADE diffuse replacement</code> |
| <a id="l480"></a>480 | <code>                // Only the character's diffuse lobe is reconstructed here.</code> |
| <a id="l481"></a>481 | <code>                // Leave band/albedo/normal and every existing rim/spec/ink</code> |
| <a id="l482"></a>482 | <code>                // equation untouched. Scene shadow casters/receivers also stay.</code> |
| <a id="l483"></a>483 | <code>                float cleanFaceBand=smoothstep(_CleanFaceUnderStart,_CleanFaceUnderEnd,n.y);</code> |
| <a id="l484"></a>484 | <code>                float cleanSkinBand=skinBand;</code> |
| <a id="l485"></a>485 | <code>                float cleanClothSignal=(nl+_RampOffset+(ilm.g-_RampMaskCenter)*_RampMaskStrength*_CleanClothMaskWeight)*lerp(1.0,ao,_CleanClothAOWeight);</code> |
| <a id="l486"></a>486 | <code>                float cleanClothBand=smoothstep(_LightTreshold-_CleanClothSoftness,_LightTreshold+_CleanClothSoftness,cleanClothSignal);</code> |
| <a id="l487"></a>487 | <code>                float cleanSleeveBand=smoothstep(_SleeveShadeThreshold-_CleanClothSoftness,_SleeveShadeThreshold+_CleanClothSoftness,cleanClothSignal);</code> |
| <a id="l488"></a>488 | <code>                float cleanTunicBand=cleanClothBand;</code> |
| <a id="l489"></a>489 | <code>                float cleanClothClass=saturate(tex2D(_FourMaterialSpecMask,i.uv.xy).g)*saturate(_FourMaterialSpecEnabled)*(1.0-head);</code> |
| <a id="l490"></a>490 | <code>                float cleanOtherCloth=cleanClothClass*(1.0-saturate(paletteSkin+sleeveRegion+tunicRegion));</code> |
| <a id="l491"></a>491 | <code>                float cleanTotal=paletteSkin+sleeveRegion+tunicRegion+cleanOtherCloth;</code> |
| <a id="l492"></a>492 | <code>                float cleanCoverage=saturate(cleanTotal);</code> |
| <a id="l493"></a>493 | <code>                float3 cleanGate=float3(faceRegionMask,bodySkinRegion,saturate(sleeveRegion+tunicRegion+cleanOtherCloth));</code> |
| <a id="l494"></a>494 | <code>                half3 cleanClothDark=lerp(albedo,sss*_ShadowTint.rgb,_ShadowIntensity);</code> |
| <a id="l495"></a>495 | <code>                half3 cleanFace=lerp(faceDiffuseDark,albedo,cleanFaceBand)*lerp(float3(1,1,1),lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,cleanFaceBand),saturate(_PaletteEnabled));</code> |
| <a id="l496"></a>496 | <code>                half3 cleanSkin=lerp(skinDark,albedo,cleanSkinBand)*lerp(float3(1,1,1),lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,cleanSkinBand),saturate(_PaletteEnabled));</code> |
| <a id="l497"></a>497 | <code>                half3 cleanSleeve=lerp(sleeveDark,albedo,cleanSleeveBand)*lerp(float3(1,1,1),lerp(_PaletteSleeveDark.rgb,_PaletteSleeveLight.rgb,cleanSleeveBand),saturate(_PaletteEnabled));</code> |
| <a id="l498"></a>498 | <code>                half3 cleanTunic=lerp(cleanClothDark,albedo,cleanTunicBand)*lerp(float3(1,1,1),lerp(_PaletteTunicDark.rgb,_PaletteTunicLight.rgb,cleanTunicBand),saturate(_PaletteEnabled));</code> |
| <a id="l499"></a>499 | <code>                half3 cleanCloth=lerp(cleanClothDark,albedo,cleanClothBand);</code> |
| <a id="l500"></a>500 | <code>                half3 cleanDiffuse=(cleanFace*faceRegionMask+cleanSkin*bodySkinRegion+cleanSleeve*sleeveRegion+cleanTunic*tunicRegion+cleanCloth*cleanOtherCloth)/max(cleanTotal,0.0001)*_LightColor0.rgb*_LightIntensity;</code> |
| <a id="l501"></a>501 | <code>                diffuse=lerp(diffuse,cleanDiffuse,saturate(_CleanShadeEnabled)*cleanCoverage);</code> |
| <a id="l502"></a>502 | <code>// END GGST CLEAN SHADE diffuse replacement</code> |
| <a id="l503"></a>503 | <code></code> |
| <a id="l504"></a>504 | <code>// BEGIN GGST FOCUSED LIGHT diffuse bands</code> |
| <a id="l505"></a>505 | <code>                // UV region verified against the immutable original leg skin</code> |
| <a id="l506"></a>506 | <code>                // weights. Atlas-based boundaries follow every existing pose.</code> |
| <a id="l507"></a>507 | <code>                float focusedLegDomain=step(200.0,palettePixel.x)*step(palettePixel.x,510.0)*step(880.0,palettePixel.y)*step(palettePixel.y,1195.0);</code> |
| <a id="l508"></a>508 | <code>                float focusedLegRegion=bodySkinRegion*focusedLegDomain;</code> |
| <a id="l509"></a>509 | <code>                float focusedCalf=smoothstep(1035.0,1070.0,palettePixel.y);</code> |
| <a id="l510"></a>510 | <code>                float focusedKnee=smoothstep(1015.0,1035.0,palettePixel.y)*(1.0-smoothstep(1055.0,1075.0,palettePixel.y));</code> |
| <a id="l511"></a>511 | <code>                float focusedLegThreshold=lerp(_FocusedThighThreshold,_FocusedCalfThreshold,focusedCalf);</code> |
| <a id="l512"></a>512 | <code>                focusedLegThreshold=lerp(focusedLegThreshold,_FocusedKneeThreshold,focusedKnee);</code> |
| <a id="l513"></a>513 | <code>                float focusedLegBand=smoothstep(focusedLegThreshold-regionSoft,focusedLegThreshold+regionSoft,regionalSignal);</code> |
| <a id="l514"></a>514 | <code>                float focusedSkinBand=lerp(cleanSkinBand,focusedLegBand,focusedLegDomain*saturate(_FocusedShadeEnabled));</code> |
| <a id="l515"></a>515 | <code>                float focusedTunicBand=lerp(cleanTunicBand,smoothstep(_FocusedTunicThreshold-_CleanClothSoftness,_FocusedTunicThreshold+_CleanClothSoftness,cleanClothSignal),saturate(_FocusedShadeEnabled));</code> |
| <a id="l516"></a>516 | <code>                half3 focusedSkin=lerp(skinDark,albedo,focusedSkinBand)*lerp(float3(1,1,1),lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,focusedSkinBand),saturate(_PaletteEnabled));</code> |
| <a id="l517"></a>517 | <code>                half3 focusedTunic=lerp(cleanClothDark,albedo,focusedTunicBand)*lerp(float3(1,1,1),lerp(_PaletteTunicDark.rgb,_PaletteTunicLight.rgb,focusedTunicBand),saturate(_PaletteEnabled));</code> |
| <a id="l518"></a>518 | <code>                diffuse+=((focusedSkin-cleanSkin)*focusedLegRegion+(focusedTunic-cleanTunic)*tunicRegion)/max(cleanTotal,0.0001)*_LightColor0.rgb*_LightIntensity*saturate(_CleanShadeEnabled)*cleanCoverage;</code> |
| <a id="l519"></a>519 | <code>// END GGST FOCUSED LIGHT diffuse bands</code> |
| <a id="l520"></a>520 | <code></code> |
| <a id="l521"></a>521 | <code>// BEGIN GGST EYE REFINEMENT diffuse layers</code> |
| <a id="l522"></a>522 | <code>                half3 eyeBeforeDiffuse=diffuse;</code> |
| <a id="l523"></a>523 | <code>                float eyeDepth=saturate(_EyeIrisUpperDepth*eyeUpper+_EyeIrisEdgeDepth*eyeEdge);</code> |
| <a id="l524"></a>524 | <code>                diffuse*=1.0-eyeIrisMask*eyeDepth;</code> |
| <a id="l525"></a>525 | <code>                // Reuse the original iris hue and the same lit/shadow band.</code> |
| <a id="l526"></a>526 | <code>                // No emission or time-driven sparkle is introduced.</code> |
| <a id="l527"></a>527 | <code>                diffuse+=albedo*half3(0.70,1.0,0.92)*_LightColor0.rgb*_LightIntensity*band*eyeIrisMask*eyeLower*_EyeIrisLowerLift;</code> |
| <a id="l528"></a>528 | <code>                diffuse*=lerp(half3(1,1,1),half3(0.70,0.85,1.0),eyeScleraMask*_EyeScleraShade);</code> |
| <a id="l529"></a>529 | <code>                half3 eyeDiffuseDelta=diffuse-eyeBeforeDiffuse;</code> |
| <a id="l530"></a>530 | <code>// END GGST EYE REFINEMENT diffuse layers</code> |
| <a id="l531"></a>531 | <code></code> |
| <a id="l532"></a>532 | <code>                // Give ambient its own small, explicit contribution instead of washing out every lit region.</code> |
| <a id="l533"></a>533 | <code>                half3 ambient=UNITY_LIGHTMODEL_AMBIENT.rgb*albedo*_AmbientStrength;</code> |
| <a id="l534"></a>534 | <code>                float rimEdge=smoothstep(1.0-_RimWidth,1.0-_RimWidth+0.035,1.0-nv);</code> |
| <a id="l535"></a>535 | <code>                half3 rim=rimEdge*_RimIntensity*albedo*band*_LightColor0.rgb;</code> |
| <a id="l536"></a>536 | <code>                // BEGIN GGST SPECULAR REFINEMENT calculations</code> |
| <a id="l537"></a>537 | <code>                float nh=saturate(dot(n,normalize(l+v)));</code> |
| <a id="l538"></a>538 | <code>                half3 spec=pow(nh,_SpecularPower)*_SpecularIntensity*ilm.b*albedo;</code> |
| <a id="l539"></a>539 | <code>                float maskByte=ilm.b*255.0;</code> |
| <a id="l540"></a>540 | <code>                float bodyMask=saturate(skin+leather)*step(0.5,maskByte)*(1.0-step(140.5,maskByte));</code> |
| <a id="l541"></a>541 | <code>                float hairMask=hair*step(140.5,maskByte);</code> |
| <a id="l542"></a>542 | <code>                spec=lerp(spec,step(1.0-_BodySpecularWidth,1.0-nv)*_BodySpecularIntensity*albedo,bodyMask);</code> |
| <a id="l543"></a>543 | <code>                spec=lerp(spec,step(1.0-_HeadSpecularWidth,nv)*_HeadSpecularIntensity*albedo,hairMask);</code> |
| <a id="l544"></a>544 | <code>                spec+=metal*step(1.0-_MetallicStepSpecularWidth,nl)*_MetallicStepSpecularIntensity*ilm.b*albedo;</code> |
| <a id="l545"></a>545 | <code>                spec*=_LightColor0.rgb*band;</code> |
| <a id="l546"></a>546 | <code>                // Keep the exact original specular expression above as the</code> |
| <a id="l547"></a>547 | <code>                // fallback for eyes, lips and other intentionally unclassified UVs.</code> |
| <a id="l548"></a>548 | <code>                float4 specClass=saturate(tex2D(_FourMaterialSpecMask,i.uv.xy))*saturate(_FourMaterialSpecEnabled);</code> |
| <a id="l549"></a>549 | <code>                float specCoverage=saturate(specClass.r+specClass.g+specClass.b+specClass.a);</code> |
| <a id="l550"></a>550 | <code>                float shineAA=max(fwidth(nh)*0.65,0.006);</code> |
| <a id="l551"></a>551 | <code>                float paintedShine=saturate(ilm.b);</code> |
| <a id="l552"></a>552 | <code>                float hairShoulder=smoothstep(1.0-_HairShineWidth-shineAA,1.0-_HairShineWidth+shineAA,nh);</code> |
| <a id="l553"></a>553 | <code>                float hairCore=smoothstep(1.0-_HairShineWidth*0.28-shineAA,1.0-_HairShineWidth*0.28+shineAA,nh);</code> |
| <a id="l554"></a>554 | <code>                // ILM.B is sparse authored highlight detail, not whole-surface</code> |
| <a id="l555"></a>555 | <code>                // reflectance. A weak base and localized painted core stay separate.</code> |
| <a id="l556"></a>556 | <code>                float hairShape=0.22*hairShoulder+0.78*paintedShine*(0.4*hairShoulder+0.6*hairCore);</code> |
| <a id="l557"></a>557 | <code>                half3 shineHair=lerp(albedo,_HairShineTint.rgb,0.32)*_HairShineStrength*hairShape;</code> |
| <a id="l558"></a>558 | <code>                float clothShape=pow(nh,max(_ClothShinePower,2.0))*(0.30+0.70*paintedShine);</code> |
| <a id="l559"></a>559 | <code>                half3 shineCloth=albedo*_ClothShineTint.rgb*_ClothShineStrength*clothShape;</code> |
| <a id="l560"></a>560 | <code>                float skinShape=pow(nh,max(_SkinShinePower,4.0))*(0.25+0.75*paintedShine);</code> |
| <a id="l561"></a>561 | <code>                half3 shineSkin=lerp(albedo,_SkinShineTint.rgb,0.12)*_SkinShineStrength*skinShape;</code> |
| <a id="l562"></a>562 | <code>                float metalShoulder=smoothstep(1.0-_MetalShineWidth-shineAA,1.0-_MetalShineWidth+shineAA,nh);</code> |
| <a id="l563"></a>563 | <code>                float metalCore=smoothstep(1.0-_MetalShineWidth*0.23-shineAA,1.0-_MetalShineWidth*0.23+shineAA,nh);</code> |
| <a id="l564"></a>564 | <code>                float metalShape=(0.23*metalShoulder+0.77*metalCore)*(0.55+0.45*paintedShine);</code> |
| <a id="l565"></a>565 | <code>                half3 shineMetal=lerp(albedo,half3(1,1,1),0.38)*_MetalShineTint.rgb*_MetalShineStrength*metalShape;</code> |
| <a id="l566"></a>566 | <code>                half3 classifiedSpec=(shineHair*specClass.r+shineCloth*specClass.g+shineSkin*specClass.b+shineMetal*specClass.a)*_LightColor0.rgb*band;</code> |
| <a id="l567"></a>567 | <code>                spec=spec*(1.0-specCoverage)+classifiedSpec;</code> |
| <a id="l568"></a>568 | <code>                // END GGST SPECULAR REFINEMENT calculations</code> |
| <a id="l569"></a>569 | <code>// BEGIN GGST FOCUSED LIGHT specular replacement</code> |
| <a id="l570"></a>570 | <code>                // Preserve the previous rim's band. Only the specular lobe</code> |
| <a id="l571"></a>571 | <code>                // uses the unoccluded diffuse bands; eye/face glints are excluded.</code> |
| <a id="l572"></a>572 | <code>                float focusedUnoccluded=smoothstep(_LightTreshold-soft,_LightTreshold+soft,signal);</code> |
| <a id="l573"></a>573 | <code>                float focusedRegional=(cleanFaceBand*faceRegionMask+focusedSkinBand*bodySkinRegion+cleanSleeveBand*sleeveRegion+focusedTunicBand*tunicRegion+cleanClothBand*cleanOtherCloth)/max(cleanTotal,0.0001);</code> |
| <a id="l574"></a>574 | <code>                float focusedSpecBand=lerp(focusedUnoccluded,focusedRegional,saturate(_CleanShadeEnabled)*cleanCoverage);</code> |
| <a id="l575"></a>575 | <code>                float focusedSkinAA=max(fwidth(nh)*0.65,0.008);</code> |
| <a id="l576"></a>576 | <code>                float focusedSkinShoulder=smoothstep(1.0-_FocusedSkinWidth-focusedSkinAA,1.0-_FocusedSkinWidth+focusedSkinAA,nh);</code> |
| <a id="l577"></a>577 | <code>                float focusedSkinCore=smoothstep(1.0-_FocusedSkinWidth*0.45-focusedSkinAA,1.0-_FocusedSkinWidth*0.45+focusedSkinAA,nh);</code> |
| <a id="l578"></a>578 | <code>                half3 focusedSkinShine=lerp(albedo,_SkinShineTint.rgb,0.12)*_FocusedSkinStrength*(0.8*focusedSkinShoulder+0.2*focusedSkinCore)*(0.7+0.3*paintedShine);</code> |
| <a id="l579"></a>579 | <code>                focusedSkinShine=lerp(shineSkin,focusedSkinShine,focusedLegDomain*(1.0-head));</code> |
| <a id="l580"></a>580 | <code>// BEGIN GGST THIGH LOBE specular</code> |
| <a id="l581"></a>581 | <code>                // Immutable skin UVs place the painted lobe on the upper thigh.</code> |
| <a id="l582"></a>582 | <code>                // The taper follows the existing skinning without modifying mesh data.</code> |
| <a id="l583"></a>583 | <code>                float thighT=saturate((palettePixel.y-918.0)/82.0);</code> |
| <a id="l584"></a>584 | <code>                // Follow the measured anterior meridian of the original UV island;</code> |
| <a id="l585"></a>585 | <code>                // its ring spacing bends at y=981, so a straight UV line is not</code> |
| <a id="l586"></a>586 | <code>                // a straight line on the existing thigh surface.</code> |
| <a id="l587"></a>587 | <code>                float thighCenter=357.89;</code> |
| <a id="l588"></a>588 | <code>                thighCenter+=(-0.44)*saturate((palettePixel.y-916.85)/11.84);</code> |
| <a id="l589"></a>589 | <code>                thighCenter+=(-1.35)*saturate((palettePixel.y-928.69)/12.07);</code> |
| <a id="l590"></a>590 | <code>                thighCenter+=(-1.70)*saturate((palettePixel.y-940.76)/13.24);</code> |
| <a id="l591"></a>591 | <code>                thighCenter+=(-1.90)*saturate((palettePixel.y-954.0)/13.74);</code> |
| <a id="l592"></a>592 | <code>                thighCenter+=(4.90)*saturate((palettePixel.y-967.74)/13.89);</code> |
| <a id="l593"></a>593 | <code>                thighCenter+=(-1.30)*saturate((palettePixel.y-981.63)/9.42);</code> |
| <a id="l594"></a>594 | <code>                thighCenter+=(-1.24)*saturate((palettePixel.y-991.05)/9.62);</code> |
| <a id="l595"></a>595 | <code>                float thighHalfWidth=7.2*(1.0-pow(thighT,1.15));</code> |
| <a id="l596"></a>596 | <code>                float thighEdge=thighHalfWidth-abs(palettePixel.x-thighCenter);</code> |
| <a id="l597"></a>597 | <code>                float thighAA=max(fwidth(thighEdge)*0.65,0.35);</code> |
| <a id="l598"></a>598 | <code>                float thighLobe=smoothstep(-thighAA,thighAA,thighEdge);</code> |
| <a id="l599"></a>599 | <code>                thighLobe*=smoothstep(916.0,920.0,palettePixel.y)*(1.0-smoothstep(998.0,1001.0,palettePixel.y));</code> |
| <a id="l600"></a>600 | <code>                float thighReplace=focusedLegDomain*(1.0-head)*(1.0-smoothstep(1015.0,1030.0,palettePixel.y));</code> |
| <a id="l601"></a>601 | <code>                float thighFacing=smoothstep(0.2,0.55,nv)*smoothstep(0.50,0.68,nl);</code> |
| <a id="l602"></a>602 | <code>                half3 thighShine=_ThighLobeTint.rgb*_ThighLobeStrength*thighLobe*thighFacing;</code> |
| <a id="l603"></a>603 | <code>                focusedSkinShine=lerp(focusedSkinShine,thighShine,thighReplace*saturate(_ThighLobeEnabled));</code> |
| <a id="l604"></a>604 | <code>// END GGST THIGH LOBE specular</code> |
| <a id="l605"></a>605 | <code>                float4 focusedClasses=specClass*float4(1,1,1.0-faceRegionMask,1);</code> |
| <a id="l606"></a>606 | <code>                float focusedSpecCoverage=saturate(dot(focusedClasses,float4(1,1,1,1)));</code> |
| <a id="l607"></a>607 | <code>                half3 focusedOldSpec=(shineHair*focusedClasses.r+shineCloth*focusedClasses.g+shineSkin*focusedClasses.b+shineMetal*focusedClasses.a)*_LightColor0.rgb*band;</code> |
| <a id="l608"></a>608 | <code>                half3 focusedNewSpec=(shineHair*_FocusedHairGain*focusedClasses.r+shineCloth*_FocusedClothGain*focusedClasses.g+focusedSkinShine*focusedClasses.b+shineMetal*_FocusedMetalGain*focusedClasses.a)*_LightColor0.rgb*focusedSpecBand;</code> |
| <a id="l609"></a>609 | <code>                spec+=(focusedNewSpec-focusedOldSpec)*saturate(_FocusedSpecEnabled);</code> |
| <a id="l610"></a>610 | <code>// END GGST FOCUSED LIGHT specular replacement</code> |
| <a id="l611"></a>611 | <code></code> |
| <a id="l612"></a>612 | <code>// BEGIN GGST RIM REFINE calculations</code> |
| <a id="l613"></a>613 | <code>                // Artistic rim only: preserve the approved diffuse, specular,</code> |
| <a id="l614"></a>614 | <code>                // eye, ink and shadow computations and the original fallback.</code> |
| <a id="l615"></a>615 | <code>                // Material atlas excludes eyes/lips; face receives a softer rim.</code> |
| <a id="l616"></a>616 | <code>                float rimAA=max(fwidth(nv)*0.65,0.008);</code> |
| <a id="l617"></a>617 | <code>                float referenceRimEdge=1.0-smoothstep(_ReferenceRimWidth-rimAA,_ReferenceRimWidth+rimAA,nv);</code> |
| <a id="l618"></a>618 | <code>                float rimMaterialScale=dot(specClass,_ReferenceRimMaterial)/max(specCoverage,0.0001);</code> |
| <a id="l619"></a>619 | <code>                rimMaterialScale*=lerp(1.0,_ReferenceRimFaceScale,faceRegionMask);</code> |
| <a id="l620"></a>620 | <code>                half3 referenceRimColor=lerp(albedo,_ReferenceRimTint.rgb,_ReferenceRimTintMix);</code> |
| <a id="l621"></a>621 | <code>                float referenceRimLight=lerp(_ReferenceRimShadowFloor,1.0,saturate(band));</code> |
| <a id="l622"></a>622 | <code>                half3 referenceRim=referenceRimColor*referenceRimEdge*_ReferenceRimStrength*rimMaterialScale*referenceRimLight*_LightColor0.rgb;</code> |
| <a id="l623"></a>623 | <code>                rim=lerp(rim,referenceRim,saturate(_ReferenceRimEnabled)*specCoverage);</code> |
| <a id="l624"></a>624 | <code>// END GGST RIM REFINE calculations</code> |
| <a id="l625"></a>625 | <code>                half3 color=diffuse+ambient+rim+spec;</code> |
| <a id="l626"></a>626 | <code>                // Restore verified line-shaped Alpha data after lighting, so rim does not erase ink.</code> |
| <a id="l627"></a>627 | <code>// BEGIN GGST LINE REFINEMENT save lighting and specular</code> |
| <a id="l628"></a>628 | <code>                half3 lineBaseColor=color;</code> |
| <a id="l629"></a>629 | <code>// END GGST LINE REFINEMENT save lighting and specular</code> |
| <a id="l630"></a>630 | <code>                color=lerp(color,_InnerLineColor.rgb,(1.0-saturate(ilm.a))*_InnerLineStrength);</code> |
| <a id="l631"></a>631 | <code>// BEGIN GGST LINE REFINEMENT internal line</code> |
| <a id="l632"></a>632 | <code>                float4 inkClass=saturate(tex2D(_FourMaterialSpecMask,i.uv.xy));</code> |
| <a id="l633"></a>633 | <code>                float inkClassTotal=dot(inkClass,float4(1,1,1,1));</code> |
| <a id="l634"></a>634 | <code>                float inkCoverage=saturate(inkClassTotal)*step(0.5,_LineRefineEnabled);</code> |
| <a id="l635"></a>635 | <code>                float rawInk=1.0-saturate(ilm.a);</code> |
| <a id="l636"></a>636 | <code>                // Only Alpha receives screen-footprint filtering. Original ILM</code> |
| <a id="l637"></a>637 | <code>                // RGB lighting and sparse highlight data remain untouched.</code> |
| <a id="l638"></a>638 | <code>                float2 inkDx=ddx(i.uv.xy)*0.28,inkDy=ddy(i.uv.xy)*0.28;</code> |
| <a id="l639"></a>639 | <code>                float filteredInk=0.5*rawInk+0.125*(4.0-</code> |
| <a id="l640"></a>640 | <code>                    tex2D(_LightMap,i.uv.xy+inkDx+inkDy).a-</code> |
| <a id="l641"></a>641 | <code>                    tex2D(_LightMap,i.uv.xy+inkDx-inkDy).a-</code> |
| <a id="l642"></a>642 | <code>                    tex2D(_LightMap,i.uv.xy-inkDx+inkDy).a-</code> |
| <a id="l643"></a>643 | <code>                    tex2D(_LightMap,i.uv.xy-inkDx-inkDy).a);</code> |
| <a id="l644"></a>644 | <code>                // Continuous coverage preserves minified thin painted lines.</code> |
| <a id="l645"></a>645 | <code>                // Unclassified eyes, lips and detail keep the exact old blend.</code> |
| <a id="l646"></a>646 | <code>                float refinedInk=lerp(rawInk,saturate(filteredInk),saturate(_LineInnerFilter));</code> |
| <a id="l647"></a>647 | <code>                float inkStrength=dot(inkClass,_LineInnerStrengths)/max(inkClassTotal,0.0001);</code> |
| <a id="l648"></a>648 | <code>                inkStrength*=_InnerLineStrength/0.65;</code> |
| <a id="l649"></a>649 | <code>                half3 materialInk=(_LineHairInk.rgb*inkClass.r+_LineClothInk.rgb*inkClass.g+</code> |
| <a id="l650"></a>650 | <code>                    _LineSkinInk.rgb*inkClass.b+_LineMetalInk.rgb*inkClass.a)/max(inkClassTotal,0.0001);</code> |
| <a id="l651"></a>651 | <code>                half3 styledInk=lerp(_InnerLineColor.rgb,materialInk,saturate(_LineInnerTintMix));</code> |
| <a id="l652"></a>652 | <code>                color=lerp(color,lerp(lineBaseColor,styledInk,saturate(refinedInk*inkStrength)),inkCoverage);</code> |
| <a id="l653"></a>653 | <code>// END GGST LINE REFINEMENT internal line</code> |
| <a id="l654"></a>654 | <code>// BEGIN GGST EYE REFINEMENT authored catchlight clarity</code> |
| <a id="l655"></a>655 | <code>                half3 eyeBeforeCatch=color;</code> |
| <a id="l656"></a>656 | <code>                half3 eyeCatchTarget=max(color,base*_LightColor0.rgb*_LightIntensity);</code> |
| <a id="l657"></a>657 | <code>                color=lerp(color,eyeCatchTarget,saturate(_EyeCatchlightLift)*eyeCatchMask);</code> |
| <a id="l658"></a>658 | <code>// END GGST EYE REFINEMENT authored catchlight clarity</code> |
| <a id="l659"></a>659 | <code></code> |
| <a id="l660"></a>660 | <code>                int mode=(int)(_DebugMode+0.5);</code> |
| <a id="l661"></a>661 | <code>// BEGIN GGST FACE DIFFUSE diagnostics</code> |
| <a id="l662"></a>662 | <code>if(mode==35)return half4(faceRefineGate.xxx,1);</code> |
| <a id="l663"></a>663 | <code>                if(mode==36)return half4(abs(faceDiffuseDelta),1);</code> |
| <a id="l664"></a>664 | <code>// END GGST FACE DIFFUSE diagnostics</code> |
| <a id="l665"></a>665 | <code></code> |
| <a id="l666"></a>666 | <code>// BEGIN GGST EYE REFINEMENT diagnostics</code> |
| <a id="l667"></a>667 | <code>                if(mode==33)return half4(eyeIrisMask,eyeScleraMask,eyeCatchMask,1);</code> |
| <a id="l668"></a>668 | <code>                if(mode==34)return half4(abs(eyeDiffuseDelta)+abs(color-eyeBeforeCatch),1);</code> |
| <a id="l669"></a>669 | <code>// END GGST EYE REFINEMENT diagnostics</code> |
| <a id="l670"></a>670 | <code></code> |
| <a id="l671"></a>671 | <code>// BEGIN GGST LINE REFINEMENT diagnostics</code> |
| <a id="l672"></a>672 | <code>                if(mode==30)return half4((refinedInk*inkCoverage).xxx,1);</code> |
| <a id="l673"></a>673 | <code>                if(mode==31)return half4(styledInk*refinedInk*inkCoverage,1);</code> |
| <a id="l674"></a>674 | <code>// END GGST LINE REFINEMENT diagnostics</code> |
| <a id="l675"></a>675 | <code>// BEGIN GGST SHADOW REFINEMENT hair visibility diagnostic</code> |
| <a id="l676"></a>676 | <code>                if(mode==32)return half4(hairFaceOcclusion.xxx,1);</code> |
| <a id="l677"></a>677 | <code>// END GGST SHADOW REFINEMENT hair visibility diagnostic</code> |
| <a id="l678"></a>678 | <code>                if(mode==1)return half4(base,1);</code> |
| <a id="l679"></a>679 | <code>                if(mode==2)return half4(sss,1);</code> |
| <a id="l680"></a>680 | <code>                if(mode==3)return half4(detail,1);</code> |
| <a id="l681"></a>681 | <code>                if(mode==4)return half4(ilm.rrr,1);</code> |
| <a id="l682"></a>682 | <code>                if(mode==5)return half4(ilm.ggg,1);</code> |
| <a id="l683"></a>683 | <code>                if(mode==6)return half4(ilm.bbb,1);</code> |
| <a id="l684"></a>684 | <code>                if(mode==7)return half4(ilm.aaa,1);</code> |
| <a id="l685"></a>685 | <code>                if(mode==8)return half4(i.color.rrr,1);</code> |
| <a id="l686"></a>686 | <code>                if(mode==9)return half4(n*0.5+0.5,1);</code> |
| <a id="l687"></a>687 | <code>                if(mode==10)return half4(band.xxx,1);</code> |
| <a id="l688"></a>688 | <code>                if(mode==11)return half4(rawShadow.xxx,1);</code> |
| <a id="l689"></a>689 | <code>                if(mode==12)return half4(rim,1);</code> |
| <a id="l690"></a>690 | <code>                if(mode==13)return half4(spec,1);</code> |
| <a id="l691"></a>691 | <code>                if(mode==14)return half4(skin*half3(1,0.35,0.2)+hair*half3(0.2,0.4,1)+leather*half3(0.8,0.2,1)+metal*half3(0.2,1,0.8),1);</code> |
| <a id="l692"></a>692 | <code>                if(mode==15)return half4(tex2D(_OutlineMap,i.uv.xy).rgb,1);</code> |
| <a id="l693"></a>693 | <code>                if(mode==16)return half4(diffuse,1);</code> |
| <a id="l694"></a>694 | <code>                if(mode==17)return half4(step(1.0,max(color.r,max(color.g,color.b)))*half3(1,0,0),1);</code> |
| <a id="l695"></a>695 | <code>                if(mode==18)return half4(secondShade.xxx,1);</code> |
| <a id="l696"></a>696 | <code>                if(mode==19)return half4(tasteHeight,tasteHorizontalNormal,tasteGradient,1);</code> |
| <a id="l697"></a>697 | <code>                if(mode==20)return half4((faceRegion*float3(1,0.2,0.1)+legRegion*float3(0.1,1,0.2)+hair*float3(0.2,0.4,1)+coatRegion*float3(0.8,0.2,1))*regionalNl,1);</code> |
| <a id="l698"></a>698 | <code>                if(mode==21)return half4(i.color.gba,1);</code> |
| <a id="l699"></a>699 | <code>                if(mode==22)return half4(faceRegionMask,bodySkinRegion,sleeveRegion,1);</code> |
| <a id="l700"></a>700 | <code>// BEGIN GGST PALETTE diagnostic</code> |
| <a id="l701"></a>701 | <code>                if(mode==37)return half4(paletteGate,1);</code> |
| <a id="l702"></a>702 | <code>// END GGST PALETTE diagnostic</code> |
| <a id="l703"></a>703 | <code>// BEGIN GGST CLEAN SHADE diagnostic</code> |
| <a id="l704"></a>704 | <code>                if(mode==38)return half4(cleanGate,1);</code> |
| <a id="l705"></a>705 | <code>// END GGST CLEAN SHADE diagnostic</code> |
| <a id="l706"></a>706 | <code>// BEGIN GGST FOCUSED LIGHT diagnostics</code> |
| <a id="l707"></a>707 | <code>// BEGIN GGST THIGH LOBE diagnostics</code> |
| <a id="l708"></a>708 | <code>                if(mode==43)return half4((thighReplace*bodySkinRegion).xxx,1);</code> |
| <a id="l709"></a>709 | <code>                if(mode==44)return half4((thighLobe*thighFacing*thighReplace*bodySkinRegion).xxx,1);</code> |
| <a id="l710"></a>710 | <code>// END GGST THIGH LOBE diagnostics</code> |
| <a id="l711"></a>711 | <code>                if(mode==39)return half4(float3(saturate(focusedLegRegion+tunicRegion),focusedSpecCoverage,0),1);</code> |
| <a id="l712"></a>712 | <code>                if(mode==40)return half4(focusedLegRegion.xxx,1);</code> |
| <a id="l713"></a>713 | <code>                if(mode==41)return half4(lerp(cleanSkinBand,focusedSkinBand,saturate(_FocusedShadeEnabled)).xxx*focusedLegRegion,1);</code> |
| <a id="l714"></a>714 | <code>                if(mode==42)return half4(lerp(cleanTunicBand,focusedTunicBand,saturate(_FocusedShadeEnabled)).xxx*tunicRegion,1);</code> |
| <a id="l715"></a>715 | <code>// END GGST FOCUSED LIGHT diagnostics</code> |
| <a id="l716"></a>716 | <code>                if(mode==23)return half4(lerp(band,regionalSignal,regionTotal).xxx,1);</code> |
| <a id="l717"></a>717 | <code>                if(mode==24)return half4(lerp(albedo,dark,regionTotal),1);</code> |
| <a id="l718"></a>718 | <code>                // BEGIN GGST SPECULAR REFINEMENT diagnostics</code> |
| <a id="l719"></a>719 | <code>                if(mode==25)return half4(specClass.r+specClass.a,specClass.g+specClass.a,specClass.b+specClass.a,1);</code> |
| <a id="l720"></a>720 | <code>                if(mode==26)return half4(shineHair*specClass.r*_LightColor0.rgb*band,1);</code> |
| <a id="l721"></a>721 | <code>                if(mode==27)return half4(shineCloth*specClass.g*_LightColor0.rgb*band,1);</code> |
| <a id="l722"></a>722 | <code>                if(mode==28)return half4(shineSkin*specClass.b*_LightColor0.rgb*band,1);</code> |
| <a id="l723"></a>723 | <code>                if(mode==29)return half4(shineMetal*specClass.a*_LightColor0.rgb*band,1);</code> |
| <a id="l724"></a>724 | <code>                // END GGST SPECULAR REFINEMENT diagnostics</code> |
| <a id="l725"></a>725 | <code>                return half4(color,1);</code> |
| <a id="l726"></a>726 | <code>            }</code> |
| <a id="l727"></a>727 | <code>            ENDCG</code> |
| <a id="l728"></a>728 | <code>        }</code> |
| <a id="l729"></a>729 | <code>        Pass</code> |
| <a id="l730"></a>730 | <code>        {</code> |
| <a id="l731"></a>731 | <code>            Name "OUTLINE"</code> |
| <a id="l732"></a>732 | <code>            Tags {"LightMode"="Always"}</code> |
| <a id="l733"></a>733 | <code>            Cull Front ZWrite Off ZTest LEqual</code> |
| <a id="l734"></a>734 | <code>            CGPROGRAM</code> |
| <a id="l735"></a>735 | <code>            #pragma target 3.0</code> |
| <a id="l736"></a>736 | <code>            #pragma vertex vertOutline</code> |
| <a id="l737"></a>737 | <code>            #pragma fragment fragOutline</code> |
| <a id="l738"></a>738 | <code>            #include "UnityCG.cginc"</code> |
| <a id="l739"></a>739 | <code>            sampler2D _LightMap,_OutlineMap;</code> |
| <a id="l740"></a>740 | <code>// BEGIN GGST LINE REFINEMENT outline declarations</code> |
| <a id="l741"></a>741 | <code>            sampler2D _FourMaterialSpecMask;</code> |
| <a id="l742"></a>742 | <code>            float _LineRefineEnabled,_LineContourTintMix,_LineInnerFilter,_LineInnerTintMix;</code> |
| <a id="l743"></a>743 | <code>            float4 _LineContourWidths,_LineInnerStrengths;</code> |
| <a id="l744"></a>744 | <code>            half4 _LineHairInk,_LineClothInk,_LineSkinInk,_LineMetalInk;</code> |
| <a id="l745"></a>745 | <code>// END GGST LINE REFINEMENT outline declarations</code> |
| <a id="l746"></a>746 | <code>            float4 _MainTex_ST;</code> |
| <a id="l747"></a>747 | <code>            float _UseMirroredUV,_OutlineWidth,_OutlineSkinScale,_OutlineMapStrength,_LayerMaskStep,_DebugMode,_UseSmoothOutline;</code> |
| <a id="l748"></a>748 | <code>            half4 _OutlineColor;</code> |
| <a id="l749"></a>749 | <code>            struct a {float4 vertex:POSITION;float3 normal:NORMAL;float4 smoothNormal:TANGENT;float2 uv:TEXCOORD0;float2 mirror:TEXCOORD2;};</code> |
| <a id="l750"></a>750 | <code>            struct f {float4 pos:SV_POSITION;float2 uv:TEXCOORD0;};</code> |
| <a id="l751"></a>751 | <code>            f vertOutline(a v)</code> |
| <a id="l752"></a>752 | <code>            {</code> |
| <a id="l753"></a>753 | <code>                f o; o.pos=UnityObjectToClipPos(v.vertex);</code> |
| <a id="l754"></a>754 | <code>                o.uv=TRANSFORM_TEX(lerp(v.uv,v.mirror,step(0.5,_UseMirroredUV)),_MainTex);</code> |
| <a id="l755"></a>755 | <code>                float layer=tex2Dlod(_LightMap,float4(o.uv,0,0)).r*255.0;</code> |
| <a id="l756"></a>756 | <code>                float skin=step(10.0,layer)*(1.0-step(_LayerMaskStep,layer));</code> |
| <a id="l757"></a>757 | <code>                float3 outlineNormal=normalize(lerp(v.normal,v.smoothNormal.xyz,step(0.5,_UseSmoothOutline)));</code> |
| <a id="l758"></a>758 | <code>                float3 wn=UnityObjectToWorldNormal(outlineNormal);</code> |
| <a id="l759"></a>759 | <code>                float3 vn=mul((float3x3)UNITY_MATRIX_V,wn);</code> |
| <a id="l760"></a>760 | <code>                float2 direction=float2(UNITY_MATRIX_P[0][0]*vn.x,UNITY_MATRIX_P[1][1]*vn.y)*_ScreenParams.xy;</code> |
| <a id="l761"></a>761 | <code>                direction/=max(length(direction),0.0001);</code> |
| <a id="l762"></a>762 | <code>                float width=_OutlineWidth*lerp(1.0,_OutlineSkinScale,skin);</code> |
| <a id="l763"></a>763 | <code>// BEGIN GGST LINE REFINEMENT contour width</code> |
| <a id="l764"></a>764 | <code>                // Reuse the audited class atlas rather than confusing white</code> |
| <a id="l765"></a>765 | <code>                // cloth with low-ILM-R skin. Existing zero-width layers stay off.</code> |
| <a id="l766"></a>766 | <code>                float4 contourClass=saturate(tex2Dlod(_FourMaterialSpecMask,float4(o.uv,0,0)));</code> |
| <a id="l767"></a>767 | <code>                float contourTotal=dot(contourClass,float4(1,1,1,1));</code> |
| <a id="l768"></a>768 | <code>                float styledWidth=_OutlineWidth*dot(contourClass,_LineContourWidths/0.8)/max(contourTotal,0.0001);</code> |
| <a id="l769"></a>769 | <code>                width=lerp(width,styledWidth,saturate(contourTotal)*step(0.5,_LineRefineEnabled));</code> |
| <a id="l770"></a>770 | <code>// END GGST LINE REFINEMENT contour width</code> |
| <a id="l771"></a>771 | <code>                o.pos.xy+=direction*(2.0*width/_ScreenParams.xy)*o.pos.w;</code> |
| <a id="l772"></a>772 | <code>                return o;</code> |
| <a id="l773"></a>773 | <code>            }</code> |
| <a id="l774"></a>774 | <code>            half4 fragOutline(f i):SV_Target</code> |
| <a id="l775"></a>775 | <code>            {</code> |
| <a id="l776"></a>776 | <code>                clip(_OutlineWidth-0.001); clip(0.5-_DebugMode);</code> |
| <a id="l777"></a>777 | <code>                half3 map=tex2D(_OutlineMap,i.uv).rgb;</code> |
| <a id="l778"></a>778 | <code>// BEGIN GGST LINE REFINEMENT contour ink</code> |
| <a id="l779"></a>779 | <code>                if(_LineRefineEnabled&gt;0.5)</code> |
| <a id="l780"></a>780 | <code>                {</code> |
| <a id="l781"></a>781 | <code>                    float4 contourClass=saturate(tex2D(_FourMaterialSpecMask,i.uv));</code> |
| <a id="l782"></a>782 | <code>                    float contourTotal=dot(contourClass,float4(1,1,1,1));</code> |
| <a id="l783"></a>783 | <code>                    half3 materialInk=(_LineHairInk.rgb*contourClass.r+_LineClothInk.rgb*contourClass.g+</code> |
| <a id="l784"></a>784 | <code>                        _LineSkinInk.rgb*contourClass.b+_LineMetalInk.rgb*contourClass.a)/max(contourTotal,0.0001);</code> |
| <a id="l785"></a>785 | <code>                    // OLM is authored sRGB color, not an alpha width mask.</code> |
| <a id="l786"></a>786 | <code>                    // Retain its black/gray region distinction in the new tint.</code> |
| <a id="l787"></a>787 | <code>                    materialInk*=lerp(0.78,1.0,saturate(map.r/0.03310477));</code> |
| <a id="l788"></a>788 | <code>                    half3 originalInk=lerp(_OutlineColor.rgb,map,_OutlineMapStrength);</code> |
| <a id="l789"></a>789 | <code>                    return half4(lerp(originalInk,materialInk,saturate(contourTotal)*saturate(_LineContourTintMix)),1);</code> |
| <a id="l790"></a>790 | <code>                }</code> |
| <a id="l791"></a>791 | <code>// END GGST LINE REFINEMENT contour ink</code> |
| <a id="l792"></a>792 | <code>                return half4(lerp(_OutlineColor.rgb,map,_OutlineMapStrength),1);</code> |
| <a id="l793"></a>793 | <code>            }</code> |
| <a id="l794"></a>794 | <code>            ENDCG</code> |
| <a id="l795"></a>795 | <code>        }</code> |
| <a id="l796"></a>796 | <code>        Pass</code> |
| <a id="l797"></a>797 | <code>        {</code> |
| <a id="l798"></a>798 | <code>            Name "SHADOWCASTER"</code> |
| <a id="l799"></a>799 | <code>            Tags {"LightMode"="ShadowCaster"}</code> |
| <a id="l800"></a>800 | <code>            Cull [_CullMode] ZWrite On ZTest LEqual</code> |
| <a id="l801"></a>801 | <code>            CGPROGRAM</code> |
| <a id="l802"></a>802 | <code>            #pragma vertex vertShadow</code> |
| <a id="l803"></a>803 | <code>            #pragma fragment fragShadow</code> |
| <a id="l804"></a>804 | <code>            #pragma multi_compile_shadowcaster</code> |
| <a id="l805"></a>805 | <code>            #include "UnityCG.cginc"</code> |
| <a id="l806"></a>806 | <code>            struct v2f {V2F_SHADOW_CASTER;};</code> |
| <a id="l807"></a>807 | <code>            v2f vertShadow(appdata_base v){v2f o;TRANSFER_SHADOW_CASTER_NORMALOFFSET(o);return o;}</code> |
| <a id="l808"></a>808 | <code>            float4 fragShadow(v2f i):SV_Target{SHADOW_CASTER_FRAGMENT(i)}</code> |
| <a id="l809"></a>809 | <code>            ENDCG</code> |
| <a id="l810"></a>810 | <code>        }</code> |
| <a id="l811"></a>811 | <code>    }</code> |
| <a id="l812"></a>812 | <code>    Fallback Off</code> |
| <a id="l813"></a>813 | <code>}</code> |
