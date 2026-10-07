from recv import *
r=load_recv()
u=load('unsubs.jsonl',('message_id',))
sp=load('spam.jsonl',())
fam={'SiaNLu':'welcome','T2SmtR':'failure','Y2TmNB':'checkout','Tsg2tV':'checkout','SwkMyn':'cart','TBWngE':'cart','Wj6x6V':'browse','TyEjuQ':'browse','RL3TU6':'post','UEfh4h':'winback','WvRupU':'mystery','YcXbHx':'education','S7V4a7':'sunset'}
r=r.copy(); r['fam']=r['$flow'].map(fam)
r.loc[r['$flow'].isna(),'fam']='campagne'; r['fam']=r.fam.fillna('overige flow')
start=r.ts.min().normalize(); end=r.ts.max()
r['wk']=((r.ts-start).dt.days//7).astype(int)
r=r[r.wk<12]
print('venster',start,'12 weken; mails',len(r),'profielen',r.pid.nunique())
ct=pd.crosstab([r.pid,r.wk],r.fam)
ct['n']=ct.sum(axis=1)
def mark(ev):
    ev=ev[(ev.ts>=start)&ev.pid.notna()].copy(); ev['wk']=((ev.ts-start).dt.days//7).astype(int)
    s=set(zip(ev.pid,ev.wk)); return np.array([k in s for k in ct.index])
ct['unsub']=mark(u); ct['spam']=mark(sp)
ct['nb']=pd.cut(ct.n,[0,1,2,3,4,5,7,10,15,1000],labels=['1','2','3','4','5','6-7','8-10','11-15','16+'])
t=ct.groupby('nb',observed=True).agg(profielweken=('n','size'),mails=('n','sum'),unsub=('unsub','mean'),uns_n=('unsub','sum'),spam=('spam','mean'))
t['unsub% per profielweek']=(t.unsub*100).round(3); t['unsubs per 1000 mails']=(t.uns_n/t.mails*1000).round(2); t['spam% per profielweek']=(t.spam*100).round(3)
print(t[['profielweken','mails','unsub% per profielweek','unsubs per 1000 mails','spam% per profielweek']].to_string())
# only-campaign recipients vs campaign+flows
camp_only=ct[(ct.n==ct.get('campagne',0))]
print('campagne-only profielweken',len(camp_only))
t2=camp_only.groupby('nb',observed=True).agg(pw=('n','size'),unsub=('unsub','mean'))
t2['unsub%']=(t2.unsub*100).round(3); print('alleen campagnes:',t2[['pw','unsub%']].T.to_string())
w=ct.welcome>0
for other in ['checkout','cart','browse','failure','campagne','post']:
    b=w & (ct[other]>0); nb_=w & (ct[other]==0)
    print(f'welcome-week met {other}: {b.sum()} ({b.sum()/w.sum()*100:.1f}% van {w.sum()} welcome-weken) unsub {ct[b].unsub.mean()*100:.2f}% vs zonder {ct[nb_].unsub.mean()*100:.2f}%; mails/week {ct[b].n.mean():.1f} vs {ct[nb_].n.mean():.1f}')
sales=(ct.checkout>0).astype(int)+(ct.cart>0)+(ct.browse>0)
print('weken met >=1 verlatingsflow',(sales>=1).sum(),'>=2',(sales>=2).sum(), 'unsub 1 vs >=2:',round(ct[sales==1].unsub.mean()*100,2),round(ct[sales>=2].unsub.mean()*100,2))
print('mails per profielweek kwantielen',ct.n.quantile([.5,.75,.9,.95,.99]).to_dict())
print(r.fam.value_counts().to_string())
ct.to_pickle('profileweek.pkl')
