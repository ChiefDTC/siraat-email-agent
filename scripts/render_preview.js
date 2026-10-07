// Gebruik: node scripts/render_preview.js <preview.html> <uit-prefix>
// Schrijft <uit-prefix>-desktop.png (700 breed) en <uit-prefix>-mobile.png (390 breed).
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path=require('path');
(async()=>{const [src,out]=process.argv.slice(2);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const [w,suf] of [[700,'desktop'],[390,'mobile']]){const p=await b.newPage({viewport:{width:w,height:900}});
await p.goto('file://'+path.resolve(src),{waitUntil:'networkidle'}).catch(()=>{});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
await p.screenshot({path:`${out}-${suf}.png`,fullPage:true});}
await b.close();console.log('ok',out);})();
