import sys, json; sys.path.insert(0,"/tmp/hist/scripts")
from kl import req
stats=["recipients","delivered","opens_unique","clicks_unique","conversion_uniques","conversion_value","conversions","unsubscribe_uniques","spam_complaints","bounced"]
res=[]
for s,e in [("2024-10-08T00:00:00","2025-10-07T00:00:00"),("2025-10-07T00:00:00","2026-10-07T23:59:59")]:
    body={"data":{"type":"flow-values-report","attributes":{"statistics":stats,"timeframe":{"start":s,"end":e},"conversion_metric_id":"RSNxYV","group_by":["flow_id","flow_message_id","send_channel"],"filter":"equals(send_channel,\"email\")"}}}
    url="https://a.klaviyo.com/api/flow-values-reports"
    n=0
    while url:
        d=req(url,body)
        if "data" not in d: print(json.dumps(d)[:1500]); break
        r=d["data"]["attributes"]["results"]
        for x in r: x["window"]=s[:10]
        res+=r; n+=len(r)
        url=(d.get("links") or {}).get("next")
    print(s,n)
json.dump(res,open("/tmp/hist/data/flow_values.json","w"))
