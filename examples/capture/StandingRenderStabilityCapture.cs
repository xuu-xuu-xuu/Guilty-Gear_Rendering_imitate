// New rendering acceptance collector for an isolated copy of the existing project.
// Uses its existing standing playback API; never writes animation, mesh, bind pose,
// bone transforms or controllers. Not a standalone adapter. No scene/asset saves.
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

[InitializeOnLoad]
public static class StandingRenderStabilityCapture
{
    const string SessionKey="StandingRenderStabilityCapture.Pending";
    static string output;
    static UEOriginalActionPlayer player;
    static GGSTRegionalShading regional;
    static GGSTGeometryShadowMaps shadows;
    static Renderer[] subjects, receivers;
    static MaterialPropertyBlock[] blocks, receiverBlocks;
    static Camera camera;
    static RenderTexture rt, previousTarget;
    static Texture2D pixels;
    static Matrix4x4 projection;
    static bool hdr, msaa, naturalDone, finishing;
    static float aspect;
    static readonly List<object> samples=new List<object>();
    static readonly List<string> errors=new List<string>();
    static readonly HashSet<int> naturalCells=new HashSet<int>();
    static double naturalStart;
    static string[] sourceBefore;
    static string scheduleHash, assetHash;
    static int firstIteration=-1;
    static string naturalFailure;
    static bool controlledActive;
    static int controlledTick, controlledPhase, lastControlledUnityFrame=-1;
    static string preparedKind;
    static int preparedDebug;
    static Schedule schedule;
    static Matrix4x4 closeProjection;

    static StandingRenderStabilityCapture()
    {EditorApplication.playModeStateChanged+=PlayState;EditorApplication.update+=EditorUpdate;}
    static string Hash(byte[] b)
    {using(var sha=SHA256.Create())return BitConverter.ToString(sha.ComputeHash(b)).Replace("-","").ToLowerInvariant();}
    static float[] Flat(Matrix4x4 m)
    {return Enumerable.Range(0,16).Select(i=>m[i/4,i%4]).ToArray();}
    static void Write(string file,object value)
    {File.WriteAllText(Path.Combine(output,file),JsonConvert.SerializeObject(value,Formatting.Indented));}
    static MaterialPropertyBlock Block(Renderer r)
    {var b=new MaterialPropertyBlock();r.GetPropertyBlock(b);return b;}
    static void Require(bool b,string message){if(!b)throw new Exception(message);}
    static void Log(string message,string stack,LogType type)
    {if(type==LogType.Error||type==LogType.Exception||type==LogType.Assert)errors.Add(message);}
    static void Resolve()
    {
        player=UnityEngine.Object.FindObjectOfType<UEOriginalActionPlayer>();
        Require(player&&player.nativeRendering,"Existing player/render bridge required");
        Require(!player.runValidationSuite&&!player.captureValidation&&player.loopStanding&&!player.followCamera&&!player.showTestControls&&player.standingStartFrame==0,"Require saved standing-only production defaults");
        Require(!player.nativeRendering.captureNativeFrames,"Unrelated native capture must be off");
        regional=player.GetComponent<GGSTRegionalShading>();shadows=player.GetComponent<GGSTGeometryShadowMaps>();
        Require(regional&&shadows&&!shadows.suspendMaps&&shadows.drawStageCasters&&shadows.drawHairCasters,"Final regional/shadow paths required");
        var b=player.nativeRendering;
        subjects=new[]{b.originalBody,b.standingHead,b.originalFace,b.originalHair}.Where(r=>r).Distinct().Cast<Renderer>().ToArray();
        receivers=UnityEngine.Object.FindObjectsOfType<Renderer>().Where(r=>r.enabled&&r.gameObject.activeInHierarchy&&r.sharedMaterials.Any(m=>m&&m.shader.name=="GGST/StageShadowReceiver")).OrderBy(r=>r.name).ToArray();
        Require(receivers.Length==2,"Two stage receivers required");
        camera=Camera.main;Require(camera,"Main camera required");
        scheduleHash=Hash(player.standingSchedule.bytes);assetHash=Hash(player.standingAnimation.bytes);
    }
    static void SetupCamera()
    {
        previousTarget=camera.targetTexture;hdr=camera.allowHDR;msaa=camera.allowMSAA;aspect=camera.aspect;
        camera.allowHDR=false;camera.allowMSAA=false;camera.aspect=16f/9;
        rt=RenderTexture.GetTemporary(1600,900,24,RenderTextureFormat.ARGB32,RenderTextureReadWrite.Default,1);
        camera.targetTexture=rt;camera.ResetProjectionMatrix();projection=camera.projectionMatrix;
        pixels=new Texture2D(1600,900,TextureFormat.RGB24,false);
    }
    static void RestoreCamera()
    {
        if(camera){camera.targetTexture=previousTarget;camera.allowHDR=hdr;camera.allowMSAA=msaa;camera.aspect=aspect;camera.ResetProjectionMatrix();}
        if(pixels)UnityEngine.Object.DestroyImmediate(pixels);
        if(rt)RenderTexture.ReleaseTemporary(rt);
    }
    static void RefreshUniforms()
    {
        regional.Apply();
        foreach(var p in UnityEngine.Object.FindObjectsOfType<BridgetImitateProfile>())p.SendMessage("LateUpdate");
    }
    static void SaveBlocks(){blocks=subjects.Select(Block).ToArray();receiverBlocks=receivers.Select(Block).ToArray();}
    static void RestoreBlocks()
    {
        for(int i=0;i<subjects.Length;i++)subjects[i].SetPropertyBlock(blocks[i]);
        for(int i=0;i<receivers.Length;i++)receivers[i].SetPropertyBlock(receiverBlocks[i]);
    }
    static void DebugMode(int n)
    {foreach(var r in subjects){var b=Block(r);b.SetFloat("_DebugMode",n);r.SetPropertyBlock(b);}}
    static string ReadImage()
    {
        var old=RenderTexture.active;
        try{RenderTexture.active=rt;pixels.ReadPixels(new Rect(0,0,1600,900),0,0);pixels.Apply();
            byte[] data=pixels.EncodeToPNG();string h=Hash(data);string path=Path.Combine(output,"objects",h+".png");
            if(!File.Exists(path))File.WriteAllBytes(path,data);return h;
        }finally{RenderTexture.active=old;}
    }
    static object Inputs()
    {
        return subjects.Select(r=>{var b=Block(r);return new{r.name,r.enabled,r.forceRenderingOff,active=r.gameObject.activeInHierarchy,
            regional=b.GetFloat("_RegionalEnabled"),head=b.GetFloat("_RegionalHead"),frameValid=b.GetFloat("_FaceFrameValid"),
            faceOrigin=b.GetVector("_FaceOriginWS").ToString("R"),faceRight=b.GetVector("_FaceRightWS").ToString("R"),
            eyeOverride=b.HasFloat("_EyeRefineEnabled"),eye=b.GetFloat("_EyeRefineEnabled"),debug=b.GetFloat("_DebugMode"),
            characterOrigin=b.GetVector("_CharacterOriginWS").ToString("R"),characterHeight=b.GetFloat("_CharacterHeight")};}).ToArray();
    }
    static string PoseHash()
    {
        // Only a hash is exported; no bone arrays/animation/resource data distributed.
        var values=player.characterRoot.GetComponentsInChildren<Transform>(true).OrderBy(t=>t.GetInstanceID()).Select(t=>new{
            id=t.GetInstanceID(),p=t.localPosition.ToString("R"),q=t.localRotation.ToString("R"),s=t.localScale.ToString("R")});
        return Hash(Encoding.UTF8.GetBytes(JsonConvert.SerializeObject(values)));
    }
    static object Record(string kind,string image,int debug)
    {
        var b=player.nativeRendering;
        Require(player.currentAction=="stand"&&b.currentAction=="stand","Only standing may be rendered");
        Require(b.originalBody.enabled&&b.standingHead.enabled&&!b.originalFace.enabled&&!b.originalHair.enabled,"Standing visibility changed");
        Require(Shader.GetGlobalFloat("_StageShadowEnabled")==1&&Shader.GetGlobalFloat("_HairShadowEnabled")==1,"Shadow map disabled");
        return new{kind,image,debug,unityFrame=Time.frameCount,elapsed=player.standingLoopElapsedSeconds,
            gameTick=player.standingGameTick,cycle=player.loopIteration,tick=player.standingCycleTick,cell=player.standingCell,sourceFrame=player.frame,
            poseHash=PoseHash(),view=Flat(camera.worldToCameraMatrix),projection=Flat(camera.projectionMatrix),inputs=Inputs(),
            stageDraws=shadows.StageDrawCount,hairDraws=shadows.HairDrawCount,stageVP=Flat(shadows.StageVP),hairVP=Flat(shadows.HairVP),
            stageCenter=shadows.StageCenter.ToString("R"),hairCenter=shadows.HairCenter.ToString("R"),
            stageEnabled=Shader.GetGlobalFloat("_StageShadowEnabled"),hairEnabled=Shader.GetGlobalFloat("_HairShadowEnabled"),
            proxyError=b.maximumProxyMatrixError};
    }
    static object EnvironmentInfo()
    {return new{unity=Application.unityVersion,device=SystemInfo.graphicsDeviceName,api=SystemInfo.graphicsDeviceType.ToString(),
        colorSpace=QualitySettings.activeColorSpace.ToString(),width=1600,height=900,hdr=false,cameraMSAA=false,targetMSAA=1,
        qualityMSAA=QualitySettings.antiAliasing,standingAnimationSHA256=assetHash,scheduleSHA256=scheduleHash};}
    public static void Run()
    {
        try{
            output=Environment.GetEnvironmentVariable("GGST_STANDING_OUTPUT");Require(!string.IsNullOrEmpty(output),"GGST_STANDING_OUTPUT required");
            string root=Directory.GetParent(Application.dataPath).FullName;
            Require(Application.isBatchMode&&File.ReadAllText(Path.Combine(root,"EvidenceCaptureIsolation.marker"))=="rendering-only-evidence-20261021","Marked isolated batch project required");
            Directory.CreateDirectory(Path.Combine(output,"objects"));
            Require(!EditorApplication.isPlayingOrWillChangePlaymode,"Start in Edit mode");
            Application.logMessageReceived+=Log;UEOriginalEditPreview.Suspend();
            EditorSceneManager.OpenScene("Assets/Scenes/Bridget_ReferenceMatch.unity");UEOriginalEditPreview.Suspend();
            Resolve();
            SessionState.SetBool(SessionKey,true);EditorApplication.isPlaying=true;
        }catch(Exception e){Fail(e);}
    }
    public static void ControlledStep()
    {
        if(!controlledActive)return;
        try{
            Require(Time.frameCount>lastControlledUnityFrame,"Each controlled tick requires a new Unity frame");
            lastControlledUnityFrame=Time.frameCount;
            if(controlledTick==0&&controlledPhase==0){
                player.enabled=false;
                sourceBefore=player.StandingSourceHashes();
                schedule=JsonConvert.DeserializeObject<Schedule>(player.standingSchedule.text);
                Require(schedule.tickRate==60&&schedule.totalTicks==63&&schedule.rows.Length==13,"Unexpected standing timing");
                var close=Matrix4x4.identity;close.m00=3.5f;close.m11=3.5f;close.m03=-(0.517f*2-1)*3.5f;close.m13=-(0.83f*2-1)*3.5f;
                closeProjection=close*projection;
            }
            if(controlledTick<189){
                int n=controlledTick;
                if(controlledPhase==0){player.SampleStandingLoopAt((n+0.25)/schedule.tickRate);RefreshUniforms();SaveBlocks();}
                RestoreBlocks();camera.projectionMatrix=projection;
                string[] kinds={"full-first","full-settled","specular","outline-off","stage-receivers-off","eye-final","eye-regions","eye-contribution"};
                preparedKind=kinds[controlledPhase];preparedDebug=controlledPhase==2?13:controlledPhase==6?33:controlledPhase==7?34:0;
                if(controlledPhase==3)foreach(var r in subjects){var b=Block(r);b.SetFloat("_OutlineWidth",0);r.SetPropertyBlock(b);}
                if(controlledPhase==4)foreach(var r in receivers){var b=Block(r);b.SetFloat("_GeometryShadowFloor",1);r.SetPropertyBlock(b);}
                if(controlledPhase>=5)camera.projectionMatrix=closeProjection;
                DebugMode(preparedDebug);
                return; // The normal Unity main camera renders AFTER all LateUpdate calls.
            }
            bool unchanged=sourceBefore.SequenceEqual(player.StandingSourceHashes());Require(unchanged,"Standing source arrays changed");
            var shaderErrors=subjects.SelectMany(r=>r.sharedMaterials).Where(m=>m).Select(m=>m.shader).Distinct().SelectMany(s=>ShaderUtil.GetShaderMessages(s)).Where(m=>m.severity.ToString()=="Error").Select(m=>m.message).ToArray();
            Write("controlled.json",new{schema="standing-render-stability-v3",completed=true,playMode=true,environment=EnvironmentInfo(),
                method="Existing SampleStandingLoopAt at (tick+0.25)/60, held across first and next real Unity main-camera frame; production player temporarily disabled; uniforms refreshed; all images read in normal camera onPostRender, no Camera.Render; three 63-tick periods and 13 cell-start diagnostics",schedule,
                sourceArraysUnchanged=unchanged,sourceHashesBefore=sourceBefore,sourceHashesAfter=player.StandingSourceHashes(),shaderErrors,errors,samples});
            RestoreBlocks();camera.projectionMatrix=projection;samples.Clear();controlledActive=false;
            player.enabled=true;player.RestartAction("stand");camera.enabled=true;
            sourceBefore=player.StandingSourceHashes();naturalStart=EditorApplication.timeSinceStartup;

        }catch(Exception e){Fail(e);}
    }
    [Serializable] sealed class Schedule{public int tickRate,totalTicks;public Cell[] rows;}
    [Serializable] sealed class Cell{public int cell,startTick,endTickExclusive,holdTicks,sourceSampleFrame;public string sprite;}
    static void PlayState(PlayModeStateChange state)
    {
        if(!SessionState.GetBool(SessionKey,false))return;
        try{
            output=Environment.GetEnvironmentVariable("GGST_STANDING_OUTPUT");
            if(state==PlayModeStateChange.EnteredPlayMode){
                Application.logMessageReceived+=Log;Resolve();Require(UEOriginalEditPreview.ActivePreviewCount==0,"Edit preview leaked into Play");
                sourceBefore=player.StandingSourceHashes();SetupCamera();controlledActive=true;
                Camera.onPostRender+=NaturalFrame;
                var pump=new GameObject("StandingRenderAcceptance_Transient");pump.hideFlags=HideFlags.HideAndDontSave;
                pump.AddComponent<StandingRenderCapturePump>();
            }else if(state==PlayModeStateChange.EnteredEditMode){
                SessionState.SetBool(SessionKey,false);EditorApplication.Exit(File.Exists(Path.Combine(output,"natural.json"))?0:2);
            }
        }catch(Exception e){Fail(e);}
    }
    static void NaturalFrame(Camera c)
    {
        if(c!=camera||naturalDone||finishing)return;
        if(controlledActive){
            try{
                if(controlledTick>=189)return;
                samples.Add(Record(preparedKind,ReadImage(),preparedDebug));
                int phases=controlledTick<63&&schedule.rows.Any(r=>r.startTick==controlledTick)?8:2;
                controlledPhase++;
                if(controlledPhase==phases){controlledPhase=0;controlledTick++;}
            }catch(Exception e){Fail(e);}
            return;
        }
        try{
            // Observe normal player LateUpdate and normal main-camera rendering only.
            if(player.standingLoopElapsedSeconds<=0)return;
            if(firstIteration<0)firstIteration=player.loopIteration;
            naturalCells.Add(player.standingCell);
            samples.Add(Record("natural",ReadImage(),0));
            if(player.loopIteration-firstIteration>=8&&naturalCells.Count==13)naturalDone=true;
        }catch(Exception e){naturalFailure=e.ToString();naturalDone=true;}
    }
    static void EditorUpdate()
    {
        if(!SessionState.GetBool(SessionKey,false)||!EditorApplication.isPlaying||finishing||!camera||controlledActive)return;
        if(EditorApplication.timeSinceStartup-naturalStart>30){naturalFailure="30s watchdog: coverage incomplete";naturalDone=true;}
        if(!naturalDone)return;
        finishing=true;
        try{
            Camera.onPostRender-=NaturalFrame;
            bool unchanged=sourceBefore.SequenceEqual(player.StandingSourceHashes());
            Write("natural.json",new{schema="standing-render-natural-v1",completed=naturalFailure==null&&unchanged,playMode=true,
                environment=EnvironmentInfo(),method="Unmodified existing standing LateUpdate; normal camera onPostRender; no manual pose sampling or Camera.Render in this phase",
                firstIteration,lastIteration=player.loopIteration,observedCycleSpan=player.loopIteration-firstIteration,coveredCells=naturalCells.OrderBy(x=>x).ToArray(),
                sourceHashesBefore=sourceBefore,sourceHashesAfter=player.StandingSourceHashes(),sourceArraysUnchanged=unchanged,
                wallSeconds=EditorApplication.timeSinceStartup-naturalStart,error=naturalFailure,errors,samples});
            RestoreCamera();EditorApplication.isPlaying=false;
        }catch(Exception e){Fail(e);}
    }
    static void Fail(Exception e)
    {
        if(!string.IsNullOrEmpty(output)){Directory.CreateDirectory(output);Write("failure.json",new{error=e.ToString()});}
        SessionState.SetBool(SessionKey,false);Debug.LogException(e);EditorApplication.Exit(2);
    }
}

[DefaultExecutionOrder(2000)]
public sealed class StandingRenderCapturePump : MonoBehaviour
{
    void LateUpdate(){StandingRenderStabilityCapture.ControlledStep();}
}
