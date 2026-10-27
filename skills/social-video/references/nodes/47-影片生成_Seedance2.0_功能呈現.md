# 47. 影片生成_Seedance2.0_功能呈現(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `1453736` |
| 型別 | `http` |
| 拓樸序 | 47 |
| DAG 層深 | 9 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`1717375` 參考圖轉url_3
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

- 本節點引用的上游變數:`{{block_output_100001.PRODUCT_INFO}}`, `{{block_output_121547.output}}`, `{{block_output_1717375.images_url}}`, `{{block_output_1807253.data.url}}`, `{{block_output_1998343.data.url}}`

## 提示詞原文(逐字保留,不得修改)

### `body.prompt`

- SHA-256:`7cefc0f43466703dbfd1aa440bcd290a79e0e71698bde8f52571872f41369a5f`
- 長度:4507 字元

<!-- PROMPT-BEGIN body.prompt -->
生成一支 15 秒、9:16、TikTok 產品破圈短影音。

影片類型是 TikTok product breakout video、effect-demonstration ad、visual hook product ad。不是 premium branding commercial，不是 UGC，不要真人口播，不要手持開箱感，不要生活隨拍感，不要 vlog 感，不要像 Amazon Listing 說明片。

這支影片的核心任務是：用第一秒奇特、有反差、有視覺衝擊的 Hook 吸引 TikTok 觀眾停下來，接著自然置入產品，放大產品的核心賣點，讓觀眾快速理解產品為什麼值得注意。

請使用上傳的 TikTok 影片分鏡圖作為影片鏡頭方向參考：{{block_output_1998343.data.url}}。分鏡圖只負責影片的故事節奏、鏡頭方向、第一秒 Hook、產品出場位置、畫面構圖、視覺對比、情緒張力與賣點呈現方向。不要把分鏡圖本身直接放進影片裡。

請使用上傳的原產品圖作為產品外觀主參考：{{block_output_1807253.data.url}}。原產品圖是產品外觀最高優先級參考，負責鎖定產品的真實類型、整體外觀、數量、款式、排列關係、比例、形狀、顏色系統、產品家族一致性與整體視覺辨識。不要把原產品圖本身直接放進影片裡。

請使用上傳的產品細節結構圖作為產品外觀細節鎖定參考：{{block_output_1807253.data.url}}。產品細節結構圖只負責補充鎖定目標產品外觀細節，包括產品類型、形狀、輪廓、比例、厚度、材質、表面質感、顏色配置、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、變體差異與產品結構。不要把產品細節結構圖本身直接放進影片裡。

產品資訊：{{block_output_100001.PRODUCT_INFO}}

TikTok 影片腳本與分鏡策略：{{block_output_121547.output}}

TikTok 影片分鏡圖：
{{block_output_1998343.data.url}}

原產品圖：
{{block_output_1717375.images_url}}

產品細節結構圖：
{{block_output_1807253.data.url}}

產品外觀準確度是最高優先級。優先級順序為：第一，原產品圖；第二，產品細節結構圖；第三，產品資訊；第四，TikTok 分鏡圖與腳本。如果 TikTok 分鏡圖、影片腳本、原產品圖、產品細節結構圖和產品資訊發生衝突，請優先保留原產品圖與產品細節結構圖中的產品外觀。不要為了畫面更吸睛而改變產品外觀。不要把產品改成更常見、更漂亮、更像其他商品的替代品。

所有上傳圖片都只是 reference。不要直接顯示 storyboard image、original product image、product detail board、product layout board、catalog sheet、grid layout、collage、poster、keyframe sheet、frame sheet 或 static graphic board。請把參考圖片轉譯成真實的 TikTok-style cinematic moving footage。

影片第 0–2 秒必須是強 Hook。第一幀就要有奇特、反常識、荒謬、強對比、視覺衝擊或情緒衝突的動態畫面。不要用產品靜態展示開場，不要用品牌 Logo 開場，不要用普通車內慢鏡頭開場，不要用普通開箱開場，不要用產品展示板開場，不要用分鏡圖開場。第一秒必須讓觀眾覺得：這是什麼、為什麼會這樣、這畫面好怪但我想繼續看。

請嚴格根據 TikTok 影片腳本與分鏡策略執行每一個時間段。影片節奏必須清楚：第一秒奇特 Hook → 問題或反差放大 → 產品自然出場 → 主攻賣點視覺化 → 輔助賣點補充 → CTA 收尾。

0–2 秒：生成奇特 Hook。畫面必須有強烈吸睛點、荒謬感、嫌棄感、視覺反差或 AI 奇觀。這一段不是產品普通展示，而是讓觀眾停下來。

2–4 秒：放大問題或反差。讓觀眾理解開頭的奇特畫面和產品痛點有關。畫面要快速、直接，不要長鋪陳。

4–6 秒：產品第一次自然出場。產品必須作為前面問題的解法出現，不要硬塞。產品要清楚、穩定、可辨識。

6–10 秒：主攻賣點視覺化。用畫面呈現核心賣點，而不是只靠文字說明。如果主賣點是外觀質感，請用廉價 vs 低調、突兀 vs 協調的對比呈現。如果主賣點是多選擇，請用混亂選擇 vs 一組清楚展開呈現。如果主賣點是使用方便，請用麻煩流程 vs 簡單動作呈現。

10–13 秒：輔助賣點補充。最多補充 1–2 個輔助賣點，不要塞太多資訊。畫面要清楚，節奏要快。

13–15 秒：TikTok CTA 收尾。收尾要有產品記憶點和簡短行動提示，例如 Upgrade your drive、Try the 5 scent pack、Shop now、Start with five。不要只放 Logo。

畫面風格：TikTok-style、fast-paced、visually striking、high-contrast、clean product ad、cinematic but not slow、sharp visual storytelling。畫面可以有 AI 奇觀、荒謬設定、強對比、掃描標記、警告感、審判感、抓包感、Before/After 轉換，但必須服務產品賣點，不能只是怪。

字幕必須短、直白、有 TikTok 感。字幕只負責點出問題、補充判斷、強化反差與 CTA。不要使用長文案，不要使用正式品牌廣告語，不要使用大段說明。每句英文字幕不超過 12 個單字。字幕可以是：This looks wrong. / Your car deserves better. / Meet SPACION. / Matte black. Clean look. / 5 scents. One pack. / Open. Hang. Done. / Upgrade your drive.

請使用原產品圖、產品資訊與產品細節結構圖作為目標產品外觀的唯一依據。必須保留產品的真實商品類型、產品數量、款式數量、形狀、輪廓、尺寸、比例、厚度、材質、表面質感、紋理、顏色、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、包裝狀態與使用方式。不要重新設計產品，不要改變產品類別，不要用相似商品替代目標產品，不要新增產品資訊中沒有出現的功能、零件、配件、包裝、材質、結構或使用方式，不要刪除產品原本存在的重要特徵。產品在整支影片中必須保持一致，不得出現 shot-to-shot product drift。

如果產品有多個款式，每個款式必須保持獨立。不得混用不同款式的顏色、文字、名稱、logo、圖案、字體或版面。總覽鏡頭可以展示多個款式。細節特寫鏡頭只使用單一 selected product unit 或 selected variant，避免多款產品細節混亂。

產品上的所有文字、logo、icon、標籤、slogan、香型名稱、型號、符號與印刷圖案，都必須視為鎖定的 raster artwork，不是可編輯文字。不要重寫產品文字，不要翻譯產品文字，不要替換產品文字，不要改變字體，不要改變文字大小，不要改變文字顏色，不要改變文字位置，不要新增假文字，不要產生亂碼。如果小字在動態影片中無法完全清楚，請保持原本文字區塊的位置、排列和視覺結構，讓它自然地微模糊或動態模糊，不要生成新的錯誤文字。

如果產品資訊顯示沒有包裝，或沒有明確要求展示包裝，影片中不得出現任何包裝。不要出現 box、tray、sleeve、pouch、bag、plastic wrap、retail package、shipping carton、package label、package sticker、package seal、package logo、package text、package graphics。

功效呈現必須安全。可以呈現使用前後的視覺差異、質感差異、選擇差異、使用流程差異，但不得暗示未被證明的效果。不要出現細菌消失、臭氣雲瞬間消失、空氣被科學淨化、髒污被清除、永久效果、100% 效果、醫療效果、抗菌效果、除菌效果。不可視化的功效只能用情境、氛圍、象徵畫面與短字幕輔助，不要拍成實驗證明。

如果本產品是車用香氛吊卡，請特別注意：它是 hanging scent card，不是 spray bottle、perfume bottle、electronic diffuser、cleaning cloth、liquid fragrance bottle、plastic thick tag、car ornament 或電子設備。使用方式是取出並吊掛，不是噴灑、擦拭、插電、倒液體或貼在表面。

負面提示詞：不要重新設計產品。不要讓產品變形。不要改變產品類別。不要用相似商品替代目標產品。不要改變產品形狀。不要改變產品輪廓。不要改變產品比例。不要改變產品尺寸。不要讓產品變厚。不要使用錯誤材質。不要改變表面質感。不要顏色漂移。不要 logo 漂移。不要文字漂移。不要圖案漂移。不要比例漂移。不要包裝漂移。不要類別漂移。不要款式混用。不要交換顏色。不要交換 slogan。不要交換名稱。不要出現假文字。不要出現亂碼。不要新增 logo。不要新增配件。不要新增包裝。不要新增按鈕。不要新增螢幕。不要新增燈光零件。不要新增夾具。不要新增蓋子。不要新增手柄。不要新增標籤。不要新增瓶子。不要新增盒子。不要新增電子零件，除非產品資訊明確說明。不要移除產品現有特徵。不要拉伸。不要扭曲。不要彎折。不要摺疊。不要融化。不要旋轉到比例錯誤。不要膨脹。不要縮小成錯誤尺度。不要裁掉重要產品細節。不要重複生成不必要產品。不要讓產品模糊。不要簡化產品圖案。不要鏡頭之間產品外觀漂移。不要顯示 storyboard sheet。不要顯示 original product image。不要顯示 product detail board。不要顯示 catalog board。不要顯示 grid panel。不要顯示 collage。不要顯示 poster layout。不要顯示 static keyframe。不要 UGC。不要真人口播。不要手持開箱。不要 casual vlog。不要普通商品展示片。不要慢節奏品牌形象片。不要細菌消失。不要臭氣雲瞬間消失。不要科學淨化效果。不要清潔效果。不要醫療效果。不要 100% 效果。不要永久效果。不要假評論。不要假測試結果。不要把不可視化功效拍成直接證明。
<!-- PROMPT-END body.prompt -->

## 請求 body 樣板(逐字保留)

```json
{
  "model": "doubao-seedance-2.0-fast",
  "prompt": "生成一支 15 秒、9:16、TikTok 產品破圈短影音。\n\n影片類型是 TikTok product breakout video、effect-demonstration ad、visual hook product ad。不是 premium branding commercial，不是 UGC，不要真人口播，不要手持開箱感，不要生活隨拍感，不要 vlog 感，不要像 Amazon Listing 說明片。\n\n這支影片的核心任務是：用第一秒奇特、有反差、有視覺衝擊的 Hook 吸引 TikTok 觀眾停下來，接著自然置入產品，放大產品的核心賣點，讓觀眾快速理解產品為什麼值得注意。\n\n請使用上傳的 TikTok 影片分鏡圖作為影片鏡頭方向參考：{{block_output_1998343.data.url}}。分鏡圖只負責影片的故事節奏、鏡頭方向、第一秒 Hook、產品出場位置、畫面構圖、視覺對比、情緒張力與賣點呈現方向。不要把分鏡圖本身直接放進影片裡。\n\n請使用上傳的原產品圖作為產品外觀主參考：{{block_output_1807253.data.url}}。原產品圖是產品外觀最高優先級參考，負責鎖定產品的真實類型、整體外觀、數量、款式、排列關係、比例、形狀、顏色系統、產品家族一致性與整體視覺辨識。不要把原產品圖本身直接放進影片裡。\n\n請使用上傳的產品細節結構圖作為產品外觀細節鎖定參考：{{block_output_1807253.data.url}}。產品細節結構圖只負責補充鎖定目標產品外觀細節，包括產品類型、形狀、輪廓、比例、厚度、材質、表面質感、顏色配置、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、變體差異與產品結構。不要把產品細節結構圖本身直接放進影片裡。\n\n產品資訊：{{block_output_100001.PRODUCT_INFO}}\n\nTikTok 影片腳本與分鏡策略：{{block_output_121547.output}}\n\nTikTok 影片分鏡圖：\n{{block_output_1998343.data.url}}\n\n原產品圖：\n{{block_output_1717375.images_url}}\n\n產品細節結構圖：\n{{block_output_1807253.data.url}}\n\n產品外觀準確度是最高優先級。優先級順序為：第一，原產品圖；第二，產品細節結構圖；第三，產品資訊；第四，TikTok 分鏡圖與腳本。如果 TikTok 分鏡圖、影片腳本、原產品圖、產品細節結構圖和產品資訊發生衝突，請優先保留原產品圖與產品細節結構圖中的產品外觀。不要為了畫面更吸睛而改變產品外觀。不要把產品改成更常見、更漂亮、更像其他商品的替代品。\n\n所有上傳圖片都只是 reference。不要直接顯示 storyboard image、original product image、product detail board、product layout board、catalog sheet、grid layout、collage、poster、keyframe sheet、frame sheet 或 static graphic board。請把參考圖片轉譯成真實的 TikTok-style cinematic moving footage。\n\n影片第 0–2 秒必須是強 Hook。第一幀就要有奇特、反常識、荒謬、強對比、視覺衝擊或情緒衝突的動態畫面。不要用產品靜態展示開場，不要用品牌 Logo 開場，不要用普通車內慢鏡頭開場，不要用普通開箱開場，不要用產品展示板開場，不要用分鏡圖開場。第一秒必須讓觀眾覺得：這是什麼、為什麼會這樣、這畫面好怪但我想繼續看。\n\n請嚴格根據 TikTok 影片腳本與分鏡策略執行每一個時間段。影片節奏必須清楚：第一秒奇特 Hook → 問題或反差放大 → 產品自然出場 → 主攻賣點視覺化 → 輔助賣點補充 → CTA 收尾。\n\n0–2 秒：生成奇特 Hook。畫面必須有強烈吸睛點、荒謬感、嫌棄感、視覺反差或 AI 奇觀。這一段不是產品普通展示，而是讓觀眾停下來。\n\n2–4 秒：放大問題或反差。讓觀眾理解開頭的奇特畫面和產品痛點有關。畫面要快速、直接，不要長鋪陳。\n\n4–6 秒：產品第一次自然出場。產品必須作為前面問題的解法出現，不要硬塞。產品要清楚、穩定、可辨識。\n\n6–10 秒：主攻賣點視覺化。用畫面呈現核心賣點，而不是只靠文字說明。如果主賣點是外觀質感，請用廉價 vs 低調、突兀 vs 協調的對比呈現。如果主賣點是多選擇，請用混亂選擇 vs 一組清楚展開呈現。如果主賣點是使用方便，請用麻煩流程 vs 簡單動作呈現。\n\n10–13 秒：輔助賣點補充。最多補充 1–2 個輔助賣點，不要塞太多資訊。畫面要清楚，節奏要快。\n\n13–15 秒：TikTok CTA 收尾。收尾要有產品記憶點和簡短行動提示，例如 Upgrade your drive、Try the 5 scent pack、Shop now、Start with five。不要只放 Logo。\n\n畫面風格：TikTok-style、fast-paced、visually striking、high-contrast、clean product ad、cinematic but not slow、sharp visual storytelling。畫面可以有 AI 奇觀、荒謬設定、強對比、掃描標記、警告感、審判感、抓包感、Before/After 轉換，但必須服務產品賣點，不能只是怪。\n\n字幕必須短、直白、有 TikTok 感。字幕只負責點出問題、補充判斷、強化反差與 CTA。不要使用長文案，不要使用正式品牌廣告語，不要使用大段說明。每句英文字幕不超過 12 個單字。字幕可以是：This looks wrong. / Your car deserves better. / Meet SPACION. / Matte black. Clean look. / 5 scents. One pack. / Open. Hang. Done. / Upgrade your drive.\n\n請使用原產品圖、產品資訊與產品細節結構圖作為目標產品外觀的唯一依據。必須保留產品的真實商品類型、產品數量、款式數量、形狀、輪廓、尺寸、比例、厚度、材質、表面質感、紋理、顏色、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、包裝狀態與使用方式。不要重新設計產品，不要改變產品類別，不要用相似商品替代目標產品，不要新增產品資訊中沒有出現的功能、零件、配件、包裝、材質、結構或使用方式，不要刪除產品原本存在的重要特徵。產品在整支影片中必須保持一致，不得出現 shot-to-shot product drift。\n\n如果產品有多個款式，每個款式必須保持獨立。不得混用不同款式的顏色、文字、名稱、logo、圖案、字體或版面。總覽鏡頭可以展示多個款式。細節特寫鏡頭只使用單一 selected product unit 或 selected variant，避免多款產品細節混亂。\n\n產品上的所有文字、logo、icon、標籤、slogan、香型名稱、型號、符號與印刷圖案，都必須視為鎖定的 raster artwork，不是可編輯文字。不要重寫產品文字，不要翻譯產品文字，不要替換產品文字，不要改變字體，不要改變文字大小，不要改變文字顏色，不要改變文字位置，不要新增假文字，不要產生亂碼。如果小字在動態影片中無法完全清楚，請保持原本文字區塊的位置、排列和視覺結構，讓它自然地微模糊或動態模糊，不要生成新的錯誤文字。\n\n如果產品資訊顯示沒有包裝，或沒有明確要求展示包裝，影片中不得出現任何包裝。不要出現 box、tray、sleeve、pouch、bag、plastic wrap、retail package、shipping carton、package label、package sticker、package seal、package logo、package text、package graphics。\n\n功效呈現必須安全。可以呈現使用前後的視覺差異、質感差異、選擇差異、使用流程差異，但不得暗示未被證明的效果。不要出現細菌消失、臭氣雲瞬間消失、空氣被科學淨化、髒污被清除、永久效果、100% 效果、醫療效果、抗菌效果、除菌效果。不可視化的功效只能用情境、氛圍、象徵畫面與短字幕輔助，不要拍成實驗證明。\n\n如果本產品是車用香氛吊卡，請特別注意：它是 hanging scent card，不是 spray bottle、perfume bottle、electronic diffuser、cleaning cloth、liquid fragrance bottle、plastic thick tag、car ornament 或電子設備。使用方式是取出並吊掛，不是噴灑、擦拭、插電、倒液體或貼在表面。\n\n負面提示詞：不要重新設計產品。不要讓產品變形。不要改變產品類別。不要用相似商品替代目標產品。不要改變產品形狀。不要改變產品輪廓。不要改變產品比例。不要改變產品尺寸。不要讓產品變厚。不要使用錯誤材質。不要改變表面質感。不要顏色漂移。不要 logo 漂移。不要文字漂移。不要圖案漂移。不要比例漂移。不要包裝漂移。不要類別漂移。不要款式混用。不要交換顏色。不要交換 slogan。不要交換名稱。不要出現假文字。不要出現亂碼。不要新增 logo。不要新增配件。不要新增包裝。不要新增按鈕。不要新增螢幕。不要新增燈光零件。不要新增夾具。不要新增蓋子。不要新增手柄。不要新增標籤。不要新增瓶子。不要新增盒子。不要新增電子零件，除非產品資訊明確說明。不要移除產品現有特徵。不要拉伸。不要扭曲。不要彎折。不要摺疊。不要融化。不要旋轉到比例錯誤。不要膨脹。不要縮小成錯誤尺度。不要裁掉重要產品細節。不要重複生成不必要產品。不要讓產品模糊。不要簡化產品圖案。不要鏡頭之間產品外觀漂移。不要顯示 storyboard sheet。不要顯示 original product image。不要顯示 product detail board。不要顯示 catalog board。不要顯示 grid panel。不要顯示 collage。不要顯示 poster layout。不要顯示 static keyframe。不要 UGC。不要真人口播。不要手持開箱。不要 casual vlog。不要普通商品展示片。不要慢節奏品牌形象片。不要細菌消失。不要臭氣雲瞬間消失。不要科學淨化效果。不要清潔效果。不要醫療效果。不要 100% 效果。不要永久效果。不要假評論。不要假測試結果。不要把不可視化功效拍成直接證明。",
  "image": [
    "{{block_output_1717375.images_url}}",
    "{{block_output_1807253.data.url}}",
    "{{block_output_1807253.data.url}}"
  ],
  "video": [],
  "audio": [],
  "with_audio": true,
  "aspect_ratio": "16:9",
  "duration": 15,
  "extra_body": {
    "real_person_mode": true
  },
  "async": true,
  "watermark": false
}
```

