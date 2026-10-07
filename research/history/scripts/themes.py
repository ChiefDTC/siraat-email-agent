import csv,re,statistics as st
from collections import defaultdict
rows=list(csv.DictReader(open('/tmp/hist/data/campaigns_feat.csv')))
T=[('founder_text',r'founder|plain text|text based|note from|benjamin|letter|tariff'),
   ('education_howto',r'how to|why food|tips|care|guide|recipe|hack|mistake|fix|clean|store'),
   ('comparison',r'\bvs\b|versus|comparison|compare|showdown'),
   ('pfas_health',r'pfas|toxic|micro.?plastic|chemical|health|healthier|forever'),
   ('social_proof_reviews',r'review|bestseller|best seller|most.?loved|top rated|customers|favourite|favorite|chefs love'),
   ('launch_new',r'launch|new arrival|introduc|lid|restock|back in stock|is here'),
   ('gift_bonus',r'gift|bonus|free '),
   ('sale_deadline',r'last call|ends|ending|hours left|final|tonight|extension|reminder|last push|timer'),
   ('sale_launch',r'sale|% off|off sitewide|black friday|cyber|labor day|memorial|prime|clearance|warehouse|deal|special offer|vip|early access|pay ?day'),
   ('seasonal_story',r'father|mother|thanksgiving|christmas|holiday|anniversary|valentine|easter|summer|family|cravings')]
for r in rows:
    s=(r['campaign_name']+' '+r['subject']+' '+r['preview']).lower()
    r['theme']=next((k for k,p in T if re.search(p,s)),'other')
with open('/tmp/hist/data/campaigns_feat.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
big=[r for r in rows if int(r['recipients'])>=1000 and r['rpr_index_month']]
def rep(sub,label):
    g=defaultdict(list)
    for r in sub: g[r['theme']].append(r)
    print('==',label)
    for k,v in sorted(g.items(),key=lambda kv:-st.median(float(x['rpr_index_month']) for x in kv[1])):
        d=sum(int(x['delivered']) for x in v)
        print(f"{k:22} n={len(v):3} medRPRidx={st.median(float(x['rpr_index_month']) for x in v):.2f} medClickIdx={st.median(float(x['click_index_month']) for x in v):.2f} RPR(w)={sum(float(x['revenue']) for x in v)/d:.3f} click(w)={sum(float(x['click_rate'])*int(x['delivered']) for x in v)/d*100:.2f}% unsub(w)={sum(int(x['unsubs']) for x in v)/d*100:.2f}%")
rep(big,'alle')
rep([r for r in big if r['bfcm']=='False'],'zonder BFCM')
def imgb(r):
    n=int(r['n_img'] or 0); return '0-3' if n<=3 else '4-6' if n<=6 else '7-10' if n<=10 else '11+'
g=defaultdict(list)
for r in big: g[imgb(r)].append(r)
print('== beelden')
for k,v in sorted(g.items()):
    d=sum(int(x['delivered']) for x in v)
    print(k,len(v),round(st.median(float(x['rpr_index_month']) for x in v),2),round(st.median(float(x['click_index_month']) for x in v),2),round(sum(int(x['unsubs']) for x in v)/d*100,2))
