# 新增：真实Unity渲染证据采集器

`RenderingEvidenceCapture.cs`是新增Editor采集工具，不属于不可变资料包，也不是通用渲染适配器。已在2022.3.62f3c1、Built-in/Linear、D3D11的完整工程隔离副本中编译并执行；没有进入Play，没有采样或改写动画/骨骼/网格/Bind Pose/控制器。本次使用已保存的站立frame0呈现。

仍需原工程现有类型及合法持有的完整资源；资料包不含这些输入，所以不能只克隆公开仓库运行。通用适配与全新空工程复刻仍待补。

## 隔离与前提

1. 复制完整工程的Assets、Packages、ProjectSettings到全新临时工程，保持.meta与GUID。复制后核对文件哈希；原工程仅只读，不在原工程安装采集器。
2. 在副本省略Assets/Editor下的GgstAnimationBindingFix、GgstImitateWorkbench、GgstReferenceSampler三个请求文件自动化工具及其.meta，避免执行无关命令。渲染源码、材质、纹理和保存场景不修改。其余原有类型仍需保留。
3. 将采集器放到副本Assets下的Editor目录。在副本根目录建立 `EvidenceCaptureIsolation.marker`，内容精确为 `rendering-only-evidence-20261021`。
4. 设置环境变量 `GGST_EVIDENCE_OUTPUT` 为独立输出目录，不能放在Assets。使用Unity批处理，保留真实图形设备，不添加 `-nographics`。

```text
Unity -batchmode -projectPath <隔离工程> -executeMethod RenderingEvidenceCapture.Run -logFile <独立日志文件> -force-d3d11
```

这是命令结构示意；Unity可执行位置由使用者环境决定。Run会检查批处理、隔离标记、保存相机隐式投影、站立头可见性、MPB与阴影发布。它不会调用ShowFrame、StartManual或进入Play。不能拿另一个模型直接替代这些引用。

## 捕获内容与控制

- 墙与地面分别只改变该Renderer MPB的 `_GeometryShadowFloor`：1与保存值0.1/0.08；另一个接收面不动。阴影图继续生成，避免关闭自定义投影而回退内置阴影造成歧义。
- `drawStageCasters`单独对照：关闭时接收器回退内置SHADOW_ATTENUATION，此组只能标“自定义/后备路径比较”，不能标“全部投影关闭”。
- 站立头MPB的 `_EyeRefineEnabled`只改0/1；Debug0、13、30、33、34分别成对比较。脸近景使用同一3.5倍投影取景矩阵，两张相同；没有移动相机Transform或改变姿态。
- `drawHairCasters`单独对照最终脸和Debug32，记录当前最终配置中的无差异结果，不为获得明显变化修改材质。
- 所有捕获1600×900、ARGB32、RT单采样，camera HDR/MSAA关闭；全局质量MSAA仍为4。重复帧、深度图统计和全场Transform/Renderer/Light指纹用于检测漂移。
- finally恢复MPB、相机target/HDR/MSAA/aspect、隐式投影与caster标志，输出restoration.json。成功标志必须同时满足采集、恢复、像素审计与磁盘哈希核对，不能只看completed。

原生23次捕获按SHA256去重后保存12张PNG；眼睛另作两张精确矩形裁切，没有缩放、锐化、重绘或颜色修饰。[实验附录](../../docs/reference/experiments-20261021.md)解释比较边界。

## 公开证据如何复核

```sh
python -m pip install -r requirements-docs.txt
python tools/verify_experiments.py
```

这会重算已发布图片的像素差、重复帧、眼区局部性、裁切与来源哈希，并核对导出的恢复/输入证据；它不重新执行Unity，也不能证明任意姿态或设备都成立。公开仓库只包含渲染PNG与数值证据，不包含私有工程副本、模型、纹理像素、动画或完整Editor日志。
