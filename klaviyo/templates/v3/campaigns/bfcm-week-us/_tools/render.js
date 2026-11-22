// Rendert _tools/.preview/*.html naar <map>/preview[-a|-b].png (600 px, deviceScaleFactor 1) en
// _tools/.preview/<naam>-390.png (mobiel). Meldt horizontale overflow en beelden die niet laden.
// Gebruik: node klaviyo/templates/v3/campaigns/bfcm-week-us/_tools/render.js [naam ...]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const T = __dirname, C = path.dirname(T), PREV = path.join(T, '.preview');
(async () => {
  const only = process.argv.slice(2);
  const files = fs.readdirSync(PREV).filter(f => f.endsWith('.html') && (!only.length || only.some(o => f.startsWith(o))));
  const browser = await chromium.launch();
  for (const f of files) {
    const name = f.replace('.html', ''), m = name.match(/^(m\d-[a-z0-9-]+?)(?:-([ab]))?$/);
    const map = m[1], v = m[2];
    for (const w of [600, 390]) {
      const page = await browser.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
      await page.goto('file://' + path.join(PREV, f), { waitUntil: 'networkidle', timeout: 60000 });
      await page.evaluate(() => document.fonts.ready);
      const info = await page.evaluate(() => ({
        sw: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight,
        broken: [...document.images].filter(i => !i.complete || !i.naturalWidth).map(i => i.src.slice(0, 90)),
      }));
      const out = w === 600 ? path.join(C, map, v ? `preview-${v}.png` : 'preview.png') : path.join(PREV, `${name}-390.png`);
      await page.screenshot({ path: out, fullPage: true });
      console.log(`${name} @${w}: height ${info.h}px, scrollWidth ${info.sw}${info.sw > w ? ' OVERFLOW' : ''}${info.broken.length ? ' BROKEN ' + info.broken.join(' ') : ''} -> ${path.relative(C, out)}`);
      await page.close();
    }
  }
  await browser.close();
})();
