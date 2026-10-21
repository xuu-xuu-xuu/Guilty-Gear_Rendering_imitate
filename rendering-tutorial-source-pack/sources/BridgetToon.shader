Shader "GGST/BridgetToonStudy"
{
    Properties
    {
// BEGIN GGST THIGH LOBE properties
        _ThighLobeEnabled("大腿局部收尖高光",Range(0,1))=0
        _ThighLobeStrength("大腿独立亮块强度",Range(0,0.4))=0.16
        _ThighLobeTint("大腿浅金色高光",Color)=(0.92,1,0.45,1)
// END GGST THIGH LOBE properties

// BEGIN GGST FOCUSED LIGHT properties
        _FocusedShadeEnabled("腹部与腿部阴面收窄",Range(0,1))=0
        _FocusedSpecEnabled("整理后独立材质高光",Range(0,1))=0
        _FocusedTunicThreshold("腹部明暗阈值",Range(0.2,0.7))=0.4
        _FocusedThighThreshold("大腿明暗阈值",Range(0.3,0.8))=0.57
        _FocusedCalfThreshold("小腿明暗阈值",Range(0.3,0.8))=0.59
        _FocusedKneeThreshold("膝部明暗阈值",Range(0.3,0.8))=0.62
        _FocusedSkinStrength("皮肤浅暖亮块强度",Range(0,0.4))=0.14
        _FocusedSkinWidth("皮肤亮块宽度",Range(0.02,0.4))=0.22
        _FocusedHairGain("发丝亮带倍率",Range(0,2))=1.25
        _FocusedClothGain("布料柔光倍率",Range(0,2))=1.2
        _FocusedMetalGain("金属亮芯倍率",Range(0,2))=1.05
// END GGST FOCUSED LIGHT properties

// BEGIN GGST CLEAN SHADE properties
        _CleanShadeEnabled("角色简洁漫反射明暗",Range(0,1))=0
        _CleanClothMaskWeight("衣料明暗遮罩参与",Range(0,1))=0.4
        _CleanClothAOWeight("衣料顶点暗部参与",Range(0,1))=0.25
        _CleanClothSoftness("衣料色块边界宽度",Range(0.005,0.06))=0.018
        _CleanFaceUnderStart("下颌暗面起点",Range(-1,0))=-0.7
        _CleanFaceUnderEnd("下颌亮面起点",Range(-1,0.2))=-0.45
// END GGST CLEAN SHADE properties

// BEGIN GGST PALETTE properties
        _PaletteEnabled("皮肤与浅色衣料漫反射配色",Range(0,1))=0
        _PaletteSkinLight("皮肤亮面乘色",Vector)=(0.92,1.10,1.28,0)
        _PaletteSkinDark("皮肤暖阴面乘色",Vector)=(0.82,0.70,0.82,0)
        _PaletteSleeveLight("白袖亮面乘色",Vector)=(0.99,1,1.07,0)
        _PaletteSleeveDark("白袖冷灰阴面乘色",Vector)=(0.90,0.93,1.02,0)
        _PaletteTunicLight("胸前衣料亮面乘色",Vector)=(1,1.08,1.23,0)
        _PaletteTunicDark("胸前衣料阴面乘色",Vector)=(1.03,1.06,1.19,0)
// END GGST PALETTE properties

// BEGIN GGST RIM REFINE properties
        _ReferenceRimEnabled("参考风格边缘光启用",Range(0,1))=0
        _ReferenceRimWidth("参考边缘光宽度",Range(0.02,0.4))=0.19
        _ReferenceRimStrength("参考边缘光强度",Range(0,1))=0.38
        _ReferenceRimShadowFloor("暗面边缘光保留",Range(0,1))=0.45
        _ReferenceRimTint("参考边缘光浅色",Color)=(0.94,0.97,1,1)
        _ReferenceRimTintMix("边缘光浅色混合",Range(0,1))=0.65
        _ReferenceRimMaterial("边缘光 发/布/肤/金属",Vector)=(1,0.9,0.65,0.6)
        _ReferenceRimFaceScale("脸部边缘光比例",Range(0,1))=0.15
// END GGST RIM REFINE properties

// BEGIN GGST FACE DIFFUSE properties
_FaceDiffuseRefine("脸部漫反射造型启用",Range(0,1))=0
        _FaceDiffuseBoundary("侧脸暗面边界",Range(0.25,0.85))=0.54
        _FaceDiffuseEdge("侧脸边界过渡",Range(0.015,0.12))=0.045
        _FaceDiffuseSide("侧脸阴面覆盖",Range(0,1))=0.90
        _FaceDiffuseDepth("脸部原Sss暗色混合",Range(0,1))=0.90
        _FaceDiffuseTint("脸部漫反射暖暗乘色",Color)=(1,0.84,0.84,1)
// END GGST FACE DIFFUSE properties

// BEGIN GGST EYE REFINEMENT properties
        _EyeRefineEnabled("眼睛分区层次启用",Range(0,1))=0
        _EyeIrisUpperDepth("虹膜上层深色",Range(0,0.5))=0.18
        _EyeIrisLowerLift("虹膜下层透亮",Range(0,0.4))=0.10
        _EyeIrisEdgeDepth("虹膜外缘层次",Range(0,0.3))=0.08
        _EyeCatchlightLift("原白色高光清晰度",Range(0,0.5))=0.25
        _EyeScleraShade("眼白克制冷色",Range(0,0.2))=0.06
// END GGST EYE REFINEMENT properties

// BEGIN GGST SHADOW REFINEMENT properties
        _HairFaceShadowStrength("真实头发投脸强度",Range(0,1))=0
        _HairFaceShadowBias("头发阴影深度偏移/米",Range(0,0.01))=0.0006
        _HairFaceShadowFilter("头发阴影过滤/贴素",Range(0,3))=1.1
// END GGST SHADOW REFINEMENT properties
// BEGIN GGST LINE REFINEMENT properties
        _LineRefineEnabled("材质分区线条启用",Float)=0
        _LineContourWidths("轮廓像素宽度 发/布/肤/金属",Vector)=(0.82,0.95,0.60,0.72)
        _LineContourTintMix("轮廓材质色混合",Range(0,1))=0.55
        _LineInnerStrengths("内部线强度 发/布/肤/金属",Vector)=(0.72,0.76,0.58,0.72)
        _LineInnerFilter("内部线覆盖率过滤",Range(0,1))=0.60
        _LineInnerTintMix("内部线材质色混合",Range(0,1))=0.45
        _LineHairInk("发线暖棕",Color)=(0.06,0.032,0.015,1)
        _LineClothInk("布线蓝炭",Color)=(0.023,0.031,0.042,1)
        _LineSkinInk("肤线暖棕",Color)=(0.10,0.045,0.027,1)
        _LineMetalInk("金属线深棕",Color)=(0.04,0.032,0.022,1)
// END GGST LINE REFINEMENT properties
        // BEGIN GGST SPECULAR REFINEMENT properties
        _FourMaterialSpecMask("高光分类 RGBA发/布/肤/金属",2D)="black"{}
        _FourMaterialSpecEnabled("独立材质高光启用",Range(0,1))=0
        _HairShineStrength("头发亮带强度",Range(0,0.5))=0.12
        _HairShineWidth("头发亮带宽度",Range(0.02,0.3))=0.10
        _HairShineTint("头发亮带色",Color)=(1,0.94,0.78,1)
        _ClothShineStrength("布料柔光强度",Range(0,0.2))=0.035
        _ClothShinePower("布料柔光指数",Range(2,40))=12
        _ClothShineTint("布料柔光色",Color)=(0.90,0.95,1,1)
        _SkinShineStrength("皮肤微光强度",Range(0,0.2))=0.028
        _SkinShinePower("皮肤微光指数",Range(4,80))=28
        _SkinShineTint("皮肤微光色",Color)=(1,0.82,0.68,1)
        _MetalShineStrength("金属窄亮芯强度",Range(0,1))=0.38
        _MetalShineWidth("金属亮芯宽度",Range(0.02,0.3))=0.10
        _MetalShineTint("金属亮芯色",Color)=(1,0.97,0.90,1)
        // END GGST SPECULAR REFINEMENT properties
        _MainTex("基础色",2D)="white"{}
        _ShadowMap("原 Sss 颜色图",2D)="white"{}
        _LightMap("ilm 数据",2D)="white"{}
        _DetailMap("detail / UV1",2D)="white"{}
        _OutlineMap("olm 轮廓颜色",2D)="black"{}
        _RegionalMask("独立分区 R皮肤 G白袖",2D)="black"{}
        [HideInInspector] _RegionalEnabled("分区明暗启用",Float)=0
        [HideInInspector] _RegionalHead("头部 Renderer 分区",Float)=0
        [HideInInspector] _FaceFrameValid("只读脸部坐标有效",Float)=0
        [HideInInspector] _FaceOriginWS("只读头部原点",Vector)=(0,0,0,0)
        [HideInInspector] _FaceRightWS("只读头部横向与半宽",Vector)=(1,0,0,0.083)
        _FaceSideStrength("侧脸受控阴影",Range(0,1))=0.85
        _FaceShadeThreshold("脸部明暗阈值",Range(0,1))=0.80
        _SkinShadeThreshold("身体皮肤明暗阈值",Range(0,1))=0.69
        _SleeveShadeThreshold("白袖明暗阈值",Range(0,1))=0.68
        _RegionalSoftness("分区边界宽度",Range(0.001,0.08))=0.018
        _FaceShadeStrength("脸部暖暗色强度",Range(0,1))=0.78
        _SkinShadeStrength("皮肤暖暗色强度",Range(0,1))=0.72
        _SleeveShadeStrength("白袖冷暗色强度",Range(0,1))=0.72
        _FaceShadeTint("脸部暗面乘色",Color)=(1,0.92,0.91,1)
        _SkinShadeTint("皮肤暗面乘色",Color)=(0.78,0.49,0.47,1)
        _SleeveShadeTint("白袖暗面乘色",Color)=(0.53,0.62,0.70,1)

        [Enum(UnityEngine.Rendering.CullMode)] _CullMode("面剔除",Float)=2
        [Toggle] _UseMirroredUV("读取第三套 UV",Float)=0
        _DepthOffsetFactor("深度偏移因子",Float)=0
        _DepthOffsetUnits("深度偏移单位",Float)=0
        _LightTreshold("明暗分界",Range(0,1))=0.5
        _RampOffset("区域明暗偏移",Range(-1,1))=0
        _RampMaskCenter("ilm G 中性值（实验参数）",Range(0,1))=0.4980392
        _RampMaskStrength("ilm G 偏移强度",Range(0,2))=1
        _ShadowSoftness("明暗边界宽度",Range(0,0.1))=0.008
        _ShadowIntensity("Sss 暗部混合",Range(0,1))=0.65
        _ShadowTint("暗部色调",Color)=(1,1,1,1)
        _SkinShadowOffset("低 R 分区明暗偏移",Range(-0.5,0.5))=0.06
        _SecondShadowThreshold("第二暗部阈值 / NdotL",Range(-1,1))=0.1
        _SecondShadowStrength("下半身第二暗部强度",Range(0,1))=0
        _SecondShadowTint("第二暗部乘色",Color)=(1,1,1,1)
        _LowerRegionUpper("下半身区域上界 / 相对身高",Range(0,1))=0.52
        _LowerRegionFeather("区域过渡宽度",Range(0.01,0.3))=0.08
        _LowerLightBlend("下半身独立光向混合",Range(0,1))=0
        _LowerLightDirection("下半身独立光向 / 世界空间",Vector)=(0.8,0.5,0.2,0)
        _LowerLightDynamic("下半身跟随主光（移动光源 A/B）",Range(0,1))=0
        _LowerSkinColorGate("用基础色排除低R白色材质（当前配色实验）",Range(0,1))=1
        _TasteRatePow("下半身渐变指数（实验）",Range(0.1,4))=1
        _TasteHeightStart("渐变高度下界（诊断）",Range(-1,2))=0
        _TasteHeightEnd("渐变高度上界（诊断）",Range(-1,2))=0.65
        _TasteNormalWeight("水平法线参与度（诊断）",Range(0,1))=0.5
        _RegionLightBlend("部位光向混合（诊断）",Range(0,1))=0
        _RegionLightDirection("部位候选光向（诊断）",Vector)=(0.8,0.5,0.2,0)
        [HideInInspector] _CharacterOriginWS("角色脚下参考原点",Vector)=(0,0,0,0)
        [HideInInspector] _CharacterHeight("角色参考身高",Float)=1.65
        _LightIntensity("主光贡献",Range(0,2))=0.9
        _AmbientStrength("环境光贡献",Range(0,1))=0.2
        _AOStrength("顶点 R 明暗控制",Range(0,1))=1
        _DetailIntensity("Detail 强度",Range(0,1))=0.278
        _InnerLineStrength("ilm Alpha 内部线条",Range(0,1))=0.65
        _InnerLineColor("内部线条颜色",Color)=(0.035,0.028,0.025,1)
        _RimWidth("边缘光宽度",Range(0,1))=0.16
        _RimIntensity("边缘光强度",Range(0,1))=0.16
        _SpecularPower("通用高光指数",Range(1,100))=24
        _SpecularIntensity("通用高光强度",Range(0,2))=0.12
        _LayerMaskStep("皮肤分区上界（实验分类）",Range(0,255))=60
        _BodySpecularWidth("皮肤高光宽度",Range(0,1))=0.18
        _BodySpecularIntensity("皮肤高光强度",Range(0,1))=0.15
        _HeadSpecularWidth("头发高光宽度",Range(0,1))=0.14
        _HeadSpecularIntensity("头发高光强度",Range(0,1))=0.22
        _HairLayerMin("头发/布料共享分区下界",Range(0,255))=65
        _HairLayerMax("头发/布料共享分区上界",Range(0,255))=90
        _LeatherLayerMin("手套/裙子分区下界",Range(0,255))=90
        _LeatherLayerMax("手套/裙子分区上界",Range(0,255))=125
        _MetalLayerMin("金属分区下界",Range(0,255))=145
        _MetalLayerMax("金属分区上界",Range(0,255))=200
        _MetallicStepSpecularWidth("金属高光宽度",Range(0,1))=0.2
        _MetallicStepSpecularIntensity("金属高光强度",Range(0,1))=0.25
        _ReceiveShadowStrength("接收投影强度",Range(0,1))=0.7
        _OutlineWidth("轮廓宽度 / 输出像素",Range(0,4))=0.8
        [Toggle] _UseSmoothOutline("使用蒙皮平滑描边法线（需专用网格）",Float)=0
        _OutlineSkinScale("皮肤轮廓宽度比例",Range(0,1))=0.35
        _OutlineColor("轮廓颜色",Color)=(0.04,0.03,0.025,1)
        _OutlineMapStrength("olm 颜色参与",Range(0,1))=0.6
        [IntRange] _DebugMode("调试输出 0～24（编号见修改文档）",Range(0,24))=0
    }
    SubShader
    {
        Tags {"RenderType"="Opaque" "Queue"="Geometry"}
        LOD 200
        Pass
        {
            Name "FORWARD"
            Tags {"LightMode"="ForwardBase"}
            Cull [_CullMode] ZWrite On
            Offset [_DepthOffsetFactor], [_DepthOffsetUnits]
            CGPROGRAM
            #pragma target 3.0
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_fwdbase nolightmap nodirlightmap nodynlightmap novertexlight
            #include "UnityCG.cginc"
            #include "Lighting.cginc"
            #include "AutoLight.cginc"
            // BEGIN GGST SPECULAR REFINEMENT declarations
// BEGIN GGST RIM REFINE declarations
            float _ReferenceRimEnabled,_ReferenceRimWidth,_ReferenceRimStrength;
            float _ReferenceRimShadowFloor,_ReferenceRimTintMix,_ReferenceRimFaceScale;
            half4 _ReferenceRimTint;
            float4 _ReferenceRimMaterial;
// END GGST RIM REFINE declarations
// BEGIN GGST PALETTE declarations
            float _PaletteEnabled;
            float4 _PaletteSkinLight,_PaletteSkinDark,_PaletteSleeveLight,_PaletteSleeveDark,_PaletteTunicLight,_PaletteTunicDark;
// END GGST PALETTE declarations
// BEGIN GGST CLEAN SHADE declarations
            float _CleanShadeEnabled,_CleanClothMaskWeight,_CleanClothAOWeight,_CleanClothSoftness;
            float _CleanFaceUnderStart,_CleanFaceUnderEnd;
// END GGST CLEAN SHADE declarations
// BEGIN GGST FOCUSED LIGHT declarations
// BEGIN GGST THIGH LOBE declarations
            float _ThighLobeEnabled,_ThighLobeStrength;
            half4 _ThighLobeTint;
// END GGST THIGH LOBE declarations
            float _FocusedShadeEnabled,_FocusedSpecEnabled,_FocusedTunicThreshold;
            float _FocusedThighThreshold,_FocusedCalfThreshold,_FocusedKneeThreshold;
            float _FocusedSkinStrength,_FocusedSkinWidth,_FocusedHairGain,_FocusedClothGain,_FocusedMetalGain;
// END GGST FOCUSED LIGHT declarations
            sampler2D _FourMaterialSpecMask;
            float _FourMaterialSpecEnabled,_HairShineStrength,_HairShineWidth;
            float _ClothShineStrength,_ClothShinePower,_SkinShineStrength,_SkinShinePower;
            float _MetalShineStrength,_MetalShineWidth;
            half4 _HairShineTint,_ClothShineTint,_SkinShineTint,_MetalShineTint;
            // END GGST SPECULAR REFINEMENT declarations
// BEGIN GGST LINE REFINEMENT forward declarations
            float _LineRefineEnabled,_LineContourTintMix,_LineInnerFilter,_LineInnerTintMix;
            float4 _LineContourWidths,_LineInnerStrengths;
            half4 _LineHairInk,_LineClothInk,_LineSkinInk,_LineMetalInk;
// END GGST LINE REFINEMENT forward declarations
// BEGIN GGST SHADOW REFINEMENT face receiver declarations
            sampler2D _HairShadowDepth;
            float4x4 _HairShadowVP;
            float4 _HairShadowOriginRange,_HairShadowForward,_HairShadowTexel;
            float _HairShadowEnabled,_HairFaceShadowStrength,_HairFaceShadowBias,_HairFaceShadowFilter;
            float ReadHairVisibility(float3 world)
            {
                float4 clipSpace=mul(_HairShadowVP,float4(world,1));
                float2 uv=clipSpace.xy/max(clipSpace.w,0.00001)*0.5+0.5;
                float depth=dot(world-_HairShadowOriginRange.xyz,_HairShadowForward.xyz)/max(_HairShadowOriginRange.w,0.00001);
                float inside=step(0,uv.x)*step(uv.x,1)*step(0,uv.y)*step(uv.y,1)*step(0,depth)*step(depth,1);
                float bias=_HairFaceShadowBias/max(_HairShadowOriginRange.w,0.00001);
                float visibility=0;
                [unroll] for(int x=-1;x<=1;x++)
                [unroll] for(int y=-1;y<=1;y++)
                {
                    float stored=tex2D(_HairShadowDepth,uv+float2(x,y)*_HairShadowTexel.xy*_HairFaceShadowFilter).r;
                    visibility+=step(depth-bias,stored);
                }
                return lerp(1.0,visibility/9.0,inside*saturate(_HairShadowEnabled));
            }
// END GGST SHADOW REFINEMENT face receiver declarations
            sampler2D _MainTex,_ShadowMap,_LightMap,_DetailMap,_OutlineMap,_RegionalMask;
// BEGIN GGST EYE REFINEMENT declarations
            float _EyeRefineEnabled,_EyeIrisUpperDepth,_EyeIrisLowerLift;
            float _EyeIrisEdgeDepth,_EyeCatchlightLift,_EyeScleraShade;
            float EyeDisk(float2 q)
            {
                float radius=length(q);
                float aa=clamp(fwidth(radius)*0.55,0.01,0.08);
                return 1.0-smoothstep(1.0-aa,1.0+aa,radius);
            }
// END GGST EYE REFINEMENT declarations

            float _RegionalEnabled,_RegionalHead,_FaceShadeThreshold,_SkinShadeThreshold,_SleeveShadeThreshold,_RegionalSoftness;
            float _FaceShadeStrength,_SkinShadeStrength,_SleeveShadeStrength,_FaceSideStrength,_FaceFrameValid;
            float4 _FaceOriginWS,_FaceRightWS;
            half4 _FaceShadeTint,_SkinShadeTint,_SleeveShadeTint;
// BEGIN GGST FACE DIFFUSE declarations
float _FaceDiffuseRefine,_FaceDiffuseBoundary,_FaceDiffuseEdge,_FaceDiffuseSide,_FaceDiffuseDepth;
            half4 _FaceDiffuseTint;
// END GGST FACE DIFFUSE declarations

            float4 _MainTex_ST;
            float _UseMirroredUV,_LightTreshold,_RampOffset,_RampMaskCenter,_RampMaskStrength,_ShadowSoftness;
            float _ShadowIntensity,_SkinShadowOffset,_LightIntensity,_AmbientStrength,_AOStrength,_DetailIntensity;
            float _InnerLineStrength,_RimWidth,_RimIntensity,_SpecularPower,_SpecularIntensity,_LayerMaskStep;
            float _BodySpecularWidth,_BodySpecularIntensity,_HeadSpecularWidth,_HeadSpecularIntensity;
            float _HairLayerMin,_HairLayerMax,_LeatherLayerMin,_LeatherLayerMax;
            float _MetalLayerMin,_MetalLayerMax,_MetallicStepSpecularWidth,_MetallicStepSpecularIntensity;
            float _ReceiveShadowStrength,_DebugMode;
            float _SecondShadowThreshold,_SecondShadowStrength,_LowerRegionUpper,_LowerRegionFeather,_LowerLightBlend,_LowerLightDynamic,_CharacterHeight;
            float _LowerSkinColorGate,_TasteRatePow,_TasteHeightStart,_TasteHeightEnd,_TasteNormalWeight,_RegionLightBlend;
            float4 _CharacterOriginWS,_LowerLightDirection,_RegionLightDirection;
            half4 _SecondShadowTint;
            half4 _ShadowTint,_InnerLineColor;
            struct appdata
            {
                float4 vertex:POSITION; float3 normal:NORMAL;
                float2 uv:TEXCOORD0; float2 uv1:TEXCOORD1; float2 uvMirror:TEXCOORD2;
                float4 color:COLOR;
            };
            struct v2f
            {
                float4 pos:SV_POSITION; float4 uv:TEXCOORD0;
                float3 worldPos:TEXCOORD1; float3 normal:TEXCOORD2;
                float4 color:COLOR; SHADOW_COORDS(3)
            };
            v2f vert(appdata v)
            {
                v2f o;
                o.pos=UnityObjectToClipPos(v.vertex);
                o.worldPos=mul(unity_ObjectToWorld,v.vertex).xyz;
                o.normal=UnityObjectToWorldNormal(v.normal);
                o.uv.xy=TRANSFORM_TEX(lerp(v.uv,v.uvMirror,step(0.5,_UseMirroredUV)),_MainTex);
                o.uv.zw=v.uv1; o.color=v.color;
                TRANSFER_SHADOW(o);
                return o;
            }
            half4 frag(v2f i, float facing:VFACE):SV_Target
            {
                float3 n=normalize(i.normal)*(facing>=0?1:-1);
                float3 l=normalize(UnityWorldSpaceLightDir(i.worldPos));
                float3 v=normalize(UnityWorldSpaceViewDir(i.worldPos));
                float nl=dot(n,l)*0.5+0.5, nv=saturate(dot(n,v));
                half3 base=tex2D(_MainTex,i.uv.xy).rgb;
                half3 sss=tex2D(_ShadowMap,i.uv.xy).rgb;
                float4 ilm=tex2D(_LightMap,i.uv.xy);
                half3 detail=tex2D(_DetailMap,i.uv.zw).rgb;
                half3 albedo=base*lerp(half3(1,1,1),detail,_DetailIntensity);
// BEGIN GGST EYE REFINEMENT audited atlas gates
                // Pixel-space values are measured in the immutable 2048 atlas.
                // The original small eye and high-detail eye use different UV
                // islands. Current head MPBs cover lowHead and cinematicHair;
                // body material/hood UVs cannot enter this branch.
                float2 eyePixel=float2(i.uv.x*2048.0,(1.0-i.uv.y)*2048.0);
                float eyeHead=saturate(_EyeRefineEnabled)*saturate(_RegionalHead);
                float2 eyeSmallQ=(eyePixel-float2(960.0,64.0))/float2(34.0,34.0);
                float2 eyeLargeQ=(eyePixel-float2(1152.0,130.0))/float2(104.0,100.0);
                float eyeSmallDisk=EyeDisk(eyeSmallQ);
                float eyeLargeDisk=EyeDisk(eyeLargeQ);
                float eyeSmallPupil=smoothstep(1.10,1.24,length((eyePixel-float2(960.0,64.0))/float2(13.0,13.0)));
                float eyeLargePupil=smoothstep(1.10,1.24,length((eyePixel-float2(1152.0,129.0))/float2(29.0,35.0)));
                // Bounded original teal chroma protects black pupils/ink and
                // authored white glints, including compressed texture edges.
                float eyeChroma=smoothstep(0.015,0.055,min(base.g,base.b)-base.r);
                float eyeIrisMask=saturate(eyeSmallDisk+eyeLargeDisk)*eyeSmallPupil*eyeLargePupil*eyeChroma*eyeHead;
                float2 eyeQ=lerp(eyeSmallQ,eyeLargeQ,step(1020.0,eyePixel.x));
                float eyeUp=-eyeQ.y; // PNG y increases downwards.
                float eyeUpper=smoothstep(-0.20,0.55,eyeUp);
                float eyeLower=(1.0-smoothstep(-0.35,0.40,eyeUp))*(1.0-smoothstep(0.75,1.0,length(eyeQ)));
                float eyeEdge=smoothstep(0.56,0.94,length(eyeQ));
                float eyeDomain=step(896.0,eyePixel.x)*step(eyePixel.x,1280.0)*step(0.0,eyePixel.y)*step(eyePixel.y,256.0);
                float3 eyeWhiteDistance=abs(base-half3(0.8388,0.8308,0.9301));
                float eyeNeutral=1.0-smoothstep(0.025,0.065,max(eyeWhiteDistance.r,max(eyeWhiteDistance.g,eyeWhiteDistance.b)));
                float eyeScleraMask=eyeDomain*eyeNeutral*(1.0-saturate(eyeSmallDisk+eyeLargeDisk))*eyeHead;
                // The two small-eye glints already exist in the original base.
                // Do not generate a new moving point. The high-detail eye's
                // separate original HeadGlow/HeadDecal passes stay untouched.
                float eyeAuthoredGlint=saturate(EyeDisk((eyePixel-float2(938.7075,48.0896))/float2(12.0,12.0))+EyeDisk((eyePixel-float2(983.5789,85.5))/float2(8.5,8.5)));
                float eyeCatchMask=eyeAuthoredGlint*smoothstep(0.85,0.97,min(base.r,min(base.g,base.b)))*eyeHead;
// END GGST EYE REFINEMENT audited atlas gates

                float layer=ilm.r*255.0;
                float skin=step(10.0,layer)*(1.0-step(_LayerMaskStep,layer));
                float hair=step(_HairLayerMin,layer)*(1.0-step(_HairLayerMax,layer));
                float leather=step(_LeatherLayerMin,layer)*(1.0-step(_LeatherLayerMax,layer));
                float metal=step(_MetalLayerMin,layer)*(1.0-step(_MetalLayerMax,layer));
                float relativeHeight=(i.worldPos.y-_CharacterOriginWS.y)/max(_CharacterHeight,0.01);
                float lowerHeight=pow(saturate(1.0-smoothstep(_LowerRegionUpper-_LowerRegionFeather,_LowerRegionUpper+_LowerRegionFeather,relativeHeight)),max(_TasteRatePow,0.01));
                float lowerRegion=skin*lowerHeight;
                // Diagnostic-only independent height / horizontal-normal gradient. It is not wired into final color.
                float tasteHeight=saturate(1.0-smoothstep(_TasteHeightStart,_TasteHeightEnd,relativeHeight));
                float tasteHorizontalNormal=saturate(length(n.xz));
                float tasteGradient=pow(saturate(tasteHeight*lerp(1.0,tasteHorizontalNormal,saturate(_TasteNormalWeight))),max(_TasteRatePow,0.01));
                // Diagnostic-only regional light response; it is not wired into final color.
                float3 regionalLight=normalize(_RegionLightDirection.xyz+float3(0,0.00001,0));
                float regionalNl=dot(n,lerp(l,regionalLight,saturate(_RegionLightBlend)))*0.5+0.5;
                float faceRegion=skin*smoothstep(0.58,0.80,relativeHeight);
                float legRegion=skin*(1.0-smoothstep(0.35,0.55,relativeHeight));
                float coatRegion=leather*(1.0-faceRegion);
                // Low-R also contains white material. This color gate is a default-palette hypothesis.
                float warmSkin=smoothstep(0.06,0.10,base.r-base.b)*smoothstep(0.02,0.04,base.r-base.g);
                lowerRegion*=lerp(1.0,warmSkin,saturate(_LowerSkinColorGate));
                float3 lowerLight=normalize(_LowerLightDirection.xyz+float3(0,0.00001,0));
                lowerLight=normalize(lerp(lowerLight,l,saturate(_LowerLightDynamic)));
                l=normalize(lerp(l,lowerLight,saturate(_LowerLightBlend*lowerRegion)));
                nl=dot(n,l)*0.5+0.5;
                // These are configurable reconstruction hypotheses, not the original GPU equations.
                float ao=lerp(1.0,saturate(i.color.r),_AOStrength);
                float signal=(nl+_RampOffset+(ilm.g-_RampMaskCenter)*_RampMaskStrength+skin*_SkinShadowOffset)*ao;
                float soft=max(_ShadowSoftness,0.00001);
                float band=smoothstep(_LightTreshold-soft,_LightTreshold+soft,signal);
                float rawShadow=SHADOW_ATTENUATION(i);
                float projected=lerp(1.0,rawShadow,_ReceiveShadowStrength);
                band*=projected;
                half3 dark=lerp(albedo,sss*_ShadowTint.rgb,_ShadowIntensity);
                // Reconstructed regional second shade; not the stripped native shader expression.
                float secondShade=lowerRegion*(1.0-band)*(1.0-smoothstep(_SecondShadowThreshold-0.06,_SecondShadowThreshold+0.06,dot(n,l)));
                dark*=lerp(half3(1,1,1),_SecondShadowTint.rgb,secondShade*_SecondShadowStrength);
                // Independent atlas masks keep face/skin/sleeve changes out of hair,
                // eye whites, the hood band, socks, blue coat and metal. No mesh data
                // or skinning equations are changed by this rendering-only branch.
                float2 region=saturate(tex2D(_RegionalMask,i.uv.xy).rg)*saturate(_RegionalEnabled);
                float head=saturate(_RegionalHead);
                float faceRegionMask=region.r*head;
                float bodySkinRegion=region.r*(1.0-head);
                float sleeveRegion=region.g*(1.0-head);
                float regionTotal=saturate(faceRegionMask+bodySkinRegion+sleeveRegion);
                float regionalSignal=(nl+_RampOffset+(ilm.g-_RampMaskCenter)*_RampMaskStrength)*ao;
                float regionSoft=max(_RegionalSoftness,0.001);
                float faceBand=smoothstep(_FaceShadeThreshold-regionSoft,_FaceShadeThreshold+regionSoft,regionalSignal);
                // Artist-controlled lateral face shading in a read-only head frame.
                // Main light selects the far cheek. It follows the existing Step
                // pose directly; no temporal interpolation or bone writes.
                float3 faceRight=normalize(_FaceRightWS.xyz+float3(0.000001,0,0));
                float faceX=dot(i.worldPos-_FaceOriginWS.xyz,faceRight)/max(_FaceRightWS.w,0.001);
                float lightSide=dot(l,faceRight);
                float lateral=smoothstep(0.12,0.48,abs(lightSide));
                float sideBoundary=lerp(0.92,0.30,lateral);
                float farCheek=-faceX*(lightSide>=0?1.0:-1.0);
                float cheekShade=smoothstep(sideBoundary-0.07,sideBoundary+0.07,farCheek)*smoothstep(0.04,0.18,abs(lightSide));
                faceBand=min(faceBand,1.0-cheekShade*_FaceSideStrength*saturate(_FaceFrameValid));
                float skinBand=smoothstep(_SkinShadeThreshold-regionSoft,_SkinShadeThreshold+regionSoft,regionalSignal);
                float sleeveBand=smoothstep(_SleeveShadeThreshold-regionSoft,_SleeveShadeThreshold+regionSoft,regionalSignal);
                float regionalBand=faceBand*faceRegionMask+skinBand*bodySkinRegion+sleeveBand*sleeveRegion;
                half3 faceDark=lerp(albedo,sss*_FaceShadeTint.rgb,saturate(_FaceShadeStrength));
                half3 skinDark=lerp(albedo,albedo*_SkinShadeTint.rgb,saturate(_SkinShadeStrength));
                half3 sleeveDark=lerp(albedo,albedo*_SleeveShadeTint.rgb,saturate(_SleeveShadeStrength));
                half3 regionalDark=faceDark*faceRegionMask+skinDark*bodySkinRegion+sleeveDark*sleeveRegion;
                // Weighted replacement, not a second layer of the old empirical red
                // height tint. Preserve unmasked material lighting exactly.
                float safeRegion=max(regionTotal,0.0001);
                band=lerp(band,(regionalBand/safeRegion)*projected,regionTotal);
                dark=lerp(dark,regionalDark/safeRegion,regionTotal);
                half3 diffuse=lerp(dark,albedo,band)*_LightColor0.rgb*_LightIntensity;
// BEGIN GGST SHADOW REFINEMENT true hair occlusion only in face diffuse
                float hairVisibility=ReadHairVisibility(i.worldPos);
                float hairFaceOcclusion=(1.0-hairVisibility)*faceRegionMask*saturate(_FaceFrameValid)*saturate(_HairFaceShadowStrength);
                // Reuse the approved face dark tone. Its union with an existing
                // dark face region does not multiply the same shade twice.
                diffuse=lerp(diffuse,faceDark*_LightColor0.rgb*_LightIntensity,hairFaceOcclusion);
// END GGST SHADOW REFINEMENT true hair occlusion only in face diffuse
// BEGIN GGST FACE DIFFUSE replacement
// Refine diffuse only. Keep the established band intact for
                // highlights/rim/eyes, and retain the original hair visibility.
                // The existing atlas gate excludes hair, clothing and eye UVs.
                float faceRefineGate=faceRegionMask*saturate(_FaceFrameValid)*saturate(_FaceDiffuseRefine);
                float faceBoundary=lerp(0.92,_FaceDiffuseBoundary,lateral);
                float faceEdge=max(_FaceDiffuseEdge,fwidth(farCheek)*0.55);
                float faceSideShade=smoothstep(faceBoundary-faceEdge,faceBoundary+faceEdge,farCheek)*smoothstep(0.04,0.18,abs(lightSide));
                float faceDiffuseBand=min(smoothstep(_FaceShadeThreshold-regionSoft,_FaceShadeThreshold+regionSoft,regionalSignal),1.0-faceSideShade*_FaceDiffuseSide);
                half3 faceDiffuseDark=lerp(albedo,sss*_FaceDiffuseTint.rgb,saturate(_FaceDiffuseDepth));
                half3 faceDiffuseOld=lerp(faceDark,albedo,faceBand*projected)*_LightColor0.rgb*_LightIntensity;
                half3 faceDiffuseNew=lerp(faceDiffuseDark,albedo,faceDiffuseBand*projected)*_LightColor0.rgb*_LightIntensity;
                half3 faceDiffuseDelta=(faceDiffuseNew-faceDiffuseOld)*faceRefineGate*(1.0-hairFaceOcclusion);
                diffuse+=faceDiffuseDelta;
// END GGST FACE DIFFUSE replacement

// BEGIN GGST PALETTE diffuse only
                // Immutable atlas cream swatch, verified against original body
                // UVs. Exclude hood, socks, hair and other head renderers.
                float2 palettePixel=float2(i.uv.x*2048.0,(1.0-i.uv.y)*2048.0);
                float tunicUpper=step(768.5,palettePixel.x)*step(palettePixel.x,895.5)*step(640.5,palettePixel.y)*step(palettePixel.y,895.5);
                float tunicLower=step(512.5,palettePixel.x)*step(palettePixel.x,895.5)*step(895.5,palettePixel.y)*step(palettePixel.y,1343.5);
                float tunicRegion=saturate(tunicUpper+tunicLower)*(1.0-head)*saturate(_RegionalEnabled);
                float paletteSkin=faceRegionMask+bodySkinRegion;
                float paletteSkinBand=lerp(saturate(skinBand*projected),saturate(lerp(faceBand,faceDiffuseBand,saturate(_FaceDiffuseRefine))*projected),head);
                float3 paletteSkinMultiplier=lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,paletteSkinBand);
                float3 paletteSleeveMultiplier=lerp(_PaletteSleeveDark.rgb,_PaletteSleeveLight.rgb,saturate(sleeveBand*projected));
                float3 paletteTunicMultiplier=lerp(_PaletteTunicDark.rgb,_PaletteTunicLight.rgb,saturate(band));
                float3 paletteMultiplier=1.0+(paletteSkinMultiplier-1.0)*paletteSkin+(paletteSleeveMultiplier-1.0)*sleeveRegion+(paletteTunicMultiplier-1.0)*tunicRegion;
                float3 paletteGate=float3(paletteSkin,sleeveRegion,tunicRegion);
                // Do not recolor albedo, band, ambient, specular, rim or ink.
                diffuse*=lerp(float3(1,1,1),paletteMultiplier,saturate(_PaletteEnabled));
// END GGST PALETTE diffuse only

// BEGIN GGST CLEAN SHADE diffuse replacement
                // Only the character's diffuse lobe is reconstructed here.
                // Leave band/albedo/normal and every existing rim/spec/ink
                // equation untouched. Scene shadow casters/receivers also stay.
                float cleanFaceBand=smoothstep(_CleanFaceUnderStart,_CleanFaceUnderEnd,n.y);
                float cleanSkinBand=skinBand;
                float cleanClothSignal=(nl+_RampOffset+(ilm.g-_RampMaskCenter)*_RampMaskStrength*_CleanClothMaskWeight)*lerp(1.0,ao,_CleanClothAOWeight);
                float cleanClothBand=smoothstep(_LightTreshold-_CleanClothSoftness,_LightTreshold+_CleanClothSoftness,cleanClothSignal);
                float cleanSleeveBand=smoothstep(_SleeveShadeThreshold-_CleanClothSoftness,_SleeveShadeThreshold+_CleanClothSoftness,cleanClothSignal);
                float cleanTunicBand=cleanClothBand;
                float cleanClothClass=saturate(tex2D(_FourMaterialSpecMask,i.uv.xy).g)*saturate(_FourMaterialSpecEnabled)*(1.0-head);
                float cleanOtherCloth=cleanClothClass*(1.0-saturate(paletteSkin+sleeveRegion+tunicRegion));
                float cleanTotal=paletteSkin+sleeveRegion+tunicRegion+cleanOtherCloth;
                float cleanCoverage=saturate(cleanTotal);
                float3 cleanGate=float3(faceRegionMask,bodySkinRegion,saturate(sleeveRegion+tunicRegion+cleanOtherCloth));
                half3 cleanClothDark=lerp(albedo,sss*_ShadowTint.rgb,_ShadowIntensity);
                half3 cleanFace=lerp(faceDiffuseDark,albedo,cleanFaceBand)*lerp(float3(1,1,1),lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,cleanFaceBand),saturate(_PaletteEnabled));
                half3 cleanSkin=lerp(skinDark,albedo,cleanSkinBand)*lerp(float3(1,1,1),lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,cleanSkinBand),saturate(_PaletteEnabled));
                half3 cleanSleeve=lerp(sleeveDark,albedo,cleanSleeveBand)*lerp(float3(1,1,1),lerp(_PaletteSleeveDark.rgb,_PaletteSleeveLight.rgb,cleanSleeveBand),saturate(_PaletteEnabled));
                half3 cleanTunic=lerp(cleanClothDark,albedo,cleanTunicBand)*lerp(float3(1,1,1),lerp(_PaletteTunicDark.rgb,_PaletteTunicLight.rgb,cleanTunicBand),saturate(_PaletteEnabled));
                half3 cleanCloth=lerp(cleanClothDark,albedo,cleanClothBand);
                half3 cleanDiffuse=(cleanFace*faceRegionMask+cleanSkin*bodySkinRegion+cleanSleeve*sleeveRegion+cleanTunic*tunicRegion+cleanCloth*cleanOtherCloth)/max(cleanTotal,0.0001)*_LightColor0.rgb*_LightIntensity;
                diffuse=lerp(diffuse,cleanDiffuse,saturate(_CleanShadeEnabled)*cleanCoverage);
// END GGST CLEAN SHADE diffuse replacement

// BEGIN GGST FOCUSED LIGHT diffuse bands
                // UV region verified against the immutable original leg skin
                // weights. Atlas-based boundaries follow every existing pose.
                float focusedLegDomain=step(200.0,palettePixel.x)*step(palettePixel.x,510.0)*step(880.0,palettePixel.y)*step(palettePixel.y,1195.0);
                float focusedLegRegion=bodySkinRegion*focusedLegDomain;
                float focusedCalf=smoothstep(1035.0,1070.0,palettePixel.y);
                float focusedKnee=smoothstep(1015.0,1035.0,palettePixel.y)*(1.0-smoothstep(1055.0,1075.0,palettePixel.y));
                float focusedLegThreshold=lerp(_FocusedThighThreshold,_FocusedCalfThreshold,focusedCalf);
                focusedLegThreshold=lerp(focusedLegThreshold,_FocusedKneeThreshold,focusedKnee);
                float focusedLegBand=smoothstep(focusedLegThreshold-regionSoft,focusedLegThreshold+regionSoft,regionalSignal);
                float focusedSkinBand=lerp(cleanSkinBand,focusedLegBand,focusedLegDomain*saturate(_FocusedShadeEnabled));
                float focusedTunicBand=lerp(cleanTunicBand,smoothstep(_FocusedTunicThreshold-_CleanClothSoftness,_FocusedTunicThreshold+_CleanClothSoftness,cleanClothSignal),saturate(_FocusedShadeEnabled));
                half3 focusedSkin=lerp(skinDark,albedo,focusedSkinBand)*lerp(float3(1,1,1),lerp(_PaletteSkinDark.rgb,_PaletteSkinLight.rgb,focusedSkinBand),saturate(_PaletteEnabled));
                half3 focusedTunic=lerp(cleanClothDark,albedo,focusedTunicBand)*lerp(float3(1,1,1),lerp(_PaletteTunicDark.rgb,_PaletteTunicLight.rgb,focusedTunicBand),saturate(_PaletteEnabled));
                diffuse+=((focusedSkin-cleanSkin)*focusedLegRegion+(focusedTunic-cleanTunic)*tunicRegion)/max(cleanTotal,0.0001)*_LightColor0.rgb*_LightIntensity*saturate(_CleanShadeEnabled)*cleanCoverage;
// END GGST FOCUSED LIGHT diffuse bands

// BEGIN GGST EYE REFINEMENT diffuse layers
                half3 eyeBeforeDiffuse=diffuse;
                float eyeDepth=saturate(_EyeIrisUpperDepth*eyeUpper+_EyeIrisEdgeDepth*eyeEdge);
                diffuse*=1.0-eyeIrisMask*eyeDepth;
                // Reuse the original iris hue and the same lit/shadow band.
                // No emission or time-driven sparkle is introduced.
                diffuse+=albedo*half3(0.70,1.0,0.92)*_LightColor0.rgb*_LightIntensity*band*eyeIrisMask*eyeLower*_EyeIrisLowerLift;
                diffuse*=lerp(half3(1,1,1),half3(0.70,0.85,1.0),eyeScleraMask*_EyeScleraShade);
                half3 eyeDiffuseDelta=diffuse-eyeBeforeDiffuse;
// END GGST EYE REFINEMENT diffuse layers

                // Give ambient its own small, explicit contribution instead of washing out every lit region.
                half3 ambient=UNITY_LIGHTMODEL_AMBIENT.rgb*albedo*_AmbientStrength;
                float rimEdge=smoothstep(1.0-_RimWidth,1.0-_RimWidth+0.035,1.0-nv);
                half3 rim=rimEdge*_RimIntensity*albedo*band*_LightColor0.rgb;
                // BEGIN GGST SPECULAR REFINEMENT calculations
                float nh=saturate(dot(n,normalize(l+v)));
                half3 spec=pow(nh,_SpecularPower)*_SpecularIntensity*ilm.b*albedo;
                float maskByte=ilm.b*255.0;
                float bodyMask=saturate(skin+leather)*step(0.5,maskByte)*(1.0-step(140.5,maskByte));
                float hairMask=hair*step(140.5,maskByte);
                spec=lerp(spec,step(1.0-_BodySpecularWidth,1.0-nv)*_BodySpecularIntensity*albedo,bodyMask);
                spec=lerp(spec,step(1.0-_HeadSpecularWidth,nv)*_HeadSpecularIntensity*albedo,hairMask);
                spec+=metal*step(1.0-_MetallicStepSpecularWidth,nl)*_MetallicStepSpecularIntensity*ilm.b*albedo;
                spec*=_LightColor0.rgb*band;
                // Keep the exact original specular expression above as the
                // fallback for eyes, lips and other intentionally unclassified UVs.
                float4 specClass=saturate(tex2D(_FourMaterialSpecMask,i.uv.xy))*saturate(_FourMaterialSpecEnabled);
                float specCoverage=saturate(specClass.r+specClass.g+specClass.b+specClass.a);
                float shineAA=max(fwidth(nh)*0.65,0.006);
                float paintedShine=saturate(ilm.b);
                float hairShoulder=smoothstep(1.0-_HairShineWidth-shineAA,1.0-_HairShineWidth+shineAA,nh);
                float hairCore=smoothstep(1.0-_HairShineWidth*0.28-shineAA,1.0-_HairShineWidth*0.28+shineAA,nh);
                // ILM.B is sparse authored highlight detail, not whole-surface
                // reflectance. A weak base and localized painted core stay separate.
                float hairShape=0.22*hairShoulder+0.78*paintedShine*(0.4*hairShoulder+0.6*hairCore);
                half3 shineHair=lerp(albedo,_HairShineTint.rgb,0.32)*_HairShineStrength*hairShape;
                float clothShape=pow(nh,max(_ClothShinePower,2.0))*(0.30+0.70*paintedShine);
                half3 shineCloth=albedo*_ClothShineTint.rgb*_ClothShineStrength*clothShape;
                float skinShape=pow(nh,max(_SkinShinePower,4.0))*(0.25+0.75*paintedShine);
                half3 shineSkin=lerp(albedo,_SkinShineTint.rgb,0.12)*_SkinShineStrength*skinShape;
                float metalShoulder=smoothstep(1.0-_MetalShineWidth-shineAA,1.0-_MetalShineWidth+shineAA,nh);
                float metalCore=smoothstep(1.0-_MetalShineWidth*0.23-shineAA,1.0-_MetalShineWidth*0.23+shineAA,nh);
                float metalShape=(0.23*metalShoulder+0.77*metalCore)*(0.55+0.45*paintedShine);
                half3 shineMetal=lerp(albedo,half3(1,1,1),0.38)*_MetalShineTint.rgb*_MetalShineStrength*metalShape;
                half3 classifiedSpec=(shineHair*specClass.r+shineCloth*specClass.g+shineSkin*specClass.b+shineMetal*specClass.a)*_LightColor0.rgb*band;
                spec=spec*(1.0-specCoverage)+classifiedSpec;
                // END GGST SPECULAR REFINEMENT calculations
// BEGIN GGST FOCUSED LIGHT specular replacement
                // Preserve the previous rim's band. Only the specular lobe
                // uses the unoccluded diffuse bands; eye/face glints are excluded.
                float focusedUnoccluded=smoothstep(_LightTreshold-soft,_LightTreshold+soft,signal);
                float focusedRegional=(cleanFaceBand*faceRegionMask+focusedSkinBand*bodySkinRegion+cleanSleeveBand*sleeveRegion+focusedTunicBand*tunicRegion+cleanClothBand*cleanOtherCloth)/max(cleanTotal,0.0001);
                float focusedSpecBand=lerp(focusedUnoccluded,focusedRegional,saturate(_CleanShadeEnabled)*cleanCoverage);
                float focusedSkinAA=max(fwidth(nh)*0.65,0.008);
                float focusedSkinShoulder=smoothstep(1.0-_FocusedSkinWidth-focusedSkinAA,1.0-_FocusedSkinWidth+focusedSkinAA,nh);
                float focusedSkinCore=smoothstep(1.0-_FocusedSkinWidth*0.45-focusedSkinAA,1.0-_FocusedSkinWidth*0.45+focusedSkinAA,nh);
                half3 focusedSkinShine=lerp(albedo,_SkinShineTint.rgb,0.12)*_FocusedSkinStrength*(0.8*focusedSkinShoulder+0.2*focusedSkinCore)*(0.7+0.3*paintedShine);
                focusedSkinShine=lerp(shineSkin,focusedSkinShine,focusedLegDomain*(1.0-head));
// BEGIN GGST THIGH LOBE specular
                // Immutable skin UVs place the painted lobe on the upper thigh.
                // The taper follows the existing skinning without modifying mesh data.
                float thighT=saturate((palettePixel.y-918.0)/82.0);
                // Follow the measured anterior meridian of the original UV island;
                // its ring spacing bends at y=981, so a straight UV line is not
                // a straight line on the existing thigh surface.
                float thighCenter=357.89;
                thighCenter+=(-0.44)*saturate((palettePixel.y-916.85)/11.84);
                thighCenter+=(-1.35)*saturate((palettePixel.y-928.69)/12.07);
                thighCenter+=(-1.70)*saturate((palettePixel.y-940.76)/13.24);
                thighCenter+=(-1.90)*saturate((palettePixel.y-954.0)/13.74);
                thighCenter+=(4.90)*saturate((palettePixel.y-967.74)/13.89);
                thighCenter+=(-1.30)*saturate((palettePixel.y-981.63)/9.42);
                thighCenter+=(-1.24)*saturate((palettePixel.y-991.05)/9.62);
                float thighHalfWidth=7.2*(1.0-pow(thighT,1.15));
                float thighEdge=thighHalfWidth-abs(palettePixel.x-thighCenter);
                float thighAA=max(fwidth(thighEdge)*0.65,0.35);
                float thighLobe=smoothstep(-thighAA,thighAA,thighEdge);
                thighLobe*=smoothstep(916.0,920.0,palettePixel.y)*(1.0-smoothstep(998.0,1001.0,palettePixel.y));
                float thighReplace=focusedLegDomain*(1.0-head)*(1.0-smoothstep(1015.0,1030.0,palettePixel.y));
                float thighFacing=smoothstep(0.2,0.55,nv)*smoothstep(0.50,0.68,nl);
                half3 thighShine=_ThighLobeTint.rgb*_ThighLobeStrength*thighLobe*thighFacing;
                focusedSkinShine=lerp(focusedSkinShine,thighShine,thighReplace*saturate(_ThighLobeEnabled));
// END GGST THIGH LOBE specular
                float4 focusedClasses=specClass*float4(1,1,1.0-faceRegionMask,1);
                float focusedSpecCoverage=saturate(dot(focusedClasses,float4(1,1,1,1)));
                half3 focusedOldSpec=(shineHair*focusedClasses.r+shineCloth*focusedClasses.g+shineSkin*focusedClasses.b+shineMetal*focusedClasses.a)*_LightColor0.rgb*band;
                half3 focusedNewSpec=(shineHair*_FocusedHairGain*focusedClasses.r+shineCloth*_FocusedClothGain*focusedClasses.g+focusedSkinShine*focusedClasses.b+shineMetal*_FocusedMetalGain*focusedClasses.a)*_LightColor0.rgb*focusedSpecBand;
                spec+=(focusedNewSpec-focusedOldSpec)*saturate(_FocusedSpecEnabled);
// END GGST FOCUSED LIGHT specular replacement

// BEGIN GGST RIM REFINE calculations
                // Artistic rim only: preserve the approved diffuse, specular,
                // eye, ink and shadow computations and the original fallback.
                // Material atlas excludes eyes/lips; face receives a softer rim.
                float rimAA=max(fwidth(nv)*0.65,0.008);
                float referenceRimEdge=1.0-smoothstep(_ReferenceRimWidth-rimAA,_ReferenceRimWidth+rimAA,nv);
                float rimMaterialScale=dot(specClass,_ReferenceRimMaterial)/max(specCoverage,0.0001);
                rimMaterialScale*=lerp(1.0,_ReferenceRimFaceScale,faceRegionMask);
                half3 referenceRimColor=lerp(albedo,_ReferenceRimTint.rgb,_ReferenceRimTintMix);
                float referenceRimLight=lerp(_ReferenceRimShadowFloor,1.0,saturate(band));
                half3 referenceRim=referenceRimColor*referenceRimEdge*_ReferenceRimStrength*rimMaterialScale*referenceRimLight*_LightColor0.rgb;
                rim=lerp(rim,referenceRim,saturate(_ReferenceRimEnabled)*specCoverage);
// END GGST RIM REFINE calculations
                half3 color=diffuse+ambient+rim+spec;
                // Restore verified line-shaped Alpha data after lighting, so rim does not erase ink.
// BEGIN GGST LINE REFINEMENT save lighting and specular
                half3 lineBaseColor=color;
// END GGST LINE REFINEMENT save lighting and specular
                color=lerp(color,_InnerLineColor.rgb,(1.0-saturate(ilm.a))*_InnerLineStrength);
// BEGIN GGST LINE REFINEMENT internal line
                float4 inkClass=saturate(tex2D(_FourMaterialSpecMask,i.uv.xy));
                float inkClassTotal=dot(inkClass,float4(1,1,1,1));
                float inkCoverage=saturate(inkClassTotal)*step(0.5,_LineRefineEnabled);
                float rawInk=1.0-saturate(ilm.a);
                // Only Alpha receives screen-footprint filtering. Original ILM
                // RGB lighting and sparse highlight data remain untouched.
                float2 inkDx=ddx(i.uv.xy)*0.28,inkDy=ddy(i.uv.xy)*0.28;
                float filteredInk=0.5*rawInk+0.125*(4.0-
                    tex2D(_LightMap,i.uv.xy+inkDx+inkDy).a-
                    tex2D(_LightMap,i.uv.xy+inkDx-inkDy).a-
                    tex2D(_LightMap,i.uv.xy-inkDx+inkDy).a-
                    tex2D(_LightMap,i.uv.xy-inkDx-inkDy).a);
                // Continuous coverage preserves minified thin painted lines.
                // Unclassified eyes, lips and detail keep the exact old blend.
                float refinedInk=lerp(rawInk,saturate(filteredInk),saturate(_LineInnerFilter));
                float inkStrength=dot(inkClass,_LineInnerStrengths)/max(inkClassTotal,0.0001);
                inkStrength*=_InnerLineStrength/0.65;
                half3 materialInk=(_LineHairInk.rgb*inkClass.r+_LineClothInk.rgb*inkClass.g+
                    _LineSkinInk.rgb*inkClass.b+_LineMetalInk.rgb*inkClass.a)/max(inkClassTotal,0.0001);
                half3 styledInk=lerp(_InnerLineColor.rgb,materialInk,saturate(_LineInnerTintMix));
                color=lerp(color,lerp(lineBaseColor,styledInk,saturate(refinedInk*inkStrength)),inkCoverage);
// END GGST LINE REFINEMENT internal line
// BEGIN GGST EYE REFINEMENT authored catchlight clarity
                half3 eyeBeforeCatch=color;
                half3 eyeCatchTarget=max(color,base*_LightColor0.rgb*_LightIntensity);
                color=lerp(color,eyeCatchTarget,saturate(_EyeCatchlightLift)*eyeCatchMask);
// END GGST EYE REFINEMENT authored catchlight clarity

                int mode=(int)(_DebugMode+0.5);
// BEGIN GGST FACE DIFFUSE diagnostics
if(mode==35)return half4(faceRefineGate.xxx,1);
                if(mode==36)return half4(abs(faceDiffuseDelta),1);
// END GGST FACE DIFFUSE diagnostics

// BEGIN GGST EYE REFINEMENT diagnostics
                if(mode==33)return half4(eyeIrisMask,eyeScleraMask,eyeCatchMask,1);
                if(mode==34)return half4(abs(eyeDiffuseDelta)+abs(color-eyeBeforeCatch),1);
// END GGST EYE REFINEMENT diagnostics

// BEGIN GGST LINE REFINEMENT diagnostics
                if(mode==30)return half4((refinedInk*inkCoverage).xxx,1);
                if(mode==31)return half4(styledInk*refinedInk*inkCoverage,1);
// END GGST LINE REFINEMENT diagnostics
// BEGIN GGST SHADOW REFINEMENT hair visibility diagnostic
                if(mode==32)return half4(hairFaceOcclusion.xxx,1);
// END GGST SHADOW REFINEMENT hair visibility diagnostic
                if(mode==1)return half4(base,1);
                if(mode==2)return half4(sss,1);
                if(mode==3)return half4(detail,1);
                if(mode==4)return half4(ilm.rrr,1);
                if(mode==5)return half4(ilm.ggg,1);
                if(mode==6)return half4(ilm.bbb,1);
                if(mode==7)return half4(ilm.aaa,1);
                if(mode==8)return half4(i.color.rrr,1);
                if(mode==9)return half4(n*0.5+0.5,1);
                if(mode==10)return half4(band.xxx,1);
                if(mode==11)return half4(rawShadow.xxx,1);
                if(mode==12)return half4(rim,1);
                if(mode==13)return half4(spec,1);
                if(mode==14)return half4(skin*half3(1,0.35,0.2)+hair*half3(0.2,0.4,1)+leather*half3(0.8,0.2,1)+metal*half3(0.2,1,0.8),1);
                if(mode==15)return half4(tex2D(_OutlineMap,i.uv.xy).rgb,1);
                if(mode==16)return half4(diffuse,1);
                if(mode==17)return half4(step(1.0,max(color.r,max(color.g,color.b)))*half3(1,0,0),1);
                if(mode==18)return half4(secondShade.xxx,1);
                if(mode==19)return half4(tasteHeight,tasteHorizontalNormal,tasteGradient,1);
                if(mode==20)return half4((faceRegion*float3(1,0.2,0.1)+legRegion*float3(0.1,1,0.2)+hair*float3(0.2,0.4,1)+coatRegion*float3(0.8,0.2,1))*regionalNl,1);
                if(mode==21)return half4(i.color.gba,1);
                if(mode==22)return half4(faceRegionMask,bodySkinRegion,sleeveRegion,1);
// BEGIN GGST PALETTE diagnostic
                if(mode==37)return half4(paletteGate,1);
// END GGST PALETTE diagnostic
// BEGIN GGST CLEAN SHADE diagnostic
                if(mode==38)return half4(cleanGate,1);
// END GGST CLEAN SHADE diagnostic
// BEGIN GGST FOCUSED LIGHT diagnostics
// BEGIN GGST THIGH LOBE diagnostics
                if(mode==43)return half4((thighReplace*bodySkinRegion).xxx,1);
                if(mode==44)return half4((thighLobe*thighFacing*thighReplace*bodySkinRegion).xxx,1);
// END GGST THIGH LOBE diagnostics
                if(mode==39)return half4(float3(saturate(focusedLegRegion+tunicRegion),focusedSpecCoverage,0),1);
                if(mode==40)return half4(focusedLegRegion.xxx,1);
                if(mode==41)return half4(lerp(cleanSkinBand,focusedSkinBand,saturate(_FocusedShadeEnabled)).xxx*focusedLegRegion,1);
                if(mode==42)return half4(lerp(cleanTunicBand,focusedTunicBand,saturate(_FocusedShadeEnabled)).xxx*tunicRegion,1);
// END GGST FOCUSED LIGHT diagnostics
                if(mode==23)return half4(lerp(band,regionalSignal,regionTotal).xxx,1);
                if(mode==24)return half4(lerp(albedo,dark,regionTotal),1);
                // BEGIN GGST SPECULAR REFINEMENT diagnostics
                if(mode==25)return half4(specClass.r+specClass.a,specClass.g+specClass.a,specClass.b+specClass.a,1);
                if(mode==26)return half4(shineHair*specClass.r*_LightColor0.rgb*band,1);
                if(mode==27)return half4(shineCloth*specClass.g*_LightColor0.rgb*band,1);
                if(mode==28)return half4(shineSkin*specClass.b*_LightColor0.rgb*band,1);
                if(mode==29)return half4(shineMetal*specClass.a*_LightColor0.rgb*band,1);
                // END GGST SPECULAR REFINEMENT diagnostics
                return half4(color,1);
            }
            ENDCG
        }
        Pass
        {
            Name "OUTLINE"
            Tags {"LightMode"="Always"}
            Cull Front ZWrite Off ZTest LEqual
            CGPROGRAM
            #pragma target 3.0
            #pragma vertex vertOutline
            #pragma fragment fragOutline
            #include "UnityCG.cginc"
            sampler2D _LightMap,_OutlineMap;
// BEGIN GGST LINE REFINEMENT outline declarations
            sampler2D _FourMaterialSpecMask;
            float _LineRefineEnabled,_LineContourTintMix,_LineInnerFilter,_LineInnerTintMix;
            float4 _LineContourWidths,_LineInnerStrengths;
            half4 _LineHairInk,_LineClothInk,_LineSkinInk,_LineMetalInk;
// END GGST LINE REFINEMENT outline declarations
            float4 _MainTex_ST;
            float _UseMirroredUV,_OutlineWidth,_OutlineSkinScale,_OutlineMapStrength,_LayerMaskStep,_DebugMode,_UseSmoothOutline;
            half4 _OutlineColor;
            struct a {float4 vertex:POSITION;float3 normal:NORMAL;float4 smoothNormal:TANGENT;float2 uv:TEXCOORD0;float2 mirror:TEXCOORD2;};
            struct f {float4 pos:SV_POSITION;float2 uv:TEXCOORD0;};
            f vertOutline(a v)
            {
                f o; o.pos=UnityObjectToClipPos(v.vertex);
                o.uv=TRANSFORM_TEX(lerp(v.uv,v.mirror,step(0.5,_UseMirroredUV)),_MainTex);
                float layer=tex2Dlod(_LightMap,float4(o.uv,0,0)).r*255.0;
                float skin=step(10.0,layer)*(1.0-step(_LayerMaskStep,layer));
                float3 outlineNormal=normalize(lerp(v.normal,v.smoothNormal.xyz,step(0.5,_UseSmoothOutline)));
                float3 wn=UnityObjectToWorldNormal(outlineNormal);
                float3 vn=mul((float3x3)UNITY_MATRIX_V,wn);
                float2 direction=float2(UNITY_MATRIX_P[0][0]*vn.x,UNITY_MATRIX_P[1][1]*vn.y)*_ScreenParams.xy;
                direction/=max(length(direction),0.0001);
                float width=_OutlineWidth*lerp(1.0,_OutlineSkinScale,skin);
// BEGIN GGST LINE REFINEMENT contour width
                // Reuse the audited class atlas rather than confusing white
                // cloth with low-ILM-R skin. Existing zero-width layers stay off.
                float4 contourClass=saturate(tex2Dlod(_FourMaterialSpecMask,float4(o.uv,0,0)));
                float contourTotal=dot(contourClass,float4(1,1,1,1));
                float styledWidth=_OutlineWidth*dot(contourClass,_LineContourWidths/0.8)/max(contourTotal,0.0001);
                width=lerp(width,styledWidth,saturate(contourTotal)*step(0.5,_LineRefineEnabled));
// END GGST LINE REFINEMENT contour width
                o.pos.xy+=direction*(2.0*width/_ScreenParams.xy)*o.pos.w;
                return o;
            }
            half4 fragOutline(f i):SV_Target
            {
                clip(_OutlineWidth-0.001); clip(0.5-_DebugMode);
                half3 map=tex2D(_OutlineMap,i.uv).rgb;
// BEGIN GGST LINE REFINEMENT contour ink
                if(_LineRefineEnabled>0.5)
                {
                    float4 contourClass=saturate(tex2D(_FourMaterialSpecMask,i.uv));
                    float contourTotal=dot(contourClass,float4(1,1,1,1));
                    half3 materialInk=(_LineHairInk.rgb*contourClass.r+_LineClothInk.rgb*contourClass.g+
                        _LineSkinInk.rgb*contourClass.b+_LineMetalInk.rgb*contourClass.a)/max(contourTotal,0.0001);
                    // OLM is authored sRGB color, not an alpha width mask.
                    // Retain its black/gray region distinction in the new tint.
                    materialInk*=lerp(0.78,1.0,saturate(map.r/0.03310477));
                    half3 originalInk=lerp(_OutlineColor.rgb,map,_OutlineMapStrength);
                    return half4(lerp(originalInk,materialInk,saturate(contourTotal)*saturate(_LineContourTintMix)),1);
                }
// END GGST LINE REFINEMENT contour ink
                return half4(lerp(_OutlineColor.rgb,map,_OutlineMapStrength),1);
            }
            ENDCG
        }
        Pass
        {
            Name "SHADOWCASTER"
            Tags {"LightMode"="ShadowCaster"}
            Cull [_CullMode] ZWrite On ZTest LEqual
            CGPROGRAM
            #pragma vertex vertShadow
            #pragma fragment fragShadow
            #pragma multi_compile_shadowcaster
            #include "UnityCG.cginc"
            struct v2f {V2F_SHADOW_CASTER;};
            v2f vertShadow(appdata_base v){v2f o;TRANSFER_SHADOW_CASTER_NORMALOFFSET(o);return o;}
            float4 fragShadow(v2f i):SV_Target{SHADOW_CASTER_FRAGMENT(i)}
            ENDCG
        }
    }
    Fallback Off
}
