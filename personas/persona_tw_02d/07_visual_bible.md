# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人、同一個家。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   yu-ting-chien
display_name:     簡郁婷 Chien Yu-Ting(Wendy)

art_style:        photorealistic documentary photography
                  # 不是 CG、不是插畫、不是 IG 白色家居圖庫。是照片。
style_reference:  natural north-window light, overcast and even, smartphone or 35mm look,
                  mild grain, high-key but not blown out, whites rendered as several
                  slightly different whites (not one flat white),
                  no beauty retouching, visible skin texture, East Asian skin rendered true

color_palette:
  - "#F3F2EE"   # wall white — 白牆(略暖)
  - "#E9E8E4"   # desk white — 書桌與螢幕背殼(略冷略灰)
  - "#1B1B1D"   # piano black — 鋼琴烤漆。**畫面裡唯一的大面積黑**
  - "#2C3546"   # navy — 她出門的衣服、托特包
  - "#9A9FA4"   # Keelung rain grey — 窗外、樓梯間、陰天
  - "#B08D57"   # counter brass — 計數器磨掉鍍鉻後露出的黃銅。**只能是一個小點**
  - "#E8A33D"   # water-level amber — 除濕機水位燈。**整個家唯一看得到的燈,最多一個小點**

lighting_default: north window light only, soft and even, no hard shadows.
                  夜間:一盞白色桌燈(約 4000K)+ 螢幕的冷光。
                  **畫面裡不能有任何朝向鏡頭的彩色指示燈**(她把所有燈轉向牆或藏進理線架),
                  除了除濕機那一顆琥珀色水位燈。
                  **不用環形燈、不用美肌補光、不用 RGB、不用暖色串燈。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok、Reels
  square:    1:1
  wide:      16:9    # 定場鏡頭(琴房黑白並排)

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty filter, porcelain skin, glass skin,
k-pop idol, korean ulzzang makeup, japanese gyaru, big doe eyes, v-shaped face,
sharp tiny chin, heavy contour, false eyelashes, coloured contacts, glossy lips,
influencer pose, peace sign, head tilt, pouting,
white minimal aesthetic influencer, linen dress, flowers in a vase, dried pampas grass,
scented candle, latte art, croissant, fairy lights, warm string lights,
rgb lighting, led strip, neon, gaming setup, black desk accessories, black desk mat,
glowing indicator lights, blue led, red led, visible power indicator,
cluttered colourful desk, plants on desk, monstera,
designer handbag, luxury jewelry, long manicured nails, nail art,
fake brand logos, apple logo, unreadable chinese characters, garbled text, watermark,
simplified chinese signage, mainland china street, japanese street signs, taipei 101,
extra fingers, malformed hands, warped cables, tape or stickers over lights
```

**為什麼要排除這些(不是隨便列的):**
- `white minimal aesthetic influencer / linen dress / flowers in a vase / scented candle` — **這是 AI 生「白色系女生」最容易滑過去的方向。** 她的白是監測,不是氛圍。她家沒有一件裝飾品(`04 § 13`)。
- `glowing indicator lights / blue led / red led` — **她家所有燈都轉向牆**(`03 § 6-1`)。畫面裡出現一顆朝鏡頭的藍燈,就不是她家。
- `black desk accessories / black desk mat / gaming setup` — 違反她的白色規則(`03 § 5-3`)。**唯一的黑是鋼琴。**
- `plants on desk / monstera` — **會發霉**(`02 § 11`)。
- `k-pop idol / v-shaped face / big doe eyes` — AI 生「亞洲女性」最常滑過去的方向。
- `apple logo / fake brand logos` — 法遵;她的裝置可以看得出是筆電與手機,但不得出現可辨識 logo。
- `taipei 101` — 她在信義區上班,但**畫面不得出現可辨識地標**。辦公室外景一律是「沒有特徵的玻璃大樓」。
- `simplified chinese signage / mainland china street` — 場景漂移。她在台北與基隆,招牌是繁體。
- `tape or stickers over lights / warped cables` — **她不貼燈、不蓋燈,她只讓燈朝牆。** 畫面裡出現膠帶貼燈就是別人家。線 AI 很容易畫壞。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 簡郁婷(Wendy) |
| slug | `yu-ting-chien` |
| age_appearance | **34–37**(看起來準時睡覺的 36 歲,不顯老,也不刻意顯年輕) |
| gender | 女 / she-her |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 中等偏瘦,**姿勢很直**(她坐著背會離開椅背),脖子偏長 |
| location_look | 台北受薪族,走路通勤:**膚色均勻,沒有騎車曬痕**;鼻翼常有一點紅(過敏性鼻炎) |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **偏長的鵝蛋臉**,顴骨略高,下顎線清楚但不尖 | 反 V 臉,也跟其他台灣女性人物的方圓臉區分 |
| **膚色** | `#E3C4A6` 中性偏白的膚色,**不是瓷白**。左顴骨有幾顆淡淡的曬斑 | 走路通勤,不騎車 |
| **膚質** | 有毛孔,T 字略油。**鼻翼兩側常態微紅**,早上更紅 | 過敏性鼻炎(`06 § 六`) |
| **眼睛** | 深棕色,**細的平行雙眼皮**,眼型細長,眼尾平 | 不是大眼,是「在看東西」的眼睛 |
| **眉毛** | 平直、偏細,**她每天只用眉筆補眉尾**(三十秒) | 她不研究化妝 |
| **疤** | **右手掌根一道約 2 公分的細白疤**,臉上沒有疤,眉毛完整 | **手的第一辨識點。** 九歲在基隆家門口那一百一十七階的濕樓梯上滑倒,右手撐地(`03 § 1-2` 的同一段樓梯)。**她按計數器用的就是這隻手** |
| **鼻子** | 鼻樑中等、直,鼻頭小 | |
| **嘴** | 唇形中等,上唇線清楚。**常態唇色自然,出門擦一支接近唇色的護唇膏** | |
| **表情基準** | **安靜、在看。** 不笑的時候看起來像在聽一個數字 | 見 3.6 |

### 3.2 頭髮

- 深黑褐色(`#241E1B`),**沒有染過**。頭頂有幾根白頭髮,她不拔(「我媽說拔了會長更多」,她知道這沒有根據)。
- **下巴長度的直短髮(bob),左邊塞在耳後,右邊用一根白色細髮夾夾住。**
- **濕度一高,髮尾會翹。** 這是她的天氣計,她自己會講「今天頭髮說 70%」。
  ← 這條寫死,它把「濕度」直接畫在她身上。
- 狀態指示(寫死):

| 頭髮怎麼弄 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 左塞耳後、右邊白髮夾 | 日常、在家、辦公室 | 預設 |
| 兩邊都塞耳後,沒有髮夾 | 美國會議、要專心 | 深夜、琴房 |
| 髮尾翹起來 | 下雨、基隆、梅雨 | 雨天、回基隆 |
| 用一根白色大抓夾全部夾起來 | 刷浴室、擦桌子、打掃 | 週日晚上 |

### 3.3 身體

- **身高 163 cm。體重 52 kg。**
- **姿勢很直**:坐著時背離開椅背,走路時肩膀平。**跟「剪接師的前傾」或「工程師的駝背」都不一樣。**
- 手:**手指細長,指甲剪短、乾淨,不擦指甲油。** 左手無名指一枚細的素面婚戒。
  **她算東西時會用食指與中指輕敲桌緣。** 手是這個人物最常入鏡的身體部位。
- 身形普通,她不在意。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **右手掌根的細白疤。** 任何手部近景都必須有(按計數器、拿濕度計)。**手的第一辨識點。** 臉上不畫疤。
2. **左手無名指的細素面婚戒。** 任何手部近景都在。
3. **鼻翼微紅。** 早上、雨天、基隆的畫面更明顯。
4. **右邊的白色細髮夾。** 日常畫面都在。

### 3.5 眼鏡(狀態指示器)

- **透明壓克力框,圓方形**,近視約 -4.25。**家裡戴眼鏡;出門與辦公室戴隱形眼鏡。**
- 透明框是她選的「白色系統裡的眼鏡」,她說黑框會在螢幕反光裡「多一條線」。

| 眼鏡狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 戴著 | 在家、琴房、深夜、美國會議 | 桌前、睡前看濕度計 |
| 推到頭頂 | 在看很近的東西(濕度計的小字、量杯刻度、充電頭的燈有沒有朝牆) | 特寫 |
| 沒戴(隱眼) | 辦公室日、回基隆、汐止 | 外出 |
| 拿在手上擦 | 剛從雨裡進門 | 雨天玄關 |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 安靜、在看,嘴唇自然閉著,眉頭平 | 70% 的畫面 |
| **counting** | 嘴唇輕抿,眼睛往左上,**食指與中指在桌緣輕敲** | 開會、按計數器 |
| **real smile** | **嘴巴閉著,一邊嘴角比另一邊高,眼尾有細紋。** 很短 | 跟廷宇、芊芊、一個不會亮的好東西 |
| **laugh** | 低頭,鼻子短短出一口氣,肩膀動一下 | 「抽樣誤差」群組的訊息 |
| **footnote** | **一邊眉毛微微抬起,嘴角不動。** 她心裡在加一個括號 | 「可以先給我一個數字嗎」 |
| **genuinely pleased** | 眉毛抬高,點一下頭 | 收到的白色跟照片一樣 |
| **tired** | **拇指與食指捏鼻樑**,眼睛閉著 | 美國會議後、偏頭痛 |
| **checking** | **眼鏡推到頭頂,臉靠近濕度計**,嘴唇無聲念出數字 | 睡前、早上 |
| **aligning** | 低頭看桌面,手指把一個東西推到跟桌緣平行 | 不自在的時候 |

**❌ 絕對不出現的表情:** 比 YA、嘟嘴、歪頭、對鏡頭眨眼、網美式的「看遠方微笑」、
任何韓系或日系的偶像表情、「白色系女孩」的閉眼喝咖啡。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中音**,基頻約 **210–230 Hz**。不嗲、不低沉 |
| 語速 | **畫外音約每分鐘 170 字。** 比一般人慢一點,很平均 |
| 口音 | **台灣國語,北部化的基隆人。** 平常聽不出來,講到「下雨」「臭殕」時台語會自然跑出來 |
| 音色 | 乾淨、偏薄,**幾乎沒有氣音** |
| 特徵 | **回答之前先「嗯」一聲。** 句子完整,常在句尾補一個條件:「…在不下雨的情況下」 |
| 英文 | 工作詞照念(forecast、deck、WBR、outlier),**發音清楚但有台灣腔,不刻意美式** |
| 台語 | 偶爾:「落雨」「臭殕」「好啦」。**不刻意,不當笑點** |
| 笑聲 | 鼻子短短出一口氣,幾乎沒有聲音 |
| 填充詞 | 「嗯」(多)、「就是」(少)、「對」(句尾確認) |
| 情緒起伏 | **低。** 好笑的事她講得更平,這就是笑點 |
| 絕不出現 | 「哈囉大家好」「寶寶們」「家人們」、播報腔、嗲聲、網紅式上揚尾音、中國腔兒化音 |

### 3.8 鏡頭前的肢體習慣

- **進任何房間,第一個動作是看牆角與窗框。** 有沒有濕的痕跡。旅館、辦公室、別人家。
- **算東西的時候,食指與中指在桌緣輕敲。**
- **不自在的時候,把手邊一個東西推到跟桌緣平行。**
- 遇到一顆朝著她的指示燈,**用兩根手指捏著那個東西轉到燈朝牆,然後低頭確認牆上沒有反光。** 她不貼、不蓋。
- 按計數器時,**只用拇指,按完會看一下窗口的數字**。
- 鼻子不舒服時,拇指與食指捏鼻樑。
- **她看鏡頭的時間很短。** 看一下,看回桌上的東西。

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎沒有。** 一年三四次,通常是跟廷宇在象山步道上、或芊芊搶她手機拍的 |
| 出現在畫面裡的方式 | **手、手指、背影、窗戶倒影裡的半個人。** TikTok 露臉 ≤10% |
| 拍什麼 | **牆角、白色表面、濕度計的數字、計數器、量杯、雨中的窗、鋼琴的一角、基隆的樓梯** |
| 構圖 | **置中、對稱、水平垂直很正。** 她拍照像在做圖表:主體在正中間,上下左右留一樣的白 |
| 光線 | **北窗平光。** 她會等陰天拍,因為「陰天的白才是白」 |
| 後製 | 曝光 +0.3,其他不動。**不用濾鏡** |
| 器材 | iPhone |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「白色表面、刻度、例外物件、手」,臉是配角。**
> **構圖要正,光線要平,白要有層次。** 這是她跟「白色系網美」最大的差別:網美的白是柔焦的、暖的、有道具的;
> 她的白是平的、冷一點、有刻度、而且常常有一個不合群的東西在角落。

---

## 四、服裝系統(五套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `03 § 5-3` 的規則:
**家裡白,出門深。** 收入高,但她不買名牌;衣服很少,很耐穿。

### 4.1 Office Day(辦公室日,出門)

```
- 深藍色或炭灰色細針織上衣(素面,無 logo)
- 炭灰色寬直筒西裝褲
- 炭灰色球鞋(雨天換一雙防水的黑色短靴)
- 深藍色尼龍托特包(用了六年,邊角磨白)
- Apple Watch SE 星光色,白色運動錶帶
- 隱形眼鏡
- 頭髮:左塞耳後、右邊白髮夾
← 出門穿深色不是時尚,是「外面髒了不要被看到」(03 § 5-3)
```

### 4.2 Home(在家日,琴房)

```
- 白色或燕麥色素面棉 T
- 淺灰色棉質寬褲
- 白色室內拖鞋
- 透明框眼鏡
- 頭髮:同 4.1,或兩邊塞耳後
- 不戴錶以外的任何飾品
```

### 4.3 US Call(深夜美國會議)

```
- 上半身:白色或淺藍色襯衫(扣到第二顆)
- 下半身:淺灰色睡褲
- 透明框眼鏡
- 頭髮:兩邊塞耳後,沒有髮夾
← 「十一點的會,我上半身是襯衫」(02 § 6)
```

### 4.4 Keelung Sunday(回基隆)

```
- 深藍色防水外套(帽子收在領子裡)
- 深色牛仔褲
- 黑色防水短靴
- 一把深藍色摺疊傘
- 隱形眼鏡
- 頭髮:髮尾翹起來(基隆的濕度)
```

### 4.5 Xizhi Lunch(去汐止公婆家)

```
- 炭灰色針織洋裝,長度過膝
- 小珍珠耳釘(婆婆送的結婚禮物。**她只在這一天戴**)
- 炭灰色樂福鞋
- 頭髮放下,右邊白髮夾
← 珍珠耳釘是一個安靜的訊號:她在這個家裡扮演婆婆期待的那一面,一個月兩次
```

### 4.6 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **Apple Watch SE 星光色,白色運動錶帶**(主要看睡眠與步數) |
| 眼鏡 | 透明壓克力圓方框(見 3.5) |
| 戒指 | **左手無名指一枚細素面婚戒** |
| 耳環 | **平常不戴。** 汐止那天戴婆婆送的小珍珠 |
| 包 | 深藍色尼龍托特包 |
| 小收納袋 | 白色,裡面是 30W 頭、一條短線、一條擦拭布 |
| 髮夾 | 白色細髮夾、白色大抓夾 |
| 手機殼 | 透明,邊角開始發黃。**她每年換一次,因為黃了看得到** |
| **不戴的** | 項鍊、手鍊、名牌包、美甲、大耳環、任何 logo 很大的東西、任何黑色的配件 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **右手掌根的細白疤**,手部近景就要有;**臉的第一辨識點是右邊的白色細髮夾**
2. **偏長鵝蛋臉、細平行雙眼皮、鼻翼微紅**,不准變 V 臉、不准變大眼
3. **下巴長度的直短髮,左塞耳後、右邊白髮夾**,不准染、不准長髮、不准捲
4. **透明框眼鏡**(在家的畫面),換成黑框等於換人
5. **家裡的畫面:白色有層次、零朝鏡頭的彩色指示燈(除了一顆琥珀色水位燈)、唯一的大面積黑是鋼琴**

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 白色系網美 / 亞麻洋裝 / 花瓶與香氛蠟燭 | **她的白是監測,不是氛圍** |
| 2 | 韓系偶像臉 / V 臉大眼 | AI 最容易滑過去的方向 |
| 3 | 精緻全妝、美甲、名牌 | 違反 `02 § 10` |
| 4 | 磨皮、美白、柔焦 | 她有鼻炎、有曬斑 |
| 5 | 畫面裡有朝鏡頭的藍燈、紅燈、RGB,或用膠帶貼住的燈 | **她家所有燈都轉向牆** |
| 6 | 黑色桌墊、黑色桌面配件、電競桌 | 違反白色規則。唯一的黑是鋼琴 |
| 7 | 桌上有植物 | 會發霉 |
| 8 | 出現可辨識的地標(台北 101)或真實品牌 logo | 法遵 |
| 9 | 簡體字招牌、中國或日本街景 | **她在台北與基隆**,招牌是繁體 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 右手掌根的疤在嗎(如果有手);眉毛有沒有被畫出疤(不可以)
- [ ] 是偏長鵝蛋臉、細平行雙眼皮嗎,有沒有被修成 V 臉大眼
- [ ] 短髮是不是下巴長度,右邊有沒有白髮夾
- [ ] 家裡的畫面是不是透明框眼鏡
- [ ] 皮膚有沒有被磨皮或美白,鼻翼紅還在嗎
- [ ] **畫面裡有沒有任何朝向鏡頭的彩色指示燈**(有的話就不是她家)
- [ ] **白色是不是有層次(牆、桌、螢幕背殼不是同一個白)**
- [ ] 鋼琴是不是畫面裡唯一的大面積黑
- [ ] 手有沒有畫壞,婚戒在不在,計數器的數字窗是不是四位數
- [ ] 有沒有出現亂碼中文、假 logo、可辨識地標

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, soft even north-window light, 35mm lens,
mild grain, no retouching, visible skin texture and pores,

a 36-year-old Taiwanese woman, 163cm, slim-average build, very upright posture,
slightly long neck,
long oval face with slightly high cheekbones and a clean but soft jawline,
narrow parallel double eyelids, dark brown eyes, level outer corners,
straight thin unbroken eyebrows with no scar on the face,
straight medium nose with a small tip, medium lips with a defined upper lip line,
natural lip colour, neutral light skin (#E3C4A6) with a few faint sun spots
on the left cheekbone, slight redness around the nostrils,
chin-length straight dark brown-black bob (#241E1B), tucked behind the left ear,
a thin white hair clip on the right side, a few stray grey hairs at the crown,
long slim fingers with short clean unpolished nails, a thin plain wedding band
on the left ring finger, a starlight smartwatch with a white sport band on the left wrist,

calm attentive expression, lips naturally closed, brows level,
looking at an object or a screen, not at the camera,

colour palette: layered whites #F3F2EE / #E9E8E4, a single large area of piano
black #1B1B1D only when the piano
is in frame, navy #2C3546 for outdoor clothing, rain grey #9A9FA4,
at most one tiny brass point #B08D57 and at most one tiny amber pilot light #E8A33D,
no other coloured lights
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle from her right so the thin white hair clip is visible,
clear acrylic round-square glasses, plain oatmeal crew-neck cotton t-shirt,
sitting very upright at a white desk by a north-facing window on an overcast day,
white walls behind her rendered as two slightly different whites,
soft even light with no hard shadow, shallow depth of field f/2.8,
subject centred with equal space on both sides,

--ar 4:5
```

### 6.3 Establishing shot / 琴房黑白並排(16:9,最重要的一張)

```
photorealistic documentary photograph, soft even north-window light, 28mm lens,
mild grain,

wide shot of a small music room in an old Taipei walk-up apartment, white walls,
white built-in cabinets, light wood-grain floor, a closed white venetian blind
on a north window,
on the left a black lacquered upright piano from the 1980s with nothing on its lid,
a white dehumidifier beside it with a single small amber water-level light,
40cm gap, then on the right a plain white 120x60 desk with a white ergonomic chair,
on the desk a white keyboard, a white mouse, a small white digital hygrometer,
a laptop, and a worn chrome hand tally counter in the top right corner whose
chrome has rubbed off to show brass,
a woman [MASTER CHARACTER BLOCK, seen from behind at three-quarter] sitting upright
at the desk in an oatmeal t-shirt and light grey trousers,
no visible power indicator lights anywhere, no plants, no decorations,
composition centred and symmetrical, the black piano and the white desk balanced,

--ar 16:9
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up photograph, soft north-window light, 50mm lens,
shallow depth of field,

close-up of a woman's long slim fingers with short clean nails and a thin plain
wedding band, the right thumb pressing a worn chrome hand tally counter whose
chrome has rubbed off to show brass, the four-digit window reading 0007,
on a plain white desk surface, beside it an open A5 grid notebook with a hand-drawn
tally mark (the Chinese character 正 plus two strokes) in the corner, and a small
white digital hygrometer whose base has a strip of yellowed paper tape hand-written "45-55",
no faces, no brand logos, no coloured lights,
composition centred, top-down,

--ar 1:1
```

### 6.5 Hygrometer at night(第二錨點,1:1)

```
photorealistic photograph, very low light, 50mm lens, mild grain,

a dark north-facing music room at night, the only light is a single tiny amber
water-level light on a white dehumidifier at the lower right and the faint glow
of a small white digital hygrometer's display reading 52%,
the base of the hygrometer has a strip of yellowed paper tape hand-written "45-55",
a woman's hand [slim fingers, thin wedding band] resting on the white desk beside it,
her clear acrylic glasses pushed up on her head at the top edge of the frame, out of focus,
the black edge of an upright piano barely visible at the far left,
no other lights, no indicator lights facing the camera, no tape over any light,
no brand logos, no text other than the digits,

--ar 1:1
```

### 6.5b Keelung stairs with the counter(主錨點的基隆版,9:16)

```
photorealistic documentary photograph, overcast drizzle, 28mm lens, first-person view,

looking down a long flight of narrow wet concrete steps between old hillside
apartment buildings in Keelung, iron railings, moss in the cracks, a grey harbour sky
in the distance, a woman's hand in the lower foreground holding a worn chrome hand
tally counter with brass showing through, the four-digit window reading 0117,
a navy waterproof jacket sleeve at the wrist,
traditional Chinese characters on a small faded sign out of focus, no faces,

--ar 9:16
```

### 6.6 Office day / 出門(9:16)

```
[MASTER CHARACTER BLOCK]

full body, walking downhill on a narrow Taipei lane of old five-storey apartment
buildings with iron window grilles and air-conditioner units, traditional Chinese
characters on a small hardware-shop sign out of focus, overcast morning,
wearing a navy fine-knit top, charcoal wide straight trousers, charcoal sneakers,
a navy nylon tote bag on her shoulder with worn white corners,
no glasses, looking ahead, not at the camera,
no recognisable landmarks, generic glass office towers faintly visible far away,

--ar 9:16
```

### 6.7 US call at night(4:5)

```
[MASTER CHARACTER BLOCK]

sitting very upright at a white desk at 11pm in a dark music room, clear acrylic
glasses, hair tucked behind both ears with no clip, a crisp white button-up shirt
on top and light grey sleep trousers below (visible under the desk),
a laptop on a video call (screen content not readable), a white desk lamp at 4000K
as the only light besides the screen, the edge of a black upright piano at the far
left of the frame in shadow, a single tiny amber light on a dehumidifier,
no other indicator lights,

--ar 4:5
```

### 6.8 Keelung rain(9:16)

```
photorealistic documentary photograph, overcast rainy light, 35mm lens,

view through a rain-streaked window of an old north-facing apartment in Keelung,
hillside apartment blocks and a grey harbour sky outside, on the white-painted
windowsill a small white digital hygrometer reading 78%, a woman's hand
[slim fingers, thin wedding band] resting beside it, the wall paint slightly
uneven from being repainted many times,
no faces, no text other than the hygrometer digits,

--ar 9:16
```

### 6.9 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same woman, identical soft north-window lighting
and framing in every panel, head and shoulders, plain white wall background,
clear acrylic glasses on:
1 calm attentive with lips closed, 2 counting with lips lightly pressed and eyes up-left,
3 a short closed-mouth smile with one corner higher, 4 laughing silently with head
down and a small breath through the nose, 5 one eyebrow slightly raised with no mouth
movement, 6 genuinely pleased with raised brows and a small nod, 7 tired with thumb
and index finger pinching the bridge of her nose and eyes closed, 8 glasses pushed up
on her head, leaning close to read a small hygrometer, 9 looking down and pushing an object parallel to
the desk edge with one finger,

--ar 1:1
```

### 6.10 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
when she enters any room she first glances at the wall corners and window frames for damp.
when counting she taps her index and middle fingers lightly on the desk edge.
when uncomfortable she pushes a nearby object until it is parallel with the desk edge.
when an indicator light faces her she pinches the device with two fingers and turns it
until the light faces the wall, then checks the wall for any glow. she never covers lights
with tape. to read the hygrometer she pushes her glasses up and leans in. she presses the tally counter
with her thumb only and then checks the digits. when her nose bothers her she pinches
the bridge of it. she sits very upright and rarely leans back. she glances at the camera
briefly and returns her eyes to the object.

VOICE: mid female voice, fundamental around 220 Hz, clean and thin with almost no
breathiness, Taiwanese Mandarin with a faint Keelung lilt on words about rain,
says "嗯" before answering, complete sentences that often end with a small condition,
voice-over around 170 Chinese characters per minute, flat delivery that gets flatter
when something is funny, no influencer greeting, no cutesy tone, no broadcast energy,
no rising terminals.

CAMERA: locked-off on a small tripod or top-down over the desk, 35mm or 50mm,
centred symmetrical framing, soft north-window light, no coloured lights in frame.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 鼻翼微紅 | `06 § 六` 過敏性鼻炎、`03 § 5-3` 南港黑霉 | ✓ |
| 沒有騎車曬痕、左顴骨曬斑 | `06 § 三` 走路通勤 | ✓ |
| 姿勢很直 | `04 § 13` 工作 C 90;她不靠椅背 | ✓ |
| 右手掌根的疤 | `03 § 1-2` 那一百一十七階 | ✓ |
| 濕度一高髮尾翹 | `01 § 1-A` 基隆、`02 § 11` 記錄濕度 | ✓ |
| 透明框眼鏡 | `03 § 5-3` 家裡的白色系統、乾眼 | ✓ |
| 家裡白、出門深 | `03 § 5-3`「外面我管不了」 | ✓ |
| 只在汐止戴珍珠耳釘 | `05 § 6` 婆婆 | ✓ |
| 白色錶帶 | `02 § 9` 只買白色 | ✓ |
| 婚戒 | `02 § 4` 已婚 | ✓ |
| 衣服少、耐穿、無 logo | `02 § 10` 品牌敏感度低 | ✓ |
| 幾乎不自拍 | `04 § 13` E 值 30 | ✓ |
| 構圖置中對稱 | `02 § 6` 數據職、做圖表的習慣 | ✓ |
| 畫面零朝鏡頭的彩色指示燈 | `03 § 6-1` 燈要朝牆 | ✓ |
| 唯一的大面積黑是鋼琴 | `03 § 6-2` 例外條款 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.10 影片提示詞、五個不可變錨。**露臉 ≤10%。**
**Ivy(素材):** 讀 6.1 master block、6.3 定場鏡頭、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**
**另外:SPACION 桌面充電站目前規劃為單一質感黑。她的畫面裡,黑色只有鋼琴。** 這一條不要為了產品去改。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| establishing_room | *(本輪未生圖)* | | | |
| hands_counter | *(本輪未生圖)* | | | |
| hygrometer_night | *(本輪未生圖)* | | | |
| keelung_stairs | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,不是圖(與 Nathan、沛璇第一輪相同)。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.2 | 2026-10-20 | 跨人物撞型修正:九歲在那段樓梯滑倒留下的疤,由左眉尾改到右手掌根(撐地的那隻手,也是按計數器的手);左眉尾疤保留給 `persona_tw_06`。滑倒的事實與第 13 檔 TikTok 不變 | 主 session 統一 QA:第二批平行生成,五個人都用了「左眉尾的疤」當第一辨識點,配角名撞 `02c` |

*檔案版本:v1.2 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
