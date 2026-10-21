# 纹理通道、UV与顶点输入

先按这个表连接资源，再检查导入和Debug。通道含义描述的是本Shader的读取方式，不代表通用游戏格式。

| 属性 / 示例资源 | RGB用途 | Alpha用途 | UV / sRGB |
|---|---|---|---|---|
| _MainTex / BGT_base | 基础色 | 主体不作透明 | 主UV / 开 |
| _ShadowMap / BGT_Sss | 阴面颜色混合 | 不作透明 | 主UV / 开；不是物理SSS |
| _LightMap / BGT_ilm | R×255基础分类；G偏移明暗；B高光细节 | 1-A为内部线覆盖 | 主UV / 关 |
| _DetailMap / BGT_detail | 乘法细节 | 主体公式不使用 | UV1 / 关 |
| _OutlineMap / BGT_olm | 墨色 | 不是线宽 | 主UV / 开 |
| _RegionalMask | R皮肤，G白袖 | 非透明 | 主UV / 关，还需要head/enable |
| _FourMaterialSpecMask | R头发，G布料，B皮肤 | 金属类别 | 主UV / 关，保留Alpha |
| 贴花_MainTex / BGT_decal | X2 Multiply色，中性0.5 | 不是普通Alpha混合 | 自身UV / 关 |

ILM的基础分类区间来自R×255，skin为[10,_LayerMaskStep)，发/皮革/金属分别使用对应Min/Max。该分类不能可靠区分所有衣料和皮肤，因此精修使用独立RGBA分类遮罩。

## 顶点输入

| 数据 | 用途 | 连接前确认 |
|---|---|---|
| POSITION | 已有模型的蒙皮位置 | 动画能正常播放 |
| NORMAL | 主光、高光和rim | 变换到世界后归一化，背面按VFACE翻转 |
| COLOR.R | AO/明暗控制 | 缺值或全黑会影响受光信号 |
| UV0 / mesh.uv | 主图集 | 主输入应用_MainTex_ST |
| UV1 / mesh.uv2 | Detail | 不是UV0；强度为0时看不出变化 |
| UV2 / mesh.uv3 | 可选镜像 | 四主体_UseMirroredUV=0 |
| TANGENT.xyz | 平滑外描边法线 | 只有已满足专用约定的网格才打开_UseSmoothOutline |

普通模型切线不能直接顶替描边法线。没有这种数据时，在练习材质关闭_UseSmoothOutline使用几何法线观察，不修改骨骼或Bind Pose。

## 换UV必须重做的区域

| 区域 | 代码 | 需要重新标定 |
|---|---|---|
| 眼睛 | [337–362](code/BridgetToon.shader.md#l337) | 虹膜、瞳孔、眼白、原白点和颜色门控 |
| 胸前衣料 | [464–467](code/BridgetToon.shader.md#l464) | 两块衣料UV岛或新的区域遮罩 |
| 腿和大腿亮块 | [507–518](code/BridgetToon.shader.md#l507)、[583–603](code/BridgetToon.shader.md#l583) | 腿域、中心曲线、宽度、纵向窗口与膝过渡 |

图集常量描述当前角色，不会自动识别新模型的身体部位。贴图与模型像素数据不在源码中，需要使用自己的资源准备输入。

## 导入与排错

逐张设置见[导入表](texture-imports.md)。数据遮罩关闭sRGB和Alpha Is Transparency，Alpha仍要保留；纹理名字中有Sss也不意味着实现了物理次表面散射。

出现高光/线条同时串色时，先查ILM的RGB/A是否被一并模糊或错误sRGB解码。检查实际平台覆盖是否启用，不凭textureFormat=-1推断GPU格式。
