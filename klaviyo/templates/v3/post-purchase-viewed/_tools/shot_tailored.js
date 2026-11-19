// PNG op 600 en 390 px (DSF 2) van alle previews; check kapotte beelden, overloop, gedachtestreepjes. node _tools/shot.js
const { chromium } = require('/opt/node-tools/node_modules/playwright');const path=require('path');const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const D=path.resolve(__dirname,'../tailored');
for(const f of fs.readdirSync(D).filter(x=>/^s[0-9]+\.html$/.test(x))){
for(const w of [600,390]){const p=await b.newPage({viewport:{width:w,height:900},deviceScaleFactor:2});
 await p.goto('file://'+path.join(D,f),{waitUntil:'networkidle',timeout:60000}).catch(()=>{});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
 const r=await p.evaluate(()=>{const W=document.documentElement.clientWidth;return{broken:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src.slice(0,80)),sw:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight,
  wide:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>W+1).slice(0,5).map(e=>e.tagName+'.'+e.className),dash:document.body.innerText.includes('—'),leftover:/[{}]{2}|\{%|#\s*Your/.test(document.body.innerText)}});
 await p.screenshot({path:path.join(D,'renders',f.replace('.html','')+'-'+w+'.png'),fullPage:true});
 console.log(f,w,'h',r.h,'overflow',r.sw>w?r.sw:'no',r.wide,'broken',r.broken.length?r.broken:0,'emdash',r.dash,'leftover',r.leftover);await p.close();}}
await b.close();})();
