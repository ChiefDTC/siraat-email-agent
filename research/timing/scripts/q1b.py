from load import *
maxd=pd.Timestamp('2026-09-30',tz='UTC')
files={'checkout':'ep_Checkout_Star.pkl','cart':'ep_Added_to.pkl','view_api':'ep_view_api.pkl','view_tp':'ep_view_tp.pkl'}
T=[('5m',5),('10m',10),('15m',15),('30m',30),('1u',60),('2u',120),('4u',240),('12u',720),('24u',1440),('2d',2880),('3d',4320),('7d',10080)]
rows=[]
for k,f in files.items():
    e=pd.read_pickle(f); e=e[e.ts<maxd]
    if k=='checkout':
        # exclude no-location (mostly non-identified) none; keep all
        pass
    for base_lbl,base in [('5m',5),('15m',15),('60m',60)]:
        for seg,s in [('alle',e),('US',e[e.reg=='US']),('niet-US',e[(e.reg!='US')&(e.reg!='onbekend')])]+([('>=300',e[pd.to_numeric(e['$value'],errors='coerce')>=300]),('<300',e[pd.to_numeric(e['$value'],errors='coerce')<300])] if '$value' in e else [])+[('nieuw',e[e.prior==0]),('eerder gekocht',e[e.prior>0])]:
            a=s[~(s.delay<=base)]
            r={'trigger':k,'basis: nog niet gekocht na':base_lbl,'segment':seg,'n':len(a)}
            for l,m in T:
                if m<=base: continue
                r[l]=round(100*np.mean(a.delay<=m),2)
            rows.append(r)
R=pd.DataFrame(rows)
pd.set_option('display.width',300); pd.set_option('display.max_columns',30)
print(R.to_string(index=False))
R.to_csv('q1_conditional.csv',index=False)
