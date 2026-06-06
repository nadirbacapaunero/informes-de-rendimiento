// Renders logo-*.html to 1080x1080 PNGs. Files starting with "logo-mark" or "logo-lockup" get transparent bg.
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const DIR = __dirname;
const S = 1080, SCALE = 2;
(async () => {
  const files = fs.readdirSync(DIR).filter(f => f.startsWith('logo-') && f.endsWith('.html'));
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox','--force-color-profile=srgb','--hide-scrollbars'] });
  for (const file of files) {
    const transparent = !file.includes('profile');
    const wide = file.includes('lockup');
    const w = wide ? 1600 : S, h = wide ? 520 : S;
    const page = await browser.newPage();
    await page.setViewport({ width: w, height: h, deviceScaleFactor: SCALE });
    await page.goto('file:///' + path.join(DIR, file).replace(/\\/g,'/'), { waitUntil: 'networkidle0' });
    await page.evaluate(async () => { if (document.fonts) await document.fonts.ready; });
    await new Promise(r => setTimeout(r, 300));
    const out = path.join(DIR, file.replace('.html','.png'));
    await page.screenshot({ path: out, type: 'png', omitBackground: transparent, clip: { x:0, y:0, width:w, height:h } });
    console.log('rendered', out, transparent ? '(transparent)' : '(navy)');
    await page.close();
  }
  await browser.close();
})();
