// Screenshots 375 en 600 (2x), check op kapotte beelden, horizontale overloop en klikbaarheid (elk beeld in een link). Gebruik: node shot_redeem.js <uitmap> <previewmap>
const { chromium } = require('/opt/node-tools/node_modules/playwright');const fs=require('fs'),path=require('path');
(async()=>{const [dir,out]=process.argv.slice(2);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const f of fs.readdirSync(dir).filter(f=>/^r[12]-(checkout|cart)(-withcode)?\.html$/.test(f))){
 for(const w of [375,600]){const p=await b.newPage({viewport:{width:w,height:800},deviceScaleFactor:2});
  await p.goto('file://'+path.resolve(dir,f),{waitUntil:'networkidle'}).catch(()=>{});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
  const r=await p.evaluate(()=>({broken:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.slice(0,90)),unlinked:[...document.images].filter(i=>i.width>1&&!i.closest('a')).map(i=>i.src.slice(-40)),bg:[...document.querySelectorAll('td[background]')].filter(t=>!t.querySelector('a')).length,sw:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight}));
  const name=f.replace('.html','')+'-'+w+'.png';await p.screenshot({path:path.join(out,name),fullPage:true});
  console.log(name,'h',r.h,'overflow',r.sw>w?r.sw:'no','broken',r.broken.length?r.broken:'0','unlinked',r.unlinked.length?r.unlinked:'0','bgNoLink',r.bg);await p.close();}}
await b.close();})();
