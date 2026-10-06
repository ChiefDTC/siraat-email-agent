// Siraat email design system: Foundations page + variables. Run via Figma MCP use_figma.
const T = {
  cream:'#F8F7F2', paper:'#FFFFFF', sand:'#ECE7DD', stone:'#9A948B', slate:'#727272',
  ink:'#282828', charcoal:'#2B2929', espresso:'#321E1D', black:'#111111', brick:'#AC3B19', brickDark:'#8A2D12', brickTint:'#F3E3DC',
  titanium:'#C9C6C0', success:'#3D6B4F'
};
function hex(h){const n=parseInt(h.slice(1),16);return {r:((n>>16)&255)/255,g:((n>>8)&255)/255,b:(n&255)/255};}
const DISPLAY=[{family:'TT Ramillas',style:'Light Italic'},{family:'TT Ramillas Trl',style:'Light Italic'},{family:'Instrument Serif',style:'Italic'},{family:'Playfair Display',style:'Italic'}];
const SANS={family:'Inter',style:'Regular'}, SANS_B={family:'Inter',style:'Semi Bold'}, SANS_L={family:'Inter',style:'Light'};
let display=null;
for(const f of DISPLAY){try{await figma.loadFontAsync(f);display=f;break;}catch(e){}}
await figma.loadFontAsync(SANS);await figma.loadFontAsync(SANS_B);await figma.loadFontAsync(SANS_L);

// page
let page=figma.root.children.find(p=>p.name==='00 Foundations');
if(!page){page=figma.createPage();page.name='00 Foundations';}
await figma.setCurrentPageAsync(page);
for(const c of [...page.children]) c.remove();

// variables
const cols=await figma.variables.getLocalVariableCollectionsAsync();
let col=cols.find(c=>c.name==='Email tokens');
if(!col){col=figma.variables.createVariableCollection('Email tokens');}
const mode=col.modes[0].modeId;
const existing=await figma.variables.getLocalVariablesAsync('COLOR');
const vars={};
for(const [k,v] of Object.entries(T)){
  let vr=existing.find(x=>x.name==='color/'+k && x.variableCollectionId===col.id);
  if(!vr) vr=figma.variables.createVariable('color/'+k,col,'COLOR');
  vr.setValueForMode(mode,{...hex(v),a:1}); vars[k]=vr;
}
const existingF=await figma.variables.getLocalVariablesAsync('FLOAT');
const SP={xs:8,s:16,m:24,l:32,xl:48,xxl:64};
for(const [k,v] of Object.entries(SP)){
  let vr=existingF.find(x=>x.name==='space/'+k && x.variableCollectionId===col.id);
  if(!vr) vr=figma.variables.createVariable('space/'+k,col,'FLOAT');
  vr.setValueForMode(mode,v);
}

// helpers
function frame(name,w,dir,gap,pad){const f=figma.createFrame();f.name=name;f.layoutMode=dir;f.itemSpacing=gap;f.paddingTop=f.paddingBottom=f.paddingLeft=f.paddingRight=pad;if(w){f.resize(w,10);f.counterAxisSizingMode='FIXED';}else{f.counterAxisSizingMode='AUTO';}f.primaryAxisSizingMode='AUTO';f.clipsContent=false;f.fills=[];return f;}
function text(s,font,size,color,opts={}){const t=figma.createText();t.fontName=font;t.characters=s;t.fontSize=size;t.fills=[{type:'SOLID',color:hex(color)}];if(opts.ls)t.letterSpacing={unit:'PERCENT',value:opts.ls};if(opts.lh)t.lineHeight={unit:'PERCENT',value:opts.lh};if(opts.upper)t.textCase='UPPER';if(opts.w){t.textAutoResize='HEIGHT';t.resize(opts.w,10);}return t;}

const root=frame('Foundations',null,'VERTICAL',64,80); root.fills=[{type:'SOLID',color:hex(T.paper)}];
root.appendChild(text('Siraat’s Kitchen · Email design system',SANS_B,14,T.slate,{ls:8,upper:true}));
root.appendChild(text('Foundations',display,64,T.ink));
root.appendChild(text('Basis: de verzonden Homestead-campagnes (crème, baksteenrood, antraciet) met meer contrast, grotere koppen en meer fotografie. 600px breed, image-slice export via Email Love plugin.',SANS,16,T.slate,{w:720,lh:150}));

// colours
const cSec=frame('Colour',null,'VERTICAL',16,0);
cSec.appendChild(text('01  Colour',SANS_B,12,T.slate,{ls:8,upper:true}));
const groups=[['Surfaces',['cream','paper','sand','charcoal','espresso','black']],['Text',['ink','slate','stone','titanium']],['Accent',['brick','brickDark','brickTint','success']]];
for(const [g,keys] of groups){
  const row=frame(g,null,'HORIZONTAL',16,0);
  row.appendChild(text(g,SANS,13,T.ink,{w:90}));
  for(const k of keys){
    const sw=frame('swatch/'+k,160,'VERTICAL',8,0);
    const box=figma.createRectangle();box.resize(160,96);box.cornerRadius=4;box.fills=[figma.variables.setBoundVariableForPaint({type:'SOLID',color:hex(T[k])},'color',vars[k])];
    if(['cream','paper'].includes(k)){box.strokes=[{type:'SOLID',color:hex(T.sand)}];box.strokeWeight=1;}
    sw.appendChild(box);sw.appendChild(text(k,SANS_B,13,T.ink));sw.appendChild(text(T[k],SANS,12,T.slate));
    row.appendChild(sw);
  }
  cSec.appendChild(row);
}
root.appendChild(cSec);

// contrast pairs
const pSec=frame('Contrast pairs',null,'VERTICAL',16,0);
pSec.appendChild(text('02  Toegestane combinaties (WCAG AA op 16px)',SANS_B,12,T.slate,{ls:8,upper:true}));
const pairs=[['cream','ink','Ink on cream  ·  13.9:1'],['charcoal','cream','Cream on charcoal  ·  13.2:1'],['brick','cream','Cream on brick  ·  6.4:1'],['cream','brick','Brick on cream  ·  6.4:1'],['sand','ink','Ink on sand  ·  12.1:1'],['black','titanium','Titanium on black  ·  10.2:1']];
const prow=frame('pairs',null,'HORIZONTAL',16,0);
for(const [bg,fg,label] of pairs){
  const f=frame(label,220,'VERTICAL',6,20);f.fills=[{type:'SOLID',color:hex(T[bg])}];f.cornerRadius=4;
  if(bg==='cream'){f.strokes=[{type:'SOLID',color:hex(T.sand)}];f.strokeWeight=1;}
  f.appendChild(text('Aa',display,40,T[fg]));f.appendChild(text(label,SANS,12,T[fg]));prow.appendChild(f);
}
pSec.appendChild(prow);root.appendChild(pSec);

// typography
const tSec=frame('Typography',null,'VERTICAL',24,0);
tSec.appendChild(text('03  Typography  ·  '+(display?display.family+' '+display.style:'(geen display font)')+' + Inter',SANS_B,12,T.slate,{ls:8,upper:true}));
const scale=[['Display XL',display,56,T.ink,'Hand-hammered titanium.',{lh:105}],['Display L',display,44,T.ink,'The cookware your fall kitchen has been waiting for',{lh:108}],['Display M',display,34,T.ink,'This week’s bestsellers',{lh:112}],['Heading',SANS_B,22,T.ink,'Inside every roaster',{}],['Eyebrow',SANS_B,12,T.brick,'Warehouse clearance sale  ·  up to 50% off',{ls:12,upper:true}],['Body L',SANS,18,T.ink,'No coatings to scratch. No toxins. Just pure titanium, hand-hammered and backed by a 75-year warranty.',{lh:150,w:560}],['Body',SANS,16,T.ink,'Every year the same question comes up: what do you get someone who cooks? Sign up for SMS alerts and be the first to see our holiday recommendations.',{lh:155,w:560}],['Caption',SANS,13,T.slate,'Warehouse Clearance Sale runs while supplies last.',{lh:150}],['Legal',SANS_L,11,T.stone,'© 2026 Siraat’s Kitchen · 1305 Collins Ave, Miami Beach, FL 33139 · Unsubscribe · Manage preferences',{lh:150}]];
for(const [n,f,s,c,sample,o] of scale){
  const row=frame(n,null,'HORIZONTAL',24,0);row.counterAxisAlignItems='MIN';
  row.appendChild(text(n+'  '+s+'px',SANS,12,T.slate,{w:140}));
  row.appendChild(text(sample,f,s,c,o));tSec.appendChild(row);
}
root.appendChild(tSec);

// spacing
const sSec=frame('Spacing',null,'VERTICAL',16,0);
sSec.appendChild(text('04  Spacing  ·  8px basis, 600px canvas, 40px zijmarge in tekstblokken',SANS_B,12,T.slate,{ls:8,upper:true}));
const srow=frame('spacing',null,'HORIZONTAL',24,0);srow.counterAxisAlignItems='MAX';
for(const [k,v] of Object.entries(SP)){const f=frame('space/'+k,null,'VERTICAL',8,0);f.counterAxisAlignItems='CENTER';const r=figma.createRectangle();r.resize(v,v);r.fills=[{type:'SOLID',color:hex(T.brick)}];f.appendChild(r);f.appendChild(text(k+' · '+v,SANS,12,T.slate));srow.appendChild(f);}
sSec.appendChild(srow);root.appendChild(sSec);

// buttons
const bSec=frame('Buttons',null,'VERTICAL',16,0);
bSec.appendChild(text('05  Buttons  ·  Inter Semi Bold 13, +8% tracking, uppercase, 16/32 padding, radius 2',SANS_B,12,T.slate,{ls:8,upper:true}));
const brow=frame('buttons',null,'HORIZONTAL',24,0);
const bdefs=[['Primary',T.brick,T.cream,null,T.cream],['Secondary',null,T.ink,T.ink,T.cream],['On dark',T.cream,T.ink,null,T.charcoal],['On dark outline',null,T.cream,T.cream,T.charcoal],['Text link',null,T.brick,null,T.cream]];
for(const [n,bg,fg,stroke,surface] of bdefs){
  const wrap=frame(n,null,'VERTICAL',8,24);wrap.fills=[{type:'SOLID',color:hex(surface)}];wrap.counterAxisAlignItems='CENTER';
  const b=frame('btn/'+n,null,'HORIZONTAL',0,0);b.paddingTop=b.paddingBottom=16;b.paddingLeft=b.paddingRight=32;b.cornerRadius=2;
  if(bg)b.fills=[{type:'SOLID',color:hex(bg)}];if(stroke){b.strokes=[{type:'SOLID',color:hex(stroke)}];b.strokeWeight=1.5;}
  const lbl=text('Shop the sale',SANS_B,13,fg,{ls:8,upper:true});if(n==='Text link'){lbl.textDecoration='UNDERLINE';b.paddingLeft=b.paddingRight=0;}
  b.appendChild(lbl);wrap.appendChild(b);wrap.appendChild(text(n,SANS,12,surface===T.charcoal?T.titanium:T.slate));brow.appendChild(wrap);
}
bSec.appendChild(brow);root.appendChild(bSec);

// rules
const rSec=frame('Rules',null,'VERTICAL',8,0);
rSec.appendChild(text('06  Regels',SANS_B,12,T.slate,{ls:8,upper:true}));
for(const r of ['Elke mail opent met een foto of een crème hero met display-kop van minimaal 44px. Nooit een tekstblok als eerste scherm.','Crème is de basis. Antraciet en baksteenrood zijn secties, niet de hele mail. Maximaal 1 donker blok per 3 secties.','Baksteenrood alleen voor knoppen, eyebrows, kortingsbars en 1 accentwoord. Nooit als tekstkleur in body.','Display-font altijd italic, nooit uppercase. Inter Semi Bold uppercase +8% voor eyebrows, knoppen en navigatie.','Productfoto’s vrijstaand op crème of sand, lifestyle full-bleed 600px breed. Geen afbeeldingen smaller dan 280px in een 2-koloms grid.','Trust bar (100K+ customers, 75-year warranty, tested PFAS-free, 100-day trial) staat in elke flow-mail boven de footer.','Footer is altijd het antraciet “Built for Life” blok met monogram, navigatie, social en legal in Inter Light 11.']){
  rSec.appendChild(text('—  '+r,SANS,14,T.ink,{w:900,lh:150}));
}
root.appendChild(rSec);
figma.viewport.scrollAndZoomIntoView([root]);
return {page:page.id,root:root.id,display:display?display.family:null,vars:Object.keys(vars).length};
