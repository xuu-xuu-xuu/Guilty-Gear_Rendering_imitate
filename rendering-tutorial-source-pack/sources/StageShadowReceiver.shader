Shader "GGST/StageShadowReceiver"
{
    Properties
    {
// BEGIN GGST SHADOW REFINEMENT stage properties
        _GeometryShadowFloor ("投影最低可见率",Range(0,1))=0.10
        _GeometryShadowBias ("投影深度偏移/米",Range(0,0.02))=0.001
        _GeometryShadowFilter ("投影边缘过滤/贴素",Range(0,4))=0.8
        _GeometryShadowFade ("离接收面距离衰减",Range(0,0.5))=0.08
// END GGST SHADOW REFINEMENT stage properties
        // sRGB-facing color: the reference backdrop reads 179/255 on the bright side.
        _Color ("Backdrop Color", Color) = (0.702, 0.702, 0.702, 1)
        // Reference backdrop falls from 179 (right) to 155 (left): 155/179 = 0.866.
        _GradientStrength ("Horizontal Falloff", Range(0, 1)) = 0.134
    }
    SubShader
    {
        Tags { "RenderType" = "Opaque" "Queue" = "Geometry" }
        Pass
        {
            Tags { "LightMode" = "ForwardBase" }
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_fwdbase
            #pragma multi_compile_fog
            #include "UnityCG.cginc"
            #include "AutoLight.cginc"

            struct appdata { float4 vertex : POSITION; };
// BEGIN GGST SHADOW REFINEMENT stage varying
#if 0
            struct v2f { float4 pos : SV_POSITION; SHADOW_COORDS(0) UNITY_FOG_COORDS(1) };
#else
            struct v2f { float4 pos : SV_POSITION; SHADOW_COORDS(0) UNITY_FOG_COORDS(1) float3 worldPos:TEXCOORD2; };
#endif
// END GGST SHADOW REFINEMENT stage varying

// BEGIN GGST SHADOW REFINEMENT stage sampling declarations
            sampler2D _StageShadowDepth;
            float4x4 _StageShadowVP;
            float4 _StageShadowOriginRange,_StageShadowForward,_StageShadowTexel;
            float _StageShadowEnabled,_GeometryShadowFloor,_GeometryShadowBias,_GeometryShadowFilter,_GeometryShadowFade;
            float GeometryStageVisibility(float3 world)
            {
                float4 clipSpace=mul(_StageShadowVP,float4(world,1));
                float2 uv=clipSpace.xy/max(clipSpace.w,0.00001)*0.5+0.5;
                float depth=dot(world-_StageShadowOriginRange.xyz,_StageShadowForward.xyz)/max(_StageShadowOriginRange.w,0.00001);
                float inside=step(0,uv.x)*step(uv.x,1)*step(0,uv.y)*step(uv.y,1)*step(0,depth)*step(depth,1);
                float closest=tex2D(_StageShadowDepth,uv).r;
                float separation=max(0,(depth-closest)*_StageShadowOriginRange.w);
                float radius=_GeometryShadowFilter*(1+min(separation*0.6,1.5));
                float bias=_GeometryShadowBias/max(_StageShadowOriginRange.w,0.00001);
                float visibility=0;
                [unroll] for(int x=-1;x<=1;x++)
                [unroll] for(int y=-1;y<=1;y++)
                    visibility+=step(depth-bias,tex2D(_StageShadowDepth,uv+float2(x,y)*_StageShadowTexel.xy*radius).r);
                float occlusion=(1-visibility/9)*inside*saturate(1-separation*_GeometryShadowFade);
                return 1-occlusion*(1-saturate(_GeometryShadowFloor));
            }
// END GGST SHADOW REFINEMENT stage sampling declarations
            fixed4 _Color;
            float _GradientStrength;

            v2f vert (appdata v)
            {
                v2f o;
                o.pos = UnityObjectToClipPos(v.vertex);
                TRANSFER_SHADOW(o);
                UNITY_TRANSFER_FOG(o, o.pos);
// BEGIN GGST SHADOW REFINEMENT stage world position
                o.worldPos=mul(unity_ObjectToWorld,v.vertex).xyz;
// END GGST SHADOW REFINEMENT stage world position
                return o;
            }

            // Fixed screen-space brightness like the reference backdrop, darkened only by realtime shadows.
            fixed4 frag (v2f i) : SV_Target
            {
                fixed atten = SHADOW_ATTENUATION(i);
// BEGIN GGST SHADOW REFINEMENT stage independent projection
                if(_StageShadowEnabled>0.5)atten=GeometryStageVisibility(i.worldPos);
// END GGST SHADOW REFINEMENT stage independent projection
                fixed u = saturate(i.pos.x / _ScreenParams.x);
                fixed falloff = lerp(1.0 - _GradientStrength, 1.0, u);
                fixed3 c = _Color.rgb * atten * falloff;
                UNITY_APPLY_FOG(i.fogCoord, c);
                return fixed4(c, 1);
            }
            ENDCG
        }
        UsePass "Legacy Shaders/VertexLit/SHADOWCASTER"
    }
    Fallback "Legacy Shaders/Diffuse"
}
