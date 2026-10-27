/**
 * HTML -> 整頁 PNG。用系統既有的 Chrome,不下載 Chromium。
 *
 *   node shot.mjs <html檔或URL> <輸出png> [寬度] [--dark]
 */
import puppeteer from "puppeteer-core";
import { existsSync, statSync } from "node:fs";
import { pathToFileURL } from "node:url";

const CHROME = [
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
].find(existsSync);

if (!CHROME) {
  console.error("找不到 Chrome 或 Edge");
  process.exit(1);
}

const [input, out, widthArg, ...rest] = process.argv.slice(2);
if (!input || !out) {
  console.error("用法: node shot.mjs <html或url> <out.png> [寬度] [--dark]");
  process.exit(1);
}
const width = parseInt(widthArg || "1280", 10);
const dark = rest.includes("--dark");

const url = /^https?:\/\//.test(input) ? input : pathToFileURL(input).href;

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: "new",
  args: ["--no-sandbox", "--disable-dev-shm-usage", "--hide-scrollbars"],
});

try {
  const page = await browser.newPage();
  await page.emulateMediaFeatures([
    { name: "prefers-color-scheme", value: dark ? "dark" : "light" },
  ]);
  await page.setViewport({ width, height: 900, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

  // 捲動淡入特效(.reveal{opacity:0} + IntersectionObserver)在整頁截圖時是災難:
  // fullPage 是一次展開拍照,首屏外的元素從沒進過 viewport,observer 不會觸發,
  // 永遠停在 opacity:0 —— 截出來就是「只有上面一小塊有東西,下面全空白」。
  // 解法:先真的捲一遍讓 observer 全部觸發,再用 CSS 強制把所有動畫關掉收尾。
  await page.evaluate(async () => {
    const step = Math.max(200, window.innerHeight * 0.8);
    for (let y = 0; y < document.body.scrollHeight; y += step) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 60));
    }
    window.scrollTo(0, 0);
  });
  await page.addStyleTag({
    content:
      "*,*::before,*::after{" +
      "animation:none!important;" +
      "transition:none!important;" +
      "opacity:1!important;" +
      "transform:none!important;" +
      "visibility:visible!important;" +
      "}",
  });

  // 等字體與延遲渲染的內容
  await page.evaluate(() => document.fonts && document.fonts.ready);
  await new Promise((r) => setTimeout(r, 400));

  await page.screenshot({ path: out, fullPage: true, type: "png" });

  const { height } = await page.evaluate(() => ({
    height: document.documentElement.scrollHeight,
  }));
  const kb = Math.round(statSync(out).size / 1024);
  console.log(JSON.stringify({ ok: true, out, width, pageHeight: height, sizeKB: kb }));
} finally {
  await browser.close();
}
