from load import *
s=pd.read_pickle('subs_ep.pkl'); p=s[(s.prior==0)&~(s.dd*24<=1)]
p=p[p.ts<pd.Timestamp('2026-09-25',tz='UTC')]
co=pd.read_pickle('ep_Checkout_Star.pkl'); atc=pd.read_pickle('ep_Added_to.pkl'); va=pd.read_pickle('ep_view_api.pkl')
def within(df,days,abandoned_only=True):
    if abandoned_only: df=df[~(df.delay<=15)]
    g=df.groupby('pid').ts.apply(lambda x:x.values.astype('datetime64[ns]')).to_dict()
    out=[]
    for pid,ts in zip(p.pid,p.ts.values.astype('datetime64[ns]')):
        a=g.get(pid)
        if a is None: out.append(False); continue
        i=np.searchsorted(a,ts+np.timedelta64(1,'h'))
        out.append(i<len(a) and (a[i]-ts)/np.timedelta64(1,'D')<=days)
    return np.array(out)
print('prospects (geen order binnen 1u na inschrijving), n',len(p))
for nm,df in [('checkout verlaten',co),('cart verlaten',atc)]:
    for d in [3,10,14]:
        print(f' {nm} binnen {d}d na inschrijving: {within(df,d).mean()*100:.2f}%')
vv=va[va.ts>=pd.Timestamp('2026-08-08',tz='UTC')]
p2=p[p.ts>=pd.Timestamp('2026-08-08',tz='UTC')]
pp=p; p=p2
print(' (aug-sep subset n',len(p2),') product bekeken binnen 10d (onsite metric):',round(within(vv,10,False).mean()*100,2),'%')
p=pp
