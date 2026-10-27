# Amazon 主圖 + 輔圖生成(Zhu_tu_TORRAS) — DAG 連線圖與執行順序

來源:`Zhu_tu_TORRAS/workflow/Zhu_tu_TORRAS-draft.yaml`(Coze 匯出,已消毒;金鑰為 `${VAR}` 佔位符)

| 統計 | 值 |
| --- | --- |
| 節點總數(含批次子節點) | 51 |
| 頂層節點 | 48 |
| 批次容器內子節點 | 3 |
| 頂層連線 | 44 |
| 批次容器內部連線 | 7 |
| DAG 最大層深 | 19 |
| 條件分支節點 | 2 |
| 批次節點 | 3 |
| 節點型別分布 | async_job_call×1, batch×3, code×15, comment×2, condition×2, end×1, http×12, image_generate×1, llm×9, plugin×4, start×1 |

## 執行順序(拓樸排序)

| # | 層深 | 型別 | 節點 | ID | 可否本機執行 | 節點檔 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | comment | （未命名） ⚠孤立 | `143458` | 是 | [01-comment.md](nodes/01-comment.md) |
| 2 | 0 | llm | 0.反推提示詞_1 ⚠孤立 | `1048863` | 否(需 Coze) | [02-0.反推提示詞_1.md](nodes/02-0.反推提示詞_1.md) |
| 3 | 0 | llm | 檔案分析 ⚠孤立 | `148157` | 否(需 Coze) | [03-檔案分析.md](nodes/03-檔案分析.md) |
| 4 | 0 | llm | 影片脚本_1 ⚠孤立 | `1825568` | 否(需 Coze) | [04-影片脚本_1.md](nodes/04-影片脚本_1.md) |
| 5 | 1 | plugin | mivideo_slowspeed_1 ⚠孤立 | `1440616` | 否(需 Coze) | [05-mivideo_slowspeed_1.md](nodes/05-mivideo_slowspeed_1.md) |
| 6 | 0 | code | Html代碼編譯 ⚠孤立 | `180775` | 是 | [06-Html代碼編譯.md](nodes/06-Html代碼編譯.md) |
| 7 | 0 | comment | （未命名） ⚠孤立 | `105378` | 是 | [07-comment.md](nodes/07-comment.md) |
| 8 | 0 | code | Youtube_short ⚠孤立 | `156417` | 是 | [08-Youtube_short.md](nodes/08-Youtube_short.md) |
| 9 | 0 | http | GLM 5 ⚠孤立 | `186013` | 是 | [09-GLM_5.md](nodes/09-GLM_5.md) |
| 10 | 0 | start | 开始 | `100001` | 是 | [10-开始.md](nodes/10-开始.md) |
| 11 | 1 | llm | 2.提取參考圖的風格 | `185690` | 否(需 Coze) | [11-2.提取參考圖的風格.md](nodes/11-2.提取參考圖的風格.md) |
| 12 | 1 | llm | 0.反推提示詞 | `138410` | 否(需 Coze) | [12-0.反推提示詞.md](nodes/12-0.反推提示詞.md) |
| 13 | 2 | llm | 1.產品核心信息 | `193707` | 否(需 Coze) | [13-1.產品核心信息.md](nodes/13-1.產品核心信息.md) |
| 14 | 1 | http | Google意向搜寻 | `144826` | 是 | [14-Google意向搜寻.md](nodes/14-Google意向搜寻.md) |
| 15 | 1 | http | Reddit Comment Search | `118241` | 是 | [15-Reddit_Comment_Search.md](nodes/15-Reddit_Comment_Search.md) |
| 16 | 2 | code | 清洗 | `113844` | 是 | [16-清洗.md](nodes/16-清洗.md) |
| 17 | 2 | code | 清洗_1 | `1791005` | 是 | [17-清洗_1.md](nodes/17-清洗_1.md) |
| 18 | 1 | plugin | read | `134927` | 否(需 Coze) | [18-read.md](nodes/18-read.md) |
| 19 | 1 | http | 競品搜尋 | `178577` | 是 | [19-競品搜尋.md](nodes/19-競品搜尋.md) |
| 20 | 0 | llm | 圖片策略架構 ⚠孤立 | `128621` | 否(需 Coze) | [20-圖片策略架構.md](nodes/20-圖片策略架構.md) |
| 21 | 1 | http | Youtube_Search_Serpapi | `167462` | 是 | [21-Youtube_Search_Serpapi.md](nodes/21-Youtube_Search_Serpapi.md) |
| 22 | 2 | code | YT清洗 | `120638` | 是 | [22-YT清洗.md](nodes/22-YT清洗.md) |
| 23 | 3 | batch | YT_VideoID查詢 | `128609` | 否(需 Coze) | [23-YT_VideoID查詢.md](nodes/23-YT_VideoID查詢.md) |
| 24 | 0 | http | YT評論 | `109664` | 是 | [24-YT評論.md](nodes/24-YT評論.md) |
| 25 | 4 | code | YT搜尋資料清洗 | `116382` | 是 | [25-YT搜尋資料清洗.md](nodes/25-YT搜尋資料清洗.md) |
| 26 | 5 | llm | Person行為分析 | `113656` | 否(需 Coze) | [26-Person行為分析.md](nodes/26-Person行為分析.md) |
| 27 | 0 | async_job_call | 异步任务 ⚠孤立 | `157536` | 否(需 Coze) | [27-异步任务.md](nodes/27-异步任务.md) |
| 28 | 2 | code | ASIN提取 | `138773` | 是 | [28-ASIN提取.md](nodes/28-ASIN提取.md) |
| 29 | 3 | batch | ASIN競品查詢 | `184391` | 否(需 Coze) | [29-ASIN競品查詢.md](nodes/29-ASIN競品查詢.md) |
| 30 | 0 | http | Amazon竟品搜尋 | `127740` | 是 | [30-Amazon竟品搜尋.md](nodes/30-Amazon竟品搜尋.md) |
| 31 | 4 | code | 競品搜尋_清洗 | `133295` | 是 | [31-競品搜尋_清洗.md](nodes/31-競品搜尋_清洗.md) |
| 32 | 0 | http | HTTP 请求 ⚠孤立 | `139160` | 是 | [32-HTTP_请求.md](nodes/32-HTTP_请求.md) |
| 33 | 1 | code | 代码 ⚠孤立 | `107177` | 是 | [33-代码.md](nodes/33-代码.md) |
| 34 | 2 | code | 檔案清洗 | `180956` | 是 | [34-檔案清洗.md](nodes/34-檔案清洗.md) |
| 35 | 3 | http | Qwen3.5-27B_檔案分析 | `1942015` | 是 | [35-Qwen3.5-27B_檔案分析.md](nodes/35-Qwen3.5-27B_檔案分析.md) |
| 36 | 6 | http | Gemimi2.5pro 圖片策略架構 | `1642400` | 是 | [36-Gemimi2.5pro_圖片策略架構.md](nodes/36-Gemimi2.5pro_圖片策略架構.md) |
| 37 | 7 | code | img_array2str | `197995` | 是 | [37-img_array2str.md](nodes/37-img_array2str.md) |
| 38 | 8 | http | Gemimi2.5pro 3.生成主圖+輔圖提示詞 | `185098` | 是 | [38-Gemimi2.5pro_3.生成主圖+輔圖提示詞.md](nodes/38-Gemimi2.5pro_3.生成主圖+輔圖提示詞.md) |
| 39 | 9 | code | 節點_prompt string轉array | `105725` | 是 | [39-節點_prompt_string轉array.md](nodes/39-節點_prompt_string轉array.md) |
| 40 | 10 | llm | 4.拼圖提示詞 | `182406` | 否(需 Coze) | [40-4.拼圖提示詞.md](nodes/40-4.拼圖提示詞.md) |
| 41 | 11 | condition | 选择器 | `188581` | 是 | [41-选择器.md](nodes/41-选择器.md) |
| 42 | 12 | image_generate | 图像生成 | `121698` | 否(需 Coze) | [42-图像生成.md](nodes/42-图像生成.md) |
| 43 | 12 | batch | 批处理 | `147162` | 否(需 Coze) | [43-批处理.md](nodes/43-批处理.md) |
| 44 | 0 | plugin | g2_generate_image | `157548` | 否(需 Coze) | [44-g2_generate_image.md](nodes/44-g2_generate_image.md) |
| 45 | 13 | condition | 选择器_3 | `1487634` | 是 | [45-选择器_3.md](nodes/45-选择器_3.md) |
| 46 | 14 | code | 代码_1 | `1412202` | 是 | [46-代码_1.md](nodes/46-代码_1.md) |
| 47 | 15 | code | 最終參考圖轉url | `154873` | 是 | [47-最終參考圖轉url.md](nodes/47-最終參考圖轉url.md) |
| 48 | 16 | http | html生成 | `1432717` | 是 | [48-html生成.md](nodes/48-html生成.md) |
| 49 | 17 | code | html code清洗 | `169597` | 是 | [49-html_code清洗.md](nodes/49-html_code清洗.md) |
| 50 | 18 | plugin | html2url_download | `116266` | 否(需 Coze) | [50-html2url_download.md](nodes/50-html2url_download.md) |
| 51 | 19 | end | 结束 | `900001` | 是 | [51-结束.md](nodes/51-结束.md) |

## 連線明細(頂層)

| 來源 | port | 目標 |
| --- | --- | --- |
| `138410` 0.反推提示詞 | default | `193707` 1.產品核心信息 |
| `193707` 1.產品核心信息 | default | `197995` img_array2str |
| `100001` 开始 | default | `185690` 2.提取參考圖的風格 |
| `185690` 2.提取參考圖的風格 | default | `197995` img_array2str |
| `105725` 節點_prompt string轉array | default | `182406` 4.拼圖提示詞 |
| `182406` 4.拼圖提示詞 | default | `188581` 选择器 |
| `188581` 选择器 | true | `121698` 图像生成 |
| `188581` 选择器 | false | `147162` 批处理 |
| `121698` 图像生成 | default | `1487634` 选择器_3 |
| `147162` 批处理 | batch-output | `1487634` 选择器_3 |
| `100001` 开始 | default | `138410` 0.反推提示詞 |
| `100001` 开始 | default | `144826` Google意向搜寻 |
| `144826` Google意向搜寻 | default | `113844` 清洗 |
| `113844` 清洗 | default | `113656` Person行為分析 |
| `1791005` 清洗_1 | default | `113656` Person行為分析 |
| `116382` YT搜尋資料清洗 | default | `113656` Person行為分析 |
| `113656` Person行為分析 | default | `1642400` Gemimi2.5pro 圖片策略架構 |
| `100001` 开始 | default | `118241` Reddit Comment Search |
| `118241` Reddit Comment Search | default | `1791005` 清洗_1 |
| `1487634` 选择器_3 | true | `1412202` 代码_1 |
| `1487634` 选择器_3 | false | `900001` 结束 |
| `1412202` 代码_1 | default | `154873` 最終參考圖轉url |
| `1825568` 影片脚本_1 | default | `1440616` mivideo_slowspeed_1 |
| `100001` 开始 | default | `134927` read |
| `134927` read | default | `180956` 檔案清洗 |
| `167462` Youtube_Search_Serpapi | default | `120638` YT清洗 |
| `120638` YT清洗 | default | `128609` YT_VideoID查詢 |
| `169597` html code清洗 | default | `116266` html2url_download |
| `116266` html2url_download | default | `900001` 结束 |
| `100001` 开始 | default | `178577` 競品搜尋 |
| `178577` 競品搜尋 | default | `138773` ASIN提取 |
| `184391` ASIN競品查詢 | batch-output | `133295` 競品搜尋_清洗 |
| `133295` 競品搜尋_清洗 | default | `197995` img_array2str |
| `154873` 最終參考圖轉url | default | `1432717` html生成 |
| `197995` img_array2str | default | `185098` Gemimi2.5pro 3.生成主圖+輔圖提示詞 |
| `185098` Gemimi2.5pro 3.生成主圖+輔圖提示詞 | default | `105725` 節點_prompt string轉array |
| `1642400` Gemimi2.5pro 圖片策略架構 | default | `197995` img_array2str |
| `100001` 开始 | default | `167462` Youtube_Search_Serpapi |
| `180956` 檔案清洗 | default | `1942015` Qwen3.5-27B_檔案分析 |
| `1942015` Qwen3.5-27B_檔案分析 | default | `1642400` Gemimi2.5pro 圖片策略架構 |
| `1432717` html生成 | default | `169597` html code清洗 |
| `128609` YT_VideoID查詢 | batch-output | `116382` YT搜尋資料清洗 |
| `138773` ASIN提取 | default | `184391` ASIN競品查詢 |
| `139160` HTTP 请求 | default | `107177` 代码 |

## 批次容器內部連線

| 容器 | 來源 | source_port | 目標 | target_port |
| --- | --- | --- | --- | --- |
| `147162` | `147162` | batch-function-inline-output | `157548` | - |
| `147162` | `157548` | default | `147162` | batch-function-inline-input |
| `147162` | `157548` | branch_error | `147162` | batch-function-inline-input |
| `128609` | `128609` | batch-function-inline-output | `109664` | - |
| `128609` | `109664` | - | `128609` | batch-function-inline-input |
| `184391` | `184391` | batch-function-inline-output | `127740` | - |
| `184391` | `127740` | - | `184391` | batch-function-inline-input |

## Mermaid

```mermaid
graph TD
  N1048863[llm<br/>0.反推提示詞_1]
  N148157[llm<br/>檔案分析]
  N1825568[llm<br/>影片脚本_1]
  N1440616[plugin<br/>mivideo_slowspeed_1]
  N180775[code<br/>Html代碼編譯]
  N156417[code<br/>Youtube_short]
  N186013[http<br/>GLM 5]
  N100001([start<br/>开始])
  N185690[llm<br/>2.提取參考圖的風格]
  N138410[llm<br/>0.反推提示詞]
  N193707[llm<br/>1.產品核心信息]
  N144826[http<br/>Google意向搜寻]
  N118241[http<br/>Reddit Comment Search]
  N113844[code<br/>清洗]
  N1791005[code<br/>清洗_1]
  N134927[plugin<br/>read]
  N178577[http<br/>競品搜尋]
  N128621[llm<br/>圖片策略架構]
  N167462[http<br/>Youtube_Search_Serpapi]
  N120638[code<br/>YT清洗]
  N128609[[batch<br/>YT_VideoID查詢]]
  N109664[http<br/>YT評論]
  N116382[code<br/>YT搜尋資料清洗]
  N113656[llm<br/>Person行為分析]
  N157536[async_job_call<br/>异步任务]
  N138773[code<br/>ASIN提取]
  N184391[[batch<br/>ASIN競品查詢]]
  N127740[http<br/>Amazon竟品搜尋]
  N133295[code<br/>競品搜尋_清洗]
  N139160[http<br/>HTTP 请求]
  N107177[code<br/>代码]
  N180956[code<br/>檔案清洗]
  N1942015[http<br/>Qwen3.5-27B_檔案分析]
  N1642400[http<br/>Gemimi2.5pro 圖片策略架構]
  N197995[code<br/>img_array2str]
  N185098[http<br/>Gemimi2.5pro 3.生成主圖+輔圖提示詞]
  N105725[code<br/>節點_prompt string轉array]
  N182406[llm<br/>4.拼圖提示詞]
  N188581{condition<br/>选择器}
  N121698[image_generate<br/>图像生成]
  N147162[[batch<br/>批处理]]
  N157548[plugin<br/>g2_generate_image]
  N1487634{condition<br/>选择器_3}
  N1412202[code<br/>代码_1]
  N154873[code<br/>最終參考圖轉url]
  N1432717[http<br/>html生成]
  N169597[code<br/>html code清洗]
  N116266[plugin<br/>html2url_download]
  N900001([end<br/>结束])
  N138410 --> N193707
  N193707 --> N197995
  N100001 --> N185690
  N185690 --> N197995
  N105725 --> N182406
  N182406 --> N188581
  N188581 -->|true| N121698
  N188581 -->|false| N147162
  N121698 --> N1487634
  N147162 -->|batch-output| N1487634
  N100001 --> N138410
  N100001 --> N144826
  N144826 --> N113844
  N113844 --> N113656
  N1791005 --> N113656
  N116382 --> N113656
  N113656 --> N1642400
  N100001 --> N118241
  N118241 --> N1791005
  N1487634 -->|true| N1412202
  N1487634 -->|false| N900001
  N1412202 --> N154873
  N1825568 --> N1440616
  N100001 --> N134927
  N134927 --> N180956
  N167462 --> N120638
  N120638 --> N128609
  N169597 --> N116266
  N116266 --> N900001
  N100001 --> N178577
  N178577 --> N138773
  N184391 -->|batch-output| N133295
  N133295 --> N197995
  N154873 --> N1432717
  N197995 --> N185098
  N185098 --> N105725
  N1642400 --> N197995
  N100001 --> N167462
  N180956 --> N1942015
  N1942015 --> N1642400
  N1432717 --> N169597
  N128609 -->|batch-output| N116382
  N138773 --> N184391
  N139160 --> N107177
  N147162 -.->|batch-function-inline-output| N157548
  N157548 -.->|default| N147162
  N157548 -.->|branch_error| N147162
  N128609 -.->|batch-function-inline-output| N109664
  N109664 -.->|batch-function-inline-input| N128609
  N184391 -.->|batch-function-inline-output| N127740
  N127740 -.->|batch-function-inline-input| N184391
```

## 未連到起始節點的節點(孤立 / 停用分支)

這些節點在 Coze 畫布上存在但**沒有任何從 `start` 出發的路徑可以到達**,屬於作者留在畫布上的舊版或備用分支。已完整保留,執行時不會被觸發。

- `143458` （未命名）(comment)
- `1048863` 0.反推提示詞_1(llm)
- `1440616` mivideo_slowspeed_1(plugin)
- `148157` 檔案分析(llm)
- `1825568` 影片脚本_1(llm)
- `180775` Html代碼編譯(code)
- `105378` （未命名）(comment)
- `156417` Youtube_short(code)
- `186013` GLM 5(http)
- `128621` 圖片策略架構(llm)
- `157536` 异步任务(async_job_call)
- `139160` HTTP 请求(http)
- `107177` 代码(code)

