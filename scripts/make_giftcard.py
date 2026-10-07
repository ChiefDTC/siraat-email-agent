"""Welcome gift card (W1-B): 1200x700, espresso card, officieel logo, TT Ramillas.
Gebruik: python3 -I scripts/make_giftcard.py <uit.jpg> [CODE] [regel]"""
import sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R='/home/user/siraat-email-agent/'
TT=R+'klaviyo/fonts/TTRamillas-LightItalic.ttf'
IM='/usr/share/fonts/opentype/inter/Inter-Medium.otf'; IS='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
out=sys.argv[1]; code=sys.argv[2] if len(sys.argv)>2 else 'HI10'; line=sys.argv[3] if len(sys.argv)>3 else '10% on top of the sale'
Wd,H=1200,700; TI=(201,198,192)
bg=Image.new('RGB',(Wd,H),(248,247,242))
sh=Image.new('L',(Wd,H),0); ImageDraw.Draw(sh).rounded_rectangle((70,72,Wd-70,H-38),radius=36,fill=110); sh=sh.filter(ImageFilter.GaussianBlur(22))
bg.paste((90,70,60),(0,0),sh)
card=Image.new('RGB',(Wd-120,H-100),(50,30,29)); cw,ch=card.size; d=ImageDraw.Draw(card)
for i in range(0,cw+ch,6):
    a=int(10*max(0,1-abs(i-(cw+ch)*0.62)/420))
    if a: d.line((i,0,i-ch,ch),fill=(50+a,30+a,29+a),width=6)
d.rounded_rectangle((22,22,cw-22,ch-22),radius=22,outline=TI,width=2)
logo=Image.open(R+'klaviyo/templates/partials/assets/logo-white.png').convert('RGBA')
logo=logo.resize((int(logo.width*0.75),int(logo.height*0.75)),Image.LANCZOS); card.paste(logo,(64,60),logo)
fl=ImageFont.truetype(IS,22); t='WELCOME GIFT CARD'; d.text((cw-64-d.textlength(t,font=fl),82),t,font=fl,fill=TI)
fh=ImageFont.truetype(TT,136); t='Welcome gift'; d.text(((cw-d.textlength(t,font=fh))/2,168),t,font=fh,fill=(255,255,255))
fs=ImageFont.truetype(IM,38); d.text(((cw-d.textlength(line,font=fs))/2,372),line,font=fs,fill=(240,236,228))
fc=ImageFont.truetype(IS,46); fk=ImageFont.truetype(IS,18)
lab='CODE'; gap=24; inner=d.textlength(lab,font=fk)+gap+d.textlength(code,font=fc)
bw=inner+96; x0=round((cw-bw)/2); y0=448; x1=round(x0+bw); y1=y0+84
def dash(xa,ya,xb,yb):
    L=math.hypot(xb-xa,yb-ya); n=max(1,round((L-10)/18)); step=(L-10)/n
    for k in range(n+1):
        s=k*step; e=min(s+10,L)
        d.line((xa+(xb-xa)*s/L,ya+(yb-ya)*s/L,xa+(xb-xa)*e/L,ya+(yb-ya)*e/L),fill=TI,width=3)
dash(x0,y0,x1,y0); dash(x1,y0,x1,y1); dash(x1,y1,x0,y1); dash(x0,y1,x0,y0)
tx=x0+48; d.text((tx,y0+33),lab,font=fk,fill=TI); d.text((tx+d.textlength(lab,font=fk)+gap,y0+14),code,font=fc,fill=(255,255,255))
mask=Image.new('L',card.size,0); ImageDraw.Draw(mask).rounded_rectangle((0,0,cw,ch),radius=30,fill=255)
bg.paste(card,(60,40),mask); bg.save(out,quality=88); print(out)
