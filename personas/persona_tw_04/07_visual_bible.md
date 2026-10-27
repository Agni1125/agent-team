# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人,而且放在同一張胡桃木桌前。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   chih-ning-ho
display_name:     何芷寧 Ho Chih-Ning(Ning)

art_style:        photorealistic editorial documentary photography
                  # 不是 CG、不是插畫、不是韓系網美照、不是極簡白色圖庫。是照片。
style_reference:  quiet natural-light interior and still-life photography,
                  35mm or 50mm look, very mild grain, accurate white balance,
                  orthogonal compositions (objects squared to the frame, top-down flat lays aligned),
                  late-afternoon window light, no beauty retouching, visible skin texture,
                  East Asian skin rendered true

color_palette:
  - "#5C3B28"   # walnut — 家裡那張胡桃木桌,畫面的主色
  - "#D8CFC0"   # oatmeal — 她的衣服、帆布、牆
  - "#B9B4AA"   # terrazzo grey — 磨石子底色、老屋的水泥、工作室樓梯
  - "#1B1B1D"   # ink black — 提案日的外套、霧黑的金屬、iPad 支架
  - "#B08D57"   # brushed brass — 檯燈、尺、戒指。點綴用,不超過畫面 6%
  - "#3D7BFF"   # cheap blue LED — **只在講那個盒子的畫面出現,而且只能是一兩個小點**

lighting_default: natural window light first.
                  家裡:西南向的午後窗光 + 黃銅檯燈的暖光(2700K 左右);
                  工作室:北向窗的平光 + 螢幕;
                  老屋:陰天或側光,看得到材質的起伏。
                  **不用環形燈、不用美肌補光、不用韓系柔焦、不用過曝的白色極簡光。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok、Reels
  square:    1:1     # 材質特寫、那張卡
  wide:      16:9    # 工作室全景

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty filter, porcelain white skin, glass skin,
k-pop idol, korean ulzzang makeup, big doe eyes, v-shaped face, tiny face,
heavy contour, glossy lips, false eyelashes, coloured contacts,
bangs, fringe, long hair, wavy hair, curly hair, dyed hair, highlights,
eyeglasses, round glasses,
influencer pose, peace sign, hand on chin pose,
all-white minimalist room, white desk, white marble, scandinavian showroom,
cafe latte art, dried flower arrangement, pastel aesthetic, soft focus glow,
ring light catchlight, studio beauty lighting, teal-and-orange grade,
RGB lighting, neon, gaming setup, glowing blue LEDs everywhere,
anime, illustration, 3d render, cgi, doll-like, overly slim, model physique,
designer handbag, visible luxury logos, luxury jewelry, long manicured nails, nail art,
fake brand logos, unreadable chinese characters, garbled text, watermark,
simplified chinese signage, mainland china street, japanese street signs,
extra fingers, malformed hands, warped cables, melted objects, floating objects
```

**為什麼要排除這些(不是隨便列的):**
- `k-pop idol / ulzzang / v-shaped face / big doe eyes` — AI 生「亞洲女性」最常滑過去的方向。她是太平長大的工業設計系畢業生。
- `bangs / long hair / wavy hair / dyed hair` — **她的齊下巴短髮沒有瀏海,是五個不可變錨之一。** AI 很喜歡給東亞女性加瀏海。
- `eyeglasses / round glasses` — **她平常不戴眼鏡。** 這是她跟其他台灣人物在視覺上最明顯的區別之一。
- `all-white minimalist room / white desk / scandinavian showroom` — **她的桌子是胡桃木,不是白色極簡。** 違反 `04 § 16`。
- `RGB lighting / neon / glowing blue LEDs everywhere` — 她對藍光有生理級的反感(`03 § 4-1`)。藍光只能是盒子縫裡的一兩點。
- `designer handbag / visible luxury logos` — 違反 `02 § 10`:她會因為 logo 太大而不買。
- `simplified chinese signage / japanese street signs` — **場景漂移。她在台中。** 招牌要是繁體中文,或乾脆不出現文字。
- `warped cables / melted objects` — 她的畫面常有線、磨石子、黃銅,AI 很容易畫壞。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 何芷寧(Ning) |
| slug | `chih-ning-ho` |
| age_appearance | **33–36**(看起來精神,但眼角有細紋,不顯年輕也不顯老) |
| gender | 女 / she-her |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 中等身高、偏瘦但有肩膀。**游泳兩年,肩膀比一般辦公室女性寬一點** |
| location_look | 台中、走路上班:**鼻樑上有一點淡淡的雀斑**,秋天皮膚偏乾 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **長橢圓臉**,顴骨略高,兩頰平,下顎線清楚但不尖 | 反 V 臉,也跟圓臉的人物拉開 |
| **膚色** | `#DCC0A3` 中性偏冷的淺小麥色。**不白,也不黃。** 秋天兩頰與鼻翼偏乾 | 台中乾燥、走路曬 |
| **膚質** | **有毛孔,鼻樑上有一片淡淡的雀斑**,眼角有細紋 | 反美肌 |
| **眼睛** | 深棕色,**細長的窄雙眼皮**(眼皺很細、平行型),眼尾平,不上揚也不下垂 | 看東西時會微微瞇起 |
| **眉毛** | **平直、偏細**,眉頭與眉尾幾乎一樣高。她會修,形狀很穩定 | 「一條直線」是她的審美 |
| **鼻子** | 鼻樑中等,鼻頭窄 | |
| **嘴** | 嘴型偏寬,**上唇薄、下唇略厚**,常態閉著 | |
| **表情基準** | **評估中:頭微微偏一邊,眼睛稍瞇,嘴唇閉著。** 不笑的時候看起來很冷靜,不兇 | 見 3.6 |

### 3.2 頭髮

- 黑色(`#1A1716`),**自然黑帶一點深棕**,游泳後髮尾有點乾。沒染過。
- **齊下巴的鮑伯短髮,髮尾是一條直線,沒有瀏海**,額頭露出來,左側分線。
  **每六週剪一次,所以長度幾乎永遠一樣。** ← 這條寫死,它是「一致」的視覺速記。
- 狀態指示(寫死):

| 頭髮怎麼弄 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| **右邊塞在耳後** | 工作中、在看東西 | 桌前、工作室、實體店 |
| 一支霧黑金屬小髮夾夾住右邊 | 畫圖中、專注 | 家裡桌前、深夜 |
| 濕的、往後梳 | 游泳完 | 早上、週二週五 |
| 放下、被風吹 | 走路、拍老屋 | 綠園道、老街 |

- **不要畫成有瀏海、不要畫成長髮、不要捲。**

### 3.3 身體

- **身高 163 cm。體重 52 kg。**
- 肩膀比一般辦公室女性寬一點(游泳),**脖子長,站姿直**。
- 手:**中等大小,手指長,指節不粗,指甲剪短、沒有塗。**
  **左手拇指根部一道白色細疤(約 1.5 公分,2012 年美工刀)。**
  **左手中指一枚細的霧面黃銅戒指。**
  **手是這個人物最重要的身體部位之一:摸邊、翻底部、拿那張卡,都是手。**
- 右手腕偶爾有一點紅,畫圖太久。**不要畫護腕。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **齊下巴、無瀏海、髮尾一條直線的黑色短髮。** 任何正臉或側臉都必須是這個髮型。**第一辨識點。**
2. **鼻樑上的淡雀斑。** 近景與半身必須有,不要被磨掉。
3. **左手拇指的白色細疤 + 左手中指的黃銅細戒。** 手部特寫的辨識點。
4. **右耳耳骨一顆極小的霧銀耳釘,兩邊耳垂各一根短的霧銀細條耳環。**
5. **左手腕的 Apple Watch,燕麥色編織錶帶。**

### 3.5 眼鏡

- **平常不戴。** 輕度近視約 -1.50,開車與看電影才戴(黑色細框方形,但**任何內容都不出現**)。
- ← 寫死:這個人物的生圖一律**不戴眼鏡**。

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(評估中)** | 頭微偏,眼睛稍瞇,嘴唇閉著,看著物件 | 70% 的畫面 |
| **tracing** | 低頭,眼睛跟著拇指沿邊移動 | 摸邊時 |
| **real smile** | **閉嘴笑,右邊嘴角比左邊高一點**,眼睛彎起來 | 一個便宜的東西收邊很好、跟承翊鬥嘴 |
| **laugh** | 頭往後仰一點,鼻子短短出一口氣,手背遮一下嘴 | 自己的錯被講出來 |
| **unimpressed** | 眉毛不動,嘴角往下壓一點點,看向別處 | 「屬正常色差範圍」 |
| **genuinely pleased** | 眉毛抬起,嘴巴微張,把東西舉近一點看 | 好的收邊、老屋的好材質 |
| **tired** | 閉眼,用兩根手指按眉心 | 擴編的會議之後 |
| **comparing** | **一手拿產品、一手拿那張卡,兩個並排,眼睛在兩者之間來回** | 實體店、退貨 |
| **squaring** | **低頭,用指尖把桌上一個東西推到跟桌緣平行** | 壓力訊號 |

**❌ 絕對不出現的表情:** 比 YA、嘟嘴、歪頭裝可愛、對鏡頭眨眼、手托下巴的網美姿勢、
「看遠方微笑」、任何韓系或日系的偶像表情。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中音**,基頻約 **200–220 Hz**。不嗲、不尖 |
| 語速 | **畫外音約每分鐘 170 字;提案時約 190 字。** 比一般創作者慢 |
| 口音 | **台中長大的標準國語**,幾乎聽不出地區;跟媽媽講話時台語的語尾會出來 |
| 音色 | 乾淨、略低,句尾收得很穩 |
| 特徵 | **名詞前會停半拍**:「這個⋯⋯收邊」「它的⋯⋯分模線」。**句子完整,很少省略主詞** |
| 台語 | 很少。偶爾「袂穤」(還不錯)、「歹勢」。**不刻意,不當笑點** |
| 笑聲 | 鼻子短短出一口氣,或一聲很輕的「哈」 |
| 填充詞 | 「嗯」(思考)、「對」(確認)、「就是」(少) |
| 情緒起伏 | **低到中。** 好的東西會讓她語速變慢、聲音變輕,不是變快 |
| 絕不出現 | 「哈囉大家好」「寶寶們」「家人們」、播報腔、嗲聲、網紅式上揚尾音、中國腔兒化音 |

### 3.8 鏡頭前的肢體習慣

- **拿起任何東西:先翻到底部,再用右手拇指沿著邊緣摸一圈。** 招牌動作。
- **把東西轉正。** 桌上的物件會被她用指尖推到跟桌緣平行。
- **拿著東西對著光斜一下**,看表面的反光與霧面的均勻度。
- **從手機殼背面抽出那張卡**,貼在產品旁邊比顏色。
- 想事情時用 Apple Pencil 的尾端**在 iPad 邊框上輕點兩下**。
- 站著時重心在一隻腳,雙手交叉抓著對側的手肘。
- **她看鏡頭的時間很短。** 她會看物件,看鏡頭一秒,再看回物件。

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎沒有。** 一年不到五張,通常是旅行時店家的鏡子裡 |
| 出現在畫面裡的方式 | **手、手腕、側背影、窗戶反射。** TikTok 約 10–15% 露臉(側臉,在畫圖) |
| 拍什麼 | **材質與收邊。** 老屋的磨石子、鐵窗花、接縫、轉角;桌上的物件;工具 |
| 構圖 | **正交、對稱、俯拍時所有物件轉正。** 她的照片有一種「被整理過」的感覺,她自己知道 |
| 光線 | **自然光,選時間。** 她會為了一張磨石子等下午三點的側光 |
| 後製 | **只校白平衡與曝光**,讓材質是它本來的顏色。不加濾鏡、不調色風格 |
| 器材 | 老屋用那台富士定焦機;日常用 iPhone |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「材質、收邊、手、桌面」,臉幾乎不出現。**
> 需要臉的時候(TikTok 少量、商業素材)才用完整人像,而且臉要符合第五節的不可變錨。
> **構圖要準,光要對。** 她跟網美的差別不在光好不好看,在**每一張都看得出她在看什麼**。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**每天會摸到的東西可以貴(桌子、包、筆),身上穿的是少而耐穿、沒有大 logo 的。**

### 4.1 Studio Day(工作室日常)

```
- 燕麥色寬版棉麻襯衫,袖子捲到手肘,最上面一顆扣子開著
- 炭灰色寬褲,九分
- 白色皮革休閒鞋(她會擦,所以很乾淨)
- Apple Watch,燕麥色編織錶帶
- 頭髮右邊塞在耳後
- 灰綠帆布托特包掛在椅背
← 顏色永遠只有兩到三種,而且一定有一個是燕麥或炭灰
```

### 4.2 Client Day(提案日)

```
- 墨黑色寬版西裝外套(二手,日本品牌,沒有外露 logo)
- 裡面白色或燕麥色素 T
- 黑色直筒西裝褲
- 黑色樂福鞋
- 頭髮放下,右邊塞耳後
- 防曬、眉筆、一支豆沙色的潤色護唇膏。這是她的全妝
```

### 4.3 Weekend / 老屋(週六拍老屋)

```
- 炭灰色工作外套(2025 年東京買的,棉質,四個口袋)
- 灰色素 T
- 卡其色工作褲
- 黑色帆布鞋
- 富士定焦機用手腕帶掛在右手
- 灰綠帆布托特包
- 頭髮放下,被風吹
```

### 4.4 Factory Day(工具機廠現場)

```
- 深灰色長袖 T
- 黑色長褲
- 黑色包鞋(工廠規定不能露腳趾)
- 頭髮用霧黑金屬髮夾夾起來
- 一副工廠給的手套(她戴著按觸控螢幕)
- iPad 放在一個防摔殼裡
← 這一套是她在社群上唯一會出現「工作現場」的樣子,但工廠與機台永遠不露標誌
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **Apple Watch,燕麥色編織錶帶** |
| 戒指 | **左手中指一枚細的霧面黃銅戒指**(朋友的工作室做的) |
| 耳環 | **兩邊耳垂各一根短的霧銀細條;右耳耳骨一顆極小霧銀耳釘** |
| 包 | **灰綠色帆布托特包**(台南老帆布行),底部一圈磨白 |
| 手機殼 | **透明,背面夾著那張卡與悠遊卡** |
| 髮具 | 一支霧黑金屬小髮夾 |
| 小物 | 托特包裡一支不鏽鋼湯匙、一把十五公分黃銅尺 |
| **不戴的** | 項鍊、手鍊、名牌包、美甲、大耳環、眼鏡、任何 logo 很大的東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **齊下巴、無瀏海、髮尾一條直線的黑色短髮,左側分線**,不准有瀏海、不准變長、不准捲、不准染
2. **長橢圓臉、平直細眉、細長窄雙眼皮**,不准變 V 臉、不准變大眼、不准變單眼皮圓臉
3. **鼻樑上的淡雀斑 + 有毛孔的中性淺小麥膚色**,不准磨皮、不准美白
4. **不戴眼鏡**,任何畫面都不戴
5. **左手拇指的白色細疤 + 左手中指的黃銅細戒**(手部畫面)

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系網美 / 偶像臉 / V 臉大眼 | 違反人物出身與職業,也是 AI 最容易滑過去的方向 |
| 2 | 白色極簡房間、白色桌子、大理石 | **她的桌子是胡桃木**,她的世界是木頭、磨石子、黃銅、墨黑 |
| 3 | 瀏海、長髮、捲髮 | 違反第一辨識點 |
| 4 | 戴眼鏡 | 她不戴 |
| 5 | 精緻全妝、美甲、名牌包 | 違反 `02 § 10` 與 4.2 的「全妝」定義 |
| 6 | 咖啡廳擺拍、乾燥花、粉彩色調 | 「質感生活」漂移,違反 `04 § 16` |
| 7 | RGB、霓虹、滿屋子的藍光 | 她對藍光有生理級反感。**藍光只能是盒子縫裡一兩點** |
| 8 | 簡體字招牌、中國或日本街景 | **她在台中**,招牌是繁體 |
| 9 | 乾淨無線的桌面(在家裡那張的「沙發視角」) | **家裡那張從沙發看得到盒子的縫**;俯拍的桌面可以乾淨,沙發視角不行 |
| 10 | 出現可辨識的真實品牌 logo 或真人臉 | 法遵 |

### 連續性檢查表(每次出圖後跑)

- [ ] 頭髮是齊下巴、無瀏海、直線髮尾嗎
- [ ] 有沒有戴眼鏡(不應該有)
- [ ] 是長橢圓臉、平直細眉、窄雙眼皮嗎,有沒有被修成 V 臉大眼
- [ ] 鼻樑的雀斑在嗎(近景)
- [ ] 皮膚有沒有被磨皮或美白
- [ ] 手部:左手拇指的疤、左手中指的黃銅戒在嗎
- [ ] 桌子是胡桃木嗎,有沒有變成白色桌子
- [ ] 色板有沒有跑掉(`#3D7BFF` 藍光是不是只有一兩個小點,或者根本沒有)
- [ ] 手有沒有畫壞,線、磨石子、黃銅有沒有變形
- [ ] 有沒有出現亂碼中文、假 logo、名牌

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic editorial documentary photograph, natural window light,
50mm lens, very mild grain, accurate white balance, no retouching,
visible skin texture and pores,

a 34-year-old Taiwanese woman, 163cm, slim with slightly broad swimmer's shoulders,
long neck, upright posture,
long oval face with slightly high cheekbones and flat cheeks, clean jawline,
narrow dark brown eyes with thin parallel double eyelids, level outer corners,
straight thin eyebrows, medium nose bridge with a narrow tip,
wide mouth with a thin upper lip and slightly fuller lower lip, lips closed,
neutral light tan skin (#DCC0A3), faint freckles across the bridge of the nose,
fine lines at the outer corners of the eyes, slightly dry skin around the nose,
chin-length blunt bob of natural black hair (#1A1716) with a perfectly straight hem,
no bangs, forehead visible, side part on the left, right side tucked behind the ear,
no glasses,
long fingers with short unpainted nails, a thin white scar at the base of the left thumb,
a thin brushed brass ring on the left middle finger,
short matte silver bar earrings, a tiny matte silver stud on the right ear helix,
an Apple-style smartwatch with an oatmeal woven band on the left wrist,

calm evaluating expression, head tilted slightly, eyes slightly narrowed,
looking at an object, not at the camera,

colour palette: walnut #5C3B28, oatmeal #D8CFC0, terrazzo grey #B9B4AA,
ink black #1B1B1D, with brushed brass #B08D57 under 6% of the frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, slightly turned away from camera,
oatmeal linen shirt with the top button open, sleeves rolled,
sitting at a solid walnut desk in a late-afternoon living room,
warm window light from the left, a brass desk lamp out of focus behind her,
holding an object close to her face and looking at its edge,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,老屋,9:16)

```
[MASTER CHARACTER BLOCK]

full body, standing on the landing of a 1970s Taiwanese townhouse staircase
with grey terrazzo steps divided by thin brass strips and an old painted iron handrail,
wearing a charcoal cotton chore jacket over a grey t-shirt, khaki work trousers,
black canvas shoes, a compact fixed-lens camera hanging from her right wrist by a strap,
a grey-green heavy canvas tote bag on her shoulder,
looking down at the edge of a step, overcast side light from a window,
terrazzo texture clearly visible,

--ar 9:16
```

### 6.4 Hands / detail(主錨點:那張卡,1:1)

```
photorealistic close-up still-life photograph, soft natural window light,
50mm macro, shallow depth of field, accurate white balance,

close-up of a woman's hands with long fingers and short unpainted nails,
a thin white scar at the base of the left thumb and a thin brushed brass ring
on the left middle finger, holding a small 2 x 9 cm handmade paper colour strip
with five slightly different white swatches, each labelled in tiny handwriting,
next to the white edge of a small electronic charger on a walnut desk,
two whites side by side that do not quite match,
no faces, no brand logos, no readable text on the product,

--ar 1:1
```

### 6.5 Desk at night / 桌子 A 的「沙發視角」(4:5)

```
photorealistic documentary interior photograph, evening, 35mm lens,
viewed from a sofa in a 1990s Taiwanese apartment living room,

a solid walnut desk against a window wall, a 13-inch tablet on a folding aluminium stand,
a palm-sized piece of grey terrazzo with a brass strip used as a paperweight,
a half-sphere brass desk lamp casting warm light,
a white charging cable hanging from the edge of the desk down to the floor,
on the floor under the desk a light hinoki wood cable box with its lid resting
at an angle, a narrow gap along one side, and one or two tiny blue pilot lights
glowing through the gap,
a white self-adhesive cable channel running along a beige wall to the sofa,
no person in frame,

--ar 4:5
```

### 6.6 Desk top-down / 桌子 A 的俯拍(她自己會拍的那一面,1:1)

```
photorealistic top-down still-life photograph, late-afternoon window light,
all objects squared to the frame and aligned with the desk edge,

a solid walnut desk surface with a slightly worn edge,
a 13-inch tablet with a stylus wrapped in a matte grey silicone grip,
a palm-sized piece of grey terrazzo with a brass strip,
a 15 cm brass ruler, a stack of square grid sticky notes,
a plastic cup of iced black tea from a market stall,
a woman's left hand entering the frame, pushing the ruler parallel to the desk edge,
no cables visible on the desk surface,

--ar 1:1
```

### 6.7 Studio / 工作室(16:9)

```
[MASTER CHARACTER BLOCK]

wide shot of the second floor of a renovated 1970s Taichung townhouse used as a
small design studio, seven identical desks with white oak tops and black square-steel legs
in rows, she sits at the desk nearest the window,
a 27-inch monitor, a closed laptop on a stand, a tablet in front of her, drawing,
a small black clip holding the tablet's charging cable behind the stand,
a metal mesh basket under the desk holding a white power strip,
north window light, grey terrazzo floor, other desks blurred,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same woman, identical lighting and framing in every panel,
head and shoulders, plain oatmeal background, no glasses, chin-length bob with no bangs:
1 calm evaluating look with head slightly tilted,
2 looking down, eyes following her thumb along an object's edge,
3 a closed-mouth smile with the right corner higher than the left,
4 a short laugh with head tipped back slightly and the back of a hand near her mouth,
5 unimpressed, eyebrows still, mouth corners pressed down slightly, looking away,
6 genuinely pleased, eyebrows raised, lips slightly parted, holding an object closer,
7 tired, eyes closed, two fingertips pressed between the eyebrows,
8 comparing, eyes moving between an object in one hand and a small paper colour strip in the other,
9 looking down, a fingertip pushing an object square to the desk edge,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
when she picks up any object she first turns it over to look at the bottom, then runs
her right thumb slowly along the edge all the way around. she tilts objects against
the window light to check the surface. she pulls a small paper colour strip out from
behind her clear phone case and holds it beside a product to compare whites.
when stressed she uses a fingertip to push objects on the desk until they are parallel
to the edge. while thinking she taps the end of her stylus twice on the tablet bezel.
she stands with her weight on one leg, arms crossed, holding the opposite elbows.
she glances at the camera for about one second and returns her eyes to the object.

VOICE: mid-range female voice, fundamental around 210 Hz, clean and slightly low,
standard Taiwanese Mandarin raised in Taichung, unhurried, around 170 Chinese characters
per minute for voice-over, a half-beat pause before nouns, complete sentences,
no influencer greeting, no cutesy tone, no broadcast energy, no rising terminals.

CAMERA: locked-off on a small tripod or top-down over the walnut desk, 35mm or 50mm,
natural window light, orthogonal framing.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 齊下巴短髮、每六週剪一次 | `04 § 1` 一致;`03 § 5-2` 數有幾種 | ✓ |
| 肩膀寬一點 | `06 § 六` 每週游泳兩次 | ✓ |
| 鼻樑雀斑、皮膚偏乾 | `06 § 三` 每天走路;`01 § 四` 台中乾燥 | ✓ |
| 左手拇指的疤 | `03 § 3-1` 2012 美工刀 | ✓ |
| 不戴眼鏡 | `06 § 六` 輕度近視 -1.50 | ✓ |
| 指甲短、不塗 | `02 § 6` 每天用 Pencil 與觸控 | ✓ |
| 衣服少而耐穿、沒有大 logo | `02 § 10` 「每天會摸到的才值得貴」、logo 扣分 | ✓ |
| 二手日本外套、東京工作外套 | `02 § 2` 每次出國都去道具街與五金行;`03 § 11-2025` | ✓ |
| 帆布托特包 | `06 § 一` 道具 9 | ✓ |
| Apple Watch | `02 § 9` 游泳計趟 | ✓ |
| 黃銅戒指、黃銅尺、黃銅燈 | `06 § 一` 道具;她喜歡會隨時間變色的金屬 | ✓ |
| 構圖正交、只校白平衡 | `04 § 8` 把東西轉正;`03 § 7-4` 顏色要準 | ✓ |
| 很少自拍 | `04 § 13` 私下 E 值 35 | ✓ |
| 藍光只在盒子縫裡 | `03 § 4-1`、`03 § 7-3` | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.9 影片提示詞、五個不可變錨。
**Ivy(素材):** 讀 6.1 master block、6.4 那張卡的手部鏡頭、6.5 沙發視角、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**
**6.5 的「沙發視角」只能用在她自己講那個盒子的內容裡,不能被剪成任何產品的「使用前」畫面。**
**v1.1(2026-10-20):** 盒子與藍光的畫面**到桌下托架裝好(約 12 月)之前照舊**。之後的沙發視角是一片胡桃木擋板,桌面零充電物件,藍光是否還看得到「她自己也不知道」,**生圖時不要自行決定有或沒有,先回報 Gaia**。托架是木作,不得畫成任何充電產品,也不得被當成產品的「使用後」畫面(`03 § 7-6`、`06 § 一`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| full_body | *(本輪未生圖)* | | | |
| hands_detail(那張卡) | *(本輪未生圖)* | | | |
| desk_sofa_view | *(本輪未生圖)* | | | |
| desk_top_down | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,不是圖(與前兩輪相同)。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---

## 變更紀錄

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.0 | 2026-10-20 | 建立 | — |
| v1.1 | 2026-10-20 | § 八 給下游的摘要加一段:盒子畫面的有效期、托架裝好之後的沙發視角、藍光不得自行決定。**外型、五個不可變錨、提示詞一個字都沒改** | 購買意願改為「不會買」,盒子 12 月會被托架取代(`03 § 7-6`) |

---

*檔案版本:v1.1 — 2026-10-20 修訂(v1.0 同日建立)*
