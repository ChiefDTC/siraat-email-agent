import json, csv, re
from collections import defaultdict
C=json.load(open('/tmp/hist/data/campaigns.json'))
camps={c["id"]:c for c in C["data"]}
msgs={m["id"]:m for m in C["included"] if m["type"]=="campaign-message"}
V=json.load(open('/tmp/hist/data/camp_values.json'))
agg=defaultdict(lambda: defaultdict(float))
for x in V:
    k=(x["groupings"]["campaign_id"],x["groupings"]["campaign_message_id"])
    for s,v in x["statistics"].items():
        if s in ("recipients","delivered","opens_unique","clicks_unique","conversion_uniques","conversion_value","conversions","unsubscribe_uniques","spam_complaints","bounced"):
            agg[k][s]+=v or 0
rows=[]
for (cid,mid),s in agg.items():
    c=camps.get(cid,{}).get("attributes",{})
    ms=sorted([mm for mm in msgs.values() if mm["relationships"]["campaign"]["data"]["id"]==cid],key=lambda mm:mm["attributes"]["definition"].get("label",""))
    m=ms[0] if ms else {}
    ma=m.get("attributes",{})
    J=lambda f:" || ".join(f(mm) or "" for mm in ms)
    cont={"subject":J(lambda mm:mm["attributes"]["definition"]["content"].get("subject")),"preview_text":J(lambda mm:mm["attributes"]["definition"]["content"].get("preview_text")),"from_label":ms[0]["attributes"]["definition"]["content"].get("from_label") if ms else ""}
    tpl=J(lambda mm:((mm["relationships"].get("template") or {}).get("data") or {}).get("id",""))
    st=(ma.get("send_times") or [{}])
    d=s["delivered"] or 1
    nvar=sum(1 for mm in msgs.values() if mm["relationships"]["campaign"]["data"]["id"]==cid)
    rows.append(dict(send_time=(c.get("send_time") or (st[0].get("datetime") if st else "") or "")[:16].replace("T"," "),
        campaign_id=cid,message_id=mid,campaign_name=c.get("name",""),variant=(ma.get("definition") or {}).get("label",""),n_messages=nvar,
        subject=cont.get("subject",""),preview=cont.get("preview_text",""),from_label=cont.get("from_label",""),template_id=tpl,
        is_local=(st[0].get("is_local") if st else ""),
        recipients=int(s["recipients"]),delivered=int(s["delivered"]),
        open_rate=round(s["opens_unique"]/d,4),click_rate=round(s["clicks_unique"]/d,4),
        conversion_rate=round(s["conversion_uniques"]/d,5),orders=int(s["conversions"]),revenue=round(s["conversion_value"],2),
        rpr=round(s["conversion_value"]/d,4),unsub_rate=round(s["unsubscribe_uniques"]/d,5),spam_rate=round(s["spam_complaints"]/d,5),
        unsubs=int(s["unsubscribe_uniques"]),spam=int(s["spam_complaints"])))
rows.sort(key=lambda r:r["send_time"])
with open('/tmp/hist/data/campaigns_all.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(len(rows), sum(r["revenue"] for r in rows), sum(r["delivered"] for r in rows))
print(rows[0]["send_time"], rows[-1]["send_time"])
big=[r for r in rows if r["recipients"]>=1000]; print("big",len(big))
