Shader "GGST/GlowBase" {
    Properties { _MainTex("原版发光基础色",2D)="white"{} _GlowMultiplier("发光倍率",Float)=2 }
    SubShader {
        Tags {"Queue"="Geometry" "RenderType"="Opaque"}
        Pass {
            Cull Back ZWrite On
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            struct a {float4 vertex:POSITION;float2 uv:TEXCOORD0;};
            struct f {float4 pos:SV_POSITION;float2 uv:TEXCOORD0;};
            sampler2D _MainTex;float4 _MainTex_ST;float _GlowMultiplier;
            f vert(a v){f o;o.pos=UnityObjectToClipPos(v.vertex);o.uv=TRANSFORM_TEX(v.uv,_MainTex);return o;}
            fixed4 frag(f i):SV_Target{return fixed4(tex2D(_MainTex,i.uv).rgb*_GlowMultiplier,1);}
            ENDCG
        }
    }
}
