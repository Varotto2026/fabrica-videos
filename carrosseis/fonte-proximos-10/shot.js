const { chromium } = require('playwright'); const fs = require('fs');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
 const man = JSON.parse(fs.readFileSync('manifest.json')); const bad = [];
 for (const m of man) for (let i = 1; i <= m.n; i++) {
   await p.goto('file://' + process.cwd() + `/${m.dir}/slide${i}.html`); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
   const r = await p.evaluate(() => { const w = document.getElementById('w').getBoundingClientRect(); const e = document.querySelector('.ebook'); const btn = document.querySelector('.btn');
     return { bottom: w.bottom, right: w.right, eb: e ? e.getBoundingClientRect().top : null, btn: btn ? btn.getBoundingClientRect().bottom : null }; });
   const limit = i === 1 ? 740 : 1180;
   if (r.bottom > limit || (r.btn && r.btn > 760)) bad.push(`${m.dir}/${i} bottom=${Math.round(r.bottom)} btn=${r.btn && Math.round(r.btn)}`);
   await p.screenshot({ path: `${m.dir}/slide${i}.png` });
 }
 console.log('BAD', JSON.stringify(bad, null, 1)); await b.close(); })();
