import sys, json; sys.path.insert(0,"/tmp/hist/scripts")
from kl import pages
allc=[];inc=[]
for arch in ["false","true"]:
    u=f"https://a.klaviyo.com/api/campaigns?filter=and(equals(messages.channel,'email'),equals(archived,{arch}))&include=campaign-messages"
    d,i=pages(u); allc+=d; inc+=i
json.dump({"data":allc,"included":inc},open("/tmp/hist/data/campaigns.json","w"))
from collections import Counter
print(len(allc), Counter(c["attributes"]["status"] for c in allc))
print(min(c["attributes"]["send_time"] or "z" for c in allc))
