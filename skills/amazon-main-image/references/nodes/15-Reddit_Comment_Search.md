# 15. Reddit Comment Search(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `118241` |
| 型別 | `http` |
| 拓樸序 | 15 |
| DAG 層深 | 1 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`100001` 开始
- 下游:`1791005` 清洗_1

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `body` | string | 本節點產出 |
| `headers` | string | 本節點產出 |
| `statusCode` | integer | 本節點產出 |

## API

- Method:`GET`
- Endpoint:`https://reddit34.p.rapidapi.com/getSearchPosts`
- Body type:`EMPTY`
- Timeout:120 秒,重試 3 次

| Header | 值 |
| --- | --- |
| `X-Rapidapi-Key` | `${RAPIDAPI_API_KEY}` |

| Query 參數 | 值 |
| --- | --- |
| `query` | `{'path': 'product_name', 'ref_node': '100001'}` |
| `subreddit` | `` |
| `sort` | `top` |
| `time` | `all` |
| `cursor` | `4` |

