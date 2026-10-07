// Browsermetingen voor scripts/qa_inbox.py (niet los gebruiken): dark mode, toegankelijkheid, beeld tegenover tekst.
// Gebruik: node scripts/qa_inbox.js <jobs.json> <resultaat.json>
// jobs: [{key, html, width, mode: light|dark|partial|full, shot (pad of null)}]
//   light    gewone weergave
//   dark     prefers-color-scheme: dark (Apple Mail, iOS Mail, Outlook Mac respecteren <meta name="color-scheme">)
//   partial  simulatie gedeeltelijke inversie (Gmail Android, Outlook.com, Outlook app): lichte achtergronden worden donker,
//            donkere tekst wordt licht; donkere achtergronden en lichte tekst blijven; beelden blijven ongewijzigd
//   full     simulatie volledige inversie (Gmail iOS, Outlook Windows dark): alle kleuren krijgen omgekeerde lichtheid; beelden blijven
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const [jobsFile, outFile] = process.argv.slice(2);
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const res = {}; let i = 0;
  async function worker() {
    while (i < jobs.length) {
      const j = jobs[i++];
      const ctx = await b.newContext({ colorScheme: j.mode === 'dark' ? 'dark' : 'light' });
      await ctx.route(/^https?:/, r => r.abort());
      const p = await ctx.newPage();
      await p.setViewportSize({ width: j.width, height: 900 });
      try {
        await p.goto('file://' + path.resolve(j.html), { waitUntil: 'load', timeout: 30000 });
        await p.evaluate(() => Promise.all([...document.images].map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; setTimeout(r, 5000); }))));
        const m = await p.evaluate((mode) => {
          const parse = c => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const v = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; };
          const lin = c => { c /= 255; return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); };
          const lum = c => 0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]);
          const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
          function hsl([r, g, b]) { r /= 255; g /= 255; b /= 255; const mx = Math.max(r, g, b), mn = Math.min(r, g, b); let h = 0, s = 0, l = (mx + mn) / 2;
            if (mx !== mn) { const d = mx - mn; s = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn);
              h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6; } return [h, s, l]; }
          function rgb([h, s, l]) { if (!s) return [l * 255, l * 255, l * 255].map(Math.round);
            const q = l < 0.5 ? l * (1 + s) : l + s - l * s, p = 2 * l - q;
            const f = t => { if (t < 0) t += 1; if (t > 1) t -= 1; return t < 1 / 6 ? p + (q - p) * 6 * t : t < 1 / 2 ? q : t < 2 / 3 ? p + (q - p) * (2 / 3 - t) * 6 : p; };
            return [f(h + 1 / 3), f(h), f(h - 1 / 3)].map(x => Math.round(x * 255)); }
          // omgekeerde lichtheid, zoals de mailclients doen (donker wordt niet zuiver zwart, licht niet zuiver wit)
          const inv = c => { const [h, s, l] = hsl(c); return rgb([h, s * 0.85, Math.min(0.93, Math.max(0.07, 1 - l))]); };
          const css = c => 'rgb(' + c.slice(0, 3).join(',') + ')';
          if (mode === 'partial' || mode === 'full') {
            const all = [document.documentElement, ...document.querySelectorAll('body, body *')];
            const plan = [];
            for (const el of all) {
              if (el.tagName === 'IMG') continue;
              const cs = getComputedStyle(el); const bg = parse(cs.backgroundColor), fg = parse(cs.color);
              const ch = {};
              if (bg && bg[3] > 0 && (mode === 'full' || lum(bg) > 0.4)) ch['background-color'] = css(inv(bg));
              if (fg && (mode === 'full' || lum(fg) < 0.4)) ch['color'] = css(inv(fg));
              for (const s of ['top', 'right', 'bottom', 'left']) {
                const bc = parse(cs['border' + s[0].toUpperCase() + s.slice(1) + 'Color']); const bw = parseFloat(cs['border' + s[0].toUpperCase() + s.slice(1) + 'Width']);
                if (bc && bw > 0 && (mode === 'full' || lum(bc) > 0.4)) ch['border-' + s + '-color'] = css(inv(bc));
              }
              plan.push([el, ch]);
            }
            if (getComputedStyle(document.body).backgroundColor === 'rgba(0, 0, 0, 0)') plan.push([document.body, { 'background-color': 'rgb(18,18,18)' }]);
            for (const [el, ch] of plan) for (const k in ch) el.style.setProperty(k, ch[k], 'important');
          }
          const vis = el => { for (let e = el; e && e !== document.body; e = e.parentElement) { const s = getComputedStyle(e); if (s.display === 'none' || s.visibility === 'hidden' || parseFloat(s.opacity) === 0 || (s.maxHeight === '0px' && s.overflow === 'hidden')) return false; } return true; };
          const bgOf = el => { for (let e = el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor); if (c && c[3] > 0.5) return c; } return mode === 'dark' ? [18, 18, 18, 1] : [255, 255, 255, 1]; };
          const main = document.querySelector('table.w') || document.querySelector('table[width="600"]');
          const mr = main ? main.getBoundingClientRect() : { width: innerWidth, height: document.body.scrollHeight };
          const footer = [...document.querySelectorAll('td')].filter(td => /NON-TOXIC COOKWARE/.test(td.innerText || '') && /Unsubscribe|Manage preferences/.test(td.innerText || '') && td.querySelector('img')).pop();
          const out = { contrastFail: [], nText: 0, small: [], tap: [], imgs: [], imgArea: 0, mainArea: Math.round(mr.width * mr.height), textChars: 0, height: Math.max(document.documentElement.scrollHeight, document.body.scrollHeight) };
          // tekst: per element met eigen tekst
          const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; const seen = new Set();
          while ((n = tw.nextNode())) {
            const t = n.nodeValue.replace(/[\s‌ ]+/g, ' ').trim(); if (t.length < 2) continue;
            const el = n.parentElement; if (!el || seen.has(el) || !vis(el)) continue; seen.add(el);
            const cs = getComputedStyle(el); const fs = parseFloat(cs.fontSize); if (fs <= 2) continue;
            const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
            const own = [...el.childNodes].filter(c => c.nodeType === 3).map(c => c.nodeValue).join(' ').replace(/[\s‌ ]+/g, ' ').trim();
            out.nText++; out.textChars += own.length;
            const fg = parse(cs.color), bg = bgOf(el); const big = fs >= 24 || (fs >= 18.66 && parseInt(cs.fontWeight) >= 700);
            const cr = ratio(fg, bg); const inFoot = footer ? footer.contains(el) : false;
            if (cr < (big ? 3 : 4.5)) out.contrastFail.push({ t: own.slice(0, 50), r: +cr.toFixed(2), fs, fg: css(fg), bg: css(bg), foot: inFoot });
            if (fs < 14) out.small.push({ t: own.slice(0, 50), fs, len: own.length, foot: inFoot, link: !!el.closest('a') });
          }
          // tap targets: losse links (geen link midden in lopende tekst, WCAG 2.5.5-uitzondering 'inline')
          for (const a of document.querySelectorAll('a[href]')) {
            if (!vis(a)) continue; const r = a.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
            let blk = a.parentElement; while (blk && getComputedStyle(blk).display === 'inline') blk = blk.parentElement;
            const bt = (blk ? blk.innerText : '').replace(/\s+/g, ' ').trim(), at = (a.innerText || '').replace(/\s+/g, ' ').trim();
            const inline = !a.querySelector('img') && bt.length > at.length + 12;
            if (!inline && (r.height < 44 || r.width < 44)) out.tap.push({ t: (at || (a.querySelector('img') || {}).alt || '').slice(0, 40), w: Math.round(r.width), h: Math.round(r.height), foot: footer ? footer.contains(a) : false });
          }
          for (const im of document.images) {
            if (!vis(im)) continue; const r = im.getBoundingClientRect(); if (r.width < 2 || r.height < 2) continue;
            out.imgArea += r.width * r.height;
            const src = decodeURIComponent((im.getAttribute('src') || '').replace(/^file:\/\//, ''));
            out.imgs.push({ src, w: Math.round(r.width), h: Math.round(r.height), bg: css(bgOf(im.parentElement)), alt: im.getAttribute('alt') });
          }
          out.imgArea = Math.round(out.imgArea);
          return out;
        }, j.mode);
        if (j.shot) await p.screenshot({ path: j.shot, fullPage: true, type: 'jpeg', quality: 70 });
        res[j.key] = m;
      } catch (e) { res[j.key] = { error: String(e).slice(0, 300) }; }
      await ctx.close();
    }
  }
  await Promise.all([worker(), worker(), worker(), worker()]);
  await b.close();
  fs.writeFileSync(outFile, JSON.stringify(res));
})();
