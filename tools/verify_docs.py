"""Verify evidence integrity and reproducible documentation. No Unity claims."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
from prepare_reference import ROOT, PACK, rows, verify_pack, generate
import write_chapters

BASE = 'f8980fad7a742d76cf8b941843234cd292c7ae82'

def hashes():
    paths=list((ROOT/'docs').rglob('*'))+[ROOT/'tools/excerpts.json']
    return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}

def main():
    count=verify_pack()
    baseline=subprocess.check_output(['git','show',f'{BASE}:rendering-tutorial-source-pack/MANIFEST.json'],cwd=ROOT)
    assert (PACK/'MANIFEST.json').read_bytes()==baseline, 'MANIFEST differs from original Git baseline'
    changed=subprocess.check_output(['git','diff',BASE,'--','rendering-tutorial-source-pack'],cwd=ROOT)
    assert not changed, 'Source pack differs from baseline'
    before=hashes()
    generate()
    write_chapters.generate()
    assert hashes()==before, 'Derived pages were stale. Review regenerated changes and commit them.'
    snippets=json.loads((ROOT/'tools/excerpts.json').read_text(encoding='utf-8'))
    for s in snippets:
        lines=(PACK/'sources'/s['file']).read_text(encoding='utf-8-sig').splitlines()
        assert s['text']=='\n'.join(lines[s['start']-1:s['end']]), s
        chapter=(ROOT/'docs/chapters'/f"{s['chapter']}.md").read_text(encoding='utf-8')
        assert '\n'+s['text']+'\n```' in chapter, s
    for r in rows('data/shader_properties.csv'):
        lines=(PACK/'sources'/Path(r['shader']).name).read_text(encoding='utf-8-sig').splitlines()
        line=lines[int(r['line'])-1]
        match=re.search(re.escape(r['property'])+r'\s*\(\s*"[^"]*"\s*,\s*'+re.escape(r['type'])+r'\s*\)\s*=\s*("[^"]*"|\([^)]*\)|[-+\d.eE]+)',line)
        assert match,r
        literal=match.group(1)
        if literal.startswith('('): value=[float(v.strip()) for v in literal[1:-1].split(',')]
        elif literal.startswith('"'): value=json.loads(literal)
        else: value=float(literal)
        assert value==json.loads(r['default']),r
    declarations={(r['shader'],r['property']):r for r in rows('data/shader_properties.csv')}
    materials=json.loads((PACK/'data/materials_saved.json').read_text(encoding='utf-8-sig'))
    for r in rows('data/material_parameters.csv'):
        declaration=declarations[(r['shader'],r['property'])]
        assert r['type']==declaration['type'] and json.loads(r['shaderDefault'])==json.loads(declaration['default']),r
        source=materials[r['material']]['textures' if r['type']=='2D' else 'savedValues']
        assert (r['savedPresent']=='True')==(r['property'] in source),r
        assert json.loads(r['savedValue'])==source.get(r['property']),r
    for r in rows('data/debug_outputs.csv'):
        line=(PACK/r['source']).read_text(encoding='utf-8-sig').splitlines()[int(r['line'])-1]
        assert r['expression'] in line,r
    for r in rows('data/runtime_write_sites.csv'):
        line=(PACK/r['source']).read_text(encoding='utf-8-sig').splitlines()[int(r['line'])-1]
        assert r['code'] in line,r
    metadata=json.loads((ROOT/'tools/chapter_map.json').read_text(encoding='utf-8'))
    for c in metadata:
        for name,start,end in c['refs']:
            lines=(PACK/'sources'/name).read_text(encoding='utf-8-sig').splitlines()
            assert 1<=start<=end<=len(lines),(c['id'],name,start,end)
    provenance=json.loads((ROOT/'docs/assets/image-provenance.json').read_text(encoding='utf-8'))
    expected={x['document_path'] for x in provenance}
    actual={p.relative_to(ROOT).as_posix() for p in (ROOT/'docs/assets/images').rglob('*') if p.is_file()}
    assert actual==expected, (actual-expected,expected-actual)
    assert len(actual)==21
    for im in provenance:
        assert hashlib.sha256((ROOT/im['document_path']).read_bytes()).hexdigest()==im['sha256']
    md_paths=[ROOT/'README.md',ROOT/'THIRD_PARTY_NOTICES.md']+list((ROOT/'docs').rglob('*.md'))
    links=0
    for path in md_paths:
        text=path.read_text(encoding='utf-8')
        assert not re.search(r'(?i)\b[A-Z]:[\\/]',text),f'Local machine path in {path}'
        assert not re.search(r'<(?:audio|video|iframe)\b',text,re.I),path
        for raw in re.findall(r'\]\(([^\s)]+)\)',text):
            u=urlsplit(raw)
            if u.scheme or u.netloc or not u.path:
                continue
            assert not u.path.startswith('/'),(path,raw)
            target=(path.parent/unquote(u.path)).resolve()
            assert target.is_relative_to(ROOT),(path,raw)
            assert target.exists(),(path,raw)
            links+=1
    # The tracked additions are restricted to documentation/config/build tools.
    tracked=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT).decode().split('\0')
    for name in filter(None,tracked):
        if name.startswith('rendering-tutorial-source-pack/'):
            continue
        if name=='.gitignore':
            continue
        suffix=Path(name).suffix.lower()
        if suffix=='.png':
            assert name in expected, f'Image outside whitelist: {name}'
        else:
            assert suffix in {'.md','.py','.json','.yml','.txt','.css','.gitignore'},f'Unexpected asset/type: {name}'
    print(f'PASS: {count}+1 original files; {len(snippets)} verbatim excerpts; 165 declarations/defaults; 793 parameter rows vs saved JSON; 44 Debug outputs; runtime write lines; {len(actual)} exact whitelist images; {links} relative Markdown links; 15 chapters reproducible.')

if __name__=='__main__':
    main()
