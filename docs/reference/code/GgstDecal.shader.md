# GgstDecal.shader

按行查找正文中的函数与Pass。以下保留源码原文，属性拼写与分支顺序以此为准。代码依赖所用渲染管线及[输入连接](../dependencies.md)，不能把文件索引当作独立工程。

| 行 | 代码 |
|---|---|
| <a id="l1"></a>1 | <code>Shader "GGST/DecalX2Multiply" {</code> |
| <a id="l2"></a>2 | <code>    Properties { _MainTex ("原版贴花（线性数据）",2D)="gray"{} _Strength("贴花强度",Range(0,1))=1 }</code> |
| <a id="l3"></a>3 | <code>    SubShader {</code> |
| <a id="l4"></a>4 | <code>        Tags {"Queue"="Geometry+10" "RenderType"="Transparent"}</code> |
| <a id="l5"></a>5 | <code>        Pass {</code> |
| <a id="l6"></a>6 | <code>            Cull Off ZWrite Off ZTest LEqual Offset -1,-1</code> |
| <a id="l7"></a>7 | <code>            // Native M_CharaDecal uses BLEND_X2Multiply: 50% grey is neutral.</code> |
| <a id="l8"></a>8 | <code>            Blend DstColor SrcColor</code> |
| <a id="l9"></a>9 | <code>            CGPROGRAM</code> |
| <a id="l10"></a>10 | <code>            #pragma vertex vert</code> |
| <a id="l11"></a>11 | <code>            #pragma fragment frag</code> |
| <a id="l12"></a>12 | <code>            #include "UnityCG.cginc"</code> |
| <a id="l13"></a>13 | <code>            struct a {float4 vertex:POSITION;float2 uv:TEXCOORD0;};</code> |
| <a id="l14"></a>14 | <code>            struct f {float4 pos:SV_POSITION;float2 uv:TEXCOORD0;};</code> |
| <a id="l15"></a>15 | <code>            sampler2D _MainTex;float4 _MainTex_ST;float _Strength;</code> |
| <a id="l16"></a>16 | <code>            f vert(a v){f o;o.pos=UnityObjectToClipPos(v.vertex);o.uv=TRANSFORM_TEX(v.uv,_MainTex);return o;}</code> |
| <a id="l17"></a>17 | <code>            fixed4 frag(f i):SV_Target{return fixed4(lerp(0.5,tex2D(_MainTex,i.uv).rgb,_Strength),0.5);}</code> |
| <a id="l18"></a>18 | <code>            ENDCG</code> |
| <a id="l19"></a>19 | <code>        }</code> |
| <a id="l20"></a>20 | <code>    }</code> |
| <a id="l21"></a>21 | <code>}</code> |
