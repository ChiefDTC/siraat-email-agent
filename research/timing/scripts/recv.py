from load import *
def load_recv():
    import os
    if os.path.exists('recv.pkl'): return pd.read_pickle('recv.pkl')
    a=load('received.jsonl',('$flow','$message','Campaign Name'))
    b=load('received_old.jsonl',('$flow','$message','Campaign Name'))
    r=pd.concat([a,b]).drop_duplicates('id').sort_values('ts').reset_index(drop=True)
    r=r[r.pid.notna()]
    r.to_pickle('recv.pkl'); return r
