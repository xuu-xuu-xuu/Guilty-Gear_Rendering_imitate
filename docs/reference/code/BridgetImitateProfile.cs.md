# BridgetImitateProfile.cs

按行查找正文中的函数与Pass。以下保留源码原文，属性拼写与分支顺序以此为准。代码依赖所用渲染管线及[输入连接](../dependencies.md)，不能把文件索引当作独立工程。

| 行 | 代码 |
|---|---|
| <a id="l1"></a>1 | <code>using UnityEngine;</code> |
| <a id="l2"></a>2 | <code></code> |
| <a id="l3"></a>3 | <code>// Only active in the independent study scene. Restore global quality when leaving it.</code> |
| <a id="l4"></a>4 | <code>[ExecuteAlways]</code> |
| <a id="l5"></a>5 | <code>public sealed class BridgetImitateProfile : MonoBehaviour</code> |
| <a id="l6"></a>6 | <code>{</code> |
| <a id="l7"></a>7 | <code>    public int msaaSamples=4;</code> |
| <a id="l8"></a>8 | <code>    public float shadowDistance=20;</code> |
| <a id="l9"></a>9 | <code>    public SkinnedMeshRenderer character;</code> |
| <a id="l10"></a>10 | <code>    // Extra renderers that must receive the same per-object uniforms (for example the hair</code> |
| <a id="l11"></a>11 | <code>    // mesh that was split off the body to get its own bone set).</code> |
| <a id="l12"></a>12 | <code>    public SkinnedMeshRenderer[] additional;</code> |
| <a id="l13"></a>13 | <code>    MaterialPropertyBlock previousBlock,currentBlock;</code> |
| <a id="l14"></a>14 | <code>    float originOffset,referenceHeight;</code> |
| <a id="l15"></a>15 | <code>    int previousAA;</code> |
| <a id="l16"></a>16 | <code>    float previousDistance;</code> |
| <a id="l17"></a>17 | <code>    ShadowQuality previousShadows;</code> |
| <a id="l18"></a>18 | <code>    ShadowResolution previousResolution;</code> |
| <a id="l19"></a>19 | <code>    bool applied;</code> |
| <a id="l20"></a>20 | <code>    void OnEnable()</code> |
| <a id="l21"></a>21 | <code>    {</code> |
| <a id="l22"></a>22 | <code>        if(applied)return;</code> |
| <a id="l23"></a>23 | <code>        previousAA=QualitySettings.antiAliasing;previousDistance=QualitySettings.shadowDistance;</code> |
| <a id="l24"></a>24 | <code>        previousShadows=QualitySettings.shadows;previousResolution=QualitySettings.shadowResolution;</code> |
| <a id="l25"></a>25 | <code>        if(!character){foreach(var r in FindObjectsOfType&lt;SkinnedMeshRenderer&gt;())if(r.name=="bgt_body.001"){character=r;break;}}</code> |
| <a id="l26"></a>26 | <code>        if(character){previousBlock=new MaterialPropertyBlock();currentBlock=new MaterialPropertyBlock();character.GetPropertyBlock(previousBlock);var root=character.rootBone?character.rootBone:character.transform;originOffset=character.bounds.min.y-root.position.y;referenceHeight=character.bounds.size.y;}</code> |
| <a id="l27"></a>27 | <code>        applied=true;Apply();LateUpdate();</code> |
| <a id="l28"></a>28 | <code>    }</code> |
| <a id="l29"></a>29 | <code>    void OnValidate(){if(applied)Apply();}</code> |
| <a id="l30"></a>30 | <code>    void Apply(){QualitySettings.antiAliasing=msaaSamples;QualitySettings.shadowDistance=shadowDistance;QualitySettings.shadows=ShadowQuality.All;QualitySettings.shadowResolution=ShadowResolution.High;}</code> |
| <a id="l31"></a>31 | <code>    void LateUpdate()</code> |
| <a id="l32"></a>32 | <code>    {</code> |
| <a id="l33"></a>33 | <code>        if(!applied&#124;&#124;!character&#124;&#124;currentBlock==null)return;</code> |
| <a id="l34"></a>34 | <code>        var root=character.rootBone?character.rootBone:character.transform;var origin=root.position+Vector3.up*originOffset;</code> |
| <a id="l35"></a>35 | <code>        var originValue=new Vector4(origin.x,origin.y,origin.z,0);float height=Mathf.Max(referenceHeight,0.01f);</code> |
| <a id="l36"></a>36 | <code>        character.GetPropertyBlock(currentBlock);currentBlock.SetVector("_CharacterOriginWS",originValue);currentBlock.SetFloat("_CharacterHeight",height);character.SetPropertyBlock(currentBlock);</code> |
| <a id="l37"></a>37 | <code>        if(additional!=null)</code> |
| <a id="l38"></a>38 | <code>        {</code> |
| <a id="l39"></a>39 | <code>            foreach(var r in additional)</code> |
| <a id="l40"></a>40 | <code>            {</code> |
| <a id="l41"></a>41 | <code>                if(!r&#124;&#124;r==character)continue;</code> |
| <a id="l42"></a>42 | <code>                r.GetPropertyBlock(currentBlock);currentBlock.SetVector("_CharacterOriginWS",originValue);currentBlock.SetFloat("_CharacterHeight",height);r.SetPropertyBlock(currentBlock);</code> |
| <a id="l43"></a>43 | <code>            }</code> |
| <a id="l44"></a>44 | <code>        }</code> |
| <a id="l45"></a>45 | <code>    }</code> |
| <a id="l46"></a>46 | <code>    void OnDisable()</code> |
| <a id="l47"></a>47 | <code>    {</code> |
| <a id="l48"></a>48 | <code>        if(!applied)return;</code> |
| <a id="l49"></a>49 | <code>        if(character&amp;&amp;previousBlock!=null)character.SetPropertyBlock(previousBlock);</code> |
| <a id="l50"></a>50 | <code>        QualitySettings.antiAliasing=previousAA;QualitySettings.shadowDistance=previousDistance;</code> |
| <a id="l51"></a>51 | <code>        QualitySettings.shadows=previousShadows;QualitySettings.shadowResolution=previousResolution;applied=false;</code> |
| <a id="l52"></a>52 | <code>    }</code> |
| <a id="l53"></a>53 | <code>}</code> |
