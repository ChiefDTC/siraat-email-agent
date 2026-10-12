"""Korte hero voor de reviewmail (flow XzHrez, research/v6-golive/19-review-hero.md, 12 okt 2026).
Gebruik: python3 -I scripts/make_review_hero.py [uit.jpg]
Bron: klaviyo/figma/ai/review-hero-dark-1200.jpg (zelfde flitsfoto als de live hero, al donker, zonder tekst).
Uitsnede 1200x1020 (y 50..1070): beide gezichten en de pan blijven in beeld; op 375 px is de hero 319 px hoog (was 375 plus 8 px rand, kop en subregel erin).
In het beeld alleen eyebrow en kop (TT Ramillas). Logo staat in de vaste header, de subregel staat als live tekst onder het beeld."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R='/home/user/siraat-email-agent/'
SRC=R+'klaviyo/figma/ai/review-hero-dark-1200.jpg'
OUT=sys.argv[1] if len(sys.argv)>1 else R+'klaviyo/templates/v3/review/assets/review-hero-short.jpg'
TT=R+'klaviyo/fonts/TTRamillas-LightItalic.ttf'
INTERS='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
W,H,Y0=1200,1020,50
im=Image.open(SRC).convert('RGB').crop((0,Y0,W,Y0+H))
# zachte donkere vlek achter de tekst (zelfde aanpak als make_hero.py), gezichten en pan blijven helder
dark=Image.new('RGB',(W,H),(18,13,11))
mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).ellipse((90,370,W-90,810),fill=150)
im=Image.composite(dark,im,mask.filter(ImageFilter.GaussianBlur(120)))
d=ImageDraw.Draw(im)
fe=ImageFont.truetype(INTERS,38); fh=ImageFont.truetype(TT,132)
eyebrow='THANK YOU FOR YOUR ORDER'; sp=9
ew=sum(d.textlength(c,font=fe) for c in eyebrow)+sp*(len(eyebrow)-1)
lines=['Win your purchase','amount back']; lh=140
block=48+40+len(lines)*lh
y=595-block//2
x=(W-ew)/2
for c in eyebrow:
    d.text((x,y),c,font=fe,fill=(214,208,198)); x+=d.textlength(c,font=fe)+sp
y+=48+40
for ln in lines:
    tw=d.textlength(ln,font=fh); d.text(((W-tw)/2,y),ln,font=fh,fill=(255,255,255)); y+=lh
im.save(OUT,quality=80,optimize=True,progressive=True); print(OUT)
