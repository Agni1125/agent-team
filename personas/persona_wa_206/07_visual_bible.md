# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
> **本輪不生圖,seed 表留空。**
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點:最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   tess-halvorsen
display_name:     Teresa "Tess" Halvorsen

art_style:        photorealistic documentary photography
                  # 照片。不是 CG、不是插畫、不是 3D、不是時尚大片。
style_reference:  overcast Pacific Northwest natural light, iPhone-like or 35mm look,
                  mild noise in low light, no beauty retouching, visible skin texture,
                  practical light sources visible in frame (lamps, streetlights, screens)

color_palette:
  - "#2B2F33"   # wet asphalt charcoal — 她的衣服、夜裡濕的路面、車內
  - "#8C9A8E"   # Puget Sound grey-green — 天空、海、房子的外牆
  - "#C8A27A"   # kraft tag brown — MOCKUP 吊牌、紙箱、胡桃木桌
  - "#F3E9DC"   # 2700K warm white — 她家裡所有的燈光
  - "#D9E021"   # hi-vis yellow-green — 反光背心。唯一的高彩度色,點綴用,不超過畫面 5%

lighting_default: 現場光(available / practical light only)。
                  白天:西雅圖陰天的柔光,窗光為主。
                  晚上:一盞暖色檯燈 + 窗外的路燈或車燈。
                  **不用棚燈、不用環形燈、不用美肌補光、不用霓虹。**
                  畫面裡**一定看得到光源**(她是做燈光的,這是她的畫面語言)。

aspect_ratios:
  portrait:  4:5
  vertical:  9:16   # Threads / Reels / TikTok
  square:    1:1
  wide:      16:9

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  同一張圖微調用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty retouch, glamour makeup, contour makeup,
fashion model, influencer pose, duck lips, perfect teeth, bright white teeth,
dyed hair, hair highlights, balayage, removing the white streak,
studio lighting, ring light, softbox, neon lights, RGB lighting, purple LED glow,
blue LED glow, teal-and-orange grade, HDR, oversaturated, cyberpunk,
designer handbag, luxury watch, gold jewelry, diamond ring, high heels,
sports car, luxury car interior, visible car brand logo, visible product logos,
anime, illustration, 3d render, cgi, cartoon,
extra fingers, malformed hands, warped text, unreadable text, watermark,
stock-photo smile, thumbs up, peace sign, hands on hips power pose,
sunny tropical beach, desert, snow-covered city
```

**為什麼要排除這些(不是隨便列的):**
- `dyed hair / highlights / removing the white streak` — 左邊髮際的天生白髮是第一辨識點。生圖最容易把它「修掉」或變成挑染。
- `purple LED glow / blue LED glow / RGB` — 她對這兩種顏色的指示燈有生理反應(`04 § 7`),畫面裡出現會讓人物自相矛盾。
- `perfect teeth / bright white teeth` — 左門牙有一個小缺角。
- `luxury car interior / visible car brand logo` — 她的車是中古小型 SUV,不能變成豪車廣告,也不能出現可辨識的車廠標誌。
- `designer handbag / gold jewelry` — 她的高價消費全在「每天用、看不出來」的東西上(`02 § 10`)。
- `studio lighting / ring light` — 一個照明設計師的照片裡如果有環形燈,就是寫壞了。
- `sunny tropical beach / desert / snow-covered city` — 場景漂移。她在陰天的西雅圖,偶爾在乾的 Wenatchee(那是唯一合法的晴天)。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | Teresa "Tess" Halvorsen |
| slug | `tess-halvorsen` |
| age_appearance | **31–35** |
| gender | 女 / cis |
| ethnicity | 菲律賓裔(母系)與挪威裔(父系)混血。**東南亞與北歐骨相的混合,不偏向任何一邊的刻板樣子** |
| build_class | 普通偏結實,肩膀比一般辦公室工作者寬(劇場扛燈的底子) |
| location_look | 太平洋西北的室內膚色:冬天偏白一點,夏天在 Wenatchee 曬過之後前臂會深一個色階 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | 鵝蛋偏短,顴骨柔和但明顯,下巴小而圓 | 混血骨相 |
| **膚色** | `#C89F7E` 暖調淺橄欖色。冬天偏淡 | 母系的菲律賓血統 + 西雅圖的陰天 |
| **膚質** | **有毛孔,鼻翼兩側有一點泛紅,額頭偶爾有一顆小痘。** 冬天嘴角有點乾 | 反美肌,33 歲 |
| **眼睛** | 深棕色,杏眼,內雙(上眼皮的摺痕很淺,靠內眼角幾乎看不到) | 混血 |
| **眼下** | 淡淡的陰影,夜間調燈的隔天明顯 | |
| **眉毛** | 濃、平直、自然,只修雜毛 | 她不在這件事上花時間 |
| **鼻子** | 鼻樑偏低,鼻頭圓 | |
| **嘴** | 中等厚度,上唇有清楚的唇峰 | |
| **牙齒** | 整齊、自然的米白色。**左上門牙邊緣有一個小缺角(約 1 mm),只有笑開才看得到** | 2017 年劇場拆台的舊傷(見 `03`) |
| **表情基準** | **專注,眼睛微瞇,視線常常往上(在看光從哪裡來)** | 見 3.6 |

### 3.2 頭髮

- 深棕近黑(`#2E231D`),直,髮量多,髮質粗。長度到鎖骨。
- **日常:用一支霧黑色鯊魚夾隨手挽在後腦,有幾撮掉下來。** 放下來的時候很少。
- **【第一辨識點】左邊額頭髮際線,一撮約 1.5 cm 寬的天生白髮(poliosis 樣),往後梳時會形成一條白色的線。**
  從 lola 遺傳的。**她從來不染,任何一張圖都不可以把它修掉、染掉、或變成挑染。**
- 分線:自然偏右分,白髮在左邊所以永遠看得到。
- 下雨天:髮尾會有點毛躁,額前幾根黏在臉上。

### 3.3 身體

- **身高 165 cm(5'5")。體重約 62 kg。**
- 肩膀比一般辦公室工作者寬,上臂有一點線條(劇場扛燈的底子,現在只剩一半)。
- **姿勢:站的時候重心在後腳跟,雙手常常抱著自己的手肘。** 坐著看筆電時肩膀會往前圓。
- 左肩偶爾會痠,她會轉一下肩膀(爬梯子的舊傷)。
- 手:**指甲短、乾淨、沒有指甲油。冬天指節乾。** 右手中指第一節側面有一點筆繭(Apple Pencil)。
  左手無名指一只**霧面鈦金屬的細婚戒**。
- 右耳軟骨(耳輪上緣)一個小銀圈耳環。兩邊耳垂有耳洞,通常不戴。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **【第一辨識點】左邊髮際約 1.5 cm 寬的天生白髮。** 任何人像、任何側臉都必須有。
2. **左上門牙邊緣的小缺角。** 只在笑開的表情出現。
3. 右耳軟骨的小銀圈。
4. **不可以出現的:** 雀斑、眉毛上的疤、臉上任何疤痕、手指上的疤(這四樣已經被其他人物用作辨識點,也不屬於她)。

### 3.5 眼鏡

**不戴。** 她有輕微散光,沒有矯正。**晚上開車時看路燈會有星芒,她會微微瞇眼。**
→ 夜間車內畫面:路燈與對向車燈在她眼裡有放射狀的光芒。她是照明設計師,她知道那是散光,她不打算處理(**這是她自己承認的矛盾之一**)。

### 3.6 表情庫(九宮格)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 專注,眼睛微瞇,嘴唇閉著,視線往上或往側面(在看光) | 70% 的畫面 |
| **reading the light** | 頭微仰,看天花板或光源,眉毛輕輕挑起 | 進任何空間的第一秒 |
| **half-smile** | 嘴角兩邊都動但不張嘴,眼尾有細紋 | 她最常見的笑 |
| **real laugh** | 頭往前低一點,**露出左門牙的缺角**,眼睛瞇起來 | 跟 Maren、跟 Graham |
| **unimpressed** | 嘴唇抿平,一邊眉毛微抬,不看對方看東西 | 看到「適用所有車款」 |
| **delighted** | 眼睛睜大,嘴微開,**手已經在掏手機** | 一道剛好的光 |
| **tired** | 眼下加深,髮夾鬆了,頭髮掉下來一半 | 夜間調燈之後 |
| **irritated** | 下巴收緊,看著那個東西,不看人。**不皺眉** | 支架掉下來、充電頭被拔掉 |
| **hold, please** | 整個人停住,一隻手掌朝下平舉 | 看到危險,工作狀態 |

**❌ 絕對不出現的表情:** 誇張大笑、比讚、比 YA、嘟嘴、對鏡頭眨眼、網紅式的驚訝摀嘴、「開心的上班族」圖庫笑容。

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | 中低的女聲(alto),基頻約 **180–200 Hz** |
| 語速 | **中等,約每分鐘 150 詞。** 講到數字時會放慢、咬字清楚(劇場叫 cue 的習慣) |
| 口音 | **內陸西北(Inland Northwest)的平:** 母音不誇張,句尾不上揚。偶爾說 "you bet" |
| 音色 | 乾淨,略帶沙。**早上第一句話比較低** |
| 特徵 | **講口令時會變短、變平、變大聲一點**("Standby." "Go." "Hold, please.") |
| 笑聲 | 一聲短的 "ha",從鼻子出來,眉毛同時往上 |
| 填充詞 | "okay so"、"like"(少)、"honestly" |
| 情緒起伏 | 小。**興奮時講快一點、手會比出光的方向** |
| 絕不出現 | 播報腔、廣告腔、上揚的句尾、"Hey guys!"、"you guys"、氣音撒嬌 |

### 3.8 鏡頭前的肢體習慣

- **進任何空間先抬頭看天花板。** 招牌動作,任何換場鏡頭都可以用。
- **用兩根手指(食指與中指併攏)指光源。** 照明設計師在現場指燈的手勢。
- **收線:看到一條線就會順手用 over-under 的方式繞成圈**(劇場收線法,不會打結)。
- 想事情的時候雙手抱著自己的手肘。
- 測試東西的穩不穩:**用指節輕敲兩下。**
- **不看鏡頭。** 她看光、看東西、看手上的事。要看鏡頭是刻意的,而且短。
- 講話時右手會動,左手常常拿著東西(手機、吊牌、照度計)。

### 3.9 拍照與自拍行為(決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **一年 0–3 張。** 通常是窗玻璃或車窗的倒影,半張臉,白髮看得到 |
| 出現在畫面裡的方式 | **手、側影、倒影、背影(穿反光背心)。** 臉極少 |
| 拍什麼 | **光(60%)、東西(25%)、地方(15%)。** 不拍人、不拍食物擺盤 |
| 構圖 | **畫面裡一定有光源。** 構圖比一般人準(職業),但不刻意 |
| 後製 | **不調色、不加濾鏡。** 只裁切。「光本來就是那個顏色」 |
| 器材 | iPhone 17 Pro Max |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「光」與「手」,不是「臉」。**

---

## 四、服裝系統(三套 + 變體)

外型必須對得起 `02 § 10`:**錢花在每天用、看不出牌子的東西上。** 沒有任何看得見的 logo。

### 4.1 Site Outfit(工地日,一週一到三次)

```
- 黑色直筒牛仔褲,膝蓋有點磨白
- 炭灰色美麗諾羊毛圓領長袖(她有三件一樣的)
- 那件 US$599 的三層防水硬殼外套,石墨灰色,沒有看得見的 logo,袖口有一點磨損
- 棕色複合材質包頭的健行工地鞋,鞋頭刮傷,鞋帶換過一次(黑色)
- 螢光黃反光背心,背後麥克筆寫 HALVORSEN(在車上穿上)
- 白色工地安全帽(放在後座,工地才戴)
- 頭髮用鯊魚夾挽起,冷的時候戴一頂炭灰色毛帽
- 右手拿照度計或手機
```

### 4.2 Office Outfit(進辦公室,週二到週四沒有工地的時段)

```
- 炭灰或黑色的針織毛衣(寬鬆)
- 黑色寬褲
- 黑色皮革休閒鞋,已經穿出鞋頭的摺痕
- Apple Watch,黑色運動錶帶
- 霧面鈦金屬婚戒、右耳軟骨的小銀圈
- 頭髮用鯊魚夾挽起
```

### 4.3 Home / Weekend(在家工作、週末、Lincoln Park)

```
- 一件洗到褪色的深藍色連帽衫(Graham 的舊衣服,沒有任何字)
- 灰色棉褲、羊毛襪
- Lincoln Park:同一件硬殼外套 + 黑色緊身褲 + 越野跑鞋
- 頭髮放下來或隨便綁
```

### 4.4 Driving(車內畫面)

```
- 依當天是工地日或辦公室日(4.1 或 4.2)
- 副駕車門裡露出反光背心的黃色
- 不戴眼鏡(她本來就不戴),晚上會微微瞇眼
- 2026 年 10 月 6 日之後:手機在杯架裡,螢幕朝上
- 之前(歷史畫面):手機在中控螢幕右下角的磁吸支架上,支架臂綁著 MOCKUP 4 的吊牌
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | Apple Watch,黑色運動錶帶。**不是機械錶、不是精品錶** |
| 戒指 | 霧面鈦金屬細婚戒,左手無名指。**只有這一只** |
| 耳環 | 右耳軟骨一個小銀圈。耳垂通常不戴 |
| 髮夾 | 霧黑色鯊魚夾(她有四支一樣的) |
| 包 | 那個 Kickstarter 的深灰模組化後背包,側袋放 commuter brick(線用 over-under 收成八字) |
| 眼鏡 | **不戴** |
| **不戴的** | 項鍊、手鍊、名牌包、精品錶、任何有大 logo 的東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

### 五個不可變的錨(Immutable Anchors)

1. **左邊髮際 1.5 cm 的天生白髮**,不准修掉、不准染、不准變挑染
2. **左上門牙的小缺角**,笑開時必須有
3. **深棕近黑的直髮 + 霧黑鯊魚夾**,換髮型等於換人
4. **皮膚有毛孔、鼻翼泛紅、不磨皮**,反美肌
5. **畫面裡一定看得到光源**,她的畫面語言

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 網美 / 時尚模特 / 精緻妝感 | 她一天化妝五分鐘 |
| 2 | 白髮被修掉、染黑、或變成挑染 | 第一辨識點 |
| 3 | 精品包、名錶、金飾、高跟鞋 | 違反 `02 § 10` 的消費邏輯 |
| 4 | 棚燈、環形燈、霓虹、RGB、紫色或藍色的光 | 照明設計師的畫面裡不會有這些 |
| 5 | 豪車內裝、看得見的車廠標誌 | 她開的是中古小型 SUV |
| 6 | 對鏡頭笑、比讚、power pose | 圖庫感 |
| 7 | 大晴天、海灘、沙漠、雪城 | 她在陰天的西雅圖 |
| 8 | 臉部特寫為主的帳號 | 主體是光與手 |
| 9 | 出現可辨識的真實品牌 logo 或真實人物 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段 |

### 連續性檢查表(每次出圖後跑)

- [ ] 左邊髮際的白髮在嗎?寬度對嗎?(不可以是挑染)
- [ ] 笑開的圖,左門牙的缺角在嗎?
- [ ] 頭髮是深棕近黑、直、鯊魚夾?
- [ ] 皮膚有沒有被磨皮?
- [ ] 畫面裡有沒有一個看得見的光源?
- [ ] 有沒有出現紫色、藍色、RGB 的光?(不可以)
- [ ] 有沒有不該有的珠寶、名牌、logo?
- [ ] 臉上、眉毛、手指有沒有被畫出疤?(不可以)
- [ ] 場景是不是陰天的西北太平洋?
- [ ] 手有沒有畫壞?吊牌上的字是不是 `MOCKUP` 加編號?

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, available light only, practical light
sources visible in the frame, mild noise in low light, no retouching,
visible skin texture and pores,

a 33-year-old American woman of mixed Filipino and Norwegian descent,
165cm, average build with slightly broad shoulders,
short oval face with soft but defined cheekbones and a small rounded chin,
warm light olive skin (#C89F7E), no freckles,
slight natural redness at the sides of the nose,
dark brown almond eyes with a very low inner eyelid crease,
thick straight natural eyebrows,
a low nose bridge with a rounded tip, medium lips with a defined cupid's bow,
thick straight very dark brown hair (#2E231D) to the collarbone,
twisted up loosely in a matte black claw clip with loose strands falling,
a natural white streak of hair about 1.5cm wide at the left front hairline,
clearly visible, not dyed, not highlights,
a small silver hoop in the upper cartilage of her right ear,
short unpolished nails, a thin matte titanium wedding band on her left hand,
no glasses,

focused expression with eyes slightly narrowed, looking toward a light source
rather than at the camera,

colour palette: wet asphalt charcoal #2B2F33, Puget Sound grey-green #8C9A8E,
kraft tag brown #C8A27A, 2700K warm white #F3E9DC,
with a small accent of hi-vis yellow-green #D9E021 under 5% of frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, turned slightly away from camera,
looking up toward a warm desk lamp just out of frame on the left,
charcoal merino crew-neck sweater, the white streak in her hair catching the light,
overcast window light from the right, a rain-streaked window behind her,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,工地日,9:16)

```
[MASTER CHARACTER BLOCK]

full body standing on a gravel construction access road at dusk,
weight on her back foot, holding a small grey handheld light meter in her right hand,
graphite three-layer rain shell with no visible logo, black straight jeans,
brown composite-toe hiking boots with scuffed toes,
a hi-vis yellow-green safety vest with HALVORSEN written by hand in black marker
on the back, seen from a three-quarter back angle,
white hard hat in her left hand, light drizzle, wet gravel reflecting
temporary site floodlights, a parked dark grey compact SUV out of focus behind her,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up product-style photograph, natural window light,
50mm lens, shallow depth of field,

close-up of a woman's hands with short unpolished nails and a thin matte
titanium wedding band, tying a kraft paper shipping tag with a reinforced
paper ring around the string hole onto a cheap white plastic phone charger with a cotton string,
the tag handwritten in black marker reading "MOCKUP 1 (06/23)",
a walnut desktop, a dark grey desk lamp casting warm 2700K light from the left,
a coil of white cable wrapped over-under in a figure-eight beside it,
a black-and-white tuxedo cat's tail just entering the frame at the top edge,
no faces, no logos,

--ar 1:1
```

### 6.5 Driving / in-car(9:16)

```
[MASTER CHARACTER BLOCK]

seated in the driver's seat of a dark grey compact European SUV with a black
interior, a portrait-oriented centre touchscreen, vertical slatted air vents,
and a softly textured dashboard, no visible brand logo anywhere,
night, parked in a residential driveway, engine off, rain on the windshield,
warm 2700K porch light glowing through the rain from a small grey-green house
ahead, her face lit only by the dim phone screen,
a smartphone lying face up in the centre cupholder, screen at lowest brightness,
a faint circular adhesive mark on the dashboard to the lower right of the
touchscreen, a hi-vis yellow-green vest folded in the passenger door pocket,
she is looking at the house windows, not at the camera,
shot from the passenger seat,

--ar 9:16
```

### 6.6 Home desk / night(4:5)

```
[MASTER CHARACTER BLOCK]

sitting at a walnut desk in the corner of a small 1940s dining room at night,
faded navy hoodie with no print, hair half falling out of the claw clip,
a 16-inch laptop open, a dark grey desk lamp with a glare shield giving warm
2700K light, a white 3-port wall charger leaning against the desk leg facing
the wall with a kraft "MOCKUP 1" tag hanging from it, a power strip on the
floor, a corkboard above the desk with one retired kraft tag pinned to it,
a black-and-white tuxedo cat asleep on the desk beside the charger cable,
the dark window reflecting the lamp, no blue or purple light anywhere,
she is reaching to switch off the lamp, not looking at the camera,

--ar 4:5
```

### 6.7 Office desk / shared floor box(16:9)

```
[MASTER CHARACTER BLOCK]

morning in an open-plan design studio on the third floor of an 1890s brick
building, exposed timber beams, tall windows with grey daylight,
two white desks side by side, a single floor outlet box on the wooden floor
between them with one shared power strip, she is crouching to plug a white
laptop power brick into the last free socket, charcoal knit sweater,
black wide trousers, a younger colleague's monitor cables already taking the
other sockets, a handheld light meter and a laser distance measure on the desk,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same woman, identical lighting and framing
in every panel, head and shoulders, plain warm grey background, the white
streak at her left hairline visible in every panel:
1 focused with eyes slightly narrowed, 2 looking up toward a light source with
eyebrows slightly raised, 3 closed-mouth half-smile with crinkled eye corners,
4 a real laugh with head tipped forward showing a tiny chip on the edge of her
upper left front tooth, 5 unimpressed with lips pressed flat and one eyebrow raised,
6 delighted with eyes wide and lips parted, 7 tired with deeper under-eye
shadows and hair falling out of the clip, 8 irritated with a tightened jaw
looking at an object, 9 completely still with one palm held flat and level,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
when she enters a space she looks up at the ceiling and the light sources first.
she points at lights with her index and middle fingers held together.
when she picks up a loose cable she automatically coils it over-under.
she tests whether something is solid by tapping it twice with a knuckle.
when thinking she holds her own elbows. she does not look at the camera;
she looks at the light or at the object in her hands. her right hand moves
when she talks; her left usually holds something.

VOICE: alto female voice, around 190 Hz, about 150 words per minute,
flat Inland Northwest vowels, no rising terminals, slightly husky in the
morning, numbers spoken slowly and clearly, theatre calls ("standby", "go",
"hold, please") spoken shorter and flatter, a single short "ha" laugh through
the nose with raised eyebrows. no broadcast energy, no sales tone.

CAMERA: handheld, slight natural drift, 35mm, eye level, available light only,
at least one practical light source visible in frame.
```

---

## 七、外型與人設的一致性驗算

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 左邊髮際的天生白髮 | `05` lola 的遺傳 | ✓ |
| 左門牙缺角 | `03` 2017 年劇場拆台 | ✓ |
| 肩膀偏寬、左肩會痠 | `03` 劇場扛燈與爬梯子 | ✓ |
| 沒有雀斑 | 刻意:避開與其他人物撞型(`00 § 四` 第 13 項) | ✓ |
| 不戴眼鏡、夜間微瞇 | `04 § 0` 衍生矛盾(照明設計師不矯正散光) | ✓ |
| 三件一樣的美麗諾上衣、US$599 外套 | `02 § 10` 每天用的東西買好的 | ✓ |
| 沒有珠寶、只有婚戒與一個耳環 | `02 § 10` 不在乎別人看得到的貴 | ✓ |
| 霧面鈦金屬婚戒 | 「不用再想它」(不會刮花) | ✓ |
| 反光背心 + 名字 | `05` Rocco:「自己帶背心的設計師」 | ✓ |
| 幾乎不自拍、畫面主體是光 | `02 § 11` found light | ✓ |
| 用 over-under 收線 | `03` 劇場 | ✓ |
| 抬頭看光 | `02 § 6` 職業反射動作 | ✓ |

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲音、3.8 肢體、6.9 影片提示詞、五個不可變錨。**畫面裡一定要有光源。**
**Ivy(Amazon 素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**她是照明設計師這件事,不可以出現在任何燈號、螢幕、色溫相關的商業素材上**(專家薦證風險,見 `08 § 9.6`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生成)* | | | |
| full_body_site | *(本輪未生成)* | | | |
| hands_detail_tag | *(本輪未生成)* | | | |
| in_car_night | *(本輪未生成)* | | | |
| home_desk_night | *(本輪未生成)* | | | |
| expression_sheet | *(本輪未生成)* | | | |

> **本輪任務指定不生圖。** 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。
> **第一次出圖要特別檢查白髮有沒有被模型修掉**,這是這個人物最容易失敗的地方。

---

*檔案版本:v1.0 — 2026-10-21 建立*
