import json, re, csv, html as H, statistics as st
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.t=[]; s.skip=0; s.imgs=[]; s.links=0
    def handle_starttag(s,tag,a):
        a=dict(a)
        if tag in("style","script","title"): s.skip+=1
        if tag=="img": s.imgs.append((a.get("alt") or "",a.get("src") or "",a.get("width") or ""))
        if tag=="a": s.links+=1
    def handle_endtag(s,tag):
        if tag in("style","script","title"): s.skip=max(0,s.skip-1)
    def handle_data(s,d):
        if not s.skip: s.t.append(d)
def parse(tid):
    try: a=json.load(open(f'/tmp/hist/tpl/{tid}.json'))['data']['attributes']
    except Exception: return None
    p=P(); p.feed(a.get('html') or '')
    txt=re.sub(r'\{%.*?%\}|\{\{.*?\}\}',' ',' '.join(p.t)); txt=re.sub(r'\s+',' ',txt).strip()
    BOIL={'Privacy Policy','SIRAAT','Terms of Service','IG Page','FB Page','FOLLOW US','SIRAAT PRIME TIME SALE | UP TO 56% OFF',"Siraat's Kitchen",'ABOUT US','SHOP','FAQ','FREE SHIPPING | FREE SHIPPING | 100-DAY TRIAL | MADE WITH LOVE','Free Worldwide Shipping','100K+ Happy Customers','Instagram',"SIRAAT'S KITCHEN",'LinkedIn','30,000+ Customers','FREE SHIPPING | 30,000 HAPPY CUSTOMERS | 100-DAY TRIAL','Rated 4.9/5 by 30,000+ Customers'}
    p.imgs=[x for x in p.imgs if x[0] not in BOIL]
    alts=' '.join(x[0] for x in p.imgs)
    return dict(editor=a.get('editor_type'),words=len(txt.split()),n_img=len(p.imgs),n_links=p.links,text=txt,alts=alts,imgs=p.imgs,html_kb=round(len(a.get('html') or '')/1024,1))
EMO=re.compile('[\U0001F000-\U0001FAFF☀-➿⭐✅⏰-⏿]')
def subj_feat(s):
    sl=s.lower()
    f={}
    f['s_len_chars']=len(s); f['s_len_words']=len(s.split())
    f['s_question']='?' in s
    f['s_number']=bool(re.search(r'\d',re.sub(r'\{\{.*?\}\}','',s)))
    f['s_discount']=bool(re.search(r'%|\boff\b|sale|save|\$\d|discount|deal|clearance|bogo|price',sl))
    f['s_gift']=bool(re.search(r'gift|free\b|bonus|mystery',sl))
    f['s_urgency']=bool(re.search(r'last|ends?\b|ending|tonight|hours? left|final|today only|expires|hurry|left\b|don.t miss|before it|gone|forever|countdown|midnight|extended|extension',sl))
    f['s_socialproof']=bool(re.search(r'customer|review|rated|bestsell|best-sell|#1|favorite|favourite|loved|love it|people|chefs?\b|everyone|million|\d{2,3},?000',sl))
    f['s_pfas']=bool(re.search(r'pfas|toxic|chemical|micro.?plastic|teflon|forever chem|coating|safe|healthy|healthier|clean cooking|non-?stick',sl))
    f['s_emoji']=bool(EMO.search(s))
    f['s_personal']='first_name' in sl or 'organization' in sl
    f['s_founder']=bool(re.search(r'benjamin|founder|note from|letter|personal|from me',sl))
    f['s_howto']=bool(re.search(r'how to|why |tips?\b|guide|recipe|mistake|secret|fix|learn|care',sl))
    f['s_launch']=bool(re.search(r'new\b|launch|introduc|meet|just dropped|back in stock|restock|is here|arrived',sl))
    f['s_curiosity']=(not f['s_discount'] and not f['s_gift'] and not f['s_launch'] and (f['s_question'] or bool(re.search(r'\bthis\b|why|secret|truth|mistake|nobody|what |you.re|surpris|\.\.\.|…',sl))))
    return f
def offer_feat(t):
    tl=t.lower()
    pct=[int(x) for x in re.findall(r'(\d{1,2})\s?%\s?off',tl)]+[int(x) for x in re.findall(r'(?:up to|save)\s(\d{1,2})\s?%',tl)]
    f={}
    f['o_maxpct']=max(pct) if pct else 0
    f['o_code']=bool(re.search(r'\bcode\b|use code|with code',tl))
    f['o_gift']=bool(re.search(r'free gift|mystery gift|gifts?\b.*(with|every) order|\$\d+ in gifts|bonus gift|free e-?book|free apron|free lid',tl))
    f['o_freeship']='free shipping' in tl
    f['o_bundle']=bool(re.search(r'bundle|set\b|buy \d|bogo|2 for|two for',tl))
    return f
PROD={'pan_pro':r'pan pro|hammered pan|frying pan|skillet|the pan\b|our pan|titanium pan','wok':r'\bwok','crepe':r'cr[eê]pe','deep':r'deep pan|saut[eé]|deep','set':r'\bset\b|cookware set|6-piece|12-piece|bundle','board':r'cutting board|chopping board|\bboard\b','lid':r'\blids?\b','apron':r'apron','strips':r'dishwasher|detergent|strips','utensils':r'utensil|spatula|tongs|knife|knives','steamer':r'steamer|pot\b|saucepan'}
def products(t):
    tl=t.lower(); return {k:len(re.findall(v,tl)) for k,v in PROD.items()}
