from load import *
import ast
cl=load('clicks.jsonl',('$flow','$message','Bot Click','$internal','Campaign Name'))
cl=cl[cl['Bot Click']!=True].copy()
def ho(x):
    if isinstance(x,dict): return x.get('Handoff Time')
    return None
cl['send']=pd.to_datetime(cl['$internal'].map(ho),unit='s',utc=True)
cl['lat_min']=(cl.ts-cl.send).dt.total_seconds()/60
cl['type']=np.where(cl['$flow'].notna(),'flow','campagne')
# first click per message send per profile
fc=cl.sort_values('ts').drop_duplicates(['pid','$message','send'])
print('unieke klikken (eerste per ontvanger per mail) n',len(fc),'met send-tijd',fc.send.notna().sum())
Q=[.1,.25,.5,.75,.9]
for t,s in fc.groupby('type'):
    x=s.lat_min.dropna(); x=x[x>=0]
    print(t,'send->klik minuten kwantielen',x.quantile(Q).round(0).to_dict())
    print('   cumulatief % klikken binnen', {k: round((x<=m).mean()*100,1) for k,m in [('1u',60),('4u',240),('24u',1440),('48u',2880),('72u',4320),('7d',10080)]})
op=load('opens.jsonl',('$flow','$message','machine_open','$internal'))
op=op[op.machine_open!=True].copy()
op['send']=pd.to_datetime(op['$internal'].map(ho),unit='s',utc=True)
op['lat']=(op.ts-op.send).dt.total_seconds()/60
fo=op.sort_values('ts').drop_duplicates(['pid','$message','send'])
fo['type']=np.where(fo['$flow'].notna(),'flow','campagne')
for t,s in fo.groupby('type'):
    x=s.lat.dropna(); x=x[x>=0]
    print(t,'send->echte open (7d steekproef) n',len(x),x.quantile(Q).round(0).to_dict(), {k: round((x<=m).mean()*100,1) for k,m in [('1u',60),('4u',240),('24u',1440),('48u',2880)]})
# open -> click: for clicks, find first real open of same pid+message before click
m=fc.merge(fo[['pid','$message','send','ts']].rename(columns={'ts':'open_ts'}),on=['pid','$message','send'],how='inner')
x=(m.ts-m.open_ts).dt.total_seconds()/60; x=x[x>=0]
print('open->klik (alleen echte opens) n',len(x),x.quantile(Q).round(1).to_dict())
# click -> order
o=pd.read_pickle('orders_all.pkl'); o=o[o.ts>=pd.Timestamp('2025-10-07',tz='UTC')]
cg=fc.sort_values('ts').groupby('pid')
carr={pid:(g.ts.values.astype('datetime64[ns]'),g.send.values.astype('datetime64[ns]'),g.type.values,g['$flow'].values) for pid,g in cg}
rows=[]
for pid,ts in zip(o.pid,o.ts.values.astype('datetime64[ns]')):
    a=carr.get(pid)
    if a is None: continue
    i=np.searchsorted(a[0],ts)-1
    if i<0: continue
    dt=(ts-a[0][i])/np.timedelta64(1,'m')
    if dt>7*1440: continue
    rows.append((dt,(ts-a[1][i])/np.timedelta64(1,'m'),a[2][i],a[3][i]))
r=pd.DataFrame(rows,columns=['click_to_order','send_to_order','type','flow'])
print('orders met klik binnen 7d ervoor n',len(r),'van',len(o))
for t,s in r.groupby('type'):
    x=s.click_to_order
    print(t,'klik->order min',x.quantile(Q).round(0).to_dict(),{k: round((x<=mm).mean()*100,1) for k,mm in [('10m',10),('30m',30),('1u',60),('4u',240),('24u',1440),('48u',2880),('5d',7200)]})
    y=s.send_to_order.dropna()
    print('   send->order (uren)',(y/60).quantile(Q).round(1).to_dict(),{k: round((y<=mm).mean()*100,1) for k,mm in [('1u',60),('4u',240),('24u',1440),('48u',2880),('72u',4320),('5d',7200)]})
r.to_pickle('click_order.pkl'); fc.to_pickle('clicks_first.pkl')
