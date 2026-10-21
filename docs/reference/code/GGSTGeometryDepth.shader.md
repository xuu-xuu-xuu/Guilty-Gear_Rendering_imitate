# GGSTGeometryDepth.shader 逐行索引

原文件：`sources/GGSTGeometryDepth.shader`；原工程路径：`Assets/GGST_Imitate/GeometryShadows/GGSTGeometryDepth.shader`。

SHA256：`f95b339c6837532ed9618ba5c8804f6665caedc499b5eda6e275c986a3f3d04e`。以下由原文生成，未修正拼写或分支。每行锚点用于正文核查；这是源码摘录索引，不是可直接运行工程。

| 行 | 原文 |
|---|---|
| <a id="l1"></a>1 | <code>Shader "GGST/GeometryShadowDepth"</code> |
| <a id="l2"></a>2 | <code>{</code> |
| <a id="l3"></a>3 | <code>    SubShader</code> |
| <a id="l4"></a>4 | <code>    {</code> |
| <a id="l5"></a>5 | <code>        Tags { "RenderType"="Opaque" "Queue"="Geometry" }</code> |
| <a id="l6"></a>6 | <code>        Pass</code> |
| <a id="l7"></a>7 | <code>        {</code> |
| <a id="l8"></a>8 | <code>            Name "GEOMETRY_DEPTH"</code> |
| <a id="l9"></a>9 | <code>            Cull Off ZWrite On ZTest LEqual Blend Off</code> |
| <a id="l10"></a>10 | <code>            CGPROGRAM</code> |
| <a id="l11"></a>11 | <code>            #pragma target 3.0</code> |
| <a id="l12"></a>12 | <code>            #pragma vertex vert</code> |
| <a id="l13"></a>13 | <code>            #pragma fragment frag</code> |
| <a id="l14"></a>14 | <code>            #include "UnityCG.cginc"</code> |
| <a id="l15"></a>15 | <code>            // Unique command-buffer globals, never original material uniforms.</code> |
| <a id="l16"></a>16 | <code>            sampler2D _GGSTShadowCasterHairMask;</code> |
| <a id="l17"></a>17 | <code>            float _GGSTShadowCasterHairOnly,_GGSTShadowCasterUseMirror;</code> |
| <a id="l18"></a>18 | <code>            float4 _GGSTShadowCasterTexST;</code> |
| <a id="l19"></a>19 | <code>            float4 _GGSTShadowCasterOriginRange,_GGSTShadowCasterForward;</code> |
| <a id="l20"></a>20 | <code>            struct a</code> |
| <a id="l21"></a>21 | <code>            {</code> |
| <a id="l22"></a>22 | <code>                float4 vertex:POSITION;</code> |
| <a id="l23"></a>23 | <code>                float2 uv:TEXCOORD0;</code> |
| <a id="l24"></a>24 | <code>                float2 mirror:TEXCOORD2;</code> |
| <a id="l25"></a>25 | <code>            };</code> |
| <a id="l26"></a>26 | <code>            struct f { float4 pos:SV_POSITION; float3 world:TEXCOORD0; float2 uv:TEXCOORD1; };</code> |
| <a id="l27"></a>27 | <code>            f vert(a v)</code> |
| <a id="l28"></a>28 | <code>            {</code> |
| <a id="l29"></a>29 | <code>                f o;</code> |
| <a id="l30"></a>30 | <code>                // DrawRenderer consumes the existing native skinned stream.</code> |
| <a id="l31"></a>31 | <code>                // This shader performs no skinning, rebind or custom bone reads.</code> |
| <a id="l32"></a>32 | <code>                o.pos=UnityObjectToClipPos(v.vertex);</code> |
| <a id="l33"></a>33 | <code>                o.world=mul(unity_ObjectToWorld,v.vertex).xyz;</code> |
| <a id="l34"></a>34 | <code>                o.uv=lerp(v.uv,v.mirror,step(0.5,_GGSTShadowCasterUseMirror));</code> |
| <a id="l35"></a>35 | <code>                o.uv=o.uv*_GGSTShadowCasterTexST.xy+_GGSTShadowCasterTexST.zw;</code> |
| <a id="l36"></a>36 | <code>                return o;</code> |
| <a id="l37"></a>37 | <code>            }</code> |
| <a id="l38"></a>38 | <code>            float4 frag(f i):SV_Target</code> |
| <a id="l39"></a>39 | <code>            {</code> |
| <a id="l40"></a>40 | <code>                if(_GGSTShadowCasterHairOnly&gt;0.5)</code> |
| <a id="l41"></a>41 | <code>                    clip(tex2D(_GGSTShadowCasterHairMask,i.uv).r-0.5);</code> |
| <a id="l42"></a>42 | <code>                // Original base alpha is encoded data (gold hair mostly 66/67),</code> |
| <a id="l43"></a>43 | <code>                // and ILM alpha is ink. Neither is used as transparency here.</code> |
| <a id="l44"></a>44 | <code>                float d=dot(i.world-_GGSTShadowCasterOriginRange.xyz,</code> |
| <a id="l45"></a>45 | <code>                            _GGSTShadowCasterForward.xyz)/max(_GGSTShadowCasterOriginRange.w,0.0001);</code> |
| <a id="l46"></a>46 | <code>                return float4(saturate(d),0,0,1);</code> |
| <a id="l47"></a>47 | <code>            }</code> |
| <a id="l48"></a>48 | <code>            ENDCG</code> |
| <a id="l49"></a>49 | <code>        }</code> |
| <a id="l50"></a>50 | <code>    }</code> |
| <a id="l51"></a>51 | <code>    Fallback Off</code> |
| <a id="l52"></a>52 | <code>}</code> |
