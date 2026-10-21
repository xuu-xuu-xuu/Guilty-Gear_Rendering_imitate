"""Metrics on actual exported Unity PNGs. Does not run Unity or judge motion quality."""
from functools import lru_cache
from collections import defaultdict
from PIL import ImageChops
from evidence_pixels import rgb, compare, eye_coverage

EYE_BOX=(451,207,969,506)  # Union of all 13 Debug33 eye bounds plus 16 pixels.

def calculate(controlled,natural,load):
    comparisons={}
    @lru_cache(maxsize=120)
    def image(h):return load(h)
    def pair(a,b):
        key=a['image']+':'+b['image']
        if key not in comparisons:
            comparisons[key]={'a':a['image'],'b':b['image'],**compare(image(a['image']),image(b['image']))}
        return key
    def repeat_stats(rows,key):
        groups=defaultdict(list)
        for r in rows:groups[key(r)].append(r)
        pairs=[pair(rs[0],r) for rs in groups.values() for r in rs[1:]]
        return {'groups':len(groups),'comparisons':len(pairs),'nonzero':sum(comparisons[k]['changedPixels']>0 for k in pairs),
                'maxChangedPixels':max((comparisons[k]['changedPixels'] for k in pairs),default=0),'pairs':pairs}
    rows=controlled['samples'];play=natural['samples']
    full=[r for r in rows if r['kind']=='full-settled']
    first=[r for r in rows if r['kind']=='full-first']
    first_pairs=[pair(a,b) for a,b in zip(first,full)]
    starts={r['cell']:r for r in full if r['cycle']==0}
    diagnostics={kind:{r['cell']:r for r in rows if r['kind']==kind} for kind in ['specular','outline-off','stage-receivers-off','eye-final','eye-regions','eye-contribution']}
    cells=[]
    for cell in range(13):
        base=starts[cell];prev=starts[(cell-1)%13]
        eye=diagnostics['eye-final'][cell];before=diagnostics['eye-final'][(cell-1)%13]
        crop=compare(image(before['image']).crop(EYE_BOX),image(eye['image']).crop(EYE_BOX))
        mask=eye_coverage(image(diagnostics['eye-regions'][cell]['image']))
        shadow=pair(base,diagnostics['stage-receivers-off'][cell])
        outline=pair(base,diagnostics['outline-off'][cell])
        cells.append({'cell':cell,'startTick':next(x['startTick'] for x in controlled['schedule']['rows'] if x['cell']==cell),
            'fullTransitionFromPrevious':pair(prev,base),'specTransitionFromPrevious':pair(diagnostics['specular'][(cell-1)%13],diagnostics['specular'][cell]),
            'outlineComparison':outline,'shadowComparison':shadow,'outlineChangedPixels':comparisons[outline]['changedPixels'],
            'stageReceiverChangedPixels':comparisons[shadow]['changedPixels'],
            'eyeCoveragePixels':mask.histogram()[255],'eyeBBoxXYXY':list(mask.getbbox()) if mask.getbbox() else None,
            'eyeCropTransitionFromPrevious':crop})
    play_starts={}
    for r in play:play_starts.setdefault(r['cell'],r)
    cross=[pair(starts[cell],play_starts[cell]) for cell in range(13)]
    return {'schema':'standing-render-pixel-audit-v1',
        'firstVsSettled':{'comparisons':len(first_pairs),'nonzero':sum(comparisons[k]['changedPixels']>0 for k in first_pairs),'pairs':first_pairs},
        'controlledSameTickAcrossCycles':repeat_stats(full,lambda r:r['tick']),
        'controlledSameCell':repeat_stats(full,lambda r:r['cell']),
        'naturalSameCell':repeat_stats(play,lambda r:r['cell']),
        'naturalSameTick':repeat_stats(play,lambda r:r['tick']),
        'naturalMissingTicks':sorted(set(range(63))-{r['tick'] for r in play}),
        'naturalSameCellPoseHashes':{str(cell):len({r['poseHash'] for r in play if r['cell']==cell}) for cell in range(13)},
        'crossPhaseComparisons':cross,'cells':cells,'comparisons':comparisons}
