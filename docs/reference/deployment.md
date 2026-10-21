# 构建、审阅与 GitHub Pages

本交付通过分支和Pull Request供审阅，不自动合并。2026-10-21已用GitHub API将本仓库Pages设为 `build_type=workflow`，API核实成功；实际项目地址当前返回HTTP404，**教程尚未上线**，等待PR审阅合并后的首次部署。

## 两条工作流

- **文档检查**：pull_request、main推送和手动触发执行原包/来源核查、MkDocs严格构建、HTML链接及子路径检查，上传docs-preview构建产物供下载。
- **部署教程到Pages**：main推送或手动触发；build和deploy都限制在仓库默认分支。PR只检查，不发布未合并内容。部署使用configure-pages、upload-pages-artifact、deploy-pages，权限限于相应job。

PR构建产物是静态文件，不是公开预览URL；下载后在目录运行 `python -m http.server 8000` 可检查。正文相对链接由MkDocs转换，站内资源不以网站根 `/assets/` 硬编码，兼容项目子路径。

## 仓库启用步骤

1. 本次已配置为GitHub Actions。可在仓库 **Settings → Pages → Build and deployment → Source** 核实；若迁移或重建仓库，在这里选择 **GitHub Actions**，无需手动创建gh-pages分支。
2. 审阅PR并合并到main；main推送会运行部署。若已合并但未自动运行，在 **Actions → 部署教程到Pages → Run workflow** 选择main。
3. 如github-pages环境有保护规则，按仓库已有流程批准该次部署。若Actions被仓库策略禁用，先由有权限者启用相应工作流。
4. 以deploy-pages输出的page_url为实际发布地址，访问首页、章节和图片核实成功；在此之前不把配置地址当作已经上线。

配置的预期地址为 [GitHub Pages项目地址](https://xuu-xuu-xuu.github.io/Guilty-Gear_Rendering_imitate/)，这是仓库命名决定的**目标地址**，当前审阅版不声称可访问。site_url仅用于正确生成项目路径和元数据。

操作依据[GitHub官方自定义工作流文档](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。主题配置参照[Material设置](https://squidfunk.github.io/mkdocs-material/setup/)，严格校验参照[MkDocs配置](https://www.mkdocs.org/user-guide/configuration/)。

## 本地命令

Python3.12激活专用虚拟环境后：

```sh
python -m pip install -r requirements-docs.txt
python tools/verify_docs.py
python -m mkdocs build --strict
python tools/check_site.py
python -m mkdocs serve
```

更改作者文本后运行 `python tools/write_chapters.py`；更改生成规则后运行 `python tools/prepare_reference.py`。原资料只读；需要新证据时另开目录并记录来源，不能修改快照补洞。CI重新生成并比较，确保已提交Markdown可直接在GitHub阅读。

`.gitattributes`将原始资料目录设为 `-text`，避免Windows新克隆时自动换行转换破坏原始SHA256；新增文档/配置使用LF。这只规定检出方式，不修改任何原始资料字节。

## 交付检查记录

2026-10-21本地实际执行：

| 检查 | 结果与范围 |
|---|---|
| MANIFEST与Git基线 | 57项大小/SHA256通过，MANIFEST自身与原提交逐字节相同；共58文件，资料目录无差异 |
| 源码/参数 | 35个连续摘录原文一致；165项属性名称/类型/默认/行号；793行参数与12份保存JSON交叉核对；44个Debug表达式及运行写入行匹配 |
| 生成一致性 | 15章与附录重新生成后无变化，已提交Markdown可直接阅读 |
| 图片及禁止资源 | 21张白名单PNG与清单哈希一致；没有新增模型、原贴图、自制遮罩像素、动画、音频或视频 |
| Markdown链接 | 本地相对目标存在；没有本机盘符路径；准确数量由verify_docs日志输出 |
| 依赖 | Python3.12专用虚拟环境安装固定直接依赖；pip check无损坏依赖 |
| 严格构建 | MkDocs1.6.1 + Material9.7.7，mkdocs build --strict退出0，39个HTML页面；无MkDocs文档诊断警告/错误 |
| 构建产物 | 5968个本地链接/资源/锚点检查通过，235条搜索索引；普通页相对资源，404页使用正确项目前缀 |
| 桌面/手机 | Chrome155，1440×1000与390×844，分别检查首页、10章、参数附录、源码索引；无文档横向溢出、坏图或JS/HTTP错误；表格单独横向滚动；大腿中文搜索与手机抽屉导航通过 |
| 人工看图 | 实看桌面章节/参数表、手机首页/参数表截图，确认文字、并排/堆叠图片与表格可读；截图仅作本地QA，不混入渲染图片白名单 |
| Pages状态 | GitHub API返回Pages配置成功，build_type=workflow；实际地址HTTP404，等待合并后首次发布 |

Material启动时另印有关于未来MkDocs2.0的上游提示；本项目固定使用1.6.1，严格构建本身未产生文档警告。上述浏览器检查只在本地构建产物进行，尚非线上部署检查。

Unity编译、Play、GPU性能与站立循环复测均未执行；对应待补见[证据附录](evidence.md)。远端PR工作流结论以PR Checks实际记录为准，不能用本地结果冒充。
