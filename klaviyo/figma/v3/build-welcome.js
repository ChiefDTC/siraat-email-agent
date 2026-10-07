const SPEC={"title": "Welcome", "sub": "Vervangt SiaNLu en Failure to launch T2SmtR. Baseline: $2,53 per nieuwe inschrijver.", "trigger": ["Toegevoegd aan lijst Uw8eZG (Alia Card Game, kans op order refund)", "E-mail bevat niet test@", "Nooit eerder in deze flow", "Smart sending uit, quiet hours 21-08"], "lane": {"after": 0, "label": "Split A \u00b7 Placed Order > 0 ooit? JA = klant", "items": [{"t": "delay", "v": "10 min"}, {"t": "email", "id": "w0"}, {"t": "end", "v": "Einde, post-purchase neemt over"}]}, "seq": [{"t": "split", "v": "Split A \u00b7 Placed Order > 0 ooit?", "note": "Nee = prospect (dit pad). Ja = klant (pad onder)."}, {"t": "delay", "v": "10 min"}, {"t": "split", "v": "A/B-test W1: HI10 als code of als gift card", "rows": [["A \u00b7 code", "w1-a"], ["B \u00b7 gift card", "w1-b"]]}, {"t": "delay", "v": "tot dag 1, 10:00"}, {"t": "email", "id": "w2"}, {"t": "delay", "v": "tot dag 3, 10:00"}, {"t": "email", "id": "w3"}, {"t": "delay", "v": "tot dag 6, 10:00"}, {"t": "split", "v": "Split B \u00b7 Land = United States?", "rows": [["Ja \u00b7 US", "w4-us"], ["Nee \u00b7 internationaal", "w4-int"]]}, {"t": "delay", "v": "tot dag 9, 10:00"}, {"t": "email", "id": "w5"}, {"t": "end", "v": "Einde dag 10. Naar campagnes."}]}; const KEY="welcome"; const PAGEID="";
let page;
if(PAGEID){page=await figma.getNodeByIdAsync(PAGEID);}else{page=figma.root.children.find(p=>p.name===SPEC.title)||figma.createPage();page.name=SPEC.title;}
await figma.setCurrentPageAsync(page);
for(const c of [...page.children]) c.remove();
for(const f of [{family:"Inter",style:"Regular"},{family:"Inter",style:"Semi Bold"},{family:"Inter",style:"Bold"},{family:"Instrument Serif",style:"Italic"}]) await figma.loadFontAsync(f);
const C={ink:{r:.157,g:.157,b:.157},cream:{r:.973,g:.969,b:.949},sand:{r:.925,g:.906,b:.867},brick:{r:.675,g:.231,b:.098},grey:{r:.447,g:.447,b:.447},white:{r:1,g:1,b:1},blue:{r:.17,g:.33,b:.62},green:{r:.18,g:.42,b:.25},amber:{r:.80,g:.55,b:.10},esp:{r:.196,g:.118,b:.114}};
const S=c=>[{type:'SOLID',color:c}];
function T(s,size,style,color,w,fam){const t=figma.createText();t.fontName={family:fam||"Inter",style:style||"Regular"};t.characters=s;t.fontSize=size;t.fills=S(color||C.ink);t.lineHeight={unit:'PERCENT',value:135};if(w){t.resize(w,10);t.textAutoResize='HEIGHT';}return t;}
function card(name,title,lines,w,stroke,fill,titleColor){const f=figma.createAutoLayout('VERTICAL',{name,itemSpacing:6,paddingTop:14,paddingBottom:14,paddingLeft:16,paddingRight:16});f.fills=S(fill||C.white);f.strokes=S(stroke||C.sand);f.strokeWeight=2;f.cornerRadius=10;f.resize(w,10);f.primaryAxisSizingMode='AUTO';f.counterAxisSizingMode='FIXED';f.appendChild(T(title,15,'Bold',titleColor||C.ink,w-32));for(const l of (lines||[]))f.appendChild(T(l,12,'Regular',C.grey,w-32));page.appendChild(f);return f;}
function line(x1,y1,x2,y2,col){const v=figma.createVector();v.vectorPaths=[{windingRule:'NONE',data:`M ${x1} ${y1} L ${x2} ${y2}`}];v.strokes=S(col||C.grey);v.strokeWeight=3;page.appendChild(v);return v;}
const out={emails:{}};
const TOP=260, ROWH=2350, EW=380, DW=230, SW=300, GAP=50;
const title=T(SPEC.title,64,'Italic',C.ink,null,'Instrument Serif');title.x=0;title.y=0;page.appendChild(title);
const sub=T(SPEC.sub,18,'Regular',C.grey,1600);sub.x=0;sub.y=90;page.appendChild(sub);
const leg=T("Legenda: zwart = trigger · grijs = wachttijd · blauw = split · bruinrood = mail · groen = einde. Onder elke mail staat de volledige mail op desktop.",14,'Regular',C.grey,1600);leg.x=0;leg.y=130;page.appendChild(leg);
let x=0; let rows=1;
function emailNode(id,X,Y){const c=card('NODE '+id,id.toUpperCase(),['(onderwerp volgt)'],EW,C.brick,C.white,C.brick);c.x=X;c.y=Y;const f=figma.createFrame();f.name='EMAIL '+id;f.resize(360,1900);f.fills=S(C.sand);f.x=X+10;f.y=Y+170;page.appendChild(f);out.emails[id]={card:c.id,frame:f.id};return c;}
function seqRun(items,startX,Y){let X=startX;let prevRight=null;let prevRows=1;
 for(const it of items){let w=0;
  if(prevRight!==null){line(prevRight,Y+40,X,Y+40);for(let r=1;r<prevRows;r++){const mx=prevRight+GAP/2;line(prevRight,Y+r*ROWH+40,mx,Y+r*ROWH+40,C.blue);line(mx,Y+r*ROWH+40,mx,Y+40,C.blue);}}
  prevRows=1;
  if(it.t==='delay'){const c=card('DELAY',"⏱ "+it.v,[],DW,C.sand,C.cream);c.x=X;c.y=Y;w=DW;}
  else if(it.t==='email'){emailNode(it.id,X,Y);w=EW;}
  else if(it.t==='split'){const c=card('SPLIT',"◆ "+it.v,it.note?[it.note]:(it.rows?it.rows.map(r=>r[0]):[]),SW,C.blue,C.white,C.blue);c.x=X;c.y=Y;w=SW;
    if(it.rows){const sx=X+SW;X+=SW+GAP;let r=0;for(const [lab,id] of it.rows){const L=T(lab,13,'Semi Bold',C.blue,EW);L.x=X;L.y=Y+r*ROWH-26;page.appendChild(L);emailNode(id,X,Y+r*ROWH);
        if(r===0){line(sx,Y+40,X,Y+40,C.blue);}else{line(sx-SW/2,Y+120,sx-SW/2,Y+r*ROWH+40,C.blue);line(sx-SW/2,Y+r*ROWH+40,X,Y+r*ROWH+40,C.blue);}r++;}
      prevRows=it.rows.length;prevRight=X+EW;X+=EW+GAP;continue;}}
  else if(it.t==='note'){const c=card('NOTE',it.v,[],EW,C.amber,C.white);c.x=X;c.y=Y;w=EW;}
  else if(it.t==='end'){const c=card('END',"■ "+it.v,[],DW,C.green,C.white,C.green);c.x=X;c.y=Y;w=DW;}
  prevRight=X+w;X+=w+GAP;}
 return {X};}
const trig=card('TRIGGER',"⚡ TRIGGER",SPEC.trigger,340,C.ink,C.white);trig.x=0;trig.y=TOP;
let res=seqRun(SPEC.seq,340+GAP,TOP);
line(340,TOP+40,340+GAP,TOP+40);
if(SPEC.lane){const LY=TOP+2*ROWH+200;const lab=T(SPEC.lane.label,16,'Bold',C.blue,1200);lab.x=340+GAP;lab.y=LY-40;page.appendChild(lab);line(340+GAP+SW/2,TOP+120,340+GAP+SW/2,LY,C.blue);seqRun(SPEC.lane.items,340+GAP,LY);}
out.page=page.id;return out;
