# 开始调参：找到材质、切换Debug与恢复设置

先完成这里的操作，再开始每章的小实验。文中的“预期”分两类：图片旁的说明描述已有真实渲染图；未附同条件图片的参数试验是依据源码提出的观察方法，**尚未在Unity逐项验证**。实际画面还取决于你的模型、纹理、灯光及参数覆盖。

## 先确认能练到哪一步

| 已有输入 | 可以开始的操作 | 还不能直接完成的操作 |
|---|---|---|
| 自己的正常渲染角色、匹配的Base/Sss/ILM及UV | 导入Shader、绑定纹理、基础两段式、查看Debug | 不能承诺得到与图示完全一致的角色外观 |
| 另有RegionalMask和RGBA分类遮罩 | 接入头体标志、练分区明暗和分类效果 | 缺少配套图集域时，先关闭FocusedShade、ThighLobe与EyeRefine |
| 已有只读头部/root引用及渲染连接层 | 写入头体MPB和动态坐标 | 包内缺少的Player/Presentation类型仍需在自己的连接层适配 |
| 已有匹配深度输入及主相机调度 | 接墙地投影、排查投脸 | 单改接收面参数不能替代深度图生成 |

源码快照不能作为完整Unity工程直接打开。导入带有缺失类型的脚本会阻止编译；需要先读[渲染接口](dependencies.md)。没有桥接实现时，可以在独立工程只导入Shader，用自己的模型练习已具备输入的部分；自定义投影和动态脸坐标仍未接通，不应显示为成功。

## 从Renderer找到实际使用的材质

1. 在Hierarchy选中实际可见的身体对象，在Inspector找到`Skinned Mesh Renderer > Materials`。记录每个Element的编号和材质；编号从0开始，对应submesh。再对头部Renderer做同样操作。不要根据对象名称猜它正在显示哪张材质。
2. 单击Material槽中的资源定位Project里的`.mat`。在Project选中后按`Ctrl+D`复制，给副本加`_Practice`后缀，再把副本拖回原来的Element。共享原材质的其他Renderer也要逐个确认；只替换练习对象的主体槽，保留HeadGlow/HeadDecal及其他辅助槽。
3. 选中该副本，在材质Inspector的Shader下拉框选择`GGST > BridgetToonStudy`。面板中文名和源码属性名不相同；各章参数表提供二者的对应。选中GameObject的Transform面板不能修改这些属性。
4. 保存练习场景。按本章表格填入适用材质的保存值；Shader默认值只是新建材质的起点。一次只改一张材质的一个参数，确定结果后再同步其他需要的主体材质。

修改共享的Material会影响全部使用者，Play模式下修改材质资源也不能假定退出Play会撤销。结束一个试验后按事先记下的值恢复，或重新使用未改过的练习副本。不要把BodyBaseFlip的零描边宽度覆盖成Base的0.8。

Unity中材质面板由Shader决定，见[Material Inspector说明](https://docs.unity3d.com/2022.3/Documentation/Manual/class-Material.html)。

## 高编号Debug怎么打开

`_DebugMode`面板滑条只声明0–24，Shader实际支持到44。不要通过修改原Shader的Range来迁就教学。下面提供一个**新增教学示例**，用于从菜单设置练习材质的Debug；它不是原工程组件，**尚未在Unity编译或运行验证**。

1. 下载[RenderingTutorialDebugWindow.cs.txt](../assets/examples/RenderingTutorialDebugWindow.cs.txt)，保存为`RenderingTutorialDebugWindow.cs`，放入自己工程的`Assets/Editor/`。不要放进原始资料目录。
2. 等待Console编译。如果出现错误，先处理报错；不要继续假定工具可用。本示例不提供缺失的Player/Presentation类型。
3. 打开`Tools > Rendering Tutorial > Debug View`。把上一节的练习材质拖到`Practice Material`，设置`Debug Mode`，单击`Apply Debug to Material`。此按钮实际调用`Material.SetFloat("_DebugMode", 编号)`，不受面板滑条范围限制。
4. 保持该值，回Game视图看同一相机、同一姿态。多个主体材质需要逐个设置；只改Base时，使用Secondary/Coat等材质的部位仍可保持最终颜色，这是局部调试，不代表Debug失败。
5. 单击`Return to Debug 0`恢复完整画面。不要把“设44”和“设0”连在同一次调用里，否则看不到44。需要时在材质选中状态按`Ctrl+Z`撤销示例按钮的修改。

如果有自己的渲染连接层，也可以在其中单独执行`material.SetFloat("_DebugMode", 44f)`，观察后另行设回0。这里的`material`必须是Renderer实际使用的练习材质，不是临时新建却未分配的对象。[SetFloat API](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/Material.SetFloat.html)支持按准确属性名赋值。

Debug非0时外轮廓Pass主动裁掉，因此33或44画面缺外轮廓是设计行为。参阅[Debug速查](debug.md)选择输出。

投影组件已接通时，可将现有`GGSTGeometryShadowMaps`组件拖入`Shadow Maps Component`，正常主相机出图后点`Read Shadow Status`读取LastStatus、draw数、深度纹理名称和LastRenderedFrame。它们是公开C#属性，默认Inspector不会显示。若显示`not found`，拖入的组件不符合接口；纹理非空或draw数大于0也不单独证明采样坐标正确，仍要做投影对照。

## MPB覆盖在哪里改

MaterialPropertyBlock（MPB，逐Renderer属性覆盖）不显示在普通材质面板。先修改负责写它的组件，而不是反复改同名材质值：

| 想改的输入 | 在哪里操作 | 观察什么 |
|---|---|---|
| 分区启用 | 已接通的`GGSTRegionalShading > Strength`设1 | body/standingHead获得`_RegionalEnabled=1`，Debug22不再因该开关全黑 |
| 头体身份 | 组件的Body与Standing Head分别连接现有Renderer；或在自己的渲染连接层写`_RegionalHead` | body=0、head=1；它不是按材质名自动推断 |
| 脸部坐标 | 原呈现层的只读头引用；缺少该类型则在自己的适配层提供 | 有效位、原点、横轴与宽度一起更新，不能只把`_FaceFrameValid`设1 |
| 墙地接收强度 | 先查该接收Renderer是否有`_GeometryShadowFloor`的MPB | 有覆盖就改同一写入者；无覆盖时改该面的独立练习材质 |

在Debug窗口的`Renderer`拖入目标组件，`Material Slot`填Element编号，`Float Property`填`_RegionalEnabled`等Float/Range属性，点`Read Float Source`。窗口会区分材质槽MPB、Renderer MPB和材质回退；读取不写入MPB，也不推断未绑定的全局值。每次读到的是按钮执行时的值，不能证明之后的帧没有其他写入者。

自己的连接层写浮点覆盖时遵循以下**API调用片段**（不是完整组件；`target`需由现有代码提供；尚未在Unity验证）：

```csharp
var block = new MaterialPropertyBlock();
target.GetPropertyBlock(block);
block.SetFloat("_RegionalHead", 1f); // 只用于已确认的头Renderer
target.SetPropertyBlock(block);
```

该片段不提供脸坐标、不解决每帧更新，也不自动保存旧值。测试前保存该字段原有来源；若原来没有MPB字段，就不要用写0冒充“移除覆盖”。交还原写入组件处理。不要用`SetPropertyBlock(null)`清空其他组件的数据。

有材质槽MPB时该块优先于Renderer级MPB，二者不逐字段叠加；应在已有写入者和同一作用域改值。规则见[Renderer.SetPropertyBlock](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/Renderer.SetPropertyBlock.html)，判断字段是否存在用[HasProperty](https://docs.unity3d.com/2022.3/Documentation/ScriptReference/MaterialPropertyBlock.HasProperty.html)，不能将不存在字段的GetFloat=0当成覆盖值。

## 每章如何做同条件比较

1. 使用Game视图和真正渲染角色的Camera，固定输出尺寸、相机、主光、HDR/MSAA及背景。先播放已有站立动画，再点Unity工具栏Pause暂停；同姿态比较期间不要点Step或拖动Scene相机。
2. 写下目标Renderer、材质槽、原参数、Debug编号，以及临时关闭的分支。只改一个变量，等主相机正常出图后再观察；没有变化先查覆盖来源。
3. 根据本章预期检查目标局部及域外区域。输入正确但当前姿态不满足受光/朝向门控时，效果可能为零；不要盲目增加强度。
4. 恢复参数与Debug0，再回完整画面。站立循环问题按[逐姿态排查](../chapters/14.md)操作；不会仅凭网页图片或参数表认定新工程已经复现。

暂停与逐帧按钮的位置见Unity的[Game视图说明](https://docs.unity3d.com/2022.3/Documentation/Manual/GameView.html)。本教程没有附Unity界面操作截图；只有资料中真实渲染图，不能据此核实你的Inspector连接状态。
