"""Maak/werk template 'PP viewed tailored · VIP · TEST' bij in Klaviyo en render elk scenario via POST /api/template-render/.
python3 -I _tools/render_api.py   -> tailored/<id>.html + tailored/results.json"""
import sys, os, json, re
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive'); sys.path.insert(0, os.path.dirname(__file__))
from kl import api
from scenarios import S, ctx
from ppv_catalog import BYKEY
D = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
html = open(os.path.join(D, 'ppv-tailored.html')).read()
idf = os.path.join(D, 'tailored', 'template-id.txt')
NAME = 'PP viewed tailored · VIP · TEST'
if os.path.exists(idf):
    tid = open(idf).read().strip()
    r = api('PATCH', f'/api/templates/{tid}/', {'data': {'type': 'template', 'id': tid, 'attributes': {'html': html}}})
else:
    r = api('POST', '/api/templates/', {'data': {'type': 'template', 'attributes': {'name': NAME, 'editor_type': 'CODE', 'html': html}}})
    tid = r['data']['id']; open(idf, 'w').write(tid + '\n')
assert 'data' in r, json.dumps(r)[:500]
print('template', tid)
res = {}
for s in S:
    d = api('POST', '/api/template-render/', {'data': {'type': 'template', 'id': tid, 'attributes': {'context': ctx(s)}}})
    if 'data' not in d: print(s['id'], json.dumps(d)[:400]); continue
    out = d['data']['attributes']['html']
    open(os.path.join(D, 'tailored', s['id'] + '.html'), 'w').write(out)
    hero = '12-Pcs' if 'ppv-set12' in out or '813a3024' in out else ('6-Pcs' if '03423581' in out else None)
    got = re.findall(r'utm_content%3D([a-z0-9]{3})(?:%26|")', out)
    seen = []
    for g in got:
        if g in BYKEY and g not in seen: seen.append(g)
    ok = hero == s['expect_hero'] and seen == s['expect']
    left = re.findall(r'\{%|\{\{', out)
    res[s['id']] = dict(title=s['title'], hero=hero, cards=seen, expect_hero=s['expect_hero'], expect=s['expect'], ok=ok, leftovers=len(left), bytes=len(out))
    print(s['id'], 'OK' if ok else 'FOUT', hero, seen, 'verwacht', s['expect_hero'], s['expect'], 'rest-tags', len(left), len(out))
json.dump(res, open(os.path.join(D, 'tailored', 'results.json'), 'w'), indent=1, ensure_ascii=False)
