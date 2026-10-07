// Renders svg/<color>/*.svg to png/<color>/<name>-48.png and <name>-96.png, plus preview.png.
// Run: node render_icons.js   (needs playwright at /opt/node-tools/node_modules/playwright)
const path = require('path'), fs = require('fs');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const HERE = __dirname;
const exe = ['/opt/pw-browsers/chromium', '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'].find(p => { try { return fs.statSync(p).isFile(); } catch { return false; } });
(async () => {
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  const colors = fs.readdirSync(path.join(HERE, 'svg'));
  for (const c of colors) {
    fs.mkdirSync(path.join(HERE, 'png', c), { recursive: true });
    for (const f of fs.readdirSync(path.join(HERE, 'svg', c)).filter(f => f.endsWith('.svg'))) {
      const svg = fs.readFileSync(path.join(HERE, 'svg', c, f), 'utf8').replace('width="24" height="24"', 'width="48" height="48"');
      for (const [size, scale] of [[48, 1], [96, 2]]) {
        const page = await browser.newPage({ viewport: { width: 48, height: 48 }, deviceScaleFactor: scale });
        await page.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
        await page.locator('svg').screenshot({ path: path.join(HERE, 'png', c, f.replace('.svg', `-${size}.png`)), omitBackground: true });
        await page.close();
      }
    }
  }
  // preview sheet
  const names = fs.readdirSync(path.join(HERE, 'svg', 'brick')).filter(f => f.endsWith('.svg')).sort();
  const cell = (c, n, bg) => `<div class="cell" style="background:${bg}">${fs.readFileSync(path.join(HERE, 'svg', c, n), 'utf8').replace('width="24" height="24"', 'width="48" height="48"')}<span style="color:${bg === '#282828' ? '#C9C6C0' : '#727272'}">${n.replace('.svg', '')}</span></div>`;
  const white = fs.readFileSync(path.join(HERE, 'svg', 'ink', names[0]), 'utf8');
  const html = `<html><head><style>
    body{margin:0;padding:32px;background:#FFFFFF;font:13px Inter,Arial,sans-serif;color:#282828}
    h1{font:600 20px Inter,Arial;margin:0 0 4px} p{margin:0 0 20px;color:#727272}
    h2{font:600 14px Inter,Arial;margin:24px 0 10px}
    .grid{display:grid;grid-template-columns:repeat(8,1fr);gap:8px}
    .cell{display:flex;flex-direction:column;align-items:center;gap:8px;padding:16px 4px;border:1px solid #ECE7DD;border-radius:6px}
    .cell span{font-size:11px;text-align:center}
  </style></head><body>
  <h1>Siraat line icons</h1><p>24px grid, 1.75px stroke, round caps and joins. Shown at 48px. Brick #AC3B19, ink #282828.</p>
  <h2>Brick on paper</h2><div class="grid">${names.map(n => cell('brick', n, '#FFFFFF')).join('')}</div>
  <h2>Ink on cream</h2><div class="grid">${names.map(n => cell('ink', n, '#F8F7F2')).join('')}</div>
  <h2>Brick on charcoal (footer check)</h2><div class="grid">${names.map(n => cell('brick', n, '#282828')).join('')}</div>
  </body></html>`;
  const page = await browser.newPage({ viewport: { width: 1100, height: 800 }, deviceScaleFactor: 1 });
  await page.setContent(html);
  await page.screenshot({ path: path.join(HERE, 'preview.png'), fullPage: true });
  await browser.close();
  console.log('done', colors, names.length);
})();
