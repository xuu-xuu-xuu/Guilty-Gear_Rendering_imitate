# 证据范围、差异与待补实验

教程采用资料包的真实代码与数据，没有打开Unity、进入Play或重新验证站立。采集日为2026-10-21，北京时间；配图和播放报告是2026-10-20已有产物。磁盘只读快照不能证明编辑器未保存内存与之相同。

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

下表是未来实验方案，**没有在本次执行**；需要读者自己的资源与独立Unity环境。

| 缺口 | 应固定的条件 | 应补输出/判断 |
|---|---|---|
| 环境与通道诊断 | 相机/主光/分辨率/站立cell/资源版本 | Debug1–9、实际导入平台与顶点通道检查 |
| MPB与独立接入 | 同Renderer材质/同姿态、显式只读引用 | MPB采样、Debug22、生命周期还原与禁用顺序 |
| 两段式与分区归因 | Palette/spec/rim/线等其他项不变 | 10/16、38/41/42，各次只切一个开关 |
| 最终投影A/B | 同相机/姿态/地面墙面/最终材质 | Stage开关、hair路径、内置阴影分开，附深度/visibility |
| 眼睛最终局部开关 | 同姿态近景、相同像素窗口 | 0/33/34，保留黑瞳/线条/原白点；裁图需坐标及来源 |
| TANGENT合同 | 使用自己合法现有模型，不修改动画/骨骼 | 记录TANGENT.xyz真实语义与描边结果；普通切线不能顶替 |
| 换UV的专用域 | 新图集、区域遮罩、固定光照 | 眼/胸前/腿曲线重新设计并检验，不能复制常量当通用 |
| 新工程可复刻性 | Built-in/Linear、所需输入已连接 | Unity编译、渲染适配器、静态对照、完整站立循环记录 |

## 本次交付检查与Unity验收分离

资料哈希、源码摘录、参数转录、图片白名单、链接/子路径、MkDocs严格构建和浏览器桌面/手机排版属于文档检查。实际执行结果见[构建记录](deployment.md)。这些检查均不授予Unity“已通过”状态。
