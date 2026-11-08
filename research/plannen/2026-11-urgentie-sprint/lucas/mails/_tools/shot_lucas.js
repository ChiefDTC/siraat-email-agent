// 1x screenshots (600 px voor mails, 1280 voor de buybox) van alle voorbeeldmails naar ../screenshots/. Gebruik: node shot_lucas.js
const { chromium } = require('/opt/node-tools/node_modules/playwright'); const fs = require('fs'), path = require('path');
const M = path.resolve(__dirname, '..'); const out = path.join(M, 'screenshots'); fs.mkdirSync(out, { recursive: true });
const files = [...fs.readdirSync(M).filter(f => f.endsWith('.html') && f !== 'index.html'), ...fs.readdirSync(path.join(M, 'redeem')).map(f => 'redeem/' + f)];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const f of files) {
    const w = f.includes('buybox') ? 1280 : 600;
    const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.join(M, f), { waitUntil: 'networkidle' }).catch(() => {}); await p.waitForTimeout(500);
    const r = await p.evaluate(() => ({ h: document.documentElement.scrollHeight, sw: document.documentElement.scrollWidth,
      broken: [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(-60)), dash: /[\u2013\u2014]/.test(document.body.innerText) }));
    await p.screenshot({ path: path.join(out, f.replace('/', '-').replace('.html', '.png')), fullPage: true });
    console.log(f, 'h', r.h, '| overflow', r.sw > w ? r.sw : 'no', '| broken', r.broken.length ? r.broken : 0, r.dash ? 'STREEPJE' : '');
    await p.close();
  }
  await b.close();
})();
