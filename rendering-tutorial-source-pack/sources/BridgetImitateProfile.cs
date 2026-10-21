using UnityEngine;

// Only active in the independent study scene. Restore global quality when leaving it.
[ExecuteAlways]
public sealed class BridgetImitateProfile : MonoBehaviour
{
    public int msaaSamples=4;
    public float shadowDistance=20;
    public SkinnedMeshRenderer character;
    // Extra renderers that must receive the same per-object uniforms (for example the hair
    // mesh that was split off the body to get its own bone set).
    public SkinnedMeshRenderer[] additional;
    MaterialPropertyBlock previousBlock,currentBlock;
    float originOffset,referenceHeight;
    int previousAA;
    float previousDistance;
    ShadowQuality previousShadows;
    ShadowResolution previousResolution;
    bool applied;
    void OnEnable()
    {
        if(applied)return;
        previousAA=QualitySettings.antiAliasing;previousDistance=QualitySettings.shadowDistance;
        previousShadows=QualitySettings.shadows;previousResolution=QualitySettings.shadowResolution;
        if(!character){foreach(var r in FindObjectsOfType<SkinnedMeshRenderer>())if(r.name=="bgt_body.001"){character=r;break;}}
        if(character){previousBlock=new MaterialPropertyBlock();currentBlock=new MaterialPropertyBlock();character.GetPropertyBlock(previousBlock);var root=character.rootBone?character.rootBone:character.transform;originOffset=character.bounds.min.y-root.position.y;referenceHeight=character.bounds.size.y;}
        applied=true;Apply();LateUpdate();
    }
    void OnValidate(){if(applied)Apply();}
    void Apply(){QualitySettings.antiAliasing=msaaSamples;QualitySettings.shadowDistance=shadowDistance;QualitySettings.shadows=ShadowQuality.All;QualitySettings.shadowResolution=ShadowResolution.High;}
    void LateUpdate()
    {
        if(!applied||!character||currentBlock==null)return;
        var root=character.rootBone?character.rootBone:character.transform;var origin=root.position+Vector3.up*originOffset;
        var originValue=new Vector4(origin.x,origin.y,origin.z,0);float height=Mathf.Max(referenceHeight,0.01f);
        character.GetPropertyBlock(currentBlock);currentBlock.SetVector("_CharacterOriginWS",originValue);currentBlock.SetFloat("_CharacterHeight",height);character.SetPropertyBlock(currentBlock);
        if(additional!=null)
        {
            foreach(var r in additional)
            {
                if(!r||r==character)continue;
                r.GetPropertyBlock(currentBlock);currentBlock.SetVector("_CharacterOriginWS",originValue);currentBlock.SetFloat("_CharacterHeight",height);r.SetPropertyBlock(currentBlock);
            }
        }
    }
    void OnDisable()
    {
        if(!applied)return;
        if(character&&previousBlock!=null)character.SetPropertyBlock(previousBlock);
        QualitySettings.antiAliasing=previousAA;QualitySettings.shadowDistance=previousDistance;
        QualitySettings.shadows=previousShadows;QualitySettings.shadowResolution=previousResolution;applied=false;
    }
}
