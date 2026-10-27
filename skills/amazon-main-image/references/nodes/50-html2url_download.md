# 50. html2url_download(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `116266` |
| 型別 | `plugin` |
| 拓樸序 | 50 |
| DAG 層深 | 18 |
| Coze 說明 | 接收html代码并输出为一个可以下载的html文件，打开后即可预览 |

## 連線

- 上游:`169597` html code清洗
- 下游:`900001` 结束

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `html` | string | `{{block_output_169597.file_content}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `url` | string | 本節點產出 |

## Coze 外掛

- api_name:`html2url_download`
- api_id:`7614802629255970856`
- plugin_name:`html转url_栗子`
- plugin_id:`7614802629255938088`

> 這是 Coze 平台託管的外掛,**無法在 Coze 之外執行**。要在本機跑,必須自行以對應的第三方 API 取代。

