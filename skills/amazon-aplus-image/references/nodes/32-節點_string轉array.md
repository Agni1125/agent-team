# 32. 節點_string轉array(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `105725` |
| 型別 | `code` |
| 拓樸序 | 32 |
| DAG 層深 | 9 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:`185098` Gemimi2.5pro 3.A+圖片提示詞生成
- 下游:`182406` 4.拼圖提示詞

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `input` | - | `{{block_output_185098.body}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `prompt` | list[string] | 本節點產出 |

## 程式碼(javascript,逐字保留)

````javascript
async function main({ params }) {
  function tryParse(value) {
    if (typeof value !== "string") {
      return value;
    }

    let text = value.trim();

    text = text
      .replace(/^```json\s*/i, "")
      .replace(/^```\s*/i, "")
      .replace(/```$/i, "")
      .trim();

    try {
      return JSON.parse(text);
    } catch (err) {
      return value;
    }
  }

  function deepParse(value, maxDepth = 8) {
    let current = value;

    for (let i = 0; i < maxDepth; i++) {
      const parsed = tryParse(current);

      if (parsed === current) {
        break;
      }

      current = parsed;
    }

    return current;
  }

  function extractJsonArrayByKey(text, key) {
    if (typeof text !== "string") {
      return null;
    }

    const keyIndex = text.indexOf(`"${key}"`);
    if (keyIndex === -1) {
      return null;
    }

    const arrayStart = text.indexOf("[", keyIndex);
    if (arrayStart === -1) {
      return null;
    }

    let depth = 0;
    let inString = false;
    let escaped = false;

    for (let i = arrayStart; i < text.length; i++) {
      const char = text[i];

      if (escaped) {
        escaped = false;
        continue;
      }

      if (char === "\\") {
        escaped = true;
        continue;
      }

      if (char === "\"") {
        inString = !inString;
        continue;
      }

      if (!inString) {
        if (char === "[") {
          depth++;
        }

        if (char === "]") {
          depth--;

          if (depth === 0) {
            const arrayText = text.slice(arrayStart, i + 1);
            return JSON.parse(arrayText);
          }
        }
      }
    }

    return null;
  }

  let rawInput = params.input || params;

  let outer = deepParse(rawInput);

  if (outer && outer.input) {
    outer = deepParse(outer.input);
  }

  let apiBody = outer;

  if (outer && outer.body) {
    apiBody = deepParse(outer.body);
  }

  const contentText = apiBody?.choices?.[0]?.message?.content;

  if (!contentText) {
    return {
      prompt: null,
      prompt_count: 0,
      error: "找不到 choices[0].message.content"
    };
  }

  let promptsArray = null;

  const modelOutput = deepParse(contentText);

  if (
    modelOutput &&
    typeof modelOutput === "object" &&
    Array.isArray(modelOutput.prompts_array)
  ) {
    promptsArray = modelOutput.prompts_array;
  }

  if (!Array.isArray(promptsArray)) {
    promptsArray = extractJsonArrayByKey(contentText, "prompts_array");
  }

  if (!Array.isArray(promptsArray)) {
    return {
      prompt: null,
      prompt_count: 0,
      error: "抓不到 prompts_array。請確認 HTTP 節點輸出中有 prompts_array，且沒有在 prompts_array 中間被截斷。"
    };
  }

  return {
    prompt: promptsArray,
    prompt_count: promptsArray.length,
    prompts_array_text: JSON.stringify(promptsArray, null, 2)
  };
}
````

