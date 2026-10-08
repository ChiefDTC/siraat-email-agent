"""Zet de screenshots naast elkaar: per mail twee rijen (voor / na), vijf kolommen (weergaven). Bovenste 1500 px. Uitvoer: img/<mail>-vergelijking.jpg"""
import os
from PIL import Image, ImageDraw, ImageFont
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.join(D,'shots'); O=os.path.join(D,'img'); os.makedirs(O,exist_ok=True)
MODES=[('light','Licht'),('apple','Apple Mail donker'),('algo','Android-webview / Gmail nieuw?'),('partial','Outlook.com/-app (gedeeltelijk)'),('full','Gmail iOS oud / Outlook Win (volledig)')]
H=1500; W=375; G=12; TOP=40; LAB=34
try: F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',13)
except Exception: F=ImageFont.load_default()
def sheet(mail,rows):
    im=Image.new('RGB',(len(MODES)*(W+G)+G+70,TOP+len(rows)*(H+LAB+G)),(120,120,120)); d=ImageDraw.Draw(im)
    for i,(m,t) in enumerate(MODES): d.text((70+G+i*(W+G),12),t,fill=(255,255,255),font=F)
    for r,(dir_,lab) in enumerate(rows):
        y=TOP+r*(H+LAB+G); d.text((6,y+H//2),lab,fill=(255,255,255),font=F)
        for i,(m,_) in enumerate(MODES):
            p=os.path.join(S,'%s-%s-%s.jpg'%(mail if dir_!='B' else 'c1-B','after' if dir_ in('after','B') else 'before',m))
            if not os.path.exists(p): continue
            s=Image.open(p).convert('RGB'); s=s.crop((0,0,W,min(H,s.height))); im.paste(s,(70+G+i*(W+G),y))
    im.save(os.path.join(O,'%s-vergelijking.jpg'%mail),quality=72); print('ok',mail)
sheet('c1',[('before','VOOR'),('after','NA (A)'),('B','B: niet')])
sheet('w1-a',[('before','VOOR'),('after','NA (A)')])
sheet('p1-first',[('before','VOOR'),('after','NA (A)')])
