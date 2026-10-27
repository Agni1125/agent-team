---
name: gen-image
description: 用 DMXAPI 實際產生圖片(文生圖 / 圖生圖 / 多圖融合),把提示詞變成真的 PNG 檔。當任務要「生圖」「出圖」「做主圖」「做 A+ 圖」「把提示詞跑成圖片」時使用。amazon-main-image 與 amazon-aplus-image 產出提示詞之後,一律接這個 skill 把圖生出來 —— Owner 要的是圖,不是提示詞文件。關鍵字:生圖、出圖、產圖、圖片生成、seedream、即夢、圖生圖、多圖融合。
---

# gen-image:把提示詞跑成真的圖

**Owner 要的交付物是圖片,不是 markdown 提示詞檔。** 產出提示詞只是中間步驟,沒生成圖片等於沒交付。

## 用法

單張:

```bash
python "~/.claude/skills/gen-image/scripts/gen.py" \
  --prompt "..." --out "C:/.../out.png" \
  --ref "C:/.../產品照.jpg" --ref "C:/.../參考圖.jpg" \
  --ratio 4:3 --model seedreampro
```

批次(A+ 六模組一次跑完):

```bash
python ".../gen.py" --batch prompts.json --outdir "C:/.../imgs"
```

`prompts.json` 格式:

```json
[
  {"prompt": "...", "out": "01-hero.png", "ratio": "16:9", "ref": ["產品照.jpg"]},
  {"prompt": "...", "out": "02-texture.png", "ratio": "1:1"}
]
```

## 模型怎麼選

| `--model` | 實際模型 | 用在哪 |
|---|---|---|
| `seedreampro`(預設) | `doubao-seedream-5-0-pro-260628` | **A+ 與主圖用這個**。支援圖生圖與多圖融合 |
| `seedream` | `doubao-seedream-5.0-lite` | 便宜,品質略低,試版型用 |
| `wan` | `wan2.7-image` | 阿里萬象,備援 |

**電商素材一律帶 `--ref` 產品照。** 純文生圖會把商品重畫,比例、文字、孔洞全跑掉 —— Owner 明確禁止這件事。

## 三種模式(同一個端點,差在 `image` 欄位)

- **文生圖** — 不帶 `--ref`
- **圖生圖** — 一個 `--ref`(保住商品本體,只換場景/光線)
- **多圖融合** — 兩個以上 `--ref`(產品照 + 風格參考圖,最多 10 張)

本機圖會自動轉成 data URL 送出,因為 DMXAPI 的伺服器連不到你的本機路徑。

## 硬規則

- **不要停下來問可不可以生。** Owner 交辦圖片任務時費用已預先授權,直接跑到出圖。`--dry-run` 只在你改了 payload 結構時才需要;正常交付流程不必先 dry-run。
- 批次前先單張試一張確認風格,對了再全跑 —— 這是為了少浪費,不是為了等人核准。
- 上限:單次任務 30 張,或估計 US$5。超過才回報。
- 金鑰讀環境變數 `DMXAPI_API_KEY`,**不寫死、不印出、不寫進任何檔案**。
- 生成失敗會回 `{"ok": false, "error": ...}`,**不會靜默產出空檔**。
- 生完**自己開圖看一眼**再交付:商品比例對不對、文字有沒有變形、孔洞吊繩在不在、產品跟背景有沒有融合。Owner 對這幾點會逐項檢查。

## 交付流程

生完圖直接貼 Discord,不要只回檔案路徑:

```bash
python "~/.claude/skills/html-shot/scripts/post.py" <圖片> "說明"
```
