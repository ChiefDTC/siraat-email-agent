import sys,datetime as d; sys.path.insert(0,'/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/golive')
from kl import api
flows=["Rn556d","YqKCmH","Vd38Vc","VbYwA8","WTY94m","YwsKcf","X3ySuU","VQ93sx","QUBUQV","TZG9Mx","T4a5Mk","WdRz5k","QNZyEb","TvfJYU","XzHrez","T5riz5","TF2B5x","VTkxFL","VLGhbR","T2SmtR","TbYQmX","UEfh4h","YyaMjx","VPixnJ"]
for aid,fid in (('119850685','WdRz5k'),('119850622','TZG9Mx'),('119850583','QUBUQV')):
    df=api('GET','/api/flow-actions/'+aid).get('data',{}).get('attributes',{}).get('definition') or {}
    pct=(df.get('data') or {}).get('profile_filter',{}).get('condition_groups',[{}])[0].get('conditions',[{}])[0].get('percentage')
    print('split',fid,api('GET','/api/flows/'+fid)['data']['attributes']['status'],pct)
now=d.datetime.now(d.timezone.utc).replace(microsecond=0)
S=["recipients","delivered","clicks_unique","conversion_uniques","conversion_value","bounced","unsubscribes","spam_complaints"]
b={"data":{"type":"flow-values-report","attributes":{"statistics":S,"timeframe":{"start":(now-d.timedelta(days=1)).isoformat(),"end":now.isoformat()},"conversion_metric_id":"RSNxYV","filter":"contains-any(flow_id,["+",".join('"%s"'%f for f in flows)+"])"}}}
r=api("POST","/api/flow-values-reports",b)
if 'errors' in r: print(r['errors']); raise SystemExit
agg={}
for x in r["data"]["attributes"]["results"]:
    f=x["groupings"]["flow_id"]; a=agg.setdefault(f,{k:0 for k in S})
    for k in S: a[k]+=x["statistics"].get(k) or 0
tot=0
for f,s in sorted(agg.items(),key=lambda kv:-kv[1]['conversion_value']):
    rc=s['recipients'] or 1; dl=s['delivered'] or 1; tot+=s['conversion_value']
    fl=[]
    if s['recipients']>=30:
        if s['bounced']/rc>0.05: fl.append('BOUNCE')
        if s['spam_complaints']/dl>0.003: fl.append('SPAM')
        if s['unsubscribes']/dl>0.01: fl.append('UNSUB')
    print(f"{f}|ontv {s['recipients']:.0f}|klik {100*s['clicks_unique']/dl:.1f}%|orders {s['conversion_uniques']:.0f}|${s['conversion_value']:.0f}|RPR {s['conversion_value']/rc:.2f}|bounce {100*s['bounced']/rc:.1f}%|uitschr {100*s['unsubscribes']/dl:.2f}%|spam {100*s['spam_complaints']/dl:.3f}% {' '.join(fl)}")
print('totaal',round(tot))

# --- A/B-tests (toegevoegd 18 nov 2026): per variant ontvangers, orders, omzet sinds start
def _abtests():
    import datetime as _dt
    tests=[('BF-W1 image B (SdaYcV 60/40)','SdaYcV','125640456','2026-11-18T12:52:00'),
           ('Browse B2 brief (WdRz5k 80/20)','WdRz5k','125683568','2026-11-18T16:34:00')]
    now=_dt.datetime.now(_dt.UTC).strftime('%Y-%m-%dT%H:%M:%S')
    for lab,fid,aid,start in tests:
        d=api('GET',f'/api/flows/{fid}?additional-fields[flow]=definition')['data']['attributes']['definition']
        ab=[a for a in d['actions'] if a['id']==aid][0]['data']
        names={v['data']['message']['id']:v['data']['message']['name'] for v in ab['current_experiment']['variations']}
        def agg(metric,meas,by,flt):
            b={'data':{'type':'metric-aggregate','attributes':{'metric_id':metric,'measurements':meas,'interval':'month','by':[by],'filter':[f'greater-or-equal(datetime,{start})',f'less-than(datetime,{now})',flt],'timezone':'UTC'}}}
            return {tuple(x['dimensions'])[0]:{k:sum(v) for k,v in x['measurements'].items()} for x in api('POST','/api/metric-aggregates',b)['data']['attributes']['data']}
        rec=agg('YkRM4Q',['count'],'$variation',f'equals($flow,"{fid}")')
        ords=agg('RSNxYV',['count','sum_value'],'$attributed_variation',f'equals($attributed_flow,"{fid}")')
        print('AB',lab,'status',ab.get('experiment_status'),ab['current_experiment'].get('allocations'))
        for mid,n in names.items():
            r=rec.get(mid,{}).get('count',0); o=ords.get(mid,{})
            print(f"   {n[:40]:40} ontv {r:.0f} orders {o.get('count',0):.0f} ${o.get('sum_value',0):.0f} rpr {o.get('sum_value',0)/r if r else 0:.2f}")
try: _abtests()
except Exception as e: print('AB-fout',e)
