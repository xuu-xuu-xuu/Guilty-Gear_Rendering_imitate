// New teaching example, not part of the source snapshot.
// Not compiled or exercised in Unity. Intended API baseline: Unity 2022.3.
#if UNITY_EDITOR
using UnityEditor;
using UnityEngine;

public sealed class RenderingTutorialDebugWindow : EditorWindow
{
    Material practiceMaterial;
    Renderer targetRenderer;
    int materialSlot;
    int debugMode;
    string floatProperty = "_RegionalHead";
    string reading = "";
    MonoBehaviour shadowMaps;
    string shadowReading = "";

    [MenuItem("Tools/Rendering Tutorial/Debug View")]
    static void Open() { GetWindow<RenderingTutorialDebugWindow>("Rendering Debug"); }

    void OnGUI()
    {
        EditorGUILayout.HelpBox("New teaching example; not verified in Unity. Use a practice material copy. Debug writes persist on that material and affect all renderers sharing it.", MessageType.Warning);
        practiceMaterial = (Material)EditorGUILayout.ObjectField("Practice Material", practiceMaterial, typeof(Material), false);
        debugMode = EditorGUILayout.IntSlider("Debug Mode", debugMode, 0, 44);
        bool supportsDebug = practiceMaterial && practiceMaterial.HasProperty("_DebugMode");
        using (new EditorGUI.DisabledScope(!supportsDebug))
        {
            if (GUILayout.Button("Apply Debug to Material")) SetDebug(debugMode);
            if (GUILayout.Button("Return to Debug 0")) { debugMode = 0; SetDebug(0); }
        }
        EditorGUILayout.Space();
        EditorGUILayout.LabelField("Read float source (no MPB writes)", EditorStyles.boldLabel);
        targetRenderer = (Renderer)EditorGUILayout.ObjectField("Renderer", targetRenderer, typeof(Renderer), true);
        materialSlot = EditorGUILayout.IntField("Material Slot (0-based)", materialSlot);
        floatProperty = EditorGUILayout.TextField("Float Property", floatProperty);
        if (GUILayout.Button("Read Float Source")) ReadFloat();
        EditorGUILayout.HelpBox(reading, MessageType.Info);
        EditorGUILayout.Space();
        shadowMaps = (MonoBehaviour)EditorGUILayout.ObjectField("Shadow Maps Component", shadowMaps, typeof(MonoBehaviour), true);
        if (GUILayout.Button("Read Shadow Status"))
        {
            var text = new System.Text.StringBuilder();
            if (shadowMaps)
            {
                foreach (var name in new[] { "LastStatus", "HairDrawCount", "StageDrawCount", "HairDepthTexture", "StageDepthTexture", "LastRenderedFrame" })
                {
                    var property = shadowMaps.GetType().GetProperty(name);
                    text.AppendLine(name + ": " + (property != null ? System.Convert.ToString(property.GetValue(shadowMaps, null)) : "not found"));
                }
            }
            shadowReading = text.Length > 0 ? text.ToString() : "Assign the existing shadow component; no missing bridge is supplied.";
        }
        EditorGUILayout.HelpBox(shadowReading, MessageType.Info);
    }

    void SetDebug(int value)
    {
        Undo.RecordObject(practiceMaterial, "Change tutorial Debug mode");
        practiceMaterial.SetFloat("_DebugMode", value);
        EditorUtility.SetDirty(practiceMaterial);
        EditorApplication.QueuePlayerLoopUpdate();
        SceneView.RepaintAll();
    }

    void ReadFloat()
    {
        if (!targetRenderer || string.IsNullOrWhiteSpace(floatProperty))
        { reading = "Choose a renderer and a Float/Range property name."; return; }
        var materials = targetRenderer.sharedMaterials;
        if (materialSlot < 0 || materialSlot >= materials.Length || !materials[materialSlot])
        { reading = "Invalid material slot or missing material."; return; }
        var perMaterial = new MaterialPropertyBlock();
        var perRenderer = new MaterialPropertyBlock();
        targetRenderer.GetPropertyBlock(perMaterial, materialSlot);
        targetRenderer.GetPropertyBlock(perRenderer);
        // An existing per-material block takes precedence as a block, even if
        // the queried property is absent. Do not merge the two block scopes.
        var active = perMaterial.isEmpty ? perRenderer : perMaterial;
        string scope = perMaterial.isEmpty ? "Renderer MPB" : "Material-slot MPB";
        if (active.HasProperty(floatProperty))
        { reading = scope + ": " + floatProperty + " = " + active.GetFloat(floatProperty); return; }
        var material = materials[materialSlot];
        if (material.HasProperty(floatProperty))
        { reading = "Material (no active MPB field): " + floatProperty + " = " + material.GetFloat(floatProperty); return; }
        reading = "No active MPB field or material property. Global/unbound input is not inferred.";
    }
}
#endif
