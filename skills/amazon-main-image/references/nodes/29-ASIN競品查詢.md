# 29. ASIN競品查詢(批次容器)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `184391` |
| 型別 | `batch` |
| 拓樸序 | 29 |
| DAG 層深 | 3 |
| Coze 說明 | 通过设定批量运行次数和逻辑，运行批处理体内的任务 |

## 連線

- 上游:`138773` ASIN提取, `127740` Amazon竟品搜尋
- 下游:`133295` 競品搜尋_清洗(port=batch-output), `127740` Amazon竟品搜尋(port=batch-function-inline-output)

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `input` | list | `{{block_output_138773.asin_array}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `output` | list | `{{block_output_127740.body}}` |

## 批次設定

- batchSize:`100`,concurrentSize:`10`
- 迴圈體節點:`127740`(Amazon竟品搜尋)
- 批次完成後,結果經 `source_port: batch-output` 的邊送往下游。

