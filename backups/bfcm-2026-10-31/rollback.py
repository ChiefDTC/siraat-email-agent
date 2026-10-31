"""Rollback BF-switch 31 okt 2026.
Zet de html van elke gepatchte flow-template terug uit backup/template-<id>.html en
zet onderwerp en preview terug voor de acties waarvan die zijn aangepast.
Standaard dry-run; met --apply wordt het uitgevoerd. Optioneel: flow-id(s) als argument om te beperken.
"""
import json,glob,sys,time,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from kl import api
APPLY='--apply' in sys.argv
ONLY=[a for a in sys.argv[1:] if not a.startswith('--')]
def A(m,u,b=None):
    for i in range(6):
        r=api(m,u,b)
        if isinstance(r,dict) and 'errors' in r and any(str(e.get('status')) in ('429','500','502','503') for e in r['errors']): time.sleep(2+3*i); continue
        return r
    return r
n_t=n_s=0; fouten=[]
for f in sorted(glob.glob('switch-*.json')):
    d=json.load(open(f))
    if ONLY and d['flow'] not in ONLY: continue
    print('==',d['flow'])
    for a in d['actions']:
        tid=a['template_id']
        if a['kind']=='email':  # actuele template-id uit de actie (voor het geval Klaviyo een kopie maakte)
            g=A('GET',f"/api/flow-actions/{a['action']}")
            if 'errors' in g: fouten.append((a['action'],'GET actie')); continue
            cur=g['data']['attributes']['definition']; tid=cur['data']['message']['template_id']
        old=open(f"backup/template-{a['template_id']}.html").read()
        now=A('GET',f'/api/templates/{tid}')['data']['attributes']['html']
        need_t=(now!=old)
        need_s=a.get('subject_patched') and (cur['data']['message']['subject_line']!=a['old_subject'] or cur['data']['message']['preview_text']!=a['old_preview'])
        print(f"  {a['message_name']:<45} template {tid}: {'terugzetten' if need_t else 'al origineel'}" + (f" | onderwerp/preview terug naar {a['old_subject']!r}" if need_s else ''))
        if not APPLY: n_t+=need_t; n_s+=bool(need_s); continue
        if need_t:
            r=A('PATCH',f'/api/templates/{tid}',{'data':{'type':'template','id':tid,'attributes':{'html':old}}})
            if 'errors' in r: fouten.append((tid,str(r['errors'])[:200]))
            else: n_t+=1
        if need_s:
            cur['data']['message']['subject_line']=a['old_subject']; cur['data']['message']['preview_text']=a['old_preview']
            r=A('PATCH',f"/api/flow-actions/{a['action']}",{'data':{'type':'flow-action','id':a['action'],'attributes':{'definition':cur}}})
            if 'errors' in r: fouten.append((a['action'],str(r['errors'])[:200]))
            else: n_s+=1
        time.sleep(0.3)
print(('UITGEVOERD' if APPLY else 'DRY-RUN'),': templates',n_t,'| onderwerp/preview',n_s,'| fouten',fouten)
