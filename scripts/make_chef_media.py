"""Scherpe (2x) GIF's en stills voor P2, P2-safe en W0 uit de chef-video (care and use, 1080p).
Bron: https://cdn.shopify.com/videos/c/o/v/59e8423c235b4e71a38a64910b48faac.mp4 (brand/proof/README.md). Lokaal downloaden, nooit in de repo.
Gebruik: python3 -I scripts/make_chef_media.py <video.mp4> [--gifsicle=/pad/naar/gifsicle] [--only=naam,naam]
- Uitsnede: de bovenste 1920x840 van het beeld (onder y=840 staan de ingebrande ondertitels), zelfde uitsnede als de oude 480x210-versies.
- Tijden en frames gemeten tegen de oude bestanden (7 okt 2026). 3,5 fps zoals de QA-patch (elke tweede frame weg).
- Gewicht: GIF < 1 MB, W0 (twee GIF's) samen < 1,2 MB. Zonder gifsicle (--lossy) worden de GIF's te zwaar: dan stopt het script.
  gifsicle staat niet op het systeem; in de sessie van 7 okt via `npm install gifsicle@7.0.1` in de scratchpad (vendor/gifsicle).
"""
import sys,os,subprocess,tempfile
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','klaviyo','templates','v3')
opts={a.split('=',1)[0]:a.split('=',1)[1] for a in sys.argv[1:] if a.startswith('--')}
pos=[a for a in sys.argv[1:] if not a.startswith('--')]
video=pos[0]; G=opts.get('--gifsicle')
CROP='crop=1920:840:0:0'
# naam: (doel, soort, start s, duur s, breedte, kleuren, lossy)
JOBS={
 'p2-egg':   ('post-purchase/assets/egg-slide-lite.gif','gif',74.03,3.95,840,128,100),
 'w0-egg':   ('welcome/assets/gif-egg-slide.gif','gif',74.03,3.95,960,128,110),
 'w0-water': ('welcome/assets/gif-water-test.gif','gif',43.20,2.40,960,128,100),
 'p2-oil':   ('post-purchase/assets/oil-shimmer-still.jpg','jpg',54.77,0,960,0,0),
 'p2-water': ('post-purchase/assets/water-test-still.jpg','jpg',43.77,0,960,0,0),
}
only=opts.get('--only','').split(',') if opts.get('--only') else list(JOBS)
for k in only:
    out,kind,t0,dur,w,cols,lossy=JOBS[k]; out=os.path.join(R,out)
    if kind=='jpg':
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t0),'-i',video,'-frames:v','1','-vf',CROP+',scale=%d:-1:flags=lanczos'%w,'-q:v','3',out],check=True)
    else:
        if not G: sys.exit('gifsicle nodig voor %s (--gifsicle=...)'%k)
        tmp=tempfile.mktemp(suffix='.gif')
        vf=CROP+',hqdn3d=4:3:6:6,fps=3.5,scale=%d:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=%d:stats_mode=diff[p];[b][p]paletteuse=dither=none:diff_mode=rectangle'%(w,cols)
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t0),'-t',str(dur),'-i',video,'-vf',vf,'-loop','0',tmp],check=True)
        subprocess.run([G,'-O3','--lossy=%d'%lossy,tmp,'-o',out],check=True,stderr=subprocess.DEVNULL); os.remove(tmp)
    print(k,os.path.relpath(out,R),os.path.getsize(out)//1024,'KB')
