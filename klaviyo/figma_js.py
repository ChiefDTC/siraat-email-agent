"""Emit use_figma scripts for the Figma file "Siraat's Kitchen · Klaviyo flows".

  python3 klaviyo/figma_js.py            -> klaviyo/figma/01..09-*.js (flows) + 10-oktober-campagnes.js

Style = Homestead "SIRAAT – Client Review 2026" footer system:
  bg #2B2929, text #F2F2F2, display font TT Ramillas Trl Light It (fallback chain in JS),
  nav Inter Bold uppercase +5% tracking, legal Inter Light, SIRAAT monogram + FB/IG icons (assets/*.svg).
Each flow script first removes the previous section with the same name, so it is safe to re-run.
"""
import html as H
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET = lambda n: open(os.path.join(HERE, "figma", "assets", n)).read()  # noqa: E731

HELPERS = r'''
await figma.loadFontAsync({ family: "Inter", style: "Regular" });
await figma.loadFontAsync({ family: "Inter", style: "Bold" });
await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
let LIGHT={family:"Inter",style:"Regular"}; try{await figma.loadFontAsync({family:"Inter",style:"Light"});LIGHT={family:"Inter",style:"Light"};}catch(e){}
let DISPLAY={family:"Inter",style:"Regular"};
for (const f of [{family:"TT Ramillas",style:"Light Italic"},{family:"TT Ramillas Trl",style:"Light It"},{family:"Instrument Serif",style:"Italic"},{family:"Playfair Display",style:"Italic"},{family:"EB Garamond",style:"Italic"}]) { try { await figma.loadFontAsync(f); DISPLAY=f; break; } catch(e) {} }
const ink={r:0.169,g:0.161,b:0.161}, cream={r:0.949,g:0.949,b:0.949}, white={r:1,g:1,b:1}, sand={r:0.96,g:0.945,b:0.925}, grey={r:0.42,g:0.42,b:0.42}, line={r:0.88,g:0.87,b:0.85}, rule={r:0.6,g:0.6,b:0.6};
const W=600;
const LOGO_SVG=__LOGO__, FB_SVG=__FB__, IG_SVG=__IG__;
function text(chars,size,font,color,o={}){const t=figma.createText();t.fontName=font;t.characters=chars;t.fontSize=size;t.fills=[{type:"SOLID",color}];t.textAlignHorizontal=o.align||"CENTER";t.lineHeight={unit:"PERCENT",value:o.lh||140};if(o.ls!==undefined)t.letterSpacing={unit:"PERCENT",value:o.ls};if(o.upper)t.textCase="UPPER";return t;}
const F={reg:{family:"Inter",style:"Regular"},bold:{family:"Inter",style:"Bold"},semi:{family:"Inter",style:"Semi Bold"}};
function addText(p,n,w){p.appendChild(n);n.resize(w||(W-80),20);n.textAutoResize="HEIGHT";n.layoutSizingHorizontal="FILL";return n;}
function img(name,h,url){const f=figma.createFrame();f.name="IMG "+name;f.resize(W,h);f.fills=[{type:"SOLID",color:sand}];const l=text(name+"\n"+url,11,F.reg,grey);f.appendChild(l);l.resize(W-40,40);l.textAutoResize="HEIGHT";l.x=20;l.y=h/2-20;return f;}
function section(name,pv,ph,gap,bg){const s=figma.createAutoLayout("VERTICAL",{name,itemSpacing:gap,paddingTop:pv,paddingBottom:pv,paddingLeft:ph,paddingRight:ph});s.counterAxisAlignItems="CENTER";s.fills=bg?[{type:"SOLID",color:bg}]:[];return s;}
function svgNode(svg,size,name,fill){const n=figma.createNodeFromSvg(svg);n.name=name;n.resize(size,size);if(fill){for(const v of n.findAll(x=>"fills" in x)){try{v.fills=v.fills.map(p=>p.type==="SOLID"?{...p,color:fill}:p);}catch(e){}}}return n;}
function header(mail){
  const h=figma.createAutoLayout("HORIZONTAL",{name:"Header",itemSpacing:16,paddingTop:18,paddingBottom:18,paddingLeft:40,paddingRight:40});h.counterAxisAlignItems="CENTER";h.fills=[{type:"SOLID",color:cream}];
  const mono=svgNode(LOGO_SVG,34,"SIRAAT monogram",ink);h.appendChild(mono);
  const wm=text("Built for Life",22,DISPLAY,ink,{align:"LEFT",ls:-4,lh:110});h.appendChild(wm);
  const sp=figma.createFrame();sp.resize(10,10);sp.fills=[];h.appendChild(sp);sp.layoutSizingHorizontal="FILL";
  for(const n of ["Cookware","Sets","About"]){h.appendChild(text(n,11,F.bold,ink,{ls:5,upper:true}));}
  mail.appendChild(h);h.layoutSizingHorizontal="FILL";return h;
}
function footer(mail){
  const f=section("Footer SIRAAT (Homestead)",36,40,0,ink);mail.appendChild(f);f.layoutSizingHorizontal="FILL";f.counterAxisAlignItems="MIN";
  const top=figma.createAutoLayout("HORIZONTAL",{name:"Brand",itemSpacing:22});top.counterAxisAlignItems="CENTER";top.fills=[];
  top.appendChild(svgNode(LOGO_SVG,76,"SIRAAT monogram",cream));
  const col=figma.createAutoLayout("VERTICAL",{itemSpacing:2});col.fills=[];col.appendChild(text("Built for Life",46,DISPLAY,cream,{align:"LEFT",ls:-5,lh:110}));col.appendChild(text("Non-Toxic Cookware",19,F.reg,cream,{align:"LEFT",ls:-2}));top.appendChild(col);
  f.appendChild(top);
  const gap=figma.createFrame();gap.resize(10,28);gap.fills=[];f.appendChild(gap);
  for(const [n,u] of [["Titanium Cookware","/collections/cookware"],["Bundle & Sets","/collections/bundles"],["Accessories","/collections/accessories"],["About Us","/pages/faq"]]){
    const ln=figma.createRectangle();ln.resize(W-80,1);ln.fills=[{type:"SOLID",color:rule}];f.appendChild(ln);ln.layoutSizingHorizontal="FILL";
    const row=figma.createAutoLayout("HORIZONTAL",{name:"Nav · "+u,paddingTop:16,paddingBottom:16,paddingLeft:8,paddingRight:8});row.fills=[];row.appendChild(text(n+"  →",19,F.bold,cream,{align:"LEFT",ls:5,upper:true}));f.appendChild(row);
  }
  const ln2=figma.createRectangle();ln2.resize(W-80,1);ln2.fills=[{type:"SOLID",color:rule}];f.appendChild(ln2);ln2.layoutSizingHorizontal="FILL";
  const soc=figma.createAutoLayout("HORIZONTAL",{name:"Social",itemSpacing:40,paddingTop:36,paddingBottom:28});soc.primaryAxisAlignItems="CENTER";soc.fills=[];soc.appendChild(svgNode(FB_SVG,36,"Facebook"));soc.appendChild(svgNode(IG_SVG,36,"Instagram"));f.appendChild(soc);soc.layoutSizingHorizontal="FILL";
  addText(f,text("{% unsubscribe 'Unsubscribe' %} | {% manage_preferences %} | {% web_view %}\n\n{{ organization.name }} | {{ organization.full_address }}",12,LIGHT,cream,{ls:-2}));
  return f;
}
function box(parent,label,codeTag){const cb=figma.createAutoLayout("VERTICAL",{name:"Code block",itemSpacing:8,paddingTop:18,paddingBottom:18,paddingLeft:18,paddingRight:18});cb.counterAxisAlignItems="CENTER";cb.fills=[{type:"SOLID",color:cream}];parent.appendChild(cb);cb.layoutSizingHorizontal="FILL";addText(cb,text(label,11,F.bold,grey,{ls:5,upper:true}));const c=figma.createAutoLayout("HORIZONTAL",{name:"Code",paddingTop:10,paddingBottom:10,paddingLeft:18,paddingRight:18});c.strokes=[{type:"SOLID",color:ink}];c.strokeWeight=1;c.dashPattern=[4,4];c.appendChild(text(codeTag,22,F.bold,ink,{ls:4}));cb.appendChild(c);}
function button(parent,label,url){const b=figma.createAutoLayout("HORIZONTAL",{name:"Button · "+url,paddingTop:16,paddingBottom:16,paddingLeft:36,paddingRight:36});b.fills=[{type:"SOLID",color:ink}];b.appendChild(text(label,13,F.bold,cream,{ls:5,upper:true}));parent.appendChild(b);return b;}
function productCard(parent,n,p,file){const card=figma.createAutoLayout("VERTICAL",{name:"Product · "+n,itemSpacing:8,paddingTop:8,paddingBottom:8});card.counterAxisAlignItems="CENTER";const im=figma.createFrame();im.name="IMG "+file;im.resize(170,170);im.fills=[{type:"SOLID",color:sand}];card.appendChild(im);card.appendChild(text(n,13,F.reg,ink));card.appendChild(text(p,13,F.bold,ink));parent.appendChild(card);card.layoutSizingHorizontal="FILL";}
function meta(spec,x,y){const m=figma.createAutoLayout("VERTICAL",{name:"Meta · "+spec.name,itemSpacing:4,paddingTop:12,paddingBottom:12,paddingLeft:16,paddingRight:16});m.fills=[{type:"SOLID",color:{r:1,g:0.97,b:0.9}}];m.resize(W,10);figma.currentPage.appendChild(m);m.x=x;m.y=y;addText(m,text("Onderwerp: "+spec.subject,12,F.semi,ink,{align:"LEFT"}));addText(m,text("Preview: "+(spec.preview||"")+"  ·  "+spec.delay+(spec.smart?"  ·  Smart sending "+spec.smart:"")+(spec.filters?"  ·  Filter: "+spec.filters:""),11,F.reg,grey,{align:"LEFT"}));return m;}
function shell(name,x,y){const mail=figma.createAutoLayout("VERTICAL",{name,itemSpacing:0});mail.fills=[{type:"SOLID",color:white}];mail.resize(W,100);mail.layoutSizingHorizontal="FIXED";mail.clipsContent=true;figma.currentPage.appendChild(mail);mail.x=x;mail.y=y;header(mail);return mail;}
function build(spec,x,y){
  const m=meta(spec,x,y);
  const mail=shell(spec.name,x,y+110);
  mail.appendChild(img("Hero: "+spec.heroName,300,spec.heroUrl));
  const body=section("Body",32,40,14,white);mail.appendChild(body);body.layoutSizingHorizontal="FILL";
  addText(body,text(spec.headline,34,DISPLAY,ink,{lh:115,ls:-3}));
  for(const b of spec.blocks){ if(b.t==="p") addText(body,text(b.v,15,F.reg,ink,{lh:160})); else if(b.t==="code") box(body,b.label,b.v); else if(b.t==="li") addText(body,text(b.v,15,F.reg,ink,{lh:160,align:"LEFT"})); }
  if(spec.product==="checkout"){const pr=section("Cart items (dynamic: event.extra.line_items)",12,40,8,white);mail.appendChild(pr);pr.layoutSizingHorizontal="FILL";const row=figma.createAutoLayout("HORIZONTAL",{name:"Line item",itemSpacing:12,paddingTop:12,paddingBottom:12,paddingLeft:12,paddingRight:12});row.fills=[{type:"SOLID",color:cream}];const im=figma.createFrame();im.name="IMG {{ item.product.images.0.src }}";im.resize(130,130);im.fills=[{type:"SOLID",color:sand}];row.appendChild(im);const col=figma.createAutoLayout("VERTICAL",{itemSpacing:4});col.appendChild(text("{{ item.product.title }}",16,F.reg,ink,{align:"LEFT"}));col.appendChild(text("Qty {{ item.quantity }} · {{ event.extra.currency }} {{ item.line_price }}",14,F.reg,grey,{align:"LEFT"}));row.appendChild(col);pr.appendChild(row);row.layoutSizingHorizontal="FILL";}
  if(spec.product==="single"){const pr=section("Viewed product (dynamic: event.ImageURL / ProductName)",12,40,8,white);mail.appendChild(pr);pr.layoutSizingHorizontal="FILL";const im=figma.createFrame();im.name="IMG {{ event.ImageURL }}";im.resize(320,320);im.fills=[{type:"SOLID",color:sand}];pr.appendChild(im);addText(pr,text("{{ event.ProductName }}",16,F.reg,ink));addText(pr,text("Free shipping · 100-day trial",13,F.reg,grey));}
  if(spec.product==="bestsellers"){const grid=figma.createAutoLayout("HORIZONTAL",{name:"Bestsellers",itemSpacing:8,paddingBottom:8,paddingLeft:28,paddingRight:28});mail.appendChild(grid);grid.layoutSizingHorizontal="FILL";productCard(grid,"Pan Pro Standard","$134","Titanium_hammered_pan_pro_standard.webp");productCard(grid,"Pan Pro Large","$139","Titanium_hammered_pan_pro_large.webp");productCard(grid,"Wok Pan Pro","from $119","WokHammedPan_3.webp");}
  const cw=section("CTA",8,40,0,white);cw.paddingBottom=28;mail.appendChild(cw);cw.layoutSizingHorizontal="FILL";button(cw,spec.cta,spec.ctaUrl);
  if(spec.featureUrl) mail.appendChild(img("Feature: "+spec.featureName,220,spec.featureUrl));
  if(spec.reviews){const rv=section("Reviews (replace with Loox/Trustpilot)",8,40,10,white);mail.appendChild(rv);rv.layoutSizingHorizontal="FILL";for(const q of ["★★★★★ “Eggs slide off with no oil. I threw out three non-stick pans the week this arrived.” — Dana R.","★★★★★ “Metal spatula, dishwasher, high heat. Nothing to scratch off because there is no coating.” — Marcus T.","★★★★★ “Half the weight of my cast iron and heats faster. Bought a second one for my mum.” — Priya K."]) addText(rv,text(q,14,F.reg,ink,{align:"LEFT",lh:150}));}
  const tb=figma.createAutoLayout("HORIZONTAL",{name:"Trust bar",itemSpacing:0,paddingTop:14,paddingBottom:14});tb.fills=[{type:"SOLID",color:cream}];for(const t of ["Free shipping","100-day trial","75-year warranty"]){const c=figma.createAutoLayout("HORIZONTAL",{primaryAxisAlignItems:"CENTER"});c.resize(200,20);c.fills=[];c.primaryAxisAlignItems="CENTER";c.appendChild(text(t,10,F.bold,ink,{ls:5,upper:true}));tb.appendChild(c);}mail.appendChild(tb);tb.layoutSizingHorizontal="FILL";
  footer(mail);
  return [mail,m];
}
function campaign(c,x,y){
  const m=meta({name:c.name,subject:c.subject||"(geen onderwerp)",preview:c.preview,delay:(c.planned_send_date||"")+"  ·  "+c.channel.toUpperCase()+"  ·  "+c.status},x,y);
  if(c.channel==="sms"){const ph=figma.createAutoLayout("VERTICAL",{name:c.name,paddingTop:24,paddingBottom:24,paddingLeft:20,paddingRight:20,itemSpacing:8});ph.fills=[{type:"SOLID",color:cream}];ph.resize(360,100);ph.layoutSizingHorizontal="FIXED";ph.cornerRadius=24;figma.currentPage.appendChild(ph);ph.x=x;ph.y=y+110;const bub=figma.createAutoLayout("VERTICAL",{paddingTop:14,paddingBottom:14,paddingLeft:16,paddingRight:16});bub.fills=[{type:"SOLID",color:white}];bub.cornerRadius=18;ph.appendChild(bub);bub.layoutSizingHorizontal="FILL";addText(bub,text(c.sms_body||"",15,F.reg,ink,{align:"LEFT",lh:145}),320);return [ph,m];}
  const mail=shell(c.name,x,y+110);
  const body=section("Body",32,40,14,white);mail.appendChild(body);body.layoutSizingHorizontal="FILL";
  let first=true;
  for(const b of c.blocks){
    if(b.type==="image"){mail.appendChild(img((b.alt||"image").slice(0,90),b.alt&&b.alt.length>60?260:200,b.src));}
    else if(b.type==="text"){const isHead=first&&b.text.length<80;addText(body,text(b.text,isHead?34:15,isHead?DISPLAY:F.reg,ink,{lh:isHead?115:160,ls:isHead?-3:0,align:isHead?"CENTER":"LEFT"}));first=false;}
    else if(b.type==="button"){const cw=section("CTA",4,0,0,white);body.appendChild(cw);cw.layoutSizingHorizontal="FILL";button(cw,b.text.replace(/→/g,"").trim().slice(0,40),b.href||"");}
  }
  if(c.variations&&c.variations.length){addText(body,text("A/B variatie B: "+c.variations.length+" alternatieve template(s), zie JSON",11,F.reg,grey));}
  footer(mail);
  return [mail,m];
}
'''


def strip(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = H.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def blocks_of(e):
    out = []
    for b in e["body"]:
        if 'class="code"' in b:
            m = re.search(r'margin-bottom:8px;">(.*?)</div>\s*<span class="code">(.*?)</span>', b, re.S)
            out.append({"t": "code", "label": strip(m.group(1)), "v": strip(m.group(2))})
        elif b.startswith("<ol") or b.startswith("<table"):
            for li in re.findall(r"<li>(.*?)</li>", b, re.S):
                out.append({"t": "li", "v": "• " + strip(li)})
            if b.startswith("<table"):
                out.append({"t": "li", "v": "[Vergelijkingstabel non-stick vs titanium: surface, metal utensils, lifespan, chemicals]"})
        else:
            out.append({"t": "p", "v": strip(b)})
    return out


def spec(e):
    hero_key = B.HERO.get(e["file"], "standard")
    hero_url = hero_key if hero_key.startswith("{{") else B.shop_img(hero_key)
    feat = B.FEATURE.get(e["file"])
    product = ("checkout" if e.get("product") == B.CHECKOUT_ITEMS else "single" if e.get("product") == B.SINGLE_PRODUCT
               else "bestsellers" if e.get("product") == B.BESTSELLERS else "")
    return {
        "name": f"{e['file'].split('-')[0].upper()} · {strip(e['headline'])} ({e['delay']})",
        "subject": e["subject"], "preview": e["preview"], "delay": e["delay"], "smart": e["smart"], "filters": e["filters"],
        "headline": strip(e["headline"]), "blocks": blocks_of(e), "product": product, "cta": e["cta"][0], "ctaUrl": e["cta"][1],
        "heroName": hero_key, "heroUrl": hero_url, "featureName": feat or "", "featureUrl": B.shop_img(feat) if feat else "",
        "reviews": bool(e.get("proof")),
    }


def helpers() -> str:
    return (HELPERS.replace("__LOGO__", json.dumps(ASSET("logo.svg")))
            .replace("__FB__", json.dumps(ASSET("facebook.svg")))
            .replace("__IG__", json.dumps(ASSET("instagram.svg"))))


def main():
    out_dir = os.path.join(HERE, "figma")
    os.makedirs(out_dir, exist_ok=True)
    for i, fl in enumerate(B.FLOWS):
        specs = [spec(e) for e in fl["emails"]]
        name = fl["slug"] + " · " + fl["name"]
        js = helpers() + f'''
const SECNAME={json.dumps(name)};
for(const old of figma.currentPage.children.filter(c=>c.type==="SECTION"&&c.name===SECNAME)) old.remove();
const X0=0;
const sec=figma.createSection();sec.name=SECNAME;figma.currentPage.appendChild(sec);sec.x={i*4000+100};sec.y=0;
const tree=text({json.dumps(fl["tree"])},12,F.reg,ink,{{align:"LEFT",lh:150}});sec.appendChild(tree);tree.resize(700,40);tree.textAutoResize="HEIGHT";tree.x=X0;tree.y=100;
const specs={json.dumps(specs, ensure_ascii=False)};
const ids=[];let x=X0+800;for(const s of specs){{const [m,mt]=build(s,x,100);sec.appendChild(m);sec.appendChild(mt);ids.push(m.id);x+=700;}}
sec.resizeWithoutConstraints(Math.max(900,x-X0+100),2800);
return {{section:sec.id,mails:ids,display:DISPLAY}};
'''
        open(os.path.join(out_dir, f"{fl['slug']}.js"), "w").write(js)
        print(fl["slug"], len(js))

    # October campaign drafts -> own page
    drafts = json.load(open(os.path.join(HERE, "campaigns", "oct-drafts.json")))
    drafts = [d for d in drafts if d.get("blocks") or d.get("sms_body")]
    js = f'''
let page=figma.root.children.find(p=>p.name==="Oktober campagnes (drafts)");
if(!page){{page=figma.createPage();page.name="Oktober campagnes (drafts)";}}
await figma.setCurrentPageAsync(page);
for(const old of page.children.slice()) old.remove();
''' + helpers() + f'''
const drafts={json.dumps(drafts, ensure_ascii=False)};
const ids=[];let x=100;
for(const c of drafts){{const [m,mt]=campaign(c,x,100);ids.push(m.id);x+=(c.channel==="sms"?460:700);}}
return {{page:page.id,frames:ids,display:DISPLAY}};
'''
    open(os.path.join(out_dir, "10-oktober-campagnes.js"), "w").write(js)
    print("10-oktober-campagnes", len(js), "drafts:", len(drafts))


if __name__ == "__main__":
    main()
