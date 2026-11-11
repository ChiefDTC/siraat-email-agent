// Rendert variant-X.liquid met een voorbeeldorder naar variant-X-preview.html en previews/*.png (600 breed, DSF 2) plus 390 mobiel.
// Gebruik (vanuit shopify-order-confirmation): LIQUIDJS=/pad/naar/node_modules/liquidjs node _tools/render.js
// liquidjs@10.16.1 (npm i liquidjs@10.16.1 in een losse map), Playwright uit /opt/node-tools.
const path = require('path'), fs = require('fs');
const { Liquid } = require(process.env.LIQUIDJS || 'liquidjs');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const DIR = path.resolve(__dirname, '..');
const samples = require('./samples.json');
const eng = new Liquid({ strictFilters: true });
const fmt = (c) => (Number(c) / 100).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
let CUR = 'USD';
eng.registerFilter('money', (c) => '$' + fmt(c));
eng.registerFilter('money_with_currency', (c) => '$' + fmt(c) + ' ' + CUR);
eng.registerFilter('img_url', (u) => String(u));
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const report = [];
  for (const v of (process.env.VARIANTS || 'a,b,c').split(',')) {
    const src = fs.readFileSync(path.join(DIR, `variant-${v}.liquid`), 'utf8');
    for (const [sk, ctx] of Object.entries(samples)) {
      CUR = ctx.presentment_currency || 'USD';
      const html = await eng.parseAndRender(src, ctx);
      const name = sk === 'us_sub' ? `variant-${v}-preview.html` : `previews/_check-${v}-${sk}.html`;
      const out = path.join(DIR, name);
      fs.writeFileSync(out, html);
      for (const [w, suf] of [[600, ''], [390, '-mobile']]) {
        const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 2 });
        await p.goto('file://' + out, { waitUntil: 'networkidle' }).catch(() => {});
        await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
        const m = await p.evaluate(() => {
          const sw = document.documentElement.scrollWidth, vw = window.innerWidth;
          const broken = [...document.images].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.src.slice(0, 80));
          // overlap: tekstblokken die buiten hun cel lopen
          const over = [...document.querySelectorAll('td')].filter(td => td.scrollWidth > td.clientWidth + 2 && td.clientWidth > 0).length;
          const txt = document.body.innerText;
          // contrast hero-overlay: achtergrond onder de tekst (tekst tijdelijk onzichtbaar), zie _tools/contrast.py
          const ht = document.querySelector('.herotxt'); let hero = null;
          if (ht && ht.children.length) { const a = ht.children[0].getBoundingClientRect(), z = ht.children[ht.children.length - 1].getBoundingClientRect(); hero = [a.left, a.top + window.scrollY, a.width, z.bottom - a.top]; }
          return { sw, vw, broken, over, h: document.body.scrollHeight, hero, leftovers: (txt.match(/\{\{|\{%/g) || []).length, dash: /[\u2013\u2014]/.test(document.documentElement.outerHTML) };
        });
        report.push({ v, sk, w, ...m });
        const png = sk === 'us_sub' ? `previews/variant-${v}${suf}.png` : `previews/_check-${v}-${sk}${suf}.png`;
        await p.screenshot({ path: path.join(DIR, png), fullPage: true });
        if (m.hero) { await p.addStyleTag({ content: '.herotxt, .herotxt *{color:transparent!important;text-shadow:none!important}' });
          await p.screenshot({ path: path.join(DIR, 'previews', `_bg-${v}-${sk}${suf}.png`), clip: { x: m.hero[0], y: m.hero[1], width: m.hero[2], height: m.hero[3] } }); }
        await p.close();
      }
    }
  }
  await b.close();
  for (const r of report) console.log(JSON.stringify(r));
})();
