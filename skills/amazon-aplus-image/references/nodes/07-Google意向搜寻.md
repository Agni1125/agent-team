# 07. Google意向搜寻(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `144826` |
| 型別 | `http` |
| 拓樸序 | 7 |
| DAG 層深 | 1 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`100001` 开始
- 下游:`113844` 清洗

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `body` | string | 本節點產出 |
| `headers` | string | 本節點產出 |
| `statusCode` | integer | 本節點產出 |

## API

- Method:`GET`
- Endpoint:`https://serpapi.com/search`
- Body type:`EMPTY`
- Timeout:120 秒,重試 3 次

| Query 參數 | 值 |
| --- | --- |
| `engine` | `google` |
| `q` | `{'path': 'product_name', 'ref_node': '100001'}` |
| `location` | `Austin, Texas, United States` |
| `google_domain` | `google.com` |
| `hl` | `en` |
| `gl` | `us` |
| `api_key` | `${SERPAPI_API_KEY}` |

