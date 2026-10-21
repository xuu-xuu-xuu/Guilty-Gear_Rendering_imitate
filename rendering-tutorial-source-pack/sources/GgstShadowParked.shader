Shader "GGST/NativeShadowGeometryParked" {
    SubShader {
        Tags {"Queue"="Geometry" "RenderType"="Opaque"}
        Pass { ZWrite Off ColorMask 0
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            float4 vert(float4 vertex:POSITION):SV_POSITION{return UnityObjectToClipPos(vertex);}
            fixed4 frag():SV_Target{clip(-1);return 0;}
            ENDCG
        }
    }
}
