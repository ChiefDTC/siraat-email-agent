// Gifts: screenshots 375 en 600 (2x), plus check op kapotte beelden en horizontale overloop. Gebruik: node shot_roast.js <uitmap> <previewmap> [regex]
const { chromium } = require('/opt/node-tools/node_modules/playwright');const fs=require('fs'),path=require('path');
(async()=>{const [dir,out,re]=process.argv.slice(2);const rx=new RegExp(re||'^gifts-.*-preview\\.html$');const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const f of fs.readdirSync(dir).filter(f=>rx.test(f))){
 for(const w of [375,600]){const p=await b.newPage({viewport:{width:w,height:800},deviceScaleFactor:2});
  await p.goto('file://'+path.resolve(dir,f),{waitUntil:'networkidle',timeout:60000}).catch(()=>{});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
  const r=await p.evaluate(()=>({broken:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.slice(0,90)),sw:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight}));
  const name=f.replace('-preview.html','')+'-'+w+'.png';await p.screenshot({path:path.join(out,name),fullPage:true});
  console.log(name,'h',r.h,'overflow',r.sw>w?r.sw:'no','broken',r.broken.length?r.broken:'0');await p.close();}}
await b.close();})();
