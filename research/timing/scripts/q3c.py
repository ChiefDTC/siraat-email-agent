from recv import *
m=pd.read_pickle('recv_enriched.pkl')
fc=pd.read_pickle('clicks_first.pkl')[['pid','$message','ts']].rename(columns={'ts':'cts'}).dropna()
m=m[m.grp!='campagne'].copy() if False else m.copy()
m=m.sort_values('ts'); fc=fc.sort_values('cts')
fc['key']=fc.pid+'|'+fc['$message'].astype(str); m['key']=m.pid+'|'+m['$message'].astype(str)
x=pd.merge_asof(m,fc[['key','cts']],left_on='ts',right_on='cts',by='key',direction='forward',tolerance=pd.Timedelta('3D'))
x['clicked']=x.cts.notna()
print('clicked share',x.clicked.mean())
FIRST={'RpzC3U','RZ4Urm','X37MuT','VGsrUf','R4g5Wr','W7cyzk','URatk6','Y7wqBq','WUsPxr','Vm6cZj','Wwv3Tb','VWL44n','SUi5iD'}
x['kind']=np.where(x['$message'].isin(FIRST),'realtime (mail 1 verlating)',np.where(x.grp=='abandonment','verlating vervolg (tot 08:00)',x.grp))
pd.set_option('display.width',300)
x['win']=pd.cut(x.lh,[-1,5,7,9,11,13,16,18,20,21,23],labels=['00-06','06-08','08-10','10-12','12-14','14-17','17-19','19-21','21-22','22-24'])
for k in ['realtime (mail 1 verlating)','verlating vervolg (tot 08:00)','welcome','campagne']:
    s=x[x.kind==k]
    t=s.groupby('win',observed=True).agg(n=('id','size'),ctr=('clicked','mean'),ord24=('order24','mean'))
    t['ctr%']=(t.ctr*100).round(2); t['order24%']=(t.ord24*100).round(2)
    print('==',k,len(s)); print(t[['n','ctr%','order24%']].T.to_string())
    w=s.groupby('wd').agg(n=('id','size'),ctr=('clicked','mean'),ord24=('order24','mean'))
    w['ctr%']=(w.ctr*100).round(2); w['order24%']=(w.ord24*100).round(2); print(w[['n','ctr%','order24%']].T.to_string())
x[['id','pid','ts','$flow','$message','lh','wd','reg','clicked','order24','grp','kind']].to_pickle('recv_enriched2.pkl')
