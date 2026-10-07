import sys, json; sys.path.insert(0,"/tmp/hist/scripts")
from kl import req
stats=["recipients","delivered","opens_unique","clicks_unique","conversion_uniques","conversion_value","conversions","unsubscribe_uniques","spam_complaints","bounced","open_rate","click_rate","conversion_rate","revenue_per_recipient","unsubscribe_rate"]
res=[]
for s,e in [("2025-01-01T00:00:00","2025-12-31T23:59:59"),("2026-01-01T00:00:00","2026-10-08T00:00:00")]:
    body={"data":{"type":"campaign-values-report","attributes":{"statistics":stats,"timeframe":{"start":s,"end":e},"conversion_metric_id":"RSNxYV","group_by":["campaign_id","campaign_message_id","send_channel"],"filter":"equals(send_channel,\"email\")"}}}
    d=req("https://a.klaviyo.com/api/campaign-values-reports",body)
    if "data" not in d: print(json.dumps(d)[:1500]); continue
    r=d["data"]["attributes"]["results"]; print(s,len(r)); res+=r
json.dump(res,open("/tmp/hist/data/camp_values.json","w"))
