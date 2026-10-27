# 25. YT_VideoID查詢(批次容器)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `128609` |
| 型別 | `batch` |
| 拓樸序 | 25 |
| DAG 層深 | 3 |
| Coze 說明 | 通过设定批量运行次数和逻辑，运行批处理体内的任务 |

## 連線

- 上游:`1318212` YT清洗_1, `109664` YT評論
- 下游:`116382` YT搜尋資料清洗(port=batch-output), `109664` YT評論(port=batch-function-inline-output)

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `input` | - | `{{block_output_1318212.YT_output}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `output` | list | `{{block_output_109664.body}}` |

## 批次設定

- batchSize:`100`,concurrentSize:`10`
- 迴圈體節點:`109664`(YT評論)
- 批次完成後,結果經 `source_port: batch-output` 的邊送往下游。

