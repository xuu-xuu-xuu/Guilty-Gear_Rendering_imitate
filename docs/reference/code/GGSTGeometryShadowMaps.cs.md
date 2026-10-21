# GGSTGeometryShadowMaps.cs

按行查找正文中的函数与Pass。以下保留源码原文，属性拼写与分支顺序以此为准。代码依赖所用渲染管线及[输入连接](../dependencies.md)，不能把文件索引当作独立工程。

| 行 | 代码 |
|---|---|
| <a id="l1"></a>1 | <code>using System;</code> |
| <a id="l2"></a>2 | <code>using System.Collections.Generic;</code> |
| <a id="l3"></a>3 | <code>using UnityEngine;</code> |
| <a id="l4"></a>4 | <code>using UnityEngine.Rendering;</code> |
| <a id="l5"></a>5 | <code></code> |
| <a id="l6"></a>6 | <code>// Offscreen rendering only. Existing actual native SMRs supply the current</code> |
| <a id="l7"></a>7 | <code>// skinned vertices; no copied/baked mesh, Transform, bone or MPB writes.</code> |
| <a id="l8"></a>8 | <code>[ExecuteAlways, DisallowMultipleComponent, DefaultExecutionOrder(1400)]</code> |
| <a id="l9"></a>9 | <code>public sealed class GGSTGeometryShadowMaps : MonoBehaviour</code> |
| <a id="l10"></a>10 | <code>{</code> |
| <a id="l11"></a>11 | <code>    public UEOriginalActionPlayer p;</code> |
| <a id="l12"></a>12 | <code>    public Light lightSource;</code> |
| <a id="l13"></a>13 | <code>    public Texture2D hairMask;</code> |
| <a id="l14"></a>14 | <code>    public Shader depthShader;</code> |
| <a id="l15"></a>15 | <code>    public Camera mainCamera;</code> |
| <a id="l16"></a>16 | <code>    public bool suspendMaps;</code> |
| <a id="l17"></a>17 | <code>    public bool drawHairCasters=true,drawStageCasters=true;</code> |
| <a id="l18"></a>18 | <code>    [Min(0.05f)] public float hairRadius=0.28f;</code> |
| <a id="l19"></a>19 | <code>    [Min(0.1f)] public float hairRange=1.2f;</code> |
| <a id="l20"></a>20 | <code>    public float hairWorldUpOffset=0.08f;</code> |
| <a id="l21"></a>21 | <code>    [Min(0.5f)] public float stageRadius=2f;</code> |
| <a id="l22"></a>22 | <code>    [Min(1f)] public float stageRange=8f;</code> |
| <a id="l23"></a>23 | <code></code> |
| <a id="l24"></a>24 | <code>    public RenderTexture HairDepthTexture { get { return hairDepth; } }</code> |
| <a id="l25"></a>25 | <code>    public RenderTexture StageDepthTexture { get { return stageDepth; } }</code> |
| <a id="l26"></a>26 | <code>    public int RenderCount { get; private set; }</code> |
| <a id="l27"></a>27 | <code>    public int RecordCount { get; private set; }</code> |
| <a id="l28"></a>28 | <code>    public int LastRenderedFrame { get; private set; }=-1;</code> |
| <a id="l29"></a>29 | <code>    public int LastRecordedFrame { get; private set; }=-1;</code> |
| <a id="l30"></a>30 | <code>    public int HairDrawCount { get; private set; }</code> |
| <a id="l31"></a>31 | <code>    public int StageDrawCount { get; private set; }</code> |
| <a id="l32"></a>32 | <code>    public string ActiveHairSource { get; private set; }="";</code> |
| <a id="l33"></a>33 | <code>    public string ActiveStageSources { get; private set; }="";</code> |
| <a id="l34"></a>34 | <code>    public string LastStatus { get; private set; }="Disabled";</code> |
| <a id="l35"></a>35 | <code>    public Matrix4x4 HairVP { get; private set; }</code> |
| <a id="l36"></a>36 | <code>    public Matrix4x4 StageVP { get; private set; }</code> |
| <a id="l37"></a>37 | <code>    public Vector4 HairOriginRange { get; private set; }</code> |
| <a id="l38"></a>38 | <code>    public Vector4 StageOriginRange { get; private set; }</code> |
| <a id="l39"></a>39 | <code>    public Vector3 LightForward { get; private set; }</code> |
| <a id="l40"></a>40 | <code>    public Vector3 HairCenter { get; private set; }</code> |
| <a id="l41"></a>41 | <code>    public Vector3 StageCenter { get; private set; }</code> |
| <a id="l42"></a>42 | <code></code> |
| <a id="l43"></a>43 | <code>    const int HairResolution=1024,StageResolution=2048;</code> |
| <a id="l44"></a>44 | <code>    const string ToonShader="GGST/BridgetToonStudy";</code> |
| <a id="l45"></a>45 | <code>    const CameraEvent Event=CameraEvent.BeforeForwardOpaque;</code> |
| <a id="l46"></a>46 | <code>    RenderTexture hairDepth,stageDepth;</code> |
| <a id="l47"></a>47 | <code>    Material depthMaterial;</code> |
| <a id="l48"></a>48 | <code>    CommandBuffer commands;</code> |
| <a id="l49"></a>49 | <code>    Camera attachedCamera;</code> |
| <a id="l50"></a>50 | <code>    MaterialPropertyBlock readBlock;</code> |
| <a id="l51"></a>51 | <code>    UEOriginalPersistentPresentation presentation;</code> |
| <a id="l52"></a>52 | <code>    Transform standingPelvis,cinematicPelvis;</code> |
| <a id="l53"></a>53 | <code>    bool submitted;</code> |
| <a id="l54"></a>54 | <code>    int submittedFrame;</code> |
| <a id="l55"></a>55 | <code>    readonly List&lt;SkinnedMeshRenderer&gt; stageSources=new List&lt;SkinnedMeshRenderer&gt;(4);</code> |
| <a id="l56"></a>56 | <code>    readonly List&lt;string&gt; stageNames=new List&lt;string&gt;(4);</code> |
| <a id="l57"></a>57 | <code>    static readonly int HairEnabledID=Shader.PropertyToID("_HairShadowEnabled");</code> |
| <a id="l58"></a>58 | <code>    static readonly int StageEnabledID=Shader.PropertyToID("_StageShadowEnabled");</code> |
| <a id="l59"></a>59 | <code>    static readonly int CasterOriginID=Shader.PropertyToID("_GGSTShadowCasterOriginRange");</code> |
| <a id="l60"></a>60 | <code>    static readonly int CasterForwardID=Shader.PropertyToID("_GGSTShadowCasterForward");</code> |
| <a id="l61"></a>61 | <code>    static readonly int CasterHairID=Shader.PropertyToID("_GGSTShadowCasterHairOnly");</code> |
| <a id="l62"></a>62 | <code>    static readonly int CasterMaskID=Shader.PropertyToID("_GGSTShadowCasterHairMask");</code> |
| <a id="l63"></a>63 | <code>    static readonly int CasterMirrorID=Shader.PropertyToID("_GGSTShadowCasterUseMirror");</code> |
| <a id="l64"></a>64 | <code>    static readonly int CasterSTID=Shader.PropertyToID("_GGSTShadowCasterTexST");</code> |
| <a id="l65"></a>65 | <code></code> |
| <a id="l66"></a>66 | <code>    void OnEnable()</code> |
| <a id="l67"></a>67 | <code>    {</code> |
| <a id="l68"></a>68 | <code>        Camera.onPreCull+=RenderMaps;</code> |
| <a id="l69"></a>69 | <code>        Camera.onPostRender+=Rendered;</code> |
| <a id="l70"></a>70 | <code>        ResolveReferences();</code> |
| <a id="l71"></a>71 | <code>        DisableGlobals();</code> |
| <a id="l72"></a>72 | <code>    }</code> |
| <a id="l73"></a>73 | <code>    void OnDisable()</code> |
| <a id="l74"></a>74 | <code>    {</code> |
| <a id="l75"></a>75 | <code>        Camera.onPreCull-=RenderMaps;</code> |
| <a id="l76"></a>76 | <code>        Camera.onPostRender-=Rendered;</code> |
| <a id="l77"></a>77 | <code>        Release();</code> |
| <a id="l78"></a>78 | <code>        LastStatus="Disabled";</code> |
| <a id="l79"></a>79 | <code>    }</code> |
| <a id="l80"></a>80 | <code>    void OnDestroy(){Release();}</code> |
| <a id="l81"></a>81 | <code></code> |
| <a id="l82"></a>82 | <code>    void ResolveReferences()</code> |
| <a id="l83"></a>83 | <code>    {</code> |
| <a id="l84"></a>84 | <code>        if(!p)p=GetComponent&lt;UEOriginalActionPlayer&gt;();</code> |
| <a id="l85"></a>85 | <code>        if(!p&#124;&#124;!p.gameObject.scene.IsValid())return;</code> |
| <a id="l86"></a>86 | <code>        if(!presentation)presentation=p.GetComponent&lt;UEOriginalPersistentPresentation&gt;();</code> |
| <a id="l87"></a>87 | <code>        if(!standingPelvis&#124;&#124;!cinematicPelvis)</code> |
| <a id="l88"></a>88 | <code>        {</code> |
| <a id="l89"></a>89 | <code>            if(presentation&amp;&amp;presentation.groups!=null)</code> |
| <a id="l90"></a>90 | <code>                foreach(var group in presentation.groups)</code> |
| <a id="l91"></a>91 | <code>                {</code> |
| <a id="l92"></a>92 | <code>                    if(group==null&#124;&#124;group.bones==null)continue;</code> |
| <a id="l93"></a>93 | <code>                    if(group.label!="stand_body"&amp;&amp;group.label!="900cs_body")continue;</code> |
| <a id="l94"></a>94 | <code>                    foreach(var bone in group.bones)</code> |
| <a id="l95"></a>95 | <code>                        if(bone&amp;&amp;bone.name.EndsWith("__G_pelvis",StringComparison.Ordinal))</code> |
| <a id="l96"></a>96 | <code>                        {if(group.label=="stand_body")standingPelvis=bone;else cinematicPelvis=bone;break;}</code> |
| <a id="l97"></a>97 | <code>                }</code> |
| <a id="l98"></a>98 | <code>        }</code> |
| <a id="l99"></a>99 | <code>        // Restrict fallback discovery to this player's real scene, never preview</code> |
| <a id="l100"></a>100 | <code>        // clones/resources or an unrelated open Unity scene.</code> |
| <a id="l101"></a>101 | <code>        if(!mainCamera&#124;&#124;!lightSource)</code> |
| <a id="l102"></a>102 | <code>            foreach(var root in p.gameObject.scene.GetRootGameObjects())</code> |
| <a id="l103"></a>103 | <code>            {</code> |
| <a id="l104"></a>104 | <code>                if(!mainCamera)</code> |
| <a id="l105"></a>105 | <code>                    foreach(var camera in root.GetComponentsInChildren&lt;Camera&gt;(true))</code> |
| <a id="l106"></a>106 | <code>                        if(camera.isActiveAndEnabled&amp;&amp;camera.CompareTag("MainCamera")) { mainCamera=camera;break; }</code> |
| <a id="l107"></a>107 | <code>                if(!lightSource)</code> |
| <a id="l108"></a>108 | <code>                    foreach(var light in root.GetComponentsInChildren&lt;Light&gt;(true))</code> |
| <a id="l109"></a>109 | <code>                        if(light.isActiveAndEnabled&amp;&amp;light.type==LightType.Directional) { lightSource=light;break; }</code> |
| <a id="l110"></a>110 | <code>            }</code> |
| <a id="l111"></a>111 | <code>        if(!depthShader)depthShader=Shader.Find("GGST/GeometryShadowDepth");</code> |
| <a id="l112"></a>112 | <code>        if(readBlock==null)readBlock=new MaterialPropertyBlock();</code> |
| <a id="l113"></a>113 | <code>    }</code> |
| <a id="l114"></a>114 | <code></code> |
| <a id="l115"></a>115 | <code>    bool Ready()</code> |
| <a id="l116"></a>116 | <code>    {</code> |
| <a id="l117"></a>117 | <code>        if(!p&#124;&#124;!p.nativeRendering&#124;&#124;!p.gameObject.scene.IsValid()&#124;&#124;!mainCamera&#124;&#124;</code> |
| <a id="l118"></a>118 | <code>           mainCamera.gameObject.scene!=p.gameObject.scene&#124;&#124;!lightSource&#124;&#124;!hairMask&#124;&#124;!depthShader)</code> |
| <a id="l119"></a>119 | <code>        {LastStatus="Missing explicit scene/player/light/camera/mask/depth shader";return false;}</code> |
| <a id="l120"></a>120 | <code>        if(!SystemInfo.SupportsRenderTextureFormat(RenderTextureFormat.RFloat))</code> |
| <a id="l121"></a>121 | <code>        {LastStatus="RFloat render textures are unsupported";return false;}</code> |
| <a id="l122"></a>122 | <code>        if(!depthShader.isSupported){LastStatus="Depth shader unsupported";return false;}</code> |
| <a id="l123"></a>123 | <code>        if(depthMaterial&amp;&amp;depthMaterial.shader!=depthShader)</code> |
| <a id="l124"></a>124 | <code>        {DestroyResource(depthMaterial);depthMaterial=null;}</code> |
| <a id="l125"></a>125 | <code>        if(!depthMaterial)depthMaterial=new Material(depthShader){name="GGST geometry shadow depth (hidden)",hideFlags=HideFlags.HideAndDontSave};</code> |
| <a id="l126"></a>126 | <code>        if(!hairDepth)hairDepth=CreateDepth("GGST Hair Shadow Depth",HairResolution);</code> |
| <a id="l127"></a>127 | <code>        if(!stageDepth)stageDepth=CreateDepth("GGST Stage Shadow Depth",StageResolution);</code> |
| <a id="l128"></a>128 | <code>        if(!hairDepth.IsCreated())hairDepth.Create();</code> |
| <a id="l129"></a>129 | <code>        if(!stageDepth.IsCreated())stageDepth.Create();</code> |
| <a id="l130"></a>130 | <code>        if(commands==null)commands=new CommandBuffer{name="GGST native geometry shadow maps"};</code> |
| <a id="l131"></a>131 | <code>        if(attachedCamera!=mainCamera)</code> |
| <a id="l132"></a>132 | <code>        {</code> |
| <a id="l133"></a>133 | <code>            if(attachedCamera)attachedCamera.RemoveCommandBuffer(Event,commands);</code> |
| <a id="l134"></a>134 | <code>            attachedCamera=mainCamera;attachedCamera.AddCommandBuffer(Event,commands);</code> |
| <a id="l135"></a>135 | <code>        }</code> |
| <a id="l136"></a>136 | <code>        return true;</code> |
| <a id="l137"></a>137 | <code>    }</code> |
| <a id="l138"></a>138 | <code></code> |
| <a id="l139"></a>139 | <code>    static RenderTexture CreateDepth(string label,int resolution)</code> |
| <a id="l140"></a>140 | <code>    {</code> |
| <a id="l141"></a>141 | <code>        var texture=new RenderTexture(resolution,resolution,24,RenderTextureFormat.RFloat,RenderTextureReadWrite.Linear)</code> |
| <a id="l142"></a>142 | <code>        {</code> |
| <a id="l143"></a>143 | <code>            name=label,hideFlags=HideFlags.HideAndDontSave,filterMode=FilterMode.Point,</code> |
| <a id="l144"></a>144 | <code>            wrapMode=TextureWrapMode.Clamp,useMipMap=false,autoGenerateMips=false,</code> |
| <a id="l145"></a>145 | <code>            antiAliasing=1</code> |
| <a id="l146"></a>146 | <code>        };</code> |
| <a id="l147"></a>147 | <code>        texture.Create();return texture;</code> |
| <a id="l148"></a>148 | <code>    }</code> |
| <a id="l149"></a>149 | <code>    bool Visible(SkinnedMeshRenderer renderer)</code> |
| <a id="l150"></a>150 | <code>    {</code> |
| <a id="l151"></a>151 | <code>        return renderer&amp;&amp;renderer.enabled&amp;&amp;renderer.gameObject.activeInHierarchy&amp;&amp;!renderer.forceRenderingOff&amp;&amp;</code> |
| <a id="l152"></a>152 | <code>               renderer.sharedMesh&amp;&amp;renderer.gameObject.scene==p.gameObject.scene;</code> |
| <a id="l153"></a>153 | <code>    }</code> |
| <a id="l154"></a>154 | <code>    void AddStage(SkinnedMeshRenderer renderer)</code> |
| <a id="l155"></a>155 | <code>    {</code> |
| <a id="l156"></a>156 | <code>        if(!Visible(renderer)&#124;&#124;stageSources.Contains(renderer))return;</code> |
| <a id="l157"></a>157 | <code>        stageSources.Add(renderer);stageNames.Add(renderer.name);</code> |
| <a id="l158"></a>158 | <code>    }</code> |
| <a id="l159"></a>159 | <code>    Vector3 ReadFaceOrigin(SkinnedMeshRenderer head)</code> |
| <a id="l160"></a>160 | <code>    {</code> |
| <a id="l161"></a>161 | <code>        if(head)</code> |
| <a id="l162"></a>162 | <code>        {</code> |
| <a id="l163"></a>163 | <code>            head.GetPropertyBlock(readBlock);</code> |
| <a id="l164"></a>164 | <code>            if(readBlock.GetFloat("_FaceFrameValid")&gt;0.5f)</code> |
| <a id="l165"></a>165 | <code>            {Vector4 value=readBlock.GetVector("_FaceOriginWS");return new Vector3(value.x,value.y,value.z);}</code> |
| <a id="l166"></a>166 | <code>        }</code> |
| <a id="l167"></a>167 | <code>        var pelvis=Visible(p.nativeRendering.standingHead)?standingPelvis:cinematicPelvis;</code> |
| <a id="l168"></a>168 | <code>        return pelvis?pelvis.position+Vector3.up*0.6f:p.transform.position+Vector3.up*1.5f;</code> |
| <a id="l169"></a>169 | <code>    }</code> |
| <a id="l170"></a>170 | <code>    static Quaternion LightRotation(Vector3 forward)</code> |
| <a id="l171"></a>171 | <code>    {</code> |
| <a id="l172"></a>172 | <code>        var up=Mathf.Abs(Vector3.Dot(forward,Vector3.up))&gt;0.98f?Vector3.forward:Vector3.up;</code> |
| <a id="l173"></a>173 | <code>        return Quaternion.LookRotation(forward,up);</code> |
| <a id="l174"></a>174 | <code>    }</code> |
| <a id="l175"></a>175 | <code>    static Vector3 SnapCenter(Vector3 center,Quaternion rotation,float radius,int resolution)</code> |
| <a id="l176"></a>176 | <code>    {</code> |
| <a id="l177"></a>177 | <code>        Vector3 local=Quaternion.Inverse(rotation)*center;</code> |
| <a id="l178"></a>178 | <code>        float texel=2f*radius/resolution;</code> |
| <a id="l179"></a>179 | <code>        local.x=Mathf.Round(local.x/texel)*texel;</code> |
| <a id="l180"></a>180 | <code>        local.y=Mathf.Round(local.y/texel)*texel;</code> |
| <a id="l181"></a>181 | <code>        return rotation*local;</code> |
| <a id="l182"></a>182 | <code>    }</code> |
| <a id="l183"></a>183 | <code>    static void Projection(Vector3 center,Vector3 forward,Quaternion rotation,float radius,float range,</code> |
| <a id="l184"></a>184 | <code>                           out Matrix4x4 view,out Matrix4x4 gpuProjection,out Matrix4x4 rawProjection,out Vector4 originRange)</code> |
| <a id="l185"></a>185 | <code>    {</code> |
| <a id="l186"></a>186 | <code>        const float near=0.01f;</code> |
| <a id="l187"></a>187 | <code>        Vector3 origin=center-forward*(range*0.5f);</code> |
| <a id="l188"></a>188 | <code>        Vector3 eye=origin-forward*near;</code> |
| <a id="l189"></a>189 | <code>        view=Matrix4x4.Scale(new Vector3(1,1,-1))*Matrix4x4.TRS(eye,rotation,Vector3.one).inverse;</code> |
| <a id="l190"></a>190 | <code>        rawProjection=Matrix4x4.Ortho(-radius,radius,-radius,radius,near,range+near);</code> |
| <a id="l191"></a>191 | <code>        // CommandBuffer renders this manually supplied projection without a camera RT flip.</code> |
| <a id="l192"></a>192 | <code>        // Published sampling coordinates must match the actual 2D texture rows.</code> |
| <a id="l193"></a>193 | <code>        gpuProjection=GL.GetGPUProjectionMatrix(rawProjection,false);</code> |
| <a id="l194"></a>194 | <code>        originRange=new Vector4(origin.x,origin.y,origin.z,range);</code> |
| <a id="l195"></a>195 | <code>    }</code> |
| <a id="l196"></a>196 | <code></code> |
| <a id="l197"></a>197 | <code>    // Build in onPreCull, execute after native cull/skinning and before opaque</code> |
| <a id="l198"></a>198 | <code>    // shading. An immediate ExecuteCommandBuffer during pre-cull may see the</code> |
| <a id="l199"></a>199 | <code>    // previous native skinned vertex buffer, so it is deliberately avoided.</code> |
| <a id="l200"></a>200 | <code>    void RenderMaps(Camera camera)</code> |
| <a id="l201"></a>201 | <code>    {</code> |
| <a id="l202"></a>202 | <code>        if(!isActiveAndEnabled)return;</code> |
| <a id="l203"></a>203 | <code>        ResolveReferences();</code> |
| <a id="l204"></a>204 | <code>        if(camera!=mainCamera)return;</code> |
| <a id="l205"></a>205 | <code>        if(commands!=null)commands.Clear();</code> |
| <a id="l206"></a>206 | <code>        submitted=false;HairDrawCount=0;StageDrawCount=0;</code> |
| <a id="l207"></a>207 | <code>        if(suspendMaps&#124;&#124;!Ready())</code> |
| <a id="l208"></a>208 | <code>        {DisableGlobals();if(suspendMaps)LastStatus="Suspended (offscreen draws only)";return;}</code> |
| <a id="l209"></a>209 | <code>        var bridge=p.nativeRendering;</code> |
| <a id="l210"></a>210 | <code>        var low=Visible(bridge.standingHead);</code> |
| <a id="l211"></a>211 | <code>        var hair=low?bridge.standingHead:(Visible(bridge.originalHair)?bridge.originalHair:null);</code> |
| <a id="l212"></a>212 | <code>        var face=low?bridge.standingHead:(Visible(bridge.originalFace)?bridge.originalFace:hair);</code> |
| <a id="l213"></a>213 | <code>        Vector3 origin=ReadFaceOrigin(face);</code> |
| <a id="l214"></a>214 | <code>        LightForward=lightSource.transform.forward.normalized;</code> |
| <a id="l215"></a>215 | <code>        Quaternion rotation=LightRotation(LightForward);</code> |
| <a id="l216"></a>216 | <code>        HairCenter=origin+Vector3.up*hairWorldUpOffset;</code> |
| <a id="l217"></a>217 | <code>        Transform pelvis=low?standingPelvis:cinematicPelvis;</code> |
| <a id="l218"></a>218 | <code>        StageCenter=SnapCenter(pelvis?pelvis.position:origin-Vector3.up*0.6f,rotation,Mathf.Max(stageRadius,0.5f),StageResolution);</code> |
| <a id="l219"></a>219 | <code>        Matrix4x4 hv,hp,sv,sp,hraw,sraw;Vector4 ho,so;</code> |
| <a id="l220"></a>220 | <code>        Projection(HairCenter,LightForward,rotation,Mathf.Max(hairRadius,0.05f),Mathf.Max(hairRange,0.1f),out hv,out hp,out hraw,out ho);</code> |
| <a id="l221"></a>221 | <code>        Projection(StageCenter,LightForward,rotation,Mathf.Max(stageRadius,0.5f),Mathf.Max(stageRange,1f),out sv,out sp,out sraw,out so);</code> |
| <a id="l222"></a>222 | <code>        HairVP=hp*hv;StageVP=sp*sv;HairOriginRange=ho;StageOriginRange=so;</code> |
| <a id="l223"></a>223 | <code>        ActiveHairSource=hair?hair.name:"";</code> |
| <a id="l224"></a>224 | <code>        stageSources.Clear();stageNames.Clear();</code> |
| <a id="l225"></a>225 | <code>        AddStage(bridge.originalBody);AddStage(bridge.standingHead);AddStage(bridge.originalFace);AddStage(bridge.originalHair);</code> |
| <a id="l226"></a>226 | <code>        ActiveStageSources=string.Join(" &#124; ",stageNames.ToArray());</code> |
| <a id="l227"></a>227 | <code></code> |
| <a id="l228"></a>228 | <code>        commands.SetGlobalTexture(CasterMaskID,hairMask);</code> |
| <a id="l229"></a>229 | <code>        BeginMap(hairDepth,hv,hraw,ho,true);</code> |
| <a id="l230"></a>230 | <code>        if(drawHairCasters&amp;&amp;hair)HairDrawCount=DrawToonSubmeshes(hair);</code> |
| <a id="l231"></a>231 | <code>        BeginMap(stageDepth,sv,sraw,so,false);</code> |
| <a id="l232"></a>232 | <code>        if(drawStageCasters)foreach(var renderer in stageSources)StageDrawCount+=DrawToonSubmeshes(renderer);</code> |
| <a id="l233"></a>233 | <code>        Publish(commands,"_HairShadow",hairDepth,HairVP,ho,drawHairCasters&amp;&amp;HairDrawCount&gt;0);</code> |
| <a id="l234"></a>234 | <code>        Publish(commands,"_StageShadow",stageDepth,StageVP,so,drawStageCasters&amp;&amp;StageDrawCount&gt;0);</code> |
| <a id="l235"></a>235 | <code>        // Restore the actual main target and camera matrices before regular</code> |
| <a id="l236"></a>236 | <code>        // opaque rendering. Do not leave the light's ortho state active.</code> |
| <a id="l237"></a>237 | <code>        commands.SetRenderTarget(BuiltinRenderTextureType.CameraTarget);</code> |
| <a id="l238"></a>238 | <code>        commands.SetViewport(camera.pixelRect);</code> |
| <a id="l239"></a>239 | <code>        commands.SetViewProjectionMatrices(camera.worldToCameraMatrix,</code> |
| <a id="l240"></a>240 | <code>            camera.projectionMatrix);</code> |
| <a id="l241"></a>241 | <code>        submitted=true;submittedFrame=Time.frameCount;</code> |
| <a id="l242"></a>242 | <code>        RecordCount++;LastRecordedFrame=Time.frameCount;</code> |
| <a id="l243"></a>243 | <code>        LastStatus="Queued before main opaque; native SMRs only";</code> |
| <a id="l244"></a>244 | <code>    }</code> |
| <a id="l245"></a>245 | <code>    void BeginMap(RenderTexture texture,Matrix4x4 view,Matrix4x4 projection,Vector4 originRange,bool hairOnly)</code> |
| <a id="l246"></a>246 | <code>    {</code> |
| <a id="l247"></a>247 | <code>        commands.SetRenderTarget(texture);</code> |
| <a id="l248"></a>248 | <code>        commands.SetViewport(new Rect(0,0,texture.width,texture.height));</code> |
| <a id="l249"></a>249 | <code>        commands.ClearRenderTarget(true,true,Color.white);</code> |
| <a id="l250"></a>250 | <code>        commands.SetViewProjectionMatrices(view,projection);</code> |
| <a id="l251"></a>251 | <code>        commands.SetGlobalVector(CasterOriginID,originRange);</code> |
| <a id="l252"></a>252 | <code>        commands.SetGlobalVector(CasterForwardID,new Vector4(LightForward.x,LightForward.y,LightForward.z,0));</code> |
| <a id="l253"></a>253 | <code>        commands.SetGlobalFloat(CasterHairID,hairOnly?1f:0f);</code> |
| <a id="l254"></a>254 | <code>    }</code> |
| <a id="l255"></a>255 | <code>    int DrawToonSubmeshes(SkinnedMeshRenderer renderer)</code> |
| <a id="l256"></a>256 | <code>    {</code> |
| <a id="l257"></a>257 | <code>        int draws=0;var materials=renderer.sharedMaterials;</code> |
| <a id="l258"></a>258 | <code>        int count=Mathf.Min(materials.Length,renderer.sharedMesh.subMeshCount);</code> |
| <a id="l259"></a>259 | <code>        for(int index=0;index&lt;count;index++)</code> |
| <a id="l260"></a>260 | <code>        {</code> |
| <a id="l261"></a>261 | <code>            var material=materials[index];</code> |
| <a id="l262"></a>262 | <code>            if(!material&#124;&#124;!material.shader&#124;&#124;material.shader.name!=ToonShader)continue;</code> |
| <a id="l263"></a>263 | <code>            float mirror=material.HasProperty("_UseMirroredUV")?material.GetFloat("_UseMirroredUV"):0f;</code> |
| <a id="l264"></a>264 | <code>            var scale=material.HasProperty("_MainTex")?material.GetTextureScale("_MainTex"):Vector2.one;</code> |
| <a id="l265"></a>265 | <code>            var offset=material.HasProperty("_MainTex")?material.GetTextureOffset("_MainTex"):Vector2.zero;</code> |
| <a id="l266"></a>266 | <code>            commands.SetGlobalFloat(CasterMirrorID,mirror);</code> |
| <a id="l267"></a>267 | <code>            commands.SetGlobalVector(CasterSTID,new Vector4(scale.x,scale.y,offset.x,offset.y));</code> |
| <a id="l268"></a>268 | <code>            commands.DrawRenderer(renderer,depthMaterial,index,0);</code> |
| <a id="l269"></a>269 | <code>            draws++;</code> |
| <a id="l270"></a>270 | <code>        }</code> |
| <a id="l271"></a>271 | <code>        return draws;</code> |
| <a id="l272"></a>272 | <code>    }</code> |
| <a id="l273"></a>273 | <code>    void Publish(CommandBuffer buffer,string prefix,RenderTexture texture,Matrix4x4 vp,Vector4 originRange,bool enabled)</code> |
| <a id="l274"></a>274 | <code>    {</code> |
| <a id="l275"></a>275 | <code>        buffer.SetGlobalTexture(prefix+"Depth",texture);</code> |
| <a id="l276"></a>276 | <code>        buffer.SetGlobalMatrix(prefix+"VP",vp);</code> |
| <a id="l277"></a>277 | <code>        buffer.SetGlobalVector(prefix+"OriginRange",originRange);</code> |
| <a id="l278"></a>278 | <code>        buffer.SetGlobalVector(prefix+"Forward",new Vector4(LightForward.x,LightForward.y,LightForward.z,0));</code> |
| <a id="l279"></a>279 | <code>        buffer.SetGlobalVector(prefix+"Texel",new Vector4(1f/texture.width,1f/texture.height,texture.width,texture.height));</code> |
| <a id="l280"></a>280 | <code>        buffer.SetGlobalFloat(prefix+"Enabled",enabled?1f:0f);</code> |
| <a id="l281"></a>281 | <code>    }</code> |
| <a id="l282"></a>282 | <code>    void Rendered(Camera camera)</code> |
| <a id="l283"></a>283 | <code>    {</code> |
| <a id="l284"></a>284 | <code>        if(camera!=mainCamera&#124;&#124;!submitted)return;</code> |
| <a id="l285"></a>285 | <code>        RenderCount++;LastRenderedFrame=submittedFrame;submitted=false;</code> |
| <a id="l286"></a>286 | <code>        LastStatus="Rendered before main opaque";</code> |
| <a id="l287"></a>287 | <code>    }</code> |
| <a id="l288"></a>288 | <code>    static void DisableGlobals()</code> |
| <a id="l289"></a>289 | <code>    {</code> |
| <a id="l290"></a>290 | <code>        Shader.SetGlobalFloat(HairEnabledID,0f);Shader.SetGlobalFloat(StageEnabledID,0f);</code> |
| <a id="l291"></a>291 | <code>    }</code> |
| <a id="l292"></a>292 | <code>    void Release()</code> |
| <a id="l293"></a>293 | <code>    {</code> |
| <a id="l294"></a>294 | <code>        DisableGlobals();submitted=false;</code> |
| <a id="l295"></a>295 | <code>        if(attachedCamera&amp;&amp;commands!=null)attachedCamera.RemoveCommandBuffer(Event,commands);</code> |
| <a id="l296"></a>296 | <code>        attachedCamera=null;</code> |
| <a id="l297"></a>297 | <code>        if(commands!=null){commands.Clear();commands.Release();commands=null;}</code> |
| <a id="l298"></a>298 | <code>        if(hairDepth){hairDepth.Release();DestroyResource(hairDepth);hairDepth=null;}</code> |
| <a id="l299"></a>299 | <code>        if(stageDepth){stageDepth.Release();DestroyResource(stageDepth);stageDepth=null;}</code> |
| <a id="l300"></a>300 | <code>        if(depthMaterial){DestroyResource(depthMaterial);depthMaterial=null;}</code> |
| <a id="l301"></a>301 | <code>        Shader.SetGlobalTexture("_HairShadowDepth",Texture2D.whiteTexture);</code> |
| <a id="l302"></a>302 | <code>        Shader.SetGlobalTexture("_StageShadowDepth",Texture2D.whiteTexture);</code> |
| <a id="l303"></a>303 | <code>    }</code> |
| <a id="l304"></a>304 | <code>    static void DestroyResource(UnityEngine.Object resource)</code> |
| <a id="l305"></a>305 | <code>    {</code> |
| <a id="l306"></a>306 | <code>        if(!resource)return;</code> |
| <a id="l307"></a>307 | <code>        if(Application.isPlaying)UnityEngine.Object.Destroy(resource);else UnityEngine.Object.DestroyImmediate(resource);</code> |
| <a id="l308"></a>308 | <code>    }</code> |
| <a id="l309"></a>309 | <code>}</code> |
| <a id="l310"></a>310 | <code></code> |
