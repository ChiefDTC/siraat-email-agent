from load import *
orders=pd.concat([load('orders_old.jsonl',('$value',)),load('orders.jsonl',('$value','Discount Codes'),loc=True)]).drop_duplicates('id').sort_values('ts')
orders=orders[orders.pid.notna()]
co=load('checkouts.jsonl',('$value',),loc=True)
atc=load('atc.jsonl',('$value','_ip_country_code'),loc=True)
va=load('views_api.jsonl',(),loc=True)
vt=load('views_tp.jsonl',())
print('n orders',len(orders),'co',len(co),'atc',len(atc),'views api',len(va),'views tp',len(vt))
# order time index per pid
og=orders.groupby('pid')['ts'].apply(lambda s: s.values.astype('datetime64[ns]')).to_dict()
def episodes(df,gap='7D'):
    df=df[df.pid.notna()].sort_values(['pid','ts']).copy()
    prev=df.groupby('pid')['ts'].shift()
    keep=prev.isna() | ((df.ts-prev)>pd.Timedelta(gap))
    return df[keep]
def next_order_delay(df):
    out=[]
    for pid,ts in zip(df.pid,df.ts.values.astype('datetime64[ns]')):
        arr=og.get(pid)
        if arr is None: out.append(np.nan); continue
        i=np.searchsorted(arr,ts)  # first order >= ts
        out.append((arr[i]-ts)/np.timedelta64(1,'m') if i<len(arr) else np.nan)
    return np.array(out)
def prior_orders(df):
    out=[]
    for pid,ts in zip(df.pid,df.ts.values.astype('datetime64[ns]')):
        arr=og.get(pid); out.append(0 if arr is None else int(np.searchsorted(arr,ts)))
    return np.array(out)
B=[15,60,240,1440,4320,10080]
L=['15m','1u','4u','24u','3d','7d']
def curve(df,name,maxdate):
    df=df[df.ts< maxdate - pd.Timedelta('7D')]
    d=df['delay']
    res={'groep':name,'n':len(df)}
    for b,l in zip(B,L): res[l]=round(100*np.mean(d<=b),2)
    # conditional: of not bought at 1h, bought 1h-24h
    return res
maxdate=pd.Timestamp('2026-10-07',tz='UTC')
rows=[]
for name,df in [('Checkout Started',co),('Added to Cart',atc),('Viewed Product (Klaviyo onsite)',va),('Viewed Product (Triple Pixel)',vt)]:
    e=episodes(df)
    e=e.assign(delay=next_order_delay(e),prior=prior_orders(e))
    if 'country' in e: e['reg']=e.country.map(region)
    else: e['reg']='onbekend'
    e.to_pickle(f'ep_{name.split()[0]}_{name.split()[1][:4]}.pkl' if 'View' not in name else ('ep_view_api.pkl' if 'onsite' in name else 'ep_view_tp.pkl'))
    rows.append(curve(e,name+' alle',maxdate))
    for r in ['US','AU','CA','UK','overig','onbekend']:
        s=e[e.reg==r]
        if len(s)>200: rows.append(curve(s,f'{name} {r}',maxdate))
    rows.append(curve(e[e.prior==0],name+' nieuwe klant',maxdate))
    rows.append(curve(e[e.prior>0],name+' eerdere koper',maxdate))
    if name!='Viewed Product (Triple Pixel)' and '$value' in e:
        v=pd.to_numeric(e['$value'],errors='coerce')
        rows.append(curve(e[v>=300],name+' waarde >= $300',maxdate))
        rows.append(curve(e[v<300],name+' waarde < $300',maxdate))
R=pd.DataFrame(rows)
pd.set_option('display.width',250)
print(R.to_string(index=False))
R.to_csv('q1_curves.csv',index=False)
