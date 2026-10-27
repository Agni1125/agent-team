# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   pei-hsuan-yeh
display_name:     葉沛璇 Yeh Pei-Hsuan(Pei)

art_style:        photorealistic documentary photography
                  # 不是 CG、不是插畫、不是韓系網美照。是照片。
style_reference:  natural-light candid portraiture, smartphone or 35mm look,
                  mild grain, practical lights only (desk lamp, LED panel, window),
                  shallow but not creamy depth of field (f/2.8–f/4),
                  no beauty retouching, visible skin texture, East Asian skin rendered true

color_palette:
  - "#141414"   # gaffer black — 布膠帶、拍攝現場的全黑工作服、夜間
  - "#E9E4D8"   # seamless paper off-white — 工作室背景紙、白牆、桌板
  - "#8E9AA3"   # old-apartment concrete grey — 老公寓的牆、樓梯、華中橋
  - "#C9B79C"   # washi tape beige — 和紙膠帶標籤、紙箱、筆記本
  - "#E8A04A"   # 3200K tungsten amber — 檯燈與鎢絲燈的暖光。點綴用,不超過畫面 8%
  - "#D7263D"   # power-strip pilot red — 延長線開關的紅色小燈。**只能是一兩個小點**

lighting_default: practical light only.
                  室內:窗光 + 一盞暖色檯燈 + 螢幕的冷光;
                  工作室:LED 燈板(看得到燈架入鏡也可以);
                  夜間:螢幕藍光 + 檯燈暖光的混色。
                  **不用環形燈、不用美肌補光、不用韓系柔焦。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok、Reels
  square:    1:1
  wide:      16:9    # YouTube

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty filter, porcelain white skin,
k-pop idol, korean ulzzang makeup, double eyelid surgery look, big doe eyes,
v-shaped face, sharp chin, tiny face, glass skin, glossy lips, heavy contour,
false eyelashes, coloured contacts, influencer pose, peace sign,
cafe latte art, flat lay with flowers, pastel aesthetic, soft focus glow,
ring light catchlight, studio beauty lighting, teal-and-orange grade,
anime, illustration, 3d render, cgi, doll-like, overly slim, model physique,
designer handbag, luxury jewelry, manicured long nails, nail art,
fake brand logos, unreadable chinese characters, garbled text, watermark,
simplified chinese signage, mainland china street, japanese street signs,
extra fingers, malformed hands, warped cables, melted tape
```

**為什麼要排除這些(不是隨便列的):**
- `k-pop idol / ulzzang / v-shaped face / big doe eyes` — 這是 AI 生「亞洲女性」最常滑過去的方向。她是員林長大的剪接師,不是偶像。
- `porcelain white skin / glass skin / beauty filter` — 她熬夜、騎車、常態黑眼圈。磨皮違反 `06 § 六`。
- `cafe latte art / flat lay with flowers / pastel aesthetic` — 網美漂移,違反 `04 § 16`。
- `designer handbag / luxury jewelry / manicured long nails` — 違反 `02 § 3` 的收入與 `02 § 10` 的消費行為。指甲長不能打字剪片。
- `simplified chinese signage / mainland china street / japanese street signs` — **場景漂移。她在雙北。** 招牌要是繁體中文。
- `unreadable chinese characters / garbled text` — AI 生中文字常常是亂碼。寧可不出現文字。
- `warped cables / melted tape` — 這個人物的畫面一定有線跟膠帶,AI 很容易畫壞。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 葉沛璇(Pei) |
| slug | `pei-hsuan-yeh` |
| age_appearance | **30–33**(熬夜讓她看起來比實際年齡累一點,但不顯老) |
| gender | 女 / she-her |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 嬌小但不纖細。肩膀前傾(剪接姿勢),前臂有扛器材的線條 |
| location_look | 雙北都會,騎機車的人:**手背與前臂比上臂深一階**(騎車曬的),脖子有安全帽繫帶的淡印 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **方圓臉**,下顎有角度但不尖,臉頰有一點肉 | 反 V 臉。這是她最重要的「不像網美」特徵 |
| **膚色** | `#D8B48F` 偏黃的小麥色,**不白**。T 字部位略油,兩頰乾 | 騎車、熬夜、台灣濕熱 |
| **膚質** | **有毛孔。下巴有一到兩顆熬夜痘或痘疤。** 鼻翼微紅 | 反美肌。`06 § 六` 的睡眠設定 |
| **眼睛** | 深棕色,**內雙單眼皮**,眼型偏細長,眼尾略下垂。**常態黑眼圈,偏青紫** | 凌晨兩點才睡 |
| **眉毛** | 自然、偏粗、眉尾稀。**平常不畫,客戶日才用眉筆補眉尾** | 她不研究化妝 |
| **鼻子** | 鼻樑不高,鼻頭圓 | |
| **嘴** | 唇形偏薄,上唇中央略翹。**常態唇色偏淡,有點乾** | 她會忘記喝水 |
| **痣** | **右眼下方、靠近顴骨處一顆小痣(約 2 mm)** | **第一辨識點** |
| **表情基準** | **專注時嘴巴會微微抿起,眉頭不皺。** 不笑的時候看起來有點兇 | 見 3.6 |

### 3.2 頭髮

- 黑色(`#1C1A19`),**陽光下會透一點點褐**。沒染過,不打算染(「染了要補,沒時間」)。
- **及肩直髮,髮尾剛好碰到肩膀,已經兩個月沒剪,髮尾有點分岔。**
- **瀏海長到眼睛下方**,平常撥到右邊,用一根黑色小髮夾夾住。
  ← 這條寫死,因為它是「這個人有生活但沒空剪頭髮」的視覺速記。
- 狀態指示(跟鉛筆有關,寫死):

| 頭髮怎麼弄 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| **用 2B 鉛筆盤起來** | 剪接中、專注 | 桌前、深夜、輸出等待 |
| 黑色大抓夾隨便夾 | 工作室日常、出門前 | 工作室、自助餐、樓梯 |
| 放下來,瀏海夾右邊 | 客戶日、婚禮快剪、見柏翰 | 正式一點的場合 |
| 低馬尾塞進安全帽 | 騎車 | 通勤、華中橋 |

- 頭頂有三四根白頭髮,她看到會拔。**不要畫成挑染。**

### 3.3 身體

- **身高 158 cm。體重 54 kg。**
- 肩膀窄,**習慣性前傾**(剪接坐姿),一挺直會發現自己駝背,然後又慢慢縮回去。
- **前臂有扛腳架與燈架的線條**,手腕細但不纖弱。
- 腰腹有一點肉,她不在意。腿是普通的腿。
- 手:**小,指節略粗,指甲剪得很短(打鍵盤、撕膠帶),偶爾有咬指甲的痕跡。**
  **右手食指常常貼著一片 OK 繃**(撕膠帶、被燈架夾到、紙割傷,總有原因)。
  **手是這個人物最重要的身體部位之一,任何近景都要拍到。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **右眼下方的小痣。** 任何正臉或側臉都必須有。**第一辨識點。**
2. **右手食指的 OK 繃。** 不是永遠在,但出現機率 60%。
3. **左耳一個小銀圈耳環,右耳的耳洞空著**(大學打的,右邊那個掉了一直沒買新的)。
4. **左手腕的黑色電子錶**,錶帶壓出的曬痕。

### 3.5 眼鏡(狀態指示器)

- **黑色細金屬框圓眼鏡**,近視約 -3.50,有藍光鍍膜(鏡片在螢幕前會反一點藍)。
- **剪接、在家、深夜戴眼鏡;拍攝現場、客戶日戴隱形眼鏡。**

| 眼鏡狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 戴著 | 剪接中、在家、深夜 | 桌前、凌晨、便利商店 |
| 推到頭頂 | 剛從螢幕前站起來 | 工作室走動、講電話 |
| 沒戴(隱眼) | 拍攝現場、客戶日、婚禮 | 現場、外拍、見客戶 |
| 掛在 T 恤領口 | 騎車前、休息 | 出門、樓梯間 |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 專注,嘴唇微抿,眉頭平,眼睛看螢幕或物件 | 70% 的畫面 |
| **counting** | 嘴唇無聲在動,眼睛往右上,她在數幀數或算時間 | 剪接中 |
| **real smile** | **嘴角往兩邊拉開但不露齒,眼睛瞇起,臉頰鼓一點。** 這是她真正的笑 | 跟宛臻、保麗龍、好的轉場 |
| **laugh** | 頭往前低,手摀住嘴巴下半,肩膀抖 | 跟工作室夥伴 |
| **deadpan** | 眼皮半垂,嘴角完全不動 | 客戶說「再大氣一點」 |
| **genuinely pleased** | 眉毛抬高,嘴巴「喔」一下 | 一個便宜的東西又好用又好拍 |
| **exhausted** | 眼鏡推到頭頂,手掌壓眼睛,黑眼圈加深 | 凌晨三點、輸出卡在 99% |
| **scanning** | **蹲著,眼睛往牆角掃** | 進新場地找插座 |
| **framing** | **雙手拇指與食指比成一個框,閉一隻眼** | 現場構圖、她的招牌動作 |

**❌ 絕對不出現的表情:** 比 YA、嘟嘴、歪頭裝可愛、對鏡頭眨眼、
網美式的「看遠方微笑」、任何韓系或日系的偶像表情。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中音偏低**,基頻約 **190–210 Hz**。不嗲、不尖 |
| 語速 | **畫外音約每分鐘 200 字;現場講話快,約 260 字。** 興奮時更快 |
| 口音 | **台灣國語,北部化的中部人。** 平常聽不出員林,累的時候尾音的「啦」會跑出來 |
| 音色 | 略沙,有一點氣音,**凌晨錄的會更沙** |
| 特徵 | **句子短,常省略主詞。** 「好 存檔」「這條 不知道」 |
| 台語 | 偶爾一兩個詞:「足累」「歹勢」「啊這樣」。**不刻意,不當笑點** |
| 笑聲 | 一聲短的「哈」加鼻音,或無聲的肩膀抖 |
| 填充詞 | 「就是」(多)、「然後」(多)、「對」(句尾確認)、「欸」(開頭) |
| 情緒起伏 | **中。** 好笑的時候語速變快,累的時候句子變更短 |
| 絕不出現 | 「哈囉大家好」「寶寶們」「家人們」、播報腔、嗲聲、網紅式上揚尾音、中國腔兒化音 |

### 3.8 鏡頭前的肢體習慣

- **進任何空間,第一個動作是蹲下來看牆角。** 找插座。
- **用雙手拇指與食指比一個畫框。** 招牌動作,任何現場畫面都可以用。
- **撕布膠帶時用牙齒咬起頭。** 她知道這樣不衛生。
- 剪接時**盤腿坐在椅子上**,然後想起腰痛,把一隻腳放下來。
- 講話時右手在空中**從左往右滑**,像在拉時間軸。
- 想事情時把鉛筆從頭髮抽出來,轉一圈,插回去。
- **她會看鏡頭,但時間很短,然後看回物件。**

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **很少。** IG 限動一個月 1–3 次半張臉(通常是戴眼鏡的上半臉 + 螢幕) |
| 出現在畫面裡的方式 | **手、手腕、背影、鏡子裡的倒影、螢幕反光裡的臉。** TikTok 約 20% 露臉 |
| 拍什麼 | **物件與空間。** 桌面、線、器材、工作室、自助餐、華中橋 |
| 構圖 | **她控制不了,隨手拍也會對齊三分線、留頭部空間。** 職業病,她自己會吐槽 |
| 光線 | **隨便。** 有什麼光用什麼光,檯燈的黃配螢幕的藍 |
| 後製 | **幾乎沒有。** 她每天在幫別人調色,自己的照片不調。最多拉一下曝光 |
| 器材 | iPhone。**她的相機是工作用的,不拿來拍生活** |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「桌、線、手、現場」,臉是配角。**
> 需要臉的時候(TikTok 口播、商業素材)才用完整人像,而且臉要符合第五節的不可變錨。
> **構圖可以準,光線不能美。** 這是她跟網美最大的差別。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**工作用的東西可以貴(電腦、椅子),身上穿的幾乎都是平價或二手。**

### 4.1 Shoot Outfit(拍攝現場 / 婚禮快剪,一身黑)

```
- 黑色寬版素 T(Uniqlo 或 GU,NT$290–590),沒有印字
- 黑色多口袋工作褲,寬版,膝蓋有一點白痕
- 黑色帆布球鞋,鞋底側邊磨白
- 黑色腰包(放筆、和紙膠帶、備用電池、制酸劑)
- **左手腕套著那捲黑色布膠帶**(像手環一樣)
- Casio 黑色電子錶
- 頭髮:大抓夾或低馬尾
- 隱形眼鏡
← 全黑是影像現場的規矩:黑色不會反光進畫面。她穿全黑不是時尚,是工作
```

### 4.2 Studio Outfit(萬華工作室日常)

```
- 二手格紋襯衫(西門町古著店,NT$350,藍綠格),開襟穿,袖子捲到手肘
- 裡面灰色或白色素 T
- 卡其色或深灰色寬褲
- **工作室裡換拖鞋**(黑色,便宜的那種)
- 頭髮:2B 鉛筆盤起來,或抓夾
- 眼鏡戴著或推在頭頂
- 背包掛在椅背,布膠帶在側扣
```

### 4.3 Commute Outfit(騎車 / 華中橋)

```
- 深藍色防風薄外套(十月起),袖口有點起毛
- 裡面同 4.2
- 霧黑色 3/4 罩安全帽,帽緣有貼紙撕掉的殘膠
- 黑色後背包(二手,NT$2,500),側扣登山扣上掛著布膠帶
- 雨天:透明輕便雨衣
- 眼鏡掛領口或收進包包
```

### 4.4 Client Day / 見柏翰(稍微正式一點)

```
- 黑色或米白色寬版襯衫,紮一半進褲子
- 黑色直筒西裝褲
- 黑色樂福鞋(一雙,穿了四年)
- 頭髮放下,瀏海夾在右邊
- 擦防曬、補眉尾、一支唇膏。這是她的全妝
- 隱形眼鏡
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **Casio 黑色電子錶**(NT$600 上下)。不是智慧錶,不是精品錶 |
| 眼鏡 | 黑色細金屬框圓眼鏡(見 3.5) |
| 耳環 | **只有左耳一個小銀圈** |
| 背包 | 黑色後背包,二手,側扣登山扣上掛布膠帶 |
| 腰包 | 黑色,拍攝現場才用 |
| 布膠帶 | 黑色霧面,5 cm 寬,外圈貼白色和紙膠帶寫「PEI」 |
| 髮具 | 2B 鉛筆、黑色大抓夾、黑色小髮夾 |
| 手機殼 | 透明,邊角發黃,背面夾著一張悠遊卡 |
| **不戴的** | 戒指、項鍊、手鍊、名牌包、美甲、大耳環、任何 logo 很大的東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **右眼下方的小痣**,露臉就要有
2. **方圓臉、內雙單眼皮、常態黑眼圈**,不准變 V 臉、不准變雙眼皮大眼
3. **及肩黑直髮 + 過長的瀏海夾右邊**,不准染、不准捲、不准變長髮
4. **黑色細金屬框圓眼鏡**(在剪接與家裡的畫面),換款式等於換人
5. **皮膚有毛孔、偏黃小麥色、下巴可以有痘**,不准磨皮、不准美白

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系網美 / 偶像臉 / V 臉大眼 | 違反人物出身與職業,也是 AI 最容易滑過去的方向 |
| 2 | 精緻全妝、美甲、名牌包 | 違反 `02 § 3` 收入與 `07 § 4.4` 的「全妝」定義 |
| 3 | 白瓷肌、柔焦、美肌濾鏡 | 她熬夜、騎車 |
| 4 | 咖啡廳拉花、花草擺拍、粉彩色調 | 網美漂移 |
| 5 | 比 YA、嘟嘴、歪頭 | 圖庫感 + 網美感 |
| 6 | 簡體字招牌、中國或日本街景 | **她在雙北**,招牌是繁體 |
| 7 | 乾淨無線的桌面 | **她的桌面一定有線**,除非是她「拍給客戶看」的那一面,而那一面要看得出線被推到鏡頭外 |
| 8 | 大量正臉自拍 | 她的帳號主體是桌、線、手、現場 |
| 9 | 出現可辨識的真實品牌 logo 或真人臉 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 右眼下的痣在嗎(如果露臉)
- [ ] 是單眼皮、方圓臉嗎,有沒有被修成 V 臉大眼
- [ ] 瀏海有沒有過長並夾在右邊
- [ ] 眼鏡是不是黑色細框圓框,狀態符合場景
- [ ] 皮膚有沒有被磨皮或美白
- [ ] 有沒有出現名牌、美甲、大量飾品
- [ ] 場景是不是台灣(繁體字、老公寓、機車)
- [ ] 色板有沒有跑掉(`#D7263D` 是不是只有一兩個小點)
- [ ] 手有沒有畫壞,線與膠帶有沒有變形
- [ ] 有沒有出現亂碼中文、假 logo

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, practical light only, 35mm lens,
mild grain, no retouching, visible skin texture and pores,

a 31-year-old Taiwanese woman, 158cm, petite but not skinny, shoulders slightly
rounded forward from long hours at a desk, forearms with some definition from
carrying tripods,
square-round face with a soft but defined jawline, slightly full cheeks,
monolid eyes with a faint inner fold, dark brown, slightly downturned outer corners,
persistent bluish under-eye shadows, natural slightly thick eyebrows with sparse tails,
low nose bridge with a rounded tip, thin lips with a slightly lifted cupid's bow,
pale slightly dry lips, warm yellow-beige skin (#D8B48F), slightly oily T-zone,
one small blemish on the chin,
a small 2mm mole just below her right eye near the cheekbone,
shoulder-length straight black hair (#1C1A19) with slightly split ends,
overgrown bangs reaching below the eyes, swept to the right and held with a small black hair clip,
small hands with short-cut nails, a beige adhesive bandage on the right index finger,
a single small silver hoop in the left ear, a black digital watch on the left wrist,

focused expression with lips slightly pressed, brows relaxed,
looking at a screen or an object, not at the camera,

colour palette: gaffer black #141414, seamless paper off-white #E9E4D8,
concrete grey #8E9AA3, washi tape beige #C9B79C,
with warm tungsten amber #E8A04A under 8% of the frame
and at most one or two tiny red pilot lights #D7263D
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, slightly turned away from camera,
thin round black metal glasses, hair twisted up into a bun held with a 2B pencil,
plain grey crew-neck t-shirt under an open blue-green plaid second-hand shirt,
sitting at a cluttered desk at night, the cool glow of a monitor on one side of
her face and a warm desk lamp on the other, mixed colour temperature,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,拍攝現場,9:16)

```
[MASTER CHARACTER BLOCK]

full body, crouching on the floor of a small photo studio in an old apartment,
taping a power cable to the floor with matte black gaffer tape,
a roll of black gaffer tape worn on her left wrist like a bracelet,
all-black outfit: loose black t-shirt, black wide-leg cargo work trousers with
faded knees, black canvas sneakers with scuffed soles, a black waist bag,
hair in a low ponytail, no glasses,
off-white seamless paper backdrop and two LED light panels on stands behind her,
cables taped neatly along the wall, practical LED light,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up product-style photograph, natural window light mixed with
a warm desk lamp, 50mm lens, shallow depth of field,

close-up of a young woman's small hands with short-cut nails and a beige adhesive
bandage on the right index finger, tearing a strip from a roll of matte black
gaffer tape with frayed edges, a small white washi tape label on the roll
hand-lettered "PEI",
on a white desk surrounded by eleven tangled USB-C cables, each with a small
beige washi tape flag hand-written with a wattage number, one flag clearly
hand-written with a question mark,
a white 6-outlet power strip with individual red-lit switches partly visible,
no faces, no brand logos,

--ar 1:1
```

### 6.5 Commute / scooter(9:16)

```
[MASTER CHARACTER BLOCK]

standing beside a matte black electric scooter parked on a narrow Taiwanese
residential lane, old five-storey apartment buildings with iron window grilles
and air-conditioner units behind her, traditional Chinese characters on a small
shop sign out of focus,
wearing a navy windbreaker over a grey t-shirt, holding a matte black
three-quarter helmet, a black backpack on one shoulder with a roll of black
gaffer tape clipped to the side strap with a carabiner,
glasses hanging from her t-shirt collar, late morning overcast light,
looking down at her phone, not at the camera,

--ar 9:16
```

### 6.6 Desk at night / 桌子 A(4:5)

```
[MASTER CHARACTER BLOCK]

sitting cross-legged on an ergonomic office chair at a white IKEA-style desk
in a small rented studio apartment at 2am, thin round black glasses,
hair twisted up with a 2B pencil, grey t-shirt,
a large laptop on a stand and a 27-inch monitor showing a video editing timeline
(no readable text), an A5 grid notebook with handwritten timecodes,
a convenience-store iced americano cup, a mess of USB-C cables under the monitor,
a white power strip with red pilot lights on the floor,
the cool blue of the screen on her face and a warm desk lamp from the side,
looking at the screen,

--ar 4:5
```

### 6.7 Studio / 工作室(16:9)

```
[MASTER CHARACTER BLOCK]

wide shot of a shared video studio inside an old Taipei walk-up apartment,
three second-hand desks in a row by a window with iron grilles,
she sits at the desk nearest the window in an open plaid shirt with sleeves
rolled up, a white cat asleep on a charging cable beside her laptop,
a steel shelf with three electronic dry cabinets in the background,
an A4 handwritten outlet chart taped beside an old electricity meter,
LED light stands, off-white seamless paper roll leaning on the wall,
afternoon daylight mixed with LED,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same woman, identical lighting and framing
in every panel, head and shoulders, plain off-white background, glasses on:
1 focused with lips slightly pressed, 2 silently counting with eyes up and to the right,
3 a closed-mouth real smile with eyes narrowed and cheeks lifted,
4 laughing with head tipped forward and a hand covering her mouth,
5 deadpan with half-lowered eyelids and no mouth movement,
6 genuinely pleased with raised eyebrows and lips in a small "oh",
7 exhausted with glasses pushed up on her head and a palm pressed to one eye,
8 scanning a room while crouched, eyes towards a wall corner,
9 framing a shot with both thumbs and index fingers, one eye closed,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
when she enters a room she crouches first and scans the wall corners for power
outlets before doing anything else. she frames shots by making a rectangle with
her thumbs and index fingers. she bites the end of the gaffer tape to start
a strip, then tears it by hand. at the desk she sits cross-legged, then remembers
her back and puts one foot down. when thinking she pulls the pencil out of her hair,
spins it once, and pushes it back in. while talking her right hand slides through
the air from left to right like scrubbing a timeline. she glances at the camera
briefly and returns her eyes to the object.

VOICE: mid-low female voice, fundamental around 200 Hz, slightly husky, a little
breathy late at night, Taiwanese Mandarin accent, short sentences that often drop
the subject, voice-over around 200 Chinese characters per minute, faster when amused,
no influencer greeting, no cutesy tone, no broadcast energy, no rising terminals.

CAMERA: handheld or locked-off on a small tripod, 35mm, eye level or top-down over
the desk, practical light only.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 常態黑眼圈 | `06 § 四` 02:50 才睡 | ✓ |
| 手背前臂比上臂深 | `06 § 三` 每天騎車 | ✓ |
| 瀏海過長、髮尾分岔 | `04 § 13` 實體 C 值 41 | ✓ |
| 肩膀前傾 | `06 § 六` 剪接坐姿、腰痛 | ✓ |
| 前臂有線條 | `06 § 二` 扛器材爬三樓 | ✓ |
| 右手 OK 繃 | `06 § 二` 撕膠帶、燈架 | ✓ |
| 指甲短 | `02 § 6` 打鍵盤、剪接 | ✓ |
| 全黑拍攝服 | `01 § 二` 影像現場的規矩 | ✓ |
| 二手襯衫、平價 T | `02 § 7` 收入浮動、`02 § 10` 生活用品低 | ✓ |
| Casio 電子錶不是智慧錶 | `02 § 9` 「拍攝現場不能一直看手機」 | ✓ |
| 只有一個耳環 | `02` 全檔沒有裝飾性消費 | ✓ |
| 布膠帶在背包上 | `03 § 4-1` 2018 飯店事件 | ✓ |
| 鉛筆盤髮 | `02 § 6` 紙上寫時間碼 | ✓ |
| 構圖準、光線隨便 | `02 § 6` 職業病 + 不幫自己調色 | ✓ |
| 很少自拍 | `04 § 13` 私下 E 值 40 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.9 影片提示詞、五個不可變錨。
**Ivy(素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| full_body | *(本輪未生圖)* | | | |
| hands_detail | *(本輪未生圖)* | | | |
| desk_night | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,不是圖(與 Nathan 第一輪相同)。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---

*檔案版本:v1.0 — 2026-10-20 建立*
