"""Generate practical chapters with exact source excerpts and material values."""
import json
from prepare_reference import ROOT,PACK,rows,write,table
from reader_content import CHAPTERS

ORDER=['00','01','02','03','04','08','05','06','07','12','09','10','13','11','14']
MATERIALS=['Base_Imitate','BaseSecondary_Imitate','BodyBaseFlip_Imitate','CoatExterior_Imitate']
SHORT=['Base','Secondary','Flip','Coat']

def standing_image(kind,cell):
    base=ROOT/'evidence/standing-render-20261021'
    capture=json.loads((base/'controlled.json').read_text(encoding='utf-8'))
    mapping=json.loads((base/'image-map.json').read_text(encoding='utf-8'))
    record=next(r for r in capture['samples'] if r['kind']==kind and r['cell']==cell)
    return mapping[record['image']].removeprefix('docs/assets/images/')

def picture(path,label,link=None,prefix='../assets/images/'):
    return f'**{label}** [![{label}]({prefix}{path})]({prefix}{link or path})'

def pair(left,right):
    return '| 对照 | 对照 |\n|---|---|\n| '+left+' | '+right+' |\n\n'

def figures(number):
    single={
        '00':('project/final.png','完整角色效果，Debug0'),
        '01':('project/final.png','主光、环境与投影共同作用的画面'),
        '02':('stages/00.png','基础色示意，不是纹理通道导出'),
        '03':('project/region_debug.png','Debug38：CleanShade覆盖范围'),
        '04':('stages/08.png','漫反射、高光、边缘光与线条的合成示意'),
        '07':('stages/03.png','区域配色示意'),
        '13':('project/rim_debug.png','Debug12：单独查看rim'),
    }
    if number in single:
        path,label=single[number];body=picture(path,label)+'\n\n'
        if path.startswith('stages/'):
            body+='此组累计效果示意固定姿态，省略角色投影，并调整了构图和4K描边像素宽度；用于认识该层外观，不是单个参数的独立开关对照。\n\n'
        elif number=='03':body+='该图只说明CleanShade覆盖；头体分区请在自己的材质中使用Debug22。\n\n'
        elif number=='13':body+='这是诊断分量，不是最终屏幕颜色，也不能据此判断外描边。\n\n'
        return body
    if number=='05':
        return pair(picture('stages/00.png','基础色'),picture('stages/01.png','两段式明暗示意'))+'两图是累计效果示意：姿态相同，但不代表只改变阈值；图中未包含角色投影。\n\n'
    if number=='06':
        return pair(picture('project/face.png','脸部效果近景'),picture('project/region_debug.png','Debug38：覆盖范围'))+'两图用途和取景不同，用来分别认识效果与覆盖，不作为效果开关A/B。\n\n'
    if number=='08':
        return pair(picture('experiments/20261021/wall_receiver_off.png','墙面接收下限=1'),picture('experiments/20261021/floor_receiver_on.png','墙面接收下限=0.1'))+'同姿态、同镜头、Debug0、1600×900、HDR关闭、RT单采样；只改墙接收Renderer的一个MPB属性，地面影子保留。\n\n'
    if number=='09':
        return pair(picture('project/final.png','完整效果'),picture('project/specular_debug.png','Debug13：最终spec'))+'效果图与诊断图用于看不同分量，不作为同条件的强度开关A/B。\n\n'
    if number=='10':
        return pair(picture('project/thigh_before.png','ThighLobe关闭'),picture('project/thigh_after.png','ThighLobe开启'))+'同条件的局部高光开关对照；颜色是最终合成结果，不等于Tint参数本身。\n\n'
    if number=='11':
        return pair(picture(standing_image('full-settled',0),'原描边，Debug0'),picture(standing_image('outline-off',0),'只把外描边宽度设为0'))+'同姿态、同镜头、1600×900、HDR关闭、RT单采样；内部线保留。这个对照用于区分外壳与纹理线。\n\n'+picture('project/ink_debug.png','Debug31：内部墨线')+'\n\n'
    if number=='12':
        return pair(picture('experiments/20261021/eye_off_crop.png','眼睛细化关闭',link='experiments/20261021/eye_off_0.png'),picture('experiments/20261021/eye_on_crop.png','眼睛细化开启',link='experiments/20261021/eye_on_0.png'))+'同姿态、同取景、Debug0原图的相同矩形裁切；1600×900、HDR关闭、RT单采样。只改头Renderer的_EyeRefineEnabled，点击查看完整近景。\n\n'
    if number=='14':
        return pair(picture(standing_image('full-settled',0),'站立cell00'),picture(standing_image('full-settled',7),'站立cell07'))+'同镜头、同材质、不同姿态；1600×900、HDR关闭、RT单采样。观察投影和亮块随姿态的位置，不把两幅不同姿态当效果开关对照。\n\n'
    raise ValueError(number)

def compact(value):
    value=json.loads(value)
    if isinstance(value,dict) and set(value)=={'r','g','b','a'}:
        return '('+', '.join(str(value[k]) for k in ['r','g','b','a'])+')'
    if value is None:return '未保存'
    return str(value)

def generate():
    meta={r['id']:r for r in json.loads((ROOT/'tools/chapter_map.json').read_text(encoding='utf-8'))}
    mp=rows('data/material_parameters.csv');excerpts=[]
    by={(r['material'],r['property']):r for r in mp}
    for number in ORDER:
        c=meta[number];a=CHAPTERS[number]
        body=f"# {c['title']}\n\n{a['problem']}\n\n"+figures(number)
        body+='## 准备输入\n\n'+a['inputs']+'\n\n'
        body+='## 操作步骤\n\n'+a['steps']+'\n\n'
        body+='## 原理与代码位置\n\n'+a['principle']+'\n\n'
        for name,start,end in c['refs']:
            if name=='BridgetToon.shader':
                context='SubShader / FORWARD入口' if end<204 else 'OUTLINE与SHADOWCASTER：描边及阴影Pass' if start>=729 and end>=798 else 'OUTLINE：vertOutline / fragOutline' if start>=729 else 'FORWARD：vert / frag及其计算函数'
            else:context={'GGSTRegionalShading.cs':'Apply / ResolveFrames / Set','BridgetImitateProfile.cs':'OnEnable / LateUpdate / OnDisable','GGSTGeometryShadowMaps.cs':'Ready / RenderMaps / DrawToonSubmeshes / Publish','GGSTGeometryDepth.shader':'GEOMETRY_DEPTH：vert / frag','StageShadowReceiver.shader':'GeometryStageVisibility / frag'}[name]
            body+=f'- [{name}:{start}–{end}](../reference/code/{name}.md#l{start})：{context}。\n'
        body+='\n'
        for name,start,end in c['excerpts']:
            code='\n'.join((PACK/'sources'/name).read_text(encoding='utf-8-sig').splitlines()[start-1:end])
            body+=f'局部摘录（需结合完整上下文）：[{name}:{start}–{end}](../reference/code/{name}.md#l{start})。\n\n```'+('csharp' if name.endswith('.cs') else 'hlsl')+'\n'+code+'\n```\n\n'
            excerpts.append({'chapter':number,'file':name,'start':start,'end':end,'text':code})
        if a['params']:
            body+='## 参数怎么调\n\n下表区分Shader默认值与四主体材质设置。Base/Secondary/Flip/Coat对应四种主体材质；同名字段还可能被[MPB或全局输入](../reference/overrides.md)覆盖。完整属性类型和纹理绑定见[参数参考](../reference/parameters.md)。\n\n'
            data=[]
            for prop,purpose in a['params']:
                entries=[by[(material,prop)] for material in MATERIALS]
                values=[compact(x['savedValue']) if x['savedPresent']=='True' else '未保存' for x in entries]
                current=values[0] if len(set(values))==1 else '；'.join(f'{label}={v}' for label,v in zip(SHORT,values))
                data.append([prop,entries[0]['type'],compact(entries[0]['shaderDefault']),current,purpose])
            body+=table(['属性','类型','Shader默认','材质设置','作用'],data)
        body+='## 画面判断与排错\n\n'+a['troubleshoot']+'\n\n'
        index=ORDER.index(number);links=[]
        if index:links.append(f"[上一步：{meta[ORDER[index-1]]['title']}]({ORDER[index-1]}.md)")
        if index+1<len(ORDER):links.append(f"[下一步：{meta[ORDER[index+1]]['title']}]({ORDER[index+1]}.md)")
        links.append('[教程导航](../index.md)');body+=' · '.join(links)+'\n'
        write(ROOT/'docs/chapters'/f'{number}.md',body)
    write(ROOT/'tools/excerpts.json',json.dumps(excerpts,ensure_ascii=False,indent=2))
    print(f'Generated {len(CHAPTERS)} practical chapters; {len(excerpts)} exact source excerpts.')

if __name__=='__main__':generate()
