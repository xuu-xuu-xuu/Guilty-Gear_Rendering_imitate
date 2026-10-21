Shader "GGST/GeometryShadowDepth"
{
    SubShader
    {
        Tags { "RenderType"="Opaque" "Queue"="Geometry" }
        Pass
        {
            Name "GEOMETRY_DEPTH"
            Cull Off ZWrite On ZTest LEqual Blend Off
            CGPROGRAM
            #pragma target 3.0
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            // Unique command-buffer globals, never original material uniforms.
            sampler2D _GGSTShadowCasterHairMask;
            float _GGSTShadowCasterHairOnly,_GGSTShadowCasterUseMirror;
            float4 _GGSTShadowCasterTexST;
            float4 _GGSTShadowCasterOriginRange,_GGSTShadowCasterForward;
            struct a
            {
                float4 vertex:POSITION;
                float2 uv:TEXCOORD0;
                float2 mirror:TEXCOORD2;
            };
            struct f { float4 pos:SV_POSITION; float3 world:TEXCOORD0; float2 uv:TEXCOORD1; };
            f vert(a v)
            {
                f o;
                // DrawRenderer consumes the existing native skinned stream.
                // This shader performs no skinning, rebind or custom bone reads.
                o.pos=UnityObjectToClipPos(v.vertex);
                o.world=mul(unity_ObjectToWorld,v.vertex).xyz;
                o.uv=lerp(v.uv,v.mirror,step(0.5,_GGSTShadowCasterUseMirror));
                o.uv=o.uv*_GGSTShadowCasterTexST.xy+_GGSTShadowCasterTexST.zw;
                return o;
            }
            float4 frag(f i):SV_Target
            {
                if(_GGSTShadowCasterHairOnly>0.5)
                    clip(tex2D(_GGSTShadowCasterHairMask,i.uv).r-0.5);
                // Original base alpha is encoded data (gold hair mostly 66/67),
                // and ILM alpha is ink. Neither is used as transparency here.
                float d=dot(i.world-_GGSTShadowCasterOriginRange.xyz,
                            _GGSTShadowCasterForward.xyz)/max(_GGSTShadowCasterOriginRange.w,0.0001);
                return float4(saturate(d),0,0,1);
            }
            ENDCG
        }
    }
    Fallback Off
}
