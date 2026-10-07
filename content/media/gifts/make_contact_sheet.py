import sys,os
from PIL import Image,ImageDraw,ImageFont
src,out=sys.argv[1],sys.argv[2]
files=sorted(f for f in os.listdir(src) if f.lower().endswith(('.png','.jpg','.jpeg')))
cell=300;cols=4;rows=(len(files)+cols-1)//cols
sheet=Image.new('RGB',(cols*cell,rows*(cell+40)),'#F5F1EA')
d=ImageDraw.Draw(sheet)
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
except: font=ImageFont.load_default()
for i,f in enumerate(files):
    im=Image.open(os.path.join(src,f)).convert('RGBA'); w,h=im.size
    im.thumbnail((cell-16,cell-16))
    bg=Image.new('RGBA',im.size,'white');bg.alpha_composite(im)
    x=(i%cols)*cell; y=(i//cols)*(cell+40)
    sheet.paste(bg.convert('RGB'),(x+(cell-im.width)//2,y+8+(cell-16-im.height)//2))
    d.text((x+8,y+cell+2),f[:44],fill='#282828',font=font); d.text((x+8,y+cell+18),f'{w}x{h}',fill='#AC3B19',font=font)
sheet.save(out); print(out,sheet.size)
