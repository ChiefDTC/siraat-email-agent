"""Uploadt beelden uit een map naar de Klaviyo-beeldbibliotheek en schrijft 'bestand url' in <map>/klaviyo-urls.txt.
Slaat bestanden over die er al in staan. Naam in Klaviyo: siraat-<map>-<bestand>.
Gebruik: python3 -I scripts/upload_images.py <map> [prefix]"""
import sys,os,json,subprocess
d=sys.argv[1]; pre=sys.argv[2] if len(sys.argv)>2 else os.path.basename(os.path.abspath(d))
u=os.path.join(d,'klaviyo-urls.txt')
have=dict(l.split() for l in open(u) if l.strip()) if os.path.exists(u) else {}
ok=0
for f in sorted(os.listdir(d)):
    if f in have or not f.lower().endswith(('.png','.jpg','.jpeg','.gif')): continue
    r=subprocess.run(['curl','-sS','-X','POST','https://a.klaviyo.com/api/image-upload','-H','revision: 2025-10-15','-H','accept: application/vnd.api+json',
        '-F','file=@'+os.path.join(d,f),'-F','name=siraat-%s-%s'%(pre,f)],capture_output=True,text=True)
    try: url=json.loads(r.stdout)['data']['attributes']['image_url']
    except Exception: print('FOUT',f,r.stdout[:200]); continue
    have[f]=url; ok+=1
    open(u,'a').write('%s %s\n'%(f,url))
print('geupload',ok,'totaal',len(have))
