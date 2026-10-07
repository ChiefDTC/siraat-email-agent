import csv,statistics as st,sys
from collections import defaultdict
kind=sys.argv[1]
if kind=='camp':
    r=[x for x in csv.DictReader(open('/tmp/hist/data/campaigns_feat.csv')) if int(x['recipients'])>=1000 and x['rpr_index_month']]
    I,C='rpr_index_month','click_index_month'
else:
    r=[x for x in csv.DictReader(open('/tmp/hist/data/flows_feat.csv')) if int(x['recipients'])>=1000 and x['rpr_index_cat']]
    I,C='rpr_index_cat','click_index_cat'
out=[]
def grp(key,label):
    g=defaultdict(list)
    for x in r: g[key(x)].append(x)
    print('--',label)
    for k,v in sorted(g.items(),key=lambda kv:str(kv[0])):
        d=sum(int(x['delivered']) for x in v); rev=sum(float(x['revenue']) for x in v)
        cl=sum(float(x['click_rate'])*int(x['delivered']) for x in v)/d; un=sum(int(x['unsubs']) for x in v)/d
        row=dict(feature=label,value=k,n=len(v),delivered=d,rpr_weighted=round(rev/d,3),median_rpr_index=round(st.median(float(x[I]) for x in v),2),median_click_index=round(st.median(float(x[C]) for x in v),2),click_weighted=round(cl,4),unsub_weighted=round(un,4))
        out.append(row)
        print(f"{str(k):22} n={len(v):3} RPR(w)={rev/d:.3f} medRPRidx={row['median_rpr_index']:.2f} medClickIdx={row['median_click_index']:.2f} click(w)={cl*100:.2f}% unsub={un*100:.2f}%")
grp(lambda x:x.get('format'),'format')
for f in ['s_question','s_number','s_discount','s_gift','s_urgency','s_socialproof','s_pfas','s_emoji','s_personal','s_founder','s_howto','s_launch','s_curiosity','o_code','o_gift','o_freeship']:
    grp(lambda x:x[f],f)
grp(lambda x:('0' if x['o_maxpct'] in('0','') else ('<=20' if int(x['o_maxpct'])<=20 else ('21-49' if int(x['o_maxpct'])<50 else '50+'))),'pct_off')
grp(lambda x:x.get('main_product'),'main_product')
grp(lambda x:min(int(x['s_len_words'])//3*3,12),'subj_words_bucket')
grp(lambda x:('none' if not x['preview'].strip() else 'yes'),'has_preview')
grp(lambda x:x.get('from_label'),'from_label')
if kind=='camp':
    grp(lambda x:x['bfcm'],'bfcm')
    grp(lambda x:('engaged30' if '30' in x['audience'] else 'engaged60-90' if ('90' in x['audience'] or '60' in x['audience']) else 'engaged120-180+' if ('120' in x['audience'] or '180' in x['audience'] or '365' in x['audience']) else 'buyers' if ('buyer' in x['audience'].lower() or 'order' in x['audience'].lower()) else 'other'),'audience')
else:
    grp(lambda x:x['category'],'category')
with open(f'/tmp/hist/data/patterns_{kind}.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
