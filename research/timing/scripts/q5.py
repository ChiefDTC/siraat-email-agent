from load import *
import re
from urllib.parse import urlparse, parse_qs
cl=load('clicks.jsonl',('$flow','$message','Bot Click','URL','Campaign Name'))
cl=cl[(cl['Bot Click']!=True)&cl['$flow'].notna()&(cl.ts>=pd.Timestamp('2026-07-09',tz='UTC'))]
def norm(u):
    if not isinstance(u,str): return 'geen'
    p=urlparse(u); path=p.path.rstrip('/')
    q=parse_qs(p.query)
    h=p.netloc.replace('www.','')
    if 'checkouts' in path or 'recover' in path: return 'checkout-herstel'
    if '/cart' in path: return 'cart'
    if 'unsubscribe' in u or 'manage_preferences' in u or 'klaviyo.com/p' in u: return 'uitschrijven/voorkeuren'
    if any(s in h for s in ['instagram','facebook','tiktok','youtube','pinterest','x.com','twitter']): return 'social'
    if 'trustpilot' in h or 'review' in path: return 'reviews'
    if 'parcelpanel' in path or 'track' in path: return 'tracking'
    if '/products/' in path: return 'product:'+path.split('/products/')[1][:40]
    if '/collections/' in path: return 'collectie:'+path.split('/collections/')[1][:30]
    if path in ('','/'): return 'homepage'
    if '/pages/' in path: return 'pagina:'+path.split('/pages/')[1][:30]
    if '/discount/' in path: return 'discount-link'
    return h+path[:40]
cl['dest']=cl.URL.map(norm)
fc=cl.drop_duplicates(['pid','$message','dest'])
mm=pd.read_csv('/home/user/siraat-email-agent/baselines/flow-messages-90d.csv')
name=dict(zip(mm.flow_message_id,mm.flow_id+' '+mm.message_name))
deliv=dict(zip(mm.flow_message_id,mm.delivered))
rows=[]
for msg,s in fc.groupby('$message'):
    if msg not in name: continue
    vc=s.dest.map(lambda d: d.split(':')[0]).value_counts()
    tot=len(s)
    top=s.dest.value_counts().head(4)
    rows.append({'msg':msg,'naam':name[msg][:55],'klikken (uniek pid x bestemming)':tot,'delivered90':deliv[msg],
        **{k:round(v/tot*100) for k,v in vc.head(6).items()},'top':'; '.join(f'{k} {round(v/tot*100)}%' for k,v in top.items())})
R=pd.DataFrame(rows).sort_values('naam')
pd.set_option('display.width',400); pd.set_option('display.max_colwidth',140)
print(R[['naam','klikken (uniek pid x bestemming)','top']].to_string(index=False))
R.to_csv('q5_urls.csv',index=False)
# UTM presence
print('UTM aanwezig in klik-URL:',round(cl.URL.str.contains('utm_',na=False).mean()*100,1),'%; utm_content aanwezig', round(cl.URL.str.contains('utm_content',na=False).mean()*100,1))
print(cl.URL.dropna().sample(5,random_state=1).tolist())
