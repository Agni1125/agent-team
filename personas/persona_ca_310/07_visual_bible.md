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
character_slug:   ani-kaprielian
display_name:     Anahit "Ani" Kaprielian

art_style:        photorealistic documentary photography
                  # 照片。不是 CG、不是插畫、不是 3D、不是時尚大片。
style_reference:  Southern California daylight, hazy marine-layer mornings on the Westside,
                  hard late-afternoon sun in the Valley, iPhone-like look, mild grain,
                  no beauty retouching, visible skin texture, everyday clutter left in frame

color_palette:
  - "#9FC5C0"   # sea glass:她那台 Prius 的車色,也是 Westside 早上的天
  - "#E9D9C4"   # dingbat stucco cream:公寓外牆、停車棚
  - "#B5835A"   # tan leather:MagSafe 卡套、tatik 的咖啡杯碟、楓木桌
  - "#2F3A40"   # 405 asphalt slate:停車場、車內、她的牛仔褲
  - "#F2B544"   # Meyer lemon:唯一的高彩度點綴,不超過畫面 5%

lighting_default: 現場光。
                  早上:Westside 的霧光(柔、灰白),或公司停車場四樓的斜陽 + 天花板的日光燈。
                  下午:往西開的硬光、擋風玻璃上的眩光。
                  室內:窗光 + 一盞夾燈。
                  **不用棚燈、不用環形燈、不用美肌補光、不用霓虹。**

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
plastic skin, airbrushed skin, beauty retouch, glamour makeup, heavy contour, cheek dimples,
lip filler look, fashion model, influencer pose, duck lips, bright white veneers,
straightened hair, sleek blowout, hair claw clip, pencil in hair bun,
white streak in hair, gray streak, freckles, eyebrow scar, facial scar, scar on hand,
studio lighting, ring light, softbox, neon lights, RGB lighting,
Hollywood sign, palm-tree sunset cliché, beach bikini, red carpet,
luxury car interior, sports car, visible car brand logo, visible product logos,
television screen showing a recognizable app or show, streaming app interface,
designer handbag, luxury watch, large logo clothing,
anime, illustration, 3d render, cgi, cartoon,
extra fingers, malformed hands, warped text, unreadable text, watermark,
stock-photo smile, thumbs up, peace sign, hands on hips power pose,
icy grey northern city, overcast northern city
```

**為什麼要排除這些(不是隨便列的):**
- `straightened hair / sleek blowout`:深棕色長捲髮是她的第一個輪廓。生圖最容易把捲髮拉直變成「洛杉磯網美」。
- `hair claw clip / pencil in hair bun / white streak / freckles / eyebrow scar`:**這五樣是其他人物已經用掉的辨識點**(見 `00 § 四` 第 13 項),畫上去會撞。
- `Hollywood sign / palm-tree sunset / bikini / red carpet`:洛杉磯的刻板畫面。她住在 1957 年的公寓、開 2014 年的 Prius。
- `television screen showing a recognizable app / streaming app interface`:**她在串流平台工作,任何可辨識的 App 或節目畫面都會變成公司背書的暗示**(`08 § 9.6`)。
- `luxury car interior / visible car brand logo`:她的車是一台淺藍綠色的舊油電車,不能出現車廠標誌。
- `icy grey northern city, overcast northern city`:場景漂移。她在南加州。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | Anahit "Ani" Kaprielian |
| slug | `ani-kaprielian` |
| age_appearance | **27–31** |
| gender | 女 / cis |
| ethnicity | 亞美尼亞裔美國人。**地中海東岸與高加索的骨相,不誇張、不異國化** |
| build_class | 偏瘦、勻稱,攀岩的前臂與肩膀 |
| location_look | 南加州的膚色:淺橄欖色,前臂與鼻樑在夏天會深一個色階 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | 鵝蛋偏長,下巴線條柔和 | |
| **膚色** | `#C9A27E` 淺橄欖色,暖調 | 南加州日照 |
| **膚質** | **有毛孔,鼻翼與下巴偶爾有一兩顆小痘。** 眼下在通勤週有一點暗 | 反美肌,29 歲 |
| **眼睛** | 深棕色,大而圓的杏眼,雙眼皮明顯,睫毛濃 | |
| **眉毛** | 濃、自然、微微上揚的弧度,**兩眉之間是分開的**(不要畫成連眉) | 避免刻板印象 |
| **鼻子** | 鼻樑直而長,鼻頭微微下垂 | |
| **嘴** | 偏豐滿,上唇比下唇薄 | |
| **【第一辨識點】鼻釘** | **左鼻翼一顆很小的金色鼻釘**(2 mm),正面、側面都看得到 | 十八歲生日自己去打的(她少數不猶豫的決定) |
| **笑** | **笑的時候右邊嘴角先動**,笑起來是歪向右邊的;**禮貌性的笑是左右完全對稱的**(那是她在擋) | 爸爸也是這樣笑 |
| **表情基準** | **在聽。頭微微偏,眼睛看著別人的手,不看臉** | 見 3.6 |

### 3.2 頭髮

- 深棕近黑(`#2B1E18`),**長捲髮(大捲加小卷混合)**,長度到胸口上方,髮量很多。中分。
- **日常:放下來,或用一條黑色細髮圈在頸後鬆鬆綁一個低馬尾**;開車的日子綁起來(下午太陽很曬)。
- **黑色髮圈:** 她手腕上永遠有一條。**車上出風口葉片纏的那條也是同一種。**
- 不燙直、不染、不挑染。濕的時候捲得更明顯。

### 3.3 身體

- **身高 160 cm(5'3")。體重約 55 kg。**
- 偏瘦勻稱,**前臂有攀岩的線條,手指的指腹有一點繭、偶爾有白色的止滑粉**。
- **姿勢:坐著時會往前傾,雙手放在膝蓋上不動**(訪談時「手不要動,讓對方的手動」的職業習慣)。
- 手:**指甲短、沒有指甲油。** 右手中指第一節有一點筆繭。**左手腕永遠一條黑色髮圈。**
- 首飾:一對很小的金色圈形耳環、左鼻翼的金色鼻釘、Apple Watch(米色錶帶)。**沒有戒指。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **【第一辨識點】左鼻翼的小金色鼻釘。** 任何人像、任何側臉(左側)都必須有。
2. **笑起來歪向右邊**(右邊嘴角先動)。
3. **深棕色長捲髮,中分。**
4. **左手腕的黑色髮圈。**
5. **不可以出現的:** 雀斑、白髮或灰髮挑染、眉毛上的疤、臉上任何疤痕、手指上的疤、鯊魚夾、插在髮髻上的筆。
   (前五樣已被其他人物用作辨識點,後兩樣是其他人物的造型,都不屬於她)

### 3.5 眼鏡

**只有開車與看遠時戴。** 一副**細金色金屬框、圓角方形(panto)的眼鏡**,平常夾在駕駛座遮陽板上。
→ **她戴眼鏡 = 她在車裡。** 車內畫面一定戴,車外畫面一定不戴(除了外訪看門牌的時候)。

### 3.6 表情庫(九宮格)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 在聽:頭微偏,眉毛放鬆,眼睛往下看著別人的手 | 70% 的畫面 |
| **watching the hands** | 身體前傾,手放膝蓋上不動,眼睛跟著別人的手指 | 家人在用遙控器、受訪者在操作 |
| **half-smile** | **右邊嘴角先動**,左邊跟上一半 | 她最常見的笑 |
| **real laugh** | 頭往後一點,眼睛瞇起來,**嘴歪向右邊**,手擋一下嘴 | tatik、Joelle |
| **unconvinced** | 嘴唇抿著、下巴微收、一邊眉毛抬,**很禮貌** | 有人說「我明年一定會…」(包括她自己在鏡子裡) |
| **delighted** | 眼睛睜大,手指著某個方向,「你看」 | 一個人三秒就找到她以為會卡住的東西 |
| **tired** | 眼下暗,頭靠在車窗上,髮圈鬆了 | 405 兩小時之後 |
| **polite (stressed)** | **左右完全對稱的笑,眼角不動** | **媽媽問「看得怎樣」的時候。** 對稱的笑 = 她在擋 |
| **reading the road** | 戴眼鏡,眼睛微瞇看遠方,下巴微抬 | 車內 |

**❌ 絕對不出現的表情:** 誇張大笑、比讚、比 YA、嘟嘴、對鏡頭眨眼、網紅式的驚訝摀嘴、「快樂上班族」的圖庫笑容。

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | 中音女聲(mezzo),基頻約 **200–220 Hz** |
| 語速 | **偏快,約每分鐘 165 詞。** 講到時間與步驟時會一個一個數出來 |
| 口音 | **南加州的一般美式口音**,母音平,**不要做成刻板的 Valley girl 腔**(不要大量氣泡音、不要每句尾上揚) |
| 音色 | 清亮,一點點沙,**晚上比較低** |
| 特徵 | **訪談模式:放慢、很多「mm-hm」、停頓很長、讓對方先講** |
| 笑聲 | 短的兩聲 "ha-ha",嘴角歪向右邊 |
| 填充詞 | "okay", "so", "like"(中等)、"anyway" |
| 情緒起伏 | 中。**講到 tatik 的時候會軟下來** |
| 絕不出現 | 播報腔、廣告腔、"Hey guys!"、"you guys"、ASMR 氣音 |

### 3.8 鏡頭前的肢體習慣

- **看手。** 有人在用東西時,她的視線一定落在對方的手上。招牌動作。
- **手不動。** 看別人操作時,她會把自己的手放在膝蓋上或抱在胸前,讓對方的手是畫面裡唯一在動的。
- **模仿剛剛看到的動作。** 看完一個人怎麼按,她會用自己的手在空中重複一次那個動作(她在記)。
- 講路線時用食指在空中畫線(爸爸教的)。
- 想事情的時候轉手腕上的髮圈。
- **不看鏡頭。** 她看手、看路、看樓名。要看鏡頭是刻意的,而且短。

### 3.9 拍照與自拍行為(決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **一年 2–4 張。** 通常是車窗或停車場玻璃的倒影,左半張臉,**鼻釘看得到** |
| 出現在畫面裡的方式 | **她自己的手、家人的手、背影、車內的局部。** 臉極少 |
| 拍什麼 | **樓名與城市(40%)、手(30%)、車內與路(20%)、桌子(10%)** |
| 構圖 | 正面平拍(樓名)、俯拍(手與桌)、駕駛座視角(停車時) |
| 後製 | **不調色,只裁切。** 偶爾把手機畫面上的通知裁掉 |
| 器材 | iPhone 15 |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「手」與「樓名」,不是「臉」。家人永遠只有手。**

---

## 四、服裝系統(三套 + 變體)

外型必須對得起 `02 § 10`:**錢花在帶得走、用得久的東西上。** 沒有任何看得見的 logo。

### 4.1 Office Day(週二到週四,Burbank)

```
- 一件淺藍色的寬版牛仔布襯衫(敞開或扣兩顆),裡面白色素 T
- 深靛藍直筒牛仔褲,褲腳反摺一次
- 白色皮革休閒鞋,鞋頭有一點摺痕
- 灰色帆布托特包,裡面是那個「桌包」
- 公司識別證掛繩,收在包裡(進大樓才拿出來)
- 頭髮在頸後綁低馬尾,黑色髮圈
- 開車時:細金框眼鏡
```

### 4.2 Field Visit(外訪日,到受訪者家)

```
- 深藍色的素面圓領大學 T(沒有字)
- 同一條牛仔褲
- 乾淨的白色休閒鞋(進別人家前會看一眼鞋底)
- 一個深灰色的硬殼箱(測試裝置、小腳架)
- 頭髮綁起來
- 沒有任何耳環以外的首飾(她不想讓受訪者分心)
```

### 4.3 Home / Session Day(週一、週五,遠端訪談)

```
- 一件柔軟的淺灰色圓領針織衫(鏡頭裡看得到的上半身)
- 下半身:灰色棉質運動褲(鏡頭外)
- 頭髮放下來,或用髮圈綁半頭
- 不穿鞋,穿襪子
- 左手腕的髮圈
```

### 4.4 Weekend / Climbing / Ballona Creek

```
- 攀岩:黑色背心、深灰色寬鬆長褲、粉袋
- 騎車:一件褪色的鼠尾草綠帽 T、黑色緊身短褲、運動鞋、安全帽
- 週日去 Glendale:一件深綠色的針織洋裝或襯衫(媽媽會說「你今天看起來很好」的那一件)
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | Apple Watch,米色運動錶帶 |
| 耳環 | 一對很小的金色圈形耳環 |
| 鼻釘 | 左鼻翼,2 mm 金色 |
| 髮圈 | 黑色細髮圈,左手腕 |
| 包 | 灰色帆布托特包(通勤)、深灰色登山背包(後車廂的應急包,不是日常包) |
| 手機 | iPhone 15 + 透明殼 + **淺棕色皮革 MagSafe 卡套(背帶款)** |
| 鑰匙圈 | **一顆藍色的小眼睛珠子(tatik 給的)**,串在車鑰匙上 |
| 眼鏡 | 細金框,只在車裡 |
| **不戴的** | 戒指、項鍊、名牌包、精品錶、任何有大 logo 的東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

### 五個不可變的錨(Immutable Anchors)

1. **左鼻翼的小金色鼻釘**,任何左側與正面的畫面必須有
2. **深棕色長捲髮、中分**,不准拉直
3. **笑起來歪向右邊**(禮貌的笑才對稱)
4. **左手腕的黑色髮圈**
5. **車內一定戴細金框眼鏡,車外一定不戴**

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 網美、時尚模特、精緻妝感 | 她一天化妝三分鐘(睫毛膏、潤色護唇膏) |
| 2 | 頭髮被拉直、變成大波浪造型 | 第一輪廓 |
| 3 | 精品包、名錶、大 logo | 違反 `02 § 10` 的消費邏輯 |
| 4 | 好萊塢、海灘比基尼、棕櫚樹夕陽 | 洛杉磯刻板印象 |
| 5 | 豪車內裝、看得見的車廠標誌 | 她開一台 2014 年的 Prius |
| 6 | 對鏡頭笑、比讚、power pose | 圖庫感 |
| 7 | 出現任何串流 App 的畫面、片名、電視上的節目 | **公司背書的暗示(`08 § 9.6`)** |
| 8 | 家人的臉 | **家人永遠只有手** |
| 9 | 出現可辨識的真實品牌 logo 或真實人物 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段 |

### 連續性檢查表(每次出圖後跑)

- [ ] 左鼻翼的金色鼻釘在嗎?有沒有被畫到右邊?
- [ ] 有笑意的圖,是不是右邊嘴角先動?(真笑歪向右,禮貌笑才對稱)
- [ ] **有沒有被畫出酒窩?**(不可以:酒窩是 `persona_ca_949` 的辨識點)
- [ ] 頭髮是深棕色長捲髮、中分?有沒有被拉直?
- [ ] 左鼻翼的金色鼻釘在嗎?位置對嗎(左邊)?
- [ ] 左手腕有黑色髮圈嗎?
- [ ] 車內戴眼鏡、車外不戴?
- [ ] 皮膚有沒有被磨皮?
- [ ] 有沒有出現雀斑、白髮、眉毛疤、鯊魚夾、插在頭髮上的筆?(不可以)
- [ ] 畫面裡有沒有任何 App 介面、電視節目、車廠標誌、品牌 logo?(不可以)
- [ ] 家人有沒有露臉?(不可以)
- [ ] 場景是不是南加州的光?

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, available light only, Southern California
daylight, mild grain, no retouching, visible skin texture and pores,

a 29-year-old Armenian-American woman, 160cm, slim with toned climber's forearms,
long oval face with a soft jawline,
light warm olive skin (#C9A27E), no freckles, a small blemish near the chin,
large dark brown almond eyes with a clear double eyelid,
full natural eyebrows with a gentle arch, clearly separated,
a long straight nose with a slightly downturned tip, full lips with a thinner upper lip,
no dimples,
a tiny 2mm gold stud in her LEFT nostril,
long voluminous dark brown curly hair (#2B1E18), mixed loose and tight curls,
center part, falling just below the shoulders, not straightened,
a thin black elastic hair tie around her left wrist,
small gold hoop earrings, short unpolished nails, no rings,

attentive listening expression, head slightly tilted, eyes on someone's hands
or on the object in front of her rather than at the camera,

colour palette: sea glass #9FC5C0, stucco cream #E9D9C4, tan leather #B5835A,
asphalt slate #2F3A40, with a small accent of Meyer lemon yellow #F2B544 under 5% of frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle showing her left side, a lopsided half-smile
that starts at the right corner of her mouth, the tiny gold stud in her left nostril visible, light blue chambray shirt over a white tee, hair loose,
soft hazy marine-layer window light from the left, a cream stucco wall outside
the window slightly out of focus, shallow depth of field f/2.8, subject off-centre,

--ar 4:5
```

### 6.3 Full body(停車場四樓,早上 7:10,9:16)

```
[MASTER CHARACTER BLOCK]

full body standing beside the open driver's door of a pale sea-glass-green
2010s compact hybrid hatchback on the top level of a concrete office parking
structure at 7:10 am, low morning sun from the east, long shadows, distant
mountains and a small regional airport runway in the background with a plane
descending, she wears thin gold panto glasses, light blue chambray shirt,
dark straight jeans cuffed once, white leather sneakers, a grey canvas tote
on her shoulder, holding a phone with a tan leather card wallet in her other hand,
no visible car logo, no readable signage,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,1:1)

```
photorealistic close-up photograph, natural morning light through a car
windshield, 50mm lens, shallow depth of field,

close-up of a woman's hands with short unpolished nails and a thin black hair tie
on the left wrist, peeling a worn tan leather MagSafe card wallet off the back of
a smartphone in a clear case, directly above a car cupholder, a black magnetic
vent mount on the air vent in the background with one vent slat wrapped in a
black hair tie, a USB-C cable crossing a small gear selector, grey cloth interior,
no faces, no logos, no readable text,

--ar 1:1
```

### 6.5 Driving / in-car(停好車,9:16)

```
[MASTER CHARACTER BLOCK]

seated in the driver's seat of a 2010s compact hybrid hatchback with a grey
cloth interior, a digital instrument display set high in the centre of the
dashboard near the windshield, a small factory audio screen, engine off,
parked on the top level of a parking structure in early morning light,
she wears thin gold panto glasses, hair in a low ponytail,
a smartphone on a small black magnetic vent mount, a tan leather card wallet
lying in the cupholder, the corner of a worn spiral-bound street atlas with no
readable cover visible in the driver's door pocket, she is eating a piece of
braided sweet bread and looking out at the runway, not at the camera,
shot from the passenger seat, no visible brand logo anywhere,

--ar 9:16
```

### 6.6 Home desk / session morning(4:5)

```
[MASTER CHARACTER BLOCK]

9:55 am on a Friday, sitting at a solid maple desk on black bolt-on steel legs
by the window of a small 1950s Los Angeles apartment, soft grey crew-neck
sweater, hair half up, a laptop open, a 24-inch monitor, a USB microphone,
an Android test phone standing on a small aluminium phone stand plugged into
the laptop, an older tablet lying flat with a cable trailing to a small white
three-port wall charger on a power strip on the floor, five visible cables,
a flat white extension cord running under a rug, she is checking the battery
percentage on the tablet with a slight frown, not looking at the camera,
the window shows a cream stucco apartment building across the street,
no app interfaces visible on any screen, no logos,

--ar 4:5
```

### 6.7 Dingbat sign(她的 IG 主體,1:1,無人)

```
photorealistic documentary photograph, flat frontal composition, midday
Southern California light, a 1957 two-storey cream stucco apartment building
with an open tuck-under carport, a vintage cursive metal script sign on the
facade reading "The Cor l" with one letter missing and a faint shadow where the
"a" used to be, a potted Meyer lemon tree on the upstairs walkway,
no people, no car logos, no house numbers visible,

--ar 1:1
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same woman, identical soft daylight and
framing in every panel, head and shoulders, plain warm grey background,
long dark curly hair with a centre part in every panel:
1 attentive listening with head tilted and eyes looking down,
2 leaning forward with hands still on her knees, eyes following something,
3 lopsided half-smile starting at the right corner of her mouth,
4 a real laugh with eyes crinkled, mouth pulled to the right, hand near her mouth,
5 politely unconvinced with lips pressed and one eyebrow raised,
6 delighted with eyes wide, pointing at something off-frame,
7 tired with head resting against a car window, hair tie loose,
8 a perfectly symmetrical polite closed smile with no eye crinkle,
9 wearing thin gold panto glasses, eyes slightly narrowed reading the road,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
when someone else is using a device she watches their hands, not their face.
she keeps her own hands still on her knees while she watches.
after watching a motion she repeats it once in the air with her own hand.
when describing a route she draws it in the air with her index finger.
when thinking she turns the black hair tie on her left wrist.
in the car she always wears thin gold glasses; out of the car she never does.
she does not look at the camera.

VOICE: mezzo female voice around 210 Hz, about 165 words per minute,
general Southern California American accent with flat vowels, no exaggerated
vocal fry, no uptalk on every sentence, slightly husky at night,
times and steps counted out clearly, a quick two-beat "ha-ha" laugh with the
mouth pulling to the right. in interview mode she slows down and says "mm-hm".
no broadcast energy, no sales tone.

CAMERA: handheld, 35mm, eye level or passenger-seat angle, available light only.
family members appear as hands and voices only, never faces.
```

---

## 七、外型與人設的一致性驗算

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 笑歪向右邊 | `05` 爸爸也是這樣笑 | ✓ |
| **沒有酒窩** | 刻意:避開 `persona_ca_949` 的第一辨識點(`00 § 四` 第 13 項) | ✓ |
| 左鼻釘 | `02` 十八歲自己決定的事(她少數不猶豫的決定) | ✓ |
| 長捲髮、不拉直 | 一天化妝三分鐘、不花時間在造型 | ✓ |
| 攀岩前臂、指腹的繭 | `02 § 8` 一週兩次攀岩 | ✓ |
| 開車才戴眼鏡 | `06 § 五` 輕微近視 | ✓ |
| 手腕上的髮圈 = 出風口上的髮圈 | `03 § 7` 10 月 6 日之後 | ✓ |
| 沒有珠寶以外的貴東西 | `02 § 10` 錢花在帶得走、用得久的東西 | ✓ |
| 坐著時手放膝蓋不動 | `02 § 6` 職業反射(看別人的手) | ✓ |
| 家人只拍手 | `03 § 2-1`、`5-2` | ✓ |
| 沒有雀斑、白髮、疤、鯊魚夾、髮筆 | 刻意:避開與其他人物撞型(`00 § 四` 第 13 項) | ✓ |

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲音、3.8 肢體、6.9 影片提示詞、五個不可變錨。**家人只有手與聲音。畫面裡不能有任何 App 介面。**
**Ivy(Amazon 素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**她是 UX 研究員這件事,不可以出現在任何產品的「好不好用」相關的商業素材上**(專家薦證風險,見 `08 § 9.6`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生成)* | | | |
| full_body_parking | *(本輪未生成)* | | | |
| hands_wallet_detail | *(本輪未生成)* | | | |
| in_car_morning | *(本輪未生成)* | | | |
| home_desk_session | *(本輪未生成)* | | | |
| dingbat_sign | *(本輪未生成)* | | | |
| expression_sheet | *(本輪未生成)* | | | |

> **本輪任務指定不生圖。** 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。
> **第一次出圖要特別檢查:捲髮有沒有被拉直、鼻釘是不是在左邊、有沒有被模型自動加上酒窩。**

---

*檔案版本:v1.0 — 2026-10-21 建立*
