# 05. mivideo_slowspeed_1(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1440616` |
| 型別 | `plugin` |
| 拓樸序 | 5 |
| DAG 層深 | 1 |
| Coze 說明 | mivideo慢速版 |

## 連線

- 上游:`1825568` 影片脚本_1
- 下游:（無）

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `key` | string | `{{block_output_100001.api_key}}` |
| `prompt` | string | `{{block_output_1825568.jiaoben}}` |
| `duration` | integer | 常數 `10` |
| `images` | list | `{{block_output_100001.images}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `data` | object | 本節點產出 |
| `message` | string | 本節點產出 |

## Coze 外掛

- api_name:`mivideo_slowspeed`
- api_id:`7622971799554506767`
- plugin_name:`MIVIDEO生成慢速版`
- plugin_id:`7622971799554490383`

> 這是 Coze 平台託管的外掛,**無法在 Coze 之外執行**。要在本機跑,必須自行以對應的第三方 API 取代。

