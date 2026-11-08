"""Tegoed 8 nov: build (build_template: .klaviyo.html met CDN-links) + Django-render met voorbeeldprofiel + checks.
Gebruik (vanuit /tmp): python3 -I render_tegoed.py <uitmap>; daarna node shot_tegoed.js <uitmap> <previewmap>."""
import sys,os,subprocess,re
sys.path.insert(0,'/home/user/siraat-email-agent/scripts'); import qa_render as Q
N='/home/user/siraat-email-agent/klaviyo/templates/v3/tegoed'; SH=Q.SH; AD='/home/user/siraat-email-agent/klaviyo/templates/partials/assets'
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
ts=os.path.join(OUT,'s.txt'); tu=os.path.join(OUT,'u.txt')
open(tu,'w').write(''.join('%s file://%s\n'%(n,os.path.join(AD,n)) for n in sorted(os.listdir(AD)) if os.path.isfile(os.path.join(AD,n))))
open(ts,'w').write(''.join('%s file://%s\n'%(n,os.path.join(SH,n)) for n in sorted(os.listdir(SH)) if os.path.isfile(os.path.join(SH,n))))
for mid in ('t1','t2','t3','t4'):
    src=os.path.join(N,mid+'.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,AD,os.path.join(AD,'klaviyo-urls.txt'),'--shared-urls='+os.path.join(SH,'klaviyo-urls.txt'),'--no-preview'],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'BUILD',r.stderr[-500:],r.stdout[-300:]); continue
    raw=os.path.join(OUT,mid+'.raw.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,AD,tu,'--out='+raw,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'RAW',r.stderr[-500:]); continue
    k=open(raw).read()
    c=Q.context('none'); c['email']='you@example.com'
    c['person'].update({'Country':'United States','siraat_credit_code':'SRT-K7Q2M','siraat_credit_value':12,'siraat_credit_expires_at':'2026-12-08T02:00:00'})
    h=Q.engine().from_string(k).render(c)
    probs=Q.after_render(h)+Q.foster(h)
    open(os.path.join(OUT,mid+'.html'),'w').write(h)
    kv=open(os.path.join(N,mid+'.klaviyo.html')).read()
    print(mid,probs[:3] or 'ok','| emdash:%d'%(kv.count('—')+kv.count('–')),'| header:%s'%('logo-black-cream' in kv or '68a06000' in kv),
          '| footer-unsub:%s'%('unsubscribe' in kv.lower()),'| coupon-tags:%d'%kv.count('coupon_code'),'| yellow:%d'%kv.upper().count('FFB800'),'| KB %.0f'%(len(kv.encode())/1024))
