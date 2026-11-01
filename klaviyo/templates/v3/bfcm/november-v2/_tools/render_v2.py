"""November v2: build (build_template) + Django-render per markt + checks. Gebruik: python3 -I render_nov.py <uitmap> [id,id]
Schrijft <uitmap>/<id>-<us|int>.html; screenshots daarna met shot_nov.js."""
import sys,os,subprocess,re
sys.path.insert(0,'/home/user/siraat-email-agent/scripts'); import qa_render as Q
N='/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/november-v2'; OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
ad=os.path.join(N,'assets'); tu=os.path.join(OUT,'u.txt'); ts=os.path.join(OUT,'s.txt')
open(tu,'w').write(''.join('%s file://%s\n'%(n,os.path.join(ad,n)) for n in sorted(os.listdir(ad)) if os.path.isfile(os.path.join(ad,n))))
open(ts,'w').write(''.join('%s file://%s\n'%(n,os.path.join(Q.SH,n)) for n in sorted(os.listdir(Q.SH)) if os.path.isfile(os.path.join(Q.SH,n))))
CO=(('us','co_set6',None),('int','co_pan_eur','Germany')); CTX={k:CO for k in ('v2-c1b','v2-c1c','v2-c2b','v2-c2c')}; CTX['v2-k1b']=(('us','atc_x_set6',None),('int','atc_lid_eur','Germany'))
TOK='XXNEXTBATCHXX'; HLB='<span style="background-color:#FFE38A;color:#272727;padding:0 3px;">[NEXT BATCH DATE]</span>'
ids=sys.argv[2].split(',') if len(sys.argv)>2 else sorted(f[:-5] for f in os.listdir(N) if f.startswith('v2-') and f.endswith('.html') and not f.endswith(('-preview.html','.klaviyo.html')))
for mid in ids:
    src=os.path.join(N,mid+'.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,os.path.join(ad,'klaviyo-urls.txt')],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'BUILD',r.stderr[-500:],r.stdout[-300:]); continue
    raw=os.path.join(OUT,mid+'.raw.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,tu,'--out='+raw,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'RAW',r.stderr[-500:]); continue
    k=open(raw).read(); F,W,_=Q.tags_filters(k)
    for tag,sample,country in CTX.get(mid,(('us',None,'United States'),('int',None,'Germany'))):
        c=Q.context(sample) if sample else Q.context('none')
        if country: c['person']['Country']=country
        c['NEXT_BATCH_DATE']=TOK
        h=Q.engine().from_string(k).render(c).replace(TOK,HLB)
        probs=Q.after_render(h)+Q.foster(h)
        open(os.path.join(OUT,'%s-%s.html'%(mid,tag)),'w').write(h)
        txt=re.sub(r'<[^>]+>',' ',re.sub(r'<style.*?</style>|<!--.*?-->','',h,flags=re.S))
        print(mid,tag,'tagsF:%d'%len(F),probs[:3] or 'ok','| emdash:%d'%h.count('—'),'| lockup:%s'%('logo-black-cream' in h or 'logo-white' in h),'| footer:%s'%('unsubscribe' in h.lower()),'| BFCODE:%d'%h.count('BFCODE'),'| batchwords:%d'%len(re.findall(r'(?i)next batch|reserve|arriving',txt)),'| 12Pcs:%s'%('12 Pcs' in h or '12&nbsp;Pcs' in h),'| KB %.0f'%(len(h.encode())/1024))
