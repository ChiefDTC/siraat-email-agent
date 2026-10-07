// QA-metingen en screenshots voor scripts/qa_render.py (niet los gebruiken).
// Gebruik: node scripts/qa_shots.js <jobs.json> <resultaat.json>
// jobs: [{key, html, width, shot (pad of null), raw (bool)}]. Externe verzoeken (fonts) worden geblokkeerd: beelden zijn lokaal.
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const [jobsFile, outFile] = process.argv.slice(2);
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const res = {}; let i = 0;
  async function worker() {
    const ctx = await b.newContext();
    await ctx.route(/^https?:/, r => r.abort());
    while (i < jobs.length) {
      const j = jobs[i++];
      const p = await ctx.newPage({ viewport: { width: j.width, height: 900 } });
      await p.setViewportSize({ width: j.width, height: 900 });
      try {
        await p.goto('file://' + path.resolve(j.html), { waitUntil: 'load', timeout: 30000 });
        await p.evaluate(() => Promise.all([...document.images].map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; setTimeout(r, 5000); }))));
        const m = await p.evaluate((raw) => {
          const vw = window.innerWidth, de = document.documentElement;
          const main = document.querySelector('table.w') || document.querySelector('table[width="600"]');
          const mr = main ? main.getBoundingClientRect() : null;
          const out = { vw, scrollWidth: Math.max(de.scrollWidth, document.body.scrollWidth), height: Math.max(de.scrollHeight, document.body.scrollHeight),
            mainWidth: mr ? Math.round(mr.width) : null, narrow: [], wideImgs: [], badImgs: [], raw: { outside: [], beforeTable: [], visible: 0 } };
          if (main) {
            const rows = [...main.rows].filter(r => r.parentElement.closest('table') === main);
            for (const r of rows) for (const c of r.cells) {
              const w = c.getBoundingClientRect().width, h = c.getBoundingClientRect().height;
              if (h > 0 && r.cells.length === 1 && Math.abs(w - mr.width) > 1) out.narrow.push((c.innerText || c.innerHTML).trim().slice(0, 60) + ' (' + Math.round(w) + ' px)');
            }
          }
          for (const im of document.images) {
            const src = im.getAttribute('src') || '';
            if (raw && /[{%]|%7B/.test(src)) continue;   // ruwe weergave: Django-logica in src laadt niet, dat is verwacht
            const r = im.getBoundingClientRect();
            if (r.width === 0 && r.height === 0 && im.offsetParent === null) continue;   // verborgen (desk/mob)
            if (!im.complete || im.naturalWidth === 0) out.badImgs.push(src.slice(-80));
            const wa = parseInt(im.getAttribute('width') || '0');
            if (main && wa >= 560 && Math.abs(r.width - mr.width) > 1) out.wideImgs.push(src.split('/').pop().slice(0, 50) + ' ' + Math.round(r.width) + '/' + Math.round(mr.width) + ' px');
          }
          const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
          let n;
          while ((n = tw.nextNode())) {
            const t = n.nodeValue; if (!/\{%|\{\{/.test(t)) continue;
            const el = n.parentElement; const st = el && getComputedStyle(el);
            if (st && (st.display === 'none' || st.visibility === 'hidden')) continue;
            out.raw.visible++;
            const snip = t.trim().replace(/\s+/g, ' ').slice(0, 70);
            if (main && !main.contains(n)) out.raw.outside.push(snip);
            else if (n.nextSibling && n.nextSibling.nodeName === 'TABLE') out.raw.beforeTable.push(snip);
          }
          return out;
        }, !!j.raw);
        if (j.shot) await p.screenshot({ path: j.shot, fullPage: true, type: 'jpeg', quality: 62 });
        res[j.key] = m;
      } catch (e) { res[j.key] = { error: String(e).slice(0, 300) }; }
      await p.close();
    }
    await ctx.close();
  }
  await Promise.all([worker(), worker(), worker(), worker()]);
  await b.close();
  fs.writeFileSync(outFile, JSON.stringify(res));
})();
