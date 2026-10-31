"""BF signup: bouwt (build_template) en rendert de Klaviyo-versie met Django voor person.Country United States, Germany en leeg (onbekend = niet-US). Gebruik: python3 render_bf.py <uitmap> bf-w1,bf-w2  ; daarna node shot375.js <uitmap>/<mail>-us.html previews/<mail>-us-375.png"""
import sys,os,subprocess
sys.path.insert(0,'/home/user/siraat-email-agent/scripts'); import qa_render as Q
S='/home/user/siraat-email-agent/klaviyo/templates/v3/bfcm/signup'; OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
ad=os.path.join(S,'assets')
tu=os.path.join(OUT,'u.txt'); ts=os.path.join(OUT,'s.txt')
open(tu,'w').write(''.join('%s file://%s\n'%(n,os.path.join(ad,n)) for n in sorted(os.listdir(ad)) if os.path.isfile(os.path.join(ad,n))))
open(ts,'w').write(''.join('%s file://%s\n'%(n,os.path.join(Q.SH,n)) for n in sorted(os.listdir(Q.SH)) if os.path.isfile(os.path.join(Q.SH,n))))
for mid in sys.argv[2].split(','):
    src=os.path.join(S,mid+'.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,os.path.join(ad,'klaviyo-urls.txt')],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'BUILD',r.stderr[-400:],r.stdout[-200:]); continue
    raw=os.path.join(OUT,mid+'.raw.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,tu,'--out='+raw,'--shared-urls='+ts,'--no-preview'],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'RAW',r.stderr[-400:]); continue
    k=open(raw).read(); F,W,_=Q.tags_filters(k)
    for tag,country in (('us','United States'),('int','Germany'),('unk',None)):
        person={'Country':country} if country else {}
        h=Q.engine().from_string(k).render({'event':{},'first_name':'Sarah','person':person,'organization':{'name':"Siraat's Kitchen",'full_address':'[address]'}})
        probs=Q.after_render(h)+Q.foster(h)
        open(os.path.join(OUT,'%s-%s.html'%(mid,tag)),'w').write(h)
        names=[n for n in ('Pan Pro Standard','Cookware Set, 12&nbsp;Pcs','Pan Set with Lids, 6&nbsp;Pcs','Deep Pan Pro','Wok Pan Pro') if '>'+n+'<' in h]
        print(mid,tag,'F:%d'%len(F),probs[:3] or 'ok','|',', '.join(names),'| emdash' if '—' in h else '','| KB %.0f'%(len(h.encode())/1024))
