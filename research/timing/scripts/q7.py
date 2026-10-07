from load import *
o=pd.concat([load('orders_old.jsonl',('$value','Items')),load('orders.jsonl',('$value','Items','Discount Codes','Source Name'),loc=True)]).drop_duplicates('id').sort_values('ts')
o=o[o.pid.notna()].copy()
o['val']=pd.to_numeric(o['$value'],errors='coerce')
print('orders',len(o),'profiles',o.pid.nunique(),'range',o.ts.min(),o.ts.max())
o['n']=o.groupby('pid').cumcount()+1
first=o[o.n==1].set_index('pid')
second=o[o.n==2].set_index('pid')
j=first[['ts','val','Items']].join(second[['ts','val','Items']],rsuffix='2',how='left')
j['gap']=(j.ts2-j.ts).dt.total_seconds()/86400
# exclude same-session duplicates (<1 day) separately
print('first orders',len(j),'with 2nd',j.gap.notna().sum())
print('2nd order within <1 day share of repeaters', round(np.mean(j.gap.dropna()<1)*100,1))
g=j.gap.dropna(); g1=g[g>=1]
print('gap>=1d n',len(g1),'median',g1.median(),'quantiles',g1.quantile([.1,.25,.5,.75,.9]).round(1).to_dict())
# cumulative repeat rate by days since first order, for cohorts with enough follow-up
end=pd.Timestamp('2026-10-07',tz='UTC')
rows=[]
for D in [7,14,30,45,60,90,120,180,270,365]:
    elig=j[j.ts< end-pd.Timedelta(days=D)]
    rep=((elig.gap>=1)&(elig.gap<=D)).mean()
    rows.append({'dagen na 1e order':D,'n cohort':len(elig),'% 2e order (>=1d)':round(rep*100,2)})
print(pd.DataFrame(rows).to_string(index=False))
# histogram buckets of gap
bins=[1,7,14,21,30,45,60,90,120,180,270,400]
h=pd.cut(g1,bins,right=False).value_counts().sort_index()
print((h/len(g1)*100).round(1).to_string())
# hazard: conditional prob of repeating in window given no repeat yet (cohort with 365d? use cohort first order before 2025-12-01)
c=j[j.ts<pd.Timestamp('2026-04-07',tz='UTC')]
print('cohort 6m+ follow-up n',len(c))
for a,b in [(0,30),(30,60),(60,90),(90,120),(120,180)]:
    at_risk=c[~((c.gap>=1)&(c.gap<a))] if a>0 else c
    at_risk=at_risk[~(at_risk.gap<1)] if a==0 else at_risk
    p=((at_risk.gap>=max(a,1))&(at_risk.gap<b)).mean()
    print(f' dag {a}-{b}: at risk {len(at_risk)} repeat {p*100:.2f}%')
# product category of first order
def cat(items):
    s=' '.join(items) if isinstance(items,list) else str(items)
    s=s.lower()
    if 'set' in s and ('pcs' in s or 'pc' in s or 'cookware set' in s): return 'set'
    if 'pan' in s: return 'pan'
    return 'accessoire/overig'
j['cat']=j.Items.map(cat)
j['cat2']=j.Items2.map(lambda x: cat(x) if isinstance(x,list) else None)
for k,s in j.groupby('cat'):
    e=s[s.ts<end-pd.Timedelta(days=90)]
    print(k,'n',len(s),'repeat90',round(((e.gap>=1)&(e.gap<=90)).mean()*100,2),'median gap',round(s.gap[s.gap>=1].median(),1),'aov',round(s.val.median(),0))
print(pd.crosstab(j.cat,j.cat2))
j.to_pickle('firstsecond.pkl'); o.to_pickle('orders_all.pkl')
