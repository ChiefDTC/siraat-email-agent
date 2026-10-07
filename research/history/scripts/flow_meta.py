import sys, json; sys.path.insert(0,"/tmp/hist/scripts")
from kl import req, pages
from concurrent.futures import ThreadPoolExecutor
r=json.load(open('/tmp/hist/data/flow_values.json'))
ids=sorted({x['groupings']['flow_message_id'] for x in r})
flows,_=pages("https://a.klaviyo.com/api/flows?page[size]=50")
# archived flows too
fa,_=pages("https://a.klaviyo.com/api/flows?filter=equals(archived,true)&page[size]=50")
fl={f["id"]:f["attributes"] for f in flows+fa}
print("flows",len(fl))
def g(i): return i, req(f"https://a.klaviyo.com/api/flow-messages/{i}")
with ThreadPoolExecutor(3) as ex: msgs=dict(ex.map(g,ids))
json.dump({"flows":fl,"msgs":msgs},open("/tmp/hist/data/flow_meta.json","w"))
print(sum(1 for m in msgs.values() if "data" in m), "msgs ok")
