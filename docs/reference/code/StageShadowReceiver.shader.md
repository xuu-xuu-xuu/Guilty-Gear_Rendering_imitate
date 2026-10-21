# StageShadowReceiver.shader

按行查找正文中的函数与Pass。以下保留源码原文，属性拼写与分支顺序以此为准。代码依赖所用渲染管线及[输入连接](../dependencies.md)，不能把文件索引当作独立工程。

| 行 | 代码 |
|---|---|
| <a id="l1"></a>1 | <code>Shader "GGST/StageShadowReceiver"</code> |
| <a id="l2"></a>2 | <code>{</code> |
| <a id="l3"></a>3 | <code>    Properties</code> |
| <a id="l4"></a>4 | <code>    {</code> |
| <a id="l5"></a>5 | <code>// BEGIN GGST SHADOW REFINEMENT stage properties</code> |
| <a id="l6"></a>6 | <code>        _GeometryShadowFloor ("投影最低可见率",Range(0,1))=0.10</code> |
| <a id="l7"></a>7 | <code>        _GeometryShadowBias ("投影深度偏移/米",Range(0,0.02))=0.001</code> |
| <a id="l8"></a>8 | <code>        _GeometryShadowFilter ("投影边缘过滤/贴素",Range(0,4))=0.8</code> |
| <a id="l9"></a>9 | <code>        _GeometryShadowFade ("离接收面距离衰减",Range(0,0.5))=0.08</code> |
| <a id="l10"></a>10 | <code>// END GGST SHADOW REFINEMENT stage properties</code> |
| <a id="l11"></a>11 | <code>        // sRGB-facing color: the reference backdrop reads 179/255 on the bright side.</code> |
| <a id="l12"></a>12 | <code>        _Color ("Backdrop Color", Color) = (0.702, 0.702, 0.702, 1)</code> |
| <a id="l13"></a>13 | <code>        // Reference backdrop falls from 179 (right) to 155 (left): 155/179 = 0.866.</code> |
| <a id="l14"></a>14 | <code>        _GradientStrength ("Horizontal Falloff", Range(0, 1)) = 0.134</code> |
| <a id="l15"></a>15 | <code>    }</code> |
| <a id="l16"></a>16 | <code>    SubShader</code> |
| <a id="l17"></a>17 | <code>    {</code> |
| <a id="l18"></a>18 | <code>        Tags { "RenderType" = "Opaque" "Queue" = "Geometry" }</code> |
| <a id="l19"></a>19 | <code>        Pass</code> |
| <a id="l20"></a>20 | <code>        {</code> |
| <a id="l21"></a>21 | <code>            Tags { "LightMode" = "ForwardBase" }</code> |
| <a id="l22"></a>22 | <code>            CGPROGRAM</code> |
| <a id="l23"></a>23 | <code>            #pragma vertex vert</code> |
| <a id="l24"></a>24 | <code>            #pragma fragment frag</code> |
| <a id="l25"></a>25 | <code>            #pragma multi_compile_fwdbase</code> |
| <a id="l26"></a>26 | <code>            #pragma multi_compile_fog</code> |
| <a id="l27"></a>27 | <code>            #include "UnityCG.cginc"</code> |
| <a id="l28"></a>28 | <code>            #include "AutoLight.cginc"</code> |
| <a id="l29"></a>29 | <code></code> |
| <a id="l30"></a>30 | <code>            struct appdata { float4 vertex : POSITION; };</code> |
| <a id="l31"></a>31 | <code>// BEGIN GGST SHADOW REFINEMENT stage varying</code> |
| <a id="l32"></a>32 | <code>#if 0</code> |
| <a id="l33"></a>33 | <code>            struct v2f { float4 pos : SV_POSITION; SHADOW_COORDS(0) UNITY_FOG_COORDS(1) };</code> |
| <a id="l34"></a>34 | <code>#else</code> |
| <a id="l35"></a>35 | <code>            struct v2f { float4 pos : SV_POSITION; SHADOW_COORDS(0) UNITY_FOG_COORDS(1) float3 worldPos:TEXCOORD2; };</code> |
| <a id="l36"></a>36 | <code>#endif</code> |
| <a id="l37"></a>37 | <code>// END GGST SHADOW REFINEMENT stage varying</code> |
| <a id="l38"></a>38 | <code></code> |
| <a id="l39"></a>39 | <code>// BEGIN GGST SHADOW REFINEMENT stage sampling declarations</code> |
| <a id="l40"></a>40 | <code>            sampler2D _StageShadowDepth;</code> |
| <a id="l41"></a>41 | <code>            float4x4 _StageShadowVP;</code> |
| <a id="l42"></a>42 | <code>            float4 _StageShadowOriginRange,_StageShadowForward,_StageShadowTexel;</code> |
| <a id="l43"></a>43 | <code>            float _StageShadowEnabled,_GeometryShadowFloor,_GeometryShadowBias,_GeometryShadowFilter,_GeometryShadowFade;</code> |
| <a id="l44"></a>44 | <code>            float GeometryStageVisibility(float3 world)</code> |
| <a id="l45"></a>45 | <code>            {</code> |
| <a id="l46"></a>46 | <code>                float4 clipSpace=mul(_StageShadowVP,float4(world,1));</code> |
| <a id="l47"></a>47 | <code>                float2 uv=clipSpace.xy/max(clipSpace.w,0.00001)*0.5+0.5;</code> |
| <a id="l48"></a>48 | <code>                float depth=dot(world-_StageShadowOriginRange.xyz,_StageShadowForward.xyz)/max(_StageShadowOriginRange.w,0.00001);</code> |
| <a id="l49"></a>49 | <code>                float inside=step(0,uv.x)*step(uv.x,1)*step(0,uv.y)*step(uv.y,1)*step(0,depth)*step(depth,1);</code> |
| <a id="l50"></a>50 | <code>                float closest=tex2D(_StageShadowDepth,uv).r;</code> |
| <a id="l51"></a>51 | <code>                float separation=max(0,(depth-closest)*_StageShadowOriginRange.w);</code> |
| <a id="l52"></a>52 | <code>                float radius=_GeometryShadowFilter*(1+min(separation*0.6,1.5));</code> |
| <a id="l53"></a>53 | <code>                float bias=_GeometryShadowBias/max(_StageShadowOriginRange.w,0.00001);</code> |
| <a id="l54"></a>54 | <code>                float visibility=0;</code> |
| <a id="l55"></a>55 | <code>                [unroll] for(int x=-1;x&lt;=1;x++)</code> |
| <a id="l56"></a>56 | <code>                [unroll] for(int y=-1;y&lt;=1;y++)</code> |
| <a id="l57"></a>57 | <code>                    visibility+=step(depth-bias,tex2D(_StageShadowDepth,uv+float2(x,y)*_StageShadowTexel.xy*radius).r);</code> |
| <a id="l58"></a>58 | <code>                float occlusion=(1-visibility/9)*inside*saturate(1-separation*_GeometryShadowFade);</code> |
| <a id="l59"></a>59 | <code>                return 1-occlusion*(1-saturate(_GeometryShadowFloor));</code> |
| <a id="l60"></a>60 | <code>            }</code> |
| <a id="l61"></a>61 | <code>// END GGST SHADOW REFINEMENT stage sampling declarations</code> |
| <a id="l62"></a>62 | <code>            fixed4 _Color;</code> |
| <a id="l63"></a>63 | <code>            float _GradientStrength;</code> |
| <a id="l64"></a>64 | <code></code> |
| <a id="l65"></a>65 | <code>            v2f vert (appdata v)</code> |
| <a id="l66"></a>66 | <code>            {</code> |
| <a id="l67"></a>67 | <code>                v2f o;</code> |
| <a id="l68"></a>68 | <code>                o.pos = UnityObjectToClipPos(v.vertex);</code> |
| <a id="l69"></a>69 | <code>                TRANSFER_SHADOW(o);</code> |
| <a id="l70"></a>70 | <code>                UNITY_TRANSFER_FOG(o, o.pos);</code> |
| <a id="l71"></a>71 | <code>// BEGIN GGST SHADOW REFINEMENT stage world position</code> |
| <a id="l72"></a>72 | <code>                o.worldPos=mul(unity_ObjectToWorld,v.vertex).xyz;</code> |
| <a id="l73"></a>73 | <code>// END GGST SHADOW REFINEMENT stage world position</code> |
| <a id="l74"></a>74 | <code>                return o;</code> |
| <a id="l75"></a>75 | <code>            }</code> |
| <a id="l76"></a>76 | <code></code> |
| <a id="l77"></a>77 | <code>            // Fixed screen-space brightness like the reference backdrop, darkened only by realtime shadows.</code> |
| <a id="l78"></a>78 | <code>            fixed4 frag (v2f i) : SV_Target</code> |
| <a id="l79"></a>79 | <code>            {</code> |
| <a id="l80"></a>80 | <code>                fixed atten = SHADOW_ATTENUATION(i);</code> |
| <a id="l81"></a>81 | <code>// BEGIN GGST SHADOW REFINEMENT stage independent projection</code> |
| <a id="l82"></a>82 | <code>                if(_StageShadowEnabled&gt;0.5)atten=GeometryStageVisibility(i.worldPos);</code> |
| <a id="l83"></a>83 | <code>// END GGST SHADOW REFINEMENT stage independent projection</code> |
| <a id="l84"></a>84 | <code>                fixed u = saturate(i.pos.x / _ScreenParams.x);</code> |
| <a id="l85"></a>85 | <code>                fixed falloff = lerp(1.0 - _GradientStrength, 1.0, u);</code> |
| <a id="l86"></a>86 | <code>                fixed3 c = _Color.rgb * atten * falloff;</code> |
| <a id="l87"></a>87 | <code>                UNITY_APPLY_FOG(i.fogCoord, c);</code> |
| <a id="l88"></a>88 | <code>                return fixed4(c, 1);</code> |
| <a id="l89"></a>89 | <code>            }</code> |
| <a id="l90"></a>90 | <code>            ENDCG</code> |
| <a id="l91"></a>91 | <code>        }</code> |
| <a id="l92"></a>92 | <code>        UsePass "Legacy Shaders/VertexLit/SHADOWCASTER"</code> |
| <a id="l93"></a>93 | <code>    }</code> |
| <a id="l94"></a>94 | <code>    Fallback "Legacy Shaders/Diffuse"</code> |
| <a id="l95"></a>95 | <code>}</code> |
