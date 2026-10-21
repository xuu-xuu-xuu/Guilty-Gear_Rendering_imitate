using System.Collections.Generic;
using UnityEngine;

// Rendering uniforms only. Never samples, moves, binds or enables a skeleton,
// mesh, animation controller, camera or light.
[ExecuteAlways, DisallowMultipleComponent, DefaultExecutionOrder(1200)]
public sealed class GGSTRegionalShading : MonoBehaviour
{
    public SkinnedMeshRenderer body, standingHead, cinematicFace, cinematicHair;
    [Range(0,1)] public float strength=1f;
    struct Uniforms {public Vector2 flags;public float frame;public Vector4 origin,right;}
    readonly Dictionary<Renderer,Uniforms> previous=new Dictionary<Renderer,Uniforms>();
    MaterialPropertyBlock block;
    Transform standFrame,cinematicFrame;
    Vector4 faceOrigin,faceRight;
    float frameValid;
    static readonly int EnabledID=Shader.PropertyToID("_RegionalEnabled");
    static readonly int HeadID=Shader.PropertyToID("_RegionalHead");

    void OnEnable(){ResolveFrames();Apply();}
    void LateUpdate(){Apply();}
    void OnValidate(){if(isActiveAndEnabled)Apply();}
    public void Apply()
    {
        if(!standFrame||!cinematicFrame)ResolveFrames();
        var high=cinematicFace&&cinematicFace.enabled&&cinematicFace.gameObject.activeInHierarchy;
        var frame=high?cinematicFrame:standFrame;
        frameValid=frame?1f:0f;
        if(frame)
        {
            var matrix=frame.localToWorldMatrix;
            Vector3 axis=matrix.GetColumn(0);
            // Cinematic proxies include imported-bone D^-1; its first column
            // negates X. Undo that basis only for the read-only shader frame.
            if(high)axis=-axis;
            float width=Mathf.Max(axis.magnitude*0.083084f,0.001f);
            axis=axis.sqrMagnitude>1e-12f?axis.normalized:Vector3.right;
            var origin=frame.position;
            faceOrigin=new Vector4(origin.x,origin.y,origin.z,0);
            faceRight=new Vector4(axis.x,axis.y,axis.z,width);
        }
        Set(body,0);Set(standingHead,1);Set(cinematicFace,1);Set(cinematicHair,1);
    }
    void ResolveFrames()
    {
        var presentation=GetComponent<UEOriginalPersistentPresentation>();
        if(!presentation)return;
        foreach(var group in presentation.groups)
        {
            if(group.label!="stand_head"&&group.label!="900cs_head")continue;
            foreach(var bone in group.bones)
                if(bone&&bone.name.EndsWith("__G_Head_def",System.StringComparison.Ordinal))
                {if(group.label=="stand_head")standFrame=bone;else cinematicFrame=bone;break;}
        }
    }
    void Set(Renderer renderer,float head)
    {
        if(!renderer)return;
        if(block==null)block=new MaterialPropertyBlock();
        renderer.GetPropertyBlock(block);
        if(!previous.ContainsKey(renderer))previous.Add(renderer,new Uniforms{flags=new Vector2(block.GetFloat(EnabledID),block.GetFloat(HeadID)),frame=block.GetFloat("_FaceFrameValid"),origin=block.GetVector("_FaceOriginWS"),right=block.GetVector("_FaceRightWS")});
        block.SetFloat(EnabledID,Mathf.Clamp01(strength));
        block.SetFloat(HeadID,head);
        block.SetFloat("_FaceFrameValid",frameValid);
        block.SetVector("_FaceOriginWS",faceOrigin);block.SetVector("_FaceRightWS",faceRight);
        renderer.SetPropertyBlock(block);
    }
    void OnDisable()
    {
        if(block==null)return;
        foreach(var item in previous)
        {
            if(!item.Key)continue;
            item.Key.GetPropertyBlock(block);
            block.SetFloat(EnabledID,item.Value.flags.x);block.SetFloat(HeadID,item.Value.flags.y);
            block.SetFloat("_FaceFrameValid",item.Value.frame);block.SetVector("_FaceOriginWS",item.Value.origin);block.SetVector("_FaceRightWS",item.Value.right);
            item.Key.SetPropertyBlock(block);
        }
        previous.Clear();
    }
}
