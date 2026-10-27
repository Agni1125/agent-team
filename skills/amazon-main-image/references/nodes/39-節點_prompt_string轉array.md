# 39. 節點_prompt string轉array(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `105725` |
| 型別 | `code` |
| 拓樸序 | 39 |
| DAG 層深 | 9 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:`185098` Gemimi2.5pro 3.生成主圖+輔圖提示詞
- 下游:`182406` 4.拼圖提示詞

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `input` | - | `{{block_output_185098.body}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `prompt` | list[string] | 本節點產出 |

## 程式碼(python,逐字保留)

````python
import json
import re


async def main(args: Args) -> Output:
    params = args.params
    raw_input = params.get("input", "")

    def try_parse(value):
        if not isinstance(value, str):
            return value

        text = value.strip()

        text = re.sub(r"^```json\s*", "", text, flags=re.I).strip()
        text = re.sub(r"^```\s*", "", text, flags=re.I).strip()
        text = re.sub(r"```$", "", text, flags=re.I).strip()

        try:
            return json.loads(text)
        except Exception:
            return value

    def deep_parse(value, max_depth=12):
        current = value

        for _ in range(max_depth):
            parsed = try_parse(current)

            if parsed == current:
                break

            current = parsed

        return current

    def find_model_content(value, max_depth=12):
        current = deep_parse(value)

        for _ in range(max_depth):
            current = deep_parse(current)

            if isinstance(current, dict):
                choices = current.get("choices")

                if isinstance(choices, list) and choices:
                    first = choices[0]

                    if isinstance(first, dict):
                        message = first.get("message", {})

                        if isinstance(message, dict) and isinstance(message.get("content"), str):
                            return message.get("content")

                for key in ["body", "input", "output", "result", "data", "content"]:
                    if isinstance(current.get(key), str):
                        current = current.get(key)
                        break
                else:
                    return current

            else:
                return current

        return current

    def find_key_recursive(obj, target_key, max_depth=10):
        obj = deep_parse(obj)

        if max_depth < 0:
            return None

        if isinstance(obj, dict):
            if target_key in obj:
                return obj[target_key]

            for value in obj.values():
                found = find_key_recursive(value, target_key, max_depth - 1)
                if found is not None:
                    return found

        elif isinstance(obj, list):
            for item in obj:
                found = find_key_recursive(item, target_key, max_depth - 1)
                if found is not None:
                    return found

        return None

    def normalize_prompt_array(value):
        value = deep_parse(value)

        if not isinstance(value, list):
            return None

        result = []

        for item in value:
            if isinstance(item, str) and item.strip():
                result.append(item.strip())

            elif isinstance(item, dict):
                prompt_text = (
                    item.get("edit_prompt")
                    or item.get("prompt")
                    or item.get("image_prompt")
                    or item.get("final_prompt")
                    or item.get("generation_prompt")
                    or ""
                )

                if isinstance(prompt_text, str) and prompt_text.strip():
                    result.append(prompt_text.strip())

        return result if result else None

    def extract_string_values_by_key(text, key):
        if not isinstance(text, str):
            return []

        candidates = [
            text,
            text.replace('\\"', '"').replace("\\\\", "\\")
        ]

        results = []

        for candidate in candidates:
            i = 0
            pattern = f'"{key}"'
            n = len(candidate)

            while True:
                key_index = candidate.find(pattern, i)

                if key_index == -1:
                    break

                colon_index = candidate.find(":", key_index + len(pattern))

                if colon_index == -1:
                    break

                j = colon_index + 1

                while j < n and candidate[j] in " \t\r\n":
                    j += 1

                if j >= n or candidate[j] != '"':
                    i = j + 1
                    continue

                start = j
                j += 1
                escaped = False

                while j < n:
                    ch = candidate[j]

                    if escaped:
                        escaped = False

                    elif ch == "\\":
                        escaped = True

                    elif ch == '"':
                        raw_string = candidate[start:j + 1]

                        try:
                            value = json.loads(raw_string)
                        except Exception:
                            value = raw_string[1:-1]

                        if isinstance(value, str) and value.strip():
                            results.append(value.strip())

                        j += 1
                        break

                    j += 1

                else:
                    break

                i = j

            if results:
                break

        deduped = []
        seen = set()

        for item in results:
            if item not in seen:
                deduped.append(item)
                seen.add(item)

        return deduped

    def extract_json_string_array_by_key(text, key):
        if not isinstance(text, str):
            return []

        candidates = [
            text,
            text.replace('\\"', '"').replace("\\\\", "\\")
        ]

        for candidate in candidates:
            key_index = candidate.find(f'"{key}"')

            if key_index == -1:
                continue

            array_start = candidate.find("[", key_index)

            if array_start == -1:
                continue

            result = []
            i = array_start + 1
            n = len(candidate)

            while i < n:
                while i < n and candidate[i] in " \t\r\n,":
                    i += 1

                if i >= n or candidate[i] == "]":
                    break

                if candidate[i] != '"':
                    break

                start = i
                i += 1
                escaped = False

                while i < n:
                    ch = candidate[i]

                    if escaped:
                        escaped = False

                    elif ch == "\\":
                        escaped = True

                    elif ch == '"':
                        raw_string = candidate[start:i + 1]

                        try:
                            value = json.loads(raw_string)
                        except Exception:
                            value = raw_string[1:-1]

                        if isinstance(value, str) and value.strip():
                            result.append(value.strip())

                        i += 1
                        break

                    i += 1

                else:
                    break

            if result:
                return result

        return []

    content_text = find_model_content(raw_input)
    parsed_content = deep_parse(content_text)

    prompts_array = None

    prompts_value = find_key_recursive(parsed_content, "prompts_array")
    prompts_array = normalize_prompt_array(prompts_value)

    if not prompts_array:
        prompts_field = find_key_recursive(parsed_content, "prompts")
        prompts_array = normalize_prompt_array(prompts_field)

    if not prompts_array and isinstance(content_text, str):
        prompts_array = extract_string_values_by_key(content_text, "edit_prompt")

    if not prompts_array and isinstance(content_text, str):
        prompts_array = extract_json_string_array_by_key(content_text, "prompts_array")

    if not prompts_array:
        prompts_array = []

    return {
        "prompt": prompts_array
    }
````

