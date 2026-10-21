"""Build read-only derived reference pages; never write to the source pack."""
import csv
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'rendering-tutorial-source-pack'
REF = ROOT / 'docs/reference'

def read_json(name):
    return json.loads((PACK / name).read_text(encoding='utf-8-sig'))

def rows(name):
    with (PACK / name).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='\n') as f:
        f.write(body.rstrip() + '\n')

def cell(value):
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('`', '&#96;').replace('\n', ' ')

def table(headers, data):
    return '| ' + ' | '.join(headers) + ' |\n|' + '|'.join('---' for _ in headers) + '|\n' + ''.join('| ' + ' | '.join(cell(v) for v in row) + ' |\n' for row in data) + '\n'

def verify_pack():
    manifest = read_json('MANIFEST.json')
    expected = {x['path'] for x in manifest} | {'MANIFEST.json'}
    actual = {x.relative_to(PACK).as_posix() for x in PACK.rglob('*') if x.is_file()}
    assert actual == expected, (actual - expected, expected - actual)
    for entry in manifest:
        b = (PACK / entry['path']).read_bytes()
        assert len(b) == entry['bytes'], entry['path']
        assert hashlib.sha256(b).hexdigest() == entry['sha256'], entry['path']
    return len(manifest)

def generate():
    count = verify_pack()
    matrix = json.loads((ROOT/'tools/chapter_map.json').read_text(encoding='utf-8'))
    body = '# 章节、源码与证据对应表\n\n此表先于初版正文建立。行号指原资料快照；参数表是磁盘保存值，运行规则是源码推导。原图与播放报告来自2026-10-20；[新增实验](experiments-20261021.md)为2026-10-21隔离副本的真实Unity静态渲染，不能扩展为Play或全新工程复刻验证。\n\n'
    body += table(['章节', '源码位置', '参数来源', '效果图', '验证证据与限制'], [
        [f"{c['id']} {c['title']}", '; '.join(f"{r[0]}:{r[1]}–{r[2]}" for r in c['refs']), c['parameters'], ', '.join(c['images']) or '待补专用诊断图', c['evidence']] for c in matrix])
    body += f'完整性基线：MANIFEST 覆盖 {count} 个文件；MANIFEST 自身是第 58 个文件，不能自证哈希，由 Git 基线及原 ZIP 逐字节比较补足。\n\n'
    body += '## 核实后的说明差异\n\n- notes/06_gpt_handoff.txt 要求先交示范章确认；本次用户明确要求直接完成全套，按本次请求执行。\n- notes/01_inventory.txt 的“12 个材质”对应 materials_saved.json；material_parameters.csv 只有 10 个有已声明属性的材质、793 行，不能把没有属性的辅助材质虚构成完整参数行。\n- notes 的执行顺序把外轮廓放在最后，适合作为阅读概览；源码实际是独立 OUTLINE Pass，SHADOWCASTER 由 Unity 阴影调度，不能当作 frag 内的末尾语句。\n- notes 称环境为 4× MSAA：这是活动 Profile 写入值和 Ultra 保存档，并非每个质量档都相同。\n- notes 的“分区开启”是源码规则与 strength=1 的组合推断；原资料采集未采样运行中MPB；本轮隔离副本静态采样另见新增实验。\n- 保存场景部分 Prefab fileID 未解析；历史 Renderer 列表可交叉参照，不能据此宣称已还原当前实例。\n- BGTW_ilm 的 sRGB=1 保留为事实，不能推广为推荐设置。\n- shade_after 与 thigh_before 哈希相同；这是同一历史画面复用，不能当成两次独立验证。\n'
    write(REF/'evidence-map.md', body)
    for source in rows('data/source_index.csv'):
        name = Path(source['package']).name
        lines = (PACK/source['package']).read_text(encoding='utf-8-sig').splitlines()
        assert len(lines) == int(source['lines'])
        body = f"# {name} 逐行索引\n\n原文件：`{source['package']}`；原工程路径：`{source['source']}`。\n\nSHA256：`{source['sha256']}`。以下由原文生成，未修正拼写或分支。每行锚点用于正文核查；这是源码摘录索引，不是可直接运行工程。\n\n"
        body += '| 行 | 原文 |\n|---|---|\n'
        for n, line in enumerate(lines, 1):
            body += f'| <a id="l{n}"></a>{n} | <code>{cell(line)}</code> |\n'
        write(REF/'code'/f'{name}.md', body)
    mp = rows('data/material_parameters.csv')
    body = '# 完整材质与属性账本\n\n由 material_parameters.csv 自动转录，共 793 行、10 个材质。材质名、类型、默认值、保存值及保存字段是否存在逐列保留；没有保存字段时不能把空值当成 0。Color 与 Vector 即使以 r/g/b/a 序列化，也必须按类型解释。运行写入和内部覆盖另见[覆盖规则](overrides.md)。数值不是屏幕取色。\n\n'
    for material in sorted({r['material'] for r in mp}):
        body += f'## {material}\n\n' + table(['属性','类型','Shader 默认','材质保存','savedPresent'], [[r[k] for k in ['property','type','shaderDefault','savedValue','savedPresent']] for r in mp if r['material']==material])
    write(REF/'parameters.md', body)
    saved=read_json('data/materials_saved.json')
    body='# 12份材质保存原貌\n\n来自 materials_saved.json，完整保留保存字段、历史冗余属性、纹理引用和未知Shader。793行声明属性账本只含10个可对应材质；不要把历史保存字段误当Shader当前仍读取的属性。StageShadowReceiver的shader=null，不能自动当作同名StageShadowReceiver Shader已解析。\n\n'
    for name,value in saved.items():
        body+=f'## {name}\n\n```json\n'+json.dumps(value,ensure_ascii=False,indent=2)+'\n```\n\n'
    write(REF/'material-snapshots.md',body)
    props = rows('data/shader_properties.csv')
    write(REF/'property-declarations.md', '# Shader 属性声明\n\n从 shader_properties.csv 转录；保留原列名与声明行号。\n\n'+table(list(props[0]),[[r[k] for k in props[0]] for r in props]))
    debug = rows('data/debug_outputs.csv')
    write(REF/'debug.md', '# Debug 输出索引\n\n面板 Range(0,24)，frag 实现 1–44；0 返回最终颜色。独立练习副本中可通过 Material.SetFloat("_DebugMode", 44f) 设置，使用后恢复 0。该调用仅示意 API，不是完整脚本，也未在 Unity 验证。Debug 会裁掉 OUTLINE Pass。\n\n10 是旧 band，16 是经过重建后的 diffuse；19/20 的诊断项未接入最终颜色。26–29 不包含最后 Focused/Thigh 修正，要看 13。32 是早期 hairFaceOcclusion，不能证明最终 CleanShade 漫反射仍含投脸。35/36 也是替换前的旧脸部贡献。43 为替换域，44 为域内形状与朝向门控，两者均没有乘 _ThighLobeEnabled，不能仅凭其非黑判断最终开关。\n\n'+table(list(debug[0]),[[r[k] for k in debug[0]] for r in debug]))
    images = read_json('data/images_manifest.json')
    copied = []
    body = '# 图片来源与比较条件\n\n原有21张图片仅从不可变资料包的images_manifest.json复制，均为历史产物。新增14张图片（12张去重后的Unity原生PNG、2张无修饰裁切）单独登记在evidence/rendering-ab-20261021/images.json，详见[新实验](experiments-20261021.md)。两份清单分开维护，原资料包不变；本文不将新图冒充原白名单旧图。\n\n'
    body += '9 张阶段图固定镜头与站立 cell 00，累计效果；刻意去掉角色投影，投影矩阵 m00/m11 ×0.94，4K 描边像素宽度 ×2。原工程保存宽度仍为 0.8/0，不能抄成 1.6/0。阶段图彼此可解释累计变化，不能证明每个参数独立影响，更不能与 project 图作单变量 A/B。\n\n'
    for im in images:
        dest = ROOT/'docs/assets'/im['path']
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(PACK/im['path'], dest)
        assert hashlib.sha256(dest.read_bytes()).hexdigest()==im['sha256']
        copied.append({'document_path':dest.relative_to(ROOT).as_posix(), **im})
        name=im['path'][len('images/'):]
        body += f"## {name}\n\n[查看图片](../assets/{im['path']}) · {im['size'][0]} × {im['size'][1]}\n\n- 原产物：`{im['origin']}`。\n- 来源类别：{im['kind']}。\n- 原始图注：{im['caption']}。\n- Debug：{'是，编号见原始图注' if 'Debug' in im['caption'] else '否'}。\n- 比较条件："
        if '/stages/' in im['path']:
            body+='同镜头、同姿势累计阶段；已知差异为效果组累计及副本构图/投影/线宽。\n'
        elif 'thigh_before' in name or 'thigh_after' in name:
            body+='清单明确记录的 thigh lobe OFF/ON 控制对；属于历史条件，未在本次重跑。\n'
        elif 'shade_' in name:
            body+='阴影与高光同时改变的历史对照，不能归因于仅阴影改变。\n'
        else:
            body+='诊断或效果展示；清单未给出同条件单变量对照，不擅自配对。\n'
        body+=f"- SHA256：`{im['sha256']}`。\n\n"
    supplemental=ROOT/'evidence/rendering-ab-20261021/images.json'
    if supplemental.exists():
        body+='## 2026-10-21新增实验登记\n\n下表每一行是一个实际捕获或裁切记录；重复帧和相同结果按哈希复用同一个PNG，原生23次捕获只存12张不同PNG，加2张裁切。来源为当前完整工程的隔离副本，Edit已保存站立姿态，不是原工程历史图或4K演示图。HDR关闭、RT单采样，与旧图的抗锯齿条件不同，不跨批次做A/B。\n\n'
        extra=json.loads(supplemental.read_text(encoding='utf-8'))
        body+=table(['记录','文档图片','Debug','唯一变量','数值','裁切'],[[r['record'],r['document_path'],r['debug'],r['variable'],r['value'],r.get('cropBoxXYXY','无')] for r in extra])
        copied.extend(extra)
        for source in supplemental.parent.glob('*.json'):
            dest=ROOT/'docs/assets/evidence/rendering-ab-20261021'/source.name
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(source,dest)
        shutil.copyfile(ROOT/'examples/capture/RenderingEvidenceCapture.cs',ROOT/'docs/assets/evidence/rendering-ab-20261021/capture-code.txt')
    write(REF/'images.md', body)
    write(ROOT/'docs/assets/image-provenance.json', json.dumps(copied,ensure_ascii=False,indent=2))
    tx = read_json('data/texture_import_settings.json')
    body = '# 贴图导入与绑定完整表\n\n本页只有接口元数据，没有纹理像素。数据来自 texture_import_settings.json 与 texture_bindings.csv。filterMode=1 是 Bilinear；wrap=0 是 Repeat、1 是 Clamp；null 代表未采到字段，不能推断实际值。平台条目 overridden=0 时不是启用的平台覆盖。保留压缩枚举数值，不凭记录推断最终 GPU 压缩格式。\n\n'
    body += table(['纹理路径','尺寸','sRGB','MipMap','filter/aniso','wrap U/V/W','alphaIsTransparency','maxTextureSize'],[[k,'×'.join(map(str,v['size'])),v['sRGB'],v['mipmaps']['enableMipMap'],f"{v['textureSettings']['filterMode']}/{v['textureSettings']['aniso']}",'/'.join(str(v['textureSettings'][x]) for x in ['wrapU','wrapV','wrapW']),v['alphaIsTransparency'],v['maxTextureSize']] for k,v in tx.items()])
    for k,v in tx.items():
        body+=f'## {Path(k).name}\n\n' + table(list(v['platformSettings'][0]),[[r[x] for x in v['platformSettings'][0]] for r in v['platformSettings']])
        body+='完整采样及 Alpha 元数据：\n\n```json\n'+json.dumps({x:y for x,y in v.items() if x!='platformSettings'},ensure_ascii=False,indent=2)+'\n```\n\n'
    bindings=rows('data/texture_bindings.csv')
    body+='## 材质纹理绑定\n\n'+table(list(bindings[0]),[[r[k] for k in bindings[0]] for r in bindings])
    write(REF/'texture-imports.md',body)
    print(f'Pack verified: {count} manifest entries + MANIFEST; references and {len(images)} whitelist images generated.')

if __name__=='__main__':
    generate()
