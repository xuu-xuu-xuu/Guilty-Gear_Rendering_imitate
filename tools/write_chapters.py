"""Authorial chapter text plus mechanically extracted, checked facts."""
import json
from pathlib import Path
from prepare_reference import ROOT, PACK, REF, rows, write, table

CHAPTERS = {}

def chapter(number, principle, inputs, steps, verify, interaction, prefixes, excerpts):
    CHAPTERS[number] = dict(principle=principle, inputs=inputs, steps=steps, verify=verify,
                           interaction=interaction, prefixes=prefixes.split(), excerpts=excerpts)

chapter('00', '''画面首先要读得出角色，再读得出材质。当前实现将连续受光压成清楚的明暗块，以独立遮罩控制皮肤、衣料、头发和金属，最后用内部墨线与屏幕像素描边组织轮廓。它是针对当前模型、图集和参考光照制作的美术近似，不宣称恢复原游戏内部算法。

“复刻”在这里指理解当前项目如何产生这种画面：两段式明暗解决体积概括，分区与 Palette 解决脸和衣料的可读性，材质高光及大腿局部亮块补充质感，眼睛、rim 与线条完成层次。读者已有能正常站立循环的模型和动画；教程不涉及解包、骨骼修复、动画移植、Bind Pose 或控制器重建。

先认识三个证据层：源码说明计算；磁盘保存值说明起点；历史截图说明曾经得到的画面。三者结合仍不等于今天在新环境重新运行过。''',
'''已有角色 Renderer、正常播放的站立动画、自有纹理及 UV 是练习前提。本包只含渲染源码快照、接口数值、截图与历史报告，没有模型、贴图像素（包括自制遮罩）或 Unity 场景。

主体为 Built-in 的 Opaque Shader，颜色输出 Alpha=1；同一视觉结果由材质参数、Renderer 的 MaterialPropertyBlock（MPB，逐渲染器属性覆盖）和全局阴影纹理共同决定。各类型不可互换：Vector 是计算乘数或坐标，Color 是颜色参数，屏幕取色还受到采样、光照和显示转换影响。''',
'''1. 从独立练习工程开始，保留自己的已有动画；记录相机、主光、分辨率和资源版本，不修改原资料包。
2. 先读 01–04，建立环境、纹理、材质和执行顺序；不要直接复制三个 C# 脚本并期待零依赖编译。
3. 依次练习 05–13，每次只改变一个可解释的效果开关，保存自己的对照图。
4. 按 14 章进行静态分层及站立循环检查；将未完成项保留为待补，而不是用历史通过替代。''',
'''先将原工程历史最终画面与无投影的 4K 副本当作两种展示条件阅读。两图构图、投影和线宽不同，不能据差异计算某个参数的效果。后续独立练习需要自己建立同镜头、同姿势、同资源的比较集。

常见错误是以“模型看起来像”替代参数和输入核对，或以网站构建通过宣称渲染复刻通过。本次只检查文档，不启动 Unity。待补：全新工程中的编译、资源连接与渲染验收。''',
'''学习顺序是问题驱动；真实执行顺序见 04。所有章节均受 02 的数据契约和 03 的运行覆盖约束。主要开关在四主体材质均保存为 1，但 Shader 默认大多为 0，不能把“新建同名材质”视为现有最终配置。''',
'_CleanShadeEnabled _FocusedShadeEnabled _FocusedSpecEnabled _PaletteEnabled _FourMaterialSpecEnabled _ThighLobeEnabled _ReferenceRimEnabled', [('BridgetToon.shader',189,203)])

chapter('01', '''如果光照、色彩空间与构图随时改变，任何“阴影偏红”或“线太细”的判断都会失去基准。先固定观察条件，再调 Shader。当前快照是 Unity 2022.3.62f3c1、Built-in、Linear；GraphicsSettings 与所有质量档的 SRP 引用为空，不能在 URP/HDRP 中直接照搬 ForwardBase 与 UnityCG 宏。

主相机为透视 FOV 54，位置 (-0.113, 0.903, 1.822)，近远裁剪 0.3/1000，HDR 与 MSAA 开。相机四元数为 (0.0007041147, 0.9988944, -0.015900236, 0.044234328)。方向光白色、Intensity=1.1，旋转四元数为 (0.07075682, 0.8591888, -0.12371239, 0.49140963)；方向光的方向取决于旋转，移动位置不会改变其平行光方向。

Linear 表示颜色纹理经过 sRGB 解码后参与运算；数据遮罩需保持线性数值。不要为压暗结果随意把 ILM 打开 sRGB，那会同时移动阈值与分类。Shader 的 _LightIntensity=0.9 与灯光 Intensity=1.1 是不同层，不能合称同一个亮度参数。''',
'''数据来源为 environment.json 的 colorSpace、unityVersion、GraphicsSettings.asset、QualitySettings.asset，以及 saved_scene_rendering.json 的 cameras、lights、renderSettings、renderingComponents。

保存的环境模式是 Skybox、强度 1；天空/赤道/地面色分别为 (0.212,0.227,0.259)、(0.114,0.125,0.133)、(0.047,0.043,0.035)，fog=0。Skybox 只有引用，像素与材质资源未随包提供；不能只抄这三组颜色就承诺同图。ambient 实际由 UNITY_LIGHTMODEL_AMBIENT × albedo × _AmbientStrength 加入。

BridgetImitateProfile 的活动写入为 MSAA=4、shadowDistance=20、All/High；OnDisable 恢复质量。它根据已有 Renderer 的 rootBone（缺省用 transform）和启用时 bounds 得到角色高度/原点，再写 MPB。动态原点不能当固定 (0,0,0)。''',
'''1. 创建独立 Built-in 练习工程，先在 Project Settings > Player 将 Color Space 设为 Linear，在 Graphics 与 Quality 确认没有 SRP Asset。
2. 接入自己已有可正常播放的角色，固定站立姿势。创建透视相机与白色 Directional Light；先按上述 FOV、强度设置，再根据自己模型尺度取景。四元数是源场景记录，不应粘贴到 Inspector 的 Euler 三格中。
3. 在相机允许 MSAA，并在当前质量档设 4×；固定预览分辨率、背景及环境光。记录 HDR 开关，关闭练习中额外引入且未记录的曝光或后处理变化。
4. 按附录的接口表准备 Renderer 与 root/头部引用。Profile 可单独阅读，但在自己的场景应显式连接 character/additional；不要依靠名字回退误选另一角色。
5. 保存配置和一张无 Debug 基准图，再进入贴图检查。''',
'''检查 1/16/17 号 Debug：1 看基础色采样，16 隔离漫反射，17 把合成颜色达到 1 的像素标红。17 是表达式阈值诊断，不是校准过的显示曝光计。先排除环境或额外灯光变化，再判断材质颜色。

若整图灰白，检查色彩空间、颜色纹理 sRGB、ambient 和后处理；若只阴影错，检查数据纹理与覆盖分支。图中只有最终效果展示，缺环境参数的同条件独立 A/B，待补该实验。本次未验证设备对 4× MSAA 的实际支持或编辑器未保存状态。''',
'''环境光加在漫反射之外，Palette 不直接乘 ambient。相机距离影响像素覆盖和内部线过滤，分辨率影响外轮廓视觉比例；因此线条章必须使用同分辨率比较。4K 演示副本的投影矩阵与线宽临时改动不是本场景参数。''',
'_LightIntensity _AmbientStrength _CharacterOriginWS _CharacterHeight', [('BridgetImitateProfile.cs',20,30),('BridgetToon.shader',532,535)])

chapter('02', '''同一张 RGBA 纹理的四个通道可能保存四类数值，并不代表颜色加透明。Shader 把 ILM.R×255 用于旧分类、G 用于受光偏移、B 用于高光细节、A 用于内部墨线。误开 sRGB 或把 Alpha 当透明会破坏多条路径。

Base 的 RGB 是基础色，Sss 的 RGB 是阴面颜色。当前只是颜色插值，不是物理次表面散射。Detail 用第二套 UV 乘进 albedo：`albedo = base × lerp(1, detail, _DetailIntensity)`。OLM.RGB 控制描边墨色，不提供 Alpha 线宽。

RegionalMask.R/G 分别为皮肤/白袖；还要乘 _RegionalEnabled，并由 _RegionalHead 区分脸与身体。FourMaterialSpecMask 的 RGBA 分别为头发、布料、皮肤、金属；A 是金属分类。它还控制 CleanShade 布料、高光、线条、rim，R 可作为头发深度 caster mask。它们不是包内可用的原图。''',
'''输入布局为 POSITION、NORMAL、COLOR、TEXCOORD0/1/2；UV0 是主图集，UV1 是 Detail（C# mesh.uv2），UV2 是可选镜像（mesh.uv3）。_UseMirroredUV 当前四主体保存为 0，主采样使用 UV0 并应用 _MainTex 的 Tiling/Offset；Detail 用 UV1，不能假定所有纹理各自 ST 都被使用。

COLOR.R 通过 lerp(1,saturate(vertex.r),_AOStrength) 控制明暗；Debug21 仅展示其余顶点分量。NORMAL 转到世界空间后参与受光，背面按 VFACE 翻转。OUTLINE 在 _UseSmoothOutline=1 时把 TANGENT.xyz 作为描边法线；普通切线不满足这一特殊契约。本次没有网格像素/通道样本来证明其内容。

完整的 11 张纹理绑定、压缩枚举、平台 overridden、MipMap、Bilinear、Repeat/Clamp 和 Alpha 字段见[导入表](../reference/texture-imports.md)。BGTW_ilm 现存 sRGB=1 是未显示武器预览的异常记录，保留事实，不作为数据纹理推荐值。''',
'''1. 在自己合法持有的资源上建立输入清单，按属性名连接 Base、Sss、ILM、Detail、OLM。资料包不提供这些纹理；没有对应像素时只能练习概念或用自己的素材验证，不可声称精确复现本图。
2. Base/Sss/OLM 按当前记录启用 sRGB；ILM/Detail/RegionalMask/分类图按记录关闭。分类图需要保留 RGBA 数据并关闭 Alpha Is Transparency。
3. 按导入附录逐张填写 MipMap、Wrap、压缩与平台覆盖，不给所有贴图套一个预设。分类图和分区图的窄边界尤其需要避免有损压缩造成串区。
4. 检查 UV0/UV1/UV2 的实际用途；CoatExterior 的 _DetailIntensity=0，不应为“看不到 Detail”错误重做 UV。
5. 在练习材质逐次设置 Debug1–9，再看22/25。确认通道职责后才开最终效果；恢复 Debug0。不要修改原快照的 _DebugMode 面板范围。''',
'''Debug1/2/3 分别看 Base/Sss/Detail；4–7 看 ILM RGBA；8 看顶点 R；9 看法线映射到 0–1 的颜色。它们是 Shader 采样诊断，不是原纹理导出。预期 ILM.A 的线在 1-A 后变成覆盖率，最终仍 Opaque。

阶段00仅展示基础色，不能替代缺失的通道诊断截图。待补：自己模型的 UV、顶点 R、TANGENT 合同检查及各通道 Debug 截图。换图集必须重做分区/分类遮罩，并重定眼睛、胸前衣料、大腿区域；只调整图片分辨率不等于移植完成。''',
'''G 的受光偏移影响基础 band 及部分分区，B 影响高光，A 影响墨线；统一模糊 RGBA 会让高光和线同时出错。当前内部线只对 Alpha 加屏幕足迹过滤，保留 ILM.RGB 原采样。切线合同只影响描边，不应为它修改现有动画或骨骼。''',
'_MainTex _ShadowMap _LightMap _DetailMap _OutlineMap _RegionalMask _FourMaterialSpecMask _UseMirroredUV _DetailIntensity _AOStrength _UseSmoothOutline', [('BridgetToon.shader',298,303),('BridgetToon.shader',310,319),('BridgetToon.shader',327,331)])

chapter('03', '''共享材质不等于共享所有逐物体参数。身体和头可以使用同一 Base 材质，但脚本把 body 的 _RegionalHead 写为 0、standingHead 写为 1，才使同一皮肤遮罩分别进入身体与脸部公式。

参数阅读分为五层：Properties 默认值 → 材质保存值 → Renderer MPB 或 Shader 全局输入 → 随姿态变化的动态坐标 → Shader 内部替换后的结果。MPB 是逐 Renderer 属性集，不会把保存材质的 _RegionalEnabled 从 0 改成 1；看 Inspector 上的 .mat 并不能判断运行分区是否打开。

GGSTRegionalShading 在 LateUpdate 读取现有头部 Transform 的矩阵，提取原点与第一轴，写入 _FaceOriginWS、_FaceRightWS 和有效位；它没有重建或修改动画。Profile 写入的是角色原点/高度，阴影脚本发布的是全局深度图和矩阵，不应在材质参数表给这些动态数据填写伪常数。''',
'''四主体为 Base_Imitate、BaseSecondary_Imitate、BodyBaseFlip_Imitate、CoatExterior_Imitate。按保存场景，站立头 0/1 槽为 Base/BaseSecondary，2/3 为 ShadowGeometryParked；身体 Prefab 覆盖的 0–7 槽依次是 Base、BaseSecondary、BodyBaseFlip、BodyDecal、HeadDecal、HeadGlow、ShadowGeometryParked、CoatExterior。身体槽来自 Prefab override，不能冒充当前完整实例解析。

GgstDecal 是 X2 Multiply 贴花（Blend DstColor SrcColor，中性输入0.5），GgstGlow 是基础色输出，GgstShadowParked 禁用旧辅助几何绘制；它们不是主体材质的等价替代。历史完整 Renderer 列表仅用于交叉核对，enabled 字段也不能单独证明 activeInHierarchy 为真。

原始 Regional 脚本还依赖未打包的 UEOriginalPersistentPresentation.groups；阴影脚本依赖 UEOriginalActionPlayer.nativeRendering。没有这些类型，不能宣称脚本直接可编译。附录给出仅接受已有对象引用的接口约定，本教程不提供未经验证的全功能适配器。''',
'''1. 在独立工程记录每个已有 Renderer 的材质槽与 submesh 对应，复制练习材质；不要把全部槽批量替成 Base。
2. 对照参数账本的四主体差异，先设置纹理、剔除、Detail 与轮廓宽度。辅助槽按各自 Shader 单独处理。
3. 准备渲染连接层：已有身体与站立头 Renderer、只读头部 Transform、根 Transform；按覆盖附录写入/检查 MPB 时先 GetPropertyBlock，保留其他写入者的字段。
4. 若尚无连接层，明确标记运行覆盖未接入；只在练习副本静态设置 _RegionalEnabled=1，并分别验证头/体，不能把这一简化称为原工程运行路径。
5. 用 Debug22 看 R脸/G身体皮肤/B白袖，随后看38。结束后恢复 Debug0，检查禁用连接层时的还原行为。''',
'''若头与身体 Debug22 同色，优先查 _RegionalHead 的逐 Renderer 覆盖；如果全黑，查 strength、引用、贴图和 _RegionalEnabled。共享材质时不要靠修改全局 .mat 值去区分头体。

本章配图是 Debug38 的 CleanShade 覆盖，只能说明该阶段区域，不能当作 Debug22 截图。待补：运行中 MPB 采样、Debug22 实图、独立适配器编译验证。Profile OnDisable 只恢复主 character 的整块旧 MPB，additional 未逐个备份恢复；多个写入者禁用顺序也需独立工程检查，不能假定生命周期完全无副作用。''',
'''分区启用决定 Palette/CleanShade 的区域，分类图还影响线宽和材质高光。BodyBaseFlip 轮廓宽度0必须保持0。修改脚本执行或覆盖粒度时，需同时检查 Profile、Regional 与阴影的读取时序。''',
'_RegionalEnabled _RegionalHead _FaceFrameValid _FaceOriginWS _FaceRightWS _OutlineWidth _DetailIntensity _EyeRefineEnabled _FaceDiffuseRefine _HairFaceShadowStrength', [('GGSTRegionalShading.cs',56,66),('BridgetImitateProfile.cs',31,43)])

chapter('04', '''按教程逐层观察，便于理解；GPU 的计算顺序却由代码定义。如果后一个分支重算 diffuse，前一个脸部调参看似有效的中间量可能不会进入最终颜色。不能因为变量在代码前半部出现，就认定它主导最后画面。

FORWARD/ForwardBase 负责主体颜色，OUTLINE/Always 是独立外轮廓 Pass，SHADOWCASTER 是由 Unity 阴影阶段调用的 Pass。文件排列不是一条“颜色完成以后再投影”的逐句执行链。主体 frag 的有序结果为：

1. 321–401：法线/视线、贴图与眼区门控、旧分类、相对高度、旧 band 和阴面。
2. 405–458：分区、脸侧面、早期投脸与旧 FaceDiffuse 修正。
3. 461–476：Palette 乘早期 diffuse；479–501：CleanShade 在覆盖区重建 diffuse，并把 Palette 乘数重新纳入，不是再乘一遍早期结果。
4. 507–518：Focused 以差值替换腿/胸前衣料漫反射；521–529：眼睛漫反射细化。
5. 532–567：ambient、后备 rim、后备及四材质高光；572–609：Focused/ThighLobe 替换高光。
6. 616–623：ReferenceRim 替换分类区的 rim；625 合成 diffuse+ambient+rim+spec。
7. 630–652：内部线覆盖颜色；655–657：恢复原有眼睛白高光清晰度；660–725：Debug 或最终输出。

这解释三个重要现象：Debug10 的 band 没有随着 CleanShade 变成最终漫反射；早期 faceDiffuseDelta/HairFaceOcclusion 非零不代表最终脸上仍有同样暗带；ThighLobe 必须经过 FocusedSpec 的差值合成才进入 spec。''',
'''主体代码使用 UnityCG/Lighting/AutoLight 的 Built-in 输入，_MainTex 等采样和 Renderer MPB、全局 _HairShadow* 是不同来源。纹理、UV 与顶点合同见02，运行覆盖见03与附录。

Properties 的 _DebugMode 仍为 Range(0,24)，frag 将 _DebugMode+0.5 转 int 并支持1–44。教程保留这一不一致，不修改源码面板。属性名 _LightTreshold 原文如此，不能改成拼写更规范却不存在的属性。''',
'''1. 先读逐行索引的 FORWARD 名称、vertex 输入和 frag 入口，再按上面的分段标注变量写入点。
2. 在练习副本中保持最终保存开关，依次观察 Debug16、13、12、31；每次保存当前 Debug 编号及参数记录。
3. 只关闭一个效果开关，比较同一输出分量。例如检查 CleanShade 用16，检查 ThighLobe 用13，检查轮廓回到0。
4. 在记录中为 diffuse/spec/rim/ink 各写一列“最后写入位置”，再解释最终色。不要用中间诊断代替最终贡献。
5. 恢复全部练习开关；不要用阶段图反推每个临时材质值，包内没有完整逐阶段临时配置。''',
'''正确的排查应能指出最后一层覆盖。最终分类区 rim 看 _ReferenceRim*；最终腿部高光看 Focused 与 Thigh，而非只看 _SpecularPower。19/20 的 taste/regional 诊断明确未接入最终颜色。

阶段08是完整累计示意，不证明执行顺序；顺序证据来自代码。待补：同条件逐开关分量对照和 Unity Frame Debugger 捕获；本次没有执行 GPU 或编译 Shader。''',
'''CleanShade=1 只在 cleanCoverage 内替换，不删除全画面后备；FocusedShade 在此基础上用差值改局部；FocusedSpec 的受光带重算可绕过旧投影 band；ReferenceRim 仍用旧 band 的 shadow floor。内部线最终压在高光/rim 之上，眼睛原白点恢复在墨线之后。''',
'_CleanShadeEnabled _FocusedShadeEnabled _FocusedSpecEnabled _ThighLobeEnabled _ReferenceRimEnabled _DebugMode', [('BridgetToon.shader',495,501),('BridgetToon.shader',605,609),('BridgetToon.shader',620,625)])

chapter('05', '''连续的 Lambert 明暗会把模型每个小凹凸都展示出来，容易产生灰、碎、脏的观感。两段式把受光信号压缩为亮面与阴面，只在阈值附近保留窄过渡。

当前源码先用半兰伯特 `nl = dot(n,l) × 0.5 + 0.5` 把方向点积从 [-1,1] 映射到 [0,1]。这里 n/l 是单位世界法线与光方向；“半兰伯特”只是经验信号，不表示物理能量模型。随后：

```text
ao = lerp(1, saturate(vertex.r), _AOStrength)
signal = (nl + _RampOffset + (ILM.G-_RampMaskCenter)*_RampMaskStrength
          + skin*_SkinShadowOffset) * ao
band = smoothstep(_LightTreshold-soft, _LightTreshold+soft, signal)
```

上式是对应391–394行的数学重述，不是完整可编译 Shader，未作独立运行验证；省略了较早的下半身光向混合与较后的投影、分区、CleanShade。smoothstep 的结果由0平滑到1，soft 越小越接近硬切。ILM.G 是信号偏移，不能简单称为乘在整图上的 AO。

旧路径 `dark=lerp(albedo, Sss×_ShadowTint, _ShadowIntensity)`，再以 band 混合亮暗。_LightTreshold=0.5、soft=0.008 是基础值，最终脸/皮肤/衣料另有阈值，不能把全图调节都归给这一项。''',
'''Base、Sss、ILM、Detail、NORMAL 与 COLOR.R；旧 skin 分类来自 ILM.R。当前 _RampMaskCenter 保存为0.49803922（声明默认0.4980392），_AOStrength=1。_LowerLightBlend=0.8 但 _LowerLightDynamic=1，源码会把 lowerLight 混到当前主光，不能仅凭保存的 _LowerLightDirection 断言固定下补光仍在主导。

_SecondShadowStrength=0.9 是旧二级阴面保存值，但后续分区与 CleanShade 会替换相应 diffuse；它不是最终皮肤色的唯一来源。_ReceiveShadowStrength=0.7 只用于旧 band 的 Unity 投影路径。''',
'''1. 先在练习副本验证 Base/Sss/ILM.G/顶点R，不接分区与分类新效果的隔离试验必须单独复制材质并记录关闭项。
2. 固定光照，输出 Debug10，看旧 band 在模型上由黑到白的分界。改变 _LightTreshold 时，阈值升高应使达到亮面的区域减少。
3. 恢复0.5，分别改变 _RampMaskStrength 与 _AOStrength，确认是纹理/顶点信号影响，而非几何法线变了。
4. 从小范围调整 _ShadowSoftness，检查过渡宽度；不要用很宽的渐变代替后续分区问题。
5. 恢复最终开关，输出 Debug16，确认当前最终漫反射的分界；这一步比 Debug10 更接近最终视觉判断。''',
'''阶段00→01展示从基础色到基础两段式的累计变化，基础色阶段同时移除了其他光照贡献；不能称为只改 _LightTreshold 的实验。

若表面碎影跟纹理走，查 G、顶点 R 和阈值；若随视角跳变，查法线与背面；若10合理而16不同，沿04检查分区替换。待补：最终材质下 Debug10/16 同姿势并排图，以及阈值单变量实验。''',
'''基础 band 仍给后备高光、部分诊断和 ReferenceRim 的受光权重使用。后续漫反射重建不等于重写所有 band，因此不能假定高光和最终漫反射始终共用同一明暗边界。''',
'_LightTreshold _RampOffset _RampMaskCenter _RampMaskStrength _ShadowSoftness _ShadowIntensity _ShadowTint _SkinShadowOffset _AOStrength _ReceiveShadowStrength _LowerLightBlend _LowerLightDynamic _LowerLightDirection _SecondShadow', [('BridgetToon.shader',386,401)])

chapter('06', '''脸上多余的暗带、腹部碎影和白袖发灰，通常不能只靠一个全局阈值解决。当前实现先用独立皮肤/白袖遮罩与头体标志划分区域，再用 CleanShade 重建简洁明暗，用 Focused 调整胸前衣料及腿部阈值。

早期 region.r×head 为脸，region.r×(1-head) 为身体皮肤，region.g×(1-head) 为白袖。旧 faceBand 还有光向选择远侧脸的逻辑与 _FaceDiffuse* 差值，但最终 CleanShade 覆盖脸时主要采用 `smoothstep(_CleanFaceUnderStart,_CleanFaceUnderEnd,n.y)`。这是世界法线向下时的简化下颌暗面，并不是通用脸部 SDF 或随脸部局部轴旋转的物理阴影。

CleanClothSignal 将 ILM.G 权重降至 _CleanClothMaskWeight=0.4，AO 权重降至0.25，softness=0.018，目的是降低小碎片而保留较大面转折。身体皮肤保留 skinBand，胸前衣料由专用 UV 域进入 tunicRegion。Focused 再将腿的阈值按图集位置在大腿0.57、小腿0.59、膝0.62之间切换；胸前衣料阈值0.4。它们是图集特定区域，不能称为自动识别解剖部位。''',
'''RegionalMask.R/G、FourMaterialSpecMask.G、ILM.G、顶点R、世界法线与 head MPB。CleanShade 里的 cleanOtherCloth 还要求 _FourMaterialSpecEnabled，并排除已覆盖的皮肤/袖/胸前衣料，防止重复计入。

胸前衣料像素域来自2048图集：上块 x=768.5…895.5/y=640.5…895.5，下块 x=512.5…895.5/y=895.5…1343.5；坐标 y=(1-v)×2048。腿域 x=200…510/y=880…1195。换模型时必须重新定位这些岛或用自己制作的区域遮罩替代教学练习逻辑，不能照抄坐标就认定通用。''',
'''1. 先按03把头/体 MPB 接正确，用22确认脸、身体皮肤、白袖互不串区。
2. 开 CleanShade，用38看覆盖，16看最终漫反射。保持 Palette 和材质高光不变，先判断明暗块是否连续；需要隔离时只在练习副本关闭高光并记录。
3. 以脸下颌为观察区，按 n.y 的 start/end 理解边界，不要继续把旧 _FaceDiffuseBoundary 当最终主要控制。
4. 用41检查腿、42检查胸前衣料的最终局部 band。调单个阈值时固定姿势，观察该域以外是否不受影响。
5. 换自己的图集时先重做区域合同，再谈数值微调；没有相应遮罩不要跳到审美判断。''',
'''38显示覆盖，不等于亮暗，也不等于22的头体分类；41/42显示局部受光信号。预期脸只保留简化下暗面，白袖与腹部减少细碎阴影，域外材质不被重着色。

shade_before/after 同时修改过阴影与高光；正文仅将其作为综合精修历史对照，不能归因于纯阴影。待补：CleanShade、Focused 各自的同条件独立开关图及站立中逐姿态脸下颌检查。''',
'''CleanShade 重新包含 Palette 乘数；Focused 用差值追加漫反射，只有 CleanShade 覆盖存在才生效。CleanShade 覆盖区会替换先前投脸和旧侧脸 diffuse，但旧 band 仍可能影响 rim 和后备高光；因此不能仅凭中间脸部 Debug 推断最终结果。''',
'_RegionalEnabled _RegionalHead _FaceShadeThreshold _SkinShadeThreshold _SleeveShadeThreshold _RegionalSoftness _Clean _FocusedShadeEnabled _FocusedTunicThreshold _FocusedThighThreshold _FocusedCalfThreshold _FocusedKneeThreshold _FaceDiffuse', [('BridgetToon.shader',405,410),('BridgetToon.shader',483,501),('BridgetToon.shader',507,518)])

chapter('07', '''同样的明暗分界，阴面可能偏脏、肤色可能过红、白袖也可能偏黄。Palette 把“在哪里变暗”和“亮暗各是什么色调”分开：用不同 RGB 乘数调整皮肤、白袖和胸前衣料的亮面/阴面。

在某区域内，乘数可直观写成 `M = lerp(M_dark, M_light, band)`；新漫反射约为原漫反射×M。此式只是局部解释，省略区域混合、CleanShade 重建与光照乘法，未作独立运行验证。不是 Color 参数的直接屏幕输出公式。

例如 _PaletteSkinLight=(0.92,1.10,1.28,0)，降低 R 相对比例并提高 G/B；_PaletteSkinDark=(0.82,0.70,0.82,0) 作用于已有阴面基色后，结果不能只凭该向量命名成某个 sRGB 色。它们在 Properties 中是 Vector，即便 JSON 采用 r/g/b/a 键保存，也不等于 Unity Color 的颜色语义。

早期 Palette 只乘 diffuse，不改 albedo、band、ambient、spec、rim、ink。CleanShade 随后重建区域 diffuse，同时重新包含同一组 Palette 乘数；这是替换路径，不能在外面额外再乘一次。''',
'''输入为皮肤/袖遮罩、head、当前图集胸前域、基础/阴面颜色与分区受光。六个 _Palette*Light/Dark 均为 Vector，第四分量保存为0但公式只用 rgb；完整默认/保存差异见下表。

四主体 _PaletteEnabled=1。亮/暗乘数实际为：皮肤 (0.92,1.1,1.28)/(0.82,0.7,0.82)，白袖 (0.99,1,1.07)/(0.9,0.93,1.02)，胸前衣料 (1,1.08,1.23)/(1.03,1.06,1.19)。这些不是贴图替代，也不直接改变线条颜色。''',
'''1. 在练习副本固定 CleanShade/Focused 和所有输入，先用37查看皮肤、袖、胸前区域。
2. 保存 Debug16 图，关闭 _PaletteEnabled，再保存同条件16图；这才是隔离配色贡献的实验。
3. 恢复 Palette，分别只调整一个区域的 Light 或 Dark 向量。先观察该区域的亮/阴面，再看整体是否仍协调。
4. 回 Debug0 检查高光、墨线和眼睛；不要因局部阴面偏色就调全局灯光白平衡。
5. 保留默认值、练习值和图像条件记录；换图集需重做胸前域，不能用肤色向量掩盖区域串色。''',
'''37仅显示区域，16是最终漫反射；0是完整合成。若调整皮肤影响头发，查遮罩与 head；若16变化但高光不跟着变，这是分量分工的预期，不能据此宣称参数失效。

阶段02→03是累计配色演示，不能推定所有独立参数开关。待补：最终版本下37和16的同条件 Palette 开关截图；没有显示取色或色彩仪测量证据。''',
'''皮肤原始阴色还受 _SkinShadeTint/Strength，脸受 _FaceDiffuseTint/Depth，布料阴色可来自 Sss。Palette 与上述项相乘或插值，影响彼此结果；ambient/rim/spec 独立合成可能让最终0模式比16更亮。''',
'_Palette _SkinShadeTint _SkinShadeStrength _SleeveShadeTint _SleeveShadeStrength _ShadowTint _ShadowIntensity', [('BridgetToon.shader',469,476),('BridgetToon.shader',494,501)])

chapter('08', '''头发投到脸上的阴影、角色自身明暗、角色投在地面/背景上的影子，是三条需要分别排查的路径。当前实现保留 Unity 内置 ShadowCaster/SHADOW_ATTENUATION，同时有自定义 RFloat 深度图：头发1024²，场景2048²。不要把其中一个开关称为“所有阴影开关”。

自定义深度图从光源方向看已有 Renderer，把位置沿光线投影后的归一化深度写入 R。接收点经 VP 矩阵投到同一贴图，比较自身深度与已存最近深度：接收点更靠后则受遮挡。Bias 是比较时的偏移，防止表面把自己误判成阴影；太大又会让影子悬空。3×3 邻域比较过滤只软化边缘，不提高深度图真实分辨率。

GGSTGeometryShadowMaps 在 onPreCull 构建命令，挂到 BeforeForwardOpaque 执行，理由是等原有蒙皮流可供 DrawRenderer 使用，再在主不透明绘制前发布纹理。它不是烘焙网格，也不改骨骼。Stage 中心在光空间按 texel 对齐以减少抖动；相机矩阵与渲染目标在命令末恢复。

脸上早期 hairFaceOcclusion=(1-visibility)×faceRegionMask×frameValid×strength，随后 diffuse 混向 faceDark。但 Base/BaseSecondary 的 strength 保存为0；另外两主体为0.75，仍需脸域和有效 frame。更关键是 CleanShade=1 在覆盖区重建 diffuse，可替换早期投脸贡献。因此 Debug32非黑也不能直接证明最终脸上存在同量投影。

地面/墙面由 StageShadowReceiver 独立接收 _StageShadowDepth。_StageShadowEnabled>0.5 时替换内置 atten；其距离衰减、边缘过滤、最低可见率不走角色 CleanShade。''',
'''必须有现有 Player/nativeRendering、同场景的主相机与方向光、实际可见的 Renderer、只读头/骨盆引用、分类图R作为 hairMask，以及 GGSTGeometryDepth Shader。Ready 还检查 RFloat 与 depthShader 支持；未就绪时关闭全局 enable，不能把白图当作“无阴影验证通过”。

当前保存：suspendMaps=0、drawHairCasters=1、drawStageCasters=1、hairRadius=0.28、hairRange=1.2、hairWorldUpOffset=0.08、stageRadius=2、stageRange=8。深度 RT 为 Point/Clamp/无 MipMap/AA1，不能和材质图 Bilinear 的设置混淆。

接收面实际保存值来自 materials_saved.json / material_parameters.csv：

| 材质 | _GeometryShadowFloor | _GeometryShadowBias | _GeometryShadowFilter | _GeometryShadowFade | _GradientStrength | _Color（Color） |
|---|---|---|---|---|---|---|
| StageFloorReceiver | 0.08 | 0.0007 | 0.65 | 0.12 | 0 | (0.74509805,0.74509805,0.74509805,1) |
| StageWallReceiver | 0.1 | 0.001 | 0.8 | 0.08 | 0.31 | (0.7019608,0.7019608,0.7019608,1) |

另有名为 StageShadowReceiver 的保存材质，其 shader=null，仅保留未知引用和颜色，不能因名字相同便视为已解析的接收Shader。

深度 Shader 只在 hairOnly 路径按分类图R裁剪，不按 Base.A 或 ILM.A 做透明。Stage receiver 的精确保存值另见参数账本的 StageFloorReceiver/StageWallReceiver；声明默认是 floor0.10、bias0.001、filter0.8、fade0.08，不能无证据把默认写成所有场景材质保存值。''',
'''1. 在独立工程先完成02/03的 Renderer 与只读引用连接。原 Player 桥接类型未提供，不能直接挂快照脚本并宣称可运行；依赖未实现时本章实验标为待补。
2. 有相应渲染适配层后，先验证 Ready、当前帧记录、绘制计数及全局纹理尺寸，再检查影子外观；不要只看材质 strength。
3. 将头发与 Stage 两路开关分开记录。在固定姿势/相机下只切 drawStageCasters，查看接收面影子；回到角色漫反射看是否独立。
4. 若研究投脸，先在练习副本隔离 CleanShade 覆盖，再比较 _HairFaceShadowStrength；同时记录 frameValid 与脸遮罩，不能用已被替换的早期输出解释最终图。
5. 按米理解 bias，先调覆盖范围、近远范围和接收位置，再小幅调偏移/过滤。恢复原练习基线后进行站立循环检查。''',
'''本章仅配原工程 final 含投影效果图，不把无投影阶段图伪装为 OFF 图。待补：最终材质下、同相机同姿势的 Stage 开关 A/B、hair 深度/visibility、内置自阴影与 CleanShade 覆盖的独立对照。

影子错位先核矩阵/纹理坐标和 target 恢复；贴面黑斑查 bias；悬空查 bias 过大；投影截断查范围；跳动查记录时序与 texel 对齐。历史截图不含足够深度图诊断，不能确认每种设备都稳定。''',
'''_ReceiveShadowStrength 属于旧角色 band，_HairFaceShadowStrength 属于早期脸 diffuse，Stage receiver 独立控制背景。FocusedSpec 会重算不含旧 projected 的受光项，而 ReferenceRim 保留旧 band 的阴面权重。修改一条阴影路径后应分别观察16/13/12及接收面。''',
'_HairFaceShadow _ReceiveShadowStrength _CleanShadeEnabled', [('GGSTGeometryDepth.shader',38,46),('BridgetToon.shader',247,261),('StageShadowReceiver.shader',80,88)])

chapter('09', '''所有表面用同一个尖亮点，会让皮肤、布料和头发都像塑料。当前方案使用独立 RGBA 分类图，把高光的形状、颜色和强度分开控制：头发有较宽肩部及 ILM.B 画定亮芯，布料是低强度幂函数柔光，皮肤较弱，金属有明显亮芯。

核心方向量为 `nh=saturate(dot(n,normalize(l+v)))`，其中 l+v 的单位方向叫半程向量。较高幂次使亮区更集中；step/smoothstep 的阈值制造更明确的亮带。代码又用 fwidth（像素间信号变化的估计）决定最小过渡，降低硬阈值锯齿。

分类后的基础 spec 是四类 shine×对应遮罩的和，乘主光颜色和旧 band。未分类的眼睛/嘴唇等保留原有后备 spec，并非全图强制替换。ILM.B 是稀疏手绘细节，头发公式将弱底与局部亮芯分开，不能把它解释成整片金属度或粗糙度。

FocusedSpec 随后以新受光带替换分类贡献：它从原 signal 和整理后的 clean/focused 区域重算 focusedSpecBand，排除脸部皮肤的 focused 覆盖，再用 HairGain=1.25、ClothGain=1.2、MetalGain=1.05 和腿部皮肤专用宽亮带更新。ThighLobe 还会进一步替换大腿皮肤高光。因此 Debug26–29只展示基础分材质结果，最终高光必须看13。''',
'''FourMaterialSpecMask.R/G/B/A=发/布/皮/金属，ILM.B=高光细节，NORMAL、视线、主光方向、bodySkin/faceRegion 及 clean/focused band。保存的四主体 _FourMaterialSpecEnabled、_FocusedSpecEnabled 都为1。

基础强度/形状：头发0.12/宽0.1，布料0.035/幂12，皮肤0.028/幂28，金属0.38/宽0.1。FocusedSkinStrength=0.14、Width=0.22。它们都不是物理 BRDF 测量参数。颜色类型与具体值保留在下表，不要拿旧 _BodySpecular*、_HeadSpecular* 当最终分类区域主要旋钮。''',
'''1. 在练习副本先用25确认分类：R/G/B分别偏红/绿/蓝，金属A合到RGB显示白色。它不是原始RGBA逐通道图，也不证明类别没有重叠。
2. 固定相机、主光与姿势，输出13，看最终高光；再用26–29理解基础分类形状，避免把后者当最终。
3. 每次只调整一类的强度或宽度/幂次，先确认其余材质不变；分类串色时先修自己遮罩而非补参数。
4. 切 _FocusedSpecEnabled 进行同条件比较，尤其观察腿部和布料。保持 Palette 和 diffuse 开关不动。
5. 回0检查高光不会抹去内部线，确认眼睛原白点未被分类覆盖；需要追踪大腿亮块时进入10章。''',
'''预期布料较柔且弱、金属有亮芯、头发亮区含手绘细节、皮肤不整片发白。13是最后 spec；若26–29有光而13不同，先检查Focused/Thigh替换。若材质边界出现异常叠加，检查分类图通道重叠与压缩。

阶段03→04是材质高光累计展示，specular_debug 为历史Debug13。待补：最终版本下每类开关独立对照、当前分类图的原像素审计；本包没有原图，不可用自动生成遮罩冒充。''',
'''高光不由 Palette 直接着色，却受 albedo、主光和 band/区域信号影响。ThighLobe 与 FocusedSpec 在分类皮肤内合成；ReferenceRim 复用同一分类图但有独立亮度。内部线在合成以后叠加，改变墨线也会改变亮区的观感。''',
'_FourMaterialSpec _HairShine _ClothShine _SkinShine _MetalShine _FocusedSpecEnabled _FocusedSkin _FocusedHairGain _FocusedClothGain _FocusedMetalGain _SpecularPower _SpecularIntensity', [('BridgetToon.shader',548,567),('BridgetToon.shader',572,579),('BridgetToon.shader',605,609)])

chapter('10', '''大腿需要一块稳定、收尖、带浅金色倾向的局部亮形，而不是追着半程向量到处跑的普通点高光。当前实现以图集坐标定义亮块形状，再以视向和光向控制可见度。这是针对当前角色 UV 的艺术绘制式近似。

坐标为 p=(u×2048,(1-v)×2048)。腿域 x=200…510、y=880…1195；沿 y 的前侧中心不是直线：从357.89起分段修正，在 y≈981附近改变走向，以适应原图集环带。完整中心系数见583–594行，不应概括成“任何模型沿UV竖线即可”。

收尖由 `t=saturate((p.y-918)/82)`、`halfWidth=7.2*(1-pow(t,1.15))` 定义。横向距离减去半宽，再用 fwidth 自适应平滑得到 lobe；y≈916–1001限制亮块纵向。朝向门控为 smoothstep(0.2,0.55,nv)×smoothstep(0.50,0.68,nl)，这里 nl 是半兰伯特值，不是原始 N·L。

亮块值为 tint×strength×lobe×facing，但替换域 thighReplace 比亮块宽得多，并在 y1015–1030前收掉；域内旧腿部皮肤高光被替换，即使域中 lobe=0，也会清理旧散光。最后只有 _FocusedSpecEnabled 参与的分类皮肤差值才能把结果送入 spec；不能把 _ThighLobeEnabled 当完全独立的最终高光开关。''',
'''当前图集坐标、分类图B皮肤、bodySkinRegion、head=0、nv、nl、主光颜色与 focusedSpecBand。四主体 _ThighLobeEnabled=1、Strength=0.16、Tint 为 Color(0.92,1,0.45,1)。这是浅金方向的参数，不是屏幕像素RGB(0.92,1,0.45)。

四材质开关相同不代表头/衣服都会出现亮块，UV域、皮肤分类和头体门控共同限制。换UV需重新设计中心曲线、宽度、纵向窗口、替换范围及膝盖过渡；不得通过修改当前网格/Bind Pose 来迁就这一章。''',
'''1. 在练习副本先确认22的身体皮肤与25的皮肤分类；再看40是否只覆盖自己的目标腿域。换图集未适配时，先把本章标为待补。
2. 用43看替换域，44看亮形×朝向；注意这两个诊断公式没有乘 _ThighLobeEnabled，只用于看域，不是开关状态证明。
3. 固定姿势、FocusedSpec=1，切换 _ThighLobeEnabled，保存0和13的同条件对照。
4. 先核形状与膝盖边界，再调 strength/tint；不要用全局 SkinShineStrength 代替局部亮形控制。
5. 在站立循环中逐姿态检查前侧亮块是否黏在正确表面、下端是否越过膝盖；同时看视向/光向变化是否合理。''',
'''thigh_before/after 是清单明确标注的历史受控OFF/ON，允许并排展示；thigh_lobe_debug 是44，只显示几何域和朝向，不是最终颜色。阶段04→05为累计展示。

如果整腿出现色带，查替换域和分类；如果44有形而13没有，查开关、FocusedSpec、分类皮肤与光带；如果亮块扭曲，先查UV和中心曲线而非骨骼。待补：新UV模型实验、同条件不同光向/视角及站立逐姿态截图。''',
'''ThighLobe 替换 focusedSkinShine，FocusedSpec 再合并到 spec；两级路径都需理解。FocusedShade 影响腿部受光带，Palette 影响漫反射而非亮块 tint；墨线覆盖与rim也会改变局部对比。''',
'_ThighLobe _FocusedSpecEnabled _FocusedSkin _FocusedThighThreshold _FocusedCalfThreshold _FocusedKneeThreshold', [('BridgetToon.shader',583,603),('BridgetToon.shader',605,609)])

chapter('11', '''轮廓决定外形，内部线交代表面结构；两者需要独立控制。当前外轮廓是 Cull Front 的反向壳式 Pass，用屏幕方向外扩已有顶点；内部线则由 1-ILM.A 在完成光照后覆盖，不是几何边缘检测。

外扩先把描边法线转到世界/视图，结合投影矩阵和屏幕尺寸求单位像素方向。裁剪坐标增量为 `direction*(2*width/_ScreenParams.xy)*clip.w`，所以 width 表示屏幕像素尺度，不是世界米。材质分类再以 _LineContourWidths/0.8 缩放宽度，保留原宽度为0的层。

内部线 rawInk=1-saturate(ILM.A)。只对 Alpha 做中心加四邻域的屏幕足迹过滤，避免把 ILM.RGB 的受光/高光信号一并糊掉。refinedInk 由 _LineInnerFilter 混合；连续覆盖率保留缩小时的细线，不把数据 Alpha 当透明度。

最终先合成 diffuse+ambient+rim+spec，再按分类墨色和强度覆盖线；高光/rim因此不会简单抹掉墨线。未分类眼睛/嘴唇保留旧混合。OUTLINE 在 Debug>0.5 时被 clip，不能从 Debug31 推断外轮廓宽度。''',
'''OUTLINE 读 POSITION、NORMAL、TANGENT.xyz、UV0/UV2、ILM.R、OLM.RGB 和分类图；_UseSmoothOutline=1 把 TANGENT.xyz 当平滑描边法线，普通模型标准切线不能自动满足。

四主体保存宽度 Base/BaseSecondary/CoatExterior=0.8，BodyBaseFlip=0；分类宽度Vector=(0.82,0.95,0.6,0.72)，分类内线强度=(0.72,0.76,0.58,0.72)。4K副本将轮廓像素宽度×2是展示条件差异，不能覆盖主工程保存值。材质墨色类型为Color，具体记录见表。''',
'''1. 在独立工程先确认模型是否已有合约要求的 TANGENT 描边法线；若无证据，在练习副本关闭 _UseSmoothOutline 使用几何法线作为降级观察，记录不等价，不改原模型。
2. 回Debug0看外轮廓，固定1080p或自己的基准分辨率，确认BodyBaseFlip等零宽层仍不绘制。
3. 分别调整 _OutlineWidth 与 _LineContourWidths，记录全局基宽和材质比例，避免两个层级同时改后失去归因。
4. 切到7查看Alpha采样，再用30/31观察内线覆盖/墨色；调 _LineInnerFilter、分类强度，不改变ILM.RGB。
5. 恢复0，比较同分辨率近景与全身。额外分辨率测试须明确比较的是像素宽度还是屏占比例，不能混用。''',
'''预期脸部线较轻、衣料结构线清楚、零宽层不产生额外壳，缩小时细线尽量连续。若轮廓朝奇怪方向刺出，查TANGENT语义；若材质边界线过粗，查分类与基宽；若Debug没有外轮廓，这是源码预期。

阶段05→06为线条效果组累计变化；ink_debug是31的内部线展示。待补：TANGENT数值审计、分辨率同屏占对照和手机缩放可读性在Unity中的验证。网站手机排版检查不等于角色线条稳定性测试。''',
'''线条依赖分类图，OLM只参与墨色。Profile MSAA、相机距离、像素覆盖和压缩都会改变线观感。眼睛原白点恢复在线条之后，但不能据此把眼线误判为高光错误。''',
'_Line _Outline _InnerLine _UseSmoothOutline', [('BridgetToon.shader',635,652),('BridgetToon.shader',755,771),('BridgetToon.shader',774,789)])

chapter('12', '''眼睛只需小幅上暗下亮、边缘层次和原白点清晰度，过强会变成自发光贴纸。当前代码不生成时间驱动的闪点，不增加新的运动高光；高细节眼仍保留原有 HeadGlow/HeadDecal 辅助路径。

先把UV换成2048图集像素坐标。小虹膜中心(960,64)、半径(34,34)，大虹膜中心(1152,130)、半径(104,100)；瞳孔另有保护椭圆。EyeDisk 用长度阈值与 fwidth 平滑边缘；色度条件 min(base.g,base.b)-base.r 保护原青色虹膜，不把黑瞳/墨线/白点一起提亮。

眼白只在 x896…1280/y0…256域内，按接近(0.8388,0.8308,0.9301)的颜色选择；这些常量来自当前图集，不能当通用眼白识别器。eyeHead 还要求 _EyeRefineEnabled×_RegionalHead。

漫反射先压暗虹膜上部和外缘，再用原albedo与同一band提亮下部，稍调眼白。最后在内部线之后，将已有白高光向不低于 base×光色×强度的目标混合。原小眼白点中心(938.7075,48.0896)/(983.5789,85.5)，不会随视角产生新点。这些都是当前工程专用数据。''',
'''Base颜色、UV0或镜像选择后的主UV、_RegionalHead MPB、主光、band；无需新眼睛纹理，但已有图集像素未提供。Base/BaseSecondary 的 _EyeRefineEnabled=1，BodyBaseFlip/CoatExterior=0；还需 head=1 才进区域。

参数为 UpperDepth0.18、LowerLift0.1、EdgeDepth0.08、CatchlightLift0.25、ScleraShade0.06，均为强度范围量，不是眼睛最终屏幕亮度。换图集必须重定虹膜、瞳孔、眼白、原白点域与颜色门控；不能只扩大UV圈而保留原坐标。''',
'''1. 在练习副本先确认头Renderer的 _RegionalHead=1，打开33查看 R虹膜/G眼白/B原白点，判断是否误选眼线或兜帽。
2. 固定同一站立姿势与相机近景，输出34看差值，再回0看实际幅度。不能把差值的亮度当最终增亮幅度。
3. 在 _EyeRefineEnabled 开关之间保存同条件近景；优先保护黑瞳和眼线，再微调上部暗、下部亮。
4. 检查原白点只变清晰，没有新增漂移点；若辅助HeadGlow/Decal存在，保持其材质槽，不批量替换。
5. 换模型时先用自己的遮罩或重新定位数据构建练习方案，明确它是新适配，尚未经本工程验证。''',
'''eye_regions 是历史Debug33，face是历史最终脸部近景；两者是诊断/效果图，不能写成效果开关A/B。阶段06→07同条件累计但变化细微，可点击原尺寸查看，不据微小差异夸大结论。

待补：最终版本同姿势局部开/关近景。本教程没有裁图或修饰；若后续裁切应标明原图及矩形位置。若瞳孔发亮，先查色度/瞳孔保护和sRGB；若整个脸改变，先查head和UV域。''',
'''眼睛漫反射细化在CleanShade/Focused之后，原白点恢复在线条之后；眼睛不应被材质分类错误覆盖。其提亮仍用旧band，因此Debug10与16边界差异也可能影响观察。''',
'_Eye _RegionalHead', [('BridgetToon.shader',337,353),('BridgetToon.shader',361,362),('BridgetToon.shader',521,529),('BridgetToon.shader',654,657)])

chapter('13', '''边缘光（rim）是在接近轮廓的表面加一层亮色，帮助角色与背景分离；它和高光不是同一个方向函数。当前主要用 nv=saturate(N·V)，nv小代表表面更侧向观察者，再按材质和阴面权重调整。

旧路径用 _RimWidth/_RimIntensity，乘 albedo、band 与主光；分类区域打开 ReferenceRim 后改用 `1-smoothstep(width-aa,width+aa,nv)`，width越大边缘区域越宽。aa=max(fwidth(nv)×0.65,0.008)，减少阈值锯齿。

ReferenceRim 颜色在albedo和 _ReferenceRimTint 之间混合；材质缩放按分类权重平均，脸额外乘 _ReferenceRimFaceScale=0.15。亮度权重 lerp(_ReferenceRimShadowFloor,1,saturate(band)) 使阴面仍保留一部分rim，而不是在阴面全部消失。这是美术描光，不是物理逆光或额外真实灯。

最终 `rim=lerp(oldRim,referenceRim,_ReferenceRimEnabled*specCoverage)`。因此旧 _RimWidth 在未分类/未启用区域仍是后备，但不是最终分类区域的主要宽度控制。''',
'''世界法线、视线、albedo、旧band、分类图、faceRegionMask与主光颜色。四主体 _ReferenceRimEnabled=1、Width=0.24（默认0.19）、Strength=0.5（默认0.38）、ShadowFloor=0.55（默认0.45）、TintMix=0.75（默认0.65）。材质Vector=(1,0.9,0.65,0.6)，Tint Color=(0.94,0.97,1,1)。

这些保存值明确不同于声明默认，不应从新材质初始值推断最终效果。脸缩放需区域门控有效；共享材质并不自动识别脸。''',
'''1. 固定背景和视角，切Debug12隔离rim，确认亮带位于轮廓附近而非正面高光中心。
2. 在练习副本只切 _ReferenceRimEnabled，保持分类图和旧rim参数不变，观察分类与未分类部分的差异。
3. 恢复开关，先调整Width看覆盖，再调Strength/TintMix看亮度和颜色，不同时改变背景。
4. 看阴面轮廓是否有适量保留，并确认脸的亮边显著弱于头发/布料；若无差别，查faceRegionMask。
5. 回0查看内部线是否仍清楚，保存同条件对照；站立循环中检查rim宽度随法线/视角变化而不是时间闪烁。''',
'''rim_debug 是历史Debug12最终rim。阶段07→08为独立副本累计边缘光展示，不与project图直接比较。预期是受控边缘亮带，而非全身发白或新增灯光。

如果正面有大块亮色，先在13看是否为高光；若12图亮带很宽，核nv/Width而非旧_RimWidth。若阴面仍亮并非必然错误，先检查ShadowFloor。待补：最终版本Width/FaceScale的独立A/B和站立逐姿态rim检查图。''',
'''ReferenceRim 沿用旧band的阴面权重，和FocusedSpec的新受光带不完全相同；CleanShade改变diffuse也不等于直接改rim。内部线最后覆盖rim，分类图复用于线/高光，错误分类可能同时影响三者。''',
'_ReferenceRim _RimWidth _RimIntensity', [('BridgetToon.shader',616,623)])

chapter('14', '''验收不是只看一张最好看的最终图，而是能解释每个分量，并确认站立循环中没有随姿态出现区域错位、线条跳变或阴影滞后一帧。把静态分层与动态稳定性分开记录，才能定位问题。

历史 standing audit 报告 passed=true、observations=627，完整13-cell循环编号为2–6，actionsObserved只有stand，issues为空。该报告只覆盖当时主相机站立采样，不声称每个显示tick都测过。这里不扩展到其他动作，也不组织动画修复或控制器测试。

历史4K报告记录30秒/1800帧、9阶段各13 cells、同镜头同姿势、无背景移动投影和原生4K源等检查通过。这是已有视频/渲染产物的历史摘要，视频不在包里；4K60不是GPU实时性能测量，本教程不提供FPS或耗时承诺。

project_snapshot_comparison 的428文件一致，只证明磁盘采集与旧快照一致；readonly_audit 明确 liveUnityInspected=false、newPlayValidation=false。网站构建与文档核对也不能补足Unity运行验证。''',
'''前提是读者独立练习中的输入合同、材质保存表、MPB与全局发布已完成连接；缺模型、原图或桥接依赖时，将相关验收标为待补。保留截图时至少记录：资源版本、Unity版本、分辨率、姿态cell、相机/光、效果开关、Debug模式、参数改动。

动态脸坐标来自只读Transform，阴影来自实际Renderer流与BeforeForwardOpaque调度。只检查现有站立播放的渲染结果，不修改骨骼、蒙皮、Bind Pose或动画。''',
'''1. 固定站立cell与相机，依次留存1/4–9（输入）、22/25/38（区域）、16（漫反射）、13（最终高光）、12（rim）、31（内线）、0（最终含轮廓）。缺某张就标待补。
2. 对每个效果只改变一个开关并记录条件；不要把原工程与演示副本、不同分辨率或不同姿势合成A/B。
3. 播放已有站立循环，按所有已知cell检查脸/皮肤/袖区域贴合、大腿亮形不越膝、眼白不串区、墨线连续及影子不滞后。至少覆盖完整循环再重复观察，测试次数自行记录，不冒用历史627。
4. 暂停在出现问题的相同姿态，先观察Debug分量再定位最后写入分支。保留失败图与参数，不通过改动画来绕开渲染问题。
5. 将验收状态分成“实测通过/实测失败/待补/不适用”，附环境与证据文件；没有Unity编译/运行环境时不填写通过。''',
'''| 症状 | 优先核查 | 判别方式 |
|---|---|---|
| 分区全黑或头体混淆 | RegionalMask、MPB、_RegionalHead | 22，再看38；不要看材质保存0就下结论 |
| 脸上旧参数改了没反应 | CleanShade最终覆盖 | 16对照；35/36只是旧贡献 |
| 高光像塑料或腿过亮 | 分类、Focused、Thigh替换 | 25→13→43/44；26–29不含最终修正 |
| 数据贴图边缘串色 | sRGB、压缩、MipMap、Wrap | 4–7与导入记录逐项核对 |
| 轮廓刺出或缺失 | TANGENT合同、零宽、Debug | 0模式检查；31只看内部线 |
| 眼睛变白/闪点 | UV域、瞳孔保护、原白点域 | 33区域与34差值；禁用新增运动点 |
| 阴影截断/抖动/滞后 | Ready、范围、bias、调度 | 看当前帧计数、独立接收面和深度；证据不足则待补 |
| 整图偏灰或过曝 | 环境、sRGB、ambient、额外后处理 | 1→16→17；17不是性能或曝光测量 |

本次没有进入Unity、没有运行Shader编译或站立播放。待补列表见[证据与缺口](../reference/evidence.md)，读者不能把文档构建通过转录为自己的渲染验收。''',
'''排错顺序为环境→输入→覆盖→漫反射→高光→rim→线条→合成→站立时序。先恢复可核查基线，再改一个因素。网站严格构建、手机布局和资源白名单检查只保证教程可读与可部署。''',
'_DebugMode _CleanShadeEnabled _FocusedShadeEnabled _FocusedSpecEnabled _ThighLobeEnabled _ReferenceRimEnabled', [('GGSTGeometryShadowMaps.cs',197,208),('BridgetToon.shader',687,693)])

def generate():
    metadata=json.loads((ROOT/'tools/chapter_map.json').read_text(encoding='utf-8'))
    mp=rows('data/material_parameters.csv')
    props=rows('data/shader_properties.csv')
    materials=['Base_Imitate','BaseSecondary_Imitate','BodyBaseFlip_Imitate','CoatExterior_Imitate']
    source_evidence=[]
    for c in metadata:
        if c['id'] not in CHAPTERS:
            continue
        a=CHAPTERS[c['id']]
        body=f"# {c['id']} {c['title']}\n\n> 本章依据磁盘源码与保存数据解释当前实现。所有配图均为 2026-10-20 历史产物；操作与预期供独立练习，尚未在本次 Unity 运行验证。\n\n"
        body+='## 视觉问题与原理\n\n'+a['principle']+'\n\n'
        body+='## 真实效果与比较边界\n\n'
        imgs=c['images']
        if len(imgs)>=2:
            body+='| 左图 | 右图 |\n|---|---|\n'
            for i in range(0,len(imgs),2):
                body+='| '+ ' | '.join(f'[![{x}](../assets/images/{x})](../assets/images/{x})' for x in imgs[i:i+2])+(' |' if len(imgs[i:i+2])==2 else ' | — |')+'\n'
            body+='\n'
        else:
            for x in imgs:
                body+=f'[![{x}](../assets/images/{x})](../assets/images/{x})\n\n'
        for x in imgs:
            im=next(v for v in json.loads((PACK/'data/images_manifest.json').read_text(encoding='utf-8')) if v['path']=='images/'+x)
            if x.startswith('stages/'):
                desc='独立演示副本历史原生4K图；非 Debug；固定镜头与站立 cell 00 的累计展示，省略投影、构图和4K线宽与主工程不同。相邻阶段是效果组累计对照，不是所有参数独立实验。'
            else:
                desc='原工程历史验收图；'+('Debug 输出，编号见原始图注。' if 'Debug' in im['caption'] else '非 Debug。')
                if 'thigh_before' in x or 'thigh_after' in x: desc+='清单记录为 thigh lobe OFF/ON 控制对；本次未重跑。'
                elif 'shade_' in x: desc+='历史阴影与高光同时修改的综合对照，不是纯阴影单变量实验。'
                else: desc+='只作本图效果/诊断展示，未有清单授权的单变量配对；不可与演示副本作单变量比较。'
            body+=f"- **{x}**：{desc}原产物 `{im['origin']}`。原始说明：{im['caption']}。\n"
        body+='\n完整尺寸、哈希和来源映射见[图片附录](../reference/images.md)。本章证据范围：'+c['evidence']+'。\n\n'
        body+='## 源码位置与原文摘录\n\n'
        for f,start,end in c['refs']:
            if f=='BridgetToon.shader':
                context='FORWARD / ForwardBase：vert、frag'
                if start>=796: context='SHADOWCASTER：vertShadow、fragShadow'
                elif start>=729: context='OUTLINE：vertOutline、fragOutline（范围跨末尾时亦包含SHADOWCASTER）'
            else:
                context={'GGSTRegionalShading.cs':'Apply、ResolveFrames、Set及生命周期', 'BridgetImitateProfile.cs':'OnEnable、Apply、LateUpdate、OnDisable', 'GGSTGeometryShadowMaps.cs':'Ready、Projection、RenderMaps、DrawToonSubmeshes、Publish（以下按行定位）', 'GGSTGeometryDepth.shader':'GEOMETRY_DEPTH：vert、frag','StageShadowReceiver.shader':'ForwardBase：GeometryStageVisibility、vert、frag'}[f]
            body+=f'- [{f}:{start}–{end}](../reference/code/{f}.md#l{start})：{context}。\n'
        body+='\n下列均为原文件连续摘录，保留原始代码；只展示局部上下文，**不是独立可编译实现**。完整分支见逐行索引。\n\n'
        for f,start,end in a['excerpts']:
            code='\n'.join((PACK/'sources'/f).read_text(encoding='utf-8-sig').splitlines()[start-1:end])
            body+=f'用途：核对本章所述计算/写入；来源 [{f}:{start}–{end}](../reference/code/{f}.md#l{start})。\n\n```'+('csharp' if f.endswith('.cs') else 'hlsl')+'\n'+code+'\n```\n\n'
            source_evidence.append({'chapter':c['id'],'file':f,'start':start,'end':end,'text':code})
        body+='## 输入合同与脚本依赖\n\n'+a['inputs']+'\n\n'
        body+='## 当前参数：默认值与保存值\n\n以下从 material_parameters.csv 自动提取，B=Base、S=BaseSecondary、F=BodyBaseFlip、C=CoatExterior；“未保存”表示字段不存在。类型及默认来自声明记录，保存值来自磁盘，**不是运行中逐帧采样**。MPB/Global 和内部覆盖见[覆盖附录](../reference/overrides.md)，完整账本见[参数附录](../reference/parameters.md)。\n\n'
        selected=[]
        for r in mp:
            if r['material']==materials[0] and any(r['property'].startswith(p) for p in a['prefixes']):
                values=[]
                for m in materials:
                    value=next((v for v in mp if v['material']==m and v['property']==r['property']),None)
                    values.append(value['savedValue'] if value and value['savedPresent']=='True' else '未保存')
                decl=next((d for d in props if d.get('property')==r['property']),None)
                selected.append([r['property'],r['type'],r['shaderDefault'],*values])
        body+=table(['属性','类型','默认','B 保存','S 保存','F 保存','C 保存'],selected)
        body+='## 独立练习的操作步骤\n\n'+a['steps']+'\n\n'
        body+='## 如何验收与排错\n\n'+a['verify']+'\n\n'
        body+='## 依赖及相互影响\n\n'+a['interaction']+'\n\n'
        body+='[返回章节导航](../index.md) · [章节—证据表](../reference/evidence-map.md) · [依赖接口](../reference/dependencies.md)\n'
        write(ROOT/'docs/chapters'/f"{c['id']}.md",body)
    write(ROOT/'tools/excerpts.json',json.dumps(source_evidence,ensure_ascii=False,indent=2))
    print(f'Chapters written: {len(CHAPTERS)}; exact excerpts recorded: {len(source_evidence)}')

if __name__=='__main__':
    generate()
