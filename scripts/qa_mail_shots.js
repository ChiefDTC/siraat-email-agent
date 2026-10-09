// Browsermetingen en screenshots voor scripts/qa_inbox.py (subcommando's mail en templates). Niet los gebruiken.
// Gebruik: node scripts/qa_mail_shots.js <jobs.json> <resultaat.json>
// jobs: [{key, html, width, mode: light|dark|forced|apple, shot (pad of null), net (bool: beelden van internet laden)}]
//   light   gewone weergave
//   dark    prefers-color-scheme: dark (Apple Mail, iOS Mail, Outlook Mac), alleen de eigen CSS van de mail
//   forced  geforceerde inversie: Chromium auto-dark (WebContentsForceDark) NA het weghalen van color-scheme (meta's en :root).
//           Benadering van clients die zelf omkeren en 'light only' negeren (Gmail-app bij niet-Google-accounts, Outlook.com/-apps,
//           Outlook Windows). Sinds de mails 'light only' melden (13-darkmode.md, 8 okt 2026) zou auto-dark ze anders altijd licht laten.
//   gmailios  Gmail-app iPhone in de strengste vorm (niet-Google-account, of Gmail die het <style>-blok weggooit): alle <style>,
//           <link> en color-scheme-meta's weg, class-attributen weg (dus geen media queries), alleen inline CSS en attributen.
//           Breder dan het scherm = Gmail schaalt de mail in (zoom), zoals de app doet. Meet lege tekstcellen en contrast.
//   gmailtrim gmailios plus Gmail-trimming in een thread (twee mails met hetzelfde onderwerp, 9 okt 2026): de laatste rijen van de
//           hoofdtabel worden uit hun tabel getild en los na de mail gezet, achter een '•••' (zoals Gmail getrimde inhoud
//           toont). <tr>/<td> buiten een tabel vallen dan weg; alleen wat een eigen <table bgcolor> heeft houdt zijn achtergrond.
//           Lichte tekst op wit in dat deel = de footerfout van 9 okt.
//   apple   wat Apple Mail (en Outlook Mac, Android-webviews die color-scheme volgen) doet: prefers-color-scheme: dark plus auto-dark
//           die de color-scheme-verklaring van de mail WEL volgt. Met 'light only' blijft de mail licht; zonder verklaring wordt hij donker.
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
      const b = (j.mode === 'forced' || j.mode === 'apple') ? forced : normal;
      const ctx = await b.newContext({ colorScheme: (j.mode === 'light' || j.mode.startsWith('gmail')) ? 'light' : 'dark', viewport: { width: j.width, height: 900 } });
      await ctx.route(/^https?:/, r => (j.net && !TRACK.test(r.request().url()) && r.request().resourceType() === 'image') ? r.continue() : r.abort());
      const p = await ctx.newPage();
      try {
        const url = j.html.startsWith('http') ? j.html : 'file://' + path.resolve(j.html);
        await p.goto(url, { waitUntil: 'load', timeout: 45000 });
        await p.evaluate(() => Promise.all([...document.images].map(im => im.complete ? 0 : new Promise(r => { im.onload = im.onerror = r; setTimeout(r, 8000); }))));
        if (j.mode === 'forced') await p.evaluate(() => {   // de echte inversie negeert de light-only-verklaring: verklaring weg, auto-dark doet de rest
          document.querySelectorAll('meta[name="color-scheme"],meta[name="supported-color-schemes"]').forEach(m => m.remove());
          const st = document.createElement('style'); st.textContent = ':root,html,body{color-scheme:normal!important;}'; document.head.appendChild(st);
          document.documentElement.style.setProperty('color-scheme', 'normal', 'important');
          return new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
        });
        if (j.mode === 'gmailios' || j.mode === 'gmailtrim') await p.evaluate((mode) => {
          // tekst per cel vóór de ingreep (voor de controle 'cel met tekst rendert leeg')
          document.querySelectorAll('td,th').forEach((td, i) => { td.setAttribute('data-qa-td', i); const t = (td.textContent || '').replace(/[\s\u200c\u034f\u00a0\u00ad\u200b]+/g, ' ').trim(); if (t) td.setAttribute('data-qa-text', t.slice(0, 60)); });
          document.querySelectorAll('style,link,meta[name="color-scheme"],meta[name="supported-color-schemes"]').forEach(e => e.remove());
          document.querySelectorAll('[class]').forEach(e => e.removeAttribute('class'));
          if (mode === 'gmailtrim') {
            const main = document.querySelector('table[width="600"]') || document.querySelector('table table');
            const rows = main ? [...main.querySelectorAll(':scope > tbody > tr, :scope > tr')] : [];
            const cut = rows.slice(Math.max(1, rows.length - 3));   // laatste rijen: knop/P.S./footer, het deel dat Gmail als herhaling inklapt
            if (cut.length) {
              const html = cut.map(r => r.outerHTML).join('');
              cut.forEach(r => r.remove());
              const dots = document.createElement('div'); dots.textContent = '\u2022\u2022\u2022'; dots.setAttribute('data-qa-dots', '1');
              dots.style.cssText = 'font:16px Arial;color:#888;padding:6px 12px;';
              const box = document.createElement('div'); box.setAttribute('data-qa-trimmed', '1'); box.innerHTML = html;   // parser laat losse tr/td vallen
              document.body.appendChild(dots); document.body.appendChild(box);
            }
          }
          return new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
        }, j.mode);
        let gmailScale = 1;
        if (j.mode === 'gmailios' || j.mode === 'gmailtrim') {   // Gmail schaalt een mail die breder is dan het scherm in: leg hem op zijn eigen breedte op en meld de schaal
          const sw = await p.evaluate(() => Math.max(document.documentElement.scrollWidth, document.body.scrollWidth));
          if (sw > j.width + 1) { gmailScale = j.width / sw; await p.setViewportSize({ width: sw, height: 900 }); }
        }
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
            if (mode === 'forced' || mode === 'apple' || !/unsubscribe|preferences|afmelden/i.test(t + ' ' + h) || !vis(a) || !t) continue;
            const fg = parse(getComputedStyle(a).color), bg = bgOf(a);
            out.unsubContrast.push({ t, ratio: +ratio(fg, bg).toFixed(2), fg: css(fg), bg: css(bg), mode });
          }
          if (mode === 'gmailios' || mode === 'gmailtrim') {
            out.emptyCells = []; out.gmailContrast = [];
            for (const td of document.querySelectorAll('td[data-qa-text]')) {
              if (!vis(td)) continue;
              const want = td.getAttribute('data-qa-text'); const r = td.getBoundingClientRect();
              const got = (td.innerText || '').replace(/\s+/g, ' ').trim();
              if (!got || r.width < 2 || r.height < 2) { out.emptyCells.push('cel rendert leeg: "' + want.slice(0, 50) + '"'); continue; }
              // tekst die buiten de cel valt of in een kolom van < 48 px wordt geperst
              const tw = document.createTreeWalker(td, NodeFilter.SHOW_TEXT); let n, outside = 0, inside = 0;
              while ((n = tw.nextNode())) {
                if (!n.nodeValue.trim() || !vis(n.parentElement)) continue;
                const rg = document.createRange(); rg.selectNodeContents(n);
                for (const q of rg.getClientRects()) { if (q.width < 1) continue; (q.right > r.right + 3 || q.left < r.left - 3 || q.bottom > r.bottom + 3 || q.top < r.top - 3) ? outside++ : inside++; }
              }
              if (outside && !inside) out.emptyCells.push('tekst staat buiten de cel: "' + want.slice(0, 50) + '"');
              else if (r.width < 48 && want.length > 24 && !td.querySelector('td')) out.emptyCells.push('tekst in een kolom van ' + Math.round(r.width) + ' px geperst: "' + want.slice(0, 50) + '"');
            }
            const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n; const seen = new Set();
            while ((n = tw.nextNode())) {
              const t = n.nodeValue.replace(/[\s\u200c\u00a0\u034f\u00ad]+/g, ' ').trim(); if (t.length < 2) continue;
              const el = n.parentElement; if (!el || seen.has(el) || !vis(el) || el.closest('[data-qa-dots]')) continue; seen.add(el);
              const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
              const fg = parse(getComputedStyle(el).color); if (!fg) continue; const bg = bgOf(el); const cr = ratio(fg, bg);
              if (cr < 3) out.gmailContrast.push({ t: t.slice(0, 40), ratio: +cr.toFixed(2), fg: css(fg), bg: css(bg), trimmed: !!el.closest('[data-qa-trimmed]') });
            }
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
        if (j.mode === 'gmailios' || j.mode === 'gmailtrim') { m.gmailScale = +gmailScale.toFixed(3); m.scrollWidth = Math.round(m.scrollWidth * gmailScale); m.vw = j.width; }
        res[j.key] = Object.assign({ width: j.width, mode: j.mode }, m);
      } catch (e) { res[j.key] = { width: j.width, mode: j.mode, error: String(e).slice(0, 300), scrollWidth: 0, vw: j.width }; }
      await ctx.close();
    }
  }
  await Promise.all([worker(), worker(), worker(), worker()]);
  await normal.close(); await forced.close();
  fs.writeFileSync(outFile, JSON.stringify(res));
})();
