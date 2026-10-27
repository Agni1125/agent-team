---
name: social-video
description: 當任務是為社群平台(TikTok / Reels / Shorts / UGC 廣告)生成短影片,或生成影片腳本、分鏡、模特形象與行為提示詞、口播稿、影片生成提示詞時使用。涵蓋 POV 第一人稱、Lifestyle UGC、功能呈現、品牌形象四種影片路線,最終輸出可直接送進 Seedance 2.0 的影片生成請求。由 Coze 工作流 viedo0526 轉換而來。關鍵字:社群影片、短影片、UGC 影片、口播腳本、分鏡、模特提示詞、Seedance、POV 影片。
---

# 社群影片生成(viedo0526)

> 擁有者:**Libai(video)** —— 影片是獨立的技能線,腳本、分鏡、口播、生成全部由 Libai 負責。
> (2026-09-04 從 Ivy 移交。Ivy 仍負責 Amazon 主圖 / A+ / Listing 等靜態素材。)
>
> **影片模型一律先問 Owner,絕不自己挑。** 影片比圖片貴一個量級,
> 圖片的預先授權不涵蓋影片。跑之前先報:模型、支數、秒數、解析度、預估花費。

由 Coze 工作流 `viedo0526`(id `7644513381228494854`)逐節點轉換而來。所有提示詞逐字保留,未刪減、未改寫、未翻譯。

## 這個 skill 做什麼

- 節點總數 **48**(頂層 47 + 批次子節點 1),連線 47 條,DAG 最大層深 **10**。
- 節點型別:batch×1, code×7, end×1, http×14, llm×14, plugin×10, start×1
- 保留的提示詞段落 **72** 段,每段都附 SHA-256。

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
| `IMAGE_STRUCTURE_ANAL` | string | 否 | - | - |
| `PERSONA_ANALYSIS` | string | 是 | - | - |
| `PRODUCT_INFO` | string | 是 | - | - |
| `Product_image` | list[image] | 是 | - | - |
| `Style_feature` | string | 否 | - | - |
| `duriation` | integer | 是 | - | - |
| `ref_viedo` | video | 否 | - | - |

## 工作流輸出(end 節點)

| 欄位 | 來源節點 |
| --- | --- |
| `body` | `1453736`.body(影片生成_Seedance2.0_功能呈現) |

## 需要的環境變數

原始工作流的明文金鑰已在來源端換成 `${VAR}` 佔位符。`run.py` 只從 `os.environ` 取值,缺少時直接報錯,不會 fallback 成空字串。

- `DMXAPI_API_KEY`
- `GEEKAI_API_KEY`



## 本機可以執行到什麼程度(誠實範圍)

`run.py` 能真正執行的只有:

- `http` 節點(標準函式庫 `urllib`)
- `code` 節點中 **Python** 的部分
- `condition` 分支判斷、`start` / `end` 的變數搬運

`batch` 容器本身**沒有實作**執行:本工作流的 1 個批次容器,迴圈體節點型別為 `plugin`。`run.py` 遇到 batch 節點會直接停下並說明原因,不會假裝跑完。要跑批次,必須由呼叫端自己對輸入清單迴圈呼叫迴圈體節點。

**無法**在 Coze 之外執行的節點型別:

- `llm`(14 個)— Coze 託管的豆包 / Doubao 模型,需要 Coze 帳號與模型額度
- `plugin`(10 個)— Coze 平台外掛,沒有公開 endpoint

對這些節點,正確用法是:agent 自己讀節點檔裡的提示詞原文,以自己的模型能力執行該節點的職責,再把結果餵給下游節點。

## 孤立節點

下列 3 個節點在原始畫布上沒有從 `start` 可達的路徑(作者留下的舊版 / 備用分支),已完整保留但正常執行不會觸發:`1168640` g2_generate_image_1, `112412` 大模型, `137979` 產品資訊與鎖外觀

## 目錄

```
social-video/
  SKILL.md
  references/
    graph.md            DAG 連線圖 + 拓樸排序 + Mermaid
    nodes/              每節點一檔,共 48 檔
  scripts/
    run.py              DAG 執行器,預設 dry-run
    graph.json          固化的節點資料(執行期不需要解析 YAML)
```

