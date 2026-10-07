import json, csv
from collections import defaultdict
V=json.load(open('/tmp/hist/data/flow_values.json')); M=json.load(open('/tmp/hist/data/flow_meta.json'))
fl=M["flows"]; msgs=M["msgs"]
agg=defaultdict(lambda: defaultdict(float)); wins=defaultdict(set)
for x in V:
    k=(x["groupings"]["flow_id"],x["groupings"]["flow_message_id"])
    for s,v in x["statistics"].items(): agg[k][s]+=v or 0
    if x["statistics"].get("recipients"): wins[k].add(x["window"])
rows=[]
for (fid,mid),s in agg.items():
    f=fl.get(fid,{}); m=(msgs.get(mid) or {}).get("data",{}).get("attributes",{}); d=m.get("definition") or {}
    dl=s["delivered"] or 1
    rows.append(dict(flow_id=fid,flow_name=f.get("name",""),flow_status=f.get("status",""),archived=f.get("archived",""),trigger=f.get("trigger_type",""),
      message_id=mid,message_name=d.get("name",""),subject=d.get("subject_line",""),preview=d.get("preview_text",""),from_label=d.get("from_label",""),template_id=d.get("template_id",""),
      created=(m.get("created") or "")[:10],windows="+".join(sorted(wins[(fid,mid)])),
      recipients=int(s["recipients"]),delivered=int(s["delivered"]),open_rate=round(s["opens_unique"]/dl,4),click_rate=round(s["clicks_unique"]/dl,4),
      conversion_rate=round(s["conversion_uniques"]/dl,5),orders=int(s["conversions"]),revenue=round(s["conversion_value"],2),rpr=round(s["conversion_value"]/dl,4),
      unsub_rate=round(s["unsubscribe_uniques"]/dl,5),spam_rate=round(s["spam_complaints"]/dl,5),unsubs=int(s["unsubscribe_uniques"]),spam=int(s["spam_complaints"])))
rows.sort(key=lambda r:(r["flow_name"],r["created"]))
with open('/tmp/hist/data/flow_messages_all.csv','w',newline='') as fo:
    w=csv.DictWriter(fo,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), round(sum(r["revenue"] for r in rows)), sum(r["delivered"] for r in rows), sum(1 for r in rows if r["recipients"]>=1000))
print(sum(1 for r in rows if not r["flow_name"]))
