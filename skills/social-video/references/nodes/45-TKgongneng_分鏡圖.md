# 45. TKgongneng_分鏡圖(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1998343` |
| 型別 | `plugin` |
| 拓樸序 | 45 |
| DAG 層深 | 7 |
| Coze 說明 | 最强图片模型 |

## 連線

- 上游:`156491` 分鏡圖提示詞
- 下游:`1717375` 參考圖轉url_3

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `key` | string | 常數 `f42730ac-c51c-4ded-9596-edd080055e5c` |
| `prompt` | string | `{{block_output_156491.output}}` |
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

