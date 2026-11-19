// BF-W1 image B: PNG op 600 en 390 px (DSF 2); check kapotte beelden, overloop, em dash; beeldaandeel = beeldhoogte / mailhoogte (zonder footer). node _tools/shot.js
const { chromium } = require('/opt/node-tools/node_modules/playwright');const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const id of ['preview-us','preview-int']){const f=path.resolve(__dirname,'../'+id+'.html');
for(const w of [600,390]){const p=await b.newPage({viewport:{width:w,height:900},deviceScaleFactor:2});
 await p.goto('file://'+f,{waitUntil:'networkidle',timeout:90000}).catch(()=>{});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
 const r=await p.evaluate(()=>{const W=document.documentElement.clientWidth;const imgs=[...document.images];
  const sec=imgs.filter(i=>i.getBoundingClientRect().width>=W*0.4);
  const main=document.querySelector('table.w').getBoundingClientRect();
  const foot=[...document.querySelectorAll('td')].find(t=>t.getAttribute('bgcolor')==='#282828'&&t.innerText.includes('NON-TOXIC'));
  const end=foot?foot.getBoundingClientRect().top:main.bottom;
  const ih=sec.filter(i=>i.getBoundingClientRect().top<end).reduce((a,i)=>a+i.getBoundingClientRect().height*(i.getBoundingClientRect().width>=W*0.8?1:i.getBoundingClientRect().width/main.width),0);
  return{broken:imgs.filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src.slice(0,80)),sw:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight,
  wide:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>W+1).slice(0,5).map(e=>e.tagName+'.'+e.className),dash:document.body.innerText.includes('—'),share:Math.round(100*ih/(end-main.top))}});
 await p.screenshot({path:path.resolve(__dirname,'../renders/'+id+'-'+w+'.png'),fullPage:true});
 console.log(id,w,'h',r.h,'overflow',r.sw>w?r.sw:'no',JSON.stringify(r.wide),'broken',r.broken.length?r.broken:0,'emdash',r.dash,'img%',r.share);await p.close();}}
await b.close();})();
