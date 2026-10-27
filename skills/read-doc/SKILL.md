---
name: read-doc
description: 讀取並分析上傳的 Excel / Word / PDF / CSV 檔案。當任務提到「主理人上傳的檔案」、收到 .xlsx .xls .docx .pdf .csv 路徑、或要求「分析這份報表 / 這份文件 / 這個 PDF」時使用。Claude 的 Read 工具讀得動 PDF 與純文字,但讀不動二進位的 .xlsx 與 .docx —— 那兩種一律走這個 skill。關鍵字:Excel、試算表、報表、Word、文件、PDF、附件、inbox、上傳的檔案、資料分析。
---

# read-doc — 讀懂上傳的檔案

Discord 上傳的檔案會落在 `tcc-agent/inbox/YYYYMMDD/<timestamp>_<原檔名>`,
路徑會直接寫在主理人的訊息後面。

## 先判斷格式,不要每種都用同一招

| 副檔名 | 怎麼讀 |
|---|---|
| `.pdf` | **直接用 Read 工具**,帶 `pages` 參數。不需要任何套件 |
| `.txt` `.md` `.json` `.csv` | 直接用 Read 工具 |
| `.xlsx` `.xlsm` `.xls` | Read 讀不動,**跑 Python**(見下) |
| `.docx` | Read 讀不動,**跑 Python**(見下) |
| 圖片 | 直接用 Read 工具 |

PDF 超過 10 頁時 `pages` 是必填,一次最多 20 頁。長 PDF 先讀前幾頁抓結構,
確定要看哪一段再讀那一段,不要整份硬拉進來。

## Excel

已裝好 `openpyxl` 與 `pandas`。**先探結構,再決定怎麼分析** —— 不要一上來就 `read_excel()` 全部吃進來。

```python
import pandas as pd
xl = pd.ExcelFile(PATH)
print(xl.sheet_names)
for s in xl.sheet_names:
    df = xl.parse(s, nrows=5)
    print(s, df.shape, list(df.columns))
```

看完欄位再讀需要的 sheet。要點:

- **表頭不一定在第 0 列。** 前幾列常是標題或說明,用 `header=` 指定。
- **合併儲存格**在 pandas 會變成 `NaN`,需要時用 `df.ffill()` 補。
- 數字欄位常被存成字串(有千分位、貨幣符號、百分比),算之前先清:
  `pd.to_numeric(df[c].astype(str).str.replace(r"[,$%\s]", "", regex=True), errors="coerce")`
- 日期用 `pd.to_datetime(..., errors="coerce")`,不要自己 parse。
- 大檔先看 `df.shape`,超過幾十萬列就用 `usecols` 只取需要的欄。

需要讀公式、儲存格顏色或註解時才用 `openpyxl`(`load_workbook(PATH, data_only=True)`
拿計算後的值,`data_only=False` 拿公式本身)。

## Word

已裝好 `python-docx`。

```python
from docx import Document
d = Document(PATH)
for p in d.paragraphs:
    if p.text.strip():
        print(p.style.name, "|", p.text)
for t in d.tables:
    for row in t.rows:
        print([c.text.strip() for c in row.cells])
```

`d.paragraphs` **不含**表格裡的文字,兩個都要跑過才算讀完整份。
標題層級看 `p.style.name`(Heading 1 / Heading 2)。

## PDF 的補充手段

Read 工具是把頁面當影像看,版面複雜或要精確抓表格時,改用已裝好的 `pdfplumber`:

```python
import pdfplumber
with pdfplumber.open(PATH) as pdf:
    print("頁數", len(pdf.pages))
    print(pdf.pages[0].extract_text())
    for t in pdf.pages[0].extract_tables():
        print(t)
```

掃描件(影像 PDF)`extract_text()` 會回空字串 —— 那種只能用 Read 工具看圖,
**不要假裝讀到了**。

## 交付規矩

1. **先講結論再給數字。** 主理人要的是判斷,不是欄位清單。
2. **口徑一定要標:** 資料來源檔名、日期範圍、單位、幣別。
   第三方估算標 `Estimated`,後台真實數據標 `Actual`,兩者不可混用。
3. **相關性不可以寫成因果。**
4. 讀不到就直說讀不到、為什麼,不要用推測填空。
5. 檔案裡有帳號、密碼、金鑰、身分證號、銀行資訊時,**不要複述內容**,
   只回報「這份含敏感資訊」與它的類型。
6. 要出圖表就跑完到 PNG,不要只給程式碼。

## 常見雷

- 路徑有中文或空白,Python 裡一律用原始字串或正斜線,`open()` 記得 `encoding="utf-8"`。
- CSV 是中文的話,先試 `utf-8`,失敗再試 `utf-8-sig`、`cp950`。
- `.xls`(舊格式)`openpyxl` 讀不了,需要 `xlrd`;沒裝就回報,不要硬轉。
