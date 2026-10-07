from recv import *
r=load_recv()
print('received n',len(r),r.ts.min(),r.ts.max())
o=pd.read_pickle('orders_all.pkl')
og=o.groupby('pid').ts.apply(lambda x:x.values.astype('datetime64[ns]')).to_dict()
arms={'Checkout Y2TmNB':[('10 min','RpzC3U',10),('30 min','RZ4Urm',30)],
      'Checkout Tsg2tV':[('10 min','X37MuT',10),('30 min','VGsrUf',30)],
      'Cart SwkMyn':[('15 min','W7cyzk',15),('30 min','URatk6',30)],
      'Browse Wj6x6V':[('10 min','Y7wqBq',10),('30 min','WUsPxr',30)],
      'Browse TyEjuQ':[('10 min','Vm6cZj',10),('30 min','Wwv3Tb',30)]}
rows=[]
for fl,al in arms.items():
    res={}
    for lbl,msg,dl in al:
        s=r[r['$message']==msg]
        s=s[s.ts< r.ts.max()-pd.Timedelta(days=7)]
        buy7=0;buy1h=0;buy24=0
        for pid,ts in zip(s.pid,s.ts.values.astype('datetime64[ns]')):
            a=og.get(pid)
            if a is None: continue
            i=np.searchsorted(a,ts)
            if i<len(a):
                d=(a[i]-ts)/np.timedelta64(1,'m')
                buy7+= d<=10080; buy1h+= d<=60; buy24+=d<=1440
        res[lbl]=(len(s),buy7,buy1h,buy24)
    (l1,(n1,b1,h1,d1)),(l2,(n2,b2,h2,d2))=list(res.items())
    diff=n1-n2
    rows.append({'flow':fl,f'ontvangers snel':n1,'kopers 7d snel':b1,'ontvangers 30m':n2,'kopers 7d 30m':b2,
                 'verschil ontvangers (=natuurlijke kopers tussen beide momenten in 30m-arm, schatting)':diff,
                 'totaal conversies snel-arm':b1,'totaal conversies 30m-arm (b2+diff)':b2+diff,
                 'kopers <=1u na mail snel':h1,'kopers <=1u na mail 30m':h2})
R=pd.DataFrame(rows)
pd.set_option('display.width',400)
print(R.T.to_string())
R.to_csv('q2_ab_delay.csv',index=False)
