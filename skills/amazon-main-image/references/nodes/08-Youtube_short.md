# 08. Youtube_short(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `156417` |
| 型別 | `code` |
| 拓樸序 | 8 |
| DAG 層深 | 0 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:（無,起點或孤立節點）
- 下游:（無）

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `product_name` | string | `{{block_output_100001.product_name}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `youtube_short` | string | 本節點產出 |

## 程式碼(python,逐字保留)

```python
import serpapi

client = serpapi.Client(api_key="${SERPAPI_API_KEY}")
results = client.search({
  "engine": "youtube",
  "search_query": ""
})
video_results = results["video_results"]
```

