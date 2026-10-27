# 06. Html代碼編譯(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `180775` |
| 型別 | `code` |
| 拓樸序 | 6 |
| DAG 層深 | 0 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:（無,起點或孤立節點）
- 下游:（無）

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `html_code` | string | `{{block_output_186013.body}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `html_output` | string | 本節點產出 |

## 程式碼(python,逐字保留)

````python
import json
import re
import html as html_lib

async def main(args):
    # 兼容 Coze args.params / dict 兩種格式
    if hasattr(args, "params"):
        params = args.params or {}
    elif isinstance(args, dict):
        params = args.get("params", args) or {}
    else:
        params = {}

    KEY_PRIORITY = [
        "html_code",
        "html_output",
        "html",
        "output",
        "result",
        "data",
        "key0",
        "input"
    ]

    VOID_TAGS = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"
    }

    def to_text(value):
        if value is None:
            return ""

        if isinstance(value, dict):
            for key in KEY_PRIORITY:
                if key in value:
                    return to_text(value[key])
            return json.dumps(value, ensure_ascii=False)

        if isinstance(value, list):
            return "\n".join(to_text(x) for x in value)

        return str(value)

    def strip_code_block(text):
        text = str(text).strip()
        text = re.sub(r"^```(?:html|json)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)
        return text.strip()

    def deep_unescape(raw):
        text = strip_code_block(to_text(raw))

        for _ in range(10):
            old = text

            # 如果外層是 JSON 字串或 JSON 物件，先拆開
            try:
                parsed = json.loads(text)
                text = strip_code_block(to_text(parsed))
            except Exception:
                pass

            # HTML entity 反轉義
            text = html_lib.unescape(text)

            # JSON escape 反轉義
            text = text.replace("\\r\\n", "\n")
            text = text.replace("\\n", "\n")
            text = text.replace("\\t", "\t")
            text = text.replace('\\"', '"')
            text = text.replace("\\'", "'")
            text = text.replace("\\/", "/")

            text = text.strip()

            if text == old:
                break

        # 如果最外層還有一組引號，移除
        if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
            text = text[1:-1].strip()

        return text

    def cut_from_html_start(text):
        lower = text.lower()
        starts = []

        for marker in [
            "<!doctype html",
            "<html",
            "<head",
            "<body",
            '<div class="container"',
            "<main",
            "<section"
        ]:
            pos = lower.find(marker)
            if pos != -1:
                starts.append(pos)

        if starts:
            text = text[min(starts):].strip()

        # 清掉尾端可能殘留的 JSON 包裝
        text = re.sub(r'"\s*}\s*"\s*}\s*$', "", text).strip()
        text = re.sub(r'"\s*}\s*$', "", text).strip()
        text = re.sub(r'"}\s*$', "", text).strip()
        text = re.sub(r'"\s*$', "", text).strip()

        return text

    def clean_title(text):
        titles = re.findall(
            r"<title[^>]*>(.*?)</title>",
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

        title = "HTML Report"

        # 優先取最後一個非空、非預設 title
        for item in reversed(titles):
            t = re.sub(r"<[^>]+>", "", item).strip()
            t = html_lib.unescape(t)
            if t and t.lower() != "html report":
                title = t
                break

        return html_lib.escape(title, quote=False)

    def clean_css(text):
        css_blocks = re.findall(
            r"<style[^>]*>(.*?)</style>",
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

        # 如果 style 沒有正常閉合，抓 style 到 head/body 前
        if not css_blocks:
            m = re.search(
                r"<style[^>]*>(.*?)(?:</head>|<body|$)",
                text,
                flags=re.IGNORECASE | re.DOTALL
            )
            if m:
                css_blocks = [m.group(1)]

        css = "\n".join(css_blocks).strip()

        # 修掉之前錯誤節點造成的 title/style 混入 CSS
        css = re.sub(
            r"<title[^>]*>.*?</title>",
            "",
            css,
            flags=re.IGNORECASE | re.DOTALL
        )
        css = re.sub(r"</?style[^>]*>", "", css, flags=re.IGNORECASE)
        css = re.sub(r"</?head[^>]*>", "", css, flags=re.IGNORECASE)
        css = re.sub(r"</?body[^>]*>", "", css, flags=re.IGNORECASE)
        css = re.sub(r"</?html[^>]*>", "", css, flags=re.IGNORECASE)

        css = css.strip()

        # 如果沒有 CSS，補最低限度樣式，避免白板
        if not css:
            css = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft JhengHei", "Noto Sans TC", Arial, sans-serif;
    background: #f5f7fb;
    color: #374151;
    line-height: 1.6;
}
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem 1.5rem;
}
""".strip()

        return css

    def extract_body(text):
        # 優先抓 body 裡面的內容
        body_match = re.search(
            r"<body[^>]*>(.*?)(?:</body>|$)",
            text,
            flags=re.IGNORECASE | re.DOTALL
        )

        if body_match:
            body_html = body_match.group(1).strip()
        else:
            # 沒有 body，就從主要內容容器開始抓
            lower = text.lower()
            starts = []

            for marker in [
                '<div class="container"',
                "<main",
                "<section"
            ]:
                pos = lower.find(marker)
                if pos != -1:
                    starts.append(pos)

            if starts:
                body_html = text[min(starts):].strip()
            else:
                # 最後兜底：移除 head/style 後當 body
                body_html = text

        # 移除不應該出現在 body 的外層殘留
        body_html = re.sub(r"<!doctype[^>]*>", "", body_html, flags=re.IGNORECASE)
        body_html = re.sub(r"</?html[^>]*>", "", body_html, flags=re.IGNORECASE)
        body_html = re.sub(
            r"<head[^>]*>.*?</head>",
            "",
            body_html,
            flags=re.IGNORECASE | re.DOTALL
        )
        body_html = re.sub(
            r"<style[^>]*>.*?</style>",
            "",
            body_html,
            flags=re.IGNORECASE | re.DOTALL
        )
        body_html = re.sub(r"</?body[^>]*>", "", body_html, flags=re.IGNORECASE)

        # 清掉尾端 JSON 殘留
        body_html = re.sub(r'"\s*}\s*"\s*}\s*$', "", body_html).strip()
        body_html = re.sub(r'"\s*}\s*$', "", body_html).strip()
        body_html = re.sub(r'"}\s*$', "", body_html).strip()
        body_html = re.sub(r'"\s*$', "", body_html).strip()

        return body_html.strip()

    def auto_close_tags(fragment):
        """
        自動補齊被截斷 HTML 的未關閉標籤。
        不會補內容，只補結構，避免 html2url 或瀏覽器解析失敗。
        """
        stack = []

        tag_pattern = re.compile(
            r"<!--.*?-->|<![^>]*>|<\s*(/)?\s*([a-zA-Z][a-zA-Z0-9:-]*)([^>]*)>",
            flags=re.DOTALL
        )

        for m in tag_pattern.finditer(fragment):
            full = m.group(0)

            if full.startswith("<!--") or full.startswith("<!"):
                continue

            is_close = bool(m.group(1))
            tag = (m.group(2) or "").lower()
            rest = m.group(3) or ""

            if not tag or tag in VOID_TAGS:
                continue

            if is_close:
                if tag in stack:
                    while stack:
                        top = stack.pop()
                        if top == tag:
                            break
                continue

            if rest.strip().endswith("/"):
                continue

            stack.append(tag)

        # 反向補齊未關閉標籤
        if stack:
            fragment += "\n" + "".join(f"</{tag}>" for tag in reversed(stack))

        return fragment

    def build_final_html(raw):
        text = deep_unescape(raw)
        text = cut_from_html_start(text)

        title = clean_title(text)
        css = clean_css(text)
        body_html = extract_body(text)

        if not body_html:
            body_html = """
<div class="container">
    <section class="section">
        <h1>HTML Parse Error</h1>
        <p>No valid HTML body content found.</p>
    </section>
</div>
""".strip()

        body_html = auto_close_tags(body_html)

        final_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
{body_html}
</body>
</html>"""

        return final_html.strip()

    raw = (
        params.get("html_code")
        or params.get("html_output")
        or params.get("html")
        or params.get("output")
        or params.get("result")
        or params.get("data")
        or params.get("input")
        or params
    )

    html_code = build_final_html(raw)

    return {
        "html_code": html_code,
        "html_output": html_code
    }
````

