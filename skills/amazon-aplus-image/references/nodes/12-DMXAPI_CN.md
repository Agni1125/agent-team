# 12. DMXAPI_CN(Coze 外掛)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `143538` |
| 型別 | `plugin` |
| 拓樸序 | 12 |
| DAG 層深 | 0 |
| Coze 說明 | DMXAPI.cn （ 国内站 ）聚合接口 |

## 連線

- 上游:（無,起點或孤立節點）
- 下游:（無）

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `apikey` | string | 常數 `${DMXAPI_API_KEY_2}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `content` | string | 本節點產出 |
| `reasoning_content` | string | 本節點產出 |

## Coze 外掛

- api_name:`DMXAPI_CN`
- api_id:`7539403763224756264`
- plugin_name:`DMXAPI_国内站国际站聚合插件`
- plugin_id:`7539403763224739880`

> 這是 Coze 平台託管的外掛,**無法在 Coze 之外執行**。要在本機跑,必須自行以對應的第三方 API 取代。

