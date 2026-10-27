# 25. Pov分鏡圖(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1977031` |
| 型別 | `plugin` |
| 拓樸序 | 25 |
| DAG 層深 | 2 |
| Coze 說明 | 最强图片模型 |

## 連線

- 上游:`163246` POV影片架構
- 下游:`1677938` 產品資訊&外觀鎖定_Pov

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `key` | string | 常數 `f42730ac-c51c-4ded-9596-edd080055e5c` |
| `prompt` | - | `{{block_output_163246.output}}` |
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

