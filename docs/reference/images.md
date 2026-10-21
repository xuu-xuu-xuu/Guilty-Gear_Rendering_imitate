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

## 新增站立循环：真实Play帧及裁切

本批578条记录按哈希去重为91张Unity原生PNG，另有13张同矩形原像素裁切。来源是完整工程隔离副本、Unity2022.3.62f3c1/D3D11/Linear、1600×900、HDR关闭、RT单采样。用途、Debug、姿态、重复帧与完整映射见[站立验收](standing-stability-20261021.md)和其下载清单；不与旧批次混作单变量实验。裁切来源为本批近景，固定[451,207,969,506]，518×299，无修色或重绘。

| SHA256 / 原图 | 类别 | 尺寸 | 用途/姿态记录数 |
|---|---|---|---|
| [03cc0ec6cfd0790587e147d99921be2dec21f8f184c6b6a9cc75f4f8bd5ad1fb](../assets/images/standing/20261021/03cc0ec6cfd0790587e147d99921be2dec21f8f184c6b6a9cc75f4f8bd5ad1fb.png) | new-real-unity-render | 1600×900 | 1 |
| [06cd49a4cfe247fb5a8d5689b1878318246a3219b6ef4348670245ac956a943d](../assets/images/standing/20261021/06cd49a4cfe247fb5a8d5689b1878318246a3219b6ef4348670245ac956a943d.png) | new-real-unity-render | 1600×900 | 1 |
| [07f4259a5c7728108d5452224be4ca953b1514ab74c853c87d0f157d1a9bc5dd](../assets/images/standing/20261021/07f4259a5c7728108d5452224be4ca953b1514ab74c853c87d0f157d1a9bc5dd.png) | new-real-unity-render | 1600×900 | 1 |
| [0997ec7b0aa9d8d304e256287aabecda815ee1b6a961c54ce71150e3f271567e](../assets/images/standing/20261021/0997ec7b0aa9d8d304e256287aabecda815ee1b6a961c54ce71150e3f271567e.png) | new-real-unity-render | 1600×900 | 1 |
| [0d305895b74d9df90c682a055b8455ce8fe9e83b413bc362fc168782f7e0931d](../assets/images/standing/20261021/0d305895b74d9df90c682a055b8455ce8fe9e83b413bc362fc168782f7e0931d.png) | new-real-unity-render | 1600×900 | 1 |
| [0e05ee1f95b7aef3becaa963e1f68c560e6199c9394d11eebff595a2e49c6f8b](../assets/images/standing/20261021/0e05ee1f95b7aef3becaa963e1f68c560e6199c9394d11eebff595a2e49c6f8b.png) | new-real-unity-render | 1600×900 | 1 |
| [0e4ec28b318b1112afe6f8679c297f39b7d70dc6f8333a4d22b77a9b21ce3087](../assets/images/standing/20261021/0e4ec28b318b1112afe6f8679c297f39b7d70dc6f8333a4d22b77a9b21ce3087.png) | new-real-unity-render | 1600×900 | 1 |
| [106337d0c096331cf0208952c538996fe3ec37328a57fa11a39caebcb3b07bf6](../assets/images/standing/20261021/106337d0c096331cf0208952c538996fe3ec37328a57fa11a39caebcb3b07bf6.png) | new-real-unity-render | 1600×900 | 1 |
| [116d37656258e5bf534d2da1ff759a2a31a8e115a24c2921fc860ef84f5b4e68](../assets/images/standing/20261021/116d37656258e5bf534d2da1ff759a2a31a8e115a24c2921fc860ef84f5b4e68.png) | new-real-unity-render | 1600×900 | 1 |
| [157b1a59a21855a2cf7af745cab2b351e3bf0ae5e2995e6c228df99bd7d5c27e](../assets/images/standing/20261021/157b1a59a21855a2cf7af745cab2b351e3bf0ae5e2995e6c228df99bd7d5c27e.png) | new-real-unity-render | 1600×900 | 1 |
| [1923cce4b3ba93b84c5282f8d3aaf3c79a8db668d4ff7d9d886f76f23962e94b](../assets/images/standing/20261021/1923cce4b3ba93b84c5282f8d3aaf3c79a8db668d4ff7d9d886f76f23962e94b.png) | new-real-unity-render | 1600×900 | 1 |
| [19a1a171418966dfe9515536f3d544f26e814bb552e956452c92209fef673336](../assets/images/standing/20261021/19a1a171418966dfe9515536f3d544f26e814bb552e956452c92209fef673336.png) | new-real-unity-render | 1600×900 | 1 |
| [2267ebc369e05653477811582a4a717d5297ff102b9665cb815e95df384a06e3](../assets/images/standing/20261021/2267ebc369e05653477811582a4a717d5297ff102b9665cb815e95df384a06e3.png) | new-real-unity-render | 1600×900 | 1 |
| [257448dc02acf01cefca3cc8dacd25b484dd587ecad18646842fa6e1cb00bcd3](../assets/images/standing/20261021/257448dc02acf01cefca3cc8dacd25b484dd587ecad18646842fa6e1cb00bcd3.png) | new-real-unity-render | 1600×900 | 1 |
| [2f656caf3d8ecc370d4e95f0139b6a283ec3fd5f788284529b01bc6b64805e92](../assets/images/standing/20261021/2f656caf3d8ecc370d4e95f0139b6a283ec3fd5f788284529b01bc6b64805e92.png) | new-real-unity-render | 1600×900 | 1 |
| [31527d96f509a5cf2696739f33d3f492eed4e59b7b017312384e51e83362978e](../assets/images/standing/20261021/31527d96f509a5cf2696739f33d3f492eed4e59b7b017312384e51e83362978e.png) | new-real-unity-render | 1600×900 | 1 |
| [335da9dee81b771e6875d24979846b29dc85a5961bdccbe21063bab314c3bbd2](../assets/images/standing/20261021/335da9dee81b771e6875d24979846b29dc85a5961bdccbe21063bab314c3bbd2.png) | new-real-unity-render | 1600×900 | 1 |
| [3478d743ca9819fb96709e99d447c167ad7bac2395a74516501966512f093d8c](../assets/images/standing/20261021/3478d743ca9819fb96709e99d447c167ad7bac2395a74516501966512f093d8c.png) | new-real-unity-render | 1600×900 | 1 |
| [35ee7d063848a34fa8f1ec5adee4b1ee52e44f50be6fa426084ba3ca55882bc1](../assets/images/standing/20261021/35ee7d063848a34fa8f1ec5adee4b1ee52e44f50be6fa426084ba3ca55882bc1.png) | new-real-unity-render | 1600×900 | 1 |
| [364f0d360cd5c063afb0018835710151d5be4796955eb77b8b101dfe2aaa077a](../assets/images/standing/20261021/364f0d360cd5c063afb0018835710151d5be4796955eb77b8b101dfe2aaa077a.png) | new-real-unity-render | 1600×900 | 1 |
| [47aac548de3f7796ee9e2b50d2c9828342bcd041a4900374c392419d7d1a7a35](../assets/images/standing/20261021/47aac548de3f7796ee9e2b50d2c9828342bcd041a4900374c392419d7d1a7a35.png) | new-real-unity-render | 1600×900 | 1 |
| [4e050a835ba2b016a0939b4932731dcc1faa7f042bbcfb33098df396ef943ca6](../assets/images/standing/20261021/4e050a835ba2b016a0939b4932731dcc1faa7f042bbcfb33098df396ef943ca6.png) | new-real-unity-render | 1600×900 | 1 |
| [51fcb048cf4dc0471b872a6e55c37f92e4d1f8d998b7dfa12fc679aca433d976](../assets/images/standing/20261021/51fcb048cf4dc0471b872a6e55c37f92e4d1f8d998b7dfa12fc679aca433d976.png) | new-real-unity-render | 1600×900 | 1 |
| [53b60358c2594719d1ec50510bb5aaa1b9dc56ea94bca27ecc6a23454be23b0f](../assets/images/standing/20261021/53b60358c2594719d1ec50510bb5aaa1b9dc56ea94bca27ecc6a23454be23b0f.png) | new-real-unity-render | 1600×900 | 1 |
| [554ebe95a48d62f6623eea360fed5dc938131a7abc8303b309c851c9f409d3f1](../assets/images/standing/20261021/554ebe95a48d62f6623eea360fed5dc938131a7abc8303b309c851c9f409d3f1.png) | new-real-unity-render | 1600×900 | 1 |
| [577c4b1afffb4e8af0829109783ea8c55ab0b20bffb584271ba6249a6812c3a9](../assets/images/standing/20261021/577c4b1afffb4e8af0829109783ea8c55ab0b20bffb584271ba6249a6812c3a9.png) | new-real-unity-render | 1600×900 | 1 |
| [590a9b000a61e5126199f733212d8fd2410c5c9a9318b36e6ce7cad11682109a](../assets/images/standing/20261021/590a9b000a61e5126199f733212d8fd2410c5c9a9318b36e6ce7cad11682109a.png) | new-real-unity-render | 1600×900 | 48 |
| [5ab886179647c6156249011ff03f0479a06623cba2decf42cea51974cf4c2a74](../assets/images/standing/20261021/5ab886179647c6156249011ff03f0479a06623cba2decf42cea51974cf4c2a74.png) | new-real-unity-render | 1600×900 | 1 |
| [5c7da6ed3bcbb45529e9e4799a259d0595cca0619c699d178362f5bfeeed22ec](../assets/images/standing/20261021/5c7da6ed3bcbb45529e9e4799a259d0595cca0619c699d178362f5bfeeed22ec.png) | new-real-unity-render | 1600×900 | 1 |
| [5fd47f2375fc5b82e67f55823c169d221537ce2666f1402c6eb675816875d2d3](../assets/images/standing/20261021/5fd47f2375fc5b82e67f55823c169d221537ce2666f1402c6eb675816875d2d3.png) | new-real-unity-render | 1600×900 | 1 |
| [62c0aef0f175fc9c0e009ce22e59f6d9006249e0a39ce71a38295850ba70da1c](../assets/images/standing/20261021/62c0aef0f175fc9c0e009ce22e59f6d9006249e0a39ce71a38295850ba70da1c.png) | new-real-unity-render | 1600×900 | 40 |
| [6461d4969010e3d0a2f4bad6a444e68834c076ca5158b71e2210ec6e3e2447ee](../assets/images/standing/20261021/6461d4969010e3d0a2f4bad6a444e68834c076ca5158b71e2210ec6e3e2447ee.png) | new-real-unity-render | 1600×900 | 1 |
| [6a5b22500cc90694c666309904988a0068560ff70ac9774cae1b0abe03187d8b](../assets/images/standing/20261021/6a5b22500cc90694c666309904988a0068560ff70ac9774cae1b0abe03187d8b.png) | new-real-unity-render | 1600×900 | 1 |
| [7437ed5c65c4df29ee00cb94ecfa941e7dfbf5b450d19fd12f8885c21b04ff37](../assets/images/standing/20261021/7437ed5c65c4df29ee00cb94ecfa941e7dfbf5b450d19fd12f8885c21b04ff37.png) | new-real-unity-render | 1600×900 | 1 |
| [7654280869510d7532a9675554bc34a71ec69cb83b438ca32e985ace2ca33a7e](../assets/images/standing/20261021/7654280869510d7532a9675554bc34a71ec69cb83b438ca32e985ace2ca33a7e.png) | new-real-unity-render | 1600×900 | 1 |
| [78a47ce3a3235b55d9ffaf410d7bc1da04b612699c045486f405df27f3f8f2d9](../assets/images/standing/20261021/78a47ce3a3235b55d9ffaf410d7bc1da04b612699c045486f405df27f3f8f2d9.png) | new-real-unity-render | 1600×900 | 32 |
| [7a16e647c4704e66eedb164ae623a588c3eefa90e6a0e6dd7e34ed1fdb27415b](../assets/images/standing/20261021/7a16e647c4704e66eedb164ae623a588c3eefa90e6a0e6dd7e34ed1fdb27415b.png) | new-real-unity-render | 1600×900 | 1 |
| [7eb1172fabb5cf34b7afcc92f0b5082b86ab3d097d9ab5d72092eda7e320f548](../assets/images/standing/20261021/7eb1172fabb5cf34b7afcc92f0b5082b86ab3d097d9ab5d72092eda7e320f548.png) | new-real-unity-render | 1600×900 | 1 |
| [7ee263fc641e4992ae3450dade4f13a5e1507cc1ad576227a09d33e1cb9f67c0](../assets/images/standing/20261021/7ee263fc641e4992ae3450dade4f13a5e1507cc1ad576227a09d33e1cb9f67c0.png) | new-real-unity-render | 1600×900 | 46 |
| [7f3bc5242a9f700bab9118b3e8a6294256c4188f79de1be53d46a67cf8294146](../assets/images/standing/20261021/7f3bc5242a9f700bab9118b3e8a6294256c4188f79de1be53d46a67cf8294146.png) | new-real-unity-render | 1600×900 | 1 |
| [801de08d9abdb614595a5b58b7b406c34196762f85641cee42fb0957ff7f81e8](../assets/images/standing/20261021/801de08d9abdb614595a5b58b7b406c34196762f85641cee42fb0957ff7f81e8.png) | new-real-unity-render | 1600×900 | 1 |
| [8187d70d25fd1d3c1b65122e59013108bf534d73f48a90bb41f98fc6de381bc6](../assets/images/standing/20261021/8187d70d25fd1d3c1b65122e59013108bf534d73f48a90bb41f98fc6de381bc6.png) | new-real-unity-render | 1600×900 | 1 |
| [854545dfa97c1600eeb6e346d7fa3f5db4a2f599f84502045a111677e3c00473](../assets/images/standing/20261021/854545dfa97c1600eeb6e346d7fa3f5db4a2f599f84502045a111677e3c00473.png) | new-real-unity-render | 1600×900 | 1 |
| [88b21ecb2cfa0b73dcb5f97d3d53ccd5e7f73c177107e6f0d4977a997ba332b6](../assets/images/standing/20261021/88b21ecb2cfa0b73dcb5f97d3d53ccd5e7f73c177107e6f0d4977a997ba332b6.png) | new-real-unity-render | 1600×900 | 31 |
| [93a8322f5517ba37285be24f3281c2871045c6e11e5df8c1c0063447a9331514](../assets/images/standing/20261021/93a8322f5517ba37285be24f3281c2871045c6e11e5df8c1c0063447a9331514.png) | new-real-unity-render | 1600×900 | 32 |
| [96130a6b74b79496219495a728210c1c5e5b4a59217b0dbddea2001eb02ee706](../assets/images/standing/20261021/96130a6b74b79496219495a728210c1c5e5b4a59217b0dbddea2001eb02ee706.png) | new-real-unity-render | 1600×900 | 1 |
| [999a740096fea2d7dea9549cbd8ade201b6335c8be7674d3124489637c436ae2](../assets/images/standing/20261021/999a740096fea2d7dea9549cbd8ade201b6335c8be7674d3124489637c436ae2.png) | new-real-unity-render | 1600×900 | 1 |
| [9f9cafd6398e656a041fbb9f28047f626d81a9afa4f8bca418145fb24e5031aa](../assets/images/standing/20261021/9f9cafd6398e656a041fbb9f28047f626d81a9afa4f8bca418145fb24e5031aa.png) | new-real-unity-render | 1600×900 | 1 |
| [a0057fb4bdeb09ba983908c2cd85c59e6cd1f35c43d51d05018e59ed9ebd68b6](../assets/images/standing/20261021/a0057fb4bdeb09ba983908c2cd85c59e6cd1f35c43d51d05018e59ed9ebd68b6.png) | new-real-unity-render | 1600×900 | 1 |
| [a2cd7c1a6a744a13c60078e93a6037ae4ef5eae5c0cf26051b732511add15d27](../assets/images/standing/20261021/a2cd7c1a6a744a13c60078e93a6037ae4ef5eae5c0cf26051b732511add15d27.png) | new-real-unity-render | 1600×900 | 47 |
| [a624847911ae8f0df4eca3c73141b367a52cdee16b61b7c9669249075b857c01](../assets/images/standing/20261021/a624847911ae8f0df4eca3c73141b367a52cdee16b61b7c9669249075b857c01.png) | new-real-unity-render | 1600×900 | 38 |
| [aa8a1e68b26c96d72b7bbaa8407431a2a3c489ec1a187128d637c318a4093f0c](../assets/images/standing/20261021/aa8a1e68b26c96d72b7bbaa8407431a2a3c489ec1a187128d637c318a4093f0c.png) | new-real-unity-render | 1600×900 | 1 |
| [aad705a56db431d7a2cbe668653a767eb52047e7ec5c3a218ffbb50d19d76b44](../assets/images/standing/20261021/aad705a56db431d7a2cbe668653a767eb52047e7ec5c3a218ffbb50d19d76b44.png) | new-real-unity-render | 1600×900 | 1 |
| [aadd04ce15b0bed9b685e3b63eb6f3a13356aa073c3424c4bc436030335a8799](../assets/images/standing/20261021/aadd04ce15b0bed9b685e3b63eb6f3a13356aa073c3424c4bc436030335a8799.png) | new-real-unity-render | 1600×900 | 1 |
| [abe07bf3664743c1a6522367942752d8c2acf2cda9f461ec1e6cf76c27a9f816](../assets/images/standing/20261021/abe07bf3664743c1a6522367942752d8c2acf2cda9f461ec1e6cf76c27a9f816.png) | new-real-unity-render | 1600×900 | 1 |
| [ad0a75075f197eb183844cd0c1f2990bde7bfb4c49654f1e4d1b330f5f8f7b9b](../assets/images/standing/20261021/ad0a75075f197eb183844cd0c1f2990bde7bfb4c49654f1e4d1b330f5f8f7b9b.png) | new-real-unity-render | 1600×900 | 1 |
| [b383211a2fb76664515ae14621d9d3eb54eb40e9381da085e394691409bf1701](../assets/images/standing/20261021/b383211a2fb76664515ae14621d9d3eb54eb40e9381da085e394691409bf1701.png) | new-real-unity-render | 1600×900 | 1 |
| [b6da68d0af0dd263f321e561e01fdb2aa33ba84aef9d960b4f5dff0e84c04281](../assets/images/standing/20261021/b6da68d0af0dd263f321e561e01fdb2aa33ba84aef9d960b4f5dff0e84c04281.png) | new-real-unity-render | 1600×900 | 1 |
| [b875bb073182cee4e63eeb26a78546aea74565bf50ddd5e090e1f41341083c61](../assets/images/standing/20261021/b875bb073182cee4e63eeb26a78546aea74565bf50ddd5e090e1f41341083c61.png) | new-real-unity-render | 1600×900 | 1 |
| [bd7455829cca8df2cecb5c04ac7d0bc0b8720dbf3c370a88de5fe66682d24222](../assets/images/standing/20261021/bd7455829cca8df2cecb5c04ac7d0bc0b8720dbf3c370a88de5fe66682d24222.png) | new-real-unity-render | 1600×900 | 1 |
| [bf326635f4ccfd43724c5c40298519b97b8a6498c25e798e69021f0f9e5396cf](../assets/images/standing/20261021/bf326635f4ccfd43724c5c40298519b97b8a6498c25e798e69021f0f9e5396cf.png) | new-real-unity-render | 1600×900 | 49 |
| [c088cfc84e410342a59def227a55fd73e53ff84bcd3b4d207f701be639bdbcf3](../assets/images/standing/20261021/c088cfc84e410342a59def227a55fd73e53ff84bcd3b4d207f701be639bdbcf3.png) | new-real-unity-render | 1600×900 | 1 |
| [c44b6915ded9c69c44a2b4b0a33eeeda71f6e3eb289f64d861e806c83094e806](../assets/images/standing/20261021/c44b6915ded9c69c44a2b4b0a33eeeda71f6e3eb289f64d861e806c83094e806.png) | new-real-unity-render | 1600×900 | 41 |
| [c8eb4ab354510ff63d6f7a40e62399c825e7a920a6e4eb7cdd4d85824da28dbe](../assets/images/standing/20261021/c8eb4ab354510ff63d6f7a40e62399c825e7a920a6e4eb7cdd4d85824da28dbe.png) | new-real-unity-render | 1600×900 | 1 |
| [c98a5985306f2df12631f0261a09fc1d4146b210f587bb9f8b6b9cdb605a2c65](../assets/images/standing/20261021/c98a5985306f2df12631f0261a09fc1d4146b210f587bb9f8b6b9cdb605a2c65.png) | new-real-unity-render | 1600×900 | 1 |
| [cb069b7568e9cb462a709ec5f3a8b18a55f8bf22eea2a55c42e9a3dbe4a43c26](../assets/images/standing/20261021/cb069b7568e9cb462a709ec5f3a8b18a55f8bf22eea2a55c42e9a3dbe4a43c26.png) | new-real-unity-render | 1600×900 | 1 |
| [ce647568baf40b9429c4a52737de2bd2454ef418cb0252ad71050735fda3ed6c](../assets/images/standing/20261021/ce647568baf40b9429c4a52737de2bd2454ef418cb0252ad71050735fda3ed6c.png) | new-real-unity-render | 1600×900 | 1 |
| [ce7ad73cd0b3b0cc1c2964041a2e0782347f89fd8d0428135fa9de8948bf4da1](../assets/images/standing/20261021/ce7ad73cd0b3b0cc1c2964041a2e0782347f89fd8d0428135fa9de8948bf4da1.png) | new-real-unity-render | 1600×900 | 1 |
| [cf05441ff809410ab9d47fef6c3b6bc1e2817dfd99e4e5bb01c26d47ecd85937](../assets/images/standing/20261021/cf05441ff809410ab9d47fef6c3b6bc1e2817dfd99e4e5bb01c26d47ecd85937.png) | new-real-unity-render | 1600×900 | 33 |
| [cf52e1d4725fae4f13480dea258315385dc93e331dbf4054915d512f224b1b40](../assets/images/standing/20261021/cf52e1d4725fae4f13480dea258315385dc93e331dbf4054915d512f224b1b40.png) | new-real-unity-render | 1600×900 | 1 |
| [cf9030e5b61e4ccc2b46171dcccc64394c387e421cc57b1ff8e379a508bd5a27](../assets/images/standing/20261021/cf9030e5b61e4ccc2b46171dcccc64394c387e421cc57b1ff8e379a508bd5a27.png) | new-real-unity-render | 1600×900 | 1 |
| [d286f6848a4736025df77304d4157aec6542a7a64fa044a1809543ca43a4efa9](../assets/images/standing/20261021/d286f6848a4736025df77304d4157aec6542a7a64fa044a1809543ca43a4efa9.png) | new-real-unity-render | 1600×900 | 1 |
| [d300ee11e4203785298e8609dbe5f3fb89cd085ef0a83ba41872cc4f76df5259](../assets/images/standing/20261021/d300ee11e4203785298e8609dbe5f3fb89cd085ef0a83ba41872cc4f76df5259.png) | new-real-unity-render | 1600×900 | 32 |
| [d345258d2a15acb33f8d37f3752dd8def034c09ce76d87a09a318cc51313f92e](../assets/images/standing/20261021/d345258d2a15acb33f8d37f3752dd8def034c09ce76d87a09a318cc51313f92e.png) | new-real-unity-render | 1600×900 | 1 |
| [d7d5618d1b761146587a81afa2fbe898ae25435cde695779ee893edb1bdb745a](../assets/images/standing/20261021/d7d5618d1b761146587a81afa2fbe898ae25435cde695779ee893edb1bdb745a.png) | new-real-unity-render | 1600×900 | 1 |
| [da0667553ac49c8e516508d124d4bd012243cbf601d21793a974a21042e1f546](../assets/images/standing/20261021/da0667553ac49c8e516508d124d4bd012243cbf601d21793a974a21042e1f546.png) | new-real-unity-render | 1600×900 | 1 |
| [da3d0e30b1ba98def2d8a6690f71a576aa8b2242363c7afbe0a869d01ca5d947](../assets/images/standing/20261021/da3d0e30b1ba98def2d8a6690f71a576aa8b2242363c7afbe0a869d01ca5d947.png) | new-real-unity-render | 1600×900 | 1 |
| [ddd5442766c87b686c23cfbe16382fa48ead1d77c33b1b1dc0c8dfa7ce5563ef](../assets/images/standing/20261021/ddd5442766c87b686c23cfbe16382fa48ead1d77c33b1b1dc0c8dfa7ce5563ef.png) | new-real-unity-render | 1600×900 | 1 |
| [e0306ab98b5c91ae9cb5a1305f7206d7aa71e3b4ffa072a89d38e732ae935283](../assets/images/standing/20261021/e0306ab98b5c91ae9cb5a1305f7206d7aa71e3b4ffa072a89d38e732ae935283.png) | new-real-unity-render | 1600×900 | 1 |
| [e34788594e9eed0617ff73a3a5d88c3d4178683c36c09ffe22bc830141d3c809](../assets/images/standing/20261021/e34788594e9eed0617ff73a3a5d88c3d4178683c36c09ffe22bc830141d3c809.png) | new-real-unity-render | 1600×900 | 1 |
| [e5fd9c9c6e6969f71ac174f8b45778c0232e1f80ff3df73ee72aee6264bd60ec](../assets/images/standing/20261021/e5fd9c9c6e6969f71ac174f8b45778c0232e1f80ff3df73ee72aee6264bd60ec.png) | new-real-unity-render | 1600×900 | 1 |
| [e6a83be62db7a89bfd2d985b73baadf24a035aaff137109bbf516b745abb23ba](../assets/images/standing/20261021/e6a83be62db7a89bfd2d985b73baadf24a035aaff137109bbf516b745abb23ba.png) | new-real-unity-render | 1600×900 | 1 |
| [e751cab84a1eef5dc672065645d7d7ebdc8d79af431561deecacf448aa1be9d3](../assets/images/standing/20261021/e751cab84a1eef5dc672065645d7d7ebdc8d79af431561deecacf448aa1be9d3.png) | new-real-unity-render | 1600×900 | 1 |
| [e794f595763524b860bbc225ebe8776045316e207c90e605e3d6c598f4c18997](../assets/images/standing/20261021/e794f595763524b860bbc225ebe8776045316e207c90e605e3d6c598f4c18997.png) | new-real-unity-render | 1600×900 | 1 |
| [ea28984b41b9e3a67c22551688a7f6bcbdb78a173bd570d34028f68d99a6e2b8](../assets/images/standing/20261021/ea28984b41b9e3a67c22551688a7f6bcbdb78a173bd570d34028f68d99a6e2b8.png) | new-real-unity-render | 1600×900 | 1 |
| [ed8de2b33a0bdf5ebd4896f2f56266fb83cd181c507f289089f62fdeb4b94440](../assets/images/standing/20261021/ed8de2b33a0bdf5ebd4896f2f56266fb83cd181c507f289089f62fdeb4b94440.png) | new-real-unity-render | 1600×900 | 1 |
| [f3975b42864464876a0bb64b8250d77cb65951e3bd8432dba3f023fc4b2ef3d1](../assets/images/standing/20261021/f3975b42864464876a0bb64b8250d77cb65951e3bd8432dba3f023fc4b2ef3d1.png) | new-real-unity-render | 1600×900 | 1 |
| [f5e1ae225d2f59102cbae545c0329619c789768b114ea3d67f986f7832901066](../assets/images/standing/20261021/f5e1ae225d2f59102cbae545c0329619c789768b114ea3d67f986f7832901066.png) | new-real-unity-render | 1600×900 | 1 |
| [f83cf3684c8f54693fa3b21bf2f744085c51df1b077c8b6ae2c52132ce57f850](../assets/images/standing/20261021/f83cf3684c8f54693fa3b21bf2f744085c51df1b077c8b6ae2c52132ce57f850.png) | new-real-unity-render | 1600×900 | 31 |
| [fa50739c62e408938ebf68ec6e202c7059ce974a5276b8d741f287c5f88e1b90](../assets/images/standing/20261021/fa50739c62e408938ebf68ec6e202c7059ce974a5276b8d741f287c5f88e1b90.png) | new-real-unity-render | 1600×900 | 1 |
| [fcc11ec4b13a72295e7dd5863a976655cf74780f4644167d7ed211732c0f561b](../assets/images/standing/20261021/fcc11ec4b13a72295e7dd5863a976655cf74780f4644167d7ed211732c0f561b.png) | new-real-unity-render | 1600×900 | 1 |
| [ed811197295cd1b48ae629bdbcfa4b958959e28822b6360351dae72998869cba](../assets/images/standing/20261021/ed811197295cd1b48ae629bdbcfa4b958959e28822b6360351dae72998869cba.png) | exact-pixel-crop | 518×299 | 1 |
| [088cb6f3d728bb53332f9656cf71d2e175a7879cad9fea3a2a080eb271983ffa](../assets/images/standing/20261021/088cb6f3d728bb53332f9656cf71d2e175a7879cad9fea3a2a080eb271983ffa.png) | exact-pixel-crop | 518×299 | 1 |
| [9210e3a93d5258c5abf4a6e995060ad7093ece39384a5ec92783933c70b30589](../assets/images/standing/20261021/9210e3a93d5258c5abf4a6e995060ad7093ece39384a5ec92783933c70b30589.png) | exact-pixel-crop | 518×299 | 1 |
| [265f0a083f46c0a40e4701c2b7e892fa6c92162b99d23c6e7558d8ba87c82da8](../assets/images/standing/20261021/265f0a083f46c0a40e4701c2b7e892fa6c92162b99d23c6e7558d8ba87c82da8.png) | exact-pixel-crop | 518×299 | 1 |
| [e52d0f7586270b85130d31f5f3c2c4071fdf4f77bb44233c41aac2707f3e0381](../assets/images/standing/20261021/e52d0f7586270b85130d31f5f3c2c4071fdf4f77bb44233c41aac2707f3e0381.png) | exact-pixel-crop | 518×299 | 1 |
| [39f03300d6458274161dc3f496de7315c96711e1d65658e2d6517c27ed442a2a](../assets/images/standing/20261021/39f03300d6458274161dc3f496de7315c96711e1d65658e2d6517c27ed442a2a.png) | exact-pixel-crop | 518×299 | 1 |
| [954a7778c339590d44f56c23085930d4d9abb71fa43c637cb8ab8575c2cdd720](../assets/images/standing/20261021/954a7778c339590d44f56c23085930d4d9abb71fa43c637cb8ab8575c2cdd720.png) | exact-pixel-crop | 518×299 | 1 |
| [20b0f1e648395935e10994f434958fc77bc36a1d5d95bab6b37d01d589986f11](../assets/images/standing/20261021/20b0f1e648395935e10994f434958fc77bc36a1d5d95bab6b37d01d589986f11.png) | exact-pixel-crop | 518×299 | 1 |
| [05fe123f5b91c96391a74a4005526bee9ec682504e02fb6e090ace15f01ba328](../assets/images/standing/20261021/05fe123f5b91c96391a74a4005526bee9ec682504e02fb6e090ace15f01ba328.png) | exact-pixel-crop | 518×299 | 1 |
| [013ecaa4e85e6cd3a796d6b66e419adfaa58bf16c8bc28f01788e4ecd9b47a44](../assets/images/standing/20261021/013ecaa4e85e6cd3a796d6b66e419adfaa58bf16c8bc28f01788e4ecd9b47a44.png) | exact-pixel-crop | 518×299 | 1 |
| [058403b25af5bfc8b8e3c97315afef165b333ec4ea23bf21689990ed8c7b62dd](../assets/images/standing/20261021/058403b25af5bfc8b8e3c97315afef165b333ec4ea23bf21689990ed8c7b62dd.png) | exact-pixel-crop | 518×299 | 1 |
| [d18a6dcb52a54349689ee00fda287c929299abe39f568a8e187d4759c92b3b79](../assets/images/standing/20261021/d18a6dcb52a54349689ee00fda287c929299abe39f568a8e187d4759c92b3b79.png) | exact-pixel-crop | 518×299 | 1 |
| [595b9533a97de9cb0116e47c8e82fd81369b940b61d4086a09700baf59008a12](../assets/images/standing/20261021/595b9533a97de9cb0116e47c8e82fd81369b940b61d4086a09700baf59008a12.png) | exact-pixel-crop | 518×299 | 1 |
