from load import *
tz=pd.read_pickle('pid_tz.pkl'); ctry=pd.read_pickle('pid_country.pkl')
def localize(df):
    df=df.copy(); df['tz']=df.pid.map(tz)
    df=df[df.tz.notna()]
    hrs=[];wd=[]
    for t,z in zip(df.ts,df.tz):
        try: lt=t.tz_convert(z)
        except Exception: hrs.append(np.nan); wd.append(np.nan); continue
        hrs.append(lt.hour); wd.append(lt.dayofweek)
    df['h']=hrs; df['wd']=wd
    df['reg']=df.pid.map(ctry).map(region)
    return df.dropna(subset=['h'])
o=pd.read_pickle('orders_all.pkl'); o=o[o.ts>=pd.Timestamp('2025-10-07',tz='UTC')]
ol=localize(o)
cl=load('clicks.jsonl',('$flow','$message','Bot Click','URL'),loc=False)
cl=cl[cl['Bot Click']!=True]
cl=localize(cl)
op=load('opens.jsonl',('$flow','machine_open'))
op=localize(op[op.machine_open!=True])
op_all=None
out={}
def dist(df,col):
    return (df[col].value_counts(normalize=True).sort_index()*100).round(2)
pd.set_option('display.width',250)
H=pd.DataFrame({'orders alle':dist(ol,'h'),'orders US':dist(ol[ol.reg=='US'],'h'),'orders AU':dist(ol[ol.reg=='AU'],'h'),'orders UK':dist(ol[ol.reg=='UK'],'h'),
 'clicks flow':dist(cl[cl['$flow'].notna()],'h'),'clicks campagne':dist(cl[cl['$flow'].isna()],'h'),'opens (echte, 7d) flow':dist(op[op['$flow'].notna()],'h'),'opens campagne':dist(op[op['$flow'].isna()],'h')})
print('n: orders',len(ol),'US',(ol.reg=='US').sum(),'clicks flow',cl['$flow'].notna().sum(),'clicks campagne',cl['$flow'].isna().sum(),'opens',len(op))
print(H.to_string())
W=pd.DataFrame({'orders':dist(ol,'wd'),'orders US':dist(ol[ol.reg=='US'],'wd'),'clicks flow':dist(cl[cl['$flow'].notna()],'wd'),'clicks campagne':dist(cl[cl['$flow'].isna()],'wd')})
print(W.to_string())
H.to_csv('q3_hour.csv'); W.to_csv('q3_weekday.csv')
ol.to_pickle('orders_local.pkl'); cl.to_pickle('clicks_local.pkl')
