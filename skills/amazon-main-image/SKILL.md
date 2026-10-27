---
name: amazon-main-image
description: 當任務是為 Amazon 產品生成主圖與輔圖(以及對應的圖像生成提示詞)時使用。涵蓋:讀取產品資訊與參考圖、抓取 Google/Reddit/YouTube/競品 ASIN 素材、反推競品爆款圖片邏輯、產出主圖 + 輔圖的完整英文圖像提示詞、拼圖提示詞與 HTML 排版稿。由 Coze 工作流 Zhu_tu_TORRAS 轉換而來。關鍵字:Amazon 主圖、輔圖、listing 圖片、產品圖提示詞、圖片策略架構、競品反推。
---

# Amazon 主圖 + 輔圖生成(Zhu_tu_TORRAS)

> 擁有者:**Ivy(creative)** —— 這三個工作流的產出屬視覺與文案範疇,內容與規格由 Ivy 定案。

由 Coze 工作流 `Zhu_tu_TORRAS`(id `7638638387914096650`)逐節點轉換而來。所有提示詞逐字保留,未刪減、未改寫、未翻譯。

## 這個 skill 做什麼

- 節點總數 **51**(頂層 48 + 批次子節點 3),連線 44 條,DAG 最大層深 **19**。
- 節點型別:async_job_call×1, batch×3, code×15, comment×2, condition×2, end×1, http×12, image_generate×1, llm×9, plugin×4, start×1
- 保留的提示詞段落 **36** 段,每段都附 SHA-256。

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
| `url1` | `116266`.url(html2url_download) |

## 需要的環境變數

原始工作流的明文金鑰已在來源端換成 `${VAR}` 佔位符。`run.py` 只從 `os.environ` 取值,缺少時直接報錯,不會 fallback 成空字串。

- `DMXAPI_API_KEY`
- `HIGHWAYAPI_API_KEY`
- `HIGHWAYAPI_API_KEY_2`
- `RAPIDAPI_API_KEY`
- `RAPIDAPI_API_KEY_2`
- `SERPAPI_API_KEY`
- `SERPAPI_API_KEY_2`

本工作流另有一個名為 `api_key` 的 **start 輸入參數**(如上表所列),那是執行時由呼叫端傳入的值,不是環境變數。

## 本機可以執行到什麼程度(誠實範圍)

`run.py` 能真正執行的只有:

- `http` 節點(標準函式庫 `urllib`)
- `code` 節點中 **Python** 的部分
- `condition` 分支判斷、`start` / `end` 的變數搬運

`batch` 容器本身**沒有實作**執行:本工作流的 3 個批次容器,迴圈體節點型別為 `http`、`plugin`。`run.py` 遇到 batch 節點會直接停下並說明原因,不會假裝跑完。要跑批次,必須由呼叫端自己對輸入清單迴圈呼叫迴圈體節點。

**無法**在 Coze 之外執行的節點型別:

- `async_job_call`(1 個)— Coze 非同步任務機制
- `image_generate`(1 個)— Coze 內建圖像生成節點
- `llm`(9 個)— Coze 託管的豆包 / Doubao 模型,需要 Coze 帳號與模型額度
- `plugin`(4 個)— Coze 平台外掛,沒有公開 endpoint

另有 1 個 JavaScript `code` 節點,`run.py` 不會執行它們,原始碼已逐字保留在節點檔中:`1412202` 代码_1

對這些節點,正確用法是:agent 自己讀節點檔裡的提示詞原文,以自己的模型能力執行該節點的職責,再把結果餵給下游節點。

## 孤立節點

下列 13 個節點在原始畫布上沒有從 `start` 可達的路徑(作者留下的舊版 / 備用分支),已完整保留但正常執行不會觸發:`143458` （未命名）, `1048863` 0.反推提示詞_1, `148157` 檔案分析, `1825568` 影片脚本_1, `1440616` mivideo_slowspeed_1, `180775` Html代碼編譯, `105378` （未命名）, `156417` Youtube_short, `186013` GLM 5, `128621` 圖片策略架構, `157536` 异步任务, `139160` HTTP 请求, `107177` 代码

## 目錄

```
amazon-main-image/
  SKILL.md
  references/
    graph.md            DAG 連線圖 + 拓樸排序 + Mermaid
    nodes/              每節點一檔,共 51 檔
  scripts/
    run.py              DAG 執行器,預設 dry-run
    graph.json          固化的節點資料(執行期不需要解析 YAML)
```

