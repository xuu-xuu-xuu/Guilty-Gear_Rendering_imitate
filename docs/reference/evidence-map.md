# 从画面问题找到控制项

先暂停在同一姿态，选择对应分量，再修改负责最后结果的参数。找不到原因时，先回到输入检查，不要同时改几个效果。

| 想改善的画面 | 优先调整或检查 | 观察输出 | 操作说明 |
|---|---|---|---|
| 整图灰、过曝 | 主光、环境、sRGB、后处理 | 1 / 16 / 17 | [环境](../chapters/01.md) |
| 贴图、高光或线条串色 | ILM通道、导入、UV | 4–9 | [贴图](../chapters/02.md) |
| 头体分区混淆 | _RegionalHead / _RegionalEnabled MPB | 22，再38 | [Renderer参数](../chapters/03.md) |
| 基础亮面过大或过小 | _LightTreshold / _RampOffset | 10，再16 | [两段式](../chapters/05.md) |
| 脸、腹部、袖子碎影 | CleanShade / FocusedShade及覆盖 | 38 / 41 / 42 / 16 | [分区明暗](../chapters/06.md) |
| 皮肤或衣料偏色 | 对应Palette Light/Dark向量 | 37 / 16 | [亮暗配色](../chapters/07.md) |
| 投影截断或脸上暗带不对 | Ready、范围、bias、接收器与CleanShade | 32仅看中间量，最终看16/0 | [投影](../chapters/08.md) |
| 材质都像塑料 | 分类遮罩、各类Shine、FocusedSpec | 25 / 13 | [材质高光](../chapters/09.md) |
| 大腿亮块错位或越膝 | UV域、中心曲线、Thigh/Focused依赖 | 43 / 44，再13 | [大腿亮块](../chapters/10.md) |
| 眼睛发白、瞳孔提亮 | head、眼区、瞳孔保护、各Eye强度 | 33 / 34，再0 | [眼睛](../chapters/12.md) |
| 边缘亮带太宽 | ReferenceRim Width、FaceScale | 12 | [边缘光](../chapters/13.md) |
| 描边刺出、内部线不清楚 | TANGENT、零宽、ILM.A、分类线参数 | 30 / 31；外壳看0 | [线条](../chapters/11.md) |
| 随姿态闪变或投影滞后 | 更新时机、动态输入、相同姿态重复 | 对应分量与0 | [站立排错](../chapters/14.md) |
