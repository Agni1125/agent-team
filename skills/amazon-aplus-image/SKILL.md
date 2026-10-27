---
name: amazon-aplus-image
description: 當任務是為 Amazon 產品生成 A+ 頁面(A+ Content / EBC)圖片與其圖像提示詞時使用。涵蓋:產品核心資訊結構化、參考圖風格提取、競品與評論素材蒐集、A+ 模組圖片提示詞生成、A+ HTML 版面產出。由 Coze 工作流 A_jia_TORRAS 轉換而來。關鍵字:Amazon A+、A+ 圖文、EBC、品牌旗艦頁圖片、A+ 模組、A+ 提示詞。
---

# Amazon A+ 圖片生成(A_jia_TORRAS)

> 擁有者:**Ivy(creative)** —— 這三個工作流的產出屬視覺與文案範疇,內容與規格由 Ivy 定案。

由 Coze 工作流 `A_jia_TORRAS`(id `7639494080460832820`)逐節點轉換而來。所有提示詞逐字保留,未刪減、未改寫、未翻譯。

## 這個 skill 做什麼

- 節點總數 **44**(頂層 41 + 批次子節點 3),連線 42 條,DAG 最大層深 **19**。
- 節點型別:batch×3, code×12, comment×2, condition×2, end×1, http×10, image_generate×1, llm×7, plugin×4, start×1, to_json×1
- 保留的提示詞段落 **30** 段,每段都附 SHA-256。

## 使用步驟

1. 先讀 `references/graph.md`,取得完整 DAG 與拓樸排序。
2. 依拓樸順序讀 `references/nodes/` 底下對應的節點檔,每檔含該節點的型別、輸入、輸出、API endpoint 與**提示詞原文**。
3. 要看流程與參數而不發請求:

   ```bash
   python scripts/run.py                       # 預設就是 dry-run
   python scripts/run.py --inputs inputs.json   # 帶入實際輸入
   python scripts/run.py --plan-json plan.json  # 輸出機器可讀的執行計畫
   python scripts/run.py --show-prompt <節點ID> # 印出該節點的提示詞原文
   ```

4. **真的要打 API** 才加 `--execute`。這條路線會產生費用,執行前必須先向使用者確認。

## 工作流輸入參數(start 節點)

| 參數 | 型別 | 必填 | 預設 | 說明 |
| --- | --- | --- | --- | --- |
| `Analyse` | list[excel] | 否 | - | - |
| `Product_ASIN` | string | 否 | - | - |
| `api_key` | string | 是 | - | - |
| `image_ref` | list[image] | 是 | - | 提取图片风格 |
| `images` | list[image] | 是 | - | 产品列表图 |
| `isAll` | boolean | 是 | true | 生成模式 |
| `isVideo` | boolean | 是 | false | 是否生成视频 |
| `language` | string | 是 | "English" | 語言輸入 |
| `num` | string | 是 | - | - |
| `product_info` | string | 是 | - | 产品相关讯息:名称、标题、描述等 |
| `product_name` | string | 是 | - | - |
| `style` | string | 是 | - | - |

## 工作流輸出(end 節點)

| 欄位 | 來源節點 |
| --- | --- |
| `data` | `121698`.data(图像生成) |
| `output` | `147162`.output2(批处理) |
| `url1` | `116266`.url(html2url_download) |

## 需要的環境變數

原始工作流的明文金鑰已在來源端換成 `${VAR}` 佔位符。`run.py` 只從 `os.environ` 取值,缺少時直接報錯,不會 fallback 成空字串。

- `DMXAPI_API_KEY_2`
- `HIGHWAYAPI_API_KEY`
- `RAPIDAPI_API_KEY`
- `RAPIDAPI_API_KEY_3`
- `SERPAPI_API_KEY`
- `SERPAPI_API_KEY_3`

本工作流另有一個名為 `api_key` 的 **start 輸入參數**(如上表所列),那是執行時由呼叫端傳入的值,不是環境變數。

## 本機可以執行到什麼程度(誠實範圍)

`run.py` 能真正執行的只有:

- `http` 節點(標準函式庫 `urllib`)
- `code` 節點中 **Python** 的部分
- `condition` 分支判斷、`start` / `end` 的變數搬運

`batch` 容器本身**沒有實作**執行:本工作流的 3 個批次容器,迴圈體節點型別為 `http`、`plugin`。`run.py` 遇到 batch 節點會直接停下並說明原因,不會假裝跑完。要跑批次,必須由呼叫端自己對輸入清單迴圈呼叫迴圈體節點。

**無法**在 Coze 之外執行的節點型別:

- `image_generate`(1 個)— Coze 內建圖像生成節點
- `llm`(7 個)— Coze 託管的豆包 / Doubao 模型,需要 Coze 帳號與模型額度
- `plugin`(4 個)— Coze 平台外掛,沒有公開 endpoint
- `to_json`(1 個)— Coze 內建型別轉換節點

另有 2 個 JavaScript `code` 節點,`run.py` 不會執行它們,原始碼已逐字保留在節點檔中:`133160` 代码, `105725` 節點_string轉array

對這些節點,正確用法是:agent 自己讀節點檔裡的提示詞原文,以自己的模型能力執行該節點的職責,再把結果餵給下游節點。

## 孤立節點

下列 6 個節點在原始畫布上沒有從 `start` 可達的路徑(作者留下的舊版 / 備用分支),已完整保留但正常執行不會觸發:`195000` 3.生成主圖+輔圖提示詞, `143458` （未命名）, `135189` html代码生成, `143538` DMXAPI_CN, `105378` （未命名）, `163345` img2Str

## 目錄

```
amazon-aplus-image/
  SKILL.md
  references/
    graph.md            DAG 連線圖 + 拓樸排序 + Mermaid
    nodes/              每節點一檔,共 44 檔
  scripts/
    run.py              DAG 執行器,預設 dry-run
    graph.json          固化的節點資料(執行期不需要解析 YAML)
```

