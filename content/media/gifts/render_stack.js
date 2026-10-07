// Renders final/gift-free-shipping.png (icon tile) and final/gift-stack-preview.png (brand-coloured 4-gift block, 600px @2x).
// Run: node render_stack.js  after python3 -I build_gifts.py
const fs = require('fs'), path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const HERE = __dirname, F = n => 'data:image/' + (n.endsWith('.png') ? 'png' : 'jpeg') + ';base64,' + fs.readFileSync(path.join(HERE, 'final', n)).toString('base64');
const truck = fs.readFileSync(path.join(HERE, '..', 'icons', 'svg', 'brick', 'free-shipping.svg'), 'utf8');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  // 1. free shipping tile
  let page = await browser.newPage({ viewport: { width: 600, height: 600 }, deviceScaleFactor: 2 });
  await page.setContent(`<body style="margin:0"><div id="t" style="width:600px;height:600px;background:#F8F7F2;display:flex;align-items:center;justify-content:center">
    <div style="width:380px;height:380px;border-radius:50%;background:#FFFFFF;border:2px solid #ECE7DD;display:flex;align-items:center;justify-content:center">
    ${truck.replace('width="24" height="24"', 'width="230" height="230"')}</div></div></body>`);
  await page.locator('#t').screenshot({ path: path.join(HERE, 'final', 'gift-free-shipping.png') });
  await page.close();
  // 2. stack preview
  const tile = (img, title, value, fit) => `<td style="width:25%;padding:0 5px;vertical-align:top;text-align:center">
     <div style="background:#FFFFFF;border:1px solid #ECE7DD;border-radius:8px;height:128px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;overflow:hidden">
     <img src="${img}" style="max-width:100%;width:${fit}px;height:${fit}px;object-fit:contain"></div>
     <div style="font:600 13px/1.3 Inter,Arial,sans-serif;color:#282828;margin-top:10px">${title}</div>
     <div style="font:400 12px/1.3 Inter,Arial,sans-serif;color:#AC3B19;margin-top:4px">${value}</div></td>`;
  page = await browser.newPage({ viewport: { width: 600, height: 400 }, deviceScaleFactor: 2 });
  await page.setContent(`<body style="margin:0"><div id="s" style="width:600px;background:#F8F7F2;padding:28px 18px 30px;box-sizing:border-box">
    <div style="font:600 11px/1 Inter,Arial,sans-serif;letter-spacing:.14em;color:#AC3B19;text-align:center">4 FREE GIFTS WITH EVERY ORDER</div>
    <div style="font:italic 300 26px/1.2 Georgia,serif;color:#282828;text-align:center;margin:10px 0 22px">Over $70 in guaranteed gift value</div>
    <table style="width:100%;border-collapse:collapse;table-layout:fixed"><tr>
    ${tile(F('gift-free-shipping.png'), 'Free Shipping', '$15 value', 128)}
    ${tile(F('gift-ebook-mockup.png'), 'Plastic&#8209;Free Home E&#8209;Book', '$30 value', 150)}
    ${tile(F('gift-mystery-cutout.png'), 'Mystery Gift', '$25 value', 150)}
    ${tile(F('gift-purifier.png'), 'Win a PFAS Water Purifier', '$450 value<br>5 winners a week', 140)}
    </tr></table></div></body>`);
  await page.locator('#s').screenshot({ path: path.join(HERE, 'final', 'gift-stack-preview.png') });
  await browser.close(); console.log('ok');
})();
