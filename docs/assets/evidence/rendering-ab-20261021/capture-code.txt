// New evidence-capture tool, not a source-pack file or general rendering adapter.
// Uses the existing saved standing presentation in an isolated project copy.
// No Play, pose sampling, animation, bone, mesh, bind-pose or controller writes.
using System;
using System.IO;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.Security.Cryptography;
using UnityEngine;
using UnityEditor;
using UnityEditor.SceneManagement;
using Newtonsoft.Json;

public static class RenderingEvidenceCapture
{
    static readonly List<object> records = new List<object>();
    static Camera camera;
    static GGSTGeometryShadowMaps shadows;
    static SkinnedMeshRenderer head;
    static Renderer[] subjects;
    static MaterialPropertyBlock[] initialBlocks;
    static Renderer[] receivers;
    static MaterialPropertyBlock[] receiverBlocks;
    static RenderTexture target;
    static Texture2D readback;
    static string output;
    static Matrix4x4 baseProjection;
    static string fixedScene;

    static string Hash(byte[] data)
    { using(var sha=SHA256.Create()) return BitConverter.ToString(sha.ComputeHash(data)).Replace("-","").ToLowerInvariant(); }
    static float[] Flat(Matrix4x4 m)
    { var a=new float[16];for(int r=0;r<4;r++)for(int c=0;c<4;c++)a[r*4+c]=m[r,c];return a; }
    static string ObjectPath(Transform t)
    { return t.parent?ObjectPath(t.parent)+"/"+t.name:t.name; }
    static MaterialPropertyBlock Block(Renderer r)
    {var b=new MaterialPropertyBlock();r.GetPropertyBlock(b);return b;}
    static string Fingerprint()
    {
        var transforms=UnityEngine.Object.FindObjectsOfType<Transform>(true).OrderBy(t=>t.GetInstanceID()).Select(t=>new {
            id=t.GetInstanceID(),parent=t.parent?t.parent.GetInstanceID():0,
            p=new[]{t.localPosition.x,t.localPosition.y,t.localPosition.z},
            q=new[]{t.localRotation.x,t.localRotation.y,t.localRotation.z,t.localRotation.w},
            s=new[]{t.localScale.x,t.localScale.y,t.localScale.z},active=t.gameObject.activeSelf }).ToArray();
        var renderers=UnityEngine.Object.FindObjectsOfType<SkinnedMeshRenderer>(true).OrderBy(r=>r.GetInstanceID()).Select(r=>new {
            id=r.GetInstanceID(),r.enabled,r.forceRenderingOff,
            mesh=r.sharedMesh?r.sharedMesh.GetInstanceID():0,root=r.rootBone?r.rootBone.GetInstanceID():0,
            bones=r.bones.Select(t=>t?t.GetInstanceID():0).ToArray(),materials=r.sharedMaterials.Select(m=>m?m.GetInstanceID():0).ToArray() }).ToArray();
        var lights=UnityEngine.Object.FindObjectsOfType<Light>(true).OrderBy(l=>l.GetInstanceID()).Select(l=>new {
            id=l.GetInstanceID(),l.enabled,l.intensity,color=new[]{l.color.r,l.color.g,l.color.b,l.color.a},shadows=l.shadows.ToString(),l.shadowBias,l.shadowNormalBias }).ToArray();
        return Hash(Encoding.UTF8.GetBytes(JsonConvert.SerializeObject(new{transforms,renderers,lights})));
    }
    static object DepthStats(RenderTexture rt)
    {
        if(!rt||!rt.IsCreated())throw new Exception("Missing depth render target");
        var old=RenderTexture.active;
        var tex=new Texture2D(rt.width,rt.height,TextureFormat.RFloat,false,true);
        try {
            RenderTexture.active=rt;tex.ReadPixels(new Rect(0,0,rt.width,rt.height),0,0);tex.Apply();
            var raw=tex.GetRawTextureData();
            int occupied=0;float min=1,max=0;
            for(int i=0;i<raw.Length;i+=4){float v=BitConverter.ToSingle(raw,i);if(float.IsNaN(v)||float.IsInfinity(v))throw new Exception("Invalid depth");min=Mathf.Min(min,v);max=Mathf.Max(max,v);if(v<0.99999f)occupied++;}
            return new{width=rt.width,height=rt.height,sha256=Hash(raw),occupiedPixels=occupied,min,max};
        } finally {RenderTexture.active=old;UnityEngine.Object.DestroyImmediate(tex);}
    }
    static object Inputs()
    {
        return subjects.Select(r=>{var b=Block(r);return new {
            renderer=ObjectPath(r.transform),r.enabled,r.forceRenderingOff,active=r.gameObject.activeInHierarchy,
            regionalEnabled=b.GetFloat("_RegionalEnabled"),regionalHead=b.GetFloat("_RegionalHead"),faceFrameValid=b.GetFloat("_FaceFrameValid"),
            eyeOverride=b.HasFloat("_EyeRefineEnabled"),eyeValue=b.GetFloat("_EyeRefineEnabled"),debugOverride=b.HasFloat("_DebugMode"),debug=b.GetFloat("_DebugMode"),
            materials=r.sharedMaterials.Select(m=>new{name=m.name,shader=m.shader.name,eye=m.HasProperty("_EyeRefineEnabled")?m.GetFloat("_EyeRefineEnabled"):-1,
                clean=m.HasProperty("_CleanShadeEnabled")?m.GetFloat("_CleanShadeEnabled"):-1,hairStrength=m.HasProperty("_HairFaceShadowStrength")?m.GetFloat("_HairFaceShadowStrength"):-1}).ToArray() };}).ToArray();
    }
    static void RestoreBlocks()
    {
        if(initialBlocks!=null)for(int i=0;i<subjects.Length;i++)subjects[i].SetPropertyBlock(initialBlocks[i]);
        if(receiverBlocks!=null)for(int i=0;i<receivers.Length;i++)receivers[i].SetPropertyBlock(receiverBlocks[i]);
    }
    static void SetDebug(int mode)
    {for(int i=0;i<subjects.Length;i++){var b=Block(subjects[i]);b.SetFloat("_DebugMode",mode);subjects[i].SetPropertyBlock(b);}}
    static void Capture(string name,string variable,object value,int debug)
    {
        if(Fingerprint()!=fixedScene)throw new Exception("Pose, renderer or lighting changed before "+name);
        SetDebug(debug);
        camera.Render();camera.Render();camera.Render();
        if(shadows.StageDrawCount<=0 && shadows.drawStageCasters)throw new Exception("No stage draws");
        if(Shader.GetGlobalFloat("_StageShadowEnabled")<0.5f && shadows.drawStageCasters)throw new Exception("Stage map not published");
        RenderTexture.active=target;readback.ReadPixels(new Rect(0,0,target.width,target.height),0,0);readback.Apply();
        var bytes=readback.EncodeToPNG();File.WriteAllBytes(Path.Combine(output,name+".png"),bytes);
        if(Fingerprint()!=fixedScene)throw new Exception("Pose, renderer or lighting changed after "+name);
        records.Add(new{name,variable,value,debug,width=target.width,height=target.height,sha256=Hash(bytes),
            projection=Flat(camera.projectionMatrix),view=Flat(camera.worldToCameraMatrix),sceneFingerprint=fixedScene,
            inputBlocks=Inputs(),stageCasters=shadows.drawStageCasters,hairCasters=shadows.drawHairCasters,
            stageEnabled=Shader.GetGlobalFloat("_StageShadowEnabled"),hairEnabled=Shader.GetGlobalFloat("_HairShadowEnabled"),
            stageDrawCount=shadows.StageDrawCount,hairDrawCount=shadows.HairDrawCount,
            stageDepth=DepthStats(shadows.StageDepthTexture),hairDepth=DepthStats(shadows.HairDepthTexture)});
    }

    public static void Run()
    {
        Camera cam=null;RenderTexture previousTarget=null,previousActive=RenderTexture.active;
        bool oldAA=false,oldHDR=false,oldHair=true,oldStage=true;float oldAspect=0;int oldMode=0;float[] initialProjection=null;
        try {
            var root=Directory.GetParent(Application.dataPath).FullName;
            var marker=Path.Combine(root,"EvidenceCaptureIsolation.marker");
            if(!Application.isBatchMode||!File.Exists(marker)||File.ReadAllText(marker)!="rendering-only-evidence-20261021")throw new Exception("Requires marked isolated batch project");
            if(EditorApplication.isPlayingOrWillChangePlaymode)throw new Exception("Edit-mode saved pose only");
            output=Environment.GetEnvironmentVariable("GGST_EVIDENCE_OUTPUT");
            if(string.IsNullOrEmpty(output))throw new Exception("GGST_EVIDENCE_OUTPUT required");
            Directory.CreateDirectory(output);
            UEOriginalEditPreview.Suspend();
            EditorSceneManager.OpenScene("Assets/Scenes/Bridget_ReferenceMatch.unity");
            UEOriginalEditPreview.Suspend();
            var player=UnityEngine.Object.FindObjectOfType<UEOriginalActionPlayer>();
            if(!player||!player.nativeRendering)throw new Exception("Saved rendering references missing");
            var bridge=player.nativeRendering;
            head=bridge.standingHead;
            if(!head||!head.enabled||!head.gameObject.activeInHierarchy||head.forceRenderingOff)throw new Exception("Saved standing head not visible");
            subjects=new[]{bridge.originalBody,bridge.standingHead,bridge.originalFace,bridge.originalHair}.Where(r=>r).Distinct().Cast<Renderer>().ToArray();
            var regional=player.GetComponent<GGSTRegionalShading>();if(!regional)throw new Exception("Regional component missing");regional.Apply();
            foreach(var profile in UnityEngine.Object.FindObjectsOfType<BridgetImitateProfile>())profile.SendMessage("LateUpdate");
            if(Block(head).GetFloat("_RegionalHead")!=1||Block(head).GetFloat("_RegionalEnabled")!=1)throw new Exception("Head MPB not resolved");
            initialBlocks=subjects.Select(Block).ToArray();
            receivers=UnityEngine.Object.FindObjectsOfType<Renderer>().Where(r=>r.enabled&&r.gameObject.activeInHierarchy&&r.sharedMaterials.Any(m=>m&&m.shader.name=="GGST/StageShadowReceiver")).OrderBy(r=>r.name).ToArray();
            if(receivers.Length!=2)throw new Exception("Expected two explicit floor/wall receivers, got "+receivers.Length);
            receiverBlocks=receivers.Select(Block).ToArray();
            shadows=player.GetComponent<GGSTGeometryShadowMaps>();if(!shadows||shadows.suspendMaps)throw new Exception("Shadow maps unavailable");
            oldHair=shadows.drawHairCasters;oldStage=shadows.drawStageCasters;
            if(!oldHair||!oldStage)throw new Exception("Require saved final caster flags");
            camera=cam=Camera.main;if(!cam)throw new Exception("Missing main camera");
            oldMode=new SerializedObject(cam).FindProperty("m_projectionMatrixMode").intValue;
            if(oldMode!=1)throw new Exception("Require saved implicit camera projection");
            previousTarget=cam.targetTexture;oldAA=cam.allowMSAA;oldHDR=cam.allowHDR;oldAspect=cam.aspect;initialProjection=Flat(cam.projectionMatrix);
            cam.aspect=16f/9f;cam.allowMSAA=false;cam.allowHDR=false;
            target=RenderTexture.GetTemporary(1600,900,24,RenderTextureFormat.ARGB32,RenderTextureReadWrite.Default,1);
            cam.targetTexture=target;cam.ResetProjectionMatrix();baseProjection=cam.projectionMatrix;
            readback=new Texture2D(1600,900,TextureFormat.RGB24,false);
            fixedScene=Fingerprint();
            var baselineInputs=Inputs();
            foreach(var renderer in receivers){
                RestoreBlocks();cam.projectionMatrix=baseProjection;
                var b=Block(renderer);b.SetFloat("_GeometryShadowFloor",1);renderer.SetPropertyBlock(b);
                string key=renderer.name.Contains("Floor")?"floor":"wall";
                Capture(key+"_receiver_off","_GeometryShadowFloor@"+renderer.name,1,0);
                RestoreBlocks();
                float saved=renderer.sharedMaterials.First(m=>m.shader.name=="GGST/StageShadowReceiver").GetFloat("_GeometryShadowFloor");
                Capture(key+"_receiver_on","_GeometryShadowFloor@"+renderer.name,saved,0);
                Capture(key+"_receiver_on_repeat","_GeometryShadowFloor@"+renderer.name,saved,0);
            }
            RestoreBlocks();cam.projectionMatrix=baseProjection;
            shadows.drawStageCasters=false;Capture("stage_casters_off","drawStageCasters",false,0);
            shadows.drawStageCasters=true;Capture("stage_casters_on","drawStageCasters",true,0);
            var crop=Matrix4x4.identity;crop.m00=3.5f;crop.m11=3.5f;crop.m03=-(0.517f*2-1)*3.5f;crop.m13=-(0.83f*2-1)*3.5f;
            cam.projectionMatrix=crop*baseProjection;
            foreach(bool on in new[]{false,true})foreach(int mode in new[]{0,13,30,33,34}){
                RestoreBlocks();var b=Block(head);b.SetFloat("_EyeRefineEnabled",on?1:0);head.SetPropertyBlock(b);
                Capture("eye_"+(on?"on":"off")+"_"+mode,"_EyeRefineEnabled@"+head.name,on?1:0,mode);
            }
            Capture("eye_on_0_repeat","_EyeRefineEnabled@"+head.name,1,0);
            foreach(bool on in new[]{false,true})foreach(int mode in new[]{0,32}){
                RestoreBlocks();shadows.drawHairCasters=on;Capture("hair_casters_"+(on?"on":"off")+"_"+mode,"drawHairCasters",on,mode);
            }
            RestoreBlocks();shadows.drawHairCasters=oldHair;shadows.drawStageCasters=oldStage;
            if(Fingerprint()!=fixedScene)throw new Exception("Final scene-state fingerprint changed");
            File.WriteAllText(Path.Combine(output,"capture.json"),JsonConvert.SerializeObject(new {
                schema="rendering-evidence-capture-v1",completed=true,unityVersion=Application.unityVersion,
                graphicsDevice=SystemInfo.graphicsDeviceName,graphicsApi=SystemInfo.graphicsDeviceType.ToString(),
                colorSpace=QualitySettings.activeColorSpace.ToString(),qualityMSAA=QualitySettings.antiAliasing,
                allowHDR=false,allowMSAA=false,targetMSAA=1,width=1600,height=900,playMode=false,
                scene="Assets/Scenes/Bridget_ReferenceMatch.unity",pose="saved standing presentation; no ShowFrame or Play invoked",
                savedPlayerFrame=player.frame,savedEditPreviewFrame=player.editPreviewFrame,savedBridgeFrame=bridge.currentFrame,
                initialProjectionMode=oldMode,baseProjection=Flat(baseProjection),closeupCrop=Flat(crop),baselineInputs,
                receivers=receivers.Select(r=>new{name=r.name,geometryShadowFloor=r.sharedMaterials.First(m=>m.shader.name=="GGST/StageShadowReceiver").GetFloat("_GeometryShadowFloor")}).ToArray(),
                shaderErrors=subjects.SelectMany(r=>r.sharedMaterials).Where(m=>m).Select(m=>m.shader).Distinct().SelectMany(s=>ShaderUtil.GetShaderMessages(s)).Where(m=>m.severity.ToString()=="Error").Select(m=>m.message).ToArray(),records
            },Formatting.Indented));
            Debug.Log("Evidence capture completed: "+records.Count+" real Unity camera renders");
        } catch(Exception e) {
            if(!string.IsNullOrEmpty(output))File.WriteAllText(Path.Combine(output,"failure.txt"),e.ToString());
            Debug.LogException(e);EditorApplication.Exit(2);return;
        } finally {
            if(subjects!=null&&initialBlocks!=null)RestoreBlocks();
            if(shadows){shadows.drawHairCasters=oldHair;shadows.drawStageCasters=oldStage;}
            if(cam){cam.targetTexture=previousTarget;cam.allowHDR=oldHDR;cam.allowMSAA=oldAA;cam.aspect=oldAspect;cam.ResetProjectionMatrix();}
            RenderTexture.active=previousActive;
            if(readback)UnityEngine.Object.DestroyImmediate(readback);
            if(target)RenderTexture.ReleaseTemporary(target);
            if(cam&&initialProjection!=null&&!string.IsNullOrEmpty(output)){
                var finalProjection=Flat(cam.projectionMatrix);
                File.WriteAllText(Path.Combine(output,"restoration.json"),JsonConvert.SerializeObject(new{
                    sceneFingerprintUnchanged=Fingerprint()==fixedScene,
                    projectionModeRestored=new SerializedObject(cam).FindProperty("m_projectionMatrixMode").intValue==oldMode,
                    projectionMaxDifference=initialProjection.Zip(finalProjection,(a,b)=>Mathf.Abs(a-b)).Max(),
                    targetRestored=cam.targetTexture==previousTarget,aaRestored=cam.allowMSAA==oldAA,hdrRestored=cam.allowHDR==oldHDR,
                    casterFlagsRestored=shadows&&shadows.drawHairCasters==oldHair&&shadows.drawStageCasters==oldStage,
                    restoredInputs=Inputs()
                },Formatting.Indented));
            }
        }
        EditorApplication.Exit(0);
    }
}
