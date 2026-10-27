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
character_slug:   yu-hsiang-liao
display_name:     廖宇翔 Liao Yu-Hsiang(小廖 / 阿翔)

art_style:        photorealistic smartphone snapshot photography
                  # 不是 CG、不是插畫、不是男團寫真。是一個 26 歲工程師的手機照。
style_reference:  everyday candid snapshot, iPhone wide lens look, slightly soft focus,
                  mild noise in low light, fluorescent office light or warm desk lamp,
                  no beauty retouching, visible skin texture, East Asian skin rendered true,
                  occasionally a faint blue haze over the whole frame (camera sticker effect)

color_palette:
  - "#3E6E8E"   # security sticker blue — 保密貼紙、識別證掛繩、週末照片的藍霧。主色
  - "#D9D4C7"   # yellowed power-strip white — 前房客的延長線、老公寓的牆
  - "#6B7A5A"   # bamboo green-grey — 竹山的竹林、阿公的筍、媽媽的保鮮盒蓋
  - "#2B2B2B"   # night scooter black — 夜騎、安全帽內襯、大肚山的夜
  - "#F2B134"   # meat-sauce amber — 員工餐廳肉燥、逢甲夜市的燈。點綴,不超過畫面 10%

lighting_default: practical light only.
                  公司:天花板日光燈,偏冷,平;
                  家裡:一盞暖色檯燈 + 螢幕光,桌子貼著床,光很近;
                  戶外:騎車的白天(台中的大太陽)或夜騎的街燈與城市夜景。
                  **不用環形燈、不用棚燈、不用柔光美肌。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok
  square:    1:1
  wide:      16:9    # YouTube(他沒有在用,保留)

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
k-pop idol, korean boy band styling, perm hair, two-block undercut with styled fringe,
dyed hair, highlights, flawless skin, airbrushed skin, beauty filter,
v-shaped face, sharp jawline model, six-pack, gym physique, muscular arms,
designer streetwear, oversized luxury logo, gold chain, luxury watch, smartwatch,
influencer pose, peace sign, model stance, studio portrait lighting, ring light catchlight,
teal-and-orange grade, cinematic color grading,
clean minimalist desk setup, rgb keyboard lighting, desk mat aesthetic, cable management showcase,
anime, illustration, 3d render, cgi,
fake brand logos, readable company name, corporate logo on lanyard,
unreadable chinese characters, garbled text, watermark,
simplified chinese signage, mainland china street, japanese street signs,
laboratory interior, clean room, test equipment close-up,
extra fingers, malformed hands, warped cables, melted plastic
```

**為什麼要排除這些(不是隨便列的):**
- `k-pop idol / two-block undercut with styled fringe / perm hair` — 這是 AI 生「亞洲年輕男性」最常滑過去的方向。他的頭髮是 NT$200 百元快剪,不是韓系髮廊。
- `six-pack / gym physique` — 他只打桌球,有一點小腹(`06 § 七`)。
- `designer streetwear / luxury watch / smartwatch` — 違反 `02 § 3` 的收入與 `02 § 10` 的二手消費。他戴 NT$990 的運動手環。
- `clean minimalist desk setup / rgb keyboard / desk mat aesthetic` — **桌面網美漂移。** 他的桌子是前房客的,不好看,他也沒在拍。那是阿哲學長的風格,不是他的。
- `readable company name / corporate logo on lanyard` — **法遵與 NDA。** 公司是虛構的,任何可辨識的字樣都會讓人以為是真的公司。
- `laboratory interior / clean room / test equipment close-up` — **他不能在實驗室拍照。** 任何實驗室畫面都會讓帳號看起來像在洩密,也會讓人以為他在「驗證」什麼產品。
- `simplified chinese signage / mainland china street` — **場景漂移。他在台中。** 招牌要是繁體中文。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 廖宇翔(小廖 / 阿翔) |
| slug | `yu-hsiang-liao` |
| age_appearance | **25–27**(剛出社會的臉,但騎車曬得比辦公室同事黑) |
| gender | 男 / he-him |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 中等身高、偏瘦但有一點小腹,肩膀不寬,手臂有騎車的曬痕 |
| location_look | 台中機車族:**手臂上明顯的短袖曬痕,臉比脖子深一點** |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **國字臉,臉不長**,下顎角看得出來但不銳利,下巴不尖 | 反 V 臉。普通台灣男生的臉 |
| **膚色** | `#C9A27E` 偏黃小麥色,**臉頰比額頭深一點**(安全帽遮額頭) | 每天騎車 |
| **膚質** | **兩頰有青春痘留下的淺凹疤**,T 字略油,鼻翼毛孔明顯 | 反美肌。研究所熬夜留下的 |
| **眼睛** | 深棕色,**外雙但眼型偏細**,眼皮有一點腫(早上) | |
| **眉毛** | 濃、平,**完整,不畫疤** | 斷眉是 `persona_tw_06` 的辨識點 |
| **疤** | **左耳上方髮際一道約 2 cm 的疤,那一塊不長頭髮;兩側推短之後一定露出來** | **第一辨識點**(國小二年級在竹林坡地摔的,`02 § 11`) |
| **鼻子** | 鼻樑中等,鼻頭略寬 | |
| **嘴** | 唇偏厚,嘴角自然微下垂 | 不笑的時候看起來有點悶 |
| **鬍子** | **下巴與上唇一點稀疏的鬍渣,兩三天刮一次** | 他用便宜的電動刮鬍刀 |
| **表情基準** | **看手機時下巴往內收,出現一點雙下巴;眉頭微微往中間靠。** 不是不高興,是在算 | 見 3.6 |

### 3.2 頭髮

- 黑色(`#151414`),**粗、硬、直**。沒染過。
- **兩側用電剪推短(不是韓系 two-block,是傳統百元快剪的推法,側邊跟頂部之間有明顯的段差),
  頂部留約 4 公分,往右邊隨便撥。** 一個月剪一次,NT$200。
- **戴安全帽之後頂部被壓扁、側邊留一圈壓痕**,他不整理。**頭頂不翹**(翹毛是 `persona_tw_02b` 的辨識點)。
- 狀態指示:

| 頭髮狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 頂部被壓扁、側邊有安全帽壓痕 | 剛騎車到 | 上班開場、到竹山 |
| 睡亂、沒梳 | 剛起床 / 週末 | 床上、週六早上 |
| 濕的、往後撥 | 剛打完桌球 | 桌球社、宵夜 |
| 剛剪完(側邊特別短) | 每月初 | 偶爾 |

### 3.3 身體

- **身高 172 cm。體重 67 kg。** 研究所時 63 kg。
- 肩膀不寬,**有一點駝**(看儀器、看手機)。坐著的時候小腹會出現。
- **手臂:短袖曬痕非常明顯**,上臂白、前臂深。
- 手:**指節粗,指甲剪很短,右手中指第一節有一個寫字的繭。** 手背有一道淡淡的舊燙傷(研究所焊東西)。
  **手是這個人物很重要的身體部位,任何近景都要拍到。**
- 腿:普通。桌球打出來的小腿肌肉有一點。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **左耳上方髮際的疤(那一塊不長頭髮)。** 任何正臉或左側臉都必須有。**第一辨識點。**
2. **兩頰的淺痘疤。** 不准修掉。
3. **手臂的短袖曬痕。** 穿短袖時一定要有。
4. **右手腕的黑色運動手環**(便宜款,錶帶有一點磨白)。

### 3.5 眼鏡(狀態指示器)

- **銀色細金屬框眼鏡,鏡片偏圓**,眼鏡行 NT$1,990 套餐。近視約 -4.00。**左邊鼻墊歪了一點**,鏡框常常滑下來。
- **他一直戴眼鏡。** 打桌球也戴(用運動眼鏡帶綁著)。

| 眼鏡狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 正常戴著 | 預設 | 大部分畫面 |
| **滑到鼻頭,用中指推回去** | 在看東西、在算 | 看手機、看標籤、看筆記本 |
| 綁著運動眼鏡帶 | 桌球 | 桌球社 |
| 推到額頭 | **在近看一個很小的東西**(標籤、字號) | **翻背面看充電頭的時候**(招牌動作) |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 眉頭微靠、下巴內收、嘴角微下,眼睛看手機或物件 | 70% 的畫面 |
| **calculating** | 眼睛往左上,嘴唇微動,手指在桌上輕點,**他在換算天數** | 看到價格 |
| **real smile** | **嘴巴張開露出上排牙,眼睛瞇成兩條線,臉頰上的痘疤更明顯** | 跟阿彬、阿公、桌球殺球得分 |
| **laugh** | 往後靠,拍桌子或拍大腿,笑出聲 | 跟室友、跟社團 |
| **awkward polite** | **嘴角往上扯但眼睛沒笑,點頭** | 學長說「舊的誰要」、親戚問年終 |
| **genuinely pleased** | 眉毛往上抬,嘴巴抿著忍笑 | 二手東西比預期好用 |
| **squinting at a label** | **眼鏡推到額頭,東西拿到離臉十公分,眼睛瞇起來** | 翻背面看字號 |
| **tired** | 眼鏡拿下來,手指捏鼻樑 | DVT 加班到八點 |
| **quiet** | 看著遠方(夜騎停在大肚山上),什麼表情都沒有 | 壓力大的時候 |

**❌ 絕對不出現的表情:** 比 YA、嘟嘴、wink、男團式的歪頭微笑、對鏡頭放電、
任何韓系或日系的偶像表情、健身房自拍的那種表情。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中音**,基頻約 **115–130 Hz**。不低沉、不尖 |
| 語速 | **畫外音約每分鐘 210 字;講到價錢會變快,約 250 字** |
| 口音 | **台灣國語,中部腔。** 「欸」很多,句尾常帶「啦」「捏」。台語詞自然混進來 |
| 音色 | 乾淨但有一點鼻音,早上講話比較啞 |
| 特徵 | **講數字很清楚、很慢**,其他都講很快。「一千五百三十三」會一個字一個字講 |
| 台語 | 自然混用:「夭壽貴」「無采」(可惜)「好啦好啦」「按呢」。**不刻意,不當笑點** |
| 笑聲 | 短的「哈」連兩三聲,或「呵呵」 |
| 填充詞 | 「欸」(多)、「就是」(多)、「然後」(多)、「對啊」(句尾) |
| 情緒起伏 | **低到中。** 講到換算天數時會有一點得意 |
| 絕不出現 | 「哈囉大家好」「各位」「家人們」、播報腔、男團式的低音撩、中國腔兒化音、業務腔 |

### 3.8 鏡頭前的肢體習慣

- **拿到任何電器,第一個動作是翻過來看背面。** 眼鏡推到額頭,拿到臉前十公分。
- **用中指推眼鏡**(鏡框右邊鬆,一直滑)。
- **算錢的時候,右手食指在桌上輕點,像在按計算機。**
- 坐椅子的時候**一腳踩在椅子邊緣**(前房客的椅子太低)。
- 講話時手放在膝蓋上,不太比手勢。
- 撕手機上的保密貼紙時,**用大拇指指甲從角落慢慢摳**,然後看殘膠。
- **他看鏡頭的時間很短,而且會有點尷尬地笑一下。** 他不習慣被拍。

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎不。** 一年兩三次,都是跟別人的合照(阿彬、桌球社) |
| 出現在畫面裡的方式 | **手、手臂(有曬痕)、背影、安全帽的倒影、合照裡的一角。** TikTok 約 10% 露臉 |
| 拍什麼 | **東西與價格。** 二手面交拿到的東西、蝦皮購物車截圖、員工餐廳的餐盤、夜騎的夜景、阿公的筍 |
| 構圖 | **普通。** 東西放中間,拍完就好。他不會調整角度 |
| 光線 | 有什麼光用什麼光 |
| 後製 | **零。** 連裁切都很少 |
| 器材 | iPhone 13。**週末的照片常常霧霧的,因為保密貼紙忘了撕** |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「東西、價格、手、台中的路」,臉是極少數的配角。**
> **構圖普通、光線普通、偶爾一層藍霧。** 這是他跟桌面 KOL 最大的差別:他的照片是在記錄,不是在展示。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**身上幾乎沒有新的東西,除了鞋子跟安全帽。**

### 4.1 Lab Outfit(上班 / 實驗室)

```
- 灰色或深藍色素 T(三件一組的那種,穿了三年,領口有點鬆)
- 公司配發的淺藍色防靜電外套(只在實驗室穿,辦公區脫掉掛椅背)
- 黑色或深灰色運動長褲
- 黑色布鞋(實驗室規定包鞋)
- 公司識別證,藍色掛繩(**無任何可辨識字樣**)
- 黑色運動手環(右手)
- 黑框眼鏡
- 頭髮:被安全帽壓過
← 防靜電外套是規定,不是時尚。外套袖口有一點黑,是儀器桌的
```

### 4.2 Home / Fengjia Outfit(下班 / 逢甲 / 房間)

```
- 褪色的大學系服 T(灰色,胸口的印字已經裂開,看不出字)
- 黑色籃球短褲
- 藍白拖
- 頭髮睡亂
- 眼鏡滑到鼻頭
← 這是他 60% 的時間的樣子。拿外帶、去自助洗衣、下樓拿外送都是這套
```

### 4.3 Table Tennis / Weekend Ride(桌球 / 夜騎)

```
- 桌球社的深綠色排汗衫(社團一起訂的,背面的字不可辨識)
- 黑色運動短褲
- **桌球鞋:白色,這是他今年唯一買新的鞋**
- 運動眼鏡帶綁著眼鏡
- 夜騎時:外面加表哥給的灰色刷毛外套,白色 3/4 罩安全帽,
  安全帽上夾著學長的舊運動攝影機
```

### 4.4 Going Home / 回竹山(冬天或正式一點)

```
- 灰色刷毛外套(表哥的,袖口起毛球)
- 裡面格紋襯衫(媽媽在竹山市場買的,NT$290)
- 深藍色牛仔褲
- 黑色布鞋
- 背一個公司尾牙抽到的黑色後背包,裝媽媽要他帶回台中的東西
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 手環 | **黑色運動手環**(NT$990 上下),右手。不是智慧錶,不是精品錶 |
| 眼鏡 | 銀色細金屬框、偏圓(見 3.5) |
| 識別證 | 藍色掛繩,**無可辨識字樣**。週末掛在房門後 |
| 鑰匙圈 | 機車鑰匙 + **媽媽在紫南宮求的紅色平安符** + 一個開瓶器 |
| 背包 | 公司尾牙抽到的黑色後背包 |
| 安全帽 | **白色 3/4 罩,新的**(2024 年,阿彬陪他買的) |
| 手機殼 | 透明軟殼,邊角發黃。**後鏡頭附近一圈白色殘膠** |
| **不戴的** | 項鍊、戒指、耳環、智慧錶、精品錶、潮牌帽、任何 logo 很大的東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **左耳上方髮際的疤**,露臉就要有
2. **國字臉、兩頰淺痘疤、皮膚偏黃小麥色**,不准變 V 臉、不准磨皮
3. **兩側推短的傳統快剪 + 頂部 4 公分黑髮**,不准染、不准燙、不准變韓系
4. **銀色細金屬框、偏圓的眼鏡**,換款式等於換人
5. **手臂的短袖曬痕**,穿短袖就要有

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系男團 / 偶像臉 / 燙髮染髮 | 違反收入與出身,也是 AI 最容易滑過去的方向 |
| 2 | 健身身材、六塊肌 | 他只打桌球,有小腹 |
| 3 | 潮牌、精品、智慧錶 | 違反 `02 § 3` 收入與 `02 § 10` 二手消費 |
| 4 | **乾淨無線的 desk setup 網美桌** | 那是阿哲的風格。他的桌子是前房客的,不好看 |
| 5 | 比 YA、男團歪頭笑 | 圖庫感 + 偶像感 |
| 6 | 簡體字招牌、中國或日本街景 | **他在台中**,招牌是繁體 |
| 7 | **實驗室、無塵室、測試儀器入鏡** | NDA,而且會讓人以為他在驗證產品 |
| 8 | 大量正臉自拍 | 他的帳號主體是東西與價格 |
| 9 | 可辨識的真實品牌 logo、公司名、真人臉 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 左耳上方髮際的疤在嗎(如果露臉);眉毛有沒有被畫出疤(不可以)
- [ ] 臉是國字臉、有痘疤嗎,有沒有被修成 V 臉磨皮
- [ ] 頭髮是傳統快剪、沒有染燙嗎
- [ ] 眼鏡是銀色細金屬框、偏圓嗎(不是黑粗框)
- [ ] 穿短袖時手臂有沒有曬痕
- [ ] 有沒有出現潮牌、精品、智慧錶
- [ ] 場景是不是台中(繁體字、老公寓、機車、逢甲、中科路)
- [ ] **有沒有出現實驗室或測試儀器**(不准)
- [ ] **識別證、掛繩、保密貼紙上有沒有可辨識字樣**(不准)
- [ ] 手有沒有畫壞,線與延長線有沒有變形

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic smartphone snapshot, practical light only, wide phone lens look,
mild noise, no retouching, visible skin texture and pores,

a 26-year-old Taiwanese man, 172cm, slim with a slight belly, narrow slightly
rounded shoulders, forearms visibly more tanned than upper arms from riding a scooter
(clear t-shirt tan line),
square face that is short rather than long, a visible but soft jaw angle, soft non-pointed chin,
faint acne scars on both cheeks, slightly oily T-zone, warm yellow-tan skin (#C9A27E),
cheeks darker than forehead,
dark brown eyes, narrow eyes with a natural outer double eyelid,
thick flat unbroken eyebrows,
a 2cm hairless scar just above his LEFT ear, exposed by the short clipped sides,
medium nose bridge with a slightly wide tip, slightly full lips with corners naturally
turned down, light stubble on chin and upper lip,
coarse straight black hair (#151414), sides clipped short with a traditional
budget-barbershop clipper fade (visible step between sides and top, not a styled undercut),
about 4cm on top casually pushed to the right, the top flattened by a scooter helmet,
thin silver metal-framed glasses with roundish lenses, the left nose pad slightly bent, slipping down his nose,
thick knuckles, very short nails, a writing callus on the right middle finger,
a cheap black fitness band on the right wrist,

neutral expression with brows slightly drawn together and chin tucked,
looking at a phone or an object, not at the camera,

colour palette: security-sticker blue #3E6E8E, yellowed off-white #D9D4C7,
bamboo green-grey #6B7A5A, night black #2B2B2B,
with warm amber #F2B134 under 10% of the frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle from his left side so the eyebrow scar is visible,
wearing a faded grey university t-shirt with cracked unreadable print,
sitting at a small worn laminate desk pressed against a single bed in a rented room
at night, a warm desk lamp on one side and the glow of an old 24-inch monitor
on the other, a white power strip with a red pilot light visible at the edge of frame,
he is pushing his glasses up with his middle finger while looking at his phone,
shallow depth of field, slightly soft focus,

--ar 4:5
```

### 6.3 Full body(全身,機車,9:16)

```
[MASTER CHARACTER BLOCK]

full body, standing beside a dark grey 2016 125cc scooter with two scratches on the
body panel, parked in a narrow lane of old five-storey apartment buildings near a
night market district in Taichung, traditional Chinese characters on out-of-focus
shop signs, a self-service laundromat on the ground floor,
wearing a faded grey t-shirt, black basketball shorts and blue-and-white rubber slippers,
holding a white three-quarter helmet, a red amulet on his key ring,
late afternoon warm light, looking down at his phone,

--ar 9:16
```

### 6.4 Hands / detail(第二錨點的稀有特寫,一年最多一次,1:1)

```
photorealistic close-up phone photograph, cool fluorescent light, shallow depth of field,

close-up of a young man's hands with thick knuckles and very short nails peeling a small
blank blue rectangular security sticker off the rear camera of an older iPhone in a
yellowed clear case, the peeled area leaving a faint white "VOID" pattern residue,
a ring of old white adhesive residue around the camera bump,
a blue lanyard and a blank ID card holder lying beside the phone on a grey office desk,
no readable text on the lanyard or card, no brand logos, no faces,

--ar 1:1
```

### 6.5 The hand-me-down notebook(主錨點,1:1)

```
photorealistic top-down phone photograph, warm desk lamp light, slightly soft focus,

a small A6 grey paper notebook open on a worn wood-grain laminate desk, hand-ruled table
written in blue ballpoint pen with columns, the last column mostly empty for some rows
and ticked for others (no readable words, just the look of handwritten Chinese and numbers),
beside it the back of an older silver laptop with a half-peeled sticker of a crooked
oscilloscope cartoon and patchy adhesive residue,
a white three-port wall charger with a small blue LED, two plain USB-C cables,
a yellowed white six-outlet power strip with no switches partly visible on the floor edge,
no brand logos,

--ar 1:1
```

### 6.6 Desk at night / 桌子 B(4:5)

```
[MASTER CHARACTER BLOCK]

sitting with one foot up on the edge of a low second-hand office chair at a small
100x60cm wood-grain laminate desk pressed right against a single bed with grey sheets,
in a 4.5-ping rented room in an old Taichung apartment at 11pm,
an old silver laptop with a half-peeled sticker on its lid, a 24-inch monitor with
a small bright pixel, a cheap mechanical keyboard, a 7-Eleven-style mug,
a small grey notebook, a white three-port charger with a blue LED,
a yellowed white six-outlet power strip on the floor with cables tangled over it,
an electric rice cooker on the floor plugged into the wall instead,
five empty electronics boxes stacked on top of an old wardrobe,
warm desk lamp light and monitor glow, the bed close enough to touch the desk,
looking at his phone with his glasses slipping down,

--ar 4:5
```

### 6.7 Staff canteen / 員工餐廳(16:9)

```
[MASTER CHARACTER BLOCK]

wide shot in a large basement staff canteen of a tech company, long tables,
fluorescent light, he sits alone at the end of a table in a navy t-shirt with a
blank blue lanyard around his neck, a light blue anti-static jacket hanging on
the chair, a stainless steel tray with rice, two vegetables and a generous spoon
of braised minced pork sauce on top, he is scrolling his phone with one hand,
no readable signage, no logos,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in every
panel, head and shoulders, plain off-white wall background, glasses on:
1 neutral with brows slightly drawn and chin tucked,
2 calculating with eyes up to the left and lips moving silently,
3 a wide open real smile showing upper teeth with eyes squeezed into lines,
4 laughing while leaning back,
5 an awkward polite smile where the mouth smiles but the eyes do not,
6 genuinely pleased, eyebrows raised, lips pressed to hold back a grin,
7 squinting at a tiny label held 10cm from his face with glasses pushed up on his forehead,
8 tired, glasses off, pinching the bridge of his nose,
9 quiet and blank, looking into the distance,

--ar 1:1
```

### 6.9 Night ride / 夜騎(9:16)

```
[MASTER CHARACTER BLOCK]

seen from behind and slightly to the side, sitting on his parked scooter at a
roadside viewpoint on a hill at night, the city lights of Taichung spread below,
wearing a grey fleece jacket with pilled cuffs and a white three-quarter helmet
with an old action camera clipped on top,
the whole image has a faint blue haze as if shot through a translucent sticker,
cool night light, street lamp from one side,

--ar 9:16
```

### 6.10 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
whenever he picks up any electrical item he immediately flips it over to look at the
label on the back, pushes his glasses up onto his forehead and holds it about 10cm
from his face, squinting. he pushes slipping glasses back up with his middle finger.
when he sees a price his right index finger taps lightly on the desk as if pressing
a calculator. he sits with one foot on the edge of the low chair. he peels the blue
camera sticker off with his thumbnail from one corner and then looks at the residue.
he rarely gestures with his hands while talking. he glances at the camera briefly,
gives a slightly awkward smile and looks back at the object.

VOICE: male mid-range voice around 120 Hz, clean with a slight nasal quality,
Taiwanese Mandarin with a central-Taiwan accent, frequent "ei" at the start and
"la" at the end of sentences, natural Taiwanese Hokkien words mixed in,
speaks fast in general but slows down and pronounces numbers clearly,
voice-over around 210 Chinese characters per minute,
no influencer greeting, no sales tone, no broadcast energy.

CAMERA: handheld phone, eye level or top-down over the desk, practical light only,
no lab interiors, no readable company text.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 手臂短袖曬痕、臉頰比額頭深 | `06 § 四` 每天騎車、安全帽 | ✓ |
| 輕微小腹 | `06 § 七` 員工餐廳、一年胖四公斤 | ✓ |
| 痘疤 | `03 § 五` 研究所熬夜 | ✓ |
| 左耳上方髮際疤 | `02 § 11` 竹山竹林坡地 | ✓ |
| 百元快剪 | `06 § 八` 理髮 NT$200 | ✓ |
| NT$1,990 眼鏡套餐 | `02 § 10` 生活用品看價錢 | ✓ |
| 運動手環不是智慧錶 | `02 § 9` NT$990 運動手環 | ✓ |
| 褪色系服、表哥的刷毛外套 | `03 § 1-2` 接手的衣服 | ✓ |
| 白色新桌球鞋、新安全帽 | `02 § 7`「保護自己的東西要新的」 | ✓ |
| 防靜電外套 | `01 § 二` 實驗室規定 | ✓ |
| 手機後鏡頭殘膠 | `06 § 三` 保密貼紙每天貼 | ✓ |
| 一腳踩椅子邊 | `06 § 一` 二手椅子太低 | ✓ |
| 翻背面的動作 | `02 § 6` 職業反射、`03 § 8` 學會看標章 | ✓ |
| 幾乎不自拍 | `04 § 13` E 值一對一 35 | ✓ |
| 構圖普通、零後製 | `02 § 11` 不研究攝影 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.10 影片提示詞、五個不可變錨。**實驗室不入鏡。**
**Ivy(素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**
**特別注意:不得讓他出現在任何「工程師測試產品」的畫面裡**(見 `08 § 9.6`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| full_body | *(本輪未生圖)* | | | |
| hands_detail | *(本輪未生圖)* | | | |
| notebook | *(本輪未生圖)* | | | |
| desk_night | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖**(派工指令明寫「不生圖,seed 表留空」)。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.2 | 2026-10-20 | 跨人物撞型修正:外型拉開:國小二年級在竹林坡地摔的疤由左眉尾改到左耳上方髮際(快剪推短就露出來;左眉尾疤保留給 `persona_tw_06`);偏長方臉改國字臉(`02c`、`06` 是長方臉);黑色粗框方形眼鏡改銀色細金屬框(黑粗方框是 `persona_tw_03`);頭頂翹毛改為安全帽壓扁(翹毛是 `persona_tw_02b`) | 主 session 統一 QA:第二批平行生成,外型辨識點(眉疤、黑粗方框、翹毛)與配角名跟其他人物撞在一起 |

*檔案版本:v1.2 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
