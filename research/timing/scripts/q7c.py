from load import *
d=load('delivered.jsonl',('Delivery Hours','Transit Hours','$value'),loc=True)
f=load('fulfilled.jsonl',('FulfillmentHours',))
print('delivered n',len(d),d.ts.min(),d.ts.max())
for c in ['Delivery Hours','Transit Hours']:
    x=pd.to_numeric(d[c],errors='coerce')/24
    print(c,'n',x.notna().sum(),'dagen kwantielen',x.quantile([.1,.25,.5,.75,.9]).round(1).to_dict())
d['reg']=d.country.map(region)
d['dd']=pd.to_numeric(d['Delivery Hours'],errors='coerce')/24
print(d.groupby('reg').dd.describe(percentiles=[.25,.5,.75,.9]).round(1))
# recent 90 days
r=d[d.ts>pd.Timestamp('2026-07-09',tz='UTC')]
print('laatste 90d', r.groupby('reg').dd.describe(percentiles=[.25,.5,.75,.9]).round(1))
x=pd.to_numeric(f.FulfillmentHours,errors='coerce')/24
print('fulfillment n',x.notna().sum(),x.quantile([.1,.25,.5,.75,.9]).round(1).to_dict())
# coverage: share of orders (last 90d) with delivered event
o=pd.read_pickle('orders_all.pkl'); o90=o[(o.ts>pd.Timestamp('2026-07-09',tz='UTC'))&(o.ts<pd.Timestamp('2026-09-20',tz='UTC'))]
dp=set(d.pid)
print('orders 9 jul-20 sep',len(o90),'with Delivered Shipment for same profile', round(o90.pid.isin(dp).mean()*100,1),'%')
o90r=o90.assign(reg=o90.country.map(region))
print(o90r.groupby('reg').apply(lambda s: round(s.pid.isin(dp).mean()*100,1)))
