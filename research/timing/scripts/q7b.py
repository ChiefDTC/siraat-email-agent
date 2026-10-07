import pandas as pd, numpy as np
from collections import Counter
o=pd.read_pickle('orders_all.pkl'); j=pd.read_pickle('firstsecond.pkl')
c=Counter(i for l in o.Items if isinstance(l,list) for i in l)
print([ (k,v) for k,v in c.items() if any(w in k.lower() for w in ['strip','dish','sheet','deterg','clean','refill','subscription'])])
GIFT=['mystery','gift','e-book','e-guide','free shipping','shipping protection','100% off','giveaway','free lid','free ']
def real(items):
    if not isinstance(items,list): return []
    return [i for i in items if not any(g in i.lower() for g in GIFT)]
def cat(items):
    r=real(items)
    if not r: return 'alleen gifts/onbekend'
    if any(('set with lids' in i.lower()) or ('cookware set' in i.lower()) or ('pcs' in i.lower()) for i in r): return 'set'
    if any('pan' in i.lower() or 'wok' in i.lower() for i in r): return 'pan'
    return 'accessoire'
j['cat']=j.Items.map(cat); j['cat2']=j.Items2.map(lambda x: cat(x) if isinstance(x,list) else None)
end=pd.Timestamp('2026-10-07',tz='UTC')
for k,s in j.groupby('cat'):
    e=s[s.ts<end-pd.Timedelta(days=90)]
    g=s.gap[s.gap>=1]
    print(f"{k}: n={len(s)} repeat<=30d={((e.gap>=1)&(e.gap<=30)).mean()*100:.2f}% repeat<=90d={((e.gap>=1)&(e.gap<=90)).mean()*100:.2f}% (cohort n={len(e)}) mediaan gap={g.median():.1f} p25={g.quantile(.25):.1f} p75={g.quantile(.75):.1f} mediaan AOV={s.val.median():.0f}")
print(pd.crosstab(j.cat,j.cat2,margins=True))
# what do repeaters buy on 2nd order: top real items
c2=Counter(i for l in j.Items2.dropna() for i in real(l))
print('top items in 2nd order:',c2.most_common(20))
# repeat timing by first-order value
j['vb']=pd.cut(j.val,[0,150,300,10000],labels=['<150','150-300','>=300'])
for k,s in j.groupby('vb',observed=True):
    e=s[s.ts<end-pd.Timedelta(days=90)]
    print('waarde',k,len(s),'repeat90',round(((e.gap>=1)&(e.gap<=90)).mean()*100,2),'median gap',round(s.gap[s.gap>=1].median(),1))
# region
o2=o.copy(); 
reg=o2.groupby('pid').country.first()
j['reg']=reg.reindex(j.index).map(lambda c: 'US' if c=='United States' else ('onbekend' if c is None or (isinstance(c,float)) else 'niet-US'))
for k,s in j.groupby('reg'):
    e=s[s.ts<end-pd.Timedelta(days=90)]
    print('regio',k,len(s),'repeat90',round(((e.gap>=1)&(e.gap<=90)).mean()*100,2),'median gap',round(s.gap[s.gap>=1].median(),1))
# 3rd order timing
o['n']=o.groupby('pid').cumcount()+1
t=o[o.n<=3].pivot_table(index='pid',columns='n',values='ts',aggfunc='first')
t=t.dropna(subset=[2,3]); gg=(t[3]-t[2]).dt.total_seconds()/86400; gg=gg[gg>=1]
print('2e->3e order n',len(gg),'median',round(gg.median(),1),gg.quantile([.25,.75]).round(1).to_dict())
j.to_pickle('firstsecond.pkl')
