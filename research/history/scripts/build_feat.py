import sys,csv,json,re,statistics as st; sys.path.insert(0,'/tmp/hist/scripts')
from features import *
from collections import defaultdict
def run(src,out,kind):
    rows=list(csv.DictReader(open(src)))
    for r in rows:
        tids=[t.strip() for t in r['template_id'].split('||') if t.strip()]
        p=parse(tids[0]) if tids else None
        subj=r['subject'].split(' || ')[0]
        r.update(subj_feat(subj))
        pv=r['preview'].split(' || ')[0]
        r['p_len']=len(pv)
        if p:
            full=subj+' '+pv+' '+p['text']+' '+p['alts']
            r.update(offer_feat(full))
            pr=products(p['text']+' '+p['alts']+' '+subj)
            r['main_product']=max(pr,key=pr.get) if max(pr.values())>0 else 'none'
            r['products']=';'.join(f'{k}:{v}' for k,v in sorted(pr.items(),key=lambda x:-x[1]) if v)
            r['words']=p['words']; r['n_img']=p['n_img']; r['n_links']=p['n_links']; r['editor']=p['editor']; r['html_kb']=p['html_kb']
            r['format']='image-only' if p['words']<60 else ('text' if p['n_img']<=2 else 'hybrid')
            r['img_alts']=' | '.join(a for a,_,_ in p['imgs'][:5])[:300]
        if kind=='camp':
            m=re.search(r'\|\s*(.*)$',r['campaign_name']); r['audience']=(m.group(1) if m else '').strip()[:40]
            r['month']=r['send_time'][:7]
            r['bfcm']=r['send_time'][:10]>='2025-11-20' and r['send_time'][:10]<='2025-12-02'
    if kind=='camp':
        big=[r for r in rows if int(r['recipients'])>=1000]
        bym=defaultdict(list)
        for r in big: bym[r['month']].append(float(r['rpr']))
        bymc=defaultdict(list)
        for r in big: bymc[r['month']].append(float(r['click_rate']))
        for r in rows:
            m=st.median(bym[r['month']]) if bym.get(r['month']) else None
            r['rpr_index_month']=round(float(r['rpr'])/m,2) if m else ''
            mc=st.median(bymc[r['month']]) if bymc.get(r['month']) else None
            r['click_index_month']=round(float(r['click_rate'])/mc,2) if mc else ''
    else:
        def cat(n):
            n=n.lower()
            for k in ['checkout','cart','browse','welcome','post purchase','winback','failure','sunset','review','trustpilot','e-book','guide','education','flash','gift','back in stock']:
                if k in n: return k
            return 'other'
        for r in rows: r['category']=cat(r['flow_name'])
        big=[r for r in rows if int(r['recipients'])>=1000]
        byc=defaultdict(list); bycc=defaultdict(list)
        for r in big: byc[r['category']].append(float(r['rpr'])); bycc[r['category']].append(float(r['click_rate']))
        for r in rows:
            m=st.median(byc[r['category']]) if byc.get(r['category']) else None
            r['rpr_index_cat']=round(float(r['rpr'])/m,2) if m else ''
            mc=st.median(bycc[r['category']]) if bycc.get(r['category']) else None
            r['click_index_cat']=round(float(r['click_rate'])/mc,2) if mc else ''
    keys=[]
    for r in rows:
        for k in r:
            if k not in keys: keys.append(k)
    with open(out,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys); w.writeheader(); w.writerows(rows)
    print(out,len(rows))
run('/tmp/hist/data/campaigns_all.csv','/tmp/hist/data/campaigns_feat.csv','camp')
run('/tmp/hist/data/flow_messages_all.csv','/tmp/hist/data/flows_feat.csv','flow')
