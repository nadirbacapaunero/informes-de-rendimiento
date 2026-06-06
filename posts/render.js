// Renders each *.html in this folder to a pixel-exact 1080x1350 PNG (2x for crispness)
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const DIR = __dirname;
const W = 1080, H = 1350, SCALE = 2;

(async () => {
  const files = fs.readdirSync(DIR).filter(f => f.endsWith('.html'));
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--no-sandbox', '--force-color-profile=srgb', '--hide-scrollbars']
  });
  for (const file of files) {
    const page = await browser.newPage();
    await page.setViewport({ width: W, height: H, deviceScaleFactor: SCALE });
    await page.goto('file:///' + path.join(DIR, file).replace(/\\/g, '/'), { waitUntil: 'networkidle0' });
    await page.evaluate(async () => { if (document.fonts) await document.fonts.ready; });
    await new Promise(r => setTimeout(r, 400));
    const out = path.join(DIR, file.replace('.html', '.png'));
    await page.screenshot({ path: out, type: 'png', clip: { x: 0, y: 0, width: W, height: H } });
    console.log('rendered', out);
    await page.close();
  }
  await browser.close();
})();
