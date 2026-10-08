// Browsermetingen en screenshots voor scripts/qa_inbox.py (subcommando's mail en templates). Niet los gebruiken.
// Gebruik: node scripts/qa_mail_shots.js <jobs.json> <resultaat.json>
// jobs: [{key, html, width, mode: light|dark|forced, shot (pad of null), net (bool: beelden van internet laden)}]
//   light   gewone weergave
//   dark    prefers-color-scheme: dark (Apple Mail, iOS Mail, Outlook Mac)
//   forced  Chromium auto-dark (WebContentsForceDark), benadering van Gmail-app en Outlook die kleuren zelf omkeren
// Meet: horizontaal scrollen, afgesneden/vervormde/uitstekende beelden, beelden die niet laden, contrast van de afmeldlink,
// en in donkere modi tekst met contrast < 3:1.
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'); const path = require('path');
const TRACK = /klclick\d?\.com|kmail-lists\.com|klaviyo\.com\/(o|l)\//;
(async () => {
  const [jobsFile, outFile] = process.argv.slice(2);
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  const exe = '/opt/pw-browsers/chromium';
  const normal = await chromium.launch({ executablePath: exe });
  const forced = await chromium.launch({ executablePath: exe, args: ['--enable-features=WebContentsForceDark', '--force-dark-mode'] });
  const res = {}; let i = 0;
  async function worker() {
    while (i < jobs.length) {
      const j = jobs[i++];
      const b = j.mode === 'forced' ? forced : normal;
      const ctx = await b.newContext({ colorScheme: j.mode === 'light' ? 'light' : 'dark', viewport: { width: j.width, height: 900 } });
      await ctx.route(/^https?:/, r => (j.net && !TRACK.test(r.request().url()) && r.request().resourceType() === 'image') ? r.continue() : r.abort());
      const p = await ctx.newPage();
      try {
        const url = j.html.startsWith('http') ? j.html : 'file://' + path.resolve(j.html);
        await p.goto(url, { waitUntil: 'load', timeout: 45000 });
        await p.evaluate(() => Promise.all([...document.images].map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; setTimeout(r, 8000); }))));
        const m = await p.evaluate((mode) => {
          const parse = c => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const v = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; };
          const lin = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
          const lum = c => 0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]);
          const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
          const css = c => 'rgb(' + c.slice(0, 3).join(',') + ')';
          const vis = el => { for (let e = el; e && e !== document.body; e = e.parentElement) { const s = getComputedStyle(e); if (s.display === 'none' || s.visibility === 'hidden' || parseFloat(s.opacity) === 0 || (s.maxHeight === '0px' && s.overflow === 'hidden')) return false; } return true; };
          const bgOf = el => { for (let e = el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c[3] > 0.5) return c; } return canvasDark ? [18, 18, 18, 1] : [255, 255, 255, 1]; };
          // zonder color-scheme-meta blijft het canvas ook bij prefers-color-scheme: dark wit
          var canvasDark = mode !== 'light' && /dark/.test(getComputedStyle(document.documentElement).colorScheme + ' ' + ((document.querySelector('meta[name="color-scheme"]') || {}).content || ''));
          const vw = window.innerWidth, de = document.documentElement;
          const out = { vw, scrollWidth: Math.max(de.scrollWidth, document.body.scrollWidth), height: Math.max(de.scrollHeight, document.body.scrollHeight), cut: [], broken: [], unsubContrast: [], lowContrast: [] };
          const name = im => (im.getAttribute('src') || '').split('?')[0].split('/').pop().slice(0, 50);
          out.imgRects = [];   // voor de pixelcontrole op de screenshot (logo zichtbaar, lichte blokken in donkere modus)
          for (const im of document.images) {
            const r = im.getBoundingClientRect(); if (r.width < 40 || r.height < 20 || !vis(im)) continue;
            const src = im.getAttribute('src') || '', alt = (im.getAttribute('alt') || '').trim().toLowerCase();
            out.imgRects.push({ name: name(im), logo: /logo|lockup/i.test(src) || alt === 'siraat', x: Math.round(r.left + scrollX), y: Math.round(r.top + scrollY), w: Math.round(r.width), h: Math.round(r.height) });
          }
          for (const im of document.images) {
            const r = im.getBoundingClientRect();
            if (r.width < 3 || r.height < 3 || !vis(im)) continue;
            if (!im.complete || im.naturalWidth === 0) { out.broken.push(name(im)); continue; }
            if (r.right > vw + 1 || r.left < -1) out.cut.push('beeld steekt buiten het scherm: ' + name(im) + ' (' + Math.round(r.left) + '..' + Math.round(r.right) + ' px)');
            const nr = im.naturalWidth / im.naturalHeight, rr = r.width / r.height;
            const fit = getComputedStyle(im).objectFit;
            if (Math.abs(nr - rr) / nr > 0.04 && !['cover', 'contain'].includes(fit)) out.cut.push('beeld vervormd: ' + name(im) + ' (' + im.naturalWidth + 'x' + im.naturalHeight + ' getoond als ' + Math.round(r.width) + 'x' + Math.round(r.height) + ')');
            for (let e = im.parentElement; e && e !== document.body; e = e.parentElement) {
              const s = getComputedStyle(e);
              if (/(hidden|clip)/.test(s.overflow + s.overflowX + s.overflowY)) {
                const er = e.getBoundingClientRect();
                if (er.width > 2 && (r.right > er.right + 2 || r.left < er.left - 2 || r.bottom > er.bottom + 2 || r.top < er.top - 2)) { out.cut.push('beeld afgesneden door container: ' + name(im)); }
                break;
              }
            }
          }
          for (const a of document.querySelectorAll('a[href]')) {
            const t = (a.innerText || '').replace(/\s+/g, ' ').trim(); const h = a.getAttribute('href') || '';
            if (mode === 'forced' || !/unsubscribe|preferences|afmelden/i.test(t + ' ' + h) || !vis(a) || !t) continue;
            const fg = parse(getComputedStyle(a).color), bg = bgOf(a);
            out.unsubContrast.push({ t, ratio: +ratio(fg, bg).toFixed(2), fg: css(fg), bg: css(bg), mode });
          }
          if (mode === 'dark') {   // forced dark wijzigt de kleuren pas bij het tekenen: alleen screenshot, geen meting
            const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; const seen = new Set();
            while ((n = tw.nextNode())) {
              const t = n.nodeValue.replace(/[\s‌ ͏­]+/g, ' ').trim(); if (t.length < 3) continue;
              const el = n.parentElement; if (!el || seen.has(el) || !vis(el)) continue; seen.add(el);
              const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
              const fg = parse(getComputedStyle(el).color); if (!fg) continue; const cr = ratio(fg, bgOf(el));
              if (cr < 3) out.lowContrast.push({ t: t.slice(0, 40), ratio: +cr.toFixed(2) });
            }
          }
          return out;
        }, j.mode);
        if (j.shot) await p.screenshot({ path: j.shot, fullPage: true, type: 'jpeg', quality: 60 });
        res[j.key] = Object.assign({ width: j.width, mode: j.mode }, m);
      } catch (e) { res[j.key] = { width: j.width, mode: j.mode, error: String(e).slice(0, 300), scrollWidth: 0, vw: j.width }; }
      await ctx.close();
    }
  }
  await Promise.all([worker(), worker(), worker(), worker()]);
  await normal.close(); await forced.close();
  fs.writeFileSync(outFile, JSON.stringify(res));
})();
