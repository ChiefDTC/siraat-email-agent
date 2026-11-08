// Controle (375 en 1280 px): horizontale overloop, kapotte beelden; screenshots per sectie in plakken < 4000 px.
// node check_shots.js [shots]
const { chromium } = require('playwright');
const path = require('path');
const DIR = path.resolve(__dirname, '..');
const SHOTS = process.argv[2] === 'shots';
(async () => {
  const b = await chromium.launch();
  for (const w of [375, 1280]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.join(DIR, 'index.html'), { waitUntil: 'domcontentloaded' });
    await p.evaluate(() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'));
    await p.waitForLoadState('networkidle', { timeout: 120000 }).catch(() => {});
    await p.evaluate(async () => { await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; setTimeout(r, 20000); }))); });
    const r = await p.evaluate(() => {
      const vw = document.documentElement.clientWidth;
      const wide = [...document.querySelectorAll('body *')].filter(e => { const b = e.getBoundingClientRect(); return b.right > vw + 1 && getComputedStyle(e).position !== 'fixed' && !e.closest('nav.top') && !e.closest('.bh'); }).slice(0, 8).map(e => e.tagName + '.' + e.className + ' ' + Math.round(e.getBoundingClientRect().right));
      const broken = [...document.images].filter(i => !(i.complete && i.naturalWidth > 0)).map(i => i.getAttribute('src'));
      const bgs = [...document.querySelectorAll('.mhero')].map(e => getComputedStyle(e).backgroundImage.slice(5, -2));
      return { vw, sw: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight, imgs: document.images.length, broken, wide, bgs: [...new Set(bgs)] };
    });
    // achtergrondbeelden van de hero-mocks laden
    const bad = [];
    for (const u of r.bgs) { const ok = await p.evaluate(u => new Promise(res => { const i = new Image(); i.onload = () => res(i.naturalWidth > 0); i.onerror = () => res(false); i.src = u; setTimeout(() => res(false), 20000); }), u); if (!ok) bad.push(u); }
    console.log(JSON.stringify({ w, vw: r.vw, scrollWidth: r.sw, height: r.h, imgs: r.imgs, broken: r.broken, wide: r.wide, heroBg: r.bgs.length, heroBgBroken: bad }));
    if (SHOTS) {
      for (const id of ['flows', 'campagnes', 'herbouwd', 'blackhat', 'site']) {
        const box = await p.evaluate(id => { const e = document.getElementById(id); const b = e.getBoundingClientRect(); return { y: b.top + scrollY, h: b.height }; }, id);
        let maxH = box.h;
        if (w === 375 && id === 'flows') { // op mobiel alleen de eerste twee flows (anders tientallen plakken)
          maxH = await p.evaluate(() => { const f = document.querySelectorAll('#flows .flow')[2]; return f.getBoundingClientRect().top + scrollY - document.getElementById('flows').getBoundingClientRect().top - scrollY; });
        }
        const SL = 3800; let i = 0;
        for (let y = 0; y < maxH; y += SL, i++) {
          const hh = Math.min(SL, maxH - y);
          await p.screenshot({ path: path.join(DIR, 'shots', `${id}-${w}-${String(i + 1).padStart(2, '0')}.jpg`), type: 'jpeg', quality: 70, fullPage: true, clip: { x: 0, y: box.y + y, width: w, height: hh } });
        }
        console.log(id, w, Math.round(box.h), 'slices', i);
      }
    }
    await p.close();
  }
  await b.close();
})();
