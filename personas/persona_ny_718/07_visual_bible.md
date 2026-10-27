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
character_slug:   rohan-seecharan
display_name:     Rohan "Ro" Seecharan

art_style:        photorealistic documentary photography
                  # 照片。不是 CG、不是插畫、不是 3D、不是時尚大片。
style_reference:  working-photographer BTS look: phone camera or 35mm, mixed practical light
                  (basement work lamp, location window light, van dome light), mild noise,
                  no beauty retouching, visible skin texture, slight motion blur on hands allowed

color_palette:
  - "#1E1F21"   # blackout basement black: 地下室的黑牆、他的衣服、沙袋
  - "#A9ADB1"   # van silver / C-stand steel: 廂型車、腳架、推車的金屬
  - "#ECE7DE"   # seamless paper off-white: 背景紙、麵包紙袋、白底圖
  - "#7A4A2E"   # roti-pan brown: 木頭鋸馬、皮革、他的膚色中間調
  - "#D9A21B"   # Liberty Ave turmeric yellow: 點綴色,手繪招牌與香料的黃,不超過畫面 5%

lighting_default: 現場光與工作光。
                  地下室:一盞工作燈 + 螢幕的光,牆是黑的。
                  拍攝現場:窗光或閃燈的「漏光」,畫面邊緣可以看到燈架或柔光箱的一角。
                  車內:清晨或陰天的擋風玻璃光。
                  **不用環形燈、不用美肌補光、不用霓虹、不用 RGB。**
                  **他是攝影師,畫面裡可以看到別的燈具,但不可以把他打得像時尚雜誌。**

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
plastic skin, airbrushed skin, beauty retouch, glamour lighting, ring light,
softbox catchlight in eyes, neon, RGB lighting, purple LED glow, blue LED glow,
teal-and-orange grade, HDR, oversaturated, cinematic fashion editorial,
fashion photographer, black turtleneck, beret, film camera around neck,
vintage camera prop, influencer pose, thumbs up, peace sign, power pose,
stock-photo smile, perfect symmetrical face,
eyeglasses, sunglasses on head, earrings, necklace, gold chain, luxury watch,
smartwatch, designer logo, visible brand logos, streetwear hype logos,
full unbroken beard covering the whole jaw, missing the bare patch on the right jaw,
uniform short boxed beard, grey in the beard, bald head, thin mustache only,
gray hair, white streak in hair, freckles, eyebrow scar, facial scars,
long hair, man bun, dreadlocks, religious headwear,
luxury car interior, sports car, electric sedan interior, visible car brand logo,
anime, illustration, 3d render, cgi, cartoon,
extra fingers, malformed hands, missing tattoo on right index finger,
warped text, unreadable text, watermark
```

**為什麼要排除這些(不是隨便列的):**
- `eyeglasses / earrings / gold chain / luxury watch / smartwatch`:他不戴眼鏡、沒有耳洞、不戴首飾;錶只有一支便宜的黑色電子錶(見 4.5)。
- `full unbroken beard / missing the bare patch`:右下顎那一小塊不長鬍子的地方是辨識點之一,生圖最容易把鬍子補滿。
- `missing tattoo on right index finger`:`1HR` 是第一辨識點,手部特寫最容易漏掉或換手。
- `gray hair / white streak / freckles / eyebrow scar`:**這幾樣已經被其他人物用作辨識點**(Tess 的白髮、台灣人物的雀斑與眉尾疤),也不屬於他。
- `fashion photographer / black turtleneck / film camera around neck`:刻板攝影師形象。他做的是商業產品與餐飲,穿工作服。
- `purple LED glow / blue LED glow`:他對推車與桌上的指示燈在意的是「倒映在產品上」,畫面裡出現會讓人物自相矛盾。
- `religious headwear`:族裔不表演。他是圭亞那印度裔美國人,這不代表任何宗教服飾。
- `electric sedan interior / luxury car interior`:他開的是 2016 年的廂型車;電動轎車是其他美國人物的車。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | Rohan "Ro" Seecharan |
| slug | `rohan-seecharan` |
| age_appearance | **33–37** |
| gender | 男 / cis |
| ethnicity | 圭亞那印度裔美國人(Indo-Guyanese American)。**南亞骨相,加勒比海出生的父母,紐約長大。不偏向任何刻板樣子** |
| build_class | 結實、肩背寬、前臂粗(搬器材),腰不細,不是健身房的身材 |
| location_look | 紐約的室內工作者:膚色冬天偏淡一點,夏天在戶外拍攝之後前臂深一個色階 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | 長橢圓偏方,下顎線清楚 | |
| **膚色** | `#8D5B3E` 中深的暖棕色 | 圭亞那印度裔 |
| **膚質** | **有毛孔,額頭與鼻翼有一點油光,下巴有幾個舊的刮鬍刀小點**。眼下有淡淡的暗沉 | 反美肌,35 歲,睡不夠 |
| **眼睛** | 深棕色,**上眼皮略重**,眼尾平 | |
| **眉毛** | 濃、平直、自然,眉頭幾乎連在一起(他不修) | |
| **鼻子** | 鼻樑直,鼻頭略寬 | |
| **嘴** | 中等偏厚,下唇比上唇厚 | |
| **鬍子** | **黑色,兩頰修短(約 5 mm)、下巴留長約 2 cm,兩頰的線剃得很清楚(跟髮線同一個理髮師)。右下顎靠近耳朵下方有一塊約 2 cm 的天生不長鬍子的地方** | 第二辨識點。他不在意,不補。**下巴留長是為了跟「短而整齊的全臉鬍」拉開**(`00 § 四` 第 13 項) |
| **表情基準** | **專注,左眼微微瞇著**(用右眼看觀景窗看了二十年的習慣) | 見 3.6 |

### 3.2 頭髮

- 黑色,短,**兩側推短(taper fade),頭頂約 3 cm,前額的髮線剃得很清楚(line-up)**。
- 每三週在 Liberty Ave 同一間理髮店剪一次(他爸也在那剪)。**拍攝前一天剪。**
- 冬天戴一頂黑色毛帽。

### 3.3 身體

- **身高 180 cm(5'11")。體重約 84 kg。**
- 肩背寬,前臂粗,手背有幾條舊的小擦傷(器材箱的邊)。
- **姿勢:站的時候重心在兩腳,手常常插在工作褲的大腿口袋裡。** 坐著修圖時脖子往前。
- 搬完器材會蹲下來,手扶著膝蓋伸展下背。
- 手:**大、指甲短、指節粗**。**右手食指外側(第一與第二指節之間)刺著 `1HR`,約 1.2 cm,黑色,手繪招牌字體。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **【第一辨識點】右手食指外側的 `1HR` 刺青。** 任何手部特寫都必須有,**必須是右手**。
2. **右下顎一塊約 2 cm 不長鬍子的地方。** 任何正臉與右側臉都必須有。
3. **左眼微瞇的專注表情。**
4. **不可以出現的:** 眼鏡、耳環、白髮、雀斑、眉毛上的疤、臉上任何疤痕(這些已經被其他人物用作辨識點,也不屬於他)。

### 3.5 眼鏡

**不戴。** 視力正常。修圖到半夜時眼睛會乾,他會用拇指與食指按眼角。

### 3.6 表情庫(九宮格)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 專注,左眼微瞇,嘴閉著,視線看著手上的東西或螢幕 | 70% 的畫面 |
| **edge zoom** | 頭往前,手機拿近,兩指放大,眉頭輕皺,在看照片的邊緣 | 看商品頁 |
| **half-grin** | 嘴角一邊往上,不露牙 | 他最常見的笑 |
| **real laugh** | 頭往後一點,露出牙,眼睛瞇起來,短促的一聲 | 跟 Theo、Kavi |
| **that's a comp** | 一邊眉毛抬起,嘴角往下壓,看著手機不看人 | 看到太完美的主圖 |
| **delighted** | 眼睛睜大,微笑,把手機轉過去給旁邊的人看 | 買家實拍跟主圖一模一樣 |
| **tired** | 眼下加深,毛帽歪了,一隻手撐著臉 | 充電排班的凌晨一點 |
| **clock face** | 下巴收緊,看著手腕上的錶,不看人 | 客戶在等、筆電掉電 |
| **sandbag it** | 整個人停住,手掌朝下往下壓的手勢 | 看到沒壓住的東西 |

**❌ 絕對不出現的表情:** 對鏡頭比讚、比 YA、嘟嘴、時尚雜誌式的冷臉、網紅式的驚訝摀嘴、「開心的上班族」圖庫笑容。

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | 中低的男聲(baritone),基頻約 **110–125 Hz** |
| 語速 | **偏快,約每分鐘 165 詞**。講到時間時會放慢、一個字一個字講(`"six. thirty."`) |
| 口音 | **紐約 Queens 口音**:`coffee` 的母音拉長、`talk` 偏 `tawk`;跟家人講話時會滑進一點圭亞那的語調 |
| 音色 | 乾淨,略粗。**清晨第一句話很低** |
| 特徵 | **講行話時變短變快**("Wrap." "Sandbag that." "We're rolling.") |
| 笑聲 | 短的一聲 "heh",從喉嚨出來 |
| 填充詞 | "like"、"bro"(只對 Kavi 與 Theo)、"honestly" |
| 情緒起伏 | 中。**看到好的實拍會講快、會把手機轉給別人看** |
| 絕不出現 | 播報腔、廣告腔、"Hey guys!"、"What's up YouTube"、氣音、刻意的口音表演 |

### 3.8 鏡頭前的肢體習慣

- **進任何空間先找插座,然後找出口。** 招牌動作,任何換場鏡頭都可以用。
- **看手機上的照片時,兩指放大,一路滑到四個角。**(edge zoom)
- **把沙袋放下時,用手掌往下壓一次。**
- 數電池時用指尖一顆一顆點過去。
- 相機背帶在右手腕上繞一圈。
- 看錶:**左手腕的便宜黑色電子錶,他看的是 call time 的倒數計時。**
- **不看鏡頭。** 他看螢幕、看產品、看錶。要看鏡頭是刻意的,而且短。

### 3.9 拍照與自拍行為(決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **一年 1–3 張。** 通常是拍攝現場鏡面產品裡的倒影,或 Theo 偷拍的 |
| 出現在畫面裡的方式 | **手、推車旁邊的側身、搬器材的背影。** 臉少 |
| 拍什麼 | **成品(30%)、BTS(35%)、passport photo 系列(20%)、紐約的街與車(15%)** |
| 構圖 | **成品照是專業的;BTS 與 passport photo 故意不修、平光、正面** |
| 後製 | 成品照:修(這是工作)。**passport photo 與 BTS:不修,只裁切** |
| 器材 | 成品:全片幅無反;BTS 與日常:Galaxy S25 Ultra |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「之前 / 之後」與「手」,不是「臉」。**
> **而且所有「之前」都會是 AI 生成的,見 `08 § 9.5`:這是這個人物最大的合規矛盾。**

---

## 四、服裝系統(三套 + 變體)

外型必須對得起 `02 § 10`:**錢花在推車與車上,不花在身上。** 沒有任何看得見的 logo。

### 4.1 Shoot Day(拍攝日)

```
- 黑色帆布工作褲,大腿有側袋,膝蓋磨白
- 深灰色厚棉 T 恤(他有五件一樣的),冷的時候外面加一件黑色拉鍊連帽外套
- 一條黑色帆布腰圍裙,口袋上夾著兩個橘色把手的 A-clamp 與一支白色油漆筆
- 黑色皮革工作球鞋,鞋頭磨出白痕
- 左手腕:便宜的黑色電子錶
- 冬天:黑色毛帽
- 右手:相機或手機
```

### 4.2 Off Day(地下室、ASP 早上、器材出租行)

```
- 灰色圓領運動衫,袖口鬆了
- 深藍色牛仔褲
- 白色帆布鞋,髒的
- 黑色電子錶
- ASP 早上:同一套,外面加一件 Inés 說「很醜」的橄欖綠工作夾克
```

### 4.3 Sunday(Richmond Hill 爸媽家)

```
- 一件媽媽燙過的淺藍色素面襯衫,袖子捲到手肘
- 卡其褲
- 黑色皮革休閒鞋
- 這是一週唯一他「穿好」的一天,而且是為了媽媽
```

### 4.4 Driving(車內畫面)

```
- 依當天是 4.1 或 4.2
- 副駕腳踏墊上的 ABRAMS 4 沙袋
- 2026 年 10 月 2 日之後:手機在儀表板中央上方的置物槽裡,螢幕朝上,靠著摺起來的拭鏡布;
  儀表板上一個圓形的黑色黏貼底座,沒有支架
- 之前(歷史畫面):手機在磁吸支架上,厚防摔殼
- ASP 早上:筆電放在方向盤上
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **便宜的黑色電子錶(約 US$20),有倒數計時**。不是機械錶、不是智慧錶 |
| 鑰匙 | 一個黑色登山扣,掛在褲子的皮帶環上 |
| 首飾 | **沒有。** 沒有耳洞,沒有戒指 |
| 包 | 一個黑色的相機後背包,側袋放充電線 |
| 眼鏡 | **不戴** |
| **不戴的** | 耳環、項鍊、戒指、名錶、智慧錶、任何有大 logo 的東西、底片相機當配件 |

---

## 五、Visual Identity Rules(長期一致性規則)

### 五個不可變的錨(Immutable Anchors)

1. **右手食指外側的 `1HR` 刺青**,必須是右手,不准消失、不准換手、不准變成別的字
2. **右下顎那一塊不長鬍子的地方**,正臉與右側臉必須有
3. **黑色短髮 + 清楚的髮線 + 兩頰短、下巴長的黑鬍子**,換髮型或鬍型等於換人
4. **皮膚有毛孔、有油光、不磨皮**,反美肌
5. **畫面裡要能看出他在工作**:一個器材、一條線、一個沙袋、一台推車,至少一樣

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 時尚攝影師 / 黑高領 / 藝術家氣質 | 他做商業產品與餐飲 |
| 2 | `1HR` 不見、換手、變成別的字 | 第一辨識點 |
| 3 | 鬍子補滿、變成均勻的短全臉鬍、變灰 | 第二辨識點;均勻短全臉鬍與灰鬍是其他人物的設定 |
| 4 | 首飾、名錶、智慧錶、潮牌 | 違反 `02 § 10` 的消費邏輯 |
| 5 | 環形燈、霓虹、RGB、紫色或藍色的光 | 他在意燈倒映在產品上 |
| 6 | 豪車、電動轎車、看得見的車廠標誌 | 他開 2016 年的廂型車 |
| 7 | 對鏡頭笑、比讚、power pose | 圖庫感 |
| 8 | 宗教或民族服飾當造型 | 族裔不表演 |
| 9 | 出現可辨識的真實品牌 logo、真實人物、真實餐廳 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段 |

### 連續性檢查表(每次出圖後跑)

- [ ] 右手食指外側有沒有 `1HR`?是右手嗎?
- [ ] 右下顎的鬍子空缺在嗎?下巴的鬍子有沒有比兩頰長?(不可以變成均勻的短全臉鬍)
- [ ] 頭髮是黑色短髮、兩側推短、髮線清楚?
- [ ] 皮膚有沒有被磨皮?
- [ ] 畫面裡有沒有一樣工作的東西(器材、線、沙袋、推車)?
- [ ] 有沒有出現紫色、藍色、RGB 的光?(不可以)
- [ ] 有沒有首飾、名錶、智慧錶、logo?
- [ ] 臉上、眉毛有沒有被畫出疤?頭髮有沒有白的?(不可以)
- [ ] 沙袋上的字是不是 `ABRAMS 4`?(不是他的名字)
- [ ] 手有沒有畫壞?

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, practical and available light only,
mild noise, no retouching, visible skin texture and pores, slight oily sheen
on forehead and nose,

a 35-year-old Indo-Guyanese American man from Queens, New York,
180cm, solid build with broad shoulders and thick forearms,
long oval face with a defined jaw, medium-deep warm brown skin (#8D5B3E),
dark brown eyes with slightly heavy upper eyelids, thick straight natural
eyebrows that nearly meet in the middle, a straight nose with a slightly
broad tip, medium-full lips,
short black hair with a taper fade on the sides and a crisp lined-up hairline,
a black beard trimmed short on the cheeks (about 5mm) and left longer on the
chin (about 2cm), with sharp shaved cheek lines, and a natural bare patch about
2cm wide on the right jawline below the ear where no beard grows,
a small black tattoo reading "1HR" in hand-painted sign lettering on the outer
side of his RIGHT index finger between the first and second knuckle,
short nails, thick knuckles, a cheap black digital watch on his left wrist,
no glasses, no earrings, no jewelry,

focused expression with his left eye slightly narrowed, looking at the object
or screen in front of him rather than at the camera,

colour palette: blackout black #1E1F21, van silver #A9ADB1,
seamless off-white #ECE7DE, roti-pan brown #7A4A2E,
with a small accent of turmeric yellow #D9A21B under 5% of frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle showing the right side of his jaw,
looking down at a phone held close to his face, pinch-zooming into the corner
of a product photo, one eyebrow slightly raised,
dark grey heavy cotton t-shirt, a black zip hoodie,
basement studio with a matte black wall, a work lamp just out of frame on the
left, the cool glow of a hooded monitor on his face from the right,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,拍攝現場,9:16)

```
[MASTER CHARACTER BLOCK]

full body standing beside a black rolling tether cart in a restaurant kitchen
before service, morning window light, stainless steel counters,
black canvas work trousers with thigh pockets, dark grey t-shirt,
a black canvas waist apron with two orange-handled spring clamps clipped to
the pocket, scuffed black leather work sneakers,
he is looking at the cheap digital watch on his left wrist,
a laptop on the cart's top tray with its screen facing away from camera,
a black saddle-style sandbag with "ABRAMS 4" painted in faded white on the
cart's bottom shelf pinning an extension cord,
a softbox on a stand partly visible at the edge of the frame,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up photograph, single overhead work lamp,
50mm lens, shallow depth of field,

close-up of a man's large hands with short nails and thick knuckles, medium-deep
brown skin, a small black "1HR" tattoo in hand-painted sign lettering on the
outer side of the RIGHT index finger, pressing down once on a black canvas
saddle-style sandbag with "ABRAMS 4" painted in half-worn white letters and
one handle re-stitched in dark grey thread,
the sandbag is pinning a tangle of six charging cables on a matte grey painted
door-slab desk, the cables run back to a glossy black six-port charger with a
row of small blue indicator lights partly covered by a black cloth,
no faces, no logos,

--ar 1:1
```

### 6.5 In-van, ASP morning(9:16)

```
[MASTER CHARACTER BLOCK]

seated in the driver's seat of a silver 2016 compact cargo-style van with a
black interior and a hard textured black dashboard, no visible brand logo
anywhere, double-parked on a Queens street of 1910s tan brick rowhouses,
morning, overcast, a laptop resting on the steering wheel showing a grid of
food photo thumbnails, a smartphone in a thick rugged case lying face up in
the open storage bin on top of the dashboard on a folded microfiber cloth,
a round black adhesive mount base left on the dash with no mount on it,
a basic radio with a slightly bent CD slot,
a black sandbag on the passenger footwell on top of a hard camera case,
an olive work jacket, he is looking at the laptop, not at the camera,
shot from the passenger seat,

--ar 9:16
```

### 6.6 Basement desk / the night before(4:5)

```
[MASTER CHARACTER BLOCK]

late at night in a low-ceiling basement with one matte black painted wall,
sitting at a desk made from an old solid-core door on two wooden sawhorses,
grey sweatshirt, black beanie slightly crooked, tired eyes,
a 27-inch monitor with a black hood, six camera batteries lined up in a row
each marked with one to six small silver paint dots, a dual battery charger,
a glossy black six-port charger with six small blue lights and six cables
pinned under a black "ABRAMS 4" sandbag, a dehumidifier in the corner,
a whiteboard with handwritten times, the cheap digital watch reading 00:28,
he is touching the batteries one by one with a fingertip, not looking at camera,

--ar 4:5
```

### 6.7 BTS / passport photo diptych(16:9)

```
photorealistic diptych, two panels side by side,
left panel: a polished commercial hero shot of a plain unbranded ceramic coffee
mug on a seamless off-white background with soft studio light,
right panel: the same mug photographed straight-on with flat light by a phone,
next to a man's right hand with a "1HR" tattoo on the index finger for scale,
on a grey painted desk, slightly noisy, no retouching,
no logos, no text overlay,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in
every panel, head and shoulders, plain dark grey background, the bare patch on
his right jaw visible in every panel:
1 focused with the left eye slightly narrowed, 2 leaning in pinch-zooming on a
phone with a slight frown, 3 a one-sided closed-mouth grin, 4 a real laugh with
head tipped back, 5 one eyebrow raised and mouth corners pressed down looking at
a phone, 6 delighted with wide eyes turning a phone toward someone, 7 tired with
deeper under-eye shadows and a crooked beanie, 8 a tightened jaw looking at a
cheap digital watch, 9 completely still with one palm pressing downward,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
when he enters a space he looks for the power outlets first, then the exit.
he checks photos on his phone by pinch-zooming and swiping to all four corners.
when he sets down a sandbag he presses it down once with his palm.
he counts batteries by touching each one with a fingertip.
he checks a cheap digital watch on his left wrist for the call-time countdown.
he does not look at the camera; he looks at the screen, the product or the watch.
after lifting gear he squats briefly with hands on knees to stretch his lower back.

VOICE: baritone male voice, around 115 Hz, about 165 words per minute,
Queens New York accent with long "coffee" vowels, times spoken slowly word by
word ("six. thirty."), crew jargon spoken short and fast ("wrap", "sandbag that"),
a single short "heh" laugh from the throat. no broadcast energy, no sales tone,
no "hey guys".

CAMERA: handheld, phone-like or 35mm, slight drift, eye level or chest level,
practical light only, at least one piece of working gear visible in frame.
```

---

## 七、外型與人設的一致性驗算

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| `1HR` 刺青,右手食指外側 | `03 § 6-1` 相館招牌、按快門的手 | ✓ |
| 右下顎鬍子空缺 | 天生,刻意選來避開疤痕型辨識點(`00 § 四` 第 13 項) | ✓ |
| 肩背寬、前臂粗、下背痛 | `06 § 五` 搬器材 | ✓ |
| 左眼微瞇 | 用右眼看觀景窗二十年 | ✓ |
| 沒有首飾、便宜電子錶 | `02 § 10` 錢花在推車與車上 | ✓ |
| 電子錶有倒數計時 | `03 § 2-1` call time | ✓ |
| 五件一樣的深灰 T 恤 | 拍攝日不想選衣服 | ✓ |
| 腰圍裙上的 A-clamp | 商業攝影現場的標配 | ✓ |
| 每三週在 Liberty Ave 剪頭髮 | `01 § 1-A`、他爸也在那剪 | ✓ |
| 週日的襯衫是媽媽燙的 | `05 § 3` | ✓ |
| 幾乎不入鏡,主體是手與「之前 / 之後」 | `03 § 1-2` 護照照片 | ✓ |

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲音、3.8 肢體、6.9 影片提示詞、五個不可變錨。**畫面裡一定要有一樣工作的東西。**
**Ivy(Amazon 素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**他是商業攝影師這件事,不可以出現在任何 SPACION 的商品圖、主圖、BTS、或「這張圖沒修過」的宣稱裡**(專家薦證風險,見 `08 § 9.6`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生成)* | | | |
| full_body_set | *(本輪未生成)* | | | |
| hands_sandbag | *(本輪未生成)* | | | |
| in_van_asp | *(本輪未生成)* | | | |
| basement_night_before | *(本輪未生成)* | | | |
| expression_sheet | *(本輪未生成)* | | | |

> **本輪任務指定不生圖。** 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。
> **第一次出圖要特別檢查 `1HR` 是不是在右手、右下顎的鬍子空缺有沒有被補滿**,這是這個人物最容易失敗的兩個地方。

---

*檔案版本:v1.0 — 2026-10-21 建立*
