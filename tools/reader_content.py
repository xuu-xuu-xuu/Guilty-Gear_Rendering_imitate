"""Reader-facing instructions. Numbers are backed by immutable rendering inputs."""
CHAPTERS={}

def add(number,problem,inputs,steps,principle,troubleshoot,params=''):
    CHAPTERS[number]=dict(problem=problem,inputs=inputs,steps=steps,principle=principle,troubleshoot=troubleshoot,
        params=[line.split('|',1) for line in params.strip().splitlines() if line.strip()])

add('00','''目标是做出清楚的明暗块、能区分头发/布料/皮肤/金属的高光，以及轻重有别的轮廓和内部线。先让角色的形体与材质读得清楚，再逐层加入局部效果。这里讲的是所附Shader的风格化方案，适用条件包括现有模型的UV、材质分区及固定角色的美术设计。''',
'''准备一个已有模型、贴图和正常站立动画的Unity项目。需要能找到身体与头部Renderer、主相机、主光和已有头部Transform。源码和示例图不包含模型、纹理像素、动画、场景或完整呈现组件；要精确得到相同图案，必须有相同输入。使用自己的模型时，先按[输入契约](../reference/channels.md)重新制作区域与分类遮罩。

使用Unity 2022.3.62f3c1、Built-in渲染管线和Linear色彩空间作为配置基准。URP/HDRP不能直接使用本教程中的ForwardBase、UnityCG和AutoLight实现。''',
'''1. 打开自己的练习场景，按[调参准备](../reference/practice.md)从身体和头Renderer找到实际材质，并复制、重新分配练习副本。预期：Game画面仍保持原来的姿态与材质槽关系；若整个角色丢失贴图，先恢复原槽，检查Shader与纹理，暂不调高光。
2. 对照[通道表](../reference/channels.md)列出自己已有的Base/Sss/ILM/Detail/OLM、区域与分类遮罩。没有随包分发的纹理不能从截图还原。缺任一输入时，按调参准备中的能力表确定可练范围，暂时关闭依赖该输入的分支。
3. 在材质上切Debug1，确认基础色和UV能对应到自己的模型，再切0。预期：眼睛、衣料和皮肤图案落在正确表面；若错位，先做贴图章，不能靠明暗阈值修正UV。
4. 按页尾路线学习。先完成01–04与08的输入，再做05–07的明暗，随后12、09、10、13、11。每章用一个固定姿态做局部试验，恢复参数后才去下一章；显示自己的角色与示例不同，不等于已经接通所有专用区域。
5. 保存一份Debug0练习场景和材质参数，进入14检查已有站立循环。预期是已有动画继续播放且渲染输入跟随；这里不要求新建动画、替换骨骼或得到与示例相同的角色。''',
'''风格化渲染的关键是把几种职责分开：明暗信号决定亮区位置，区域遮罩决定在哪里使用哪套规则，颜色乘数控制色调，高光与边缘光增加材质层次，线条整理形体。

不要把每个分支理解成连续叠加的滤镜。CleanShade会重建区域漫反射，Focused会替换局部结果，大腿亮块又会替换一部分皮肤高光。后续调参要找到最终写入位置。

正文代码块标注为“局部摘录”，用于找到需要阅读或修改的位置，不能单独编译。点击文件行号可查看完整上下文。属性名按源码使用，例如`_LightTreshold`；不要自行修正拼写后再给材质赋值。''',
'''先看全身：脸、白袖、身体皮肤应能分开阅读；头发、衣料和金属不应共用同一种亮斑；背景投影与角色表面的明暗应能独立调整。

如果一开始就追求高光和描边，容易掩盖错误的贴图通道或分区。先用Debug1确认基础色，再检查22/25的区域，最后回到0。缺少模型或桥接类型时，先完成[渲染输入连接](../reference/dependencies.md)，不要把代码文件复制进空工程后直接调参。''')

add('01','''先固定观察条件。相机距离、光照、色彩空间或曝光同时改变时，很难判断明暗和颜色究竟由哪个参数造成。''',
'''使用透视相机、白色Directional Light和已有角色。环境光参与漫反射之外的合成；示例环境模式为Skybox、强度1，fog关闭。天空/赤道/地面色为(0.212,0.227,0.259)、(0.114,0.125,0.133)、(0.047,0.043,0.035)，但实际环境还取决于Skybox材质，不能只抄这三组颜色代替天空盒。

`BridgetImitateProfile`需要显式连接character和additional Renderer，使用character.rootBone（空时Renderer.transform）计算原点和启用时高度；组件没有独立root字段。它会设置MSAA=4、shadowDistance=20、Shadows=All、分辨率High。''',
'''1. 打开`Edit > Project Settings > Player > Other Settings > Rendering`，将Color Space设为Linear。到`Graphics`检查SRP Asset，再到`Quality`逐档检查Render Pipeline Asset均为空。预期使用Built-in；若已有URP/HDRP Asset，先在独立Built-in练习工程准备输入，不直接套用本Shader。
2. 在Hierarchy选中实际输出Game画面的Camera：Projection=Perspective、Field of View=54、Clipping Planes Near/Far=0.3/1000。设置Game视图为固定1600×900进行练习，不边缩放分辨率边调线宽。相机取景应包含角色与接收面；自己的模型尺度不同时先手动取景。
3. 在Hierarchy选中主Directional Light，在Inspector设白色、Intensity=1.1。在Scene视图只旋转该光，让正面和侧面都能看到亮暗；移动Directional Light位置不会改变光向。示例保存的是四元数，见下方“准确朝向”；手动取景和转光不等于复用了该数值。
4. 打开`Window > Rendering > Lighting > Environment`，确认Environment Lighting来自Skybox、Intensity Multiplier=1，并在Other Settings关闭Fog。天空盒材质没有随包提供；不要仅抄三组环境色就声称背景和环境项一致。先保持现有天空盒不动。
5. 在自己的同条件练习中关闭Camera的Allow HDR与Allow MSAA，并固定后处理；这是1600×900对照条件，不是修改下面保存配置的事实。若已接入Profile，它的MSAA Samples=4改变质量设置，Camera禁用MSAA与质量设4并不矛盾。
6. 选中已接通的`BridgetImitateProfile`组件，将身体Renderer拖入Character，其余需要同一角色原点的Renderer放进Additional。脚本实际使用`character.rootBone`，空时回退character.transform；没有可填的Root字段。预期原点随已有root变化，身高为启用时测值；没有可用组件时先按依赖页接通，不把本步当成已生效。
7. 固定姿态，用Debug1看基础色，16看漫反射，再回0。将材质的`_AmbientStrength`临时设0再恢复原值：环境项应影响0而不改变1或16；若16也变化，检查是否同时改了灯光或其他材质。这个试验是代码推导的检查方法，未附独立同条件截图。

### 准确朝向怎么填写

上述保存坐标见[相机与主光配置](https://github.com/xuu-xuu-xuu/Guilty-Gear_Rendering_imitate/blob/main/rendering-tutorial-source-pack/data/saved_scene_rendering.json)。普通Transform Inspector显示Euler角，不能将四元数xyz填入那三格。需要精确复用保存朝向时，在自己已有的场景初始化方法中分别对Camera和Light的Transform赋Quaternion；以下是**新增教学API片段**，不是原项目代码或完整组件，尚未在Unity验证，两个引用必须先由自己的场景提供：

```csharp
practiceCamera.transform.localPosition = new Vector3(-0.113f, 0.903f, 1.822f);
practiceCamera.transform.localRotation = new Quaternion(0.0007041147f, 0.9988944f, -0.015900236f, 0.044234328f);
mainLight.transform.localRotation = new Quaternion(0.07075682f, 0.8591888f, -0.12371239f, 0.49140963f);
```

保存相机和灯没有父节点；若自己的对象有父节点，localRotation并非同一世界朝向。只做渲染练习时可使用固定的手动取景与光向，不需要为了抄坐标修改角色root。原天空盒和完整场景未提供，因此这些数值也不足以保证像素一致。''',
'''Linear模式下，sRGB颜色纹理先解码再参与光照；遮罩则要保留线性数据。Shader的`_LightIntensity=0.9`与Light组件的Intensity=1.1不是同一参数。

环境项按`UNITY_LIGHTMODEL_AMBIENT × albedo × _AmbientStrength`加入；它不直接经过Palette。整图过亮时，先区分主光、环境项和后处理，不要靠修改ILM的sRGB压暗画面。''',
'''用Debug1看基础色，用16看最终漫反射，用17看合成颜色达到1的区域。17只是代码阈值诊断，不是曝光计。

若基础色正常而最终图偏灰，先降低额外环境或后处理干扰，再检查`_AmbientStrength`。若线条忽粗忽细，固定分辨率和相机距离后再调描边；不要边缩放Game视图边判断像素宽度。''',
'''_LightIntensity|Shader中的光照强度，与Light组件强度分开调
_AmbientStrength|控制环境项，不直接改变Palette区域
_CharacterHeight|材质起始值；Profile启用后使用已有Renderer的高度覆盖''')

add('02','''把纹理连错通道，会同时改变明暗、高光和线条。先确认每个输入存的是什么数据，再调整视觉效果。''',
'''主图集使用UV0，Detail使用UV1（C#的mesh.uv2），可选镜像坐标使用UV2（mesh.uv3）。四主体材质的`_UseMirroredUV=0`，主UV应用_MainTex的Tiling/Offset。

顶点需要POSITION、NORMAL、COLOR和相应UV。COLOR.R用于AO/明暗控制。`_UseSmoothOutline=1`时，TANGENT.xyz必须预先存放专用的平滑描边法线；标准切线不能直接替代它。

Base/Sss/ILM/Detail/OLM以及区域、分类遮罩的通道、过滤、Wrap、压缩和平台覆盖分别列在[贴图连接表](../reference/texture-imports.md)。''',
'''1. 在Project逐张选择自己的纹理，在Texture Import Settings设置并点Apply：Base/Sss/OLM开启sRGB，ILM/Detail/RegionalMask/分类遮罩关闭sRGB。不要在材质球Inspector找sRGB；它属于纹理资源。若源图没有Alpha，打开“保留Alpha”也不能生成分类数据。
2. 选中练习材质，按参数表的中文面板名绑定`_MainTex`、`_ShadowMap`、`_LightMap`、`_DetailMap`、`_OutlineMap`。保持主图集Tiling=(1,1)、Offset=(0,0)作为对照起点；若自己的图集需要其他变换，逐张按绑定表核对，并确认遮罩仍与主UV一致。
3. 在自己的贴图制作工具中，以模型UV为依据准备区域遮罩：皮肤处R=1、白袖G=1，其余对应通道=0；分类遮罩在发/布/肤/金属区分别写R/G/B/A=1，其他分类通道为0，无分类处RGBA都为0。不要把Alpha删掉或让全图Alpha默认1，否则整图会混入金属。数据纹理关闭sRGB与Alpha Is Transparency，再按导入表设置尺寸、MipMap、Filter、Wrap和平台覆盖。
4. 将区域图拖到`_RegionalMask`，分类图拖到`_FourMaterialSpecMask`。逐个切Debug1/2检查Base/Sss图案，3看Detail，4/5/6/7分别看ILM.R/G/B/A：越白数值越高，7的黑处代表较强内线候选，不是孔洞。每次只改变Debug编号，检查后回0。
5. 用Debug8检查顶点R：若全黑，先在练习材质把`_AOStrength`从1暂设0，比较10；亮暗恢复只能说明AO输入影响了信号，不能证明顶点数据已修好。用Debug9看世界法线颜色是否随表面平滑变化；这里没有附网格通道数值，不能凭图认定TANGENT已合格。
6. 在有UV1的练习模型上把`_DetailIntensity`从0切到0.278，再恢复所属材质值。预期Debug3反映UV1的原始采样，强度改变后应在Debug16看漫反射；Debug1返回Detail处理前的Base，应保持不变；若16不变，先确认纹理不是纯白、材质槽正确以及UV1存在。Coat目标值是0，不应强行加细节。
7. 接通头体标志后用22看区域，25看分类。换UV时按本章“专用坐标怎么改”在自己的Shader副本重新标定眼睛、胸前衣料和腿域；未完成前关闭对应局部开关，不声称相同分辨率就能复现。

### 专用坐标怎么改

以下只在自己的Shader副本操作。源码仍按2048虚拟像素计算：`p=(u*2048,(1-v)*2048)`，左上是原点。若纹理宽高为W/H，在自己的图像工具中量得实际像素(x,y)，先换为这个虚拟坐标：`p=(x/W*2048,y/H*2048)`。保持2048公式时，所有新中心、半径和边界都使用同一虚拟单位；不能只改一个2048常量。主纹理Tiling/Offset不为单位值时，还要对应变换后的采样UV。

| 在哪里修改 | 具体先做什么 | 如何确认范围 |
|---|---|---|
| [眼区337–362](../reference/code/BridgetToon.shader.md#l337) | 在自己的Base图上量虹膜椭圆中心/半径，分别替换eyeSmallQ/eyeLargeQ与瞳孔保护参数；同时重定eyeQ的1020分界、eyeDomain矩形、眼白色门控及原白点 | Enabled=1、head=1下用33，先确认R只在虹膜、G只在眼白、B只在已有白点，再回0逐项调深浅 |
| [胸前衣料464–467](../reference/code/BridgetToon.shader.md#l464) | 原图两块矩形分别为x768.5–895.5/y640.5–895.5和x512.5–895.5/y895.5–1343.5；在自己图集找目标衣料岛，替换两块矩形的上下限 | 用37检查Tunic蓝色域、42检查局部band；相邻皮肤、头发不能被选入 |
| [腿域507–518](../reference/code/BridgetToon.shader.md#l507) | 替换腿域x200–510/y880–1195以及focusedCalf/focusedKnee沿纵向的过渡范围 | 先用40，确定只覆盖目标腿表面，再用41看大腿/膝/小腿的band |
| [亮形583–603](../reference/code/BridgetToon.shader.md#l583) | 沿自己UV岛的前侧量中心线，重做thighCenter各分段、halfWidth、916–1001纵向窗口和1015–1030替换域过渡 | 43只覆盖需要替换的皮肤范围，44在朝向门控满足时显示细长收尖形，再用13/0确认合并 |

若自己的UV岛不是矩形、前侧走向不连续，原矩形/分段式不能精确描述，需要另制区域遮罩并在自己的Shader中接入；此适配没有通用实测实现，不能给出未知模型的系数。未重标定的EyeRefine、FocusedShade和ThighLobe先保持关闭，不把没有效果解释成强度太小。''',
'''Base.RGB是基础色，Sss.RGB是阴面颜色，这里的混合不属于物理次表面散射。Detail通过`base × lerp(1,detail,_DetailIntensity)`乘入基础色。

ILM.R×255用于基础分类，G偏移明暗信号，B提供高光细节，`1-ILM.A`提供内部线覆盖。ILM.A和分类图A都不是透明度，主体输出Alpha=1。OLM.RGB只参与墨色，不提供Alpha线宽。''',
'''如果Debug7能看到线条，最终却出现透明孔洞，应检查是否误用了透明Shader，而不是继续调ILM Alpha。若高光和墨线同时串区，先检查数据纹理的sRGB和压缩。

如果Detail没有变化，检查UV1和强度；CoatExterior的Detail强度为0，本来就不显示该项。若轮廓刺出，先确认TANGENT.xyz的实际语义，不能通过修改骨骼补救。''',
'''_UseMirroredUV|主图集的UV选择；修改前确认UV2已经准备好
_DetailIntensity|乘法细节强度，先检查UV1再调值
_AOStrength|顶点R对明暗信号的权重
_UseSmoothOutline|是否按专用TANGENT.xyz读取平滑描边法线''')

add('03','''同一材质可以同时用于头和身体，但头体不能因此共用所有参数。把材质槽和逐Renderer覆盖连接正确，后续脸部、皮肤和眼睛才会进入正确分支。''',
'''保留原有submesh/材质槽：身体和站立头使用Base/BaseSecondary、BodyBaseFlip、CoatExterior；HeadGlow、HeadDecal分别使用自己的Shader。不要把贴花、发光或辅助槽批量替换成主体Shader。

准备身体、站立头Renderer、已有头部Transform、root、相机与方向光。`GGSTRegionalShading`依赖现有呈现组件的groups查头坐标，`GGSTGeometryShadowMaps`依赖Player/nativeRendering；缺少这些类型时需要先适配[输入接口](../reference/dependencies.md)，不能直接挂脚本。''',
'''1. 在Hierarchy分别选择身体和当前站立头，在`Skinned Mesh Renderer > Materials`逐槽确认实际材质。按[统一方法](../reference/practice.md)复制和分配副本；只把主体槽设为`GGST/BridgetToonStudy`，保留HeadGlow/HeadDecal。预期只有目标材质发生变化；整头消失时先恢复槽和剔除设置。
2. 对每张主体副本按参数参考填写保存值：Base/Secondary/Flip的`_DetailIntensity=0.278`，Coat=0；`_OutlineWidth`在Base/Secondary/Coat=0.8、Flip=0。不要把一张材质复制到所有槽后丢失差异。参数表中的Shader默认列不是要填入的最终值。
3. 只有现有Presentation连接可用时，才在该呈现对象上通过Add Component接入`GGSTRegionalShading`：将身体拖到Body、站立头拖到Standing Head，Strength=1；本教程不接其他动作引用。预期脚本逐Renderer写body的`_RegionalHead=0`、头=1以及`_RegionalEnabled=1`。若Console缺少类型，停在[依赖接入](../reference/dependencies.md)，不要创建空类冒充桥接。
4. 用Debug窗口的只读来源查询，对身体和头的实际材质槽分别读取`_RegionalEnabled`与`_RegionalHead`。若仍显示材质值0，先查组件是否活动、引用是否正确及是否存在材质槽MPB；不通过改共享材质的head解决头体差异。
5. 在两类主体材质切22。按源码，头皮肤应为红色脸域、身体皮肤为绿色、白袖为蓝色；头发及未覆盖区保持黑。再切38看CleanShade覆盖，两者用途不同。若脸和身体混淆，回第4步；若区域边缘偏移，回贴图章。
6. 从原有头引用读取脸原点/横轴，并且有效时才写`_FaceFrameValid=1`。Regional原脚本没有独立Head Transform槽可填；缺少Presentation时必须由自己的连接层实现这组更新，本文未提供已验证的通用桥接。最后把Debug恢复0，保留组件Strength=1再继续。''',
'''参数优先级是Shader默认值、材质值、逐Renderer MPB或全局输入；之后还要经过Shader内部替换。默认值只决定新材质起点，并不等于示例材质值。

MPB用于让共享材质的不同Renderer拥有不同head标志和坐标。脸部动态向量不能写成固定世界坐标，否则角色运动后区域会漂移。`_CharacterHeight`则是Profile启用时测得的高度，不是每帧重算的动画包围盒高度。''',
'''22全黑：依次检查区域图、strength、Renderer引用和_RegionalEnabled。头体颜色一样：检查_RegionalHead是否逐Renderer写入，是否被后来的整块MPB覆盖。

图中的Debug38只显示CleanShade覆盖，不是Debug22。多个组件写同一Renderer时，要注意Profile禁用会恢复主character的整块旧MPB，additional没有逐个备份；Regional只恢复自己的字段。组件开关后若区域消失，先排查覆盖顺序。''',
'''_RegionalEnabled|材质起点为0；Regional脚本strength=1时逐Renderer覆盖为1
_RegionalHead|材质起点为0；头Renderer需要MPB=1
_FaceFrameValid|只有有效头部坐标输入才能设为1
_DetailIntensity|四主体的细节强度不同
_OutlineWidth|保留Flip的零宽设置
_EyeRefineEnabled|还需要head门控，不能靠开关自动识别头部''')

add('04','''先知道各部分在什么时候写入颜色。调节没有进入最终结果的中间量，是“参数改了却看不出变化”的常见原因。''',
'''主体Shader包含FORWARD、OUTLINE、SHADOWCASTER三个Pass。FORWARD使用Built-in的UnityCG/Lighting/AutoLight输入；OUTLINE为独立反向壳；SHADOWCASTER由Unity阴影阶段调度。

自定义阴影深度图在主不透明绘制前准备。因此实现时先接输入与投影，再在FORWARD中建立明暗和各类着色；文件里Pass的排列不等于逐像素计算顺序。''',
'''1. 在Project选中自己的`BridgetToon.shader`，打开文件并用查找定位`half4 frag`、`Name "FORWARD"`、`Name "OUTLINE"`、`Name "SHADOWCASTER"`。只阅读本章列出的最后写入位置；局部摘录不是可粘贴到文件末尾的新Pass。
2. 对实际练习材质打开Debug窗口，依次Apply 10、16、13、12、31，每次回Game视图观察后再改下一号。10应是基础受光权重，16是最终漫反射，13是最终高光，12是rim，31是内线墨色；不能把这些分量当作连续叠加截图。
3. 以材质的`_CleanShadeEnabled`做覆盖试验：先记下1，设0，保持Debug10观察，再切16。按源码该开关不写回band，10不应因这个开关改变；16的覆盖区可能改变。若10也改变，检查是否同时改了光、姿态或其他输入。该试验尚无独立截图。
4. 恢复CleanShade=1。后续每次“参数没反应”都先定位最后写入者：16追CleanShade/FocusedShade，13追FocusedSpec/ThighLobe，12追ReferenceRim；高编号经窗口设置，不修改_DebugMode的原始Range。
5. 点击`Return to Debug 0`，确认完整颜色和外壳都回来。只切Debug时外轮廓消失是代码行为，不去增加_OutlineWidth。继续08接投影输入，再进入05搭建基础明暗。''',
'''FORWARD内的准确位置如下：

| 顺序 | 计算 | 源码行 |
|---|---|---|
| 1 | 采样、眼区、分类、基础band | 321–401 |
| 2 | 头体区域、侧脸和投脸的基础贡献 | 405–458 |
| 3 | Palette，再由CleanShade重建覆盖区diffuse并纳入Palette | 461–501 |
| 4 | Focused局部漫反射、眼睛漫反射细化 | 507–529 |
| 5 | ambient、基础rim、分类spec、Focused/Thigh高光替换 | 532–609 |
| 6 | ReferenceRim替换，再合成diffuse+ambient+rim+spec | 616–625 |
| 7 | 内部线覆盖、原眼睛白点恢复、Debug/最终输出 | 630–725 |

CleanShade不写回band。FocusedSpec重算受光带，ReferenceRim仍使用基础band的阴面权重。因此10、16、13的明暗范围不必完全相同。ThighLobe先替换focusedSkinShine，再经过FocusedSpec的差值合并进入spec。''',
'''若Debug10看起来正确而16不同，先看CleanShade和FocusedShade；26–29有亮斑而13不同，要看FocusedSpec/ThighLobe；调整_RimWidth无效时，先确认分类区是否使用ReferenceRim。

_DebugMode面板范围是0–24，代码实际支持1–44。设置高编号时使用材质或MPB的SetFloat调用，检查完恢复0；例如设置44只是查看域，不表示大腿开关已生效。19/20展示的变量没有接入最终颜色，不适合判断成图。''',
'''_CleanShadeEnabled|覆盖区重建漫反射
_FocusedShadeEnabled|修正腿与胸前衣料漫反射
_FocusedSpecEnabled|决定局部分类高光的最终合并
_ThighLobeEnabled|只在满足域与分类门控时替换腿部高光
_ReferenceRimEnabled|分类区使用ReferenceRim
_DebugMode|0为最终输出；高编号通过代码设置''')

add('05','''连续的Lambert明暗容易把模型的小凹凸都变成碎影。先压成两块清楚的亮面与阴面，只在边界保留窄过渡。''',
'''输入是世界法线、主光方向、Base、Sss、ILM.G及COLOR.R。基础皮肤分类还使用ILM.R。先连接[投影输入](08.md)，再区分表面受光和接收阴影。

_LowerLightDynamic=1时下半身光向会混回当前主光；不要只看_LowerLightDirection保存向量就以为有一盏固定补光灯。''',
'''1. 在一张单独的练习材质记录所有改动前值，按下方“隔离基础路径”暂时关闭重建、分区、局部配色、下半身修正及基础投影接收。使用Debug16看diffuse而不是混有spec/rim的0；有原生阴影不等于它还在乘入band。
2. 切Debug1、5、8检查Base、ILM.G和顶点R，再设10。基础起点用`_LightTreshold=0.5`、`_RampOffset=0`、`_RampMaskCenter=0.49803922`、`_RampMaskStrength=1`、`_AOStrength=1`、`_ShadowSoftness=0.008`。这些是示例材质保存值；以下0.4/0.6/0.03是练习试值，不是最终材质配置。
3. 只把`_LightTreshold`依次设0.4、0.6，再恢复0.5。预期同一信号在较高阈值时更难进入白色亮区，边界移动；若整块面信号全在阈值同侧，当前姿态可能看不到差异。先固定两段边界，不去调高光。
4. 保持阈值0.5，只将`_RampMaskStrength`从1设0再恢复1。Debug10不再跟随ILM.G的起伏；若G本来全在中性值附近，差异可能很小。再单独把`_AOStrength`从1设0并恢复，顶点R低于1的压暗应减弱。两次试验不能一起做。
5. 在16中将`_ShadowSoftness`从0.008暂设0.03再恢复：有分界的位置应出现更宽的过渡，而亮暗面颜色不是由该参数直接指定。再用`_RampOffset`小幅正向调整，观察整体更容易进入亮面后恢复0；没有对应单变量截图，这些是待你在练习场景核实的源码预期。
6. 按记录恢复分支和Regional Strength；示例目标CleanShade、FocusedShade、Palette等保存为1，`_ReceiveShadowStrength=0.7`。不要把隔离时的0留到后续章节。回16检查后续覆盖，再回0看完整画面；10改变而16不跟随时按04查重建分支。

### 隔离基础路径：临时值与恢复值

这是一张练习隔离表，不是目标配置。先记下自己场景的值；“示例恢复值”仅适用于已按示例表填写的材质。MPB有覆盖时要在实际写入者改，不以材质面板的0冒充已关闭。

| 在哪里改 | 临时值 | 示例恢复值 | 为什么先关 |
|---|---|---|---|
| 材质_CleanShadeEnabled | 0 | 1 | 不让区域重建覆盖基础diffuse |
| 材质_FocusedShadeEnabled | 0 | 1 | 排除腿/衣料局部修正；还依赖CleanShade |
| 材质_PaletteEnabled | 0 | 1 | 将颜色乘数与明暗边界分开 |
| 材质_EyeRefineEnabled | 0 | Base/Secondary=1，Flip/Coat=0 | 排除眼睛局部漫反射改色 |
| Regional组件Strength；无组件且无MPB时确认材质_RegionalEnabled已为0 | 0；用来源查询确认_RegionalEnabled=0 | 组件Strength=1、MPB=1；材质保存值仍0 | 排除区域/脸部路径；该材质属性隐藏，不在普通面板直接改head身份 |
| 材质_ReceiveShadowStrength | 0 | 0.7 | 让band不再乘基础投影衰减 |
| 材质_LowerLightBlend | 0 | 0.8 | 固定使用主光方向，不混下半身方向 |
| 材质_SecondShadowStrength | 0 | 0.9 | 暂不叠加下半身第二暗部颜色 |

Debug16不包含ambient/spec/rim/ink，因此无需再把所有高光与描边参数归零。保持_ShadowIntensity等基础阴色参数不动，亮暗阈值试验只验证边界；完成后恢复表中各项再进入分区章。''',
'''半兰伯特信号为`nl=dot(n,l)*0.5+0.5`，n和l是单位世界方向。它将[-1,1]映射到[0,1]，只是美术受光信号。

公式解释（不是可直接编译的源码；省略下半身光向混合、投影和后续分区）：

```text
ao = lerp(1, saturate(vertex.r), _AOStrength)
signal = (nl + _RampOffset + (ILM.G-_RampMaskCenter)*_RampMaskStrength
          + skin*_SkinShadowOffset) * ao
band = smoothstep(_LightTreshold-soft, _LightTreshold+soft, signal)
```

基础阴色为`lerp(albedo,Sss*_ShadowTint,_ShadowIntensity)`，再按band混合亮暗。G是信号偏移，不是简单乘到最终颜色上的AO。后续分区可能重建漫反射，基础band仍会被部分高光、rim和诊断读取。''',
'''图示基础色与两段式属于累计效果示意，不是仅修改_LightTreshold的独立A/B。复现时应自己固定其他开关，观察阈值带来的局部变化。

碎影跟着纹理走：查G和顶点R。碎影随视角改变：查世界法线、背面翻转。10改变而16没变：查后续重建，而不是继续拉高基础阈值。''',
'''_LightTreshold|越高越难进入亮面，保留源码拼写
_RampOffset|整体平移受光信号
_RampMaskCenter|ILM.G的偏移中心
_RampMaskStrength|G通道对分界的影响
_ShadowSoftness|基础分界的过渡宽度
_ShadowIntensity|基础阴色向Sss混合的权重
_SkinShadowOffset|基础皮肤分类的信号偏移
_AOStrength|顶点R权重''')

add('06','''脸部暗带、腹部碎影和白袖发灰，不能只用一个全局阈值解决。先分区，再为脸、身体皮肤和衣料使用不同的明暗规则。''',
'''RegionalMask.R/G分别为皮肤/白袖；_RegionalHead把皮肤分成脸和身体。FourMaterialSpecMask.G提供其他布料区域，ILM.G、顶点R和世界法线继续参与受光。

胸前衣料使用2048图集的两块域：x768.5…895.5/y640.5…895.5和x512.5…895.5/y895.5…1343.5；y=(1-v)×2048。腿域为x200…510/y880…1195。使用不同UV时，先重定这些域或制作相应遮罩，不要先调阈值。''',
'''1. 确认Regional的Strength=1且头体标志正确，在目标练习材质将`_CleanShadeEnabled=1`。先用22看脸/身体皮肤/白袖，再用38看CleanShade覆盖。预期遮罩只覆盖目标区域；域外变化先查分类和区域，不调整阴色来遮掩串区。
2. 先把`_FocusedShadeEnabled=0`作为隔离设置，在Debug16观察；Palette等保持记录值不动。这样检查基础身体皮肤阈值时，不会被腿域的Focused阈值替换。结束此小段后要恢复Focused=1。
3. 在头材质把`_CleanFaceUnderStart=-0.7`、`_CleanFaceUnderEnd=-0.45`作为起点。只将End暂改-0.3，再恢复-0.45；按世界n.y的smoothstep，部分原过渡区更难全亮，应改变下暗面过渡。若改旧的_FaceDiffuseBoundary而这里不变，属于后续重建，不是参数失效。
4. 在身体材质只将`_SkinShadeThreshold`从0.69暂改0.74，观察身体皮肤亮区缩小后恢复；再把`_SleeveShadeThreshold`从0.68暂改0.73，观察白袖后恢复。以上是练习试值，未附单参数截图；没有信号跨过阈值时不保证肉眼可见。一次只做一组，域外不应受此阈值直接影响。
5. 在含其他衣料的材质确认`_CleanClothMaskWeight=0.4`、`_CleanClothAOWeight=0.25`、`_CleanClothSoftness=0.018`。先把MaskWeight暂设0并恢复，再把AOWeight暂设0并恢复：分别减少ILM.G与顶点R对衣料信号的影响。它们不负责脸下暗面，不能用这组数调整脸。
6. 恢复`_FocusedShadeEnabled=1`，用41看腿的局部band、42看胸前衣料band。示例腿阈值大腿/小腿/膝=0.57/0.59/0.62，衣料=0.4。只把大腿阈值暂改0.62，41应仅在匹配腿UV域改变，42不应因这一个参数变化；随后恢复0.57，回16再回0。换UV未重标定时不要据此判断解剖区域已被识别。''',
'''脸、身体皮肤、白袖分别来自region.r×head、region.r×(1-head)、region.g×(1-head)。CleanShade在覆盖区重建diffuse，并纳入Palette乘数。

脸的简化下暗面主要是`smoothstep(_CleanFaceUnderStart,_CleanFaceUnderEnd,n.y)`，不是通用脸SDF，也不保证头大幅旋转时仍符合美术预期。其他布料使用独立分类并排除已经覆盖的区域，避免重复计入。

FocusedShade以差值修改已有的CleanShade局部结果。腿的阈值依图集位置在大腿0.57、小腿0.59和膝0.62之间变化，胸前衣料为0.4；不是自动识别解剖结构。''',
'''38是覆盖，不是亮暗；41/42才显示相应局部band。预期脸保留简洁下暗面，腹部和袖子减少小碎影，区域边界不串到头发或其他衣料。

切CleanShade后脸的投发暗带消失，可能是diffuse被重建的结果；应结合投影节定位最终路径。若世界n.y导致特殊头姿态不合适，需要为自己的角色重新设计脸部规则，不能只抄固定阈值。''',
'''_CleanShadeEnabled|启用区域漫反射重建
_CleanFaceUnderStart|脸下暗面过渡起点，使用世界n.y
_CleanFaceUnderEnd|脸下暗面过渡终点
_CleanClothMaskWeight|衣料对ILM.G的依赖
_CleanClothAOWeight|衣料对顶点AO的依赖
_CleanClothSoftness|衣料分界过渡
_SkinShadeThreshold|身体皮肤基础阈值；腿域还会被Focused修正
_SleeveShadeThreshold|CleanShade白袖使用的阈值
_RegionalSoftness|皮肤和Focused腿域的过渡宽度
_SkinShadeTint|身体皮肤阴色乘数
_SkinShadeStrength|身体皮肤阴色混合
_SleeveShadeTint|白袖阴色乘数
_SleeveShadeStrength|白袖阴色混合
_FaceDiffuseTint|CleanShade脸部阴色起点的颜色
_FaceDiffuseDepth|CleanShade脸部阴色起点的混合强度
_FocusedShadeEnabled|启用腿与胸前的局部修正
_FocusedTunicThreshold|胸前衣料阈值
_FocusedThighThreshold|大腿阈值
_FocusedCalfThreshold|小腿阈值
_FocusedKneeThreshold|膝盖阈值''')

add('07','''明暗边界合适以后，再调亮面和阴面的色调。这样可以修正皮肤偏脏、袖子偏黄等问题，而不破坏已经整理好的明暗形状。''',
'''Palette依赖皮肤/白袖遮罩、head标志、胸前UV域和各自band。输入仍是Base与Sss；Palette不是贴图替代。

六个_Palette*Light/Dark在Shader中是Vector，公式使用rgb，第四分量为0。它们是计算乘数，不是屏幕最终颜色，也不具有Color属性相同的颜色输入语义。''',
'''1. 在已接通区域的目标材质保留CleanShade/Focused设置，切37确认皮肤、白袖和胸前衣料范围，再切16。没有正确范围时回02/03，先不改配色向量。
2. 记下`_PaletteEnabled=1`，临时设0并恢复。预期只改变diffuse中的区域乘色；高光、rim和墨线不由Palette直接调色。若比较的是0，其他分量会让色调差异更难辨认，因此先看16。
3. 保持Palette=1，在材质“皮肤亮面乘色”`_PaletteSkinLight`的Vector四格输入临时(1,1,1,0)，再恢复示例(0.92,1.1,1.28,0)。预期只改变皮肤亮面附近的RGB比例，不移动明暗信号；纯阴面位置可能不明显。第四格W保留0，不当作透明度。
4. 单独把“皮肤暖阴面乘色”`_PaletteSkinDark`临时设(1,1,1,0)，再恢复(0.82,0.7,0.82,0)。观察皮肤阴面；若亮面也随其他开关移动，说明比较条件不固定。这两次单位向量试验是源码推导，未附各自A/B图。
5. 白袖和胸前衣料采用相同方法，但只改对应的Sleeve或Tunic向量，恢复值从下表读取。先在有亮面/阴面的位置各看一次16，再回0；不要用灯光颜色代替区域向量。更换UV后，Tunic域需先按02重新定位。''',
'''单一区域内可用`M=lerp(M_dark,M_light,band)`理解配色，漫反射再乘M。这个数学解释省略了区域混合、CleanShade重建和光照，不是完整实现。

皮肤亮面乘数(0.92,1.1,1.28)降低R相对比例，阴面乘数(0.82,0.7,0.82)与已有阴色相乘。不能仅看向量就给出最终sRGB取色。

Palette只作用于diffuse。CleanShade重建时会重新纳入相同乘数，不应在合成外再乘一次。ambient、spec、rim和墨线有独立路径。''',
'''37显示区域，16显示漫反射，0显示完整合成。16改变而高光颜色没跟着变是正常的分量分工；如果整张图一起偏色，应检查主光、环境和sRGB。

示意图用于观察配色方向，不是六个向量的独立开关对照。调参时保持同一姿态，每次只动一个区域的一组乘数。''',
'''_PaletteEnabled|控制区域配色
_PaletteSkinLight|皮肤亮面RGB乘数
_PaletteSkinDark|皮肤阴面RGB乘数
_PaletteSleeveLight|白袖亮面RGB乘数
_PaletteSleeveDark|白袖阴面RGB乘数
_PaletteTunicLight|胸前衣料亮面RGB乘数
_PaletteTunicDark|胸前衣料阴面RGB乘数''')

add('08','''先把三类阴影分开：角色表面受光、头发投脸、角色投到墙和地面。它们使用不同路径，不能用一个“阴影强度”统一解释。''',
'''需要已连接的Player/nativeRendering、实际可见Renderer、只读头/骨盆坐标、同场景主相机与方向光、分类图R作为hairMask，以及GGSTGeometryDepth Shader。缺少原呈现类型时，按[接口说明](../reference/dependencies.md)接入已有对象；没有可用的深度纹理时不能只把全局enable设为1。

GGSTGeometryShadowMaps字段基准为hairRadius=0.28、hairRange=1.2、hairWorldUpOffset=0.08、stageRadius=2、stageRange=8；suspendMaps关闭，两个draw开关打开。头发深度图1024²、Stage深度图2048²，均为RFloat、Point/Clamp、无MipMap、单采样。''',
'''1. 若完整Player/Presentation连接已具备，在该Player对象上的`GGSTGeometryShadowMaps`中填写P、Main Camera、Light Source、Hair Mask、Depth Shader；Hair Mask使用分类图R，Depth Shader选择`GGST/GeometryShadowDepth`。不要把Sss或ILM当hairMask。缺少这些类型时，本步骤没有可直接挂入的通用组件，先按[依赖页](../reference/dependencies.md)接入自己的渲染层。
2. 组件Suspend Maps关闭，Draw Hair Casters/Draw Stage Casters打开；Hair Radius/Range/World Up Offset=0.28/1.2/0.08，Stage Radius/Range=2/8。让正常主相机渲染后检查公开的HairDrawCount/StageDrawCount大于0、深度纹理非空及LastStatus。它们是公开属性而不是默认Inspector序列化字段；在教学窗口将组件拖入Shadow Maps Component并点Read Shadow Status读取。该窗口尚未在Unity验证；看不到状态时不能仅凭组件勾选就宣称已产生深度图。
3. 在自己的场景创建或使用已有墙、地接收面，确保它们不是与模型重叠的面。各分配一张独立的`GGST/StageShadowReceiver`练习材质，在“投影最低可见率/深度偏移/边缘过滤/距离衰减”填写：地面0.08/0.0007/0.65/0.12，墙面0.1/0.001/0.8/0.08。具体位置与尺寸按自己的角色取景设置，源码包没有场景可直接复制。
4. 回Debug0、暂停同一姿态，先读墙面Renderer是否有`_GeometryShadowFloor`的MPB。无覆盖时在墙面的独立材质把floor从0.1改1，再恢复0.1；有覆盖时在同一MPB写入者改值，不能通过材质越过它。预期只取消墙面自定义衰减，地面影子和角色着色保留。再单独对地面做0.08→1→0.08；地面这个单独试验没有配套A/B截图。
5. 若已确认深度路径正常，临时关闭Draw Stage Casters再恢复，理解“禁用自定义路径”会回退Unity的SHADOW_ATTENUATION，不能把剩余Unity影子判为开关失败。影子截断先增大适用的Radius/Range并逐个恢复确认，不同时改Bias与范围。
6. 头发投脸先用32读遮挡，再在16看最终漫反射。Base/Secondary保存`_HairFaceShadowStrength=0`，且CleanShade可覆盖脸部中间贡献；因此当前目标脸上没有明显发影不证明深度图无效。若要单独研究基础投脸，只在练习副本暂关CleanShade和FocusedShade，确认_FaceFrameValid=1后，只将Base/Secondary的_HairFaceShadowStrength从0暂设0.75并比较32/16，再全部恢复。该隔离实验尚未在Unity验证，不作为最终效果的操作结果。
7. 保持同姿态，在32或接收面上一次只调Bias或Filter，确认贴面误遮挡/软边的变化再恢复对应保存值。最后回0恢复全部draw开关与材质，播放已有站立循环看影子是否跟随；不通过改骨骼或动画抵消错位。''',
'''深度图从光源方向记录最近表面。接收点投到同一VP空间后比较深度，靠后的点受遮挡。Bias减少表面误判自身遮挡，太大则可能让影子悬空；3×3过滤只软化边缘。

脚本在onPreCull记录命令，通过BeforeForwardOpaque使用现有蒙皮Renderer并发布深度图。Stage中心在光空间按texel对齐；错误的更新时机可能造成影子滞后。

接收面可见率为`1-occlusion*(1-floor)`，因此floor=1会取消自定义衰减而保留有效深度路径。角色的_ReceiveShadowStrength只影响基础band；投脸先改变脸diffuse，随后可能被CleanShade覆盖。Base/Secondary的投脸强度为0，不能把它强行调高当作目标效果。''',
'''影子截断先检查radius/range，错位先检查VP和纹理坐标，贴面黑斑查bias，悬空查bias是否过大。若深度图白且draw count为0，先排查Ready与Renderer，不要判为“没有遮挡”。

最终脸部没有投发暗带时，先看当前强度和CleanShade覆盖；Debug32非黑只说明中间遮挡量存在。墙/地对照图及具体复现步骤见[投影与眼睛调试](../reference/experiments-20261021.md)。''',
'''_ReceiveShadowStrength|角色基础band接收Unity投影的权重
_HairFaceShadowStrength|投脸基础贡献，后面可能被CleanShade替换
_HairFaceShadowBias|头发深度比较偏移
_HairFaceShadowFilter|头发投影过滤范围
_CleanShadeEnabled|决定脸部是否被后续漫反射重建覆盖''')

add('09','''头发、布料、皮肤和金属不应共享同一种亮点。用分类遮罩分别控制形状、强度和颜色，避免角色看起来像同一种塑料。''',
'''FourMaterialSpecMask.R/G/B/A依次为头发/布料/皮肤/金属；ILM.B提供局部高光细节。还需要世界法线、视线、主光方向和分区受光。

_FourMaterialSpecEnabled和_FocusedSpecEnabled配合使用。未分类的部位保留后备spec；不要为了覆盖眼睛而把分类图全部填满。''',
'''1. 在头发、衣料、皮肤、金属实际使用的练习材质确认`_FourMaterialSpecEnabled=1`，用25看RGBA分类的合成显示。分类区域不能重叠到眼睛；若全图发白，先检查分类图Alpha是否被默认填1，不直接降低强度。
2. 先用13看最终spec。为比较基础四类，把`_FocusedSpecEnabled=0`、`_ThighLobeEnabled=0`，记下之后需恢复1；Palette和漫反射保持不动。26/27/28/29只隔离各类基础贡献，不等于最终13。
3. 一次只做一类强度归零：头发_HairShineStrength 0.12→0→0.12；布料_ClothShineStrength 0.035→0→0.035；皮肤_SkinShineStrength 0.028→0→0.028；金属_MetalShineStrength 0.38→0→0.38。预期13中对应类别贡献减少，其他类别不因该参数直接变化。若当前姿态本来无高光，先查看对应分类和nh，而不是提高所有强度。
4. 仍保持FocusedSpec=0，只将衣料`_ClothShinePower`从12暂设6，再恢复12。对0<nh<1的表面，幂指数减小应使亮区更宽；这个试值未附单变量截图。头发与金属用各自Width控制阈值亮带，不能套用衣料Power的数值。
5. 恢复`_FocusedSpecEnabled=1`与`_ThighLobeEnabled=1`，回13。只把_FocusedHairGain从1.25设0并恢复，再分别试布料1.2与金属1.05的Gain；这些字段才参与最终差值替换。腿域皮肤另用_FocusedSkinStrength=0.14与下一章的ThighLobe，不继续只调_SkinShinePower期待改变腿部最终亮形。
6. 回0看高光是否淹没眼睛和内部线，保持当前相机与灯光再播放已有站立循环。任一分类归零仍发亮时先用12排除rim，并查未分类后备spec、MPB与其他材质槽。本章归零/指数试验为源码预期，已有图示只证明其各自展示分量。''',
'''`nh=saturate(dot(n,normalize(l+v)))`使用半程向量。Power越高，幂函数亮区越集中；阈值与smoothstep形成亮带，fwidth提供最小像素过渡。

头发使用较宽肩部和ILM.B亮芯；布料、皮肤使用较弱幂函数；金属具有更强亮芯。基础分类spec之后，FocusedSpec重算受光带并以差值替换分类贡献，脸部皮肤排除相应覆盖。最终应看13，而不是把26–29当最后结果。

Palette不直接调spec。大腿会继续替换focusedSkinShine，内部线则在完整光照后覆盖。''',
'''26–29有亮斑但13不同：查Focused/Thigh替换。边界出现双倍亮度或串色：查分类重叠、sRGB和压缩。调整头发却影响布料：先修分类图，不要靠降低全局SpecularIntensity补偿。

逐姿态spec图见[站立画面排查](../reference/standing-stability-20261021.md)。亮块随表面朝向变化是预期行为，应重点找同一姿态的随机变化或整类贡献异常消失。''',
'''_FourMaterialSpecEnabled|启用RGBA分类高光
_HairShineStrength|头发基础高光强度
_HairShineWidth|头发基础亮带宽度
_HairShineTint|头发高光颜色
_ClothShineStrength|衣料基础强度
_ClothShinePower|衣料亮区集中程度
_ClothShineTint|衣料高光颜色
_SkinShineStrength|皮肤基础强度
_SkinShinePower|皮肤亮区集中程度
_SkinShineTint|皮肤高光颜色
_MetalShineStrength|金属基础强度
_MetalShineWidth|金属基础亮芯宽度
_MetalShineTint|金属高光颜色
_FocusedSpecEnabled|启用最终分类高光替换
_FocusedHairGain|Focused头发倍率
_FocusedClothGain|Focused布料倍率
_FocusedMetalGain|Focused金属倍率
_FocusedSkinStrength|Focused皮肤强度
_FocusedSkinWidth|Focused皮肤亮区宽度''')

add('10','''给大腿一块范围稳定、下端收尖的局部亮形，同时清除周围不需要的散光。形状由当前图集坐标定义，可见度再受光向与视向控制。''',
'''需要分类图B的皮肤、身体皮肤域、head=0、世界法线/视线/光向，以及当前2048图集的腿UV。_FocusedSpecEnabled必须接入最终高光合并。

换UV时要重新设计腿域、中心曲线、宽度、纵向窗口和膝盖过渡。普通点高光的宽度参数不能替代这些空间定义，也不要改骨骼或Bind Pose迁就图集常量。''',
'''1. 在身体实际材质保持`_RegionalHead=0`、Regional=1、FourMaterialSpec=1、FocusedSpec=1，使用22确认身体皮肤，再用25确认B类皮肤。没有分类B时，后续ThighLobe不能合并进入最终spec。
2. 用Debug窗口依次设置40、43、44：40看腿相关域，43看较宽替换域，44看收尖亮形乘朝向。预期都局限在当前匹配UV的腿区；若全黑，先按本章图集范围核对UV，不通过提高Strength修复不存在的域。
3. 固定姿态，把`_ThighLobeEnabled`先设0再1，同时分别观察13及0；一次只改这个开关。预期域内由Focused皮肤高光切换为局部收尖亮块，周围可能变暗，因为替换不是简单加亮。43/44不乘这个开关，所以它们不应被当作开关状态指示。
4. 在确认亮形可见时，将`_ThighLobeStrength`从0.16暂设0再恢复0.16，Tint保留(0.92,1,0.45,1)。预期亮块减弱至零，但替换域仍在，原Focused亮斑不会自动返回；要比较原高光应切Enabled=0。强度归零的单独试验尚未在Unity验证。
5. 换模型时只修改自己的Shader副本中507–518、583–603的域与中心曲线，先让43正确、再让44正确，最后才调强度。具体重标定顺序见02；本文不能提供未知UV的中心或膝坐标。
6. 恢复Enabled=1、Strength=0.16，回0播放已有站立循环。正常情况亮块会随表面朝向减弱或消失；只有同姿态随机变化、域越膝或整片皮肤受影响，才回13/43/44排错。''',
'''坐标为`p=(u*2048,(1-v)*2048)`，腿域x200…510、y880…1195。前侧中心从357.89起分段修正，在y约981处改变走向；完整系数见局部源码，不能概括为任意UV上的直竖条。

收尖使用`t=saturate((p.y-918)/82)`和`halfWidth=7.2*(1-pow(t,1.15))`。fwidth平滑横向边缘，纵向窗口约916–1001；朝向门控为`smoothstep(0.2,0.55,nv)*smoothstep(0.50,0.68,nl)`，nl是半兰伯特。

替换域比亮形更宽，在y1015–1030前收掉。域内即使lobe=0，也会替换掉基础腿部高光。ThighLobe先替换focusedSkinShine，再由FocusedSpec合并到spec，所以它不是完全独立的最终高光层。''',
'''44有形而13没有：查开关、FocusedSpec、皮肤分类、head及受光带。整腿变色：查替换域范围。亮形扭曲：查UV和中心曲线。

示例OFF/ON图是同条件的ThighLobe开关对照；Debug44只显示域与朝向。Tint是Color参数，屏幕亮块还受光色、受光带和显示转换影响，不应直接按Tint数值取色。''',
'''_ThighLobeEnabled|控制腿部局部替换
_ThighLobeStrength|局部亮块强度
_ThighLobeTint|亮块颜色输入，不是最终屏幕颜色
_FocusedSpecEnabled|大腿结果合并进入最终spec的依赖
_FocusedSkinStrength|替换域之外的Focused皮肤高光
_FocusedSkinWidth|Focused皮肤亮带宽度''')

add('11','''内部线说明衣料和五官结构，外轮廓整理剪影。分别控制它们，避免把所有黑色细节都当成同一套描边。''',
'''内部线使用ILM.A与分类图；外轮廓使用POSITION、NORMAL、UV、ILM.R、OLM.RGB以及可选TANGENT.xyz。开启_UseSmoothOutline前必须确认网格已保存专用描边法线。

先完成主体颜色、眼睛和边缘光，再在最终Debug0中判断线条轻重。线条对相机距离、输出分辨率和抗锯齿很敏感。''',
'''1. 在Game视图固定分辨率、相机与抗锯齿，回0。逐张主体材质确认`_OutlineWidth`：Base/Secondary/Coat=0.8，Flip=0。只把一张非零材质暂设0再恢复，预期对应外壳消失、内部纹理线仍在；若看不出，先确认你改的是轮廓可见部位的材质。
2. 使用自己的网格时，在练习材质将`_UseSmoothOutline=0`作为几何法线基线。只有另有证据表明TANGENT.xyz已存专用描边法线，才切1比较；切1后出现尖刺就恢复0。没有提供网格数据，不能保证普通模型得到平滑外壳，也不在这里重写网格。
3. `"材质分区线条启用"`即_LineRefineEnabled设1。在_LineContourWidths的X/Y/Z/W按发/布/肤/金属读取，示例为(0.82,0.95,0.6,0.72)。只把皮肤Z暂设0再恢复0.6，观察已分类皮肤轮廓是否减弱；未分类后备和Flip的0基宽不能据此产生外壳。此分量试验未附独立A/B。
4. 切7看ILM.A，30看覆盖，31看内部墨色，再回Debug0判断强度。30/31没有乘_LineInnerStrengths，改强度时它们不显示最终变化。保持LineRefine=1，只将_LineInnerStrengths皮肤Z从0.58暂设0并恢复，其他X/Y/W不动。预期已分类皮肤内线贡献减弱；若黑线不受影响，先区分贴图本身的暗色、其他材质、外壳或未分类部分。
5. 将_LineInnerFilter从0.6暂设0再恢复，比较31中细线缩小时的覆盖变化。它只过滤Alpha，不要给整张ILM.RGB加模糊或改sRGB。颜色仍由四类Ink、TintMix和OLM参与，先定覆盖再改墨色。
6. 回0恢复所有宽度与强度，播放已有站立循环。31没有外壳是Debug裁剪行为；真正的轮廓判断必须在0。4K示意的临时1.6不写回本章0.8基宽，自己的目标分辨率需要另行观察。''',
'''外轮廓是Cull Front反向壳Pass。屏幕外扩的裁剪坐标增量为`direction*(2*width/_ScreenParams.xy)*clip.w`，width是像素尺度。分类比例由_LineContourWidths/0.8参与；零宽层保持零宽。

内部线覆盖率为`1-saturate(ILM.A)`，只对Alpha做中心加四邻域的屏幕足迹过滤，ILM.RGB仍原样采样。连续覆盖率有助于缩小时保留细线。

线条在diffuse+ambient+rim+spec合成后覆盖；眼睛原白点恢复在内线之后。Debug非0时OUTLINE被裁掉，因此31只能检查内部线，不能检查外轮廓。''',
'''刺出的轮廓：查TANGENT语义。材质交界过粗：查分类、基宽和零宽层。Debug图没有外轮廓：先回0。关了外描边仍有黑线：这是内部线，继续查ILM.A。

4K累计示意把轮廓像素宽度放大两倍，不能把其1.6宽度直接写回基准材质。比较不同分辨率前，先确定要保持的是像素宽度还是屏幕占比；在自己的目标设备和抗锯齿条件下观察细线，不以网页缩放代替Unity画面判断。

内部强度变了但30/31不变是预期：这两个诊断返回过滤覆盖与墨色，没有乘inkStrength。调_LineInnerStrengths或_InnerLineStrength要回Debug0观察，不能按31亮度判断该强度是否生效。''',
'''_OutlineWidth|外轮廓像素基宽；Flip保持0
_UseSmoothOutline|读取专用TANGENT.xyz，而非普通切线
_OutlineSkinScale|基础皮肤轮廓缩放
_LineRefineEnabled|启用分类线条控制
_LineContourWidths|发/布/皮/金属外轮廓比例
_LineInnerStrengths|四类内部线覆盖强度
_LineInnerFilter|Alpha屏幕足迹过滤权重
_LineContourTintMix|外轮廓墨色混合
_LineInnerTintMix|内部线墨色混合
_LineHairInk|头发分类墨色
_LineClothInk|衣料分类墨色
_LineSkinInk|皮肤分类墨色
_LineMetalInk|金属分类墨色
_OutlineColor|后备轮廓墨色
_OutlineMapStrength|OLM参与墨色的权重''')

add('12','''给虹膜增加上暗下亮的层次，保护黑瞳、眼线和原有白点。变化要局限于眼区，避免把整张脸提亮成贴纸。''',
'''输入是主图集Base、主UV、head标志、主光和band，不需要新增眼睛纹理。_EyeRefineEnabled在Base/Secondary为1，Flip/Coat为0，还需要_RegionalHead=1。

区域是当前2048图集专用：小虹膜中心(960,64)、半径(34,34)，大虹膜中心(1152,130)、半径(104,100)。眼白域在x896…1280/y0…256，并结合接近(0.8388,0.8308,0.9301)的颜色选择。换图集要重新标定虹膜、瞳孔、眼白、原白点及颜色门控。''',
'''1. 在Hierarchy选站立头，确认所用Base/Secondary练习材质及`_RegionalHead=1`的MPB；在Debug窗口把该材质设33。预期R是虹膜、G是眼白、B是原白点，兜帽和普通脸皮肤不应成为眼区。区域不对时先改自己的图集坐标，不开始调亮度。
2. 暂停固定姿态，保持同一Camera近景与输出设置。在材质“眼睛分区层次启用”`_EyeRefineEnabled`做0→1，并在Debug0截图比较；再单独切34查贡献后回0。现有同条件裁切只支持该总开关对照，不证明下面每个子参数的独立效果已经实测。
3. 保持Enabled=1，先把“虹膜上层深色”_EyeIrisUpperDepth从0.18设0再恢复，预期取消上部暗化；再把“虹膜下层透亮”_EyeIrisLowerLift从0.1设0再恢复，预期取消受光下部提亮。两次分开做，黑瞳和眼线不应整体变亮；band为0时下部加亮可能本来不可见。
4. 单独将_EyeIrisEdgeDepth从0.08设0再恢复，检查虹膜边缘暗化；再单独将_EyeScleraShade从0.06设0再恢复，检查眼白轻微冷暗变化。当前姿态或分辨率可能让差异很小，不能把34的显示亮度当作最终画面增亮量。
5. 单独将_EyeCatchlightLift从0.25设0再恢复，只比较原白点，不期待生成新运动光点。保留HeadGlow/HeadDecal槽，白点也可能受贴图和辅助层影响。上述子参数归零试验依据源码，尚未在Unity逐个验证。
6. 全部恢复本章保存值并回0，按14播放已有站立循环，在眼形、朝向变化处暂停检查。换UV时按02先重标定虹膜/瞳孔保护/眼白/原白点与颜色门控；同分辨率的新贴图不能直接复用旧坐标。''',
'''EyeDisk通过长度阈值和fwidth形成平滑椭圆；`min(base.g,base.b)-base.r`选择青色虹膜，结合瞳孔保护，避免把黑瞳、眼线和白点一起提升。

漫反射先压暗上部和外缘，再根据原albedo与band提亮下部。内部线合成后，代码恢复已有白高光，不生成运动点。原小眼白点中心为(938.7075,48.0896)/(983.5789,85.5)，这不是通用眼睛定位方法。

如果MPB没有Eye开关覆盖，应读取材质值；对不存在的MPB字段调用GetFloat得到0，不能据此认定眼睛关闭。''',
'''瞳孔变亮：检查色度与瞳孔保护域。整脸被改色：先检查head和UV域。34很亮但0变化轻微：诊断表达式和显示颜色不同，不要继续盲目提高强度。

近景开关图来自同姿态、相同取景的Debug0图，以相同矩形[744,316,955,439]裁切为211×123，只裁切不修饰。更完整的操作对照见[投影与眼睛调试](../reference/experiments-20261021.md)。''',
'''_EyeRefineEnabled|启用眼睛细化，还需head门控
_EyeIrisUpperDepth|虹膜上部暗化
_EyeIrisLowerLift|虹膜下部提亮
_EyeIrisEdgeDepth|虹膜边缘深度感
_EyeCatchlightLift|恢复原白点清晰度
_EyeScleraShade|眼白轻微压暗
_RegionalHead|头Renderer由MPB写1''')

add('13','''在角色接近轮廓的表面增加受控亮带，让剪影从背景中分离。边缘光和正面材质高光使用不同的方向函数，要分别调。''',
'''需要世界法线、视线、albedo、基础band、材质分类图和脸区域。ReferenceRim使用分类图的发/布/皮/金属权重，脸再额外减弱。

保持背景、相机、主光和高光参数不动，先单独观察rim。''',
'''1. 在头体练习材质确认分类图正确，切12查看rim。保持主光、背景和相机不变；13才是spec，12上应主要看到接近轮廓的亮带，不以整幅0的高光判断rim。
2. 把`_ReferenceRimEnabled`从1设0再恢复1，理解分类区切回后备rim时仍可能有亮边。要仅检查ReferenceRim强度，保持Enabled=1，将`_ReferenceRimStrength`从0.5设0再恢复0.5；分类区该项应减弱，未分类后备可以保留。这两个试验不能混做。
3. 保持Strength=0.5，只把_ReferenceRimWidth从0.24暂设0.12再恢复。按nv形状，较小宽度更贴近轮廓；如果调_RimWidth仅影响零散部位，先确认那些部位是否未分类，而不是同时加两组宽度。
4. 保持宽度不动，逐个检查TintMix=0.75、Material=(1,0.9,0.65,0.6)、FaceScale=0.15。若要隔离脸部，暂设FaceScale=0再恢复，观察脸域额外衰减；若连身体一起变，先查head/区域。不要用Light Intensity代替脸部缩放。
5. 在12中将_ReferenceRimShadowFloor从0.55暂设0再恢复，观察band低于1的边缘是否减弱。基础band并非CleanShade最终diffuse，因此阴面亮边不必与16完全同域。上述子参数试验为源码预期，尚无逐项同条件图。
6. 恢复本章参数并回0，看rim是否淹没内部线；播放已有站立循环，亮边应随法线与视角变化。朝向门控造成的明暗变化不是额外逆光灯或时间动画。''',
'''令`nv=saturate(N·V)`，nv越小越靠近侧边。ReferenceRim的形状为`1-smoothstep(width-aa,width+aa,nv)`，其中`aa=max(fwidth(nv)*0.65,0.008)`。宽度越大，亮边覆盖越宽。

颜色在albedo与_ReferenceRimTint之间混合；材质缩放按分类权重平均。`lerp(_ReferenceRimShadowFloor,1,saturate(band))`让阴面保留一定亮边。

最终按_ReferenceRimEnabled×specCoverage替换rim，未分类区域仍使用_RimWidth/_RimIntensity后备。它是美术描光，不是额外的真实逆光灯。''',
'''正面出现亮块时，用13确认是否其实是spec；12的亮带太宽，再查nv和ReferenceRimWidth。阴面仍亮不一定是错误，先看ShadowFloor。

CleanShade改变diffuse不等于改rim；ReferenceRim沿用基础band，FocusedSpec则有自己的受光带。若三个分量不一致，先按各自输入排查，再回到0判断是否协调。''',
'''_ReferenceRimEnabled|分类区使用ReferenceRim
_ReferenceRimWidth|最终分类区主要亮边宽度
_ReferenceRimStrength|亮边强度
_ReferenceRimShadowFloor|阴面保留权重
_ReferenceRimTint|亮边颜色输入
_ReferenceRimTintMix|albedo与Tint之间的混合
_ReferenceRimMaterial|发/布/皮/金属权重
_ReferenceRimFaceScale|脸部额外缩放''')

add('14','''完成静态画面后，播放已有站立循环，检查投影、眼睛、高光和描边是否在相同姿态下重复出现异常变化。不同姿态的正常运动与同姿态的闪变要分开判断。''',
'''固定相机、光照、分辨率、HDR/MSAA、贴图与材质设置。先确认现有动画能正常播放，不改动画、骨骼、网格或Bind Pose排除渲染问题。

对照图使用1600×900、HDR关闭、相机MSAA关闭、单采样RT。若你的目标配置不同，按自己的配置重新观察，不能直接用图像变化像素数比较质量。''',
'''1. 在Game视图固定尺寸、相机、光、HDR/MSAA和所有参数，保留自己的既有站立播放系统。点Play，待正常主相机完成出图后点Pause；不在一次脚本更新里反复Camera.Render来假定原生蒙皮已经刷新。
2. 在同一暂停姿态依次Apply 1、4–9检查输入，22/25/38看分区与覆盖，16看diffuse，13看spec，12看rim，31看内线，最后0看外壳。每次只改Debug；把问题定位到具体分量，再改相关参数。
3. 取消Pause连续观察完整站立循环，分别盯墙地影子边缘、虹膜白点、大腿亮块和肩/发梢轮廓。若现有播放系统可只读显示姿态编号，记下异常编号，下一循环在同编号复查；不要新写动画或骨骼控制器来制造编号。
4. 用工具栏Pause与Step逐帧前进，观察离散姿态切换前后影子是否滞后一帧、眼区是否串出、高光是否整类消失、外壳是否尖刺。Step只推进帧，不保证恰好推进一张姿态；本文不提供所有工程通用的“第N帧=cell N”对应。
5. 若缺少可重复选择同一姿态的原有接口，只能做定性逐帧观察。暂时不能证明同姿态像素一致、完整连续时序都稳定或HDR/MSAA目标设备通过；不能把两幅不同姿态的图片不同称为闪变，也不把这里的示例图当作你工程的测量结果。
6. 遇到异常暂停，按下方症状表定位；在同一姿态只切对应一个开关，例如墙floor、EyeRefine、ThighLobe或OutlineWidth，然后恢复。若改变姿态才能重现，先保存原参数，等下一次同姿态再比较，不同时换光照与相机。
7. 到循环末端与回绕处复查。Step播放允许姿态跳切，重点是正常相机渲染后输入是否同步，不要求相邻画面像素相同。最后恢复全部参数与Debug0，自己的HDR/MSAA或设备条件不同需另行观察；不为消除渲染异常修改动画、骨骼或Bind Pose。''',
'''同一姿态、相机、光和输入下，画面应可重复。不同姿态则会改变法线、遮挡、投影位置和像素覆盖，不应要求零差。

排查顺序是环境→输入→区域/覆盖→漫反射→高光/rim→线条→时序。切换Debug会隐藏外轮廓，检查线条时必须记得回0。对照图只帮助判断效果职责，不能代替自己设备上的HDR、抗锯齿和细线观察。''',
'''| 症状 | 先检查 | 如何区分 |
|---|---|---|
| 分区黑或头体混淆 | RegionalMask、head/enable MPB | 22看分区，38看覆盖 |
| 脸部参数没反应 | CleanShade重建 | 16看最终diffuse；35/36是替换前贡献 |
| 腿过亮或高光像塑料 | 分类、Focused、Thigh | 25→13→43/44 |
| 贴图边缘串色 | sRGB、压缩、MipMap、Wrap | 4–7对照实际导入设置 |
| 外轮廓刺出或缺失 | TANGENT、零宽、Debug | 回0，分开关外壳与内线 |
| 眼睛发白或串区 | 图集域、瞳孔保护、head | 33看区域，34看贡献，0看幅度 |
| 投影滞后或截断 | Ready、范围、VP、调度 | 对照draw、纹理与主相机渲染时机 |
| 整图灰或过曝 | 主光、环境、后处理 | 1→16→17区分输入与合成 |

逐姿态最终图、spec图和眼睛局部，以及更细的操作顺序见[站立画面排查](../reference/standing-stability-20261021.md)。不要为消除渲染异常而修改现有动画。''',
'''_DebugMode|选择需要隔离观察的分量，结束回0
_CleanShadeEnabled|排查最终区域漫反射
_FocusedSpecEnabled|排查分类高光的最后替换
_ThighLobeEnabled|隔离腿部局部高光
_ReferenceRimEnabled|区分rim与spec''')

# Operation targets are kept next to the chapter instructions.
WORKSPACES = {'00': '在自己的独立练习场景操作，先选实际可见的身体/头Renderer，再选它们Materials槽里的材质资源。入口、Debug窗口和恢复方法见[开始调参](../reference/practice.md)。本章只建立输入与观察基线，不新增动画或控制器。',
 '01': '环境在Project '
       'Settings与Lighting窗口设置；相机、方向光和Profile引用在Hierarchy选中相应对象后到Inspector设置。Shader的_LightIntensity在材质上，与Light组件的Intensity分开。',
 '02': '导入开关在Project选中纹理后的Inspector，连接纹理在Project选中练习材质后的Inspector，UV/顶点输入来自已有网格。不要在材质上找sRGB，也不要将缺失的贴图像素当作源码可以生成的资源。',
 '03': '对象引用在Hierarchy中呈现对象的GGSTRegionalShading组件上填；材质差异在每个Renderer的Materials槽对应副本上填。MPB不在普通材质面板，使用[只读来源查询](../reference/practice.md)确认真实输入。',
 '04': '控制流在自己的Shader副本中阅读，Debug在实际使用的练习材质上切换。用[菜单窗口](../reference/practice.md)保持每个编号直到看完；不要将代码摘录粘贴为新Pass，也不要按章节编号推断执行顺序。',
 '05': '选一张可见主体材质的练习副本；分区Strength在写MPB的组件上临时改，其余下划线参数在材质上改。先记录完整恢复值，再隔离基础路径。本章练习试值是源码推导，尚未在Unity逐项验证。',
 '06': '头部下暗面参数改头材质，身体皮肤/白袖/腿参数改它们实际使用的材质。示例中共享材质的多个Renderer会同时受影响，先分配自己的练习副本。头体标志仍在MPB输入层。',
 '07': '在对应练习材质的Palette向量四格中改RGB/W，使用Vector而不是颜色吸管。各组面板中文名见参数表；Debug37/16经[Debug窗口](../reference/practice.md)设置。',
 '08': '深度输入与范围在Player对象的GGSTGeometryShadowMaps组件；墙地强度在各自接收Renderer的材质或现有MPB写入者；角色投影/投脸参数在主体材质。三个位置不要混用。本包不提供可直接挂入空场景的Player适配器。',
 '09': '在目标部位所用的主体练习材质修改分类高光参数；分类图在Project纹理导入和材质槽检查。下面先关Focused做基础试验，再恢复最终路径，不动已经整理的漫反射。',
 '10': '只在身体皮肤实际使用的材质上改开关/强度/Tint；局部域和收尖几何在自己的Shader副本中重标定。43/44使用[高编号Debug窗口](../reference/practice.md)，不修改原Shader的面板范围。',
 '11': '外壳宽度、分类比例、内部强度与墨色均在目标练习材质；TANGENT来自已有网格，不能通过材质开关自动准备。全程用固定Game输出，Debug0看外轮廓，30/31只看内线。',
 '12': '在站立头的Base/Secondary练习材质上改眼睛参数；先用来源查询确认该Renderer的head MPB为1。相机近景只在进入对照前调整一次，开关比较期间不再改构图。',
 '13': '在有分类遮罩的主体练习材质修改ReferenceRim参数，先看Debug12再回0。未分类区域仍是后备_Rim路径；保持光与相机不动，避免把spec误当rim。',
 '14': '在已有场景Game视图用Unity工具栏Play/Pause/Step观察，不重建播放系统。参数仍在各章指定的材质或MPB写入者改；没有可重复姿态输入时明确限制为定性观察。'}

for number, workspace in WORKSPACES.items():
    CHAPTERS[number]["workspace"] = workspace
