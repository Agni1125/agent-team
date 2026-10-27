# 19. Amazon竟品搜尋(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `127740` |
| 型別 | `http` |
| 拓樸序 | 19 |
| DAG 層深 | — |
| 所屬批次容器 | `184391`(ASIN競品查詢) |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`184391` ASIN競品查詢
- 下游:`184391` ASIN競品查詢

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `body` | string | 本節點產出 |
| `headers` | string | 本節點產出 |
| `statusCode` | integer | 本節點產出 |

## API

- Method:`GET`
- Endpoint:`https://serpapi.com/search.json?engine=amazon_product&asin=B072MQ5BRX&amazon_domain=amazon.com`
- Body type:`EMPTY`
- Timeout:300 秒,重試 3 次

| Query 參數 | 值 |
| --- | --- |
| `engine` | `amazon_product` |
| `asin` | `{'path': 'input', 'ref_node': '184391'}` |
| `amazon_domain` | `amazon.com` |
| `api_key` | `${SERPAPI_API_KEY_3}` |

