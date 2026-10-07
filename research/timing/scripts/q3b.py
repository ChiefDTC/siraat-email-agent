from recv import *
r=load_recv()
tz=pd.read_pickle('pid_tz.pkl'); ctry=pd.read_pickle('pid_country.pkl')
fc=pd.read_pickle('clicks_first.pkl')
o=pd.read_pickle('orders_all.pkl')
og=o.groupby('pid').ts.apply(lambda x:x.values.astype('datetime64[ns]')).to_dict()
r=r.copy(); r['tz']=r.pid.map(tz); r=r[r.tz.notna()]
# local hour of send
lh=[];wd=[]
for t,z in zip(r.ts,r.tz):
    try: lt=t.tz_convert(z); lh.append(lt.hour); wd.append(lt.dayofweek)
    except Exception: lh.append(-1); wd.append(-1)
r['lh']=lh; r['wd']=wd
r['reg']=r.pid.map(ctry).map(region)
# clicked within 3 days: key pid+message with click ts within [send, send+3d]
fc=fc[['pid','$message','send','ts']].rename(columns={'ts':'cts'})
fc['send_s']=fc.send.dt.floor('s')
r['send_s']=r.ts.dt.floor('s')
m=r.merge(fc[['pid','$message','send_s','cts']],on=['pid','$message','send_s'],how='left')
m=m.drop_duplicates('id')
m['clicked']=m.cts.notna()
# order within 24h of send
b=[]
for pid,ts in zip(m.pid,m.ts.values.astype('datetime64[ns]')):
    a=og.get(pid)
    if a is None: b.append(False); continue
    i=np.searchsorted(a,ts); b.append(i<len(a) and (a[i]-ts)/np.timedelta64(1,'h')<=24)
m['order24']=b
m['type']=np.where(m['$flow'].notna(),'flow','campagne')
ABAND={'Y2TmNB','Tsg2tV','SwkMyn','TBWngE','Wj6x6V','TyEjuQ'}
m['grp']=np.where(m['$flow'].isin(ABAND),'abandonment',np.where(m['$flow']=='SiaNLu','welcome',np.where(m.type=='campagne','campagne','overige flow')))
print('match check: kliks gematcht',m.clicked.sum(),'van',len(m))
pd.set_option('display.width',300)
for g in ['abandonment','welcome','campagne']:
    s=m[m.grp==g]
    t=s.groupby('lh').agg(n=('id','size'),ctr=('clicked','mean'),ord24=('order24','mean'))
    t['ctr']=(t.ctr*100).round(2); t['ord24']=(t.ord24*100).round(2)
    print('==',g,'n',len(s)); print(t.T.to_string())
    s.groupby('lh').agg(n=('id','size'),ctr=('clicked','mean'),ord24=('order24','mean')).to_csv(f'q3_sendhour_{g}.csv')
    w=s.groupby('wd').agg(n=('id','size'),ctr=('clicked','mean'),ord24=('order24','mean'))
    w['ctr']=(w.ctr*100).round(2); w['ord24']=(w.ord24*100).round(2); print(w.T.to_string())
# abandonment by send window buckets
s=m[m.grp=='abandonment']
s['win']=pd.cut(s.lh,[-1,5,7,11,16,20,23],labels=['00-06','06-08','08-12','12-17','17-21','21-24'])
print(s.groupby('win',observed=True).agg(n=('id','size'),ctr=('clicked','mean'),ord24=('order24','mean')).round(4).to_string())
m[['id','pid','ts','$flow','$message','lh','wd','reg','clicked','order24','grp']].to_pickle('recv_enriched.pkl')
