const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{const jobs=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const ctx=await b.newContext({viewport:{width:600,height:900}});await ctx.route(/^https?:/,r=>r.abort());
let i=0;async function w(){while(i<jobs.length){const j=jobs[i++];for(let t=0;t<3;t++){const p=await ctx.newPage();try{await p.setViewportSize({width:600,height:900});
await p.goto('file://'+path.resolve(j.html),{waitUntil:'load',timeout:60000});
await p.evaluate(()=>Promise.all([...document.images].map(im=>im.complete?0:new Promise(r=>{im.onload=im.onerror=r;setTimeout(r,5000);}))));
await p.screenshot({path:j.png,fullPage:true,timeout:90000});console.log('ok',path.basename(j.png));await p.close();break;}catch(e){console.log('retry',path.basename(j.png),String(e).slice(0,80));await p.close();}}}}
await Promise.all([w(),w()]);await b.close();})();
