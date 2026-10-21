# Unity 罪恶装备风格角色渲染复刻：从基础明暗到材质高光与线条

![原工程历史最终效果](docs/assets/images/project/final.png)

原工程历史验收，2026-10-20，非Debug，含投影；来源 `thigh_highlight_20261020/verified_play_2.png`。此图没有同条件开关配对，与4K副本不能直接作单变量A/B。新采集的[投影与眼睛静态实测](docs/reference/experiments-20261021.md)与[站立循环Play验收](docs/reference/standing-stability-20261021.md)分别登记，不扩大历史图的证明范围。

## 阅读入口与范围

- **[教程首页与00–14章导航](docs/index.md)**：GitHub内直接阅读，同一Markdown用于网站。
- [先看章节—证据表](docs/reference/evidence-map.md)，再看[参数/覆盖](docs/reference/overrides.md)、[输入契约](docs/reference/channels.md)。
- **[在线教程](https://xuu-xuu-xuu.github.io/Guilty-Gear_Rendering_imitate/)**：PR #1已于2026-10-21合并，GitHub Pages首次部署成功。[Pages配置与部署说明](docs/reference/deployment.md)记录检查范围与后续发布方法。
- 适用记录：Unity **2022.3.62f3c1、Built-in、Linear**。默认读者已有模型、贴图与正常站立动画。

范围仅限渲染：两段式明暗、分区和配色、阴影路径、材质及大腿高光、线条、眼睛、边缘光和站立渲染稳定性。没有解包、骨骼修复、动画移植、Bind Pose或控制器重建内容。

源码快照**不是独立可运行工程**；未附模型、纹理像素、动画、场景及原有呈现桥接类型。缺少的截图/实测均[明确列出](docs/reference/evidence.md)，不使用生成资源冒充。文档构建通过不等于Unity编译或渲染验收通过。

## 学习路线

01–04建立环境/输入/覆盖与执行顺序 → 05–07明暗和配色 → 08–10阴影及质感 → 11–13线条、眼睛与rim → 14静态分量与站立循环检查。章节顺序与Shader计算顺序分别说明。

完整参数账本、44种Debug输出、9份源码逐行索引、21张图片来源均在[核查附录](docs/index.md)。原始 [rendering-tutorial-source-pack/](rendering-tutorial-source-pack/) 保持字节不变，不自动授予整体MIT等许可证；见[来源和第三方内容说明](THIRD_PARTY_NOTICES.md)。

2026-10-21新增：隔离完整工程中的23次真实Unity静态捕获，按哈希去重为12张原生PNG，另有2张无修饰眼睛裁切。墙/地接收单属性A/B、最终眼睛开关近景与重复帧/局部性已有实测；[新增采集器](examples/capture/README.md)和独立证据目录随PR提交，原始资料不变。后续已补[站立循环真实Play验收](docs/reference/standing-stability-20261021.md)：456条受控帧、122条正常主相机帧，覆盖13cell、跨8次回绕；同姿态重复与首次/下一帧一致。91张原生PNG及13张精确裁切独立登记。不同姿态的Step变化、5种未观察实时tick、跨设备/HDR/MSAA与通用适配等限制仍明确保留。

## 本地预览与检查

使用Python 3.12。以下命令在仓库根目录执行；Windows激活命令是 `.venv-docs\Scripts\Activate.ps1`，macOS/Linux是 `source .venv-docs/bin/activate`。

```sh
python -m venv .venv-docs
# 按上文激活虚拟环境后继续
python -m pip install -r requirements-docs.txt
python tools/verify_docs.py
python -m mkdocs build --strict
python tools/check_site.py
python -m mkdocs serve
```

打开终端显示的本地预览地址。该地址只用于本地预览，不是线上站点。

维护正文时编辑 `tools/write_chapters.py` 中的作者文本，然后运行 `python tools/write_chapters.py`；引用/表格/图片由 `python tools/prepare_reference.py` 从只读快照生成。提交生成结果，让GitHub无需插件即可阅读。CI会重新生成并比较，防止正文摘录、参数表与源数据悄悄偏离。构建记录见[交付检查](docs/reference/deployment.md)。
