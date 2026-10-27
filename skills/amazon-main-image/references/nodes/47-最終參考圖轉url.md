# 47. 最終參考圖轉url(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `154873` |
| 型別 | `code` |
| 拓樸序 | 47 |
| DAG 層深 | 15 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:`1412202` 代码_1
- 下游:`1432717` html生成

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `imageurl` | list | `{{block_output_147162.url_list}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `final_images_text` | string | 本節點產出 |

## 程式碼(python,逐字保留)

```python
import json
import re


async def main(args):
    # ===== 1. 读取输入参数 =====
    params = getattr(args, "params", None) or {}

    raw = (
        params.get("output")
        or params.get("body")
        or params.get("data")
        or params.get("result")
        or params.get("input")
        or params
    )

    # ===== 2. 安全 JSON 解析：处理字符串化数组 / 字符串化对象 =====
    def safe_parse(value, max_depth=5):
        current = value

        for _ in range(max_depth):
            if not isinstance(current, str):
                return current

            text = current.strip()

            if not (
                (text.startswith("{") and text.endswith("}"))
                or (text.startswith("[") and text.endswith("]"))
            ):
                return current

            try:
                current = json.loads(text)
            except Exception:
                return current

        return current

    parsed = safe_parse(raw)

    # ===== 3. 递归提取所有图片 URL =====
    image_urls = []

    def add_url_from_text(text):
        if not isinstance(text, str):
            return

        matches = re.findall(r"https?://[^\s\"'<>\\]+", text)

        for url in matches:
            url = (
                url.strip()
                .replace("&amp;", "&")
                .rstrip("，。,.);]}\"'")
            )

            is_image_url = (
                re.search(r"\.(jpg|jpeg|png|webp|gif)(\?|$)", url, re.I)
                or "image" in url.lower()
                or "img" in url.lower()
                or "oss." in url.lower()
                or "byteimg" in url.lower()
                or "tos-cn" in url.lower()
            )

            if is_image_url and url not in image_urls:
                image_urls.append(url)

    def walk(value):
        value = safe_parse(value)

        if value is None:
            return

        if isinstance(value, str):
            add_url_from_text(value)
            return

        if isinstance(value, list):
            for item in value:
                walk(item)
            return

        if isinstance(value, dict):
            # 优先处理常见图片字段
            preferred_keys = [
                "image_url",
                "imageUrl",
                "url",
                "final_image_url",
                "finalImageUrl",
                "output_url",
                "outputUrl",
                "result_url",
                "resultUrl",
                "image_urls",
                "images",
                "final_images",
                "output",
                "data",
                "result",
            ]

            for key in preferred_keys:
                if key in value:
                    walk(value.get(key))

            # 再兜底扫所有字段
            for key, item in value.items():
                if key not in preferred_keys:
                    walk(item)

            return

    walk(parsed)

    # ===== 4. 二次清洗：只保留 http/https 图片 URL，并去重 =====
    cleaned_urls = []

    for url in image_urls:
        if not isinstance(url, str):
            continue

        url = url.strip()

        if not re.match(r"^https?://", url, re.I):
            continue

        if not (
            re.search(r"\.(jpg|jpeg|png|webp|gif)(\?|$)", url, re.I)
            or "image" in url.lower()
            or "img" in url.lower()
            or "oss." in url.lower()
            or "byteimg" in url.lower()
            or "tos-cn" in url.lower()
        ):
            continue

        if url not in cleaned_urls:
            cleaned_urls.append(url)

    # ===== 5. 生成给 GLM 使用的结构 =====
    final_images = []

    for index, url in enumerate(cleaned_urls):
        final_images.append({
            "image_id": f"final_image_{index + 1}",
            "image_index": index + 1,
            "url": url
        })

    # ===== 6. 额外生成 HTML img 片段，方便测试用 =====
    html_img_snippet = "\n".join([
        f'<img src="{item["url"]}" alt="Final Image {item["image_index"]}" loading="lazy">'
        for item in final_images
    ])

    # ===== 7. 输出给下游 GLM 节点 =====
    return {
        "success": len(cleaned_urls) > 0,
        "image_count": len(cleaned_urls),
        "image_urls": cleaned_urls,
        "image_urls_text": json.dumps(cleaned_urls, ensure_ascii=False, indent=2),
        "first_image_url": cleaned_urls[0] if cleaned_urls else "",
        "final_images": final_images,
        "final_images_text": json.dumps(final_images, ensure_ascii=False, indent=2),
        "html_img_snippet": html_img_snippet,
        "debug_raw_type": str(type(raw)),
        "debug_raw_preview": str(raw)[:500]
    }
```

