"""Stap 2 en dedupe: extra verzendfilters. python3 patch1.py [--live]"""
import sys,json,time,os
sys.path.insert(0,'../golive')
from kl import api
LIVE='--live' in sys.argv
def tf(op,days=None):
    d={'type':'date','operator':op}
    if days: d.update(unit='day',quantity=days)
    return d
def recv(prop,op,val,frame):
    return {'type':'profile-metric','metric_id':'YkRM4Q','measurement':'count','measurement_filter':{'type':'numeric','operator':'equals','value':0},
            'timeframe_filter':frame,'metric_filters':[{'property':prop,'filter':{'type':'string','operator':op,'value':val}}]}
P2SAFE=recv('Campaign Name','contains','P2-SAFE',tf('in-the-last',30))
PLAN={
 '119850554':[P2SAFE, recv('$flow','equals','VQ93sx',tf('in-the-last',30)), recv('$flow','equals','R9dcdY',tf('in-the-last',30))],
 '119850581':[recv('$flow','equals','R9dcdY',tf('in-the-last',30))],
 '121654816':[recv('$flow','equals','YhQJdb',tf('alltime'))],
 '121654817':[recv('$flow','equals','YhQJdb',tf('alltime'))],
 '121654822':[recv('$flow','equals','YhQJdb',tf('alltime'))],
 '121654823':[recv('$flow','equals','YhQJdb',tf('alltime'))],
 '119577632':[recv('$flow','equals','TvfJYU',tf('alltime'))],
 '119577635':[recv('$flow','equals','TvfJYU',tf('alltime'))],
}
os.makedirs('voor1',exist_ok=True)
for aid,conds in PLAN.items():
    r=api('GET',f'/api/flow-actions/{aid}')
    D=r['data']['attributes']['definition']
    if not os.path.exists(f'voor1/{aid}.json'): json.dump(D,open(f'voor1/{aid}.json','w'))
    m=D['data']['message']; f=m.get('additional_filters') or {'condition_groups':[]}
    have=[json.dumps(g['conditions'],sort_keys=True) for g in f['condition_groups']]
    add=[c for c in conds if json.dumps([c],sort_keys=True) not in have]
    if not add: print('al aanwezig',aid,m['name']); continue
    for c in add: f['condition_groups'].append({'conditions':[c]})
    m['additional_filters']=f
    if not LIVE: print('DRY',aid,m['name'],D['data']['status'],'+',len(add)); continue
    p=api('PATCH',f'/api/flow-actions/{aid}',{'data':{'type':'flow-action','id':aid,'attributes':{'definition':D}}})
    if 'errors' in p: print('FOUT',aid,json.dumps(p['errors'])[:300]); continue
    g=api('GET',f'/api/flow-actions/{aid}')['data']['attributes']['definition']['data']
    print('OK',aid,g['message']['name'],g['status'],len(g['message']['additional_filters']['condition_groups']),g['message']['template_id']==m['template_id'])
    time.sleep(0.5)
