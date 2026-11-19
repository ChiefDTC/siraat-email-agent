// PNG op 600 en 390 px (DSF 2) van previews/*.html -> renders/; meldt kapotte beelden, overloop, em dash, hoogte. node _tools/shot.js [filter]
const { chromium } = require('/opt/node-tools/node_modules/playwright');const path=require('path');const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const dir=path.resolve(__dirname,'../'+(process.env.DIR||'previews'));const f=process.argv[2]||'';const widths=(process.argv[3]||'600,390').split(',').map(Number);
for(const fn of fs.readdirSync(dir).filter(x=>x.endsWith('.html')&&x.includes(f))){
for(const w of widths){const p=await b.newPage({viewport:{width:w,height:900},deviceScaleFactor:2});
 await p.goto('file://'+dir+'/'+fn,{waitUntil:'networkidle',timeout:90000}).catch(()=>{});await p.waitForTimeout(400);
 const r=await p.evaluate(()=>{const W=document.documentElement.clientWidth;return{broken:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src.slice(-50)),sw:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight,dash:document.body.innerText.includes('—')}});
 await p.screenshot({path:path.resolve(__dirname,'../renders/'+fn.replace('.html','')+'-'+w+'.png'),fullPage:true});
 console.log(fn,w,'h',r.h,'overflow',r.sw>w?r.sw:'no','broken',r.broken.length?r.broken:0,'emdash',r.dash);await p.close();}}
await b.close();})();
