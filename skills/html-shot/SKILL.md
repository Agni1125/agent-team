---
name: html-shot
description: 把 HTML 檔案或網頁截成整頁圖片,並可直接貼到 Discord 頻道讓 Owner 一眼看完內容。當任務產出了 HTML(報告、A+ 版面、設計稿、圖表頁)需要給人看、或使用者說「截圖給我」「貼到 Discord」「傳到聊天室」「我要用看的」時使用。也可用於任何本機 HTML 的視覺驗收。關鍵字:截圖、screenshot、貼圖、傳到聊天室、Discord、預覽、HTML 預覽、整頁截圖。
---

# html-shot:HTML 截圖並送進 Discord

產出 HTML 之後**不要只給檔案路徑**。Owner 要的是打開 Discord 就看得到內容。

## 兩步

### 1. 截圖(整頁,不是只截視窗)

```bash
node "~/.claude/skills/html-shot/scripts/shot.mjs" <html檔> <輸出png> [寬度] [--dark]
```

- 用系統既有的 Chrome / Edge,**不會下載 Chromium**
- `fullPage: true`,整頁捲到底一次拍完
- 寬度預設 `1280`。手機版視覺用 `430`,寬版報表用 `1440`
- `--dark` 模擬深色模式(頁面若有 `prefers-color-scheme` 才有差)
- 回傳 JSON:`{ok, out, width, pageHeight, sizeKB}`

### 2. 貼到 Discord

```bash
python "~/.claude/skills/html-shot/scripts/post.py" <圖片> "說明文字"
```

- 預設頻道由環境變數 `DISCORD_DEFAULT_CHANNEL_ID` 指定。要換頻道加 `--channel <id>`
- token 從 `tcc-agent/.env` 讀,**不寫死、不印出**
- 回傳 JSON:`{ok, message_id, channel_id, attachments}`

## 說明文字要寫什麼

Owner 看圖之前先看到這行,所以要能回答「這是什麼、我該看哪裡」。

好:`SPACION A+ 模組三版比較,左起 A/B/C。B 版的規格表移到第二屏,想確認這樣會不會太晚出現。`

不好:`附上截圖,請查收。`

## 注意

- **超過 10MB 會被 Discord 擋掉。** 長報表先降寬度(例如 `1024`)重截,或分段截。腳本會直接報錯不會靜默失敗。
- 頁面有動畫或延遲載入時,截到的是 400ms 後的狀態。需要特定互動後的畫面,先改 HTML 的預設狀態再截。
- **外部資源(CDN 字體、遠端圖片)在離線時不會出現。** 截完自己看一眼有沒有破圖再送。
- 圖片一送出就在頻道裡了,**送出前先確認畫面上沒有金鑰、帳號、客戶個資或不該外流的數字。**

## 典型用法

產出 `report.html` 之後:

```bash
node ".../shot.mjs" "C:/.../report.html" "~/Desktop/report.png" 1280
python ".../post.py" "~/Desktop/report.png" "競品分析報告,重點在第三張圖的自然流量交叉"
```
