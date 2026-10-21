# 证据范围、差异与待补实验

初版依据只读资料包，原图及播放报告为2026-10-20产物。2026-10-21本轮已在完整工程的隔离副本中执行23次真实Unity静态捕获，新增14张去重原图/无修饰裁切，见[投影与眼睛实测](experiments-20261021.md)。没有进入Play或重验站立循环，不能把这批静态结果扩展到任意环境。

## 原始证据

原始文件保留在仓库 [evidence目录](https://github.com/xuu-xuu-xuu/Guilty-Gear_Rendering_imitate/tree/f8980fad7a742d76cf8b941843234cd292c7ae82/rendering-tutorial-source-pack/evidence)。

| 文件 | 实际记录 | 不能扩展出的结论 |
|---|---|---|
| project_snapshot_comparison.json | 与2026-10-20采集的428文件比较，changed/added空，allEqual=true | 不是今天运行过或当前内存相同 |
| historical_scene_rendering.json | 旧相机/光/Renderer资料，可交叉解释保存场景未解析Prefab | 不是本次实时场景查询，不能自行解析未知fileID |
| historical_standing_audit.json | 当时627次主相机站立观察、完整13cell循环2–6、issues空 | 不声称每个显示tick或新环境都通过，不延伸到其他动作 |
| historical_4k_validation_summary.json | 当时30秒/1800帧/4K源、各阶段13cells、同相机姿势等产物检查 | 不是GPU性能基准，也不是每个参数独立实验 |
| readonly_audit.json | 当时428工程文件只读核对，sources/images exact；liveUnityInspected=false/newPlayValidation=false | 不能用passed=true抹去这些边界 |

## 资料冲突及解释

实际已核实的说明差异集中记录在[对应表](evidence-map.md)。不存在“按notes写一套却不检查代码”的捷径：CleanShade、Focused与ThighLobe的后续覆盖必须按源码解释，旧脸部/高光/rim数值只在相应路径讨论。

materials_saved.json的12份保存数据包括无已解析Shader的StageShadowReceiver；material_parameters.csv的793行只对应10个有声明属性的材质。完整保存原貌见[12份材质](material-snapshots.md)，保留未知项，不静默补全。

图片哈希显示shade_after与thigh_before为同一画面复用，不能当独立实验；shade对比同时改过阴影与高光。9张阶段图是独立副本累计效果，不提供完整逐阶段临时材质设置。

## 待补实验清单

下表区分本轮已完成的静态证据与仍待补范围。原资料包不变，新增证据独立登记；需要原完整工程输入的测试不等于公开快照独立可运行。

| 缺口 | 应固定的条件 | 应补输出/判断 |
|---|---|---|
| 环境与通道诊断 | 相机/主光/分辨率/站立cell/资源版本 | Debug1–9、实际导入平台与顶点通道检查 |
| MPB与独立接入 | 同Renderer材质/同姿态、显式只读引用 | 已补原工程副本静态MPB采样/捕获恢复；Debug22实图、通用适配及完整生命周期仍待补 |
| 两段式与分区归因 | Palette/spec/rim/线等其他项不变 | 10/16、38/41/42，各次只切一个开关 |
| 最终投影A/B：部分已补 | 同相机/保存站立姿态/最终材质 | 墙/地各一属性接收A/B、caster回退路径、投脸零差异已补；其他姿态、内置自阴影/CleanShade组合及深度可视化仍待补 |
| 眼睛最终局部开关：静态已补 | 同姿态近景、相同像素窗口 | 已补0/33/34、13/30负对照、同矩形无修饰裁切、眼区局部性；其他姿态/设备仍待补 |
| TANGENT合同 | 使用自己合法现有模型，不修改动画/骨骼 | 记录TANGENT.xyz真实语义与描边结果；普通切线不能顶替 |
| 换UV的专用域 | 新图集、区域遮罩、固定光照 | 眼/胸前/腿曲线重新设计并检验，不能复制常量当通用 |
| 新工程可复刻性 | Built-in/Linear、所需输入已连接 | 已验证完整工程隔离副本编译/静态渲染；全新空工程适配和完整站立循环仍待补 |

## 本轮Unity实测边界

墙面/地面分别只改一个接收Renderer的_GeometryShadowFloor，两个深度图哈希相同，重复ON帧0像素变化。眼睛只改站立头MPB的_EyeRefineEnabled，最终变化3469像素，全部位于Debug33的3866像素覆盖内；最终高光及内部线覆盖OFF/ON不变。并非为获得明显效果而调高旧投脸参数。

九份渲染源码、材质和场景保持原样；源工程428文件前后哈希不变，副本422个原输入不变。副本只省略三个无关Editor自动化工具及.meta，并新增采集器。摄像机/MPB/caster恢复已记录。完整证据与采集源代码见[新实验页](experiments-20261021.md)。

## 本次交付检查与Unity验收分离

资料哈希、摘录、参数转录、白名单、链接、构建与页面排版属于文档检查。新实验的Unity静态渲染和证据复核另列，不能把文档构建或公开PNG重算当成新Unity执行，也不授予其他待补项“通过”状态。记录见[构建说明](deployment.md)。
