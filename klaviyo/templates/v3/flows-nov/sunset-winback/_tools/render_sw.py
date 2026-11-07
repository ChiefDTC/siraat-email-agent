"""Sunset/winback BF 7 nov: build (build_template, schrijft .klaviyo.html en -preview.html) + Django-render per markt + checks.
Gebruik (vanuit /tmp): python3 -I render_sw.py <uitmap>. Beide renderen op profielland (segment-triggers, geen event)."""
import sys,os,subprocess,re,copy
sys.path.insert(0,'/home/user/siraat-email-agent/scripts'); import qa_render as Q
N='/home/user/siraat-email-agent/klaviyo/templates/v3/flows-nov/sunset-winback'; AD='/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/november-v2/assets'
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
tu=os.path.join(OUT,'u.txt'); ts=os.path.join(OUT,'s.txt')
open(tu,'w').write(''.join('%s file://%s\n'%(n,os.path.join(AD,n)) for n in sorted(os.listdir(AD)) if os.path.isfile(os.path.join(AD,n))))
open(ts,'w').write(''.join('%s file://%s\n'%(n,os.path.join(Q.SH,n)) for n in sorted(os.listdir(Q.SH)) if os.path.isfile(os.path.join(Q.SH,n))))
CASES={'sbf-us':[('us','none',None,'United States')],'sbf-int':[('int','none',None,'Germany'),('au','none',None,'Australia')],
       'wbf-us':[('us','none',None,'United States')],'wbf-int':[('int','none',None,'Germany'),('au','none',None,'Australia')]}
for mid,cases in CASES.items():
    src=os.path.join(N,mid+'.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,AD,os.path.join(AD,'klaviyo-urls.txt')],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'BUILD',r.stderr[-500:],r.stdout[-300:]); continue
    raw=os.path.join(OUT,mid+'.raw.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,AD,tu,'--out='+raw,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'RAW',r.stderr[-500:]); continue
    k=open(raw).read(); F,W,_=Q.tags_filters(k)
    for tag,sample,ship,country in cases:
        c=Q.context(sample)
        if ship: c['event']=copy.deepcopy(c['event']); c['event'].setdefault('extra',{}).setdefault('shipping_address',{})['country_code']=ship
        if country: c['person']['Country']=country
        h=Q.engine().from_string(k).render(c)
        probs=Q.after_render(h)+Q.foster(h)
        open(os.path.join(OUT,'%s-%s.html'%(mid,tag)),'w').write(h)
        txt=re.sub(r'<[^>]+>',' ',re.sub(r'<style.*?</style>|<!--.*?-->','',h,flags=re.S))
        print(mid,tag,'tagsF:%d'%len(F),probs[:3] or 'ok','| emdash:%d'%(h.count('\u2014')+h.count('\u2013')),'| lockup:%s'%('logo-black-cream' in h or 'logo-white' in h or 'lockup' in h),
              '| footer:%s'%('unsubscribe' in h.lower()),'| fric:%s'%re.search(r'Free shipping[^.]*\.',txt).group(0),'| usd:%d'%txt.count('$'),'| KB %.0f'%(len(h.encode())/1024))
