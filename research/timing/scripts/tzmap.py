from load import *
import json
D='/tmp/claude-0/-home-user/63cabcd2-6467-5149-aa57-034a09c8b336/scratchpad/data/'
m={};c={}
for f in ['orders.jsonl','checkouts.jsonl','atc.jsonl','subs.jsonl','clicks.jsonl','opens.jsonl','views_api.jsonl','delivered.jsonl']:
    for l in open(D+f):
        r=json.loads(l); L=r.get('loc') or {}
        if r['pid'] and L.get('tz'): m[r['pid']]=L['tz']
        if r['pid'] and L.get('c'): c[r['pid']]=L['c']
pd.Series(m).to_pickle('pid_tz.pkl'); pd.Series(c).to_pickle('pid_country.pkl')
print(len(m),len(c))
