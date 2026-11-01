"""Roasting INT: build (build_template) + Django-render per INT-land + checks. Gebruik: python3 -I render_roast.py <uitmap>
Schrijft <uitmap>/<id>-<land>.html; screenshots daarna met shot_roast.js. Afgeleid van bfcm/november-v2/_tools/render_v2.py."""
import sys,os,subprocess,re
sys.path.insert(0,'/home/user/siraat-email-agent/scripts'); import qa_render as Q
N='/home/user/siraat-email-agent/klaviyo/templates/v3/campaigns/roasting-int'; OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
ad=os.path.join(N,'assets'); tu=os.path.join(OUT,'u.txt'); ts=os.path.join(OUT,'s.txt')
open(tu,'w').write(''.join('%s file://%s\n'%(n,os.path.join(ad,n)) for n in sorted(os.listdir(ad)) if os.path.isfile(os.path.join(ad,n))))
open(ts,'w').write(''.join('%s file://%s\n'%(n,os.path.join(Q.SH,n)) for n in sorted(os.listdir(Q.SH)) if os.path.isfile(os.path.join(Q.SH,n))))
LANDS=(('de','Germany'),('uk','United Kingdom'),('au','Australia'),('ca','Canada'),('ch','Switzerland'),('us','United States'))
ids=sorted(f[:-5] for f in os.listdir(N) if f.startswith('roast-int-') and f.endswith('.html') and not f.endswith(('-preview.html','.klaviyo.html')))
for mid in ids:
    src=os.path.join(N,mid+'.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,os.path.join(ad,'klaviyo-urls.txt')],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'BUILD',r.stderr[-500:],r.stdout[-300:]); continue
    raw=os.path.join(OUT,mid+'.raw.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,tu,'--out='+raw,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'RAW',r.stderr[-500:]); continue
    k=open(raw).read(); F,W,_=Q.tags_filters(k)
    for tag,country in LANDS:
        c=Q.context('none'); c['person']['Country']=country
        h=Q.engine().from_string(k).render(c)
        probs=Q.after_render(h)+Q.foster(h)
        open(os.path.join(OUT,'%s-%s.html'%(mid,tag)),'w').write(h)
        txt=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<style.*?</style>|<!--.*?-->','',h,flags=re.S)))
        pr=re.findall(r'[€£$]\s?[\d,.]+|[A-Z]{1,2}\$\s?[\d,.]+',txt)
        print(mid,tag,'tagsF:%d'%len(F),probs[:3] or 'ok','| emdash:%d'%h.count('—'),'| lockup:%s'%('logo-black-cream' in h),'| footer:%s'%('unsubscribe' in h.lower()),
              '| fromUS:%d'%len(re.findall(r'(?i)from the US',txt)),'| prices:%s'%sorted(set(pr)),'| KB %.0f'%(len(h.encode())/1024))
