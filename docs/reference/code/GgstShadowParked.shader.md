# GgstShadowParked.shader 逐行索引

原文件：`sources/GgstShadowParked.shader`；原工程路径：`Assets/GGST_RenderFix/GgstShadowParked.shader`。

SHA256：`3d2c83fbd22c650566fc7f8626c95462536d1beb07b37630e65b84d3cd0978e2`。以下由原文生成，未修正拼写或分支。每行锚点用于正文核查；这是源码摘录索引，不是可直接运行工程。

| 行 | 原文 |
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
