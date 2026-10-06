
const T={cream:'#F8F7F2',paper:'#FFFFFF',sand:'#ECE7DD',stone:'#9A948B',slate:'#727272',ink:'#282828',charcoal:'#2B2929',espresso:'#321E1D',black:'#111111',brick:'#AC3B19',brickDark:'#8A2D12',brickTint:'#F3E3DC',titanium:'#C9C6C0',success:'#3D6B4F'};
const LOGO_SVG="<svg width=\"151\" height=\"151\" viewBox=\"0 0 151 151\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">\n<path d=\"M47.0601 113.51H71.0415V102.15H0.417114V150.29H71.0415V138.931H47.0601V113.51ZM35.7005 138.931H11.7767V113.51H35.7005V138.931Z\" fill=\"#F2F2F2\"/>\n<path d=\"M55.5594 131.901H95.2405L95.3557 120.541H55.5594V131.901Z\" fill=\"#F2F2F2\"/>\n<path d=\"M123.434 82.1148V93.625H150.482V82.1148V62.2278H78.0557V73.5874H103.503V102.152H79.5216V113.512H103.503V138.933H79.5216V150.292L150.146 150.385V102.152H114.863V73.5874H139.123V82.1148H123.434ZM138.786 113.512V138.933H114.863V113.512H138.786Z\" fill=\"#F2F2F2\"/>\n<path d=\"M70.1084 11.3596H70.3476V0H58.988V0.0420726H58.7488V73.9016H70.1084V11.3596Z\" fill=\"#F2F2F2\"/>\n<path d=\"M103.452 42.1636H78.6642V53.5232H106.005L114.811 42.1636L114.913 11.4019H138.813V42.1636H114.862V53.5232H138.939L150.172 42.1636V0.0422897H138.813H116.724H105.365H78.538V11.4019H103.452V42.1636Z\" fill=\"#F2F2F2\"/>\n<path d=\"M11.0872 93.577H94.712L94.9312 82.2174H11.3596V73.5659H50.1926L50.1505 31.1568H11.5722V11.5266H50.3564V0.167046L0.212577 0.171474V42.5208L38.7953 42.5164V62.2064H0.132861V62.3016H0V93.577H11.0872Z\" fill=\"#F2F2F2\"/>\n</svg>\n", FB_SVG="<svg width=\"60\" height=\"60\" viewBox=\"0 0 60 60\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">\n<rect width=\"60\" height=\"60\" rx=\"22.5\" fill=\"#F2F2F2\"/>\n<path d=\"M41.6777 38.6719L43.0078 30H34.6875V24.375C34.6875 22.002 35.8477 19.6875 39.5742 19.6875H43.3594V12.3047C43.3594 12.3047 39.9258 11.7188 36.6445 11.7188C29.7891 11.7188 25.3125 15.873 25.3125 23.3906V30H17.6953V38.6719H25.3125V59.6367C26.8418 59.877 28.4063 60 30 60C31.5938 60 33.1582 59.877 34.6875 59.6367V38.6719H41.6777Z\" fill=\"#302F2F\"/>\n</svg>\n", IG_SVG="<svg width=\"60\" height=\"60\" viewBox=\"0 0 60 60\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">\n<rect width=\"60\" height=\"60\" rx=\"22.5\" fill=\"#F2F2F2\"/>\n<path d=\"M30.0048 12C25.1165 12 24.5019 12.0214 22.5794 12.1072C20.6641 12.193 19.3563 12.5003 18.2128 12.9434C17.0265 13.4007 16.0259 14.0225 15.0254 15.023C14.0249 16.0236 13.4103 17.0312 12.9457 18.2104C12.5026 19.3539 12.1953 20.6617 12.1096 22.5842C12.0238 24.4995 12.0024 25.1141 12.0024 30.0024C12.0024 34.8907 12.0238 35.5053 12.1096 37.4277C12.1953 39.343 12.5026 40.6509 12.9457 41.8015C13.4031 42.9878 14.0249 43.9884 15.0254 44.9889C16.0259 45.9894 17.0336 46.604 18.2128 47.0686C19.3563 47.5116 20.6641 47.819 22.5866 47.9047C24.509 47.9905 25.1165 48.0119 30.0119 48.0119C34.9074 48.0119 35.5148 47.9905 37.4373 47.9047C39.3526 47.819 40.6604 47.5116 41.811 47.0686C42.9974 46.6112 43.9979 45.9894 44.9984 44.9889C45.999 43.9884 46.6136 42.9807 47.0781 41.8015C47.5212 40.658 47.8285 39.3502 47.9143 37.4277C48 35.5053 48.0215 34.8978 48.0215 30.0024C48.0215 25.1069 48 24.4995 47.9143 22.577C47.8285 20.6617 47.5212 19.3539 47.0781 18.2033C46.6207 17.0169 45.999 16.0164 44.9984 15.0159C43.9979 14.0154 42.9902 13.4007 41.811 12.9362C40.6676 12.4931 39.3597 12.1858 37.4373 12.1001C35.5077 12.0214 34.8931 12 30.0048 12Z\" fill=\"#302F2F\"/>\n<path d=\"M30.0048 20.7618C24.9021 20.7618 20.757 24.8997 20.757 30.0095C20.757 35.1194 24.8949 39.2573 30.0048 39.2573C35.1146 39.2573 39.2525 35.1194 39.2525 30.0095C39.2525 24.8997 35.1146 20.7618 30.0048 20.7618ZM30.0048 36.0056C26.6887 36.0056 24.0016 33.3184 24.0016 30.0024C24.0016 26.6863 26.6887 23.9992 30.0048 23.9992C33.3208 23.9992 36.0079 26.6863 36.0079 30.0024C36.0079 33.3184 33.3208 36.0056 30.0048 36.0056Z\" fill=\"#F2F2F2\"/>\n<path d=\"M39.617 22.5484C40.809 22.5484 41.7753 21.5821 41.7753 20.3902C41.7753 19.1982 40.809 18.2319 39.617 18.2319C38.425 18.2319 37.4587 19.1982 37.4587 20.3902C37.4587 21.5821 38.425 22.5484 39.617 22.5484Z\" fill=\"#F2F2F2\"/>\n</svg>\n";
const W=600;
function hex(h){const n=parseInt(h.slice(1),16);return {r:((n>>16)&255)/255,g:((n>>8)&255)/255,b:(n&255)/255};}
const DISPLAYS=[{family:'TT Ramillas',style:'Light Italic'},{family:'TT Ramillas Trl',style:'Light Italic'},{family:'Instrument Serif',style:'Italic'},{family:'Playfair Display',style:'Italic'}];
const SANS={family:'Inter',style:'Regular'},SANS_B={family:'Inter',style:'Semi Bold'},SANS_L={family:'Inter',style:'Light'},SANS_M={family:'Inter',style:'Medium'};
let DISPLAY=null;for(const f of DISPLAYS){try{await figma.loadFontAsync(f);DISPLAY=f;break;}catch(e){}}
for(const f of [SANS,SANS_B,SANS_L,SANS_M]) await figma.loadFontAsync(f);
let page=figma.root.children.find(p=>p.name==='01 Components');
if(!page){page=figma.createPage();page.name='01 Components';}
await figma.setCurrentPageAsync(page);
for(const c of [...page.children]) c.remove();

function al(name,dir,o={}){const f=figma.createFrame();f.name=name;f.layoutMode=dir;f.itemSpacing=o.gap||0;f.paddingTop=o.pt??o.pv??0;f.paddingBottom=o.pb??o.pv??0;f.paddingLeft=o.pl??o.ph??0;f.paddingRight=o.pr??o.ph??0;f.fills=o.bg?[{type:'SOLID',color:hex(o.bg)}]:[];f.clipsContent=false;f.primaryAxisSizingMode='AUTO';f.counterAxisSizingMode='AUTO';if(o.w){f.resize(o.w,o.h||10);f.counterAxisSizingMode='FIXED';f.primaryAxisSizingMode='AUTO';}if(o.center)f.counterAxisAlignItems='CENTER';if(o.main)f.primaryAxisAlignItems=o.main;if(o.radius)f.cornerRadius=o.radius;if(o.stroke){f.strokes=[{type:'SOLID',color:hex(o.stroke)}];f.strokeWeight=o.sw||1;}return f;}
function txt(s,font,size,color,o={}){const t=figma.createText();t.fontName=font;t.characters=s;t.fontSize=size;t.fills=[{type:'SOLID',color:hex(color)}];t.lineHeight={unit:'PERCENT',value:o.lh||(size>=34?108:150)};if(o.ls!==undefined)t.letterSpacing={unit:'PERCENT',value:o.ls};if(o.upper)t.textCase='UPPER';t.textAlignHorizontal=o.align||'CENTER';if(o.strike)t.textDecoration='STRIKETHROUGH';if(o.underline)t.textDecoration='UNDERLINE';return t;}
function fill(p,t,w){p.appendChild(t);t.textAutoResize='HEIGHT';t.layoutSizingHorizontal='FILL';return t;}
function hug(p,t){p.appendChild(t);t.textAutoResize='WIDTH_AND_HEIGHT';return t;}
function imgBox(name,w,h,bg){const f=figma.createFrame();f.name='IMG '+name;f.resize(w,h);f.fills=[{type:'SOLID',color:hex(bg||T.sand)}];f.clipsContent=true;const l=txt(name+'\n'+w+'×'+h,SANS,11,T.slate);f.appendChild(l);l.resize(w-24,36);l.textAutoResize='HEIGHT';l.x=12;l.y=h/2-18;return f;}
function svgNode(svg,size,name,color){const n=figma.createNodeFromSvg(svg);n.name=name;n.resize(size,size);if(color)for(const v of n.findAll(x=>'fills' in x)){try{v.fills=v.fills.map(p=>p.type==='SOLID'?{...p,color:hex(color)}:p);}catch(e){}}return n;}
function button(label,kind){const k=kind||'primary';const b=al('Button / '+k,'HORIZONTAL',{pv:16,ph:32,radius:2,bg:k==='primary'?T.brick:k==='ondark'?T.cream:null,stroke:k==='secondary'?T.ink:k==='ondark-outline'?T.cream:null,sw:1.5});const c=k==='primary'?T.cream:k==='ondark'?T.ink:k==='ondark-outline'?T.cream:T.ink;const t=txt(label,SANS_B,13,c,{ls:8,upper:true});hug(b,t);return b;}
function eyebrow(s,color){return txt(s,SANS_B,12,color||T.brick,{ls:12,upper:true});}
function display(s,size,color,align){return txt(s,DISPLAY,size||44,color||T.ink,{lh:size>=44?104:110,align});}
function body(s,color,size,align){return txt(s,SANS,size||16,color||T.ink,{lh:155,align});}

// ---------- registry ----------
const made=[];const ROW_GAP=80;const COLW=700;
function compo(name,desc,build){const c=figma.createComponent();c.name=name;c.layoutMode='VERTICAL';c.primaryAxisSizingMode='AUTO';c.counterAxisSizingMode='FIXED';c.resize(W,10);c.primaryAxisSizingMode='AUTO';c.clipsContent=false;c.fills=[];c.description=desc||'';build(c);const btn=c.findOne(n=>n.name.startsWith('Button /'));if(btn){const bt=btn.children.find(n=>n.type==='TEXT');if(bt)prop(c,bt,'Button',bt.characters);}page.appendChild(c);made.push(c);return c;}
function prop(comp,node,name,def){try{const id=comp.addComponentProperty(name,'TEXT',def);node.componentPropertyReferences={characters:id};}catch(e){}}

// 1 Announcement bar
compo('Bars / Announcement','Baksteenrode balk boven de header. Campagne-wide aanbieding + tekstlink.',c=>{
  const bar=al('bar','HORIZONTAL',{pv:12,ph:24,gap:8,bg:T.brick,center:true,main:'CENTER'});c.appendChild(bar);bar.layoutSizingHorizontal='FILL';
  const t=hug(bar,txt('Warehouse Clearance Sale  |  Up to 50% off  |',SANS_B,12,T.cream,{ls:4,upper:true}));
  const l=hug(bar,txt('Shop now →',SANS_B,12,T.cream,{ls:4,upper:true,underline:true}));
  prop(c,t,'Text','Warehouse Clearance Sale  |  Up to 50% off  |');prop(c,l,'Link','Shop now →');
});
// 2 Header light + dark
for(const [nm,bg,fg] of [['Header / Light',T.cream,T.ink],['Header / Dark',T.charcoal,T.cream]]){
  compo(nm,'Monogram + wordmark gecentreerd, zonder menu.',c=>{
    const h=al('header','VERTICAL',{pv:28,gap:18,bg,center:true});c.appendChild(h);h.layoutSizingHorizontal='FILL';
    const row=al('logo','HORIZONTAL',{gap:12,center:true});h.appendChild(row);
    row.appendChild(svgNode(LOGO_SVG,30,'monogram',fg));hug(row,txt('SIRAAT',SANS_B,18,fg,{ls:28,upper:true}));
  });
}
// 3 Hero image full-bleed
compo('Hero / Image full-bleed','Vierkante lifestyle-foto 600\u00d7600 met logo als overlay bovenin, donkere gradient onderin, eyebrow + display 48 + knop verticaal gecentreerd. Gebruik zonder losse header.',c=>{
  const wrap=al('hero','VERTICAL',{w:W,h:600,main:'CENTER',center:true});wrap.primaryAxisSizingMode='FIXED';wrap.resize(W,600);wrap.clipsContent=true;wrap.fills=[{type:'SOLID',color:hex(T.espresso)}];c.appendChild(wrap);wrap.layoutSizingHorizontal='FILL';
  const im=imgBox('lifestyle hero',W,600,T.espresso);wrap.appendChild(im);im.layoutPositioning='ABSOLUTE';im.x=0;im.y=0;im.constraints={horizontal:'STRETCH',vertical:'STRETCH'};
  const grad=figma.createRectangle();grad.name='overlay';grad.resize(W,600);wrap.appendChild(grad);grad.layoutPositioning='ABSOLUTE';grad.x=0;grad.y=0;grad.fills=[{type:'GRADIENT_LINEAR',gradientTransform:[[0,1,0],[-1,0,1]],gradientStops:[{position:0,color:{r:0.08,g:0.06,b:0.05,a:0.3}},{position:0.5,color:{r:0.08,g:0.06,b:0.05,a:0.62}},{position:1,color:{r:0.08,g:0.06,b:0.05,a:0.85}}]}];
  const topg=figma.createRectangle();topg.name='overlay top';topg.resize(W,160);wrap.appendChild(topg);topg.layoutPositioning='ABSOLUTE';topg.x=0;topg.y=0;topg.fills=[{type:'GRADIENT_LINEAR',gradientTransform:[[0,1,0],[-1,0,1]],gradientStops:[{position:0,color:{r:0.08,g:0.06,b:0.05,a:0.55}},{position:1,color:{r:0.08,g:0.06,b:0.05,a:0}}]}];
  const hd=al('header overlay','VERTICAL',{pt:28,gap:16,center:true,w:W});wrap.appendChild(hd);hd.layoutPositioning='ABSOLUTE';hd.x=0;hd.y=0;
  const lrow=al('logo','HORIZONTAL',{gap:12,center:true});hd.appendChild(lrow);lrow.appendChild(svgNode(LOGO_SVG,30,'monogram',T.cream));hug(lrow,txt('SIRAAT',SANS_B,18,T.cream,{ls:28,upper:true}));
  const box=al('copy','VERTICAL',{gap:18,ph:48,pt:40,center:true});wrap.appendChild(box);box.layoutSizingHorizontal='FILL';
  const e=fill(box,eyebrow('Meet the latest',T.titanium));const d=fill(box,display('Titanium Hammered Roasting Pan',48,T.cream));const b=fill(box,body('Lightweight, 100% non-toxic, and beautiful enough to take center stage.',T.cream,16));box.appendChild(button('Get ready to roast','primary'));
  prop(c,e,'Eyebrow','Meet the latest');prop(c,d,'Headline','Titanium Hammered Roasting Pan');prop(c,b,'Body','Lightweight, 100% non-toxic, and beautiful enough to take center stage.');
  try{for(const [node,label] of [[e,'Show eyebrow'],[d,'Show headline'],[b,'Show body'],[box.children[box.children.length-1],'Show button']]){const k=c.addComponentProperty(label,'BOOLEAN',true);node.componentPropertyReferences={...(node.componentPropertyReferences||{}),visible:k};}}catch(e){}
});
// 4 Hero cream + product cutout
compo('Hero / Cream product','Crème hero: eyebrow, display 44, body, knop, daaronder vrijstaand product 600×420.',c=>{
  const s=al('hero','VERTICAL',{pt:48,pb:0,ph:48,gap:18,bg:T.cream,center:true});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const e=fill(s,eyebrow('Titanium cookware'));const d=fill(s,display('The cookware your fall kitchen has been waiting for',44));const b=fill(s,body('Three dishes that call for real heat and a surface that won’t let them down. Pure titanium. No coatings to scratch. No toxins.',T.slate,16));s.appendChild(button('Explore titanium cookware'));
  const im=imgBox('product cutout',W,420,T.cream);c.appendChild(im);im.layoutSizingHorizontal='FILL';
  prop(c,e,'Eyebrow','Titanium cookware');prop(c,d,'Headline','The cookware your fall kitchen has been waiting for');prop(c,b,'Body','Three dishes that call for real heat and a surface that won’t let them down. Pure titanium. No coatings to scratch. No toxins.');
});
// 5 Section intro
compo('Text / Section intro','Eyebrow + display 34 + body, gecentreerd, 48px zijmarge.',c=>{
  const s=al('intro','VERTICAL',{pt:28,pb:20,ph:48,gap:12,bg:T.cream,center:true});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const e=fill(s,eyebrow('This week'));const d=fill(s,display('This week’s bestsellers',34));const b=fill(s,body('What 100,000+ home cooks are reaching for right now.',T.slate));
  prop(c,e,'Eyebrow','This week');prop(c,d,'Headline','This week’s bestsellers');prop(c,b,'Body','What 100,000+ home cooks are reaching for right now.');
});
// 6 Split image + text (image left)
for(const [nm,imgLeft] of [['Split / Image left',true],['Split / Image right',false]]){
  compo(nm,'Twee kolommen 300/300: foto + heading, body, tekstlink. Afwisselen links/rechts voor ritme.',c=>{
    const row=al('split','HORIZONTAL',{bg:T.paper,center:true});c.appendChild(row);row.layoutSizingHorizontal='FILL';
    const im=imgBox('detail',300,300,T.sand);
    const col=al('copy','VERTICAL',{ph:32,pv:24,gap:12,w:300});
    const h=fill(col,txt('Pure titanium',SANS_B,20,T.ink,{align:'LEFT',lh:125}));const b=fill(col,body('No coatings to scratch. No toxins. Just high-performance titanium that heats fast and lasts 75 years.',T.slate,14,'LEFT'));const l=fill(col,txt('Learn more →',SANS_B,12,T.brick,{ls:6,upper:true,align:'LEFT'}));
    if(imgLeft){row.appendChild(im);row.appendChild(col);}else{row.appendChild(col);row.appendChild(im);}
    prop(c,h,'Heading','Pure titanium');prop(c,b,'Body','No coatings to scratch. No toxins. Just high-performance titanium that heats fast and lasts 75 years.');prop(c,l,'Link','Learn more →');
  });
}
// 7 Product grid 2 col
compo('Product / Grid 2','Twee productkaarten naast elkaar op crème. Foto 264×264 op sand, naam, prijs (oud doorgestreept), badge optioneel.',c=>{
  const g=al('grid','HORIZONTAL',{ph:24,pv:32,gap:24,bg:T.cream});c.appendChild(g);g.layoutSizingHorizontal='FILL';
  for(const [n,p,o] of [['Titanium Hammered Pan Pro','$149','$299'],['12-Pc Titanium Cookware Set','$699','$1,399']]){
    const card=al('card','VERTICAL',{gap:10,w:264,center:true});g.appendChild(card);
    card.appendChild(imgBox(n,264,264,T.sand));
    fill(card,txt(n,SANS_B,15,T.ink,{lh:130}));
    const pr=al('price','HORIZONTAL',{gap:8,center:true});card.appendChild(pr);hug(pr,txt(p,SANS_B,15,T.brick));hug(pr,txt(o,SANS,13,T.stone,{strike:true}));
    fill(card,txt('Shop now →',SANS_B,12,T.ink,{ls:6,upper:true}));
  }
});
// 8 Product single
compo('Product / Single','Eén product groot: foto 600×440, badge, naam, prijs, body, knop.',c=>{
  const im=imgBox('product',W,440,T.sand);c.appendChild(im);im.layoutSizingHorizontal='FILL';
  const s=al('copy','VERTICAL',{pv:32,ph:48,gap:12,bg:T.cream,center:true});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const badge=al('badge','HORIZONTAL',{pv:6,ph:12,bg:T.brick,radius:2});s.appendChild(badge);hug(badge,txt('402 sold this week',SANS_B,11,T.cream,{ls:6,upper:true}));
  const n=fill(s,display('Titanium Hammered Pan Pro',34));
  const pr=al('price','HORIZONTAL',{gap:10,center:true});s.appendChild(pr);hug(pr,txt('$149',SANS_B,20,T.brick));hug(pr,txt('$299',SANS,16,T.stone,{strike:true}));
  const b=fill(s,body('Hand-hammered titanium, no coating, 75-year warranty. The pan 100,000+ home cooks switched to.',T.slate,15));
  s.appendChild(button('Shop the pan'));
  prop(c,n,'Name','Titanium Hammered Pan Pro');prop(c,b,'Body','Hand-hammered titanium, no coating, 75-year warranty. The pan 100,000+ home cooks switched to.');
});
// 9 Offer / code block
compo('Offer / Code','Kortingsblok: brick-tint vlak, eyebrow, display-bedrag, code in gestippeld kader, vervaldatum, knop.',c=>{
  const s=al('offer','VERTICAL',{pv:40,ph:48,gap:14,bg:T.brickTint,center:true});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const e=fill(s,eyebrow('Your welcome offer'));const d=fill(s,display('10% off your first order',40));
  const code=al('code','HORIZONTAL',{pv:12,ph:24,stroke:T.ink});code.dashPattern=[5,5];s.appendChild(code);const ct=hug(code,txt('HI10',SANS_B,22,T.ink,{ls:10}));
  const x=fill(s,txt('Valid 7 days. One use per customer.',SANS,13,T.slate));s.appendChild(button('Use my code'));
  prop(c,e,'Eyebrow','Your welcome offer');prop(c,d,'Headline','10% off your first order');prop(c,ct,'Code','HI10');prop(c,x,'Expiry','Valid 7 days. One use per customer.');
});
// 10 Review
compo('Proof / Review','Sterren, quote in display 22, naam in caps. Sand kaart met 1px rand.',c=>{
  const wrap=al('wrap','VERTICAL',{pv:32,ph:48,bg:T.cream});c.appendChild(wrap);wrap.layoutSizingHorizontal='FILL';
  const card=al('card','VERTICAL',{pv:28,ph:28,gap:12,bg:T.paper,stroke:T.sand,center:true});wrap.appendChild(card);card.layoutSizingHorizontal='FILL';
  hug(card,txt('★★★★★',SANS,14,T.brick,{ls:20}));
  const q=fill(card,txt('“The pan heats evenly on my stovetop and gives me a better sear without burnt spots.”',DISPLAY,22,T.ink,{lh:130}));
  const a=fill(card,txt('— Ruby H., verified buyer',SANS_B,11,T.slate,{ls:8,upper:true}));
  prop(c,q,'Quote','“The pan heats evenly on my stovetop and gives me a better sear without burnt spots.”');prop(c,a,'Author','— Ruby H., verified buyer');
});
// 11 Numbered list
compo('Text / Numbered list','Drie regels: groot display-cijfer in brick, bold kop, body. Voor "waarom titanium" en objection handling.',c=>{
  const s=al('list','VERTICAL',{pv:40,ph:48,gap:20,bg:T.paper});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const items=[['No coating to flake','Pure titanium. Nothing to peel, chip or end up in your food.'],['75-year warranty','Not 1 to 2 years. Replace it once in your life, if ever.'],['Metal utensils welcome','Scrape, stir, sear. No special sponge, no babying.']];
  items.forEach(([h,b],i)=>{const row=al('item','HORIZONTAL',{gap:20});s.appendChild(row);row.layoutSizingHorizontal='FILL';hug(row,txt('0'+(i+1),DISPLAY,36,T.brick,{lh:100}));const col=al('copy','VERTICAL',{gap:4});row.appendChild(col);col.layoutSizingHorizontal='FILL';fill(col,txt(h,SANS_B,16,T.ink,{align:'LEFT',lh:130}));fill(col,body(b,T.slate,14,'LEFT'));if(i<2){const ln=figma.createRectangle();ln.resize(504,1);ln.fills=[{type:'SOLID',color:hex(T.sand)}];s.appendChild(ln);ln.layoutSizingHorizontal='FILL';}});
});
// 12 Comparison
compo('Proof / Comparison','Twee kolommen: Siraat titanium vs coated nonstick, vinkjes en kruisjes.',c=>{
  const s=al('cmp','VERTICAL',{pv:40,ph:48,gap:0,bg:T.cream});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const head=al('head','HORIZONTAL',{pv:12});s.appendChild(head);head.layoutSizingHorizontal='FILL';
  fill(head,txt('',SANS,13,T.ink,{align:'LEFT'}));fill(head,txt('Siraat titanium',SANS_B,12,T.brick,{ls:6,upper:true}));fill(head,txt('Coated nonstick',SANS_B,12,T.slate,{ls:6,upper:true}));
  for(const [f,a,b] of [['No PFAS or coating','✓','✗'],['Metal utensil safe','✓','✗'],['Dishwasher safe','✓','✗'],['Warranty','75 yrs','1 to 2 yrs'],['Lasts a lifetime','✓','✗']]){
    const ln=figma.createRectangle();ln.resize(504,1);ln.fills=[{type:'SOLID',color:hex(T.sand)}];s.appendChild(ln);ln.layoutSizingHorizontal='FILL';
    const row=al('row','HORIZONTAL',{pv:12,center:true});s.appendChild(row);row.layoutSizingHorizontal='FILL';
    fill(row,txt(f,SANS,14,T.ink,{align:'LEFT'}));fill(row,txt(a,SANS_B,15,T.success));fill(row,txt(b,SANS_B,15,T.stone));
  }
});
// 13 Trust bar
compo('Bars / Trust','Vier claims op antraciet. Verplicht in elke flow-mail boven de footer.',c=>{
  const s=al('trust','HORIZONTAL',{pv:28,ph:24,gap:8,bg:T.charcoal});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  for(const [big,small] of [['100K+','customers'],['75-year','warranty'],['PFAS-free','lab tested'],['100-day','home trial']]){const cell=al('cell','VERTICAL',{gap:4,center:true});s.appendChild(cell);cell.layoutSizingHorizontal='FILL';fill(cell,txt(big,SANS_B,22,T.cream,{lh:120}));fill(cell,txt(small,SANS_B,10,T.titanium,{ls:10,upper:true}));}
});
// 14 Dark story block
compo('Text / Dark story','Espresso blok: eyebrow titanium, display 40 crème, body, on-dark knop. Max 1 per 3 secties.',c=>{
  const s=al('story','VERTICAL',{pv:56,ph:48,gap:18,bg:T.espresso,center:true});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const e=fill(s,eyebrow('Why titanium',T.titanium));const d=fill(s,display('Hand-Wash Only? Not Here.',40,T.cream));const b=fill(s,body('The only thing you need to remember is to unload the dishwasher tomorrow.',T.titanium,16));s.appendChild(button('Shop the pan','ondark'));
  prop(c,e,'Eyebrow','Why titanium');prop(c,d,'Headline','Hand-Wash Only? Not Here.');prop(c,b,'Body','The only thing you need to remember is to unload the dishwasher tomorrow.');
});
// 15 Image full width
compo('Image / Full width','Enkele foto 600×400, optioneel caption. Voor recepten en lifestyle tussen tekstblokken.',c=>{
  const im=imgBox('lifestyle',W,400,T.sand);c.appendChild(im);im.layoutSizingHorizontal='FILL';
});
// 16 Image + caption grid 3
compo('Image / Grid 3','Drie foto’s 184×184 met caption. Voor recepten ("What we’re cooking") en UGC.',c=>{
  const g=al('grid','HORIZONTAL',{ph:16,pv:24,gap:8,bg:T.paper});c.appendChild(g);g.layoutSizingHorizontal='FILL';
  for(const n of ['Pasta night','Root veg roast','Sunday soup']){const col=al('cell','VERTICAL',{gap:8,center:true,w:184});g.appendChild(col);col.appendChild(imgBox(n,184,184,T.sand));fill(col,txt(n,SANS_B,12,T.ink,{ls:4,upper:true}));}
});
// 17 Founder note
compo('Text / Founder note','Persoonlijke brief: links uitgelijnd, 16px, handtekening. Voor "Benjamin" mails.',c=>{
  const s=al('note','VERTICAL',{pv:40,ph:56,gap:16,bg:T.paper});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  fill(s,txt('Hi there,',SANS,16,T.ink,{align:'LEFT'}));
  const b=fill(s,body('We spent years making a pan with nothing in it that could hurt you. No PFAS. No coating to flake into your children’s food. Then I walked into my own kitchen and looked under the sink.',T.ink,16,'LEFT'));
  fill(s,txt('Benjamin\nCo-founder, Siraat’s Kitchen',DISPLAY,20,T.ink,{align:'LEFT',lh:130}));
  prop(c,b,'Body','We spent years making a pan with nothing in it that could hurt you. No PFAS. No coating to flake into your children’s food. Then I walked into my own kitchen and looked under the sink.');
});
// 18 Footer
compo('Footer / Built for Life','Antraciet footer: monogram + Built for Life, nav-regels met pijl, social, legal. Verplicht onderaan elke mail.',c=>{
  const s=al('footer','VERTICAL',{pt:40,pb:0,gap:0,bg:T.charcoal});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const top=al('brand','HORIZONTAL',{ph:40,pb:28,gap:18,center:true});s.appendChild(top);top.appendChild(svgNode(LOGO_SVG,64,'monogram',T.cream));
  const tcol=al('tag','VERTICAL',{gap:2});top.appendChild(tcol);hug(tcol,txt('Built for Life',DISPLAY,30,T.cream,{align:'LEFT',lh:110}));hug(tcol,txt('Non-Toxic Cookware',SANS,13,T.titanium,{align:'LEFT'}));
  for(const n of ['Titanium cookware','Bundles & sets','Accessories','About us']){const ln=figma.createRectangle();ln.resize(W,1);ln.fills=[{type:'SOLID',color:{r:0.3,g:0.29,b:0.29}}];s.appendChild(ln);ln.layoutSizingHorizontal='FILL';const row=al('nav','HORIZONTAL',{pv:16,ph:40,center:true});s.appendChild(row);row.layoutSizingHorizontal='FILL';fill(row,txt(n,SANS_B,12,T.cream,{ls:10,upper:true,align:'LEFT'}));hug(row,txt('→',SANS_B,14,T.cream));}
  const soc=al('social','HORIZONTAL',{pv:28,gap:20,center:true,main:'CENTER'});s.appendChild(soc);soc.layoutSizingHorizontal='FILL';soc.appendChild(svgNode(FB_SVG,28,'facebook',null));soc.appendChild(svgNode(IG_SVG,28,'instagram',null));
  const legal=al('legal','VERTICAL',{pv:20,ph:40,gap:6,bg:'#272727',center:true});s.appendChild(legal);legal.layoutSizingHorizontal='FILL';
  fill(legal,txt('Privacy policy  ·  Terms of service  ·  Manage preferences  ·  Unsubscribe',SANS_L,11,T.titanium));
  fill(legal,txt('© 2026 Siraat’s Kitchen  ·  1305 Collins Ave, Miami Beach, FL 33139',SANS_L,11,T.stone));
});
// 19 Divider
compo('Spacer / 40','Lege ruimte 40px op crème.',c=>{const s=al('sp','VERTICAL',{pv:20,bg:T.cream});c.appendChild(s);s.layoutSizingHorizontal='FILL';});


// 20 Star rating rows
compo('Proof / Star rating rows','Vijf klikbare rijen (5 t/m 1 ster) op een witte kaart. Elke rij linkt naar de reviewpagina met score.',c=>{
  const wrap=al('wrap','VERTICAL',{pv:8,ph:48,pb:40,gap:16,bg:T.cream,center:true});c.appendChild(wrap);wrap.layoutSizingHorizontal='FILL';
  const card=al('card','VERTICAL',{bg:T.paper,stroke:T.sand,radius:2});wrap.appendChild(card);card.layoutSizingHorizontal='FILL';
  for(let n=5;n>=1;n--){const row=al('row '+n,'HORIZONTAL',{pv:18,gap:10,center:true,main:'CENTER'});card.appendChild(row);row.layoutSizingHorizontal='FILL';for(let i=0;i<n;i++){const st=figma.createStar();st.resize(30,30);st.innerRadius=0.48;st.fills=[{type:'SOLID',color:hex(T.brick)}];row.appendChild(st);}if(n>1){const ln=figma.createRectangle();ln.resize(500,1);ln.fills=[{type:'SOLID',color:hex(T.sand)}];card.appendChild(ln);ln.layoutSizingHorizontal='FILL';}}
  const cap=fill(wrap,txt('Tap the stars that match your experience',SANS,13,T.slate));prop(c,cap,'Caption','Tap the stars that match your experience');
});
// 21 Steps
compo('Text / Steps','Drie stappen, gecentreerd, groot display-cijfer boven de tekst. Tekst-properties per stap.',c=>{
  const s=al('steps','VERTICAL',{pt:12,pb:44,ph:56,gap:28,bg:T.cream,center:true});c.appendChild(s);s.layoutSizingHorizontal='FILL';
  const defs=['Tap the star below that matches your experience.','Say what you honestly think. Two minutes, good or bad.','Every month, one reviewer wins their full purchase amount back, drawn at random.'];
  defs.forEach((d,i)=>{const row=al('step','VERTICAL',{gap:8,center:true});s.appendChild(row);row.layoutSizingHorizontal='FILL';hug(row,txt(String(i+1)+'.',DISPLAY,40,T.brick,{lh:100}));const t=fill(row,txt(d,SANS,16,T.ink,{lh:150}));prop(c,t,'Step '+(i+1),d);});
});
// layout on page: 3 columns
let colH=[0,0,0];
made.forEach((c,i)=>{const col=i%3;c.x=col*COLW;c.y=colH[col];colH[col]+=c.height+ROW_GAP;});
const sec=figma.createSection();sec.name='Components';page.appendChild(sec);
for(const c of made) sec.appendChild(c);
sec.resizeWithoutConstraints(COLW*3,Math.max(...colH)+40);
figma.viewport.scrollAndZoomIntoView([sec]);
return {page:page.id,section:sec.id,components:made.map(c=>[c.name,c.id,Math.round(c.height)]),display:DISPLAY?DISPLAY.family:null};
