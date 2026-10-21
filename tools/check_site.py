"""Check rendered local links, anchors and project-prefix-safe resources."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

SITE=Path(__file__).resolve().parents[1]/'site'

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.ids=set(); self.links=[]
        self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        for key in ('href','src'):
            if key in a: self.links.append((tag,key,a[key]))

def main():
    pages={p:Page(p.read_text(encoding='utf-8')) for p in SITE.rglob('*.html')}
    assert pages,'Build site first'
    checked=0; skipped=0
    for file,page in pages.items():
        for tag,key,raw in page.links:
            u=urlsplit(raw)
            if u.scheme or u.netloc:
                skipped+=1; continue
            if u.path.startswith('/'):
                # MkDocs' 404 must work at an unknown depth and emits configured
                # project-prefixed paths. Ordinary pages must remain relative.
                prefix='/Guilty-Gear_Rendering_imitate/'
                assert file.name=='404.html' and u.path.startswith(prefix),(file,raw)
                target=(SITE/unquote(u.path[len(prefix):])).resolve()
            else:
                target=(file.parent/unquote(u.path)).resolve() if u.path else file
            if target.is_dir(): target=target/'index.html'
            assert target.is_relative_to(SITE.resolve()),(file,raw)
            assert target.exists(),(file,raw,target)
            if u.fragment and target.suffix=='.html':
                # Material uses SVG sprites; only HTML document anchors checked here.
                assert unquote(u.fragment) in pages[target].ids,(file,raw,'missing anchor')
            checked+=1
    search=json.loads((SITE/'search/search_index.json').read_text(encoding='utf-8'))
    assert len(search['docs'])>=15
    assert any('大腿' in str(x) for x in search['docs'])
    print(f'PASS: {len(pages)} HTML pages; {checked} local links/resources/anchors; {len(search["docs"])} search entries; project-prefix safe. External URLs not treated as local proof ({skipped} skipped).')

if __name__=='__main__':
    main()
