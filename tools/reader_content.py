"""Reader-facing instructions. Numbers are backed by immutable rendering inputs."""
CHAPTERS={}

def add(number,problem,inputs,steps,principle,troubleshoot,params=''):
    CHAPTERS[number]=dict(problem=problem,inputs=inputs,steps=steps,principle=principle,troubleshoot=troubleshoot,
        params=[line.split('|',1) for line in params.strip().splitlines() if line.strip()])

add('00','''目标是做出清楚的明暗块、能区分头发/布料/皮肤/金属的高光，以及轻重有别的轮廓和内部线。先让角色的形体与材质读得清楚，再逐层加入局部效果。这里讲的是所附Shader的风格化方案，适用条件包括现有模型的UV、材质分区及固定角色的美术设计。''',
'''准备一个已有模型、贴图和正常站立动画的Unity项目。需要能找到身体与头部Renderer、主相机、主光和已有头部Transform。源码和示例图不包含模型、纹理像素、动画、场景或完整呈现组件；要精确得到相同图案，必须有相同输入。使用自己的模型时，先按[输入契约](../reference/channels.md)重新制作区域与分类遮罩。

使用Unity 2022.3.62f3c1、Built-in渲染管线和Linear色彩空间作为配置基准。URP/HDRP不能直接使用本教程中的ForwardBase、UnityCG和AutoLight实现。''',
'''1. 先完成环境、贴图、材质和逐Renderer参数连接，确认角色在Debug0中正常显示。
2. 阅读Shader结构，先接好主光与投影输入，再实现两段式明暗、分区和配色。
3. 在区域漫反射之后细化眼睛，再加入四类材质高光和大腿亮块；随后处理边缘光、内部线及外轮廓。
4. 在同一姿态下逐项调整，最后播放已有站立循环，定位随姿态出现的问题。''',
'''风格化渲染的关键是把几种职责分开：明暗信号决定亮区位置，区域遮罩决定在哪里使用哪套规则，颜色乘数控制色调，高光与边缘光增加材质层次，线条整理形体。

不要把每个分支理解成连续叠加的滤镜。CleanShade会重建区域漫反射，Focused会替换局部结果，大腿亮块又会替换一部分皮肤高光。后续调参要找到最终写入位置。

正文代码块标注为“局部摘录”，用于找到需要阅读或修改的位置，不能单独编译。点击文件行号可查看完整上下文。属性名按源码使用，例如`_LightTreshold`；不要自行修正拼写后再给材质赋值。''',
'''先看全身：脸、白袖、身体皮肤应能分开阅读；头发、衣料和金属不应共用同一种亮斑；背景投影与角色表面的明暗应能独立调整。

如果一开始就追求高光和描边，容易掩盖错误的贴图通道或分区。先用Debug1确认基础色，再检查22/25的区域，最后回到0。缺少模型或桥接类型时，先完成[渲染输入连接](../reference/dependencies.md)，不要把代码文件复制进空工程后直接调参。''')

add('01','''先固定观察条件。相机距离、光照、色彩空间或曝光同时改变时，很难判断明暗和颜色究竟由哪个参数造成。''',
'''使用透视相机、白色Directional Light和已有角色。环境光参与漫反射之外的合成；示例环境模式为Skybox、强度1，fog关闭。天空/赤道/地面色为(0.212,0.227,0.259)、(0.114,0.125,0.133)、(0.047,0.043,0.035)，但实际环境还取决于Skybox材质，不能只抄这三组颜色代替天空盒。

`BridgetImitateProfile`需要显式连接character和additional Renderer，使用已有root计算原点和启用时高度。它会设置MSAA=4、shadowDistance=20、Shadows=All、分辨率High。''',
'''1. 在Project Settings > Player把Color Space设为Linear；在Graphics和Quality中确认没有SRP Asset。
2. 将主相机设为Perspective、FOV=54、Near/Far=0.3/1000。示例位置为(-0.113,0.903,1.822)，旋转四元数为(0.0007041147,0.9988944,-0.015900236,0.044234328)。先按自己的模型尺度正确取景，四元数不能填进Inspector的Euler三格。
3. 把主方向光设为白色、Intensity=1.1。示例旋转四元数为(0.07075682,0.8591888,-0.12371239,0.49140963)；平行光的方向由旋转决定，移动位置不会改变方向。
4. 固定输出分辨率、背景和后处理。相机配置基准允许HDR/MSAA，质量档为4×MSAA；文中1600×900对照图使用HDR关闭、相机MSAA关闭和单采样RT，读图时不要混淆两种条件。
5. 在`BridgetImitateProfile`中填写角色引用；固定一张Debug0基准图，再开始连接贴图。''',
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
'''1. 在主体材质上连接`_MainTex`（Base）、`_ShadowMap`（Sss）、`_LightMap`（ILM）、`_DetailMap`和`_OutlineMap`（OLM）。Base/Sss/OLM的RGB使用sRGB；ILM/Detail保留线性数据。
2. 为自己的UV准备`_RegionalMask`：R为皮肤、G为白袖。连接`_FourMaterialSpecMask`：RGBA依次为头发、布料、皮肤、金属；关闭sRGB和Alpha Is Transparency，保留Alpha通道。
3. 按逐张导入表设置MipMap、Filter、Wrap和压缩。平台overridden未启用时，不要把该条textureFormat当作生效值。先避免有损压缩破坏窄区域，再观察缩小时的表现。
4. 依次观察Debug1/2/3（Base/Sss/Detail）、4–7（ILM RGBA）、8（顶点R）、9（法线）、22/25（区域/类别）。检查完恢复0。
5. 换模型时重新标定眼睛、胸前衣料和腿部区域。相同贴图分辨率不代表相同UV布局，不能直接复制这些坐标常量。''',
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
'''1. 逐个确认角色Renderer的材质槽和submesh，复制练习材质后选择`GGST/BridgetToonStudy`，按上一节填写纹理。
2. 保留四主体差异：Base/Secondary/Flip的Detail为0.278，Coat为0；Base/Secondary/Coat外轮廓宽0.8，Flip为0。剔除和其他差异从参数参考查对应材质，不要全部覆盖成Base。
3. 在现有渲染连接层中接入`GGSTRegionalShading`：body写_RegionalHead=0，standingHead写1；strength=1时写_RegionalEnabled=1。脸原点、横轴、宽度和有效位从已有头部Transform读取。
4. 写MPB前先GetPropertyBlock，设置自己的字段后再SetPropertyBlock，保留其他组件的数据。_RegionalEnabled的材质保存值0不代表运行分区关闭。
5. 用Debug22区分脸、身体皮肤和白袖，再用38看CleanShade覆盖。恢复Debug0后继续设置投影输入。''',
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
'''1. 打开`BridgetToon.shader`，从frag入口向下追踪diffuse、spec、rim、ink，先找到各变量的最后一次写入。
2. 按下面的顺序阅读：贴图/基础信号→区域→Palette→CleanShade→FocusedShade→眼睛漫反射→ambient/spec/rim→内部线→原眼睛白点→最终输出。
3. 修改一个效果时选择对应Debug：16看最终漫反射，13看最终spec，12看rim，30/31看内线，0看完整画面与外轮廓。
4. 一次只切一个开关。若基础诊断改变而最终输出不变，沿着后面的替换分支找原因，不要同时提高多个强度。
5. 继续到投影设置，完成深度输入后再逐层搭建主体颜色。''',
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
'''1. 先用Debug1、5、8分别检查基础色、ILM.G、顶点R。制作单独练习材质，隔离基础两段式时明确关闭哪些后续重建分支。
2. 固定主光，使用Debug10观察band。先把_LightTreshold设为0.5，增大它应减少亮面；恢复后再调整_RampOffset。
3. 单独调整_RampMaskStrength，观察分界是否跟随ILM.G改变。再调整_AOStrength，确认顶点R对信号的作用。
4. 从_ShadowSoftness=0.008开始控制边缘。先保持窄边界，不要用宽渐变掩盖区域遮罩错误。
5. 恢复CleanShade等目标开关，使用Debug16看最终漫反射，再回0判断完整画面。''',
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
'''1. 在头和身体Renderer上确认head=1/0。用Debug22检查脸、身体皮肤和白袖的分区，避免共享材质导致头体走错分支。
2. 打开_CleanShadeEnabled，用38看覆盖，再用16看明暗。保持Palette、高光和rim不变，先整理脸下颌与衣料的大形。
3. 调整_CleanFaceUnderStart/End控制脸的下暗面；这里看的是世界n.y，不要把_FaceDiffuseBoundary当作该分支的主要控制。脸的阴色起点仍受_FaceDiffuseTint/Depth影响，再由Palette调色。
4. 身体皮肤用_SkinShadeThreshold，白袖用_SleeveShadeThreshold。对衣料从_CleanClothMaskWeight=0.4、AOWeight=0.25、Softness=0.018开始，减少细碎信号；先修覆盖，再调权重和各区阴色。
5. 打开_FocusedShadeEnabled，用41检查腿、42检查胸前衣料。分别调整大腿/小腿/膝/衣料阈值，确认目标域外没有改变。''',
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
'''1. 固定CleanShade/Focused和主光，用Debug37确认皮肤、白袖和胸前衣料范围。
2. 输出16，在_PaletteEnabled=0/1之间比较同姿态。先确认改变的是色调，不是区域位置。
3. 分别调整一个区域的Light或Dark向量。先观察该区域的亮面与阴面，再回0看整体。
4. 如果只想改变皮肤，不要调全局灯色；如果向量影响了头发，先修区域门控。
5. 换UV后重新定位胸前区域，再重复局部调色。''',
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
'''1. 在GGSTGeometryShadowMaps接入p、mainCamera、lightSource、hairMask和depthShader。先确认Ready、Renderer可见状态、draw count和全局纹理有效，再看影子形状。
2. 为地面、墙面设置GGST/StageShadowReceiver材质。地面floor/bias/filter/fade使用0.08/0.0007/0.65/0.12；墙面使用0.1/0.001/0.8/0.08。floor是最低可见率，不是最终屏幕颜色。
3. 固定姿态，只把一个接收Renderer的_GeometryShadowFloor设为1：该面自定义接收衰减应消失，另一面和角色明暗保留。分别恢复地面0.08、墙面0.1。
4. 单独切drawStageCasters时，要知道enable=0会回退Unity的SHADOW_ATTENUATION，这个对照不等于“全部投影关闭”。
5. 检查投脸时同时观察_FaceFrameValid、脸域、_HairFaceShadowStrength及CleanShade。固定其他分支后再调bias/filter，不要把Debug32直接当最终脸部阴影。''',
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
'''1. 用Debug25检查分类。R/G/B显示三类，金属A被合成白色显示；这不是原始RGBA逐通道查看，需留意通道重叠。
2. 固定光和相机，使用13看最终spec，再用26–29理解基础分类形状。
3. 先调一类Strength，再调Width或Power：头发先看亮带与ILM.B细节，布料保持柔而弱，皮肤避免大片发白，金属保留明显亮芯。
4. 保持漫反射不动，切_FocusedSpecEnabled比较最终高光。FocusedHair/Cloth/MetalGain是该分支的倍率，不要只调基础强度。
5. 回0确认墨线仍清楚，眼睛没有被错误分类覆盖；大腿亮块单独按下一节处理。''',
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
'''1. 先用22确认身体皮肤、25确认皮肤类别，再用40看目标腿域。
2. 用43看替换域，44看亮形×朝向。它们没有乘_ThighLobeEnabled，所以非黑不能证明最终开关打开。
3. 固定姿态和FocusedSpec=1，在_ThighLobeEnabled=0/1之间比较Debug13及最终0。先判断亮块是否在正确表面，替换域是否越过膝盖。
4. 形状正确后，从Strength=0.16和Tint=(0.92,1,0.45,1)开始调整，保持光照和Palette不动。
5. 播放已有站立循环，逐姿态确认亮块范围与下端，异常时暂停回到13/43/44排查。''',
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
'''1. 固定分辨率与相机，回Debug0。设置_OutlineWidth，保留BodyBaseFlip=0，其他主体以0.8作为示例基宽。
2. 若模型的TANGENT只是标准切线，在练习材质关闭_UseSmoothOutline，使用几何法线观察；这不等同于已经有平滑描边数据。
3. 调_LineContourWidths的发/布/皮/金属比例，再调墨色。不要同时改全局基宽和四类比例。
4. 用7看ILM.A，用30/31看内部覆盖和墨色，调整_LineInnerFilter与_LineInnerStrengths。不要模糊ILM的RGB来柔化线条。
5. 回0比较_OutlineWidth=0与基准宽度：只应取消外壳，内部线仍保留。最后在已有站立循环中检查细线和轮廓。''',
'''外轮廓是Cull Front反向壳Pass。屏幕外扩的裁剪坐标增量为`direction*(2*width/_ScreenParams.xy)*clip.w`，width是像素尺度。分类比例由_LineContourWidths/0.8参与；零宽层保持零宽。

内部线覆盖率为`1-saturate(ILM.A)`，只对Alpha做中心加四邻域的屏幕足迹过滤，ILM.RGB仍原样采样。连续覆盖率有助于缩小时保留细线。

线条在diffuse+ambient+rim+spec合成后覆盖；眼睛原白点恢复在内线之后。Debug非0时OUTLINE被裁掉，因此31只能检查内部线，不能检查外轮廓。''',
'''刺出的轮廓：查TANGENT语义。材质交界过粗：查分类、基宽和零宽层。Debug图没有外轮廓：先回0。关了外描边仍有黑线：这是内部线，继续查ILM.A。

4K累计示意把轮廓像素宽度放大两倍，不能把其1.6宽度直接写回基准材质。比较不同分辨率前，先确定要保持的是像素宽度还是屏幕占比；在自己的目标设备和抗锯齿条件下观察细线，不以网页缩放代替Unity画面判断。''',
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
'''1. 确认头Renderer的_RegionalHead=1。打开33，查看R虹膜/G眼白/B原白点，先排除兜帽、眼线等误选。
2. 固定姿态和近景，在_EyeRefineEnabled=0/1间比较Debug0。再用34看代码中的眼睛贡献，不用其亮度直接判断最终增亮量。
3. 先调_EyeIrisUpperDepth和_EyeIrisLowerLift，保留黑瞳；再调EdgeDepth，避免虹膜边缘变成硬描圈。
4. 调CatchlightLift时只让已有白点更清晰，不增加随时间移动的新点；ScleraShade只轻微压低眼白。
5. 保留已有HeadGlow/HeadDecal的材质槽。播放站立循环，暂停在眼形和朝向不同的位置，重复33与0的检查。''',
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
'''1. 切Debug12，确认亮带靠近轮廓，而不是正面高光中心。
2. 切_ReferenceRimEnabled比较分类区和后备区。分类区主要调_ReferenceRimWidth，不是_RimWidth。
3. 从Width=0.24开始调覆盖，再调Strength=0.5和TintMix=0.75；不要同时改背景颜色。
4. 检查阴面是否适量保留亮边。脸应明显弱于头发和衣料；若脸一样亮，检查脸域和FaceScale。
5. 回0确认墨线仍清楚，最后在站立循环中观察亮带是否随法线和视角合理变化。''',
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
'''1. 固定一个姿态，按1/4–9看输入，22/25/38看区域，16看漫反射，13看spec，12看rim，31看内部线，最后回0看外轮廓与完整颜色。
2. 播放完整站立循环并重复观察。重点看墙/地影子是否跟上角色、眼睛是否串区、大腿亮形是否越膝、外壳和内部细线是否突然断裂。
3. 遇到问题先暂停在同一姿态。只切一个相关开关，比较对应Debug分量，定位最后写入分支。
4. 如果仅第一次出现的姿态异常、下一帧恢复，先检查坐标/深度更新和原生蒙皮流的时序。读取画面应在正常主相机渲染结束后，不能在一次更新里反复手动Render后假定姿态已经刷新。
5. 再检查cell切换及回绕。Step动画本来就会离散换姿态，整幅图不同不等于Shader闪烁；要结合表面位置、阴影和分量一起判断。''',
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
