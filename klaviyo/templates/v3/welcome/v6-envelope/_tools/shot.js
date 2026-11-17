// PNG op 600 en 390 px (DSF 2) per mail, plus check kapotte beelden, overloop en gedachtestreepjes. node _tools/shot.js
const { chromium } = require('/opt/node-tools/node_modules/playwright');const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const id of ['e1','e2','e3','e4','e5']){const f=path.resolve(__dirname,'../'+id+'-preview.html');
for(const w of [600,390]){const p=await b.newPage({viewport:{width:w,height:900},deviceScaleFactor:2});
 await p.goto('file://'+f,{waitUntil:'networkidle',timeout:60000}).catch(()=>{});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
 const r=await p.evaluate(()=>{const W=document.documentElement.clientWidth;return{broken:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src.slice(0,80)),sw:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight,
  wide:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>W+1).slice(0,5).map(e=>e.tagName+'.'+e.className),dash:document.body.innerText.includes('—')}});
 await p.screenshot({path:path.resolve(__dirname,'../renders/'+id+'-'+w+'.png'),fullPage:true});
 console.log(id,w,'h',r.h,'overflow',r.sw>w?r.sw:'no',JSON.stringify(r.wide),'broken',r.broken.length?r.broken:0,'emdash',r.dash);await p.close();}}
await b.close();})();
