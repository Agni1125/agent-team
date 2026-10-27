# 10. 參考圖轉url(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1860244` |
| 型別 | `code` |
| 拓樸序 | 10 |
| DAG 層深 | 4 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:`1457648` 模特行為提示詞生成
- 下游:`1135706` 生成影片提示詞

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `imageurl` | - | `{{block_output_100001.Product_image}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `images_url` | string | 本節點產出 |

## 程式碼(python,逐字保留)

```python
import json
import re


async def main(args):
    params = getattr(args, "params", None) or {}

    raw = params.get("imageurl")

    image_urls = []

    def add_url(value):
        if not value:
            return

        # 如果是圖片物件，例如 {"url": "..."} 或 {"image_url": "..."}
        if isinstance(value, dict):
            for key in ["url", "uri", "src", "image_url", "imageUrl", "origin_url", "preview_url", "download_url"]:
                if key in value:
                    add_url(value.get(key))
            return

        # 如果是純字串 URL
        if isinstance(value, str):
            text = value.strip()

            # 如果字串裡包 JSON，先嘗試解析
            if (text.startswith("{") and text.endswith("}")) or (text.startswith("[") and text.endswith("]")):
                try:
                    parsed = json.loads(text)
                    add_url(parsed)
                    return
                except Exception:
                    pass

            matches = re.findall(r"https?://[^\s\"'<>\\]+", text)
            for url in matches:
                url = url.replace("&amp;", "&").rstrip("，。,.);]}\"'")
                if url not in image_urls:
                    image_urls.append(url)

            return

        # 如果是陣列，例如 Array<Image>
        if isinstance(value, list):
            for item in value:
                add_url(item)
            return

    add_url(raw)

    final_image_url = image_urls[0] if image_urls else ""

    return {
        "images_url": final_image_url
    }
```

