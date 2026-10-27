# 40. 產品細節圖_TKgongneng(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1807253` |
| 型別 | `plugin` |
| 拓樸序 | 40 |
| DAG 層深 | 2 |
| Coze 說明 | 最强图片模型 |

## 連線

- 上游:`1196782` 產品資訊&外觀鎖定_TKgongneng
- 下游:`121916` 產品與功效解析節點

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `key` | string | 常數 `f42730ac-c51c-4ded-9596-edd080055e5c` |
| `prompt` | - | `{{block_output_1196782.waiguan}}` |
| `image_urls` | - | `{{block_output_100001.Product_image}}` |
| `ratio` | string | 常數 `16:9` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `code` | integer | 本節點產出 |
| `data` | object | 本節點產出 |
| `message` | string | 本節點產出 |

## Coze 外掛

- api_name:`g2_generate_image`
- api_id:`7631560961102528512`
- plugin_name:`GT2_图片生成`
- plugin_id:`7631560961102512128`

> 這是 Coze 平台託管的外掛,**無法在 Coze 之外執行**。要在本機跑,必須自行以對應的第三方 API 取代。

