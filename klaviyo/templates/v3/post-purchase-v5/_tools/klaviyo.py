"""Maakt of werkt de 7 code-templates 'PP v5 · <mail> · TEST' bij (alleen bibliotheek, niets in een live flow) en rendert elke CASE
via POST /api/template-render/ -> api/<mail>--<id>.html. python3 -I _tools/klaviyo.py"""
import os, sys, json, re
sys.path.insert(0, '/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive'); sys.path.insert(0, os.path.dirname(__file__))
from kl import api
from ctx import CASES
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
NAMES = {'pp1-first': 'PP1 first · Order confirmed', 'pp1-repeat': 'PP1 repeat · Order confirmed', 'pp2-upsell': 'PP2 · Tailored upsell VIP15',
         'pp3-delivered': 'PP3 delivered · First egg', 'pp3-safe': 'PP3 safe · First egg', 'pp4-code': 'PP4 CODE · Cross-sell 10%', 'pp4-nocode': 'PP4 nocode · Cross-sell'}
idf = os.path.join(ROOT, 'klaviyo-template-ids.json')
ids = json.load(open(idf)) if os.path.exists(idf) else {}
for k, n in NAMES.items():
    html = open(os.path.join(ROOT, 'out', k + '.html')).read()
    if k in ids:
        r = api('PATCH', f'/api/templates/{ids[k]}/', {'data': {'type': 'template', 'id': ids[k], 'attributes': {'html': html}}})
    else:
        r = api('POST', '/api/templates/', {'data': {'type': 'template', 'attributes': {'name': f'PP v5 · {n} · TEST', 'editor_type': 'CODE', 'html': html}}})
        ids[k] = r['data']['id']
    assert 'data' in r, json.dumps(r)[:400]
    json.dump(ids, open(idf, 'w'), indent=1)
    print(k, ids[k])
os.makedirs(os.path.join(ROOT, 'api'), exist_ok=True)
for mail, cid, title, c in CASES:
    d = api('POST', '/api/template-render/', {'data': {'type': 'template', 'id': ids[mail], 'attributes': {'context': c}}})
    if 'data' not in d: print('FOUT', mail, cid, json.dumps(d)[:400]); continue
    out = d['data']['attributes']['html']
    open(os.path.join(ROOT, 'api', f'{mail}--{cid}.html'), 'w').write(out)
    cards = re.findall(r'utm_content%3D([a-z0-9]{3})(?:%26|")', out)
    seen = []
    for g in cards:
        if g not in seen: seen.append(g)
    print(mail, cid, 'tags-left', len(re.findall(r'\{%|\{\{', out)), 'cards', seen, '12pcs' if 'cookware-set%3F' in out or 'titanium-hammered-cookware-set%3F' in out else '', len(out))
