# 章节、源码与证据对应表

此表先于初版正文建立。行号指原资料快照；参数表是磁盘保存值，运行规则是源码推导。原图与播放报告来自2026-10-20；[新增实验](experiments-20261021.md)为2026-10-21隔离副本的真实Unity静态渲染，不能扩展为Play或全新工程复刻验证。

| 章节 | 源码位置 | 参数来源 | 效果图 | 验证证据与限制 |
|---|---|---|---|---|
| 00 最终效果、复刻目标与适用范围 | BridgetToon.shader:189–203 | environment.json; materials_saved.json | project/final.png, stages/08.png | readonly_audit; project_snapshot_comparison；范围说明，非新运行 |
| 01 Unity 环境、渲染管线、色彩空间、相机与主光 | BridgetImitateProfile.cs:20–51; BridgetToon.shader:310–331 | environment.json; saved_scene_rendering.json | project/final.png | 磁盘场景；缺当前独立环境复测、环境单变量图 |
| 02 贴图用途、通道含义、UV 与导入设置 | BridgetToon.shader:298–331; BridgetToon.shader:365–405; BridgetToon.shader:749–771 | texture_bindings.csv; texture_import_settings.json | stages/00.png | 源码采样与导入记录；无纹理像素和网格通道实测 |
| 03 材质划分、Renderer 对应关系与参数覆盖 | GGSTRegionalShading.cs:23–66; BridgetImitateProfile.cs:20–51 | material_parameters.csv; runtime_overrides.csv; runtime_write_sites.csv; saved_scene_rendering.json | project/region_debug.png | Debug38 非 Renderer22；专用22图待补；historical_scene_rendering仅交叉参考 |
| 04 Shader 总体结构和真实执行顺序 | BridgetToon.shader:321–725; BridgetToon.shader:729–810 | shader_properties.csv; debug_outputs.csv | stages/08.png | 源码控制流；图片只展示输出，不证明各分支独立 |
| 05 基础两段式明暗 | BridgetToon.shader:365–401; BridgetToon.shader:405–437 | material_parameters.csv: _LightTreshold/_Ramp*/_Shadow*/_AO* | stages/00.png, stages/01.png | 累计阶段；Debug10/16独立对照待补 |
| 06 脸部、皮肤与衣料的分区明暗 | BridgetToon.shader:405–458; BridgetToon.shader:479–518 | material_parameters.csv: _Clean*/_Focused*; runtime_overrides.csv | stages/01.png, stages/02.png, project/face.png, project/region_debug.png, project/shade_before.png, project/shade_after.png | Debug38覆盖；shade历史同时改高光，非纯阴影A/B |
| 07 亮面与暖色阴面的配色 | BridgetToon.shader:461–501; BridgetToon.shader:516–518 | material_parameters.csv: _Palette* (Vector) | stages/02.png, stages/03.png | 累计阶段；最终Color不等于Vector乘数 |
| 08 头发投脸、自阴影与地面背景投影的控制 | GGSTGeometryShadowMaps.cs:115–147; GGSTGeometryShadowMaps.cs:175–280; GGSTGeometryDepth.shader:27–46; BridgetToon.shader:247–261; BridgetToon.shader:438–501; StageShadowReceiver.shader:44–88 | saved_scene_rendering.json; material_parameters.csv; runtime_write_sites.csv | project/final.png | 原final历史展示；新增隔离Unity墙/地接收A/B、Stage回退及投脸零差异；其他姿态/组合仍待补 |
| 09 头发、布料、皮肤和金属的高光区分 | BridgetToon.shader:537–579; BridgetToon.shader:605–609 | material_parameters.csv: _FourMaterial*/_*Shine*/_Focused* | stages/03.png, stages/04.png, project/specular_debug.png | Debug13最终高光；26–29只基础分类分支 |
| 10 大腿高光的范围、形状与颜色 | BridgetToon.shader:507–518; BridgetToon.shader:580–609 | material_parameters.csv: _ThighLobe*; 专用UV常量 | stages/04.png, stages/05.png, project/thigh_before.png, project/thigh_after.png, project/thigh_lobe_debug.png | 历史受控OFF/ON与Debug44；新UV复测待补 |
| 11 外轮廓描边与内部线条 | BridgetToon.shader:625–652; BridgetToon.shader:729–793 | material_parameters.csv: _Line*/_Outline*/_InnerLine* | stages/05.png, stages/06.png, project/ink_debug.png | Debug31内部线；无本次网格TANGENT审计 |
| 12 眼睛层次与高光 | BridgetToon.shader:268–272; BridgetToon.shader:332–362; BridgetToon.shader:521–529; BridgetToon.shader:654–668 | material_parameters.csv: _Eye*; 专用UV常量 | stages/06.png, stages/07.png, project/face.png, project/eye_regions.png | 历史Debug33/近景；新增隔离Unity最终开关近景、精确裁切及局部性/负对照；其他姿态仍待补 |
| 13 边缘光 | BridgetToon.shader:532–535; BridgetToon.shader:612–625 | material_parameters.csv: _ReferenceRim* | stages/07.png, stages/08.png, project/rim_debug.png | Debug12隔离rim；旧_RimWidth仅后备 |
| 14 整体检查、站立循环验收与常见问题 | GGSTGeometryShadowMaps.cs:197–243; GGSTRegionalShading.cs:20–42; BridgetToon.shader:660–725 | debug_outputs.csv; 保存值与覆盖账本 | project/final.png | historical_standing_audit; historical_4k_validation_summary；不代表本次或新项目通过 |

完整性基线：MANIFEST 覆盖 57 个文件；MANIFEST 自身是第 58 个文件，不能自证哈希，由 Git 基线及原 ZIP 逐字节比较补足。

## 核实后的说明差异

- notes/06_gpt_handoff.txt 要求先交示范章确认；本次用户明确要求直接完成全套，按本次请求执行。
- notes/01_inventory.txt 的“12 个材质”对应 materials_saved.json；material_parameters.csv 只有 10 个有已声明属性的材质、793 行，不能把没有属性的辅助材质虚构成完整参数行。
- notes 的执行顺序把外轮廓放在最后，适合作为阅读概览；源码实际是独立 OUTLINE Pass，SHADOWCASTER 由 Unity 阴影调度，不能当作 frag 内的末尾语句。
- notes 称环境为 4× MSAA：这是活动 Profile 写入值和 Ultra 保存档，并非每个质量档都相同。
- notes 的“分区开启”是源码规则与 strength=1 的组合推断；原资料采集未采样运行中MPB；本轮隔离副本静态采样另见新增实验。
- 保存场景部分 Prefab fileID 未解析；历史 Renderer 列表可交叉参照，不能据此宣称已还原当前实例。
- BGTW_ilm 的 sRGB=1 保留为事实，不能推广为推荐设置。
- shade_after 与 thigh_before 哈希相同；这是同一历史画面复用，不能当成两次独立验证。
