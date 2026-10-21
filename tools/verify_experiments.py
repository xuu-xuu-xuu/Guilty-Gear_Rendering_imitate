"""Recheck the published Unity capture evidence without a Unity installation.

This validates the exported evidence and pixel comparisons, not a new render.
"""
import hashlib
import json
from pathlib import Path
from evidence_pixels import rgb,compare,eye_coverage,outside_count

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/'evidence/rendering-ab-20261021'
def read(name):return json.loads((EVIDENCE/name).read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def verify():
    capture=read('capture.json'); restoration=read('restoration.json'); integrity=read('project-integrity.json')
    manifest=read('images.json'); audit=read('pixel-audit.json')
    records={r['name']:r for r in capture['records']}
    images={r['record']:r for r in manifest}
    assert capture['completed'] and len(records)==23 and not capture['shaderErrors']
    assert not capture['playMode'] and capture['targetMSAA']==1 and not capture['allowHDR'] and not capture['allowMSAA']
    assert capture['unityVersion']=='2022.3.62f3c1' and capture['colorSpace']=='Linear'
    assert len({r['sceneFingerprint'] for r in records.values()})==1
    assert integrity['originalProjectFileCount']==428 and integrity['originalMatches20261021Collection']
    source_hashes=read('source-input-hashes.json')
    assert len(source_hashes)==428
    assert hashlib.sha256(json.dumps(source_hashes,sort_keys=True,separators=(',',':')).encode()).hexdigest()==integrity['originalInputTreeSha256']
    assert not integrity['originalChangedFiles'] and not integrity['isolatedCopyChangedOriginalInputs']
    assert sha(ROOT/'examples/capture/RenderingEvidenceCapture.cs')==integrity['captureCodeSha256']
    pack=ROOT/'rendering-tutorial-source-pack'
    import csv
    with (pack/'data/source_index.csv').open(encoding='utf-8-sig',newline='') as f: expected=list(csv.DictReader(f))
    assert {r['path']:r['sha256'] for r in integrity['renderingSources']}=={r['source']:r['sha256'] for r in expected}
    assert integrity['sceneSha256']==json.loads((pack/'data/saved_scene_rendering.json').read_text(encoding='utf-8-sig'))['sha256']
    for key in ['sceneFingerprintUnchanged','projectionModeRestored','targetRestored','aaRestored','hdrRestored','casterFlagsRestored']:assert restoration[key]
    assert restoration['projectionMaxDifference']<1e-6 and restoration['restoredInputs']==capture['baselineInputs']
    for im in manifest:
        path=ROOT/im['document_path']
        assert path.is_relative_to(ROOT/'docs/assets/images/experiments/20261021')
        assert sha(path)==im['sha256'] and list(rgb(path).size)==im['size']
        if 'derivedFrom' in im:
            assert im['resized'] is False and im['retouched'] is False
            source=rgb(ROOT/im['derivedFrom'])
            assert source.crop(im['cropBoxXYXY']).tobytes()==rgb(path).tobytes()
        else:
            record=records[im['record']]
            assert record['sha256']==im['sha256'] and record['documentImage']==im['document_path']
    assert len({r['document_path'] for r in manifest})==14
    for key,pair in audit['pairs'].items():
        if key=='eyeLocality':continue
        a,b=records[pair['a']],records[pair['b']]
        for field in ['projection','view','sceneFingerprint','debug','width','height']:assert a[field]==b[field],(key,field)
        assert a['variable']==b['variable']
        if key.startswith('eye'):
            for left,right in zip(a['inputBlocks'],b['inputBlocks']):
                for field in left:
                    if field not in {'eyeOverride','eyeValue'}:assert left[field]==right[field],(key,field)
        else:
            assert a['inputBlocks']==b['inputBlocks'],key
        if key not in {'stageCasterFallback','hair0','hair32'}:
            assert a['stageCasters']==b['stageCasters'] and a['hairCasters']==b['hairCasters']
        actual=compare(rgb(ROOT/a['documentImage']),rgb(ROOT/b['documentImage']))
        for field,value in actual.items():assert value==pair[field],(key,field,value,pair[field])
        depth_equal=all(a[field]['sha256']==b[field]['sha256'] for field in ['stageDepth','hairDepth'])
        assert depth_equal==pair['depthMapsIdentical'],key
    for key in ['wall','floor']:
        assert audit['pairs'][key]['changedPixels']>0
        assert records[key+'_receiver_off']['value']==1
        assert records[key+'_receiver_on']['value']==(0.1 if key=='wall' else 0.08)
    for key in ['wallRepeat','floorRepeat','eyeRepeat','eye13','eye30','hair0','hair32']:assert audit['pairs'][key]['changedPixels']==0,key
    coverage=eye_coverage(rgb(ROOT/records['eye_on_33']['documentImage']))
    outside=outside_count(rgb(ROOT/records['eye_off_0']['documentImage']),rgb(ROOT/records['eye_on_0']['documentImage']),coverage)
    assert outside==0 and audit['pairs']['eyeLocality']['changedOutsideDebug33Coverage']==outside
    assert coverage.histogram()[255]==audit['pairs']['eyeLocality']['debug33CoveragePixels']
    for r in records.values():
        if r['stageCasters']:assert r['stageEnabled']==1 and r['stageDrawCount']>0 and r['stageDepth']['occupiedPixels']>0
        if r['hairCasters']:assert r['hairEnabled']==1 and r['hairDrawCount']>0 and r['hairDepth']['occupiedPixels']>0
    for source in EVIDENCE.glob('*.json'):
        assert sha(source)==sha(ROOT/'docs/assets/evidence/rendering-ab-20261021'/source.name)
    assert sha(ROOT/'examples/capture/RenderingEvidenceCapture.cs')==sha(ROOT/'docs/assets/evidence/rendering-ab-20261021/capture-code.txt')
    print('PASS: 23 recorded Unity renders, 14 unique PNG/crops, pixel metrics/locality, source snapshot and restoration evidence. This is evidence rechecking, not a new Unity run.')
    return manifest

if __name__=='__main__':verify()
