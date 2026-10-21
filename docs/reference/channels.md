# 通道、UV 与模型契约

以下是当前源码的使用方式，不代表已证明原游戏通道定义。对应 [BridgetToon.shader:298–331](code/BridgetToon.shader.md#l298)、[365–405](code/BridgetToon.shader.md#l365)、[548–567](code/BridgetToon.shader.md#l548)、[635–652](code/BridgetToon.shader.md#l635)、[749–771](code/BridgetToon.shader.md#l749)。

| 属性 / 当前引用 | RGB用途 | A用途 | UV/色彩空间 |
|---|---|---|---|
| _MainTex / BGT_base | 基础色 | 主体不作为透明 | 主UV，sRGB=1 |
| _ShadowMap / BGT_Sss | 阴面颜色混合 | 未作为透明使用 | 主UV，sRGB=1；不是物理SSS |
| _LightMap / BGT_ilm | R×255旧分类，G明暗偏移，B局部高光细节 | 1-A为内部墨线覆盖 | 主UV，sRGB=0 |
| _DetailMap / BGT_detail | 乘法细节 | 不参与主体公式 | TEXCOORD1，sRGB=0 |
| _OutlineMap / BGT_olm | 墨色 | 不是线宽 | 主UV，sRGB=1 |
| _RegionalMask | R皮肤/G白袖，B未作为本路径输入 | 非透明 | 主UV，sRGB=0，需head/enable MPB |
| _FourMaterialSpecMask | R头发/G布料/B皮肤 | 金属类别 | 主UV，sRGB=0，保留Alpha数据 |
| 辅助Decal的 _MainTex / BGT_decal | X2 Multiply乘法色，中性0.5 | 不是普通Alpha混合 | 自身UV采样，sRGB=0 |

ILM旧分类区间：skin为[10,_LayerMaskStep)，hair为[_HairLayerMin,_HairLayerMax)，leather/metal同理。保存边界见参数账本。旧R分类混有衣料和皮肤，所以最终精修使用独立分类遮罩，不能把ILM.R当可靠通用材质ID。

## 顶点输入

| 数据 | 用途 | 练习前必须确认 |
|---|---|---|
| POSITION | 当前已有蒙皮输出的位置 | 动画已正常，无需本教程改骨骼 |
| NORMAL | 主光/高光/rim | 世界空间归一化，背面翻转 |
| COLOR.R | AO/明暗控制 | 缺值或全黑会影响信号；本包无顶点样本 |
| TEXCOORD0 / UV0 / mesh.uv | 主图集 | _MainTex_ST应用于主图集输入 |
| TEXCOORD1 / UV1 / mesh.uv2 | Detail | 不应把它称作UV0 |
| TEXCOORD2 / UV2 / mesh.uv3 | 可选镜像 | 四主体_UseMirroredUV=0 |
| TANGENT.xyz | _UseSmoothOutline=1时的描边法线 | 特殊合同，标准切线不等于平滑法线 |

## 图集专用区域

| 功能 | 当前坐标依据 | 换模型时的工作 |
|---|---|---|
| 眼睛 | [337–362](code/BridgetToon.shader.md#l337)，2048像素空间、瞳孔/色度/原白点门控 | 重定虹膜、眼白、瞳孔和原白点；颜色门控也要重新验证 |
| 胸前衣料 | [464–467](code/BridgetToon.shader.md#l464)，两块矩形域 | 重新标定衣料UV岛或自己制作区域遮罩 |
| 腿部/大腿亮块 | [507–518](code/BridgetToon.shader.md#l507)、[583–603](code/BridgetToon.shader.md#l583) | 重做腿域、中心曲线、宽度、纵向门控与膝过渡 |

这些式子描述当前工程的精确输入，不是任意模型通用识别。原始/自制纹理像素与网格均不随包提供。本次不下载、不补造这些资源。

## 导入与压缩

逐张记录见[导入完整表](texture-imports.md)，含11张纹理、绑定、MipMap、sRGB、filterMode、aniso、wrapU/V/W、压缩枚举、质量、Crunch和平台overridden。不能把未启用覆盖当生效值；也不能仅凭textureFormat=-1断言实际GPU格式。

数据遮罩关闭sRGB；Alpha Is Transparency=0用于保留数据，不代表Alpha被忽略。BGTW_ilm的现存sRGB=1仅作武器预览异常记录。未来练习需检查实际平台导入结果，但本次没有重导入或GPU格式验证。
