# 23. Youtube_Search_Serpapi(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `167462` |
| 型別 | `http` |
| 拓樸序 | 23 |
| DAG 層深 | 1 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`100001` 开始
- 下游:`1318212` YT清洗_1

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `body` | string | 本節點產出 |
| `headers` | string | 本節點產出 |
| `statusCode` | integer | 本節點產出 |

## API

- Method:`GET`
- Endpoint:`https://serpapi.com/search?engine=youtube`
- Body type:`EMPTY`
- Timeout:120 秒,重試 3 次

| Query 參數 | 值 |
| --- | --- |
| `engine` | `youtube` |
| `search_query` | `{'path': 'product_name', 'ref_node': '100001'}` |
| `api_key` | `${SERPAPI_API_KEY}` |

