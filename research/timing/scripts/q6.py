from load import *
s=load('subs.jsonl',('list_id',),loc=True)
print('subscribed events',len(s), s.list_id.value_counts().head(8).to_dict())
s=s[(s.list_id=='Uw8eZG')&s.pid.notna()].sort_values('ts').drop_duplicates('pid')
o=pd.read_pickle('orders_all.pkl')
og=o.groupby('pid').ts.apply(lambda x:x.values.astype('datetime64[ns]')).to_dict()
d=[];prior=[]
for pid,ts in zip(s.pid,s.ts.values.astype('datetime64[ns]')):
    a=og.get(pid)
    if a is None: d.append(np.nan); prior.append(0); continue
    i=np.searchsorted(a,ts); prior.append(i)
    d.append((a[i]-ts)/np.timedelta64(1,'h')/24 if i<len(a) else np.nan)
s['dd']=d; s['prior']=prior; s['reg']=s.country.map(region)
print('unieke inschrijvers Uw8eZG',len(s),'waarvan al koper',(s.prior>0).sum(), round((s.prior>0).mean()*100,1),'%')
p=s[s.prior==0]
end=pd.Timestamp('2026-10-07',tz='UTC')
rows=[]
for lbl,D in [('1u',1/24),('dag 0 (24u)',1),('dag 1 (48u)',2),('dag 3',4),('dag 7',8),('dag 10',11),('dag 14',15),('dag 30',31),('dag 60',61),('dag 90',91)]:
    e=p[p.ts<end-pd.Timedelta(days=max(D,1))]
    rows.append({'venster':lbl,'cohort n':len(e),'% eerste order':round((e.dd<=D).mean()*100,2)})
print(pd.DataFrame(rows).to_string(index=False))
# daily hazard: probability of first order on day k given not yet bought
e=p[p.ts<end-pd.Timedelta(days=60)]
print('hazard cohort',len(e))
hz=[]
for k in range(0,60):
    at=e[~(e.dd<k)]
    hz.append((k,len(at),round(((at.dd>=k)&(at.dd<k+1)).mean()*100,3)))
for h in hz[:21]+hz[21::5]: print(' dag',h[0],'at risk',h[1],'kans',h[2],'%')
# share of 60-day buyers by day
b=e[e.dd<=60].dd
print('verdeling kopers binnen 60d (n=%d)'%len(b), pd.cut(b,[0,1/24,1,2,4,8,11,15,31,61],right=False).value_counts(sort=False).div(len(b)).mul(100).round(1).to_dict())
for r in ['US','AU','UK','CA','overig','onbekend']:
    x=p[(p.reg==r)&(p.ts<end-pd.Timedelta(days=31))]
    if len(x)>300: print(r,'n',len(x),'d0',round((x.dd<=1).mean()*100,2),'d10',round((x.dd<=11).mean()*100,2),'d30',round((x.dd<=31).mean()*100,2))
# signup hour local
s.to_pickle('subs_ep.pkl')
