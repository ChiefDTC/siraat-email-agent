# 05 · Visuele site-check: wat gedaan is en wat nog moet

Stand: 7 oktober 2026, 17:00. siraatskitchen.com werd later op de dag bereikbaar. Een deel van de check is gedaan (A), een deel kon niet in deze omgeving (B): een product in de winkelwagen leggen en de checkout openen werd door de permissieregels geweigerd, omdat dat een handeling in de gekoppelde winkel is. B moet door Floris of een developer worden gedaan, met een echte telefoon of met het script hieronder op een machine waar dat mag. Niets bestellen.

## A. Gedaan (resultaten in 02 en 03)

Profielen: iPhone 390x844 (iOS Safari user agent, DPR 2), desktop 1440x900, Android Chrome (Pixel 7, 412x915), Facebook in-app (FBAN/FBIOS, FBAV), Instagram in-app. Chromium via Playwright, door de proxy, geen netwerkvertraging gesimuleerd.

| Pagina | iPhone | Desktop | Android, FB, IG |
|---|---|---|---|
| Home | ja | ja | ja |
| Pan Pro Standard, Large, Small, Mini | ja | ja | Standard |
| 6-set hoofdlisting en BDAY | ja | ja | BDAY |
| 12-set | ja | ja | ja |
| Pot Set 6-Pcs | 404 | 404 | |
| Deep, Pizza, Roasting, Apron (Oak) | ja | ja | |
| Collecties all, bundles, cookware, warehouse-clearance | ja | ja | |
| /cfv6 (advertentie-URL) | 404 | 404 | |
| Lege winkelwagen | ja | ja | |
| Discount-links `/discount/HI10?redirect=/cart`, `?redirect=/products/<pan>`, naar BDAY, en een niet-bestaande code `K3_10_48H` | ja | ja | |

Bestanden: `research/cro/screens/<profiel>-<pagina>-fold.jpg` (eerste scherm) en `-full.jpg` (hele pagina, verkleind), `screens/<profiel>-disc-*.jpg` (discount-links). Paginatekst: `research/cro/screens-text/<profiel>-<pagina>.txt`. Meetwaarden: `screens-text/metrics-iphone.json`, `metrics-desktop.json`, `metrics-<android|fbapp|igapp>-part.json`, `discount-links.json`.

Belangrijkste meetwaarden (lab): PDP `load` 2,6 tot 4,7 s (desktop Pan Pro Standard één keer 8,6 s), LCP 0,7 tot 2,8 s, CLS 0 tot 0,02 (Android op de sets 0,055 en 0,062), 2,3 tot 3,0 MB per PDP, home mobiel 5,4 MB, 280 tot 324 requests, 174 scripts van 22 externe domeinen op de Pan Pro. Geen horizontale scroll op 390 breed. Countdown op elke verse sessie 02:42:5x.

## B. Nog te doen (handmatig of met het script op een toegestane machine)

Gebruik een testprofiel zonder echte gegevens. Vul in de checkout alleen in wat nodig is om het volgende scherm te zien (een testmailadres zoals `cro-test@example.com` en een bestaand voorbeeldadres van een openbaar gebouw), en stop vóór de betaalknop. Nooit "Pay now" of een express-knop indrukken.

| # | Check | Wat goed is | Wat fout is | Waar het over gaat |
|---|---|---|---|---|
| 1 | Pan Pro Standard in de winkelwagen (iPhone en desktop): drawer en /cart | Pan bovenaan, gifts samengevat ("4 free gifts included"), besparing in dollars, termijnregel, trust-regel, checkout-knop boven de vouw | Drie of vier $0-regels boven de pan, "Purifier" in een regelnaam, geen besparing, knop onder de vouw | 03 par. 5; QA-rapport A3 (in 60 % van de checkouts staan gift-regels eerst) |
| 2 | 12-set en 6-set in de winkelwagen | Prijs gelijk aan PDP ($599, $349) | Prijssprong. Ticket 89741682: "3 pcs pro set ($499) but when checkout it appeared as $699" | 02, 03 |
| 3 | Checkout openen vanuit de winkelwagen | Express-knoppen (Shop Pay, PayPal, Google Pay; Apple Pay op echte iPhone), codeveld, verzending "Free", levertijd, totaal gelijk aan cart | Extra kosten, duties-regel bij EU-adres, andere valuta dan op de PDP | 03 par. 2, 3, 6 |
| 4 | Discount-link `/discount/HI10?redirect=/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern`, dan in cart, dan checkout | HI10 zichtbaar in cart of checkout, 10 % eraf, gifts blijven $0 | Code verdwijnt, melding "can't be combined", of gifts worden betaald | 03 par. 4, fix 8 |
| 5 | Zelfde met SIRAAT10 en met een flowcode (na aanmaken in Klaviyo) | idem | idem | |
| 6 | Checkout-recovery: een eigen test-checkout verlaten, de recovery-URL uit Klaviyo openen op een tweede apparaat met `&discount=HI10` | Zelfde cart, korting toegepast | Lege cart, code geweigerd | 03 par. 8 |
| 7 | Cart op ander apparaat: product in cart op telefoon, dan op desktop `/cart` openen | Verwacht: leeg. Dat is de reden om in mails permalinks te gebruiken | | 03 par. 8 |
| 8 | EU-adres (bijvoorbeeld Italië) en AU-adres in de checkout invullen tot aan de verzendstap | Prijs in eigen valuta, "duties included" of geen extra kosten, BNPL (Afterpay in AU) | Duties te betalen bij levering, USD-bedragen, geen BNPL | 03 par. 6 |
| 9 | Echte iPhone Safari, tweede bezoek | Directe pagina | Omweg via `shop.app/accounts/sur` die merkbaar laadt | 02, 03 |
| 10 | Echte Facebook- en Instagram-app: advertentie of link openen, product in cart, checkout | Shop Pay werkt in de in-app browser, cart blijft bestaan bij "open in Safari" | Login-lus bij Shop Pay, cart leeg na openen in Safari | 01 (paid social 40 % van de sessies) |
| 11 | Aftersell na een testorder (alleen in Shopify test mode of met een 100 %-testcode die daarna direct wordt verwijderd, en alleen door Floris) | Upsell past bij de aankoop, duidelijke "No thanks", bevestiging boven $300 | 12-set aan niet-US, per ongeluk geaccepteerd | 03 par. 7 |
| 12 | Snelheid op echt mobiel netwerk (Lighthouse mobiel, Slow 4G) op Pan Pro en home | LCP onder 2,5 s | Boven 2,5 s door scripts | 02 |

## C. Playwright-script (voor B, op een machine waar het mag)

Hetzelfde opzet als de check van vandaag; alleen kijken, stoppen vóór betalen. Pas `ALLOW_CART` alleen aan na akkoord van Floris.

```js
// node cro-check.js iphone
const { chromium, devices } = require('playwright');
const ALLOW_CART = false; // alleen true na akkoord, nooit betalen
const BASE = 'https://siraatskitchen.com';
const PDP = '/products/original-siraat-100-pure-titanium-pan-with-hammered-pattern';
const profiles = {
  iphone: { ...devices['iPhone 13'], viewport: { width: 390, height: 844 } },
  desktop: { viewport: { width: 1440, height: 900 } },
  fbapp: { ...devices['iPhone 13'], userAgent: devices['iPhone 13'].userAgent + ' [FBAN/FBIOS;FBAV/498.0.0.37.106]' },
};
(async () => {
  const prof = process.argv[2] || 'iphone';
  const browser = await chromium.launch();
  const ctx = await browser.newContext(profiles[prof]);
  await ctx.addInitScript(() => { window.__cls = 0; new PerformanceObserver(l => l.getEntries().forEach(e => { if (!e.hadRecentInput) window.__cls += e.value; })).observe({ type: 'layout-shift', buffered: true }); });
  const page = await ctx.newPage();
  await page.goto(BASE + '/discount/HI10?redirect=' + PDP, { waitUntil: 'load' });
  await page.screenshot({ path: `${prof}-1-pdp-with-code.png` });
  if (!ALLOW_CART) return browser.close();
  await page.locator('form[action*="/cart/add"] button[type=submit]').first().click();
  await page.waitForTimeout(3000); await page.screenshot({ path: `${prof}-2-drawer.png` });
  await page.goto(BASE + '/cart'); await page.screenshot({ path: `${prof}-3-cart.png`, fullPage: true });
  console.log(await page.evaluate(async () => (await (await fetch('/cart.js')).json())));
  await page.locator('button[name="checkout"]').first().click();
  await page.waitForURL(/checkouts/); await page.waitForTimeout(6000);
  await page.screenshot({ path: `${prof}-4-checkout.png`, fullPage: true });
  console.log('CLS', await page.evaluate(() => window.__cls));
  // stop hier: niets invullen behalve indien nodig een testadres, nooit betalen
  await browser.close();
})();
```

Te loggen per stap: URL, `cart.js` (totaal, korting per regel, `cart_level_discount_applications`), zichtbare tekst rond "discount", "HI10", "duties", "installments", en de screenshot.
