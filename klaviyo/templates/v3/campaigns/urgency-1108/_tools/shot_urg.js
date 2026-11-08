// Screenshots van de -preview.html op 375 en 600 px (2x) plus de checks uit UX-spec 6: overloop, kapotte beelden, ongelinkte beelden/blokken,
// eerste scherm (deadline, aanbod en knop 1 boven 560 px op 375, knop 1 uiterlijk op 520), hoogte <= 3600. Gebruik: node shot_urg.js [previewmap]
const { chromium } = require('/opt/node-tools/node_modules/playwright'); const fs = require('fs'), path = require('path');
const N = path.resolve(__dirname, '..'); const out = process.argv[2] || path.join(N, 'previews');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const rep = [];
  for (const f of fs.readdirSync(N).filter(f => /^urg-.*-preview\.html$/.test(f)).sort()) {
    for (const w of [375, 600]) {
      const p = await b.newPage({ viewport: { width: w, height: 800 }, deviceScaleFactor: 2 });
      await p.goto('file://' + path.join(N, f), { waitUntil: 'networkidle' }).catch(() => {}); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
      const r = await p.evaluate(() => {
        const bot = s => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().bottom + scrollY) : null; };
        const imgs = [...document.images];
        const unlinked = imgs.filter(i => !i.closest('a')).map(i => i.src.split('/').pop().slice(0, 40));
        const txt = document.body.innerText;
        return { h: document.documentElement.scrollHeight, sw: document.documentElement.scrollWidth,
          broken: imgs.filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(-50)), unlinked,
          cta1: bot('[data-urg="cta1"]') || bot('[data-urg="link1"]'), dl: bot('[data-urg="deadline"]') || bot('b'), offer: bot('[data-urg="offer"]') || bot('[data-urg="h1"]') || bot('[data-urg="deadline"]'),
          dash: /[–—]/.test(txt) };
      });
      const name = f.replace('-preview.html', '') + '-' + w + '.png'; await p.screenshot({ path: path.join(out, name), fullPage: true });
      const fs560 = w === 375 ? (r.cta1 && r.dl && r.offer && r.cta1 <= 560 && r.dl <= 560 && r.offer <= 560 ? 'ok' : 'FOUT') : '';
      console.log(name, 'h', r.h, r.h > 3600 ? 'TE LANG' : '', '| overflow', r.sw > w ? r.sw : 'no', '| broken', r.broken.length ? r.broken : 0,
        '| unlinked', r.unlinked.length ? r.unlinked : 0, w === 375 ? `| knop1 ${r.cta1} deadline ${r.dl} aanbod ${r.offer} eerste-scherm ${fs560}${r.cta1 > 520 ? ' (knop1>520)' : ''}` : '', r.dash ? '| STREEPJE' : '');
      await p.close();
    }
  }
  await b.close();
})();
