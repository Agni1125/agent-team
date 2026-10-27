# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
> **本輪不生圖,seed 表留空。**
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。
> **硬約束:任何畫面都不得出現孩子(臉、身體、背影、倒影都不行),也不得生成任何未成年人的圖像。**

---

## 一、Visual Anchor(視覺錨點:最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   andre-whitfield
display_name:     Andre Whitfield

art_style:        photorealistic documentary photography
                  # 照片。不是 CG、不是插畫、不是企業形象照、不是汽車廣告。
style_reference:  pre-dawn and late-afternoon North Carolina light, iPhone-like or 35mm look,
                  mild noise in low light, no beauty retouching, visible skin texture,
                  suburban practical light (porch lights, parking lot lights, a laptop screen, a car's center screen)

color_palette:
  - "#1E2A3E"   # pre-dawn van navy:他的車、他的連帽衫、天亮前的天空
  - "#9C4A2F"   # Piedmont red clay:北卡的土、磚、他那件褪色的紅 T 恤
  - "#3B5A3A"   # loblolly pine green:社區的松樹、後院
  - "#8FB9C2"   # pool-lot blue:室內游泳中心外牆透出來的光
  - "#F2E27D"   # legal-pad yellow:黃色便條本。唯一的亮色,點綴用,不超過畫面 5%

lighting_default: 現場光(available / practical light only)。
                  清晨:天亮前的深藍天空 + 停車場燈 + 車內螢幕的光。
                  白天:北卡的硬太陽或陰天,窗光為主。
                  晚上:門廊燈、廚房燈、筆電螢幕。
                  **不用棚燈、不用環形燈、不用企業形象照的打光。**

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
child, children, kid, kids, toddler, teenager, minor, schoolchild, baby, young girl, young boy,
child in back seat, child silhouette, child reflection,
plastic skin, airbrushed skin, beauty retouch, glamour lighting, corporate headshot,
stock-photo businessman, LinkedIn headshot pose, arms crossed power pose, thumbs up,
athlete, sports jersey, football uniform, team logo, university logo, mascot,
gold chain, necklace, earrings, luxury watch, designer clothing, visible brand logos,
company logo, readable ID badge, lanyard with logo, readable text, readable handwriting, watermark,
phone mounted on dashboard, phone mount, dash mount, vent clip, suction cup mount,
aftermarket car accessories, LED light bar, dashcam, air freshener,
luxury car interior, sports car, visible car brand logo,
studio lighting, ring light, softbox, neon lights, RGB lighting, cyberpunk, HDR, oversaturated,
anime, illustration, 3d render, cgi, cartoon,
extra fingers, malformed hands, warped text, glasses, beard with a single grey streak, freckles,
eyebrow scar, facial scar, nose scar, cheek dimple, protruding ears, ears sticking out
```

**為什麼要排除這些(不是隨便列的):**
- `child / kids / teenager / minor ...` — **孩子不入鏡是硬規則**(`08 § 9`)。生圖模型在「爸爸 + 小廂型車 + 泳池」這組提示詞下,**極容易自動補一個孩子**。全部要擋。
- `phone mounted on dashboard / vent clip / dash mount` — **他的車上沒有支架**(`06 § 二`)。模型看到「手機 + 開車」會預設畫一個支架,這會讓人物自相矛盾,也可能被誤讀成產品暗示。
- `aftermarket car accessories / LED light bar` — 他「沒跟著來的就不裝」;那是鄰居 Gary 的車。
- `athlete / jersey / team logo / university logo` — 他高中打過美式足球,但**不能被畫成運動員**;大學球隊標誌是真實商標。
- `stock-photo businessman / LinkedIn headshot pose / corporate headshot` — 「成功黑人主管」圖庫照是這個人物最大的視覺陷阱(`04 § 16`)。
- `gold chain / luxury watch / designer clothing` — 他的錢花在原廠整合,不花在別人看得到的地方(`02 § 10`)。
- `beard with a single grey streak / eyebrow scar / freckles / cheek dimple` — **撞型禁區**:單側白髮、眉尾疤、雀斑、左頰酒窩已被其他人物使用(`00 § 四`)。他的灰鬍子是**均勻的**。
- `protruding ears / ears sticking out` — 招風耳是 `persona_ca_949` 的第一辨識點(2026-10-21 收尾 QA)。他的耳朵是一般貼頭的耳朵;**他的第一辨識點是後腦右下方的胎記**,模型常把它畫丟或畫成疤。
- `glasses` — 他不戴眼鏡(手機字體調大一級,他不承認)。
- `readable ID badge / company logo` — 公司永不具名。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | Andre Whitfield |
| slug | `andre-whitfield` |
| age_appearance | **39–44** |
| gender | 男 / cis |
| ethnicity | 非裔美國人(北卡東部)。**不偏向任何刻板的樣子** |
| build_class | 高、壯、大骨架,有一點中年的肚子。前進攻線球員的底子,二十年後 |
| location_look | 北卡的戶外光:夏天比冬天深一個色階,前臂比上臂深(開車與煙燻爐) |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | 方中帶圓,下顎寬,臉頰飽滿 | 大骨架 |
| **膚色** | `#6E4630` 深暖棕色。夏天更深 | |
| **膚質** | 有毛孔,額頭與鼻翼在熱天微微出油,眼下有一點細紋 | 反美肌,41 歲,一週三天 4:55 起床 |
| **眼睛** | 深棕色,眼皮略重,**看起來永遠有一點睏**(他不是,他只是慢) | 游泳日 |
| **眼角** | 笑的時候有魚尾紋 | |
| **眉毛** | 濃、自然、平,不修 | |
| **鼻子** | 寬鼻翼,鼻樑直 | |
| **嘴** | 厚唇,嘴角自然微微下垂(不笑時看起來嚴肅) | 跟父親一樣,Tamara 說的 |
| **鬍子** | **短而整齊的全臉鬍,修得很乾淨的線條;下巴與兩側下顎均勻地灰了大約三成**(不是一撮、不是單側) | 41 歲 |
| **頭** | **光頭,自己每週剃兩次,乾淨** | 2015 年髮線後退之後就剃了 |
| **【第一辨識點】胎記** | **後腦右下方、右耳後上方一塊拇指大小、邊緣不規則的深咖啡色胎記,比膚色深兩階,平的。光頭讓它從背後與側面都看得到;正面看不到,正面靠光頭與均勻灰的鬍子辨識** | 天生的。**不是疤、不凸起、不發紅** |
| **表情基準** | **平靜、睏、在聽** | 見 3.6 |

### 3.2 頭與頭部輪廓

- **光頭,皮膚有自然的光澤,不是反光的油亮。**
- 後腦有兩條淺淺的皮膚摺痕(低頭看手機或便條本時)。
- 熱天會戴一頂**褪色的紅色鴨舌帽,沒有任何字或標誌**。

### 3.3 身體

- **身高 191 cm(6'3")。體重約 102 kg。**
- 肩寬、胸厚、手臂粗,中年的肚子。**站著時重心在右腳(左膝)。**
- **姿勢:頭微微往前,高個子長年低頭聽人講話的習慣。** 進門會本能地低一下頭(其實不用)。
- **下樓梯時左膝會響一下**(影片裡可以有聲音)。
- 手:**很大**,指甲剪得短、乾淨。左手無名指一只**素面的黃金婚戒**(唯一的珠寶)。右手腕 Apple Watch,黑色運動錶環。
- 左膝有一道開刀的舊疤(**只在穿短褲時看得到,不當辨識點**,避開與其他人物的疤撞型)。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **【第一辨識點】後腦右下方的胎記**,背面與側面的畫面都必須在,**不可以畫丟、畫成疤或畫成凸起**;正面畫面靠光頭與均勻灰的鬍子辨識。
2. **光頭 + 均勻灰的短全臉鬍。** 換髮型等於換人。
3. **191 cm 的身高與微微前傾的頭。**
4. **不可以出現的:** 雀斑、眉毛上的疤、臉上任何疤痕、手指上的疤、單側白髮或單側灰鬍、眼鏡(這些已被其他人物用作辨識點,也不屬於他)。

### 3.5 眼鏡

**不戴。** 41 歲,近距離開始有一點吃力。**他把手機的字體調大了一級,他說沒有。**
→ 畫面:看便條本時會把手臂伸遠一點。**不要畫成戴老花眼鏡**(撞型,見 `00 § 四`)。

### 3.6 表情庫(九宮格)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 平靜,眼皮略重,嘴角自然下垂,看起來在聽 | 70% 的畫面 |
| **listening** | 頭微微側、下巴往下收,看著對方或看著便條本 | 1:1、電話 |
| **half-smile** | 閉著嘴笑,嘴角往上、眼角先動 | 他最常見的笑 |
| **real laugh** | 頭往後一點、肩膀抖、眼睛瞇起來,**兩頰的笑紋很深** | 跟 T、跟 Gary、Caleb 講天氣 |
| **bless it** | 眉毛往上、嘴唇抿平、很慢地點頭 | 看到 Gary 又加裝了什麼 |
| **lane 4** | 手上的碼錶放下,胸口挺起來,嘴唇抿緊在忍笑 | 孩子碰牆的那一下(**孩子不入鏡**) |
| **pre-dawn** | 眼睛半睜,雙手捧著保溫杯 | 5:15 的車道 |
| **thinking** | 一隻手掌摸著自己的後腦,視線往下 | 管理職的問題(**不講是什麼**) |
| **eyes up** | 雙手在方向盤九點與三點,視線看遠方的路,臉完全平靜 | 開車 |

**❌ 絕對不出現的表情:** 對鏡頭比讚、雙手抱胸的「主管」姿勢、誇張大笑、對鏡頭眨眼、「成功人士」的自信微笑。

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | 低沉男中音(baritone),基頻約 **100–110 Hz** |
| 語速 | **慢,約每分鐘 125–135 詞。** 句子之間有停頓 |
| 口音 | **北卡東部的南方口音,被 Raleigh 二十年磨平了一半。** 母音拉長一點點,"y'all"、"fixing to" 自然出現。**累的時候口音會跑回來** |
| 音色 | 溫、厚、有一點沙 |
| 特徵 | **講父親的話時,會模仿父親更平、更慢的語氣**("Eyes up.") |
| 笑聲 | 低沉的兩聲 "heh, heh",肩膀先動 |
| 填充詞 | "Now,"(句首)、"I mean,"、"see," |
| 情緒起伏 | 小。**講到孩子的比賽時會快一點** |
| 絕不出現 | 播報腔、廣告腔、激勵演講的語氣、"Hey guys!"、LinkedIn 式的結尾問句 |

### 3.8 鏡頭前的肢體習慣

- **用整隻手指方向,掌心朝上,不用一根手指。** 父親在駕訓車上教學生看路標的手勢。
- **上車的固定順序:** 坐好 → 手機放上中控台的充電座 → 等 CarPlay 出現 → 才換檔。**每一次都一樣。**
- 想事情的時候**一隻手掌摸自己的後腦**。
- 聽人講話時**坐在椅子前緣,前臂放在膝蓋上**。
- **不看鏡頭。** 他看路、看便條本、看爐子的溫度。要看鏡頭是刻意的,而且短。
- 拿東西時用整隻手掌托著,很小心(他手大,小東西會掉)。

### 3.9 拍照與自拍行為(決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **一年 0–2 張。** 通常是跟父親的合照(父親同意的) |
| 出現在畫面裡的方式 | **手、背影、側面、車窗倒影。** 臉偶爾 |
| 拍什麼 | **天色與天氣(40%)、煙燻爐與食物(30%)、車與路(15%)、北卡的地方(15%)。** 孩子 0% |
| 構圖 | 普通。**不擺拍,他不會擺** |
| 後製 | **不調色、不加濾鏡。** 偶爾裁切 |
| 器材 | iPhone 16 Pro |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「天色、爐子、車、手」,不是「臉」,永遠不是孩子。**

---

## 四、服裝系統(三套 + 變體)

外型必須對得起 `02 § 10`:**錢花在原廠整合,不花在別人看得到的地方。** 沒有任何看得見的 logo。

### 4.1 Swim Morning(游泳日清晨,一週三次)

```
- 深藍色拉鍊連帽衫,沒有任何字
- 灰色運動長褲
- 拖鞋加白襪(他知道,他不在乎)
- 一頂褪色的紅色鴨舌帽,沒有任何字或標誌(天冷時換深灰毛帽)
- 手上:不鏽鋼保溫杯
```

### 4.2 Office(進辦公室,週二到週四)

```
- 炭灰色圓領毛衣,裡面是淺藍色牛津襯衫,領子翻出來
- 深海軍藍卡其褲
- 白色皮革休閒鞋,沒有 logo
- Apple Watch,黑色運動錶環
- 素面黃金婚戒
- 肩上一個深灰色後背包(公司的筆電內袋 + 黃色便條本)
```

### 4.3 Home / Weekend(在家工作、週末、煙燻爐)

```
- 一件洗到褪色的紅土色 T 恤,沒有任何字
- 卡其短褲(看得到左膝的舊疤)
- 煙燻日:一件舊的灰色帆布圍裙
- 赤腳或拖鞋
```

### 4.4 Meet Day(游泳比賽日,約兩週一次)

```
- 深藍色防風外套
- 脖子上掛著黑色碼錶,藍色繩子
- 手上一塊計時板夾(上面的字不可讀)
- 一張折疊椅在泳池看台下
- **畫面裡不得出現任何孩子、泳隊名、泳衣上的字**
```

### 4.5 Driving(車內畫面)

```
- 依當天是游泳日或辦公室日(4.1 或 4.2)
- 中控台下方的無線充電座上躺著手機,螢幕朝上
- 9 吋螢幕上是 CarPlay 的地圖(螢幕上的字不可讀)
- 儀表板上什麼都沒有
- 車頂的太陽眼鏡盒關著(或翻下來,紅色抹布包著的鏡子)
```

### 4.6 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | Apple Watch,黑色運動錶環。**不是機械錶、不是精品錶** |
| 戒指 | 素面黃金婚戒,左手無名指。**只有這一只** |
| 帽子 | 褪色紅色鴨舌帽(無標誌);冬天深灰毛帽 |
| 包 | 深灰色後背包 |
| 碼錶 | 比賽日,藍色繩子 |
| **不戴的** | 項鍊、耳環、手鍊、太陽眼鏡、任何有大 logo 的東西、識別證外露 |

---

## 五、Visual Identity Rules(長期一致性規則)

### 五個不可變的錨(Immutable Anchors)

1. **後腦右下方的胎記**,背面與側面都要在
2. **光頭 + 均勻灰的短全臉鬍**
3. **191 cm、微微前傾的頭、大手**
4. **皮膚有毛孔、不磨皮**,反美肌
5. **畫面裡沒有孩子;車上沒有支架**

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 企業形象照、圖庫的「成功主管」 | 最大的視覺陷阱 |
| 2 | 運動員、球衣、球隊標誌 | 他打球是十八歲以前的事;標誌是真實商標 |
| 3 | 金鍊、名錶、名牌 | 違反 `02 § 10` |
| 4 | **畫面裡出現孩子(任何形式)** | 硬規則 |
| 5 | **儀表板上出現手機支架** | 他的車上沒有,而且會被誤讀成產品暗示 |
| 6 | 車上出現任何加裝配件 | 那是 Gary 的車 |
| 7 | 棚燈、環形燈、RGB | 他的畫面是郊區的現場光 |
| 8 | 戴眼鏡、單側灰鬍、臉上的疤 | 撞型 |
| 9 | 出現可辨識的真實品牌 logo、公司名、車廠標誌 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段 |

### 連續性檢查表(每次出圖後跑)

- [ ] 畫面裡有沒有任何孩子(臉、身體、背影、倒影、後座的一隻手)?(**有就整張作廢**)
- [ ] 背面或側面的畫面裡,後腦右下方有沒有胎記?有沒有被畫成疤或凸起?耳朵是不是一般貼頭(不可以招風)?
- [ ] 光頭?鬍子的灰是不是均勻的(不是一撮)?
- [ ] 皮膚有沒有被磨皮?
- [ ] 車內圖:儀表板上有沒有被畫出支架或任何配件?(不可以)
- [ ] 手機在中控台下方的充電座上,螢幕朝上?
- [ ] 有沒有不該有的珠寶、logo、識別證上的字?
- [ ] 有沒有被畫成戴眼鏡?
- [ ] 手有沒有畫壞?便條本上的字是不是不可讀?
- [ ] 鏡子(如果出現):是不是用紅色抹布包著、沒有夾在擋風玻璃上?

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, available light only, practical light
sources visible in the frame, mild noise in low light, no retouching,
visible skin texture and pores,

a 41-year-old African American man from eastern North Carolina,
191cm tall with a big frame, broad shoulders, thick arms and a slight middle-age belly,
a squarish rounded face with full cheeks and a wide jaw,
deep warm brown skin (#6E4630), no freckles, no scars on the face,
dark brown eyes with slightly heavy eyelids that make him look a little sleepy,
thick natural flat eyebrows, a wide nose with a straight bridge,
full lips with corners that turn slightly down when he is not smiling,
a cleanly shaved head with a natural matte sheen,
a short full beard with clean edges, evenly greying about thirty percent at the chin
and both sides of the jaw, no single grey streak,
a thumb-sized flat dark-brown birthmark on the lower right back of his shaved head,
just behind and above the right ear, visible from behind and in profile,
ordinary ears close to the head, no earrings, no dimples,
large hands with short clean nails, a plain yellow-gold wedding band on his left hand,
an Apple-style smartwatch with a black sport band on his right wrist,
no glasses, no other jewelry,

calm listening expression, head tilted slightly forward like a tall man used to
leaning down to hear people, not looking at the camera,

colour palette: pre-dawn navy #1E2A3E, Piedmont red clay #9C4A2F,
loblolly pine green #3B5A3A, pool-lot blue #8FB9C2,
with a small accent of legal-pad yellow #F2E27D under 5% of frame,

no children anywhere in the frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, turned slightly away from camera,
looking down at a yellow legal pad held at arm's length, the handwriting unreadable,
charcoal crew-neck sweater over a light blue oxford collar,
late afternoon window light from the left, a plain bookshelf softly out of focus behind him
with an old dented metal coffee can with a faded label on the top shelf,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,游泳日清晨,9:16)

```
[MASTER CHARACTER BLOCK]

full body standing in a suburban driveway at 5:13 AM before sunrise, deep navy sky,
a single warm porch light behind him, weight on his right leg,
holding a stainless steel travel mug with both hands,
navy zip hoodie with no print, grey sweatpants, slides with white socks,
a faded red baseball cap with no logo or text,
a dark blue minivan parked beside him with its interior dome light on and the
driver's door open, the passenger side empty, nothing on the dashboard,
pine trees as dark silhouettes at the end of the cul-de-sac,
no children, no other people,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up photograph, dim pre-dawn light from a parking lot lamp
through the windshield, 50mm lens, shallow depth of field,

close-up of a man's large hands with short clean nails and a plain yellow-gold
wedding band, holding a folded red cotton shop towel just taken from the
flipped-down overhead sunglasses holder of a minivan, partly unwrapping the towel to show the scratched chrome rim of a small round convex
clip-on mirror, about three inches across, the rubber pad on its clip cracked,
the letters HW scratched by hand into the back of the mirror housing,
the minivan headliner and the open overhead holder softly out of focus above,
no faces, no logos, no readable text other than the scratched HW,

--ar 1:1
```

### 6.5 Driving / in-car(9:16)

```
[MASTER CHARACTER BLOCK]

seated in the driver's seat of a dark blue minivan with a black interior,
parked in a mostly empty parking lot outside an indoor aquatic center before sunrise,
the building's tall windows glowing pale blue (#8FB9C2), engine off,
a smartphone lying screen-up on the wireless charging pad in the lower centre console,
well below the dashboard, the centre touchscreen dimmed,
NOTHING mounted on the dashboard or the air vents, no aftermarket accessories,
he is reading a small tablet held in both hands, a steel travel mug in the cupholder,
navy zip hoodie, faded red cap with no logo,
the passenger seat holds a closed sports bag, the back seats are empty,
shot from the passenger seat, no children anywhere, no visible brand logos,

--ar 9:16
```

### 6.6 Home desk(FROG,4:5)

```
[MASTER CHARACTER BLOCK]

sitting at a plain white sit-stand desk in the corner of a carpeted bonus room
above a garage, facing a wall, a 27-inch monitor and a laptop on a stand,
a small grey docking station with a blank white asset sticker on its back,
ONE single cable running from the dock to the laptop, no other chargers,
no power strip, no desk lamp, a yellow legal pad with unreadable handwriting,
an iPhone lying face down beside the pad,
behind him out of focus: a five-shelf bookcase with an old dented metal coffee can with a faded label on the top shelf,
afternoon light from a window, faded red-clay T-shirt with no print,
no children, no toys in focus, no logos,

--ar 4:5
```

### 6.7 Office hoteling desk(16:9)

```
[MASTER CHARACTER BLOCK]

morning in a bright open-plan corporate office with rows of identical unassigned
desks, each with the same black USB-C dock and the same 27-inch monitor,
most desks completely clear, he is plugging a single cable into a laptop at one
of them, a yellow legal pad and a phone beside it, nothing else on the desk,
a backpack hanging on the chair, charcoal sweater over a blue oxford collar,
no readable signage, no company logo, no ID badge visible,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing
in every panel, head and shoulders, plain warm grey background:
1 calm listening with slightly heavy eyelids, 2 head tilted with chin down listening,
3 closed-mouth half-smile with crinkled eye corners, 4 a real laugh with his head tipped back
and shoulders shaking and deep laugh lines on both cheeks,
5 eyebrows raised and lips pressed flat in a slow nod, 6 proud with lips pressed
tight holding back a smile, 7 sleepy before dawn with eyes half open,
8 one palm rubbing the back of his shaved head while looking down,
9 completely calm eyes looking far ahead as if at the road,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
he moves slowly and deliberately. when he gets into the car he sits, places the
phone on the wireless charging pad in the lower console, waits for the centre
screen to show the map, and only then shifts into gear, every time in that order.
he never picks up the phone while driving. he points with his whole open hand,
palm up, never with one finger. when he is thinking he rubs the back of his shaved
head with one palm. when listening he sits on the front edge of the chair with his
forearms on his knees. his left knee clicks softly on stairs. he does not look at
the camera.

VOICE: warm baritone, around 105 Hz, about 130 words per minute with pauses
between sentences, eastern North Carolina accent softened by twenty years in Raleigh,
natural "y'all" and "fixing to", quotes his father in a flatter, slower voice
("Eyes up."), laughs with a low two-beat "heh, heh". no broadcast energy,
no motivational-speaker tone, no sales tone.

CAMERA: handheld, slight natural drift, 35mm, eye level, available light only,
no children in frame at any time, no phone mount on the dashboard.
```

---

## 七、外型與人設的一致性驗算

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 191 cm、大骨架 | `03` 高中進攻線 | ✓ |
| 左膝舊疤、下樓梯會響、重心在右腳 | `03` 高三的左膝 | ✓ |
| 後腦右下方的胎記 | 天生;**刻意避開酒窩與耳朵(酒窩是本批的生成吸引子,招風耳給 `persona_ca_949`,見 `00 § 十二`)** | ✓ |
| 光頭、均勻灰的鬍子 | 41 歲;**刻意避開單側白髮撞型** | ✓ |
| 不戴眼鏡、手機字體調大 | **刻意避開老花眼鏡撞型** | ✓ |
| 素面金婚戒、Apple Watch、沒有其他珠寶 | `02 § 10` 錢不花在別人看得到的地方 | ✓ |
| 褪色紅帽、紅土色 T 恤、無標誌 | 北卡的土色;不出現大學商標 | ✓ |
| 用整隻手掌指方向 | `03 § 1-1` 父親的駕訓車 | ✓ |
| 上車固定順序、開車不碰手機 | `03 § 5-2`、`6-1` | ✓ |
| 畫面主體是天色、爐子、車、手 | `02 § 11`、孩子不入鏡 | ✓ |
| 車上沒有支架 | `03 § 6-1`;**也是負面提示詞的重點** | ✓ |

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲音、3.8 肢體、6.9 影片提示詞、五個不可變錨。**畫面裡不得有孩子,儀表板上不得有支架。**
**Ivy(Amazon 素材):** 讀 6.1 master block、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**他是「不會買」的人物。他不得出現在任何 SPACION 產品的使用畫面裡,包括「被說服之後」的畫面**(`08 § 9.9`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生成)* | | | |
| full_body_driveway | *(本輪未生成)* | | | |
| hands_mirror_overhead | *(本輪未生成)* | | | |
| in_car_pool_lot | *(本輪未生成)* | | | |
| home_desk_frog | *(本輪未生成)* | | | |
| expression_sheet | *(本輪未生成)* | | | |

> **本輪任務指定不生圖。** 需要出圖時走 `gen-image` skill,把 6.1 的 master block 與完整負面提示詞帶進去,生完把 seed 回填到這張表。
> **第一次出圖要特別檢查兩件事:後座或畫面邊緣有沒有被自動補上孩子;儀表板上有沒有被自動補上支架。** 這是這個人物最容易失敗的兩個地方。

---

## 變更紀錄

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.0 | 2026-10-21 | 建立 | — |
| v1.1 | 2026-10-21 | 第一辨識點:微微外張的耳朵 → 後腦右下方的胎記;負面提示詞改擋招風耳 | Danny(ca_949)的第一辨識點是招風耳,兩人都從酒窩改到耳朵又撞;Danny 的耳朵已出現在 TikTok 模擬,由本人物讓 |

*檔案版本:v1.1 — 2026-10-21 收尾跨人物 QA(變更紀錄見上)*
