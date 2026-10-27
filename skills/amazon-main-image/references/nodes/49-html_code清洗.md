# 49. html code清洗(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `169597` |
| 型別 | `code` |
| 拓樸序 | 49 |
| DAG 層深 | 17 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:`1432717` html生成
- 下游:`116266` html2url_download

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `input` | string | `{{block_output_1432717.body}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `error` | string | 本節點產出 |
| `file_content` | string | 本節點產出 |
| `file_name` | string | 本節點產出 |
| `html_output` | string | 本節點產出 |
| `mime_type` | string | 本節點產出 |
| `success` | string | 本節點產出 |

## 程式碼(python,逐字保留)

````python
import json
import re
from typing import Any


def parse_json_if_possible(value: Any) -> Any:
    """
    如果輸入是 JSON 字串，就轉成 dict。
    如果不是 JSON，就原樣返回。
    """
    if not isinstance(value, str):
        return value

    text = value.strip()

    # 去掉可能包住的 markdown code block
    text = re.sub(r"^```json\s*", "", text, flags=re.I)
    text = re.sub(r"^```\s*", "", text, flags=re.I)
    text = re.sub(r"```$", "", text, flags=re.I).strip()

    try:
        return json.loads(text)
    except Exception:
        return value


def find_html(value: Any, depth: int = 0) -> str:
    """
    遞迴尋找 HTML。
    支援：
    1. {"input": "<!DOCTYPE html>..."}
    2. {"html_output": "<!DOCTYPE html>..."}
    3. {"html": "..."}
    4. {"content": "..."}
    5. 多層包裝的 JSON string
    """
    if depth > 10:
        return ""

    value = parse_json_if_possible(value)

    if isinstance(value, dict):
        # 優先找常見欄位
        for key in [
            "html_output",
            "html",
            "content",
            "input",
            "data",
            "output",
            "result",
            "params"
        ]:
            if key in value:
                result = find_html(value.get(key), depth + 1)
                if result:
                    return result

        # 其他欄位也掃一次，避免上游欄位名稱不固定
        for v in value.values():
            result = find_html(v, depth + 1)
            if result:
                return result

    if isinstance(value, list):
        for item in value:
            result = find_html(item, depth + 1)
            if result:
                return result

    if isinstance(value, str):
        text = value.strip()

        # 判斷是不是 HTML
        if (
            "<!DOCTYPE html" in text[:5000]
            or "<html" in text[:5000]
            or "<body" in text[:8000]
        ):
            return text

    return ""


def clean_html(raw_html: str) -> str:
    """
    清理被 JSON / LLM 節點轉義過的 HTML。
    重點處理：
    - \\n 還原成換行
    - \\" 還原成 "
    - 多餘反斜線清除
    - CSS 裡面每行尾端的 \\\\\\ 清除
    """
    html = raw_html.strip()

    # 如果整段 HTML 又被 JSON stringify 一次，先解一次
    try:
        if html.startswith('"') and html.endswith('"'):
            html = json.loads(html)
    except Exception:
        pass

    # 還原基本跳脫符號
    html = html.replace("\\n", "\n")
    html = html.replace("\\t", "\t")
    html = html.replace('\\"', '"')
    html = html.replace("\\/", "/")

    # 清除每行開頭或結尾殘留的大量反斜線
    html = re.sub(r"\\+\s*\n", "\n", html)
    html = re.sub(r"\n\s*\\+", "\n", html)

    # 清除只有反斜線的空行
    html = re.sub(r"^\s*\\+\s*$", "", html, flags=re.M)

    # 清掉連續反斜線
    html = html.replace("\\\\\\", "")
    html = html.replace("\\\\", "")

    # 清掉 style 標籤附近殘留的反斜線空白
    html = re.sub(r"<style>\s*\\*", "<style>\n", html, flags=re.I)
    html = re.sub(r"\\*\s*</style>", "\n</style>", html, flags=re.I)

    html = html.strip()

    # 如果不是完整 HTML，補完整結構
    if "<!DOCTYPE html" not in html[:500] and "<html" not in html[:500]:
        html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HTML Report</title>
</head>
<body>
{html}
</body>
</html>"""

    return html


async def main(args):
    """
    Coze Python Code 節點入口
    """

    # Coze 通常會把輸入直接放在 args
    params = args

    raw_html = find_html(params)

    if not raw_html:
        return {
            "success": False,
            "file_name": "",
            "file_content": "",
            "html_output": "",
            "mime_type": "",
            "error": "沒有找到 HTML。請確認輸入欄位是 input / html_output / html / content。"
        }

    cleaned_html = clean_html(raw_html)

    return {
        "success": True,
        "file_name": "amazon_a_plus_report.html",
        "file_content": cleaned_html,
        "html_output": cleaned_html,
        "mime_type": "text/html",
        "error": ""
    }
````

