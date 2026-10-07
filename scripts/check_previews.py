"""Controleert alle -preview.html in klaviyo/templates/v3: ontbrekende lokale beelden, restanten en verboden woorden.
Gebruik: python3 -I scripts/check_previews.py [flowmap ...]"""
import sys,os,re,glob
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','klaviyo','templates','v3')
flows=sys.argv[1:] or sorted(os.listdir(R))
BAD=['—','[[','{{BLOCK','purifier','lifetime','100-day','independent','free returns','Free returns','handle stays cool','scratch-proof','naturally non-stick']
n=0
for f in flows:
    for p in sorted(glob.glob(os.path.join(R,f,'*-preview*.html'))):
        h=open(p).read(); d=os.path.dirname(p)
        miss=[s for s in set(re.findall(r'src="([^"{}]+)"',h)) if not s.startswith('http') and not os.path.exists(os.path.join(d,s.split('?')[0]))]
        bad=[b for b in BAD if b in h]
        if miss or bad: n+=1; print(os.path.relpath(p,R),'MIST',miss[:3],'WOORD',bad)
print('problemen:',n)
