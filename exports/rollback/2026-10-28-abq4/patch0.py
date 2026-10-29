"""Stap 1: $0-filter op elke send-email in order- en bezorgflows. python3 patch0.py [--live]"""
import sys,json,time,math,os
sys.path.insert(0,'/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
sys.path.insert(0,'.')
LIVE='--live' in sys.argv
BUF={'X3ySuU':3,'VQ93sx':60,'TvfJYU':59,'YwsKcf':3,'R22pzb':62,'UEfh4h':3,'UyFc78':3,'VTkxFL':3,'XbYT7T':3,'YyaMjx':3,'VPixnJ':60}
def cond(n): return {'type':'profile-metric','metric_id':'RSNxYV','measurement':'count','measurement_filter':{'type':'numeric','operator':'greater-than','value':0},
   'timeframe_filter':{'type':'date','operator':'in-the-last','unit':'day','quantity':n},'metric_filters':[{'property':'$value','filter':{'type':'numeric','operator':'greater-than','value':0}}]}
def has0(f):
    for g in (f or {}).get('condition_groups',[]):
        cs=g['conditions']
        if len(cs)==1 and cs[0].get('metric_id')=='RSNxYV' and any(m.get('property')=='$value' and m['filter'].get('operator')=='greater-than' and float(m['filter'].get('value'))==0 for m in (cs[0].get('metric_filters') or [])): return True
    return False
exec(open('tree.py').read().split('for fid in sys.argv')[0])
targets=[]
for fid,b in BUF.items():
    d,o=walk(fid)
    best={}
    for (aid,name,st,t,tpl,hf) in o: best[aid]=max(best.get(aid,(0,))[0],t),name,st
    for aid,(t,name,st) in best.items(): targets.append((fid,aid,name,st,math.ceil(t)+b))
targets+= [('XzHrez','119577632','review A',None,75),('XzHrez','119577635','review B',None,75)]
os.makedirs('voor0',exist_ok=True)
log=[]
for fid,aid,name,st,n in targets:
    r=api('GET',f'/api/flow-actions/{aid}')
    if 'errors' in r: print('GETFOUT',aid,r['errors'][0].get('detail')); continue
    D=r['data']['attributes']['definition']
    json.dump(D,open(f'voor0/{aid}.json','w'))
    m=D['data']['message']; f=m.get('additional_filters')
    if has0(f): print('al aanwezig',fid,aid,name); log.append((fid,aid,name,n,'al')); continue
    f=f or {'condition_groups':[]}
    f['condition_groups'].append({'conditions':[cond(n)]})
    m['additional_filters']=f
    if not LIVE: print('DRY',fid,aid,name,D['data'].get('status'),n,len(f['condition_groups'])); continue
    p=api('PATCH',f'/api/flow-actions/{aid}',{'data':{'type':'flow-action','id':aid,'attributes':{'definition':D}}})
    if 'errors' in p: print('PATCHFOUT',fid,aid,name,json.dumps(p['errors'])[:300]); log.append((fid,aid,name,n,'FOUT')); continue
    g=api('GET',f'/api/flow-actions/{aid}')['data']['attributes']['definition']
    ok=has0(g['data']['message']['additional_filters']) and g['data'].get('status')==json.load(open(f'voor0/{aid}.json'))['data'].get('status') and g['data']['message']['template_id']==m['template_id']
    print('OK' if ok else 'CHECKFOUT',fid,aid,name,g['data'].get('status'),n); log.append((fid,aid,name,n,'ok' if ok else 'check'))
    time.sleep(0.5)
json.dump(log,open('patch0-log.json','w'))
