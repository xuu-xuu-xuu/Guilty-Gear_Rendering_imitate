Shader "GGST/DecalX2Multiply" {
    Properties { _MainTex ("原版贴花（线性数据）",2D)="gray"{} _Strength("贴花强度",Range(0,1))=1 }
    SubShader {
        Tags {"Queue"="Geometry+10" "RenderType"="Transparent"}
        Pass {
            Cull Off ZWrite Off ZTest LEqual Offset -1,-1
            // Native M_CharaDecal uses BLEND_X2Multiply: 50% grey is neutral.
            Blend DstColor SrcColor
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            struct a {float4 vertex:POSITION;float2 uv:TEXCOORD0;};
            struct f {float4 pos:SV_POSITION;float2 uv:TEXCOORD0;};
            sampler2D _MainTex;float4 _MainTex_ST;float _Strength;
            f vert(a v){f o;o.pos=UnityObjectToClipPos(v.vertex);o.uv=TRANSFORM_TEX(v.uv,_MainTex);return o;}
            fixed4 frag(f i):SV_Target{return fixed4(lerp(0.5,tex2D(_MainTex,i.uv).rgb,_Strength),0.5);}
            ENDCG
        }
    }
}
