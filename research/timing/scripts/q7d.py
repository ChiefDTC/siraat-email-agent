from load import *
d=load('delivered.jsonl',('Delivery Hours','Transit Hours'),loc=True)
o=pd.read_pickle('orders_all.pkl')
f=load('fulfilled.jsonl',('FulfillmentHours',))
og=o.groupby('pid').ts.apply(lambda s:s.values.astype('datetime64[ns]')).to_dict()
fg=f[f.pid.notna()].groupby('pid').ts.apply(lambda s:s.values.astype('datetime64[ns]')).to_dict()
res=[];resf=[]
for pid,ts in zip(d.pid,d.ts.values.astype('datetime64[ns]')):
    a=og.get(pid)
    if a is None: res.append(np.nan); resf.append(np.nan); continue
    i=np.searchsorted(a,ts)-1
    res.append((ts-a[i])/np.timedelta64(1,'h')/24 if i>=0 else np.nan)
    b=fg.get(pid)
    if b is None: resf.append(np.nan); continue
    k=np.searchsorted(b,ts)-1
    resf.append((ts-b[k])/np.timedelta64(1,'h')/24 if k>=0 else np.nan)
d['order_to_deliv']=res; d['ful_to_deliv']=resf
d['reg']=d.country.map(region)
d['DH']=pd.to_numeric(d['Delivery Hours'],errors='coerce')/24
print(d[['order_to_deliv','ful_to_deliv','DH']].describe(percentiles=[.1,.25,.5,.75,.9]).round(1))
print(d.groupby('reg').order_to_deliv.describe(percentiles=[.25,.5,.75,.9]).round(1))
print('corr',d[['order_to_deliv','DH']].corr().iloc[0,1])
