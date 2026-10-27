# 38. 影片生成_Seedance2.0_branding(HTTP 請求)

| 欄位 | 值 |
| --- | --- |
| 節點 ID | `106692` |
| 型別 | `http` |
| 拓樸序 | 38 |
| DAG 層深 | 8 |
| Coze 說明 | 用于发送API请求，从接口返回数据 |

## 連線

- 上游:`189371` 參考圖轉url_2
- 下游:（無）

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

- 本節點引用的上游變數:`{{block_output_100001.PRODUCT_INFO}}`, `{{block_output_176487.data.url}}`, `{{block_output_178234.data.url}}`, `{{block_output_189371.images_url}}`

## 提示詞原文(逐字保留,不得修改)

### `body.prompt`

- SHA-256:`7a5ba3b8dd18b480b94fc079516b807e90dbee22d2fc9f064ba5a0b7e31cc6be`
- 長度:3022 字元

<!-- PROMPT-BEGIN body.prompt -->
生成一支 15 秒、16:9、高級品牌形象廣告影片。

影片類型是 premium branding commercial、cinematic product film。不是 UGC，不要真人口播，不要手持開箱感，不要生活隨拍感，不要 vlog 感。

請使用上傳的品牌影片分鏡圖作為影片鏡頭方向參考{{block_output_178234.data.url}}。品牌影片分鏡圖只負責影片的構圖、鏡頭角度、光影方向、鏡頭節奏、產品位置、場景氛圍、電影感和高級品牌感。不要把品牌影片分鏡圖本身直接放進影片裡。

請使用上傳的原產品圖作為產品外觀主參考{{block_output_189371.images_url}}。原產品圖是產品外觀最高優先級參考，負責鎖定產品的真實類型、整體外觀、數量、款式、排列關係、比例、形狀、顏色系統、產品家族一致性與整體視覺辨識。不要把原產品圖本身直接放進影片裡。

請使用上傳的產品細節結構圖作為產品外觀細節鎖定參考{{block_output_176487.data.url}}。產品細節結構圖只負責補充鎖定目標產品外觀細節，包括產品類型、形狀、輪廓、比例、厚度、材質、表面質感、顏色配置、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、變體差異與產品結構。不要把產品細節結構圖本身直接放進影片裡。

產品資訊：{{block_output_100001.PRODUCT_INFO}}

品牌影片分鏡圖：
{{block_output_178234.data.url}}

原產品圖：
{{block_output_189371.images_url}}

產品細節結構圖：
{{block_output_176487.data.url}}

產品外觀準確度是最高優先級。優先級順序為：第一，原產品圖；第二，產品細節結構圖；第三，產品資訊；第四，品牌影片分鏡圖。如果品牌影片分鏡圖、原產品圖、產品細節結構圖和產品資訊發生衝突，請優先保留原產品圖與產品細節結構圖中的產品外觀。不要為了畫面更好看而改變產品外觀。不要把產品改成更常見、更漂亮、更像其他商品的替代品。

所有上傳圖片都只是 reference。不要直接顯示 storyboard image、original product image、product detail board、product layout board、catalog sheet、grid layout、collage、poster、keyframe sheet、frame sheet 或 static graphic board。請把參考圖片轉譯成真實的 cinematic moving footage。

影片第 0–2 秒必須一開始就是像真實攝影機拍攝的動態畫面。不要用靜態圖片開場，不要用分鏡圖開場，不要用原產品圖開場，不要用產品展示板開場，不要用海報或標題卡開場。第一幀就要有真實鏡頭運動或環境動態，例如 slow push-in、subtle parallax、moving reflections、soft light sweep、natural shadow movement、shallow depth-of-field shift 或 subtle product micro motion。

請嚴格根據分鏡策略與腳本架構執行每一個時間段。每個時間段都要生成清楚的電影感產品鏡頭。所有鏡頭必須連貫、精緻、高級、克制、有品牌形象廣告感。

請使用原產品圖、產品資訊與產品細節結構圖作為目標產品外觀的唯一依據。必須保留產品的真實商品類型、產品數量、款式數量、形狀、輪廓、尺寸、比例、厚度、材質、表面質感、紋理、顏色、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、包裝狀態與使用方式。不要重新設計產品，不要改變產品類別，不要用相似商品替代目標產品，不要新增產品資訊中沒有出現的功能、零件、配件、包裝、材質、結構或使用方式，不要刪除產品原本存在的重要特徵。產品在整支影片中必須保持一致，不得出現 shot-to-shot product drift。

如果產品有多個款式，每個款式必須保持獨立。不得混用不同款式的顏色、文字、名稱、logo、圖案、字體或版面。總覽鏡頭可以展示多個款式。細節特寫鏡頭只使用單一 selected product unit 或 selected variant，避免多款產品細節混亂。

產品上的所有文字、logo、icon、標籤、slogan、香型名稱、型號、符號與印刷圖案，都必須視為鎖定的 raster artwork，不是可編輯文字。不要重寫產品文字，不要翻譯產品文字，不要替換產品文字，不要改變字體，不要改變文字大小，不要改變文字顏色，不要改變文字位置，不要新增假文字，不要產生亂碼。如果小字在動態影片中無法完全清楚，請保持原本文字區塊的位置、排列和視覺結構，讓它自然地微模糊或動態模糊，不要生成新的錯誤文字。

如果產品資訊顯示沒有包裝，或沒有明確要求展示包裝，影片中不得出現任何包裝。不要出現 box、tray、sleeve、pouch、bag、plastic wrap、retail package、shipping carton、package label、package sticker、package seal、package logo、package text、package graphics。

畫面要高級、乾淨、克制、精緻。使用高級商業廣告光影、柔和電影感燈光、細膩陰影、淺景深、平滑運鏡、真實反射、精緻產品 hero framing。保持產品清楚、穩定、銳利。保持產品在所有鏡頭中的外觀一致。

負面提示詞：不要重新設計產品。不要讓產品變形。不要改變產品類別。不要用相似商品替代目標產品。不要改變產品形狀。不要改變產品輪廓。不要改變產品比例。不要改變產品尺寸。不要讓產品變厚。不要使用錯誤材質。不要改變表面質感。不要顏色漂移。不要 logo 漂移。不要文字漂移。不要圖案漂移。不要比例漂移。不要包裝漂移。不要類別漂移。不要款式混用。不要交換顏色。不要交換 slogan。不要交換名稱。不要出現假文字。不要出現亂碼。不要新增 logo。不要新增配件。不要新增包裝。不要新增按鈕。不要新增螢幕。不要新增燈光零件。不要新增夾具。不要新增蓋子。不要新增手柄。不要新增標籤。不要新增瓶子。不要新增盒子。不要新增電子零件，除非產品資訊明確說明。不要移除產品現有特徵。不要拉伸。不要扭曲。不要彎折。不要摺疊。不要融化。不要旋轉到比例錯誤。不要膨脹。不要縮小成錯誤尺度。不要裁掉重要產品細節。不要重複生成不必要產品。不要讓產品模糊。不要簡化產品圖案。不要鏡頭之間產品外觀漂移。不要顯示 storyboard sheet。不要顯示 original product image。不要顯示 product detail board。不要顯示 catalog board。不要顯示 grid panel。不要顯示 collage。不要顯示 poster layout。不要顯示 static keyframe。不要 UGC。不要真人口播。不要手持開箱。不要 casual vlog。
<!-- PROMPT-END body.prompt -->

## 請求 body 樣板(逐字保留)

```json
{
  "model": "doubao-seedance-2.0-fast",
  "prompt": "生成一支 15 秒、16:9、高級品牌形象廣告影片。\n\n影片類型是 premium branding commercial、cinematic product film。不是 UGC，不要真人口播，不要手持開箱感，不要生活隨拍感，不要 vlog 感。\n\n請使用上傳的品牌影片分鏡圖作為影片鏡頭方向參考{{block_output_178234.data.url}}。品牌影片分鏡圖只負責影片的構圖、鏡頭角度、光影方向、鏡頭節奏、產品位置、場景氛圍、電影感和高級品牌感。不要把品牌影片分鏡圖本身直接放進影片裡。\n\n請使用上傳的原產品圖作為產品外觀主參考{{block_output_189371.images_url}}。原產品圖是產品外觀最高優先級參考，負責鎖定產品的真實類型、整體外觀、數量、款式、排列關係、比例、形狀、顏色系統、產品家族一致性與整體視覺辨識。不要把原產品圖本身直接放進影片裡。\n\n請使用上傳的產品細節結構圖作為產品外觀細節鎖定參考{{block_output_176487.data.url}}。產品細節結構圖只負責補充鎖定目標產品外觀細節，包括產品類型、形狀、輪廓、比例、厚度、材質、表面質感、顏色配置、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、變體差異與產品結構。不要把產品細節結構圖本身直接放進影片裡。\n\n產品資訊：{{block_output_100001.PRODUCT_INFO}}\n\n品牌影片分鏡圖：\n{{block_output_178234.data.url}}\n\n原產品圖：\n{{block_output_189371.images_url}}\n\n產品細節結構圖：\n{{block_output_176487.data.url}}\n\n產品外觀準確度是最高優先級。優先級順序為：第一，原產品圖；第二，產品細節結構圖；第三，產品資訊；第四，品牌影片分鏡圖。如果品牌影片分鏡圖、原產品圖、產品細節結構圖和產品資訊發生衝突，請優先保留原產品圖與產品細節結構圖中的產品外觀。不要為了畫面更好看而改變產品外觀。不要把產品改成更常見、更漂亮、更像其他商品的替代品。\n\n所有上傳圖片都只是 reference。不要直接顯示 storyboard image、original product image、product detail board、product layout board、catalog sheet、grid layout、collage、poster、keyframe sheet、frame sheet 或 static graphic board。請把參考圖片轉譯成真實的 cinematic moving footage。\n\n影片第 0–2 秒必須一開始就是像真實攝影機拍攝的動態畫面。不要用靜態圖片開場，不要用分鏡圖開場，不要用原產品圖開場，不要用產品展示板開場，不要用海報或標題卡開場。第一幀就要有真實鏡頭運動或環境動態，例如 slow push-in、subtle parallax、moving reflections、soft light sweep、natural shadow movement、shallow depth-of-field shift 或 subtle product micro motion。\n\n請嚴格根據分鏡策略與腳本架構執行每一個時間段。每個時間段都要生成清楚的電影感產品鏡頭。所有鏡頭必須連貫、精緻、高級、克制、有品牌形象廣告感。\n\n請使用原產品圖、產品資訊與產品細節結構圖作為目標產品外觀的唯一依據。必須保留產品的真實商品類型、產品數量、款式數量、形狀、輪廓、尺寸、比例、厚度、材質、表面質感、紋理、顏色、logo 位置、文字位置、圖案排列、孔位、掛繩、邊角、邊緣、配件、包裝狀態與使用方式。不要重新設計產品，不要改變產品類別，不要用相似商品替代目標產品，不要新增產品資訊中沒有出現的功能、零件、配件、包裝、材質、結構或使用方式，不要刪除產品原本存在的重要特徵。產品在整支影片中必須保持一致，不得出現 shot-to-shot product drift。\n\n如果產品有多個款式，每個款式必須保持獨立。不得混用不同款式的顏色、文字、名稱、logo、圖案、字體或版面。總覽鏡頭可以展示多個款式。細節特寫鏡頭只使用單一 selected product unit 或 selected variant，避免多款產品細節混亂。\n\n產品上的所有文字、logo、icon、標籤、slogan、香型名稱、型號、符號與印刷圖案，都必須視為鎖定的 raster artwork，不是可編輯文字。不要重寫產品文字，不要翻譯產品文字，不要替換產品文字，不要改變字體，不要改變文字大小，不要改變文字顏色，不要改變文字位置，不要新增假文字，不要產生亂碼。如果小字在動態影片中無法完全清楚，請保持原本文字區塊的位置、排列和視覺結構，讓它自然地微模糊或動態模糊，不要生成新的錯誤文字。\n\n如果產品資訊顯示沒有包裝，或沒有明確要求展示包裝，影片中不得出現任何包裝。不要出現 box、tray、sleeve、pouch、bag、plastic wrap、retail package、shipping carton、package label、package sticker、package seal、package logo、package text、package graphics。\n\n畫面要高級、乾淨、克制、精緻。使用高級商業廣告光影、柔和電影感燈光、細膩陰影、淺景深、平滑運鏡、真實反射、精緻產品 hero framing。保持產品清楚、穩定、銳利。保持產品在所有鏡頭中的外觀一致。\n\n負面提示詞：不要重新設計產品。不要讓產品變形。不要改變產品類別。不要用相似商品替代目標產品。不要改變產品形狀。不要改變產品輪廓。不要改變產品比例。不要改變產品尺寸。不要讓產品變厚。不要使用錯誤材質。不要改變表面質感。不要顏色漂移。不要 logo 漂移。不要文字漂移。不要圖案漂移。不要比例漂移。不要包裝漂移。不要類別漂移。不要款式混用。不要交換顏色。不要交換 slogan。不要交換名稱。不要出現假文字。不要出現亂碼。不要新增 logo。不要新增配件。不要新增包裝。不要新增按鈕。不要新增螢幕。不要新增燈光零件。不要新增夾具。不要新增蓋子。不要新增手柄。不要新增標籤。不要新增瓶子。不要新增盒子。不要新增電子零件，除非產品資訊明確說明。不要移除產品現有特徵。不要拉伸。不要扭曲。不要彎折。不要摺疊。不要融化。不要旋轉到比例錯誤。不要膨脹。不要縮小成錯誤尺度。不要裁掉重要產品細節。不要重複生成不必要產品。不要讓產品模糊。不要簡化產品圖案。不要鏡頭之間產品外觀漂移。不要顯示 storyboard sheet。不要顯示 original product image。不要顯示 product detail board。不要顯示 catalog board。不要顯示 grid panel。不要顯示 collage。不要顯示 poster layout。不要顯示 static keyframe。不要 UGC。不要真人口播。不要手持開箱。不要 casual vlog。",
  "image": [
    "{{block_output_176487.data.url}}",
    "{{block_output_178234.data.url}}",
    "{{block_output_189371.images_url}}"
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

