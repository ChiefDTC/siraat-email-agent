// Prototype dark mode (13-darkmode.md): screenshots van before/ en after/ in vijf weergaven, 375 px breed.
// Gebruik: PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node research/v6-golive/darkmode/sim_shots.js
//   light    gewone weergave
//   apple    prefers-color-scheme: dark (Apple Mail iOS/macOS, Outlook Mac): de client volgt color-scheme en de eigen CSS
//   algo     Chromium auto-dark (WebContentsForceDark). Benadering van Android-webviews (Gmail Android, Samsung) die algoritmisch donker maken.
//            Let op: Chromium volgt 'only light'. Of Gmail dat nu ook doet, is per sept 2026 gemeld maar niet bevestigd (zie 13-darkmode.md).
//   partial  simulatie Outlook.com / Outlook iOS+Android (en Gmail Android oud): lichte achtergronden donker, donkere tekst licht,
//            background-image en beelden blijven; zet data-ogsb/data-ogsc op wat het omzet (zoals Outlook.com). Negeert color-scheme.
//   full     simulatie Gmail iOS (oud gedrag) / Outlook Windows: alle tekst- en achtergrondkleuren omgekeerd, background-image en beelden blijven,
//            body omgebouwd naar <u></u><div class="body"> zoals Gmail. Negeert color-scheme en <style>-trucs voor Outlook.
// Inversie: HSL-lichtheid omgekeerd, begrensd op 7 en 93 procent (zelfde aanname als research/deliverability/01-inbox-check.md).
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path = require('path'); const fs = require('fs');
const D = __dirname; const OUT = path.join(D, 'shots');
const MODES = ['light', 'apple', 'algo', 'partial', 'full'];
function sim(mode) {
  const parse = c => { const m = c && c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const v = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; };
  const toHsl = ([r, g, b]) => { r /= 255; g /= 255; b /= 255; const mx = Math.max(r, g, b), mn = Math.min(r, g, b); let h = 0, s = 0; const l = (mx + mn) / 2;
    if (mx !== mn) { const d = mx - mn; s = l > .5 ? d / (2 - mx - mn) : d / (mx + mn); h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6; } return [h, s, l]; };
  const toRgb = ([h, s, l]) => { if (!s) return [l, l, l].map(x => Math.round(x * 255)); const q = l < .5 ? l * (1 + s) : l + s - l * s, p = 2 * l - q;
    const f = t => { t = (t + 1) % 1; return t < 1 / 6 ? p + (q - p) * 6 * t : t < .5 ? q : t < 2 / 3 ? p + (q - p) * (2 / 3 - t) * 6 : p; }; return [f(h + 1 / 3), f(h), f(h - 1 / 3)].map(x => Math.round(x * 255)); };
  const inv = c => { const [h, s, l] = toHsl(c); return 'rgb(' + toRgb([h, s, Math.min(.93, Math.max(.07, 1 - l))]).join(',') + ')'; };
  const L = c => toHsl(c)[2];
  if (mode === 'full') {   // Gmail-structuur: <u></u><div class="body">
    const wrap = document.createElement('div'); wrap.className = 'body'; while (document.body.firstChild) wrap.appendChild(document.body.firstChild);
    document.body.appendChild(document.createElement('u')); document.body.appendChild(wrap);
    // Outlook-<style> met [data-og*] bestaat hier niet (Gmail iOS en Outlook Windows doen niets met attribuutselectoren)
  }
  const els = [document.body, ...document.body.querySelectorAll('*')];
  // alleen kleuren die het element zelf zet (inline, bgcolor, <a> uit de stijlregel a{}), net als de clients: overerving loopt vanzelf mee
  const plan = els.map(e => { const s = getComputedStyle(e); const own = e === document.body;
    return { e, bg: (own || e.style.backgroundColor || e.hasAttribute('bgcolor')) ? parse(s.backgroundColor) : null, fg: (own || e.style.color || e.tagName === 'A' || e.hasAttribute('color')) ? parse(s.color) : null }; });
  for (const { e, bg, fg } of plan) {
    if (bg && bg[3] > 0.5) {
      const change = mode === 'full' ? true : L(bg) > 0.5;
      if (change) { e.style.setProperty('background-color', inv(bg)); e.removeAttribute('bgcolor'); if (mode === 'partial') e.setAttribute('data-ogsb', ''); }
    }
    if (fg) {
      const change = mode === 'full' ? true : L(fg) < 0.5;
      if (change) { e.style.setProperty('color', inv(fg)); if (mode === 'partial') e.setAttribute('data-ogsc', ''); }
    }
  }
  if (getComputedStyle(document.body).backgroundColor === 'rgba(0, 0, 0, 0)') document.body.style.backgroundColor = 'rgb(18,18,18)';
}
(async () => {
  const exe = '/opt/pw-browsers/chromium';
  const normal = await chromium.launch({ executablePath: exe });
  const forced = await chromium.launch({ executablePath: exe, args: ['--enable-features=WebContentsForceDark', '--force-dark-mode'] });
  fs.mkdirSync(OUT, { recursive: true });
  const jobs = [];
  for (const dir of ['before', 'after']) for (const f of fs.readdirSync(path.join(D, dir)).filter(x => x.endsWith('.html'))) for (const m of MODES) jobs.push({ dir, f, m });
  for (const j of jobs) {
    const b = j.m === 'algo' ? forced : normal;
    const ctx = await b.newContext({ colorScheme: j.m === 'light' ? 'light' : 'dark', viewport: { width: 375, height: 900 }, deviceScaleFactor: 1 });
    await ctx.route(/^https?:/, r => r.abort());   // geen webfonts/netwerk: Arial-terugval, zoals Gmail
    const p = await ctx.newPage();
    await p.goto('file://' + path.join(D, j.dir, j.f), { waitUntil: 'load' });
    if (j.m === 'partial' || j.m === 'full') await p.evaluate(sim, j.m);
    const shot = path.join(OUT, `${j.f.replace('.html', '')}-${j.dir}-${j.m}.jpg`);
    await p.screenshot({ path: shot, fullPage: true });
    await ctx.close(); console.log('ok', shot);
  }
  await normal.close(); await forced.close();
})();
