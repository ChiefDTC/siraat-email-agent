from load import *
o=pd.read_pickle('orders_all.pkl'); o=o[o.ts>=pd.Timestamp('2025-10-07',tz='UTC')].copy()
dc=o['Discount Codes'].map(lambda l: [c.upper() for c in l] if isinstance(l,list) else [])
from collections import Counter
cnt=Counter(c for l in dc for c in l)
print('orders 12m',len(o),'met code',round((dc.map(len)>0).mean()*100,1),'%')
print(cnt.most_common(25))
o['hi10']=dc.map(lambda l: 'HI10' in l)
print('HI10 orders',o.hi10.sum(), 'unieke profielen',o[o.hi10].pid.nunique())
# value split of checkout episodes
e=pd.read_pickle('ep_Checkout_Star.pkl')
v=pd.to_numeric(e['$value'],errors='coerce')
ab=e[~(e.delay<=15)]
va=pd.to_numeric(ab['$value'],errors='coerce')
print('checkout-verlaters (geen order binnen 15m) n',len(ab),'waarde>=300',round((va>=300).mean()*100,1),'% ; mediaan',va.median(), 'kwantielen',va.quantile([.25,.5,.75,.9]).to_dict())
print('regio verdeling verlaters',ab.reg.value_counts(normalize=True).round(3).to_dict())
print('eerdere koper',round((ab.prior>0).mean()*100,1))
hi=set(o[o.hi10].pid)
ab['hi10_before']=ab.pid.isin(hi)
print('verlaters die ooit HI10 gebruikten (12m)',round(ab.hi10_before.mean()*100,2),'%')
# recovery 7d by value buckets
ab['vb']=pd.cut(va,[0,100,150,200,300,500,10000])
maxd=pd.Timestamp('2026-09-30',tz='UTC')
x=ab[ab.ts<maxd]
print(x.groupby('vb',observed=True).apply(lambda s: pd.Series({'n':len(s),'herstel 24u %':round((s.delay<=1440).mean()*100,2),'herstel 7d %':round((s.delay<=10080).mean()*100,2)})).to_string())
c=pd.read_pickle('ep_Added_to.pkl'); abc=c[~(c.delay<=15)]; vc=pd.to_numeric(abc['$value'],errors='coerce')
print('cart-verlaters n',len(abc),'>=300',round((vc>=300).mean()*100,1),'%','mediaan',vc.median())
x=abc[abc.ts<maxd]; x=x.assign(vb=pd.cut(pd.to_numeric(x['$value'],errors='coerce'),[0,100,150,200,300,500,10000]))
print(x.groupby('vb',observed=True).apply(lambda s: pd.Series({'n':len(s),'7d %':round((s.delay<=10080).mean()*100,2)})).to_string())
