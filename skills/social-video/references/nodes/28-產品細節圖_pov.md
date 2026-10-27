# 28. 產品細節圖_pov(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1103273` |
| 型別 | `plugin` |
| 拓樸序 | 28 |
| DAG 層深 | 5 |
| Coze 說明 | 最强图片模型 |

## 連線

- 上游:`1314338` 產品細節分鏡圖生成_Pov
- 下游:`1404396` 參考圖轉url_1

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `key` | string | 常數 `f42730ac-c51c-4ded-9596-edd080055e5c` |
| `prompt` | - | `{{block_output_1677938.waiguan}}` |
| `image_urls` | - | `{{block_output_100001.Product_image}}` |

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

