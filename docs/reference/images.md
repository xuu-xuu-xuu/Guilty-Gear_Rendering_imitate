# 图片来源与比较条件

原有21张图片仅从不可变资料包的images_manifest.json复制，均为历史产物。新增14张图片（12张去重后的Unity原生PNG、2张无修饰裁切）单独登记在evidence/rendering-ab-20261021/images.json，详见[新实验](experiments-20261021.md)。两份清单分开维护，原资料包不变；本文不将新图冒充原白名单旧图。

9 张阶段图固定镜头与站立 cell 00，累计效果；刻意去掉角色投影，投影矩阵 m00/m11 ×0.94，4K 描边像素宽度 ×2。原工程保存宽度仍为 0.8/0，不能抄成 1.6/0。阶段图彼此可解释累计变化，不能证明每个参数独立影响，更不能与 project 图作单变量 A/B。

## project/final.png

[查看图片](../assets/images/project/final.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/verified_play_2.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：historical final project playback screenshot; actual project has projection。
- Debug：否。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`364b636a5d438e930bd620fd6a5d73b19f3ee483dda4d17536de1da41ac31c60`。

## project/face.png

[查看图片](../assets/images/project/face.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_face_0_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：historical final face close-up。
- Debug：否。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`57b21d452b00304ad4fa55db6e00ad3e6d320b309894cc761baf6f5c14e9e0ae`。

## project/thigh_before.png

[查看图片](../assets/images/project/thigh_before.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_body_0_off.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：controlled thigh lobe disabled; paired with thigh_after。
- Debug：否。
- 比较条件：清单明确记录的 thigh lobe OFF/ON 控制对；属于历史条件，未在本次重跑。
- SHA256：`000fb2ac324a62ce3fcbc87a2d5cfad9205549982842cd5ce245b4041107bd6b`。

## project/thigh_after.png

[查看图片](../assets/images/project/thigh_after.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_body_0_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：controlled thigh lobe enabled; paired with thigh_before。
- Debug：否。
- 比较条件：清单明确记录的 thigh lobe OFF/ON 控制对；属于历史条件，未在本次重跑。
- SHA256：`e757979c95ff3c8fa4d3b01dcaea015112a28e41cd99a8b118a84bfed381fc6a`。

## project/rim_debug.png

[查看图片](../assets/images/project/rim_debug.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_full_12_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：Debug 12 isolated rim。
- Debug：是，编号见原始图注。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`e4ef1de9781d6b504861b6e9ff0def27adc4fc9010454f7389d9eef9efde31e7`。

## project/specular_debug.png

[查看图片](../assets/images/project/specular_debug.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_full_13_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：Debug 13 final combined specular。
- Debug：是，编号见原始图注。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`4f8b3961f1448047ceff25f5f225db309e0a702460f6000877f75ab6e6d22589`。

## project/ink_debug.png

[查看图片](../assets/images/project/ink_debug.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_full_31_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：Debug 31 styled internal lines。
- Debug：是，编号见原始图注。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`d0e354da438754fd192e715160c3f403c1d44507ebd444f46b28173622c23dcf`。

## project/region_debug.png

[查看图片](../assets/images/project/region_debug.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_full_38_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：Debug 38 clean shading coverage。
- Debug：是，编号见原始图注。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`f0c845c634dae30045f36e64f2e19c62797127ea9b3ef42f82d247104283640b`。

## project/eye_regions.png

[查看图片](../assets/images/project/eye_regions.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_face_33_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：Debug 33 iris/sclera/authored glint regions。
- Debug：是，编号见原始图注。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`91fc0f3887d2742444a101d6998daafb0c5c2cea1f0690324d859c3894277184`。

## project/thigh_lobe_debug.png

[查看图片](../assets/images/project/thigh_lobe_debug.png) · 1600 × 900

- 原产物：`thigh_highlight_20261020/controlled_body_44_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：Debug 44 thigh lobe and facing gates。
- Debug：是，编号见原始图注。
- 比较条件：诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。
- SHA256：`7ee039e2625ebd933bf0bf561e58a92f9c1956a397bc181bb07aabcbcb97919e`。

## project/shade_before.png

[查看图片](../assets/images/project/shade_before.png) · 1600 × 900

- 原产物：`shade_highlight_20261020/controlled_body_0_off.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：historical combined shading/specular refinement OFF; not single-variable diffuse comparison。
- Debug：否。
- 比较条件：阴影与高光同时改变的历史对照，不能归因于仅阴影改变。
- SHA256：`a69a1e0adaaa3f9c8388c04869744ca73e76fcfa9828e34468fd32850df2ea86`。

## project/shade_after.png

[查看图片](../assets/images/project/shade_after.png) · 1600 × 900

- 原产物：`shade_highlight_20261020/controlled_body_0_on.png`。
- 来源类别：historical actual Unity screenshot。
- 原始图注：historical combined shading/specular refinement ON; not single-variable diffuse comparison。
- Debug：否。
- 比较条件：阴影与高光同时改变的历史对照，不能归因于仅阴影改变。
- SHA256：`000fb2ac324a62ce3fcbc87a2d5cfad9205549982842cd5ce245b4041107bd6b`。

## stages/00.png

[查看图片](../assets/images/stages/00.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_00/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：基础色; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`57168c28cb57300f635f4f5a56708370baa156cb374a9cd9996f326c168cb809`。

## stages/01.png

[查看图片](../assets/images/stages/01.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_01/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：基础两段式明暗; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`68c188f91dc059c8f4766dc9b17387077a66cc87c0422f1dbe4aae201c56ca0b`。

## stages/02.png

[查看图片](../assets/images/stages/02.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_02/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：分区明暗; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`5d28ff6f3bf185073629980f9d7d218e4cd9d2869850e983bba90ab7a8a6203e`。

## stages/03.png

[查看图片](../assets/images/stages/03.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_03/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：亮面与暖色阴面; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`07a0447d86c552a7c66fc757ebc126be4066dd758583f7c7058080bc2e2bb3e1`。

## stages/04.png

[查看图片](../assets/images/stages/04.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_04/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：材质高光; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`90bc68348e29e2bf5c5f899e4f8487b3432d0e8657dbde70e4602f40a424043e`。

## stages/05.png

[查看图片](../assets/images/stages/05.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_05/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：大腿高光; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`3a3dc108d15074a65b5664c069dcd21dc086fd8b38fc6c751fa8625d7b617770`。

## stages/06.png

[查看图片](../assets/images/stages/06.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_06/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：描边与内部线条; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`561bb8acccdacbc548cbca4bf44be2a896fa31513fda279aa52d047631f34755`。

## stages/07.png

[查看图片](../assets/images/stages/07.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_07/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：眼睛层次与高光; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`74f4fe5e1d5e90a5cf9b239b29fbb315e9cc41afd1b8b7332f2a48064336abea`。

## stages/08.png

[查看图片](../assets/images/stages/08.png) · 3840 × 2160

- 原产物：`render_demo_4k_20261020/frames/stage_08/cell_00.png`。
- 来源类别：historical isolated-copy native 4K Unity render。
- 原始图注：边缘光; cumulative stage, fixed camera and same standing cell 00; projection intentionally omitted。
- Debug：否。
- 比较条件：同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。
- SHA256：`53188076162ec25dbb144778103aa79ea804c5cfafb622d71b1ea218b50c1b48`。

## 2026-10-21新增实验登记

下表每一行是一个实际捕获或裁切记录；重复帧和相同结果按哈希复用同一个PNG，原生23次捕获只存12张不同PNG，加2张裁切。来源为当前完整工程的隔离副本，Edit已保存站立姿态，不是原工程历史图或4K演示图。HDR关闭、RT单采样，与旧图的抗锯齿条件不同，不跨批次做A/B。

| 记录 | 文档图片 | Debug | 唯一变量 | 数值 | 裁切 |
|---|---|---|---|---|---|
| floor_receiver_off | docs/assets/images/experiments/20261021/floor_receiver_off.png | 0 | _GeometryShadowFloor@GGST_Floor_ShadowReceiver | 1 | 无 |
| floor_receiver_on | docs/assets/images/experiments/20261021/floor_receiver_on.png | 0 | _GeometryShadowFloor@GGST_Floor_ShadowReceiver | 0.08 | 无 |
| floor_receiver_on_repeat | docs/assets/images/experiments/20261021/floor_receiver_on.png | 0 | _GeometryShadowFloor@GGST_Floor_ShadowReceiver | 0.08 | 无 |
| wall_receiver_off | docs/assets/images/experiments/20261021/wall_receiver_off.png | 0 | _GeometryShadowFloor@GGST_Wall_ShadowReceiver | 1 | 无 |
| wall_receiver_on | docs/assets/images/experiments/20261021/floor_receiver_on.png | 0 | _GeometryShadowFloor@GGST_Wall_ShadowReceiver | 0.1 | 无 |
| wall_receiver_on_repeat | docs/assets/images/experiments/20261021/floor_receiver_on.png | 0 | _GeometryShadowFloor@GGST_Wall_ShadowReceiver | 0.1 | 无 |
| stage_casters_off | docs/assets/images/experiments/20261021/stage_casters_off.png | 0 | drawStageCasters | False | 无 |
| stage_casters_on | docs/assets/images/experiments/20261021/floor_receiver_on.png | 0 | drawStageCasters | True | 无 |
| eye_off_0 | docs/assets/images/experiments/20261021/eye_off_0.png | 0 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 0 | 无 |
| eye_off_13 | docs/assets/images/experiments/20261021/eye_off_13.png | 13 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 0 | 无 |
| eye_off_30 | docs/assets/images/experiments/20261021/eye_off_30.png | 30 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 0 | 无 |
| eye_off_33 | docs/assets/images/experiments/20261021/eye_off_33.png | 33 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 0 | 无 |
| eye_off_34 | docs/assets/images/experiments/20261021/eye_off_33.png | 34 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 0 | 无 |
| eye_on_0 | docs/assets/images/experiments/20261021/eye_on_0.png | 0 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 1 | 无 |
| eye_on_13 | docs/assets/images/experiments/20261021/eye_off_13.png | 13 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 1 | 无 |
| eye_on_30 | docs/assets/images/experiments/20261021/eye_off_30.png | 30 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 1 | 无 |
| eye_on_33 | docs/assets/images/experiments/20261021/eye_on_33.png | 33 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 1 | 无 |
| eye_on_34 | docs/assets/images/experiments/20261021/eye_on_34.png | 34 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 1 | 无 |
| eye_on_0_repeat | docs/assets/images/experiments/20261021/eye_on_0.png | 0 | _EyeRefineEnabled@Original_Stand_HeadLow_UserRender | 1 | 无 |
| hair_casters_off_0 | docs/assets/images/experiments/20261021/hair_casters_off_0.png | 0 | drawHairCasters | False | 无 |
| hair_casters_off_32 | docs/assets/images/experiments/20261021/eye_off_33.png | 32 | drawHairCasters | False | 无 |
| hair_casters_on_0 | docs/assets/images/experiments/20261021/hair_casters_off_0.png | 0 | drawHairCasters | True | 无 |
| hair_casters_on_32 | docs/assets/images/experiments/20261021/eye_off_33.png | 32 | drawHairCasters | True | 无 |
| eye_off_crop | docs/assets/images/experiments/20261021/eye_off_crop.png | 0 | _EyeRefineEnabled@standingHead | 0 | [744, 316, 955, 439] |
| eye_on_crop | docs/assets/images/experiments/20261021/eye_on_crop.png | 0 | _EyeRefineEnabled@standingHead | 1 | [744, 316, 955, 439] |
