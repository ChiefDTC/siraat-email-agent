"""Siraat e-mail hero: foto + kop (TT Ramillas) + subregel, altijd exact gecentreerd.
Gebruik: python3 -I scripts/make_hero.py <foto> <uit.jpg> "<kopregel 1|kopregel 2>" "<subregel>" ["<LABEL>"]
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
src,out,head,sub=sys.argv[1:5]; label=sys.argv[5] if len(sys.argv)>5 else ''
S=1200
im=Image.open(src).convert('RGB'); w,h=im.size; m=min(w,h)
im=im.crop(((w-m)//2,(h-m)//2,(w-m)//2+m,(h-m)//2+m)).resize((S,S),Image.LANCZOS)
# overall darken + soft centre darkening for contrast
dark=Image.new('RGB',(S,S),(18,13,11)); im=Image.blend(im,dark,0.30)
mask=Image.new('L',(S,S),0); md=ImageDraw.Draw(mask); md.ellipse((80,330,S-80,S-330),fill=150); mask=mask.filter(ImageFilter.GaussianBlur(140))
im=Image.composite(dark,im,mask)
d=ImageDraw.Draw(im)
fh=ImageFont.truetype(TT,132); fs=ImageFont.truetype(INTERM,38)
lines=head.split('|'); lh=138; gap=52
sub_h=46 if sub else 0
block=len(lines)*lh+(gap+sub_h if sub else 0)
y=(S-block)//2 - 8
for ln in lines:
    tw=d.textlength(ln,font=fh); d.text(((S-tw)/2,y),ln,font=fh,fill=(255,255,255)); y+=lh
if sub:
    y+=gap; tw=d.textlength(sub,font=fs); d.text(((S-tw)/2,y),sub,font=fs,fill=(240,236,228))
if label:
    fl=ImageFont.truetype(INTERS,26); tw=d.textlength(label,font=fl)
    x0=(S-tw-56)/2; y0=56
    d.rounded_rectangle((x0,y0,x0+tw+56,y0+62),radius=31,fill=(172,59,25)); d.text((x0+28,y0+15),label,font=fl,fill=(255,255,255))
im.save(out,quality=84); print(out)
