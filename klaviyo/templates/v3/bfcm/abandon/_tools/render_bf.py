"""Django-render van de BF-varianten met de qa_render-contexten (eerste variant per flow) + checks; schrijft gerenderde HTML."""
import sys,os,re,subprocess,glob
sys.path.insert(0,'/home/user/siraat-email-agent/scripts'); import qa_render as Q
A='/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/abandon'; OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
FL={'c':'checkout','k':'cart','b':'browse','a':'site','t':'browse'}
ad=os.path.join(A,'assets'); tu=os.path.join(OUT,'u.txt'); ts=os.path.join(OUT,'s.txt')
open(tu,'w').write(''.join('%s file://%s\n'%(n,os.path.join(ad,n)) for n in sorted(os.listdir(ad)) if os.path.isfile(os.path.join(ad,n))))
open(ts,'w').write(''.join('%s file://%s\n'%(n,os.path.join(Q.SH,n)) for n in sorted(os.listdir(Q.SH)) if os.path.isfile(os.path.join(Q.SH,n))))
only=sys.argv[2].split(',') if len(sys.argv)>2 else None
for src in sorted(glob.glob(A+'/*-bf.html')):
    mid=os.path.basename(src)[:-8]
    if only and mid not in only: continue
    flow=FL[mid[0]]; raw=os.path.join(OUT,mid+'.raw.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,tu,'--out='+raw,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True)
    if r.returncode: print(mid,'BUILD',r.stderr[-300:]); continue
    k=open(raw).read(); F,W,used=Q.tags_filters(k)
    for i,(var,label) in enumerate(Q.VARIANTS[flow]):
        try: h=Q.engine().from_string(k).render(Q.context(var))
        except Exception as ex: print(mid,var,'RENDER FAIL',str(ex)[:200]); continue
        probs=Q.after_render(h)+Q.foster(h)
        if i==0: open(os.path.join(OUT,mid+'.html'),'w').write(h)
        print(mid,var,'tags-F:%d'%len(F),'problemen:',probs[:4] if probs else 'ok', 'HI10' if 'HI10' in h else '', 'BFCODE:%d'%h.count('BFCODE'))
