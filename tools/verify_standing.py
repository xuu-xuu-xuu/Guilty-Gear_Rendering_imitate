"""Recompute exported standing render evidence; this does not start Unity."""
import csv
import hashlib
import json
from pathlib import Path
from PIL import Image
from standing_metrics import calculate,EYE_BOX

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/'evidence/standing-render-20261021'
def read(name):return json.loads((EVIDENCE/name).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def verify():
    c=read('controlled.json');n=read('natural.json');mapping=read('image-map.json');manifest=read('images.json')
    assert c['schema']=='standing-render-stability-v3' and c['completed'] and n['completed']
    assert c['playMode'] and n['playMode'] and not c['errors'] and not c['shaderErrors'] and not n['errors'] and n['error'] is None
    assert c['sourceArraysUnchanged'] and n['sourceArraysUnchanged']
    assert c['sourceHashesBefore']==c['sourceHashesAfter']==n['sourceHashesBefore']==n['sourceHashesAfter']
    assert len(c['samples'])==456 and len(n['samples'])==122
    assert len({r['unityFrame'] for r in c['samples']})==456
    assert n['observedCycleSpan']==8 and n['coveredCells']==list(range(13))
    assert c['environment']==n['environment']
    env=c['environment']
    assert env['unity']=='2022.3.62f3c1' and env['colorSpace']=='Linear' and env['api']=='Direct3D11'
    assert env['width']==1600 and env['height']==900 and not env['hdr'] and not env['cameraMSAA'] and env['targetMSAA']==1
    assert len(mapping)==91 and len(manifest)==104
    for phase in [c,n]:
        rows=phase['samples']
        assert all(a['unityFrame']<b['unityFrame'] for a,b in zip(rows,rows[1:]))
        assert len({str(r['view']) for r in rows})==1
        for r in rows:
            assert r['image'] in mapping and r['stageEnabled']==1 and r['hairEnabled']==1 and r['stageDraws']>0 and r['hairDraws']>0
            assert r['sourceFrame']==r['tick'] and r['proxyError']<1e-4
            assert r['debug']==({'specular':13,'eye-regions':33,'eye-contribution':34}.get(r['kind'],0))
            assert [x['enabled'] for x in r['inputs']]==[True,True,False,False]
            assert all(x['regional']==1 and x['frameValid']==1 and not x['eyeOverride'] for x in r['inputs'])
    for im in manifest:
        p=ROOT/im['document_path']
        assert p.is_relative_to(ROOT/'docs/assets/images/standing/20261021') and sha(p)==im['sha256']
        with Image.open(p) as pic:assert list(pic.size)==im['size']
        assert im['retouched'] is False
        if im['kind']=='exact-pixel-crop':
            assert im['cropBoxXYXY']==list(EYE_BOX) and im['resized'] is False
            with Image.open(p) as crop:
                for use in im['uses']:
                    with Image.open(ROOT/use['derivedFrom']) as source:
                        assert source.crop(EYE_BOX).tobytes()==crop.tobytes()
        else:assert mapping[im['sha256']]==im['document_path']
    def load(h):
        with Image.open(ROOT/mapping[h]) as im:return im.convert('RGB')
    actual=calculate(c,n,load)
    assert actual==read('pixel-audit.json'),'Published pixel audit is stale or incorrect'
    # These assertions state precisely the outcomes of this recorded run.
    assert actual['firstVsSettled']['nonzero']==0
    for k in ['controlledSameTickAcrossCycles','controlledSameCell','naturalSameCell','naturalSameTick']:assert actual[k]['nonzero']==0
    assert all(actual['comparisons'][p]['changedPixels']==0 for p in actual['crossPhaseComparisons'])
    # Catch stale native skinning: distinct actual main-camera images and eye bounds.
    assert len({tuple(x['eyeBBoxXYXY']) for x in actual['cells']})==13
    assert any(actual['comparisons'][x['fullTransitionFromPrevious']]['changedPixels']>100000 for x in actual['cells'])
    integrity=read('integrity.json');inputs=read('source-input-hashes.json')
    assert integrity['originalFiles']==428 and integrity['copyOriginalInputs']==422
    assert not integrity['originalChangedFiles'] and not integrity['copyChangedOriginalFiles']
    assert len(inputs)==428 and hashlib.sha256(json.dumps(inputs,sort_keys=True,separators=(',',':')).encode()).hexdigest()==integrity['inputTreeSha256']
    assert sha(ROOT/'examples/capture/StandingRenderStabilityCapture.cs')==integrity['captureCodeSha256']
    pack=ROOT/'rendering-tutorial-source-pack'
    assert integrity['sceneSha256']==json.loads((pack/'data/saved_scene_rendering.json').read_text(encoding='utf-8-sig'))['sha256']
    with (pack/'data/source_index.csv').open(encoding='utf-8-sig',newline='') as f:expected=list(csv.DictReader(f))
    assert {r['path']:r['sha256'] for r in integrity['renderSources']}=={r['source']:r['sha256'] for r in expected}
    for p in EVIDENCE.glob('*.json'):assert sha(p)==sha(ROOT/'docs/assets/evidence/standing-render-20261021'/p.name)
    assert integrity['captureCodeSha256']==sha(ROOT/'docs/assets/evidence/standing-render-20261021/capture-code.txt')
    print('PASS: standing evidence rechecked: 456 controlled Play frames, 122 natural frames, 91 native PNGs + 13 exact crops; repeated poses and first/next frame comparisons; snapshot integrity. No new Unity run in this check.')
    return manifest

if __name__=='__main__':verify()
