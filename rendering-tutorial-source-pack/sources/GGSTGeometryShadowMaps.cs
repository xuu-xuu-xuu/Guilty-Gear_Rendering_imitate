using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering;

// Offscreen rendering only. Existing actual native SMRs supply the current
// skinned vertices; no copied/baked mesh, Transform, bone or MPB writes.
[ExecuteAlways, DisallowMultipleComponent, DefaultExecutionOrder(1400)]
public sealed class GGSTGeometryShadowMaps : MonoBehaviour
{
    public UEOriginalActionPlayer p;
    public Light lightSource;
    public Texture2D hairMask;
    public Shader depthShader;
    public Camera mainCamera;
    public bool suspendMaps;
    public bool drawHairCasters=true,drawStageCasters=true;
    [Min(0.05f)] public float hairRadius=0.28f;
    [Min(0.1f)] public float hairRange=1.2f;
    public float hairWorldUpOffset=0.08f;
    [Min(0.5f)] public float stageRadius=2f;
    [Min(1f)] public float stageRange=8f;

    public RenderTexture HairDepthTexture { get { return hairDepth; } }
    public RenderTexture StageDepthTexture { get { return stageDepth; } }
    public int RenderCount { get; private set; }
    public int RecordCount { get; private set; }
    public int LastRenderedFrame { get; private set; }=-1;
    public int LastRecordedFrame { get; private set; }=-1;
    public int HairDrawCount { get; private set; }
    public int StageDrawCount { get; private set; }
    public string ActiveHairSource { get; private set; }="";
    public string ActiveStageSources { get; private set; }="";
    public string LastStatus { get; private set; }="Disabled";
    public Matrix4x4 HairVP { get; private set; }
    public Matrix4x4 StageVP { get; private set; }
    public Vector4 HairOriginRange { get; private set; }
    public Vector4 StageOriginRange { get; private set; }
    public Vector3 LightForward { get; private set; }
    public Vector3 HairCenter { get; private set; }
    public Vector3 StageCenter { get; private set; }

    const int HairResolution=1024,StageResolution=2048;
    const string ToonShader="GGST/BridgetToonStudy";
    const CameraEvent Event=CameraEvent.BeforeForwardOpaque;
    RenderTexture hairDepth,stageDepth;
    Material depthMaterial;
    CommandBuffer commands;
    Camera attachedCamera;
    MaterialPropertyBlock readBlock;
    UEOriginalPersistentPresentation presentation;
    Transform standingPelvis,cinematicPelvis;
    bool submitted;
    int submittedFrame;
    readonly List<SkinnedMeshRenderer> stageSources=new List<SkinnedMeshRenderer>(4);
    readonly List<string> stageNames=new List<string>(4);
    static readonly int HairEnabledID=Shader.PropertyToID("_HairShadowEnabled");
    static readonly int StageEnabledID=Shader.PropertyToID("_StageShadowEnabled");
    static readonly int CasterOriginID=Shader.PropertyToID("_GGSTShadowCasterOriginRange");
    static readonly int CasterForwardID=Shader.PropertyToID("_GGSTShadowCasterForward");
    static readonly int CasterHairID=Shader.PropertyToID("_GGSTShadowCasterHairOnly");
    static readonly int CasterMaskID=Shader.PropertyToID("_GGSTShadowCasterHairMask");
    static readonly int CasterMirrorID=Shader.PropertyToID("_GGSTShadowCasterUseMirror");
    static readonly int CasterSTID=Shader.PropertyToID("_GGSTShadowCasterTexST");

    void OnEnable()
    {
        Camera.onPreCull+=RenderMaps;
        Camera.onPostRender+=Rendered;
        ResolveReferences();
        DisableGlobals();
    }
    void OnDisable()
    {
        Camera.onPreCull-=RenderMaps;
        Camera.onPostRender-=Rendered;
        Release();
        LastStatus="Disabled";
    }
    void OnDestroy(){Release();}

    void ResolveReferences()
    {
        if(!p)p=GetComponent<UEOriginalActionPlayer>();
        if(!p||!p.gameObject.scene.IsValid())return;
        if(!presentation)presentation=p.GetComponent<UEOriginalPersistentPresentation>();
        if(!standingPelvis||!cinematicPelvis)
        {
            if(presentation&&presentation.groups!=null)
                foreach(var group in presentation.groups)
                {
                    if(group==null||group.bones==null)continue;
                    if(group.label!="stand_body"&&group.label!="900cs_body")continue;
                    foreach(var bone in group.bones)
                        if(bone&&bone.name.EndsWith("__G_pelvis",StringComparison.Ordinal))
                        {if(group.label=="stand_body")standingPelvis=bone;else cinematicPelvis=bone;break;}
                }
        }
        // Restrict fallback discovery to this player's real scene, never preview
        // clones/resources or an unrelated open Unity scene.
        if(!mainCamera||!lightSource)
            foreach(var root in p.gameObject.scene.GetRootGameObjects())
            {
                if(!mainCamera)
                    foreach(var camera in root.GetComponentsInChildren<Camera>(true))
                        if(camera.isActiveAndEnabled&&camera.CompareTag("MainCamera")) { mainCamera=camera;break; }
                if(!lightSource)
                    foreach(var light in root.GetComponentsInChildren<Light>(true))
                        if(light.isActiveAndEnabled&&light.type==LightType.Directional) { lightSource=light;break; }
            }
        if(!depthShader)depthShader=Shader.Find("GGST/GeometryShadowDepth");
        if(readBlock==null)readBlock=new MaterialPropertyBlock();
    }

    bool Ready()
    {
        if(!p||!p.nativeRendering||!p.gameObject.scene.IsValid()||!mainCamera||
           mainCamera.gameObject.scene!=p.gameObject.scene||!lightSource||!hairMask||!depthShader)
        {LastStatus="Missing explicit scene/player/light/camera/mask/depth shader";return false;}
        if(!SystemInfo.SupportsRenderTextureFormat(RenderTextureFormat.RFloat))
        {LastStatus="RFloat render textures are unsupported";return false;}
        if(!depthShader.isSupported){LastStatus="Depth shader unsupported";return false;}
        if(depthMaterial&&depthMaterial.shader!=depthShader)
        {DestroyResource(depthMaterial);depthMaterial=null;}
        if(!depthMaterial)depthMaterial=new Material(depthShader){name="GGST geometry shadow depth (hidden)",hideFlags=HideFlags.HideAndDontSave};
        if(!hairDepth)hairDepth=CreateDepth("GGST Hair Shadow Depth",HairResolution);
        if(!stageDepth)stageDepth=CreateDepth("GGST Stage Shadow Depth",StageResolution);
        if(!hairDepth.IsCreated())hairDepth.Create();
        if(!stageDepth.IsCreated())stageDepth.Create();
        if(commands==null)commands=new CommandBuffer{name="GGST native geometry shadow maps"};
        if(attachedCamera!=mainCamera)
        {
            if(attachedCamera)attachedCamera.RemoveCommandBuffer(Event,commands);
            attachedCamera=mainCamera;attachedCamera.AddCommandBuffer(Event,commands);
        }
        return true;
    }

    static RenderTexture CreateDepth(string label,int resolution)
    {
        var texture=new RenderTexture(resolution,resolution,24,RenderTextureFormat.RFloat,RenderTextureReadWrite.Linear)
        {
            name=label,hideFlags=HideFlags.HideAndDontSave,filterMode=FilterMode.Point,
            wrapMode=TextureWrapMode.Clamp,useMipMap=false,autoGenerateMips=false,
            antiAliasing=1
        };
        texture.Create();return texture;
    }
    bool Visible(SkinnedMeshRenderer renderer)
    {
        return renderer&&renderer.enabled&&renderer.gameObject.activeInHierarchy&&!renderer.forceRenderingOff&&
               renderer.sharedMesh&&renderer.gameObject.scene==p.gameObject.scene;
    }
    void AddStage(SkinnedMeshRenderer renderer)
    {
        if(!Visible(renderer)||stageSources.Contains(renderer))return;
        stageSources.Add(renderer);stageNames.Add(renderer.name);
    }
    Vector3 ReadFaceOrigin(SkinnedMeshRenderer head)
    {
        if(head)
        {
            head.GetPropertyBlock(readBlock);
            if(readBlock.GetFloat("_FaceFrameValid")>0.5f)
            {Vector4 value=readBlock.GetVector("_FaceOriginWS");return new Vector3(value.x,value.y,value.z);}
        }
        var pelvis=Visible(p.nativeRendering.standingHead)?standingPelvis:cinematicPelvis;
        return pelvis?pelvis.position+Vector3.up*0.6f:p.transform.position+Vector3.up*1.5f;
    }
    static Quaternion LightRotation(Vector3 forward)
    {
        var up=Mathf.Abs(Vector3.Dot(forward,Vector3.up))>0.98f?Vector3.forward:Vector3.up;
        return Quaternion.LookRotation(forward,up);
    }
    static Vector3 SnapCenter(Vector3 center,Quaternion rotation,float radius,int resolution)
    {
        Vector3 local=Quaternion.Inverse(rotation)*center;
        float texel=2f*radius/resolution;
        local.x=Mathf.Round(local.x/texel)*texel;
        local.y=Mathf.Round(local.y/texel)*texel;
        return rotation*local;
    }
    static void Projection(Vector3 center,Vector3 forward,Quaternion rotation,float radius,float range,
                           out Matrix4x4 view,out Matrix4x4 gpuProjection,out Matrix4x4 rawProjection,out Vector4 originRange)
    {
        const float near=0.01f;
        Vector3 origin=center-forward*(range*0.5f);
        Vector3 eye=origin-forward*near;
        view=Matrix4x4.Scale(new Vector3(1,1,-1))*Matrix4x4.TRS(eye,rotation,Vector3.one).inverse;
        rawProjection=Matrix4x4.Ortho(-radius,radius,-radius,radius,near,range+near);
        // CommandBuffer renders this manually supplied projection without a camera RT flip.
        // Published sampling coordinates must match the actual 2D texture rows.
        gpuProjection=GL.GetGPUProjectionMatrix(rawProjection,false);
        originRange=new Vector4(origin.x,origin.y,origin.z,range);
    }

    // Build in onPreCull, execute after native cull/skinning and before opaque
    // shading. An immediate ExecuteCommandBuffer during pre-cull may see the
    // previous native skinned vertex buffer, so it is deliberately avoided.
    void RenderMaps(Camera camera)
    {
        if(!isActiveAndEnabled)return;
        ResolveReferences();
        if(camera!=mainCamera)return;
        if(commands!=null)commands.Clear();
        submitted=false;HairDrawCount=0;StageDrawCount=0;
        if(suspendMaps||!Ready())
        {DisableGlobals();if(suspendMaps)LastStatus="Suspended (offscreen draws only)";return;}
        var bridge=p.nativeRendering;
        var low=Visible(bridge.standingHead);
        var hair=low?bridge.standingHead:(Visible(bridge.originalHair)?bridge.originalHair:null);
        var face=low?bridge.standingHead:(Visible(bridge.originalFace)?bridge.originalFace:hair);
        Vector3 origin=ReadFaceOrigin(face);
        LightForward=lightSource.transform.forward.normalized;
        Quaternion rotation=LightRotation(LightForward);
        HairCenter=origin+Vector3.up*hairWorldUpOffset;
        Transform pelvis=low?standingPelvis:cinematicPelvis;
        StageCenter=SnapCenter(pelvis?pelvis.position:origin-Vector3.up*0.6f,rotation,Mathf.Max(stageRadius,0.5f),StageResolution);
        Matrix4x4 hv,hp,sv,sp,hraw,sraw;Vector4 ho,so;
        Projection(HairCenter,LightForward,rotation,Mathf.Max(hairRadius,0.05f),Mathf.Max(hairRange,0.1f),out hv,out hp,out hraw,out ho);
        Projection(StageCenter,LightForward,rotation,Mathf.Max(stageRadius,0.5f),Mathf.Max(stageRange,1f),out sv,out sp,out sraw,out so);
        HairVP=hp*hv;StageVP=sp*sv;HairOriginRange=ho;StageOriginRange=so;
        ActiveHairSource=hair?hair.name:"";
        stageSources.Clear();stageNames.Clear();
        AddStage(bridge.originalBody);AddStage(bridge.standingHead);AddStage(bridge.originalFace);AddStage(bridge.originalHair);
        ActiveStageSources=string.Join(" | ",stageNames.ToArray());

        commands.SetGlobalTexture(CasterMaskID,hairMask);
        BeginMap(hairDepth,hv,hraw,ho,true);
        if(drawHairCasters&&hair)HairDrawCount=DrawToonSubmeshes(hair);
        BeginMap(stageDepth,sv,sraw,so,false);
        if(drawStageCasters)foreach(var renderer in stageSources)StageDrawCount+=DrawToonSubmeshes(renderer);
        Publish(commands,"_HairShadow",hairDepth,HairVP,ho,drawHairCasters&&HairDrawCount>0);
        Publish(commands,"_StageShadow",stageDepth,StageVP,so,drawStageCasters&&StageDrawCount>0);
        // Restore the actual main target and camera matrices before regular
        // opaque rendering. Do not leave the light's ortho state active.
        commands.SetRenderTarget(BuiltinRenderTextureType.CameraTarget);
        commands.SetViewport(camera.pixelRect);
        commands.SetViewProjectionMatrices(camera.worldToCameraMatrix,
            camera.projectionMatrix);
        submitted=true;submittedFrame=Time.frameCount;
        RecordCount++;LastRecordedFrame=Time.frameCount;
        LastStatus="Queued before main opaque; native SMRs only";
    }
    void BeginMap(RenderTexture texture,Matrix4x4 view,Matrix4x4 projection,Vector4 originRange,bool hairOnly)
    {
        commands.SetRenderTarget(texture);
        commands.SetViewport(new Rect(0,0,texture.width,texture.height));
        commands.ClearRenderTarget(true,true,Color.white);
        commands.SetViewProjectionMatrices(view,projection);
        commands.SetGlobalVector(CasterOriginID,originRange);
        commands.SetGlobalVector(CasterForwardID,new Vector4(LightForward.x,LightForward.y,LightForward.z,0));
        commands.SetGlobalFloat(CasterHairID,hairOnly?1f:0f);
    }
    int DrawToonSubmeshes(SkinnedMeshRenderer renderer)
    {
        int draws=0;var materials=renderer.sharedMaterials;
        int count=Mathf.Min(materials.Length,renderer.sharedMesh.subMeshCount);
        for(int index=0;index<count;index++)
        {
            var material=materials[index];
            if(!material||!material.shader||material.shader.name!=ToonShader)continue;
            float mirror=material.HasProperty("_UseMirroredUV")?material.GetFloat("_UseMirroredUV"):0f;
            var scale=material.HasProperty("_MainTex")?material.GetTextureScale("_MainTex"):Vector2.one;
            var offset=material.HasProperty("_MainTex")?material.GetTextureOffset("_MainTex"):Vector2.zero;
            commands.SetGlobalFloat(CasterMirrorID,mirror);
            commands.SetGlobalVector(CasterSTID,new Vector4(scale.x,scale.y,offset.x,offset.y));
            commands.DrawRenderer(renderer,depthMaterial,index,0);
            draws++;
        }
        return draws;
    }
    void Publish(CommandBuffer buffer,string prefix,RenderTexture texture,Matrix4x4 vp,Vector4 originRange,bool enabled)
    {
        buffer.SetGlobalTexture(prefix+"Depth",texture);
        buffer.SetGlobalMatrix(prefix+"VP",vp);
        buffer.SetGlobalVector(prefix+"OriginRange",originRange);
        buffer.SetGlobalVector(prefix+"Forward",new Vector4(LightForward.x,LightForward.y,LightForward.z,0));
        buffer.SetGlobalVector(prefix+"Texel",new Vector4(1f/texture.width,1f/texture.height,texture.width,texture.height));
        buffer.SetGlobalFloat(prefix+"Enabled",enabled?1f:0f);
    }
    void Rendered(Camera camera)
    {
        if(camera!=mainCamera||!submitted)return;
        RenderCount++;LastRenderedFrame=submittedFrame;submitted=false;
        LastStatus="Rendered before main opaque";
    }
    static void DisableGlobals()
    {
        Shader.SetGlobalFloat(HairEnabledID,0f);Shader.SetGlobalFloat(StageEnabledID,0f);
    }
    void Release()
    {
        DisableGlobals();submitted=false;
        if(attachedCamera&&commands!=null)attachedCamera.RemoveCommandBuffer(Event,commands);
        attachedCamera=null;
        if(commands!=null){commands.Clear();commands.Release();commands=null;}
        if(hairDepth){hairDepth.Release();DestroyResource(hairDepth);hairDepth=null;}
        if(stageDepth){stageDepth.Release();DestroyResource(stageDepth);stageDepth=null;}
        if(depthMaterial){DestroyResource(depthMaterial);depthMaterial=null;}
        Shader.SetGlobalTexture("_HairShadowDepth",Texture2D.whiteTexture);
        Shader.SetGlobalTexture("_StageShadowDepth",Texture2D.whiteTexture);
    }
    static void DestroyResource(UnityEngine.Object resource)
    {
        if(!resource)return;
        if(Application.isPlaying)UnityEngine.Object.Destroy(resource);else UnityEngine.Object.DestroyImmediate(resource);
    }
}

