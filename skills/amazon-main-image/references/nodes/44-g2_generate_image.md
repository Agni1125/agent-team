# 44. g2_generate_image(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `157548` |
| 型別 | `plugin` |
| 拓樸序 | 44 |
| DAG 層深 | — |
| 所屬批次容器 | `147162`(批处理) |
| Coze 說明 | 最强图片模型 |

## 連線

- 上游:`147162` 批处理
- 下游:`147162` 批处理(port=default), `147162` 批处理(port=branch_error)

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `key` | string | `{{block_output_100001.api_key}}` |
| `prompt` | string | `{{block_output_147162.input}}` |
| `image_urls` | list | `{{block_output_100001.images}}` |
| `ratio` | string | 常數 `1:1` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `code` | integer | 本節點產出 |
| `data` | object | 本節點產出 |
| `errorBody` | object | 本節點產出 |
| `isSuccess` | boolean | 本節點產出 |
| `message` | string | 本節點產出 |

## Coze 外掛

- api_name:`g2_generate_image`
- api_id:`7631560961102528512`
- plugin_name:`GT2_图片生成`
- plugin_id:`7631560961102512128`

> 這是 Coze 平台託管的外掛,**無法在 Coze 之外執行**。要在本機跑,必須自行以對應的第三方 API 取代。

