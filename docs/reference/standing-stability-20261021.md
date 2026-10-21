# 在站立循环中排查渲染问题

固定相机和光，只播放已有站立循环。先暂停在问题姿态，再分别观察投影、眼睛、高光和线条；不要通过修改动画去绕过着色问题。

## 先区分运动与闪变

同姿态、同相机、同输入的画面应可重复。不同姿态会改变法线、遮挡、投影位置和像素覆盖；Step时序还会离散切换姿态，回绕两端不要求像素相同。应找的是同一姿态下随机出现的变化、影子滞后，以及某类着色突然失去输入。

下面图集使用同一1600×900取景，HDR关闭、相机MSAA关闭、RT单采样。每个cell代表一个站立姿态；左图为最终Debug0，右图为Debug13的spec变量。背景接收面不走角色Debug，所以诊断图中仍有背景投影。点击查看原图。

## 逐项定位

| 观察部位 | 暂停后怎样操作 | 应该看到什么 |
|---|---|---|
| 墙地投影 | 检查Ready、draw、纹理与VP；分别把一个接收器floor设1再恢复 | 只改变目标接收面，不清掉角色的表面明暗 |
| 眼睛 | 同姿态近景看0/33/34，只切Eye开关 | 区域跟随眼睛，不误选脸颊；黑瞳和眼线保留 |
| 材质/大腿高光 | 25看分类，13看最终spec，43/44看腿域 | 亮块随朝向变化，目标域不越膝；不能以26–29替代最终spec |
| 外轮廓/内线 | 回0切OutlineWidth，30/31看内线 | 外壳和纹理线能独立区分，零宽层仍为零宽 |

如果只有首次出现姿态异常、下一帧恢复，先查输入更新和原生蒙皮时机。读取截图应在正常主相机渲染结束后；在一次更新里反复手动Camera.Render，不能保证拿到新姿态的蒙皮流。

## 最终画面与高光分量

每行是相同姿态的效果与诊断，用途不同，不是强度开关A/B。先看亮块属于哪个表面，再决定修改类别、受光带还是形状。

| 最终画面 | spec分量 |
|---|---|
| **cell 00 · Debug0** [![cell 00 · Debug0](../assets/images/standing/20261021/cf05441ff809410ab9d47fef6c3b6bc1e2817dfd99e4e5bb01c26d47ecd85937.png)](../assets/images/standing/20261021/cf05441ff809410ab9d47fef6c3b6bc1e2817dfd99e4e5bb01c26d47ecd85937.png) | **cell 00 · Debug13** [![cell 00 · Debug13](../assets/images/standing/20261021/c8eb4ab354510ff63d6f7a40e62399c825e7a920a6e4eb7cdd4d85824da28dbe.png)](../assets/images/standing/20261021/c8eb4ab354510ff63d6f7a40e62399c825e7a920a6e4eb7cdd4d85824da28dbe.png) |
| **cell 01 · Debug0** [![cell 01 · Debug0](../assets/images/standing/20261021/78a47ce3a3235b55d9ffaf410d7bc1da04b612699c045486f405df27f3f8f2d9.png)](../assets/images/standing/20261021/78a47ce3a3235b55d9ffaf410d7bc1da04b612699c045486f405df27f3f8f2d9.png) | **cell 01 · Debug13** [![cell 01 · Debug13](../assets/images/standing/20261021/da0667553ac49c8e516508d124d4bd012243cbf601d21793a974a21042e1f546.png)](../assets/images/standing/20261021/da0667553ac49c8e516508d124d4bd012243cbf601d21793a974a21042e1f546.png) |
| **cell 02 · Debug0** [![cell 02 · Debug0](../assets/images/standing/20261021/a624847911ae8f0df4eca3c73141b367a52cdee16b61b7c9669249075b857c01.png)](../assets/images/standing/20261021/a624847911ae8f0df4eca3c73141b367a52cdee16b61b7c9669249075b857c01.png) | **cell 02 · Debug13** [![cell 02 · Debug13](../assets/images/standing/20261021/0e05ee1f95b7aef3becaa963e1f68c560e6199c9394d11eebff595a2e49c6f8b.png)](../assets/images/standing/20261021/0e05ee1f95b7aef3becaa963e1f68c560e6199c9394d11eebff595a2e49c6f8b.png) |
| **cell 03 · Debug0** [![cell 03 · Debug0](../assets/images/standing/20261021/62c0aef0f175fc9c0e009ce22e59f6d9006249e0a39ce71a38295850ba70da1c.png)](../assets/images/standing/20261021/62c0aef0f175fc9c0e009ce22e59f6d9006249e0a39ce71a38295850ba70da1c.png) | **cell 03 · Debug13** [![cell 03 · Debug13](../assets/images/standing/20261021/157b1a59a21855a2cf7af745cab2b351e3bf0ae5e2995e6c228df99bd7d5c27e.png)](../assets/images/standing/20261021/157b1a59a21855a2cf7af745cab2b351e3bf0ae5e2995e6c228df99bd7d5c27e.png) |
| **cell 04 · Debug0** [![cell 04 · Debug0](../assets/images/standing/20261021/590a9b000a61e5126199f733212d8fd2410c5c9a9318b36e6ce7cad11682109a.png)](../assets/images/standing/20261021/590a9b000a61e5126199f733212d8fd2410c5c9a9318b36e6ce7cad11682109a.png) | **cell 04 · Debug13** [![cell 04 · Debug13](../assets/images/standing/20261021/0d305895b74d9df90c682a055b8455ce8fe9e83b413bc362fc168782f7e0931d.png)](../assets/images/standing/20261021/0d305895b74d9df90c682a055b8455ce8fe9e83b413bc362fc168782f7e0931d.png) |
| **cell 05 · Debug0** [![cell 05 · Debug0](../assets/images/standing/20261021/7ee263fc641e4992ae3450dade4f13a5e1507cc1ad576227a09d33e1cb9f67c0.png)](../assets/images/standing/20261021/7ee263fc641e4992ae3450dade4f13a5e1507cc1ad576227a09d33e1cb9f67c0.png) | **cell 05 · Debug13** [![cell 05 · Debug13](../assets/images/standing/20261021/577c4b1afffb4e8af0829109783ea8c55ab0b20bffb584271ba6249a6812c3a9.png)](../assets/images/standing/20261021/577c4b1afffb4e8af0829109783ea8c55ab0b20bffb584271ba6249a6812c3a9.png) |
| **cell 06 · Debug0** [![cell 06 · Debug0](../assets/images/standing/20261021/d300ee11e4203785298e8609dbe5f3fb89cd085ef0a83ba41872cc4f76df5259.png)](../assets/images/standing/20261021/d300ee11e4203785298e8609dbe5f3fb89cd085ef0a83ba41872cc4f76df5259.png) | **cell 06 · Debug13** [![cell 06 · Debug13](../assets/images/standing/20261021/999a740096fea2d7dea9549cbd8ade201b6335c8be7674d3124489637c436ae2.png)](../assets/images/standing/20261021/999a740096fea2d7dea9549cbd8ade201b6335c8be7674d3124489637c436ae2.png) |
| **cell 07 · Debug0** [![cell 07 · Debug0](../assets/images/standing/20261021/f83cf3684c8f54693fa3b21bf2f744085c51df1b077c8b6ae2c52132ce57f850.png)](../assets/images/standing/20261021/f83cf3684c8f54693fa3b21bf2f744085c51df1b077c8b6ae2c52132ce57f850.png) | **cell 07 · Debug13** [![cell 07 · Debug13](../assets/images/standing/20261021/335da9dee81b771e6875d24979846b29dc85a5961bdccbe21063bab314c3bbd2.png)](../assets/images/standing/20261021/335da9dee81b771e6875d24979846b29dc85a5961bdccbe21063bab314c3bbd2.png) |
| **cell 08 · Debug0** [![cell 08 · Debug0](../assets/images/standing/20261021/bf326635f4ccfd43724c5c40298519b97b8a6498c25e798e69021f0f9e5396cf.png)](../assets/images/standing/20261021/bf326635f4ccfd43724c5c40298519b97b8a6498c25e798e69021f0f9e5396cf.png) | **cell 08 · Debug13** [![cell 08 · Debug13](../assets/images/standing/20261021/2267ebc369e05653477811582a4a717d5297ff102b9665cb815e95df384a06e3.png)](../assets/images/standing/20261021/2267ebc369e05653477811582a4a717d5297ff102b9665cb815e95df384a06e3.png) |
| **cell 09 · Debug0** [![cell 09 · Debug0](../assets/images/standing/20261021/a2cd7c1a6a744a13c60078e93a6037ae4ef5eae5c0cf26051b732511add15d27.png)](../assets/images/standing/20261021/a2cd7c1a6a744a13c60078e93a6037ae4ef5eae5c0cf26051b732511add15d27.png) | **cell 09 · Debug13** [![cell 09 · Debug13](../assets/images/standing/20261021/aadd04ce15b0bed9b685e3b63eb6f3a13356aa073c3424c4bc436030335a8799.png)](../assets/images/standing/20261021/aadd04ce15b0bed9b685e3b63eb6f3a13356aa073c3424c4bc436030335a8799.png) |
| **cell 10 · Debug0** [![cell 10 · Debug0](../assets/images/standing/20261021/c44b6915ded9c69c44a2b4b0a33eeeda71f6e3eb289f64d861e806c83094e806.png)](../assets/images/standing/20261021/c44b6915ded9c69c44a2b4b0a33eeeda71f6e3eb289f64d861e806c83094e806.png) | **cell 10 · Debug13** [![cell 10 · Debug13](../assets/images/standing/20261021/ed8de2b33a0bdf5ebd4896f2f56266fb83cd181c507f289089f62fdeb4b94440.png)](../assets/images/standing/20261021/ed8de2b33a0bdf5ebd4896f2f56266fb83cd181c507f289089f62fdeb4b94440.png) |
| **cell 11 · Debug0** [![cell 11 · Debug0](../assets/images/standing/20261021/93a8322f5517ba37285be24f3281c2871045c6e11e5df8c1c0063447a9331514.png)](../assets/images/standing/20261021/93a8322f5517ba37285be24f3281c2871045c6e11e5df8c1c0063447a9331514.png) | **cell 11 · Debug13** [![cell 11 · Debug13](../assets/images/standing/20261021/7f3bc5242a9f700bab9118b3e8a6294256c4188f79de1be53d46a67cf8294146.png)](../assets/images/standing/20261021/7f3bc5242a9f700bab9118b3e8a6294256c4188f79de1be53d46a67cf8294146.png) |
| **cell 12 · Debug0** [![cell 12 · Debug0](../assets/images/standing/20261021/88b21ecb2cfa0b73dcb5f97d3d53ccd5e7f73c177107e6f0d4977a997ba332b6.png)](../assets/images/standing/20261021/88b21ecb2cfa0b73dcb5f97d3d53ccd5e7f73c177107e6f0d4977a997ba332b6.png) | **cell 12 · Debug13** [![cell 12 · Debug13](../assets/images/standing/20261021/7a16e647c4704e66eedb164ae623a588c3eefa90e6a0e6dd7e34ed1fdb27415b.png)](../assets/images/standing/20261021/7a16e647c4704e66eedb164ae623a588c3eefa90e6a0e6dd7e34ed1fdb27415b.png) |

## 眼睛局部随姿态怎么读

近景保持相同投影取景；以下局部都从原图的[451,207,969,506]矩形裁为518×299，只裁切，不修饰或逐姿态移动窗口。点击回到对应完整近景。不同姿态眼形和位置会变，不把这组图当成Eye开关A/B。

| 姿态局部 | 姿态局部 |
|---|---|
| **cell 00 · 眼睛局部** [![cell 00 · 眼睛局部](../assets/images/standing/20261021/ed811197295cd1b48ae629bdbcfa4b958959e28822b6360351dae72998869cba.png)](../assets/images/standing/20261021/ad0a75075f197eb183844cd0c1f2990bde7bfb4c49654f1e4d1b330f5f8f7b9b.png) | **cell 01 · 眼睛局部** [![cell 01 · 眼睛局部](../assets/images/standing/20261021/088cb6f3d728bb53332f9656cf71d2e175a7879cad9fea3a2a080eb271983ffa.png)](../assets/images/standing/20261021/106337d0c096331cf0208952c538996fe3ec37328a57fa11a39caebcb3b07bf6.png) |
| **cell 02 · 眼睛局部** [![cell 02 · 眼睛局部](../assets/images/standing/20261021/9210e3a93d5258c5abf4a6e995060ad7093ece39384a5ec92783933c70b30589.png)](../assets/images/standing/20261021/116d37656258e5bf534d2da1ff759a2a31a8e115a24c2921fc860ef84f5b4e68.png) | **cell 03 · 眼睛局部** [![cell 03 · 眼睛局部](../assets/images/standing/20261021/265f0a083f46c0a40e4701c2b7e892fa6c92162b99d23c6e7558d8ba87c82da8.png)](../assets/images/standing/20261021/5ab886179647c6156249011ff03f0479a06623cba2decf42cea51974cf4c2a74.png) |
| **cell 04 · 眼睛局部** [![cell 04 · 眼睛局部](../assets/images/standing/20261021/e52d0f7586270b85130d31f5f3c2c4071fdf4f77bb44233c41aac2707f3e0381.png)](../assets/images/standing/20261021/ddd5442766c87b686c23cfbe16382fa48ead1d77c33b1b1dc0c8dfa7ce5563ef.png) | **cell 05 · 眼睛局部** [![cell 05 · 眼睛局部](../assets/images/standing/20261021/39f03300d6458274161dc3f496de7315c96711e1d65658e2d6517c27ed442a2a.png)](../assets/images/standing/20261021/e5fd9c9c6e6969f71ac174f8b45778c0232e1f80ff3df73ee72aee6264bd60ec.png) |
| **cell 06 · 眼睛局部** [![cell 06 · 眼睛局部](../assets/images/standing/20261021/954a7778c339590d44f56c23085930d4d9abb71fa43c637cb8ab8575c2cdd720.png)](../assets/images/standing/20261021/e751cab84a1eef5dc672065645d7d7ebdc8d79af431561deecacf448aa1be9d3.png) | **cell 07 · 眼睛局部** [![cell 07 · 眼睛局部](../assets/images/standing/20261021/20b0f1e648395935e10994f434958fc77bc36a1d5d95bab6b37d01d589986f11.png)](../assets/images/standing/20261021/e794f595763524b860bbc225ebe8776045316e207c90e605e3d6c598f4c18997.png) |
| **cell 08 · 眼睛局部** [![cell 08 · 眼睛局部](../assets/images/standing/20261021/05fe123f5b91c96391a74a4005526bee9ec682504e02fb6e090ace15f01ba328.png)](../assets/images/standing/20261021/47aac548de3f7796ee9e2b50d2c9828342bcd041a4900374c392419d7d1a7a35.png) | **cell 09 · 眼睛局部** [![cell 09 · 眼睛局部](../assets/images/standing/20261021/013ecaa4e85e6cd3a796d6b66e419adfaa58bf16c8bc28f01788e4ecd9b47a44.png)](../assets/images/standing/20261021/03cc0ec6cfd0790587e147d99921be2dec21f8f184c6b6a9cc75f4f8bd5ad1fb.png) |
| **cell 10 · 眼睛局部** [![cell 10 · 眼睛局部](../assets/images/standing/20261021/058403b25af5bfc8b8e3c97315afef165b333ec4ea23bf21689990ed8c7b62dd.png)](../assets/images/standing/20261021/e6a83be62db7a89bfd2d985b73baadf24a035aaff137109bbf516b745abb23ba.png) | **cell 11 · 眼睛局部** [![cell 11 · 眼睛局部](../assets/images/standing/20261021/d18a6dcb52a54349689ee00fda287c929299abe39f568a8e187d4759c92b3b79.png)](../assets/images/standing/20261021/7eb1172fabb5cf34b7afcc92f0b5082b86ab3d097d9ab5d72092eda7e320f548.png) |
| **cell 12 · 眼睛局部** [![cell 12 · 眼睛局部](../assets/images/standing/20261021/595b9533a97de9cb0116e47c8e82fd81369b940b61d4086a09700baf59008a12.png)](../assets/images/standing/20261021/f5e1ae225d2f59102cbae545c0329619c789768b114ea3d67f986f7832901066.png) | — |

## 回绕时暂停两端

把循环末尾和开头分别暂停，比较手、衣摆、腿、头和投影的共同位移。它们都随姿态改变时，先识别Step切换；如果角色已到新姿态而影子仍在旧位置，再排查深度渲染与坐标更新。

| 对照 | 对照 |
|---|---|
| **回绕前cell12** [![回绕前cell12](../assets/images/standing/20261021/88b21ecb2cfa0b73dcb5f97d3d53ccd5e7f73c177107e6f0d4977a997ba332b6.png)](../assets/images/standing/20261021/88b21ecb2cfa0b73dcb5f97d3d53ccd5e7f73c177107e6f0d4977a997ba332b6.png) | **回绕后cell00** [![回绕后cell00](../assets/images/standing/20261021/cf05441ff809410ab9d47fef6c3b6bc1e2817dfd99e4e5bb01c26d47ecd85937.png)](../assets/images/standing/20261021/cf05441ff809410ab9d47fef6c3b6bc1e2817dfd99e4e5bb01c26d47ecd85937.png) |

同镜头、同材质、不同姿态；两端有明显变化，不代表角色动画完全平滑，也不能单凭变化像素数断言某个Shader分支错误。

## 继续排查

若同姿态仍不稳定，保持姿态冻结，按环境→输入→区域→漫反射→spec/rim→线条→时序的顺序排查。投影可进一步查看深度精度和自阴影；细线要在目标分辨率、HDR/MSAA和实际设备上观察。更换UV或模型则先重新制作区域，而不是沿用图集常量继续微调。

[返回画面排错步骤](../chapters/14.md) · [投影与眼睛同条件对照](experiments-20261021.md)
