// Screenshot van gerenderde huidige templates: 375 px breed, bovenste 1600 px, JPEG.
// node shot_current.js <rendermap> <uitvoermap>
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 375, height: 800 }, deviceScaleFactor: 1 });
  for (const f of fs.readdirSync(src).filter(x => x.endsWith('.html'))) {
    await p.goto('file://' + path.resolve(src, f), { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
    await p.waitForTimeout(300);
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    const broken = await p.evaluate(() => [...document.images].filter(i => i.src.startsWith('http') && !(i.complete && i.naturalWidth)).length);
    await p.screenshot({ path: path.join(out, f.replace('.html', '.jpg')), type: 'jpeg', quality: 62,
      clip: { x: 0, y: 0, width: 375, height: Math.min(h, 1600) }, fullPage: true });
    console.log(f, h, 'broken', broken);
  }
  await b.close();
})();
