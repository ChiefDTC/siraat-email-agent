import sys,json,collections,subprocess,time
sys.path.insert(0,'/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
from urllib.parse import quote
p='/api/events/?filter='+quote('equals(metric_id,"XNtYMB"),greater-or-equal(datetime,2026-10-20T17:00:00Z)')+'&fields[event]=event_properties,datetime&fields[profile]=id&page[size]=200&include=profile'
cnt=collections.Counter(); uniq=collections.defaultdict(set); urls={}; n=0
out=open('views.jsonl','w')
while p:
    d=api('GET',p)
    for e in d.get('data',[]):
        ep=e['attributes'].get('event_properties',{})
        nm=ep.get('Name') or ep.get('ProductName') or '?'
        pid=(e.get('relationships',{}).get('profile',{}).get('data') or {}).get('id')
        cnt[nm]+=1; uniq[nm].add(pid); urls.setdefault(nm,ep.get('URL')); n+=1
        out.write(json.dumps({'n':nm,'p':pid,'t':e['attributes']['datetime'],'u':ep.get('URL'),'pr':ep.get('Price'),'id':ep.get('ProductID')})+'\n')
    nx=d.get('links',{}).get('next')
    p=nx.replace('https://a.klaviyo.com','') if nx else None
    if n%10000<200: print(n,flush=True)
json.dump({k:[cnt[k],len(uniq[k]),urls[k]] for k in cnt},open('views_summary.json','w'),indent=1)
print('done',n)
