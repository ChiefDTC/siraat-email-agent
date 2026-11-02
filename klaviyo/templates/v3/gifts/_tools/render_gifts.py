"""Gifts: build (build_template) + previews + checks. Gebruik (vanuit /tmp): python3 -I render_gifts.py
Schrijft <id>.klaviyo.html en <id>-preview.html naast de bron. Beelden staan nog NIET in Klaviyo: de Klaviyo-versie gebruikt
voor de gift-beelden placeholder-URL's (https://upload-pending.invalid/gifts/<bestand>), uit _tools/pending-urls.txt; fb/ig zijn echt.
In de preview wordt de cookbook-placeholder {{COOKBOOK_URL}} '#'. Screenshots daarna met shot_gifts.js."""
import sys,os,subprocess,re
sys.path.insert(0,'/home/user/siraat-email-agent/scripts'); import qa_render as Q
N='/home/user/siraat-email-agent/klaviyo/templates/v3/gifts'; ad=os.path.join(N,'assets'); T=os.path.join(N,'_tools')
real=dict(l.split() for l in open(os.path.join(ad,'klaviyo-urls.txt')) if l.strip())
pu=os.path.join(T,'pending-urls.txt')
open(pu,'w').write(''.join('%s %s\n'%(n,real.get(n,'https://upload-pending.invalid/gifts/'+n)) for n in sorted(os.listdir(ad)) if re.search(r'\.(png|jpe?g)$',n)))
for mid in ('gifts-a','gifts-a-alt','gifts-b','gifts-c'):
    src=os.path.join(N,mid+'.html')
    r=subprocess.run([sys.executable,'-I',Q.BT,src,ad,pu],capture_output=True,text=True,cwd='/tmp')
    if r.returncode: print(mid,'BUILD',r.stderr[-500:],r.stdout[-300:]); continue
    k=open(os.path.join(N,mid+'.klaviyo.html')).read()
    c=Q.context('none'); c['person']['Country']='United States'
    h=Q.engine().from_string(k).render(c)
    probs=Q.after_render(h)+Q.foster(h)
    pv=os.path.join(N,mid+'-preview.html'); p=open(pv).read().replace('{{COOKBOOK_URL}}','#'); open(pv,'w').write(p)
    vis=re.sub(r'<style.*?</style>|<!--.*?-->','',p,flags=re.S)
    print(mid,'| django:',probs[:3] or 'ok','| emdash:%d'%(k.count('—')+k.count('&mdash;')),'| lockup:%s'%('68a06000-e2d3-4858-86cb-92587411d958' in k),
          '| footer:%s'%('unsubscribe_link' in k),'| placeholder in klaviyo:%s'%('{{COOKBOOK_URL}}' in k),
          '| preview restanten:%s'%(re.findall(r'\{\{.*?\}\}|\{%.*?%\}',vis)[:3] or 'geen'),'| ebook-links:%d'%k.count('6d8678add81ad2ad'),'| KB %.0f'%(len(k.encode())/1024))
