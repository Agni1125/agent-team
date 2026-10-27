# 15. read_1(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1058296` |
| 型別 | `plugin` |
| 拓樸序 | 15 |
| DAG 層深 | 1 |
| Coze 說明 | 读取文档内容，目前支持html、xml、doc、docx、txt、pdf、csv、xlsx格式 |

## 連線

- 上游:`100001` 开始
- 下游:`180956` 檔案清洗

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `url` | string | `{{block_output_1058296.item1}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `outputList` | list[object] | 本節點產出 |

## Coze 外掛

- api_name:`read`
- api_id:`7405805158996934683`
- plugin_name:`文件读取`
- plugin_id:`7405805158996918299`

> 這是 Coze 平台託管的外掛,**無法在 Coze 之外執行**。要在本機跑,必須自行以對應的第三方 API 取代。

