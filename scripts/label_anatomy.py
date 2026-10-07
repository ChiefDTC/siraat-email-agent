import sys
from PIL import Image, ImageDraw, ImageFont
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB'); S=im.width/1024
# crop to 1200x? keep 3:2; resize to 1200 wide
im=im.resize((1200,int(1200*im.height/im.width)),Image.LANCZOS); k=1200/1024
d=ImageDraw.Draw(im,'RGBA')
fh=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf',29)
fs=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Regular.otf',23)
fk=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf',18)
brick=(172,59,25); ink=(40,40,40); grey=(95,92,88)
rows=[(342,"0.5 mm","PURE TITANIUM","The surface you cook on."),
      (432,"1 mm","ALUMINIUM CORE","Even heat, edge to edge."),
      (522,"0.6 mm","STAINLESS STEEL","Gas, electric, induction.")]
lx=800; ex=740
for y,mm,name,sub in rows:
    d.ellipse((ex-6,y-6,ex+6,y+6),fill=brick)
    d.line((ex,y,lx-14,y),fill=brick,width=3)
    w=d.textlength(name+'  ',font=fh)
    d.text((lx,y-20),name,font=fh,fill=ink)
    d.text((lx+w,y-13),mm,font=fk,fill=brick)
    d.text((lx,y+14),sub,font=fs,fill=grey)
im.save(out,quality=86)
