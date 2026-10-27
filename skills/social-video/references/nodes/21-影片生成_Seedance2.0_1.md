# 21. 影片生成_Seedance2.0_1(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1998024` |
| 型別 | `http` |
| 拓樸序 | 21 |
| DAG 層深 | 6 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`1135706` 生成影片提示詞
- 下游:`900001` 结束

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `body` | string | 本節點產出 |
| `headers` | string | 本節點產出 |
| `statusCode` | integer | 本節點產出 |

## API

- Method:`POST`
- Endpoint:`https://geekai.co/api/v1/videos/generations`
- Body type:`JSON`
- Timeout:600 秒,重試 3 次

| Header | 值 |
| --- | --- |
| `Authorization` | `Bearer ${GEEKAI_API_KEY}` |

- 本節點引用的上游變數:`{{block_output_100001.duriation}}`, `{{block_output_1135706.body}}`, `{{block_output_164877.data.url}}`, `{{block_output_1860244.images_url}}`

## 提示詞原文(逐字保留,不得修改)

### `body.prompt`

- SHA-256:`d089676aad6248d2df2155d5a603b853ac98b371b7de6c8e4e54139dbcb4b452`
- 長度:29 字元

<!-- PROMPT-BEGIN body.prompt -->
{{block_output_1135706.body}}
<!-- PROMPT-END body.prompt -->

## 請求 body 樣板(逐字保留)

```json
{
  "model": "doubao-seedance-2.0-fast",
  "prompt": "{{block_output_1135706.body}}",
  "image": [
    "{{block_output_1860244.images_url}}",
    "{{block_output_164877.data.url}}"
  ],
  "video": [],
  "audio": [],
  "with_audio": true,
  "Aspect_ratio": "9:16",
  "duration": {{block_output_100001.duriation}},
  "extra_body": {
    "real_person_mode": true
  },
  "async": true,
  "watermark": false
}
```

