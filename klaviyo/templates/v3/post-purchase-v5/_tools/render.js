// Rendert elke sectie (sections/src/*.html) als JPG q80 op ware grootte (1200 breed; kaarten 600). node _tools/render.js [naam...]
const { chromium } = require('/opt/node-tools/node_modules/playwright');const path=require('path');const fs=require('fs');
(async()=>{const dir=path.resolve(__dirname,'../sections');let list=JSON.parse(fs.readFileSync(dir+'/src/list.json'));
 if(process.argv.length>2) list=process.argv.slice(2);
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1200,height:1000},deviceScaleFactor:1});
 for(const n of list){await p.goto('file://'+dir+'/src/'+n+'.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
  const el=await p.$('#s');await el.screenshot({path:dir+'/'+n+'.jpg',type:'jpeg',quality:80});}
 await b.close();console.log('rendered',list.length);})();
