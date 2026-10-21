# GGSTRegionalShading.cs 逐行索引

原文件：`sources/GGSTRegionalShading.cs`；原工程路径：`Assets/GGST_Imitate/RegionalShading/GGSTRegionalShading.cs`。

SHA256：`879a0cb9dcdd7cf59afc57c0bcefb93368594d720f18730d4fef12d054ff9618`。以下由原文生成，未修正拼写或分支。每行锚点用于正文核查；这是源码摘录索引，不是可直接运行工程。

| 行 | 原文 |
|---|---|
| <a id="l1"></a>1 | <code>using System.Collections.Generic;</code> |
| <a id="l2"></a>2 | <code>using UnityEngine;</code> |
| <a id="l3"></a>3 | <code></code> |
| <a id="l4"></a>4 | <code>// Rendering uniforms only. Never samples, moves, binds or enables a skeleton,</code> |
| <a id="l5"></a>5 | <code>// mesh, animation controller, camera or light.</code> |
| <a id="l6"></a>6 | <code>[ExecuteAlways, DisallowMultipleComponent, DefaultExecutionOrder(1200)]</code> |
| <a id="l7"></a>7 | <code>public sealed class GGSTRegionalShading : MonoBehaviour</code> |
| <a id="l8"></a>8 | <code>{</code> |
| <a id="l9"></a>9 | <code>    public SkinnedMeshRenderer body, standingHead, cinematicFace, cinematicHair;</code> |
| <a id="l10"></a>10 | <code>    [Range(0,1)] public float strength=1f;</code> |
| <a id="l11"></a>11 | <code>    struct Uniforms {public Vector2 flags;public float frame;public Vector4 origin,right;}</code> |
| <a id="l12"></a>12 | <code>    readonly Dictionary&lt;Renderer,Uniforms&gt; previous=new Dictionary&lt;Renderer,Uniforms&gt;();</code> |
| <a id="l13"></a>13 | <code>    MaterialPropertyBlock block;</code> |
| <a id="l14"></a>14 | <code>    Transform standFrame,cinematicFrame;</code> |
| <a id="l15"></a>15 | <code>    Vector4 faceOrigin,faceRight;</code> |
| <a id="l16"></a>16 | <code>    float frameValid;</code> |
| <a id="l17"></a>17 | <code>    static readonly int EnabledID=Shader.PropertyToID("_RegionalEnabled");</code> |
| <a id="l18"></a>18 | <code>    static readonly int HeadID=Shader.PropertyToID("_RegionalHead");</code> |
| <a id="l19"></a>19 | <code></code> |
| <a id="l20"></a>20 | <code>    void OnEnable(){ResolveFrames();Apply();}</code> |
| <a id="l21"></a>21 | <code>    void LateUpdate(){Apply();}</code> |
| <a id="l22"></a>22 | <code>    void OnValidate(){if(isActiveAndEnabled)Apply();}</code> |
| <a id="l23"></a>23 | <code>    public void Apply()</code> |
| <a id="l24"></a>24 | <code>    {</code> |
| <a id="l25"></a>25 | <code>        if(!standFrame&#124;&#124;!cinematicFrame)ResolveFrames();</code> |
| <a id="l26"></a>26 | <code>        var high=cinematicFace&amp;&amp;cinematicFace.enabled&amp;&amp;cinematicFace.gameObject.activeInHierarchy;</code> |
| <a id="l27"></a>27 | <code>        var frame=high?cinematicFrame:standFrame;</code> |
| <a id="l28"></a>28 | <code>        frameValid=frame?1f:0f;</code> |
| <a id="l29"></a>29 | <code>        if(frame)</code> |
| <a id="l30"></a>30 | <code>        {</code> |
| <a id="l31"></a>31 | <code>            var matrix=frame.localToWorldMatrix;</code> |
| <a id="l32"></a>32 | <code>            Vector3 axis=matrix.GetColumn(0);</code> |
| <a id="l33"></a>33 | <code>            // Cinematic proxies include imported-bone D^-1; its first column</code> |
| <a id="l34"></a>34 | <code>            // negates X. Undo that basis only for the read-only shader frame.</code> |
| <a id="l35"></a>35 | <code>            if(high)axis=-axis;</code> |
| <a id="l36"></a>36 | <code>            float width=Mathf.Max(axis.magnitude*0.083084f,0.001f);</code> |
| <a id="l37"></a>37 | <code>            axis=axis.sqrMagnitude&gt;1e-12f?axis.normalized:Vector3.right;</code> |
| <a id="l38"></a>38 | <code>            var origin=frame.position;</code> |
| <a id="l39"></a>39 | <code>            faceOrigin=new Vector4(origin.x,origin.y,origin.z,0);</code> |
| <a id="l40"></a>40 | <code>            faceRight=new Vector4(axis.x,axis.y,axis.z,width);</code> |
| <a id="l41"></a>41 | <code>        }</code> |
| <a id="l42"></a>42 | <code>        Set(body,0);Set(standingHead,1);Set(cinematicFace,1);Set(cinematicHair,1);</code> |
| <a id="l43"></a>43 | <code>    }</code> |
| <a id="l44"></a>44 | <code>    void ResolveFrames()</code> |
| <a id="l45"></a>45 | <code>    {</code> |
| <a id="l46"></a>46 | <code>        var presentation=GetComponent&lt;UEOriginalPersistentPresentation&gt;();</code> |
| <a id="l47"></a>47 | <code>        if(!presentation)return;</code> |
| <a id="l48"></a>48 | <code>        foreach(var group in presentation.groups)</code> |
| <a id="l49"></a>49 | <code>        {</code> |
| <a id="l50"></a>50 | <code>            if(group.label!="stand_head"&amp;&amp;group.label!="900cs_head")continue;</code> |
| <a id="l51"></a>51 | <code>            foreach(var bone in group.bones)</code> |
| <a id="l52"></a>52 | <code>                if(bone&amp;&amp;bone.name.EndsWith("__G_Head_def",System.StringComparison.Ordinal))</code> |
| <a id="l53"></a>53 | <code>                {if(group.label=="stand_head")standFrame=bone;else cinematicFrame=bone;break;}</code> |
| <a id="l54"></a>54 | <code>        }</code> |
| <a id="l55"></a>55 | <code>    }</code> |
| <a id="l56"></a>56 | <code>    void Set(Renderer renderer,float head)</code> |
| <a id="l57"></a>57 | <code>    {</code> |
| <a id="l58"></a>58 | <code>        if(!renderer)return;</code> |
| <a id="l59"></a>59 | <code>        if(block==null)block=new MaterialPropertyBlock();</code> |
| <a id="l60"></a>60 | <code>        renderer.GetPropertyBlock(block);</code> |
| <a id="l61"></a>61 | <code>        if(!previous.ContainsKey(renderer))previous.Add(renderer,new Uniforms{flags=new Vector2(block.GetFloat(EnabledID),block.GetFloat(HeadID)),frame=block.GetFloat("_FaceFrameValid"),origin=block.GetVector("_FaceOriginWS"),right=block.GetVector("_FaceRightWS")});</code> |
| <a id="l62"></a>62 | <code>        block.SetFloat(EnabledID,Mathf.Clamp01(strength));</code> |
| <a id="l63"></a>63 | <code>        block.SetFloat(HeadID,head);</code> |
| <a id="l64"></a>64 | <code>        block.SetFloat("_FaceFrameValid",frameValid);</code> |
| <a id="l65"></a>65 | <code>        block.SetVector("_FaceOriginWS",faceOrigin);block.SetVector("_FaceRightWS",faceRight);</code> |
| <a id="l66"></a>66 | <code>        renderer.SetPropertyBlock(block);</code> |
| <a id="l67"></a>67 | <code>    }</code> |
| <a id="l68"></a>68 | <code>    void OnDisable()</code> |
| <a id="l69"></a>69 | <code>    {</code> |
| <a id="l70"></a>70 | <code>        if(block==null)return;</code> |
| <a id="l71"></a>71 | <code>        foreach(var item in previous)</code> |
| <a id="l72"></a>72 | <code>        {</code> |
| <a id="l73"></a>73 | <code>            if(!item.Key)continue;</code> |
| <a id="l74"></a>74 | <code>            item.Key.GetPropertyBlock(block);</code> |
| <a id="l75"></a>75 | <code>            block.SetFloat(EnabledID,item.Value.flags.x);block.SetFloat(HeadID,item.Value.flags.y);</code> |
| <a id="l76"></a>76 | <code>            block.SetFloat("_FaceFrameValid",item.Value.frame);block.SetVector("_FaceOriginWS",item.Value.origin);block.SetVector("_FaceRightWS",item.Value.right);</code> |
| <a id="l77"></a>77 | <code>            item.Key.SetPropertyBlock(block);</code> |
| <a id="l78"></a>78 | <code>        }</code> |
| <a id="l79"></a>79 | <code>        previous.Clear();</code> |
| <a id="l80"></a>80 | <code>    }</code> |
| <a id="l81"></a>81 | <code>}</code> |
