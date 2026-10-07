import sys, json, csv, os; sys.path.insert(0,"/tmp/hist/scripts")
from kl import req
from concurrent.futures import ThreadPoolExecutor
ids=set()
for f in ['campaigns_all.csv','flow_messages_all.csv']:
    for r in csv.DictReader(open('/tmp/hist/data/'+f)):
        for t in r['template_id'].split(' || '):
            if t.strip(): ids.add(t.strip())
os.makedirs('/tmp/hist/tpl',exist_ok=True)
todo=[i for i in ids if not os.path.exists(f'/tmp/hist/tpl/{i}.json')]
print(len(ids),len(todo))
def g(i):
    d=req(f"https://a.klaviyo.com/api/templates/{i}?fields[template]=name,editor_type,html,text,created,updated")
    json.dump(d,open(f'/tmp/hist/tpl/{i}.json','w'))
with ThreadPoolExecutor(3) as ex: list(ex.map(g,todo))
