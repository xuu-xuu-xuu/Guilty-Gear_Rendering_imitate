"""Generate rendering references from immutable source/data, without process prose."""
import csv
import hashlib
import json
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
PACK=ROOT/'rendering-tutorial-source-pack'
REF=ROOT/'docs/reference'

def read_json(name):return json.loads((PACK/name).read_text(encoding='utf-8-sig'))
def rows(name):
    with (PACK/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(path,body):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='\n') as f:f.write(body.rstrip()+'\n')
def cell(value):
    return str(value).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('`','&#96;').replace('\n',' ')
def table(headers,data):
    return '| '+' | '.join(headers)+' |\n|'+'|'.join('---' for _ in headers)+'|\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in data)+'\n'
def verify_pack():
    manifest=read_json('MANIFEST.json');expected={x['path'] for x in manifest}|{'MANIFEST.json'}
    actual={x.relative_to(PACK).as_posix() for x in PACK.rglob('*') if x.is_file()}
    assert actual==expected,(actual-expected,expected-actual)
    for x in manifest:
        data=(PACK/x['path']).read_bytes()
        assert len(data)==x['bytes'] and hashlib.sha256(data).hexdigest()==x['sha256'],x['path']
    return len(manifest)

def value(text):
    v=json.loads(text)
    if isinstance(v,dict) and set(v)=={'r','g','b','a'}:return '('+', '.join(str(v[k]) for k in ['r','g','b','a'])+')'
    if isinstance(v,dict) and 'path' in v:return f"{v['path']}；Tiling={v.get('scale')}；Offset={v.get('offset')}"
    return '未保存' if v is None else str(v)

def generate():
    count=verify_pack()
    for source in rows('data/source_index.csv'):
        name=Path(source['package']).name;lines=(PACK/source['package']).read_text(encoding='utf-8-sig').splitlines()
        assert len(lines)==int(source['lines'])
        body=f'# {name}\n\n按行查找正文中的函数与Pass。以下保留源码原文，属性拼写与分支顺序以此为准。代码依赖所用渲染管线及[输入连接](../dependencies.md)，不能把文件索引当作独立工程。\n\n| 行 | 代码 |\n|---|---|\n'
        body+=''.join(f'| <a id="l{n}"></a>{n} | <code>{cell(line)}</code> |\n' for n,line in enumerate(lines,1))
        write(REF/'code'/f'{name}.md',body)
    mp=rows('data/material_parameters.csv')
    body='# 材质参数参考\n\n先在对应章节调整关键参数，再用本表查完整值。Shader默认值是新材质起点，材质设置是示例角色的保存配置；Renderer MPB和全局输入仍可能覆盖同名字段，见[参数层级](overrides.md)。Color和Vector按类型使用，数值不是最终屏幕取色。未保存不等于0。\n\n'
    order=['Base_Imitate','BaseSecondary_Imitate','BodyBaseFlip_Imitate','CoatExterior_Imitate','StageFloorReceiver','StageWallReceiver','BodyDecal_Imitate','HeadDecal_Imitate','HeadGlow_Imitate']
    for material in order:
        body+=f'## {material}\n\n'+table(['属性','类型','Shader默认','材质设置'],[[r['property'],r['type'],value(r['shaderDefault']),value(r['savedValue']) if r['savedPresent']=='True' else '未保存'] for r in mp if r['material']==material])
    write(REF/'parameters.md',body)
    props=rows('data/shader_properties.csv')
    body='# 属性名称与类型\n\n按原属性名赋值，区分Float、Range、Vector、Color和纹理。点击行号查看声明；_LightTreshold保留源码拼写。\n\n'
    body+=table(['Shader','属性','面板名称','类型','默认值','声明'],[[Path(r['shader']).name,r['property'],r['label'],r['type'],value(r['default']),f"[第{r['line']}行](code/{Path(r['shader']).name}.md#l{r['line']})"] for r in props])
    write(REF/'property-declarations.md',body)
    debug=rows('data/debug_outputs.csv')
    body='''# 选择Debug分量排查画面

先选能隔离问题的分量，检查完恢复0。面板范围是0–24，frag支持1–44；高编号通过材质或MPB的SetFloat赋值。下面是API调用示意，不是完整组件：

```csharp
material.SetFloat("_DebugMode", 44f);
// 查看后恢复最终画面
material.SetFloat("_DebugMode", 0f);
```

| 要看什么 | 编号 | 注意 |
|---|---|---|
| 纹理和顶点输入 | 1–9 | 7是ILM.A，8是顶点R |
| 头体区域/材质类别 | 22 / 25 | 38是CleanShade覆盖，不能代替22 |
| 最终漫反射 | 16 | 10仍是基础band，不是最终diffuse |
| 最终高光 | 13 | 26–29不含Focused/Thigh的最后替换 |
| 边缘光 | 12 | 与正面高光分开看 |
| 内部线 | 30 / 31 | Debug会裁掉外轮廓，外壳回0看 |
| 眼睛区域/贡献 | 33 / 34 | 34不是最终显示颜色的增亮量 |
| 大腿替换域/形状 | 43 / 44 | 没乘_ThighLobeEnabled，不能证明开关打开 |

19/20的变量未接入最终颜色；32、35、36是后续可能被CleanShade替换的基础脸部贡献。不要用它们代替16判断最终脸色。

## 输出表达式

'''
    body+=table(['编号','源码返回值','位置'],[[r['mode'],r['expression'],f"[BridgetToon.shader:{r['line']}](code/BridgetToon.shader.md#l{r['line']})"] for r in debug])
    write(REF/'debug.md',body)
    tx=read_json('data/texture_import_settings.json')
    tx={k:v for k,v in tx.items() if not Path(k).name.startswith('BGTW_')}
    body='''# 贴图连接与导入设置

先按[通道用途](channels.md)判断颜色纹理与数据纹理，再设置Inspector。Filter Mode数值1为Bilinear，Wrap数值0为Repeat、1为Clamp；null表示没有可用字段，不能据此设置成0。

平台overridden=0时，该条不是生效的覆盖；textureFormat=-1也不直接说明最终GPU格式。保留MipMap和Alpha数据，随后在目标平台查看实际导入结果。

'''
    body+=table(['纹理','尺寸','sRGB','MipMap','Filter / Aniso','Wrap U/V/W','Alpha Is Transparency','Max Size'],[[Path(k).name,'×'.join(map(str,v['size'])),v['sRGB'],v['mipmaps']['enableMipMap'],f"{v['textureSettings']['filterMode']} / {v['textureSettings']['aniso']}",'/'.join(str(v['textureSettings'][x]) for x in ['wrapU','wrapV','wrapW']),v['alphaIsTransparency'],v['maxTextureSize']] for k,v in tx.items()])
    for k,v in tx.items():
        body+=f"## {Path(k).name}\n\n"
        body+=table(['平台','启用覆盖','Max Size','格式枚举','压缩枚举','质量','Crunch','Alpha Split'],[[r.get(x) for x in ['buildTarget','overridden','maxTextureSize','textureFormat','textureCompression','compressionQuality','crunchedCompression','allowsAlphaSplitting']] for r in v['platformSettings']])
        body+=table(['采样设置','值'],[[x,v['textureSettings'][x]] for x in ['filterMode','aniso','mipBias','wrapU','wrapV','wrapW']]+[['alphaSource',v['alphaSource']],['alphaIsTransparency',v['alphaIsTransparency']]]+[[x,v['mipmaps'][x]] for x in v['mipmaps']])
    bindings=[r for r in rows('data/texture_bindings.csv') if r['material']!='Weapon_Imitate']
    body+='## 材质连接\n\n'+table(['材质','Shader纹理槽','资源引用','Tiling','Offset'],[[r[k] for k in ['material','slot','texture','tiling','offset']] for r in bindings])
    write(REF/'texture-imports.md',body)
    # Keep exact source mappings and previously published raw downloads outside
    # the reader narrative. The verification scripts continue to check them.
    copied=[]
    for im in read_json('data/images_manifest.json'):
        dest=ROOT/'docs/assets'/im['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(PACK/im['path'],dest)
        copied.append({'document_path':dest.relative_to(ROOT).as_posix(),**im})
    for folder,code in [('rendering-ab-20261021','RenderingEvidenceCapture.cs'),('standing-render-20261021','StandingRenderStabilityCapture.cs')]:
        source=ROOT/'evidence'/folder;copied.extend(json.loads((source/'images.json').read_text(encoding='utf-8')))
        dest=ROOT/'docs/assets/evidence'/folder;dest.mkdir(parents=True,exist_ok=True)
        for p in source.glob('*.json'):shutil.copyfile(p,dest/p.name)
        shutil.copyfile(ROOT/'examples/capture'/code,dest/'capture-code.txt')
    write(ROOT/'docs/assets/image-provenance.json',json.dumps(copied,ensure_ascii=False,indent=2))
    print(f'Generated rendering references; {count}+1 immutable inputs checked.')

if __name__=='__main__':generate()
