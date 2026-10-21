# 新增教学示例：Debug窗口

`RenderingTutorialDebugWindow.cs`是独立教学代码，不是原工程实测源码，**尚未在Unity编译或运行验证**。它给练习材质设置`_DebugMode`，只读查询Renderer浮点MPB来源和现有阴影组件状态，不提供呈现桥接、深度渲染或资源。

复制到自己的练习工程`Assets/Editor/`，等待脚本编译，在`Tools > Rendering Tutorial > Debug View`打开。详细操作、参数恢复和MPB限制见[练习操作方法](../../docs/reference/practice.md)。它不修改动画、Transform、骨骼、网格或Bind Pose。
