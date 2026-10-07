"""Siraat e-mail hero: foto + kop (TT Ramillas) + subregel, altijd exact gecentreerd.
Gebruik: python3 -I scripts/make_hero.py <foto> <uit.jpg> "<kopregel 1|kopregel 2>" "<subregel>" ["<LABEL>"] [--offer="10% OFF WITH HI10 · $70 IN GIFTS"] [--ratio=4:3]
- --offer: brick-balk onderaan het beeld met het aanbod (verplicht in elke verkoopmail, PLAYBOOK 10).
- --ratio=4:3: 1200x900 voor checkout, cart en browse, zodat de cart boven de vouw past.
- Kop en subregel staan als blok precies in het midden van het beeld (horizontaal en verticaal).
- Gelijkmatige donkere laag plus een zachte vignet in het midden, zodat de tekst op elke foto leesbaar is.
- 1200x1200 (vierkant), uitsnede uit het midden van de foto.
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R='/home/user/siraat-email-agent/'
TT=R+'klaviyo/fonts/TTRamillas-LightItalic.ttf'
INTERM='/usr/share/fonts/opentype/inter/Inter-Medium.otf'
INTERS='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
opts={a.split('=',1)[0]:a.split('=',1)[1] for a in sys.argv[1:] if a.startswith('--')}
pos=[a for a in sys.argv[1:] if not a.startswith('--')]
src,out,head,sub=pos[:4]; label=pos[4] if len(pos)>4 else ''
offer=opts.get('--offer',''); W=1200; H=900 if opts.get('--ratio')=='4:3' else 1200
BAR=150 if offer else 0
S=W
im=Image.open(src).convert('RGB'); w,h=im.size
r=W/H
if w/h>r: nw=int(h*r); im=im.crop(((w-nw)//2,0,(w-nw)//2+nw,h))
else: nh=int(w/r); im=im.crop((0,(h-nh)//2,w,(h-nh)//2+nh))
im=im.resize((W,H),Image.LANCZOS)
# overall darken + soft centre darkening for contrast
dark=Image.new('RGB',(W,H),(18,13,11)); im=Image.blend(im,dark,0.38)
CH=H-BAR  # tekstvlak boven de aanbodbalk
mask=Image.new('L',(W,H),0); md=ImageDraw.Draw(mask); md.ellipse((80,CH*0.27,W-80,CH*0.73),fill=175); mask=mask.filter(ImageFilter.GaussianBlur(140))
im=Image.composite(dark,im,mask)
d=ImageDraw.Draw(im)
fh=ImageFont.truetype(TT,132 if H==1200 else 120); fs=ImageFont.truetype(INTERS,48)
lines=head.split('|'); lh=138; gap=52
sub_h=58 if sub else 0
block=len(lines)*lh+(gap+sub_h if sub else 0)
y=(CH-block)//2 + (30 if label else -8)
for ln in lines:
    tw=d.textlength(ln,font=fh); d.text(((W-tw)/2,y),ln,font=fh,fill=(255,255,255)); y+=lh
if sub:
    y+=gap; tw=d.textlength(sub,font=fs); d.text(((W-tw)/2,y),sub,font=fs,fill=(240,236,228))
if label:
    fl=ImageFont.truetype(INTERS,40); tw=d.textlength(label,font=fl)
    x0=(W-tw-72)/2; y0=52
    d.rounded_rectangle((x0,y0,x0+tw+72,y0+84),radius=42,fill=(172,59,25)); d.text((x0+36,y0+19),label,font=fl,fill=(255,255,255))
if offer:
    d.rectangle((0,H-BAR,W,H),fill=(172,59,25))
    fo=ImageFont.truetype(INTERS,46); 
    while d.textlength(offer,font=fo)>W-90: fo=ImageFont.truetype(INTERS,fo.size-2)
    tw=d.textlength(offer,font=fo); d.text(((W-tw)/2,H-BAR+(BAR-fo.size)/2-6),offer,font=fo,fill=(255,255,255))
im.save(out,quality=84); print(out)
