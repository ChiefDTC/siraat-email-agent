"""Maakt de data voor een Figma-update van een flow: onderwerp, preview en hoogte van de desktop-preview per mail.
Gebruik: python3 -I scripts/figma_update_data.py <flowmap> <id1,id2,...>   (print JSON)"""
import sys,re,json
from PIL import Image
F,ids=sys.argv[1],sys.argv[2].split(',')
out={}
for i in ids:
    s=open(f'{F}/{i}.html').read(); m=re.search(r'<!--(.*?)-->',s,re.S).group(1)
    d={k.strip():v.strip() for k,v in (p.split(':',1) for p in m.split(' | ') if ':' in p)}
    w,h=Image.open(f'{F}/previews/{i}-desktop.png').size
    out[i]={'a':d.get('SUBJECT_A',''),'b':d.get('SUBJECT_B',''),'p':d.get('PREVIEW',''),'h':round(360*h/w)}
print(json.dumps(out))
