# 05. 節點_prompt string轉array(程式碼節點)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `105725` |
| 型別 | `code` |
| 拓樸序 | 5 |
| DAG 層深 | 2 |
| Coze 說明 | 编写代码，处理输入变量来生成返回值 |

## 連線

- 上游:`1942015` Qwen3.5-27B_廣告圖提示詞
- 下游:`139589` 批处理

## 輸入

| 參數 | 型別 | 來源 |
| --- | --- | --- |
| `input` | - | `{{block_output_1942015.body}}` |

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `prompt` | list[string] | 本節點產出 |

## 程式碼(python,逐字保留)

````python
import json
import re
import html


async def main(args: Args) -> Output:
    params = args.params or {}

    # 兼容不同上游欄位
    raw_input = (
        params.get("input")
        or params.get("body")
        or params.get("text")
        or params.get("output")
        or params
    )

    def to_text(value):
        if isinstance(value, str):
            return value
        try:
            return json.dumps(value, ensure_ascii=False)
        except Exception:
            return str(value)

    def clean_text(text):
        if not isinstance(text, str):
            return text

        text = html.unescape(text).strip()

        # 移除 markdown code fence
        text = re.sub(r"^```json\s*", "", text, flags=re.I).strip()
        text = re.sub(r"^```\s*", "", text, flags=re.I).strip()
        text = re.sub(r"\s*```$", "", text, flags=re.I).strip()

        return text

    def try_json_loads(value):
        """
        嘗試把 JSON 字串轉成 dict / list。
        如果不是合法 JSON，就原樣返回。
        """
        if not isinstance(value, str):
            return value

        text = clean_text(value)

        # 先直接 parse
        try:
            return json.loads(text)
        except Exception:
            pass

        # 如果文字前後有廢話，嘗試抓第一個 { 到最後一個 }
        first_obj = text.find("{")
        last_obj = text.rfind("}")
        if first_obj != -1 and last_obj != -1 and last_obj > first_obj:
            possible_json = text[first_obj:last_obj + 1]
            try:
                return json.loads(possible_json)
            except Exception:
                pass

        # 嘗試抓第一個 [ 到最後一個 ]
        first_arr = text.find("[")
        last_arr = text.rfind("]")
        if first_arr != -1 and last_arr != -1 and last_arr > first_arr:
            possible_json = text[first_arr:last_arr + 1]
            try:
                return json.loads(possible_json)
            except Exception:
                pass

        return value

    def deep_parse(value, max_depth=20):
        """
        遞迴解析多層 stringify JSON。
        """
        current = value

        for _ in range(max_depth):
            parsed = try_json_loads(current)

            if parsed == current:
                break

            current = parsed

        return current

    def extract_model_content(value):
        """
        支援：
        1. {"body": "..."}
        2. {"input": "..."}
        3. {"choices": [{"message": {"content": "..."}}]}
        4. 直接是模型輸出 JSON
        """
        current = deep_parse(value)

        if isinstance(current, dict) and "input" in current:
            current = deep_parse(current.get("input"))

        if isinstance(current, dict) and "body" in current:
            current = deep_parse(current.get("body"))

        if isinstance(current, dict) and "choices" in current:
            choices = current.get("choices", [])
            if choices and isinstance(choices, list):
                message = choices[0].get("message", {})
                content = message.get("content", "")
                current = deep_parse(content)

        return current

    def recursive_find_images(obj):
        """
        遞迴尋找 images array。
        """
        if isinstance(obj, dict):
            # 標準格式
            if "promotion_ad_image_prompts" in obj:
                promo_obj = obj.get("promotion_ad_image_prompts", {})
                if isinstance(promo_obj, dict):
                    images = promo_obj.get("images", [])
                    if isinstance(images, list):
                        return images

            # 保底：直接有 images
            if "images" in obj and isinstance(obj.get("images"), list):
                return obj.get("images")

            # 繼續往下找
            for v in obj.values():
                found = recursive_find_images(v)
                if found:
                    return found

        if isinstance(obj, list):
            # 如果這個 list 本身就是 image items
            if obj and all(isinstance(x, dict) for x in obj):
                if any("image_prompt" in x or "prompt" in x for x in obj):
                    return obj

            for v in obj:
                found = recursive_find_images(v)
                if found:
                    return found

        return []

    def normalize_plain_text(value):
        text = to_text(value)

        # 把被 stringify 的換行還原，方便 regex 抓
        text = text.replace("\\n", "\n")
        text = text.replace('\\"', '"')
        text = text.replace("\\/", "/")

        return text.strip()

    def extract_product_info(text):
        """
        從純文字裡抓 PRODUCT_INFO。
        抓不到就用空字串。
        """
        patterns = [
            r"PRODUCT_INFO['\"]?\s*[:：]\s*(.+?)(?=\n\s*['\"]?[A-Z_]+['\"]?\s*[:：]|\n\s*\*|\Z)",
            r"產品資料\s*[:：]\s*(.+?)(?=\n|\Z)",
        ]

        for p in patterns:
            m = re.search(p, text, flags=re.I | re.S)
            if m:
                return m.group(1).strip().strip("'\"")

        return ""

    def extract_brand_info(text):
        patterns = [
            r"BRAND_STYLE_INFO['\"]?\s*[:：]\s*(.+?)(?=\n\s*['\"]?[A-Z_]+['\"]?\s*[:：]|\n\s*\*|\Z)",
            r"品牌風格資料\s*[:：]\s*(.+?)(?=\n|\Z)",
        ]

        for p in patterns:
            m = re.search(p, text, flags=re.I | re.S)
            if m:
                return m.group(1).strip().strip("'\"")

        return ""

    def detect_promotion(text):
        promo_parts = []

        if re.search(r"50\s*%?\s*OFF|50% OFF", text, flags=re.I):
            promo_parts.append("50% OFF")

        if re.search(r"Buy\s*1\s*Get\s*1|BOGO|買一送一", text, flags=re.I):
            promo_parts.append("Buy 1 Get 1 Free")

        if re.search(r"2\s*PACK|2 Pack|兩入|2入", text, flags=re.I):
            promo_parts.append("2 Pack")

        if re.search(r"Limited\s*Time|限時", text, flags=re.I):
            promo_parts.append("Limited Time Deal")

        if promo_parts:
            return " / ".join(dict.fromkeys(promo_parts))

        return "Limited Time Offer"

    def parse_plain_text_images(value):
        """
        當上游不是 JSON，而是文字裡有：
        Image 1 (Hero): ...
        Image 2 (Bundle): ...
        Image 3 (Urgency): ...
        就把它轉成 images array。
        """
        text = normalize_plain_text(value)

        product_info = extract_product_info(text)
        brand_info = extract_brand_info(text)
        promotion = detect_promotion(text)

        image_blocks = []

        pattern = r"(?:^|\n)\s*\*?\s*Image\s*(\d+)\s*[（(]?([^）)\n:]*)[）)]?\s*[:：]\s*(.*?)(?=(?:\n\s*\*?\s*Image\s*\d+\s*[（(]?)|\n\s*\*?\s*\*\*Product Locking|\n\s*Product Locking|\Z)"

        matches = list(re.finditer(pattern, text, flags=re.I | re.S))

        for m in matches:
            image_no = int(m.group(1))
            role = (m.group(2) or "").strip()
            brief = (m.group(3) or "").strip()

            brief = re.sub(r"\s+", " ", brief).strip()

            if not role:
                role = f"Image {image_no}"

            image_blocks.append({
                "image_no": image_no,
                "image_role": role,
                "brief": brief
            })

        # 如果完全抓不到 Image 1/2/3，就不要硬生
        if not image_blocks:
            return []

        negative_prompt = (
            "low quality, blurry, distorted product, wrong product, wrong packaging, "
            "fake unreadable text, messy layout, extra fingers, deformed hands, "
            "cartoon, CGI, 3D render, watermark, random logo, incorrect brand, "
            "overcrowded design, unsupported claims, fake ratings, fake review numbers"
        )

        images = []

        for block in image_blocks:
            image_no = block["image_no"]
            role = block["image_role"]
            brief = block["brief"]

            role_lower = role.lower()
            brief_lower = brief.lower()

            if image_no == 1 or "hero" in role_lower:
                headline = promotion
                image_prompt = f"""
Create a high-conversion Amazon promotional hero image for the product.

Product:
{product_info}

Promotion:
{promotion}

Image Role:
Hero promotion image. The visual should use a large, clear promotion message as the main attention point.

Creative Direction:
Show the Ailun tempered glass screen protector product box, tablet/iPad screen protector, and tablet/iPad together in a clean premium e-commerce layout. Use a bold black-and-gold visual style matching the product packaging. The offer message should feel strong and instantly understandable. The composition should be clean, premium, and conversion-focused, suitable for Amazon listing image or advertising creative.

Main Visual Message:
{headline}

Additional Direction:
{brief}

Brand Style:
{brand_info}

Avoid fake claims, fake review numbers, fake star ratings, and unsupported ranking statements.
""".strip()

            elif image_no == 2 or "bundle" in role_lower or "multi" in brief_lower:
                headline = "2 Pack Value"
                image_prompt = f"""
Create a product value image for an Amazon promotion.

Product:
{product_info}

Promotion:
{promotion}

Image Role:
Bundle or multi-buy value image. The image should clearly communicate that the customer receives strong value from the 2 pack / bundle offer.

Creative Direction:
Show two screen protectors or a clear 2-pack value composition with the Ailun product box and tablet/iPad. The layout should make the bundle benefit easy to understand at a glance. Use clean spacing, premium black-and-gold accents, and a practical product-focused composition. The product should remain realistic and accurately represented.

Main Visual Message:
{headline}

Additional Direction:
{brief}

Brand Style:
{brand_info}

Avoid exaggerated claims, fake ratings, fake reviews, or unrealistic product effects.
""".strip()

            elif image_no == 3 or "urgency" in role_lower or "conversion" in role_lower:
                headline = "Limited Time Deal"
                image_prompt = f"""
Create an urgency-focused Amazon promotional image.

Product:
{product_info}

Promotion:
{promotion}

Image Role:
Urgency and conversion image. The visual should create a clear limited-time promotion feeling without using fake scarcity claims.

Creative Direction:
Show the Ailun tempered glass screen protector product packaging, tablet/iPad, and transparent glass protector in a clean promotional layout. Use strong but simple deal-focused composition. The image should feel like a limited-time offer banner for e-commerce, but still premium and trustworthy. Keep the product accurate and recognizable.

Main Visual Message:
{headline}

Additional Direction:
{brief}

Brand Style:
{brand_info}

Avoid fake countdown timers, fake stock warnings, fake review numbers, and unsupported claims.
""".strip()

            else:
                headline = role
                image_prompt = f"""
Create a realistic Amazon promotional image for the product.

Product:
{product_info}

Promotion:
{promotion}

Image Role:
{role}

Creative Direction:
{brief}

Brand Style:
{brand_info}

Keep the product accurate, premium, clean, and suitable for e-commerce advertising.
Avoid fake claims, fake ratings, and distorted product details.
""".strip()

            images.append({
                "image_no": image_no,
                "image_role": role,
                "headline": headline,
                "image_prompt": image_prompt,
                "negative_prompt": negative_prompt
            })

        return images

    def find_images_object(value):
        current = extract_model_content(value)

        # 先找 JSON 裡的 images
        images = recursive_find_images(current)

        if images:
            return images

        # 如果不是 JSON，就從純文字 Image 1/2/3 轉出 prompts
        return parse_plain_text_images(value)

    images = find_images_object(raw_input)

    prompts = []
    negative_prompts = []
    image_items = []

    for item in images:
        if not isinstance(item, dict):
            continue

        image_prompt = item.get("image_prompt") or item.get("prompt") or ""
        negative_prompt = item.get("negative_prompt", "")

        if isinstance(image_prompt, str) and image_prompt.strip():
            prompts.append(image_prompt.strip())

            negative_prompts.append(
                negative_prompt.strip() if isinstance(negative_prompt, str) else ""
            )

            image_items.append({
                "image_no": item.get("image_no"),
                "image_role": item.get("image_role", ""),
                "headline": item.get("headline", ""),
                "prompt": image_prompt.strip(),
                "negative_prompt": negative_prompt.strip() if isinstance(negative_prompt, str) else ""
            })

    return {
        "prompt": prompts,
        "negative_prompt": negative_prompts,
        "items": image_items,
        "count": len(prompts),

        # debug 用，確認到底抓到什麼
        "debug_input_type": str(type(raw_input)),
        "debug_first_300_chars": normalize_plain_text(raw_input)[:300]
    }
````

