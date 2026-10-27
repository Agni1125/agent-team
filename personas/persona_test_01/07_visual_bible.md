# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點 —— 最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   nate-sobczak
display_name:     Nathan "Nate" Sobczak

art_style:        photorealistic editorial photography
                  # 不是 CG、不是插畫、不是 3D。是照片。
style_reference:  natural-light documentary portraiture,
                  35mm / 50mm prime lens look, mild grain,
                  shallow but not creamy depth of field (f/2.8–f/4),
                  no beauty retouching, visible skin texture

color_palette:
  - "#1B2733"   # deep slate — 他的車、他的外套、夜間場景
  - "#C9CDD2"   # concrete grey — 停車場、辦公室、金屬
  - "#8A6A4B"   # worn leather tan — 皮帶、工作靴、玄關的碗
  - "#D64A2E"   # safety orange — 唯一的高彩度色,來自工廠 PPE。點綴用,不超過畫面 5%
  - "#E8E4DC"   # warm off-white — 牆、T 恤、紙箱

lighting_default: available light only.
                  室內走窗光 + 一盞暖色檯燈;
                  室外走德州的硬光或黃昏低角度。
                  **不用棚燈、不用環形燈、不用美肌補光。**

aspect_ratios:
  portrait:  4:5
  vertical:  9:16   # Threads / Reels
  square:    1:1
  wide:      16:9

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty retouch, flawless complexion,
male model, fashion model, chiseled jawline, six-pack abs,
gym physique, oiled skin, studio lighting, ring light, rim light,
teeth whitening, perfect symmetrical face, anime, illustration,
3d render, cgi, cartoon, oversaturated, HDR, teal-and-orange grade,
extra fingers, malformed hands, warped calipers, fake brand logos,
unreadable text, watermark, stock-photo smile, thumbs up,
crossed arms hero pose, luxury watch, designer clothing,
sports car, neon, cyberpunk, snow, tropical beach
```

**為什麼要排除這些(不是隨便列的):**
- `male model / gym physique / six-pack` — 他 34 歲、有椎間盤傷、不練硬舉了。健身模特身材違反 `03 § 10`。
- `luxury watch / designer clothing` — 他月收入對不上精品。違反 `02 § 3` 的階級行為設定。
- `sports car / neon / cyberpunk` — 這是最容易發生的漂移方向,一定要擋。
- `studio lighting / ring light` — 他不是內容創作者出身,他的畫面是隨手拍的。
- `stock-photo smile / thumbs up / crossed arms` — 圖庫感是這個人物的死敵。
- `snow / tropical beach` — 場景漂移。他在德州。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | Nathan "Nate" Sobczak |
| slug | `nate-sobczak` |
| age_appearance | **34–37**(比實際年齡看起來大一點點,因為髮線與眼下) |
| gender | 男 / cis |
| ethnicity | White,Eastern European descent(Polish-American),**中歐骨相** |
| build_class | mesomorph,有底子但已經軟化 |
| location_look | Central Texas,曬過但不是海灘曬 —— **前臂與後頸比上臂深兩個色階** |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | 方圓臉,下顎線有但被一點點軟組織蓋住。顴骨中等偏高 | 34 歲、坐辦公室、體重比 25 歲時多 6 kg |
| **膚色** | `#D9B396` 中性偏暖的淺褐,**德州曬痕明顯**:前臂與後頸比軀幹深 | 每天走去停車場、週末開車出城 |
| **膚質** | **有毛孔。有一點點油光。額頭有兩道淺橫紋,眉間有一道淺豎紋** | 反美肌。這是這個人物最重要的視覺特徵 |
| **眼睛** | 深棕色,眼型偏窄的杏眼,**眼下有淡淡的青灰色**(常態,不是疲勞) | 凌晨例會、六小時四十分的睡眠 |
| **眉毛** | 濃,自然,沒修過,眉尾略雜 | 他不做這件事 |
| **鼻子** | 直,鼻樑中等寬,鼻頭略圓。鼻樑左側有極輕微的偏(高中打球撞的,幾乎看不出來) | 不完美是必要的 |
| **嘴** | 中等厚度,**下唇比上唇明顯厚**。放鬆時嘴角略微下垂 —— 這讓他看起來像在思考,不是不高興 | |
| **牙齒** | 整齊但**不白**。左上第一小臼齒有一個舊的複合樹脂補綴 | 反 stock photo |
| **鬍子** | **三日鬍為預設狀態**。下巴與上唇密,兩頰稀。**鬍子裡有大約 8% 的白色** | 34 歲開始長白鬍是真的 |
| **表情基準** | **中性偏思考。不笑。** 眼睛專注,眉頭微微收 | 見 3.6 |

### 3.2 頭髮

- 深棕色(`#3A2E28`),接近黑但在陽光下明顯是棕色。
- **短髮,兩側 fade,但已經長超過三週該剪的時間** —— 側邊比 fade 該有的長度多出 5–8 mm。
  這條寫死,因為它是「這個人有生活但沒空」的視覺速記。
- 髮質偏硬、直,頂部有一點自然的分岔感。
- **髮線:兩側太陽穴已經開始後退(Norwood 2 到 2.5 之間)。他不遮,不梳過去,不戴帽子掩飾。**
  ← 這是刻意的長尾選擇。大部分 AI 生的 34 歲男性髮量完美,那是最快露餡的地方。
- 髮蠟:不用。洗完頭用毛巾擦一擦就出門。
- 太陽穴附近有零星白髮,不到 5%。

### 3.3 身體

- **身高 180 cm(5'11")。體重 81 kg(178 lb)。**
- 肩寬正常偏寬,背厚(划船機的結果),**腰腹有一層軟的** —— 不是胖,是 34 歲。
- **姿勢:站的時候重心會偏向右腳,左手常常插口袋。**
  坐的時候會不自覺往前傾,然後想起腰傷,把自己拉回來。
  ← 椎間盤傷的視覺後遺症,任何坐姿畫面都要有這個微調。
- 手:**大、乾、指節略粗。右手食指與拇指側面有薄繭(用工具的)。指甲短、平剪、乾淨但不修飾。**
  **手是這個人物最重要的身體部位,任何近景都要拍到。**
- 腿:一般。他不練腿。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **左前臂內側,距手腕約 12 cm,一道 3 cm 的白色線狀疤痕。** 縫過五針,痕跡略微凸起。
   2017 年在供應商工廠被沖壓鈑金邊緣割的。
   → **任何露出前臂的畫面都必須有。這是第一辨識點。**
2. **右手食指第二指節外側有一塊約 6 mm 的深色薄繭。**
3. **左耳垂有一個已經長合的耳洞疤痕**(19 歲打的,24 歲不戴了)。極細節,只在特寫出現。
4. 眉間那道豎紋 —— 他專注時會加深。

### 3.5 眼鏡(重要,因為它是狀態指示器)

- **Warby-Parker 風格的粗框,材質是啞光深橄欖綠玳瑁紋醋酸纖維,方圓框。**
  鏡片是抗藍光,度數很淺(-0.75 / -1.00)。
- **他只在看螢幕時戴。其他時間掛在頭頂或掛在 T 恤領口。**
- **狀態指示規則(給 Libai 與 Ivy):**

| 眼鏡在哪 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 戴著 | 工作中、專注、在讀東西 | 辦公室、拆解、螢幕前 |
| 掛在頭頂 | 剛從工作切換出來,被打斷 | 廚房、停車場、講話中 |
| 掛在領口 | 放鬆狀態 | 沙發、陽台、週末 |
| 完全沒有 | 運動、開車、剛起床 | 車內、健身、早晨 |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 中性,眉頭微收,嘴角略垂,眼睛專注 | 80% 的畫面 |
| **thinking** | 眉間豎紋加深,視線往左下,手摸下巴的鬍子 | 看到一個爛設計時 |
| **half-smile** | **只有右邊嘴角動,眼尾出現細紋。這是他的笑。** | 他最外露的正面情緒 |
| **actual laugh** | 頭往後仰一點,眼睛瞇成線,無聲。**極罕見,一年出現三次** | 只跟 Devin 或 Kass |
| **unimpressed** | 眉毛平,眼皮下垂一點點,完全沒有嘴部動作 | 看到行銷話術時 |
| **genuinely delighted** | 眉毛抬高,嘴巴微張,**這是他唯一會露出牙齒的表情** | 便宜東西做得意外好時 |
| **tired** | 眼下加深,肩膀塌,眼鏡在頭上,鬍子多一天 | 凌晨例會之後 |
| **irritated** | 下顎收緊,**不看鏡頭,看旁邊**。不皺眉 —— 他生氣時是收不是張 | 黏死的電池、供應商推責任 |
| **caught off guard** | 眉毛抬,嘴微開,身體往後一點 | 被姊姊戳破時 |

**❌ 絕對不出現的表情:** 誇張大笑、比讚、眨眼、驚訝到摀嘴、對鏡頭飛吻、
任何 stock photo 式的「開心的專業人士」。

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | 中低音,基頻約 **105–120 Hz**。不是低沉磁性,是普通男性偏低 |
| 語速 | **偏慢。約每分鐘 135 詞。** 講到技術細節時會加快到 165 |
| 口音 | **輕微的 Inland North / Great Lakes 腔** —— "bag" 的 a 音略前移,"about" 的 ou 略緊。**七年下來已經淡化,但沒消失** |
| 音色 | 乾,不共鳴,略帶氣音。**句尾會收掉,音量下降** |
| 特徵 | **句子之間停頓比一般人長 0.3–0.5 秒。** 他在想 |
| 笑聲 | 短促的鼻腔氣音,一次或兩次。**幾乎不出聲** |
| 填充詞 | "uh"(多)、"like"(少,他這年紀用得比 25 歲少)、"i mean"、"right?" |
| 情緒起伏 | **小。** 他興奮的時候只是講快一點,不是變大聲 |
| 絕不出現 | 播報腔、廣告腔、上揚的句尾、刻意的熱情、"Hey guys!" |

### 3.8 鏡頭前的肢體習慣

- **講話時右手會動,左手插口袋。** 右手的動作是描述性的 —— 他會用手比出尺寸。
- **拿東西一定翻過來看背面。** 這是他的招牌動作,任何開箱畫面必須有。
- **講到尺寸時會下意識用拇指跟食指比一個間距。** 這是這個人物最好認的肢體語言。
- 坐著會往前傾,然後想起腰,把自己拉正。
- 不確定的時候摸下巴的鬍子。
- **不看鏡頭。** 他看物件。要看鏡頭的時候是刻意的,而且短。
- **不用手勢強調重點。** 他靠停頓。

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **他不拍自拍。整個帳號的自拍數量:一年 0–2 張,而且是失焦或半張臉** |
| 出現在畫面裡的方式 | **手、前臂、肩膀、背影、鏡子裡的模糊倒影。臉極少出現** |
| 拍什麼 | **物件。90% 的照片是東西,不是人** |
| 構圖 | 不講究。**歪的、隨手的、光線不好的** |
| 後製 | **沒有。不套濾鏡,不調色,不裁切** |
| 器材 | **iPhone。** 那台 Fujifilm X100V 在抽屜裡,一年拿出來三次 |
| 什麼時候會有人拍他 | 朋友拍的、餐廳的鏡子、Devin 傳給他的、公司活動 |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「東西」與「手」,不是「臉」。**
> 需要臉的時候(影片口播、A+ 素材)才用完整人像。

---

## 四、服裝系統(三套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**啞鈴型消費 —— 鞋、外套、工具買好的;T 恤、褲子買便宜的。**

### 4.1 Work Outfit(平日進辦公室,週一到週四)

```
- 素色 crew-neck T 恤,Uniqlo 或 Gildan,US$12–22。
  顏色只有四種:炭灰、深藍、墨綠、米白。**沒有印刷,沒有 logo**
- Duluth Trading 或 Dickies 的工作長褲,卡其或深灰,US$45–60。
  **口袋有東西 —— 右後口袋有一支筆,右前口袋鼓一塊(那是卡尺)**
- 深棕色皮帶,已經有一道明顯的磨痕在習慣的那一格
- **Red Wing 或 Thorogood 的短筒工作靴,深褐色,US$220,穿了四年,鞋頭磨白**
  ← 這雙鞋是他消費哲學的視覺證據
- 公司識別證掛在腰帶上,不是掛脖子
- 手腕:Garmin Instinct 2,黑色,錶帶邊緣已經有點鬆
```

### 4.2 Weekend Outfit(週末 / 咖啡店 / 出城)

```
- 同樣的素 T,或一件洗到褪色的深藍色法蘭絨(袖子捲到手肘 —— **疤要露出來**)
- 深色直筒牛仔褲,Levi's 511,US$60,膝蓋已經有自然的白痕
- **On Cloud 5 跑鞋,灰色,US$140,已經穿到中底塌了一邊**
- 夏天:短褲(卡其,及膝上方 5 cm)+ 同樣的 T + 那雙 On Cloud
- 外套(十一月到二月):**一件炭灰色的軟殼外套,Patagonia Better Sweater 或類似,US$139,穿了六年**
- 帽子:**幾乎不戴。** 偶爾一頂沒有 logo 的深藍色棒球帽,只在正午出門時
```

### 4.3 Driving Outfit(開車 / 出城 / 車內畫面)

```
- 素 T + 短褲或牛仔褲(跟週末同套)
- **沒戴眼鏡**(開車不需要)
- 副駕上放著一件薄的長袖(德州冷氣的對策)
- 中控上放著手機,沒有支架
- **卡片鑰匙在杯架裡,上面掛著那個 1999 Ford Ranger 的鑰匙圈**
```

### 4.4 Factory Outfit(出差 / 工廠現場,一年三到五次)

```
- 短袖 polo(公司發的,左胸有小 logo)或素 T
- 同一條工作褲
- **安全鞋、安全眼鏡、耳塞掛在脖子上、白色或橘色安全帽**
  ← `#D64A2E` safety orange 在這裡合法出現
- 掛著訪客證
- 手上拿著筆記本或平板,以及卡尺
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **Garmin Instinct 2,黑色。不是 Apple Watch,不是機械錶,不是精品錶** |
| 眼鏡 | 啞光深橄欖綠方圓粗框(見 3.5) |
| 皮夾 | **深棕色雙折皮夾,用了九年,邊角磨圓,已經合不太起來** |
| 鑰匙 | Tesla 卡片鑰匙 + 1999 Ford Ranger 鑰匙圈 + 公寓鑰匙 + 一個開瓶器 |
| 背包 | 深灰色,兩年前買的,US$80,有一個側袋專門放卡尺 |
| 耳機 | Sony WH-1000XM4(**不是 5 代**),黑色,耳墊已經有一點點裂 |
| **不戴的** | 戒指、項鍊、手環、手鍊、耳環、任何珠寶。**一件都沒有** |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **左前臂 3 cm 白色疤痕** —— 露前臂就要有
2. **髮線後退到 Norwood 2–2.5,側邊比該剪的長** —— 不准長回來
3. **三日鬍,含 8% 白色** —— 不准變乾淨也不准變落腮鬍
4. **啞光深橄欖綠方圓框眼鏡** —— 換款式等於換人
5. **皮膚有毛孔、有油光、額頭兩道紋** —— 不准磨皮

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 男模 / 健身房身材 / 下顎線鋒利 | 違反年齡、腰傷、久坐設定 |
| 2 | 穿精品、戴名錶、開跑車 | 違反 `02 § 3` 收入與階級行為 |
| 3 | 髮量茂密、髮型精心打理 | 髮線是核心辨識點 |
| 4 | 棚拍打光、環形燈、色調濾鏡 | 他的畫面是隨手拍的 |
| 5 | 對鏡頭大笑、比讚、雙手抱胸 | 圖庫感 |
| 6 | 賽博龐克 / 霓虹 / 未來感場景 | 這是最容易發生的漂移 |
| 7 | 雪景、海灘、山區、歐洲街景 | 他在中德州 |
| 8 | 大量自拍、臉部特寫為主 | 他的帳號主體是物件不是臉 |
| 9 | 出現可辨識的真實品牌 logo 或人臉 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 左前臂疤痕在嗎(如果露出前臂)
- [ ] 髮線有沒有偷偷長回來
- [ ] 鬍子是不是三日長度
- [ ] 眼鏡是不是那副,而且位置符合狀態規則
- [ ] 皮膚有沒有被磨皮
- [ ] 有沒有出現不該有的珠寶或名牌
- [ ] 場景是不是德州
- [ ] 色板有沒有跑掉(`#D64A2E` 佔比是否 ≤5%)
- [ ] 手有沒有畫壞
- [ ] 有沒有出現假 logo 或無法辨識的文字

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic editorial photograph, natural available light, 35mm lens,
mild film grain, no retouching, visible skin texture and pores,

a 34-year-old white American man of Eastern European descent,
180cm, 81kg, mesomorph build gone slightly soft around the midsection,
square-oval face with a jawline softened by a little weight,
deep brown narrow almond eyes with faint blue-grey shadows underneath,
thick unshaped dark eyebrows, straight medium-wide nose,
lower lip fuller than upper, resting mouth corners turned slightly down,
three-day stubble with roughly eight percent grey hairs,
short dark brown hair (#3A2E28) with grown-out faded sides,
receding at the temples (Norwood 2.5), a few grey hairs at the temples,
two faint horizontal forehead lines and one vertical crease between the brows,
sun-weathered forearms and back of neck two shades darker than his torso,
large dry hands, short flat-cut nails, a small callus on the right index knuckle,
a 3cm thin white surgical scar on the inner left forearm 12cm above the wrist,

neutral thoughtful expression, not smiling, looking at an object not the camera,

colour palette: deep slate #1B2733, concrete grey #C9CDD2,
worn leather tan #8A6A4B, warm off-white #E8E4DC,
with a small accent of safety orange #D64A2E covering under 5% of frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, slightly turned away from camera,
matte dark olive tortoiseshell square acetate glasses pushed up on his head,
plain charcoal crew-neck cotton t-shirt, no print, no logo,
standing in a garage-level parking structure, concrete columns behind him,
overhead fluorescent light mixed with daylight spilling from a ramp,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,工作日,9:16)

```
[MASTER CHARACTER BLOCK]

full body standing, weight shifted onto his right leg, left hand in pocket,
plain dark navy crew-neck t-shirt, charcoal work trousers with a pen in the
right back pocket and a rectangular bulge in the right front pocket,
dark brown leather belt worn into one hole, dark brown leather work boots
with scuffed toecaps, black rugged GPS watch on left wrist,
matte dark olive glasses hanging from his shirt collar,
standing in a hardware lab: metal workbench, plastic sample parts,
a small parts bin, an anti-static mat, one warm desk lamp,
daylight from a high window camera-left,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic macro-leaning product photograph, natural window light,
50mm lens, shallow depth of field,

close-up of a 34-year-old man's large dry working hands holding a
6-inch digital vernier caliper, measuring the seam gap on a matte plastic
consumer product housing, the caliper's stainless beam has a fine scratch
near the 3-inch mark, short flat-cut fingernails, a small callus on the
right index knuckle, the edge of a 3cm white scar visible on the inner
left forearm at the top of the frame, sleeve rolled to the elbow,

worn wooden table, a set of keys just out of focus in the background
with an old faded truck keyring on it,
warm off-white and concrete grey tones, no faces, no text,

--ar 1:1
```

### 6.5 Driving / in-car(9:16)

```
[MASTER CHARACTER BLOCK]

seated in the driver's seat of a dark blue electric sedan with a black
minimalist interior and a single centre touchscreen, no glasses,
plain dark green crew-neck t-shirt, left hand at the bottom of the steering
wheel, right forearm resting on the centre console showing the white scar,
looking out of the windshield not at the camera,
a card key sitting in the cupholder with a battered old truck keyring on it,
late afternoon Texas sun coming in low from the left, hard light,
dust visible on the dashboard, one empty coffee cup in the door pocket,
shot from the passenger seat,

--ar 9:16
```

### 6.6 Kitchen / weekend(4:5)

```
[MASTER CHARACTER BLOCK]

standing at a small apartment kitchen counter making pour-over coffee,
faded dark blue flannel shirt with sleeves rolled to the elbow showing
the white forearm scar, matte dark olive glasses hanging from the collar,
white burr grinder with dried coffee residue on its base,
a cream ceramic pour-over dripper with a hairline crack in the handle,
a cheap digital thermometer, a bottle of hot sauce beside the sink,
morning light through a west-facing window, faux-quartz laminate counter,
two cardboard boxes half-opened on the floor behind him,
looking down at the kettle, not at the camera,

--ar 4:5
```

### 6.7 Factory / travel(16:9)

```
[MASTER CHARACTER BLOCK]

standing on a factory floor beside an injection moulding machine,
short-sleeve navy polo, charcoal work trousers, steel-toe safety shoes,
clear safety glasses, orange hard hat, foam earplugs hanging around his neck,
a visitor badge clipped to his collar, holding a caliper in his right hand
and a small plastic part in his left, examining the part, not the camera,
industrial overhead lighting mixed with daylight from high windows,
racks of grey plastic bins in the background, safety orange floor markings,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing
in every panel, head and shoulders, plain warm off-white background:
1 neutral thoughtful, 2 concentrating with the brow crease deepened,
3 a half-smile using only the right corner of the mouth,
4 a silent laugh with head tipped back and eyes narrowed to lines,
5 unimpressed with flat eyebrows and no mouth movement,
6 genuinely delighted with eyebrows raised and teeth showing,
7 tired with deeper under-eye shadows and slumped shoulders,
8 irritated with a tightened jaw looking off to the side,
9 caught off guard with raised eyebrows and mouth slightly open,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
he picks up an object and immediately turns it over to look at the back
before saying anything. he speaks slowly, about 135 words per minute,
with pauses of half a second between sentences. his right hand moves while
he talks; his left stays in his pocket. when he describes a dimension he
unconsciously holds his thumb and index finger apart to show the size.
he does not look at the camera; he looks at the object in his hands.
he does not gesture for emphasis. he leans forward when seated and then
corrects his posture. when something pleases him only the right corner of
his mouth moves.

VOICE: mid-low male voice, fundamental around 110 Hz, dry, slightly breathy,
sentence endings drop in volume, faint Great Lakes vowel colouring,
no broadcast energy, no sales tone, no rising terminals.

CAMERA: handheld, slight natural drift, 35mm, eye level or slightly below,
available light only.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 眼下青灰、睡眠不足 | `06` 凌晨 1:30 例會 | ✓ |
| 前臂比軀幹深兩階 | `06` 每天走停車場 + 週末開車出城 | ✓ |
| 髮線後退、側邊過長 | 34 歲 + `04` 私生活 C 值 52 | ✓ |
| 三日鬍含白 | 34 歲 | ✓ |
| 左前臂疤 | `03` 2017 年工廠事故 | ✓ |
| 手上的繭 | `02 § 11` 修東西、用工具 | ✓ |
| 坐姿會前傾再修正 | `03` 2024 椎間盤突出 | ✓ |
| 背厚但腰腹軟 | `06` 划船機 + 沒練腿 + 34 歲 | ✓ |
| 沒有六塊肌 | `03` 腰傷後停硬舉 | ✓ |
| US$18 的 T 恤 + US$220 的靴子 | `02 § 10` 啞鈴型消費 | ✓ |
| Garmin 不是 Apple Watch | `02 § 9` 電池 + 不想被通知追殺 | ✓ |
| 沒有任何珠寶 | `02` 全檔沒有裝飾性消費 | ✓ |
| Sony XM4 不是 XM5 | `02 § 9` 「5 代頭帶做爛了」 | ✓ |
| 幾乎不拍自拍 | `04 § 13` Extraversion 42 | ✓ |
| 不看鏡頭 | `04 § 12` 社會面具 —— 他看物件 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.9 影片提示詞、五個不可變錨。
**Ivy(Amazon 素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(待生成)* | | | |
| full_body | *(待生成)* | | | |
| hands_detail | *(待生成)* | | | |
| in_car | *(待生成)* | | | |
| expression_sheet | *(待生成)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,不是圖。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---

*檔案版本:v1.0 — 2026-09-10 建立*
