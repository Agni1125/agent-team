# 17. ASIN提取(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `138773` |
| 型別 | `code` |
| 拓樸序 | 17 |
| DAG 層深 | 2 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:`1792347` 競品搜尋
- 下游:`184391` ASIN競品查詢

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `input` | - | `{{block_output_1792347.body}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `asin_array` | list[string] | 本節點產出 |

## 程式碼(python,逐字保留)

```python
import json
import re


async def main(args):
    # ===== 1. 兼容 args 是 object / dict 的情況 =====
    if isinstance(args, dict):
        params = args.get("params", args)
    else:
        params = getattr(args, "params", {}) or {}

    # ===== 2. 優先讀 Coze 測試輸入欄位 input =====
    raw = None

    if isinstance(params, dict):
        for key in ["input", "raw_data", "data", "body", "output", "result"]:
            if params.get(key):
                raw = params.get(key)
                break

    if raw is None:
        raw = params

    # ===== 3. 轉文字，用來做最後保底抓取 =====
    def to_text(value):
        if isinstance(value, str):
            return value
        try:
            return json.dumps(value, ensure_ascii=False)
        except Exception:
            return str(value)

    full_text = to_text(raw)

    # ===== 4. 多層 JSON 字串解析 =====
    def safe_parse(value, max_depth=20):
        current = value

        for _ in range(max_depth):
            if not isinstance(current, str):
                return current

            text = current.strip()

            try:
                current = json.loads(text)
            except Exception:
                return current

        return current

    # ===== 5. 遞迴解析 dict/list 裡面的 JSON 字串 =====
    def deep_parse(value, depth=0):
        if depth > 20:
            return value

        value = safe_parse(value)

        if isinstance(value, dict):
            return {
                k: deep_parse(v, depth + 1)
                for k, v in value.items()
            }

        if isinstance(value, list):
            return [
                deep_parse(v, depth + 1)
                for v in value
            ]

        return value

    parsed = deep_parse(raw)

    # ===== 6. 遞迴搜尋所有 asin 欄位 =====
    asin_array = []

    def add_asin(value):
        if not isinstance(value, str):
            return

        value = value.strip()

        # Amazon ASIN 通常是 10 碼，這裡針對商品 ASIN 抓 B 開頭
        if re.fullmatch(r"B[0-9A-Z]{9}", value):
            if value not in asin_array:
                asin_array.append(value)

    def walk(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if str(k).lower() == "asin":
                    add_asin(v)
                walk(v)

        elif isinstance(obj, list):
            for item in obj:
                walk(item)

        elif isinstance(obj, str):
            # 字串內如果還藏著 ASIN，也抓
            for asin in re.findall(r"\bB[0-9A-Z]{9}\b", obj):
                add_asin(asin)

    walk(parsed)

    # ===== 7. 保底：如果上面還是空，直接從整包 raw text 抓 =====
    if not asin_array:
        for asin in re.findall(r"\bB[0-9A-Z]{9}\b", full_text):
            add_asin(asin)

    return {
        "asin_array": asin_array
    }
```

