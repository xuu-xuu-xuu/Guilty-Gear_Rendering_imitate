# GgstShadowParked.shader

按行查找正文中的函数与Pass。以下保留源码原文，属性拼写与分支顺序以此为准。代码依赖所用渲染管线及[输入连接](../dependencies.md)，不能把文件索引当作独立工程。

| 行 | 代码 |
|---|---|
| <a id="l1"></a>1 | <code>Shader "GGST/NativeShadowGeometryParked" {</code> |
| <a id="l2"></a>2 | <code>    SubShader {</code> |
| <a id="l3"></a>3 | <code>        Tags {"Queue"="Geometry" "RenderType"="Opaque"}</code> |
| <a id="l4"></a>4 | <code>        Pass { ZWrite Off ColorMask 0</code> |
| <a id="l5"></a>5 | <code>            CGPROGRAM</code> |
| <a id="l6"></a>6 | <code>            #pragma vertex vert</code> |
| <a id="l7"></a>7 | <code>            #pragma fragment frag</code> |
| <a id="l8"></a>8 | <code>            #include "UnityCG.cginc"</code> |
| <a id="l9"></a>9 | <code>            float4 vert(float4 vertex:POSITION):SV_POSITION{return UnityObjectToClipPos(vertex);}</code> |
| <a id="l10"></a>10 | <code>            fixed4 frag():SV_Target{clip(-1);return 0;}</code> |
| <a id="l11"></a>11 | <code>            ENDCG</code> |
| <a id="l12"></a>12 | <code>        }</code> |
| <a id="l13"></a>13 | <code>    }</code> |
| <a id="l14"></a>14 | <code>}</code> |
