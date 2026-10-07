const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs=require('fs');
(async()=>{const ids=process.argv.slice(2);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:{server:process.env.HTTPS_PROXY||process.env.https_proxy}});
for(const id of ids){const h=JSON.parse(fs.readFileSync(`/tmp/hist/tpl/${id}.json`)).data.attributes.html;
fs.writeFileSync(`/tmp/hist/shots/${id}.html`,h);
const p=await b.newPage({viewport:{width:600,height:900}});
await p.goto('file:///tmp/hist/shots/'+id+'.html',{waitUntil:'networkidle',timeout:45000}).catch(e=>console.log('t',id));
await p.waitForTimeout(500);
await p.screenshot({path:`/tmp/hist/shots/${id}.png`,fullPage:true});
const hgt=await p.evaluate(()=>document.body.scrollHeight);console.log(id,hgt);await p.close();}
await b.close();})();
