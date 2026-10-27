# 32. HTTP 请求(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `139160` |
| 型別 | `http` |
| 拓樸序 | 32 |
| DAG 層深 | 0 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:（無,起點或孤立節點）
- 下游:`107177` 代码

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `body` | string | 本節點產出 |
| `headers` | string | 本節點產出 |
| `statusCode` | integer | 本節點產出 |

## API

- Method:`GET`
- Endpoint:`https://serpapi.com/search?engine=amazon_product`
- Body type:`EMPTY`
- Timeout:400 秒,重試 3 次

| Query 參數 | 值 |
| --- | --- |
| `engine` | `amazon_product` |
| `asin` | `{'path': 'Product_ASIN', 'ref_node': '100001'}` |
| `device` | `mobile` |
| `api_key` | `${SERPAPI_API_KEY}` |

