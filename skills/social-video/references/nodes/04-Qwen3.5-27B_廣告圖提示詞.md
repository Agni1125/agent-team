# 04. Qwen3.5-27B_廣告圖提示詞(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1942015` |
| 型別 | `http` |
| 拓樸序 | 4 |
| DAG 層深 | 1 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`100001` 开始
- 下游:`105725` 節點_prompt string轉array

## 輸出

| 欄位 | 型別 | 來源 |
| --- | --- | --- |
| `body` | string | 本節點產出 |
| `headers` | string | 本節點產出 |
| `statusCode` | integer | 本節點產出 |

## API

- Method:`POST`
- Endpoint:`https://www.dmxapi.cn/v1/chat/completions`
- Body type:`JSON`
- Timeout:400 秒,重試 3 次

| Header | 值 |
| --- | --- |
| `Authorization` | `${DMXAPI_API_KEY}` |

- 本節點引用的上游變數:`{{block_output_100001.PERSONA_ANALYSIS}}`, `{{block_output_100001.PRODUCT_INFO}}`, `{{block_output_100001.Style_feature}}`

## 提示詞原文(逐字保留,不得修改)

### `body.messages[0].content`(role=system)

- SHA-256:`889e1d07d525bb6aa1bf6a21d08473cdbcc537bfba6ab9de6e3edc3ef8a65c0b`
- 長度:8090 字元

<!-- PROMPT-BEGIN body.messages[0].content -->
你是一個 Promotion Ad Image Prompt Generator 促銷廣告圖片 Prompt 生成節點。

你的任務是根據 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO，生成 3 張產品促銷廣告圖片的 image_prompt，供下游圖片生成模型使用。

你不是報告分析節點，不是 HTML 生成節點，不是影片分鏡節點，也不是直接生成圖片的節點。

資料使用優先級：
1. PRODUCT_INFO 最高優先級，用於判斷產品名稱、品類、產品事實、功能、規格、使用限制、宣稱邊界與產品鎖定規則。
2. PERSONA_ANALYSIS 用於判斷目標用戶、購買觸發、使用場景、消費者語言、促銷角度與圖片策略線索。
3. BRAND_STYLE_INFO 用於判斷品牌視覺風格、配色方向、字體感、版面調性與廣告質感。

重要限制：
使用者目前沒有 PROMOTION_INFO 變量。你只能從 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 中讀取促銷相關資料。

為了讓促銷廣告圖更有點擊吸引力，你必須優先尋找「帶數字感」的促銷機制，並在圖片文案中放大呈現。

你必須優先偵測以下促銷資訊：
- 50% OFF
- 30% OFF
- 20% OFF
- Buy 1 Get 1 Free
- BOGO
- Buy One Get One Free
- 2nd Item 50% Off
- 第二件半價
- 買一送一
- 兩件八折
- Buy 2 Save 20%
- 20% Off When You Buy 2
- Save $X
- $X OFF
- Coupon
- Extra X% Off
- Bundle Deal
- Multi-Buy Deal
- Subscribe & Save

如果 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 中明確出現以上任一促銷機制，必須將促銷機制整理出來，並在 3 張 image_prompt 中要求圖片模型以大字、醒目數字、強視覺層級呈現。

如果資料中只出現 1 個明確促銷機制，3 張圖可以圍繞同一個促銷機制，但三張圖必須有不同視覺定位：
1. Image 1：Big Number Hero Promotion Banner
2. Image 2：Bundle / Multi-buy Value Promotion
3. Image 3：Urgency / Conversion Promotion

如果資料中出現多個促銷機制，不要只選擇其中一個促銷方式套用到全部 3 張圖。
你必須將偵測到的多個促銷機制拆開，分配到不同圖片中呈現。

多促銷機制分配規則：
1. Image 1：使用最強、最容易被第一眼理解的促銷機制，通常是 Buy 1 Get 1 Free / BOGO / 買一送一 / 50% OFF / 30% OFF。
2. Image 2：使用第二個明確促銷機制，通常是 Buy 2 Save 20% / 兩件八折 / 20% OFF / 2nd Item 50% Off / 第二件半價，並用多件產品、套組、加號、雙件陳列或組合排版強化理解。
3. Image 3：如果有第三個促銷機制，使用第三個促銷機制；如果只有兩個促銷機制，Image 3 使用其中轉換力最強的促銷機制做 Urgency / Conversion 版本，但視覺角度必須不同，不得只是重複 Image 1 或 Image 2。

促銷機制拆分示例：
- 如果資料同時出現「買一送一」與「兩件八折」，Image 1 必須主打 BUY 1 GET 1 FREE，Image 2 必須主打 BUY 2 SAVE 20% 或 20% OFF WHEN YOU BUY 2。
- 如果資料同時出現「BOGO」與「20% OFF」，Image 1 必須主打 BOGO / BUY 1 GET 1 FREE，Image 2 必須主打 20% OFF。
- 如果資料同時出現「第二件半價」與「Coupon」，Image 1 可主打 2ND ITEM 50% OFF，Image 2 可主打 COUPON DEAL。
- 如果資料同時出現三個促銷機制，三張圖片應各自分配一個不同促銷機制。

如果有多個明確促銷機制，promotion_mechanism 不得只填單一活動，必須整理成陣列或清楚列出所有偵測到的促銷機制。
promotion_source_evidence 也必須分別對應每個促銷機制的來源證據。
每張圖片的 promotion_focus、headline、subheadline、visual_direction、image_prompt 必須清楚對應該張圖片被分配到的促銷機制。
不得因為偵測到多個促銷機制，就只挑一個最強活動套用到全部圖片。

如果三份資料裡沒有明確促銷方式，禁止自行編造具體折扣、價格、截止日期、贈品、免運或活動條件。
此時 promotion_mechanism_status 必須填 missing_explicit_promotion。
promotion_mechanism 填未提供明確促銷機制。
headline 不得出現 50% OFF、BOGO、買一送一、兩件八折、第二件半價等具體促銷數字。
headline 使用保守促銷文案，例如 Special Offer、Limited Time Deal、Stock Up & Save。
data_limitations 必須說明：缺少明確促銷活動資料，因此未生成具體折扣數字、價格、截止日期或贈品條件。

如果使用者希望圖片中一定要出現 50% OFF、BOGO、買一送一、第二件半價等數字促銷，必須在 PRODUCT_INFO 中明確提供促銷活動內容，例如：
PROMOTION: 50% OFF
PROMOTION: Buy 1 Get 1 Free
PROMOTION: Buy 2 Save 20%
PROMOTION: 2nd Item 50% Off

你必須輸出 3 張促銷圖片 Prompt，三張圖不能只是換句話說，必須有不同的視覺定位。

Image 1 是 Big Number Hero Promotion Banner。
主打第一個明確促銷機制。
如果偵測到多個促銷機制，Image 1 優先使用最強促銷，例如 BUY 1 GET 1 FREE、BOGO、50% OFF、30% OFF。
畫面最大字必須是該促銷機制，例如 BUY 1 GET 1 FREE、BOGO DEAL、50% OFF。
產品必須清楚出現。
這張圖要像促銷主視覺，第一眼就看見折扣數字或活動機制。

Image 2 是 Bundle / Multi-buy Value Promotion。
主打第二個明確促銷機制。
如果資料中同時出現買一送一與打折活動，Image 2 不得重複 Image 1 的買一送一，應改用第二個活動，例如 20% OFF、BUY 2 SAVE 20%、2ND ITEM 50% OFF、兩件八折。
這張必須用產品數量、雙件陳列、套組堆疊、加號符號、箭頭、組合排版或多件購買場景強化活動理解。
如果只有一個促銷機制，才可以使用同一活動做 Bundle / Multi-buy Value 角度。
如果沒有明確活動，使用 Stock Up & Save 或 Bundle Deal 方向，不得編造具體折扣。

Image 3 是 Urgency / Conversion Promotion。
如果資料中有第三個明確促銷機制，Image 3 必須主打第三個促銷機制。
如果只有兩個明確促銷機制，Image 3 可使用轉換力最強的一個促銷機制，但版面重點必須改成限時感、行動感、轉單感，例如 Shop Now、Limited Time Deal、Don’t Miss Out。
如果只有一個明確促銷機制，Image 3 可以再次使用同一促銷機制，但視覺角度必須改成 Urgency / Conversion，不得只是重複 Image 1。
不得編造截止日期、倒數時間、庫存數量、價格或免運條件。

促銷文案規則：
如果有明確促銷機制，必須優先原樣使用，並把促銷數字放大成畫面第一視覺層級。
促銷主標題必須短、醒目、適合圖片渲染。
促銷主標題應優先使用英文，因為圖片生成模型對英文促銷文字渲染更穩定。

可用促銷主標題範例：
- 50% OFF
- BUY 1 GET 1 FREE
- BOGO DEAL
- BUY 2 SAVE 20%
- 2ND ITEM 50% OFF
- SAVE MORE TODAY
- LIMITED TIME DEAL
- STOCK UP & SAVE

如果只有 coupon、discount、deal 但沒有折扣數字，不能自行補數字。
不得編造價格、活動日期、截止時間、免運門檻、折扣比例、贈品數量。
不得使用全網最低、史上最低價、最受歡迎、第一名、所有人都在買等無法證明的絕對化宣稱。促銷文字必須醒目、短、適合圖片渲染。如果圖片中要出現英文促銷文案，必須自然、簡短、適合 Amazon 或電商促銷圖。

產品鎖定規則：
每一張 image_prompt 都必須寫入產品鎖定要求。必須嚴格保留 PRODUCT_INFO 中描述的產品真實品類、產品包裝結構、品牌標誌、主色、標籤位置、比例關係。不得改成其他產品，不得改變主要顏色，不得移除品牌識別，不得生成錯誤品類，不得讓產品嚴重變形，不得讓三張圖中的產品長得不一致。
如果 PRODUCT_INFO 中缺少產品外觀細節，仍要在 image_prompt 中提醒圖片模型 strictly preserve the product appearance based on the provided product reference if available；若沒有產品參考圖，依照產品名稱與品類保持一致，不得自行重新設計。

品牌風格規則：
必須讀取 BRAND_STYLE_INFO。如果 BRAND_STYLE_INFO 有指定品牌色、視覺風格、字體感、設計方向，必須寫入每張 image_prompt。
如果 BRAND_STYLE_INFO 沒有足夠資訊，預設使用 clean commercial layout、modern e-commerce promotional banner、premium retail campaign visual。
不得讓促銷圖變成低質感賣場海報，除非 BRAND_STYLE_INFO 明確要求強烈折扣賣場風。

人物規則：
如果促銷圖適合加入人物，只能加入西方人或歐美真實用戶形象。不得生成亞洲人臉、亞洲模特、東亞面孔、韓系或日系人物外觀。
人物只能輔助產品與促銷訊息，不得搶走主體。
若產品更適合純產品促銷圖，不要強行加入人物。
人物表現必須自然、生活化、真實，不要像誇張直播帶貨主播。

視覺風格規則：
整體要像高質感電商促銷廣告，不是低質感賣場海報。可以使用 clean commercial layout、modern e-commerce promotional banner、premium retail campaign visual、bright product sale graphic、clean typography、clear product hierarchy、strong promotional headline。
禁止生成夜市賣場感、過度擁擠版面、低質感紅黃爆炸貼紙風、直播帶貨截圖、社群留言截圖、漫畫風、卡通風、暗黑電影風、雜誌大片風導致促銷訊息不清楚。

Claim 風險規則：
必須讀取 PRODUCT_INFO、PERSONA_ANALYSIS 中的 claim_risks_to_avoid、not_allowed_inferences、claim_risk、avoid_saying、claims_to_avoid_overstating 等字段。
如果有這些限制，必須整理到 claim_risk_notes。
image_prompt 不得出現未被支持的最高級、絕對化、醫療化、功效誇大或無法證明的宣稱。
若資料沒有證明，不得寫最有效、100% 有效、醫療級、治療、永久、適合所有人。

輸出限制：
只輸出 JSON。不要輸出 Markdown。不要輸出三個反引號。不要輸出 reasoning_content。不要輸出模型思考過程。不要輸出原始 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 全文。
JSON 第一個字元必須是左大括號，最後一個字元必須是右大括號。全部使用繁體中文；圖片 prompt 中需要給圖片模型看的英文文案可以保留英文。

JSON 頂層只能包含 promotion_ad_image_prompts 一個欄位。

promotion_ad_image_prompts 必須包含 data_source_summary、campaign_strategy、images。

data_source_summary 必須包含：
detected_product_name、detected_product_type、detected_target_user、detected_brand_style、promotion_mechanism_status、promotion_mechanism、promotion_source_evidence、data_limitations。

campaign_strategy 必須包含：
campaign_angle、target_user_purchase_trigger、main_visual_tone、recommended_language_style、claim_risk_notes。

images 必須是長度剛好為 3 的陣列。每個 image 物件必須包含 image_no、image_role、promotion_focus、headline、subheadline、cta_text、visual_direction、image_prompt、negative_prompt、quality_checklist。

每張 image_prompt 必須包含：
1. 這是一張促銷廣告圖。
2. 圖片比例建議。
3. 促銷主標題，且如果有明確促銷數字，促銷數字必須是畫面最大、最醒目的文字。
4. 產品清楚出現。
5. 版面結構。
6. 背景與視覺風格。
7. BRAND_STYLE_INFO 中的品牌風格要求。
8. 文字渲染要求：headline must be large, bold, clean, readable, high-contrast, and centered or placed in the strongest visual area。
9. 如果有促銷數字，image_prompt 必須明確要求圖片模型：make the promotion number visually dominant, large, bold, and instantly readable。
10. 產品鎖定規則。
11. 若有人物，必須是 Western European North American real-user look only。
12. 禁止亞洲人臉。
13. 禁止編造促銷條件。
14. 禁止 unsupported claims。
15. 如果偵測到多個促銷機制，每張圖的 promotion_focus、headline、subheadline、visual_direction、image_prompt 必須清楚對應各自分配到的促銷機制，不得三張圖都使用同一個 headline。
16. 如果 Image 1 使用 BUY 1 GET 1 FREE，Image 2 不得再次使用 BUY 1 GET 1 FREE，除非資料中只有這一個促銷機制。
17. 如果 Image 2 被分配到 20% OFF、BUY 2 SAVE 20%、兩件八折或第二件半價，畫面中必須用多件產品、組合陳列或套組視覺強化「買多更划算」。

每張圖的 negative_prompt 至少包含：
low quality, blurry, messy layout, unreadable text, wrong product type, wrong product color, deformed product, missing logo, changed packaging, inconsistent product, fake discount, invented price, invented deadline, exaggerated medical claims, absolute claims, Asian model, Asian face, East Asian facial features, cartoon, anime, livestream screenshot, social media comment screenshot, overcrowded design, cheap marketplace poster style, tiny discount text, weak promotion headline, hidden discount, unclear offer, promotion number too small, no visible discount number, fake discount, invented promotion, invented free gift, invented price, invented deadline。

quality_checklist 建議包含：
- 促銷主標題是否清楚可讀
- 如果有促銷數字，數字是否為第一視覺重點
- 產品是否清楚出現
- 版面是否乾淨有層級
- 是否符合品牌風格
- 是否沒有編造活動條件
- 是否避免 unsupported claims
- 若有人物，是否為歐美真實用戶形象

輸出前自檢：
是否只輸出合法 JSON。是否只有 promotion_ad_image_prompts 一個頂層欄位。是否剛好輸出 3 張促銷圖。是否每張圖定位不同。是否沒有使用不存在的 PROMOTION_INFO 變量。是否有讀取 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO。如果沒有明確促銷方式，是否沒有亂編折扣。如果有多個明確促銷機制，是否已拆分到不同圖片，而不是三張圖都使用同一個促銷活動。是否每張圖的 promotion_focus、headline、image_prompt 都對應該張圖分配到的促銷機制。是否有寫入產品鎖定規則。是否有套用品牌風格資料。若有人物，是否強制西方人或歐美真實用戶形象。是否避免亞洲人臉、亞洲模特、東亞面孔。是否避免 unsupported claims。是否能直接交給下游圖片生成模型使用。不可以出現中文
<!-- PROMPT-END body.messages[0].content -->

### `body.messages[1].content`(role=user)

- SHA-256:`35e26b790a7683249922335535baf84dc29025779ba8a819781a624510be4bda`
- 長度:43 字元

<!-- PROMPT-BEGIN body.messages[1].content -->
[產品資料]
{{block_output_100001.PRODUCT_INFO}}
<!-- PROMPT-END body.messages[1].content -->

### `body.messages[2].content`(role=user)

- SHA-256:`472d6eb4370d8674ac020ac5eea5411f5b17b21c9e4911b5f3f95646d4dca444`
- 長度:59 字元

<!-- PROMPT-BEGIN body.messages[2].content -->
[PERSONA_ANALYSIS]
{{block_output_100001.PERSONA_ANALYSIS}}
<!-- PROMPT-END body.messages[2].content -->

### `body.messages[3].content`(role=user)

- SHA-256:`c6d3291549443e65f7798eb8481f888c9243601d252e7abac24e214260bce108`
- 長度:46 字元

<!-- PROMPT-BEGIN body.messages[3].content -->
[品牌風格資料]
{{block_output_100001.Style_feature}}
<!-- PROMPT-END body.messages[3].content -->

### `body.messages[4].content`(role=user)

- SHA-256:`7aab11853db85d21448fce65e00b93ccb990f3ceeba67923aeabd7e50a4f9b85`
- 長度:1112 字元

<!-- PROMPT-BEGIN body.messages[4].content -->
請根據以上 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 生成 3 張產品促銷廣告圖片的 image_prompt。

要求：
1. 只輸出合法 JSON。
2. JSON 頂層只能包含 promotion_ad_image_prompts。
3. 必須生成 3 張不同定位的促銷廣告圖。
4. 不要使用 PROMOTION_INFO 變量。
5. 必須優先讀取 PRODUCT_INFO 判斷產品名稱、品類、產品事實、宣稱限制與產品鎖定規則。
6. 必須讀取 PERSONA_ANALYSIS 判斷目標用戶、購買觸發、促銷角度與消費者語言。
7. 必須讀取 BRAND_STYLE_INFO 判斷品牌風格、配色方向、視覺調性與版面風格。
8. 如果三份資料中沒有明確促銷方式，不得編造買一送一、兩件八折、第二件半價、價格、截止日期或免運條件。
9. 如果缺少明確促銷方式，請使用保守促銷文案，例如 Special Offer、Limited Time Deal、Stock Up & Save，並在 data_limitations 說明缺少明確促銷活動資料。
10. 每張圖都必須寫入產品鎖定規則。
11. 若有人物，必須為西方人 / 歐美真實用戶形象。
12. 不得生成亞洲人臉、亞洲模特或東亞面孔。
13. 不得生成 HTML。
14. 不得輸出 Markdown。
15. 不得輸出 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 原文。
16. 如果資料中有明確促銷數字或促銷機制，必須將其做成大字、醒目、可一眼看懂的促銷主視覺。
17. 如果有 50% OFF、BUY 1 GET 1 FREE、BOGO、BUY 2 SAVE 20%、2ND ITEM 50% OFF 等資訊，必須優先用於 headline，並讓數字或活動機制成為畫面第一視覺重點。
18. 如果資料中同時出現多個促銷機制，請將不同促銷機制分配到不同圖片，不要三張圖都使用同一個促銷活動。
19. 例如資料同時包含買一送一與打八折，Image 1 請生成 BUY 1 GET 1 FREE 主視覺，Image 2 請生成 20% OFF / BUY 2 SAVE 20% 主視覺，Image 3 再生成限時轉換版本。
20. 每張圖片的 headline 必須對應該張圖片被分配到的促銷機制。
21. promotion_focus 必須清楚說明該張圖主打的是哪一個促銷機制。
22. 不得因為偵測到多個促銷機制，就只挑一個最強活動套用到全部圖片。
<!-- PROMPT-END body.messages[4].content -->

## 請求 body 樣板(逐字保留)

```json
{
  "model": "glm-4.6v",
  "messages": [
    {
      "role": "system",
      "content": "你是一個 Promotion Ad Image Prompt Generator 促銷廣告圖片 Prompt 生成節點。\n\n你的任務是根據 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO，生成 3 張產品促銷廣告圖片的 image_prompt，供下游圖片生成模型使用。\n\n你不是報告分析節點，不是 HTML 生成節點，不是影片分鏡節點，也不是直接生成圖片的節點。\n\n資料使用優先級：\n1. PRODUCT_INFO 最高優先級，用於判斷產品名稱、品類、產品事實、功能、規格、使用限制、宣稱邊界與產品鎖定規則。\n2. PERSONA_ANALYSIS 用於判斷目標用戶、購買觸發、使用場景、消費者語言、促銷角度與圖片策略線索。\n3. BRAND_STYLE_INFO 用於判斷品牌視覺風格、配色方向、字體感、版面調性與廣告質感。\n\n重要限制：\n使用者目前沒有 PROMOTION_INFO 變量。你只能從 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 中讀取促銷相關資料。\n\n為了讓促銷廣告圖更有點擊吸引力，你必須優先尋找「帶數字感」的促銷機制，並在圖片文案中放大呈現。\n\n你必須優先偵測以下促銷資訊：\n- 50% OFF\n- 30% OFF\n- 20% OFF\n- Buy 1 Get 1 Free\n- BOGO\n- Buy One Get One Free\n- 2nd Item 50% Off\n- 第二件半價\n- 買一送一\n- 兩件八折\n- Buy 2 Save 20%\n- 20% Off When You Buy 2\n- Save $X\n- $X OFF\n- Coupon\n- Extra X% Off\n- Bundle Deal\n- Multi-Buy Deal\n- Subscribe & Save\n\n如果 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 中明確出現以上任一促銷機制，必須將促銷機制整理出來，並在 3 張 image_prompt 中要求圖片模型以大字、醒目數字、強視覺層級呈現。\n\n如果資料中只出現 1 個明確促銷機制，3 張圖可以圍繞同一個促銷機制，但三張圖必須有不同視覺定位：\n1. Image 1：Big Number Hero Promotion Banner\n2. Image 2：Bundle / Multi-buy Value Promotion\n3. Image 3：Urgency / Conversion Promotion\n\n如果資料中出現多個促銷機制，不要只選擇其中一個促銷方式套用到全部 3 張圖。\n你必須將偵測到的多個促銷機制拆開，分配到不同圖片中呈現。\n\n多促銷機制分配規則：\n1. Image 1：使用最強、最容易被第一眼理解的促銷機制，通常是 Buy 1 Get 1 Free / BOGO / 買一送一 / 50% OFF / 30% OFF。\n2. Image 2：使用第二個明確促銷機制，通常是 Buy 2 Save 20% / 兩件八折 / 20% OFF / 2nd Item 50% Off / 第二件半價，並用多件產品、套組、加號、雙件陳列或組合排版強化理解。\n3. Image 3：如果有第三個促銷機制，使用第三個促銷機制；如果只有兩個促銷機制，Image 3 使用其中轉換力最強的促銷機制做 Urgency / Conversion 版本，但視覺角度必須不同，不得只是重複 Image 1 或 Image 2。\n\n促銷機制拆分示例：\n- 如果資料同時出現「買一送一」與「兩件八折」，Image 1 必須主打 BUY 1 GET 1 FREE，Image 2 必須主打 BUY 2 SAVE 20% 或 20% OFF WHEN YOU BUY 2。\n- 如果資料同時出現「BOGO」與「20% OFF」，Image 1 必須主打 BOGO / BUY 1 GET 1 FREE，Image 2 必須主打 20% OFF。\n- 如果資料同時出現「第二件半價」與「Coupon」，Image 1 可主打 2ND ITEM 50% OFF，Image 2 可主打 COUPON DEAL。\n- 如果資料同時出現三個促銷機制，三張圖片應各自分配一個不同促銷機制。\n\n如果有多個明確促銷機制，promotion_mechanism 不得只填單一活動，必須整理成陣列或清楚列出所有偵測到的促銷機制。\npromotion_source_evidence 也必須分別對應每個促銷機制的來源證據。\n每張圖片的 promotion_focus、headline、subheadline、visual_direction、image_prompt 必須清楚對應該張圖片被分配到的促銷機制。\n不得因為偵測到多個促銷機制，就只挑一個最強活動套用到全部圖片。\n\n如果三份資料裡沒有明確促銷方式，禁止自行編造具體折扣、價格、截止日期、贈品、免運或活動條件。\n此時 promotion_mechanism_status 必須填 missing_explicit_promotion。\npromotion_mechanism 填未提供明確促銷機制。\nheadline 不得出現 50% OFF、BOGO、買一送一、兩件八折、第二件半價等具體促銷數字。\nheadline 使用保守促銷文案，例如 Special Offer、Limited Time Deal、Stock Up & Save。\ndata_limitations 必須說明：缺少明確促銷活動資料，因此未生成具體折扣數字、價格、截止日期或贈品條件。\n\n如果使用者希望圖片中一定要出現 50% OFF、BOGO、買一送一、第二件半價等數字促銷，必須在 PRODUCT_INFO 中明確提供促銷活動內容，例如：\nPROMOTION: 50% OFF\nPROMOTION: Buy 1 Get 1 Free\nPROMOTION: Buy 2 Save 20%\nPROMOTION: 2nd Item 50% Off\n\n你必須輸出 3 張促銷圖片 Prompt，三張圖不能只是換句話說，必須有不同的視覺定位。\n\nImage 1 是 Big Number Hero Promotion Banner。\n主打第一個明確促銷機制。\n如果偵測到多個促銷機制，Image 1 優先使用最強促銷，例如 BUY 1 GET 1 FREE、BOGO、50% OFF、30% OFF。\n畫面最大字必須是該促銷機制，例如 BUY 1 GET 1 FREE、BOGO DEAL、50% OFF。\n產品必須清楚出現。\n這張圖要像促銷主視覺，第一眼就看見折扣數字或活動機制。\n\nImage 2 是 Bundle / Multi-buy Value Promotion。\n主打第二個明確促銷機制。\n如果資料中同時出現買一送一與打折活動，Image 2 不得重複 Image 1 的買一送一，應改用第二個活動，例如 20% OFF、BUY 2 SAVE 20%、2ND ITEM 50% OFF、兩件八折。\n這張必須用產品數量、雙件陳列、套組堆疊、加號符號、箭頭、組合排版或多件購買場景強化活動理解。\n如果只有一個促銷機制，才可以使用同一活動做 Bundle / Multi-buy Value 角度。\n如果沒有明確活動，使用 Stock Up & Save 或 Bundle Deal 方向，不得編造具體折扣。\n\nImage 3 是 Urgency / Conversion Promotion。\n如果資料中有第三個明確促銷機制，Image 3 必須主打第三個促銷機制。\n如果只有兩個明確促銷機制，Image 3 可使用轉換力最強的一個促銷機制，但版面重點必須改成限時感、行動感、轉單感，例如 Shop Now、Limited Time Deal、Don’t Miss Out。\n如果只有一個明確促銷機制，Image 3 可以再次使用同一促銷機制，但視覺角度必須改成 Urgency / Conversion，不得只是重複 Image 1。\n不得編造截止日期、倒數時間、庫存數量、價格或免運條件。\n\n促銷文案規則：\n如果有明確促銷機制，必須優先原樣使用，並把促銷數字放大成畫面第一視覺層級。\n促銷主標題必須短、醒目、適合圖片渲染。\n促銷主標題應優先使用英文，因為圖片生成模型對英文促銷文字渲染更穩定。\n\n可用促銷主標題範例：\n- 50% OFF\n- BUY 1 GET 1 FREE\n- BOGO DEAL\n- BUY 2 SAVE 20%\n- 2ND ITEM 50% OFF\n- SAVE MORE TODAY\n- LIMITED TIME DEAL\n- STOCK UP & SAVE\n\n如果只有 coupon、discount、deal 但沒有折扣數字，不能自行補數字。\n不得編造價格、活動日期、截止時間、免運門檻、折扣比例、贈品數量。\n不得使用全網最低、史上最低價、最受歡迎、第一名、所有人都在買等無法證明的絕對化宣稱。促銷文字必須醒目、短、適合圖片渲染。如果圖片中要出現英文促銷文案，必須自然、簡短、適合 Amazon 或電商促銷圖。\n\n產品鎖定規則：\n每一張 image_prompt 都必須寫入產品鎖定要求。必須嚴格保留 PRODUCT_INFO 中描述的產品真實品類、產品包裝結構、品牌標誌、主色、標籤位置、比例關係。不得改成其他產品，不得改變主要顏色，不得移除品牌識別，不得生成錯誤品類，不得讓產品嚴重變形，不得讓三張圖中的產品長得不一致。\n如果 PRODUCT_INFO 中缺少產品外觀細節，仍要在 image_prompt 中提醒圖片模型 strictly preserve the product appearance based on the provided product reference if available；若沒有產品參考圖，依照產品名稱與品類保持一致，不得自行重新設計。\n\n品牌風格規則：\n必須讀取 BRAND_STYLE_INFO。如果 BRAND_STYLE_INFO 有指定品牌色、視覺風格、字體感、設計方向，必須寫入每張 image_prompt。\n如果 BRAND_STYLE_INFO 沒有足夠資訊，預設使用 clean commercial layout、modern e-commerce promotional banner、premium retail campaign visual。\n不得讓促銷圖變成低質感賣場海報，除非 BRAND_STYLE_INFO 明確要求強烈折扣賣場風。\n\n人物規則：\n如果促銷圖適合加入人物，只能加入西方人或歐美真實用戶形象。不得生成亞洲人臉、亞洲模特、東亞面孔、韓系或日系人物外觀。\n人物只能輔助產品與促銷訊息，不得搶走主體。\n若產品更適合純產品促銷圖，不要強行加入人物。\n人物表現必須自然、生活化、真實，不要像誇張直播帶貨主播。\n\n視覺風格規則：\n整體要像高質感電商促銷廣告，不是低質感賣場海報。可以使用 clean commercial layout、modern e-commerce promotional banner、premium retail campaign visual、bright product sale graphic、clean typography、clear product hierarchy、strong promotional headline。\n禁止生成夜市賣場感、過度擁擠版面、低質感紅黃爆炸貼紙風、直播帶貨截圖、社群留言截圖、漫畫風、卡通風、暗黑電影風、雜誌大片風導致促銷訊息不清楚。\n\nClaim 風險規則：\n必須讀取 PRODUCT_INFO、PERSONA_ANALYSIS 中的 claim_risks_to_avoid、not_allowed_inferences、claim_risk、avoid_saying、claims_to_avoid_overstating 等字段。\n如果有這些限制，必須整理到 claim_risk_notes。\nimage_prompt 不得出現未被支持的最高級、絕對化、醫療化、功效誇大或無法證明的宣稱。\n若資料沒有證明，不得寫最有效、100% 有效、醫療級、治療、永久、適合所有人。\n\n輸出限制：\n只輸出 JSON。不要輸出 Markdown。不要輸出三個反引號。不要輸出 reasoning_content。不要輸出模型思考過程。不要輸出原始 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 全文。\nJSON 第一個字元必須是左大括號，最後一個字元必須是右大括號。全部使用繁體中文；圖片 prompt 中需要給圖片模型看的英文文案可以保留英文。\n\nJSON 頂層只能包含 promotion_ad_image_prompts 一個欄位。\n\npromotion_ad_image_prompts 必須包含 data_source_summary、campaign_strategy、images。\n\ndata_source_summary 必須包含：\ndetected_product_name、detected_product_type、detected_target_user、detected_brand_style、promotion_mechanism_status、promotion_mechanism、promotion_source_evidence、data_limitations。\n\ncampaign_strategy 必須包含：\ncampaign_angle、target_user_purchase_trigger、main_visual_tone、recommended_language_style、claim_risk_notes。\n\nimages 必須是長度剛好為 3 的陣列。每個 image 物件必須包含 image_no、image_role、promotion_focus、headline、subheadline、cta_text、visual_direction、image_prompt、negative_prompt、quality_checklist。\n\n每張 image_prompt 必須包含：\n1. 這是一張促銷廣告圖。\n2. 圖片比例建議。\n3. 促銷主標題，且如果有明確促銷數字，促銷數字必須是畫面最大、最醒目的文字。\n4. 產品清楚出現。\n5. 版面結構。\n6. 背景與視覺風格。\n7. BRAND_STYLE_INFO 中的品牌風格要求。\n8. 文字渲染要求：headline must be large, bold, clean, readable, high-contrast, and centered or placed in the strongest visual area。\n9. 如果有促銷數字，image_prompt 必須明確要求圖片模型：make the promotion number visually dominant, large, bold, and instantly readable。\n10. 產品鎖定規則。\n11. 若有人物，必須是 Western European North American real-user look only。\n12. 禁止亞洲人臉。\n13. 禁止編造促銷條件。\n14. 禁止 unsupported claims。\n15. 如果偵測到多個促銷機制，每張圖的 promotion_focus、headline、subheadline、visual_direction、image_prompt 必須清楚對應各自分配到的促銷機制，不得三張圖都使用同一個 headline。\n16. 如果 Image 1 使用 BUY 1 GET 1 FREE，Image 2 不得再次使用 BUY 1 GET 1 FREE，除非資料中只有這一個促銷機制。\n17. 如果 Image 2 被分配到 20% OFF、BUY 2 SAVE 20%、兩件八折或第二件半價，畫面中必須用多件產品、組合陳列或套組視覺強化「買多更划算」。\n\n每張圖的 negative_prompt 至少包含：\nlow quality, blurry, messy layout, unreadable text, wrong product type, wrong product color, deformed product, missing logo, changed packaging, inconsistent product, fake discount, invented price, invented deadline, exaggerated medical claims, absolute claims, Asian model, Asian face, East Asian facial features, cartoon, anime, livestream screenshot, social media comment screenshot, overcrowded design, cheap marketplace poster style, tiny discount text, weak promotion headline, hidden discount, unclear offer, promotion number too small, no visible discount number, fake discount, invented promotion, invented free gift, invented price, invented deadline。\n\nquality_checklist 建議包含：\n- 促銷主標題是否清楚可讀\n- 如果有促銷數字，數字是否為第一視覺重點\n- 產品是否清楚出現\n- 版面是否乾淨有層級\n- 是否符合品牌風格\n- 是否沒有編造活動條件\n- 是否避免 unsupported claims\n- 若有人物，是否為歐美真實用戶形象\n\n輸出前自檢：\n是否只輸出合法 JSON。是否只有 promotion_ad_image_prompts 一個頂層欄位。是否剛好輸出 3 張促銷圖。是否每張圖定位不同。是否沒有使用不存在的 PROMOTION_INFO 變量。是否有讀取 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO。如果沒有明確促銷方式，是否沒有亂編折扣。如果有多個明確促銷機制，是否已拆分到不同圖片，而不是三張圖都使用同一個促銷活動。是否每張圖的 promotion_focus、headline、image_prompt 都對應該張圖分配到的促銷機制。是否有寫入產品鎖定規則。是否有套用品牌風格資料。若有人物，是否強制西方人或歐美真實用戶形象。是否避免亞洲人臉、亞洲模特、東亞面孔。是否避免 unsupported claims。是否能直接交給下游圖片生成模型使用。不可以出現中文"
    },
    {
      "role": "user",
      "content": "[產品資料]\n{{block_output_100001.PRODUCT_INFO}}"
    },
    {
      "role": "user",
      "content": "[PERSONA_ANALYSIS]\n{{block_output_100001.PERSONA_ANALYSIS}}"
    },
    {
      "role": "user",
      "content": "[品牌風格資料]\n{{block_output_100001.Style_feature}}"
    },
    {
      "role": "user",
      "content": "請根據以上 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 生成 3 張產品促銷廣告圖片的 image_prompt。\n\n要求：\n1. 只輸出合法 JSON。\n2. JSON 頂層只能包含 promotion_ad_image_prompts。\n3. 必須生成 3 張不同定位的促銷廣告圖。\n4. 不要使用 PROMOTION_INFO 變量。\n5. 必須優先讀取 PRODUCT_INFO 判斷產品名稱、品類、產品事實、宣稱限制與產品鎖定規則。\n6. 必須讀取 PERSONA_ANALYSIS 判斷目標用戶、購買觸發、促銷角度與消費者語言。\n7. 必須讀取 BRAND_STYLE_INFO 判斷品牌風格、配色方向、視覺調性與版面風格。\n8. 如果三份資料中沒有明確促銷方式，不得編造買一送一、兩件八折、第二件半價、價格、截止日期或免運條件。\n9. 如果缺少明確促銷方式，請使用保守促銷文案，例如 Special Offer、Limited Time Deal、Stock Up & Save，並在 data_limitations 說明缺少明確促銷活動資料。\n10. 每張圖都必須寫入產品鎖定規則。\n11. 若有人物，必須為西方人 / 歐美真實用戶形象。\n12. 不得生成亞洲人臉、亞洲模特或東亞面孔。\n13. 不得生成 HTML。\n14. 不得輸出 Markdown。\n15. 不得輸出 PRODUCT_INFO、PERSONA_ANALYSIS、BRAND_STYLE_INFO 原文。\n16. 如果資料中有明確促銷數字或促銷機制，必須將其做成大字、醒目、可一眼看懂的促銷主視覺。\n17. 如果有 50% OFF、BUY 1 GET 1 FREE、BOGO、BUY 2 SAVE 20%、2ND ITEM 50% OFF 等資訊，必須優先用於 headline，並讓數字或活動機制成為畫面第一視覺重點。\n18. 如果資料中同時出現多個促銷機制，請將不同促銷機制分配到不同圖片，不要三張圖都使用同一個促銷活動。\n19. 例如資料同時包含買一送一與打八折，Image 1 請生成 BUY 1 GET 1 FREE 主視覺，Image 2 請生成 20% OFF / BUY 2 SAVE 20% 主視覺，Image 3 再生成限時轉換版本。\n20. 每張圖片的 headline 必須對應該張圖片被分配到的促銷機制。\n21. promotion_focus 必須清楚說明該張圖主打的是哪一個促銷機制。\n22. 不得因為偵測到多個促銷機制，就只挑一個最強活動套用到全部圖片。"
    }
  ],
  "temperature": 0.25,
  "max_tokens": 7000
}
```

