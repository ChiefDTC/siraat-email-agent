import json, pandas as pd, numpy as np
D='/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/data/'
def load(name, props=(), loc=False):
    rows=[]
    with open(D+name) as f:
        for l in f:
            r=json.loads(l)
            d={'id':r['id'],'pid':r['pid'],'ts':r['ts']}
            for p in props: d[p]=r['p'].get(p)
            if loc:
                L=r.get('loc') or {}
                d['country']=L.get('c'); d['tz']=L.get('tz')
            rows.append(d)
    df=pd.DataFrame(rows).drop_duplicates('id')
    df['ts']=pd.to_datetime(df['ts'],utc=True)
    return df.sort_values('ts').reset_index(drop=True)
def region(c):
    if c is None or (isinstance(c,float)) : return 'onbekend'
    if c in ('United States','US'): return 'US'
    if c in ('Australia',): return 'AU'
    if c in ('Canada',): return 'CA'
    if c in ('United Kingdom',): return 'UK'
    return 'overig'
