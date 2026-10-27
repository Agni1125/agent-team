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
character_slug:   dez-okafor
display_name:     Desmond "Dez" Okafor

art_style:        photorealistic candid smartphone photography
                  # 照片,手機拍的。不是 CG、不是插畫、不是棚拍、不是科技廣告。
style_reference:  East Bay daylight (clear, slightly hazy, warm late afternoon),
                  iPhone-like look, mild noise indoors, no beauty retouching,
                  visible skin texture, real clutter at the edges of frame

color_palette:
  - "#3E4A3A"   # olive canvas: 他的工作外套、湖邊的樹影
  - "#C9A227"   # faded gold: 球帽的帽簷、湖邊燈串的暖光(點綴,不超過畫面 8%)
  - "#1F5C4A"   # faded green: 球帽本體
  - "#E6E3DC"   # pearl white: 那台 Leaf、停車場的水泥
  - "#F2EDE4"   # 1920s plaster cream: 公寓的牆、客廳

lighting_default: 現場光。
                  白天:灣區乾淨的日光,停車場是平光,客廳是凸窗的側光。
                  晚上:客廳一盞暖色桌燈 + 電視的光;車庫是日光燈管。
                  **不用棚燈、不用環形燈、不用美肌補光、不用霓虹、不用 RGB。**

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
plastic skin, airbrushed skin, beauty retouch, glamour lighting,
fashion model, influencer pose, smirk at camera, thumbs up, peace sign,
perfect closed teeth, teeth gap removed, veneers,
full beard, heavy beard, goatee, dreadlocks hanging loose over face,
buzz cut, bald head, dyed hair, blond locs,
studio lighting, ring light, softbox, neon lights, RGB lighting, purple LED glow,
gaming setup, battlestation, LED strip lights, multiple monitors wall,
visible sports team logo, visible brand logo on cap or clothing, visible car brand logo,
readable license plate, readable street sign, broken glass, shattered car window,
luxury car interior, sports car, designer clothing, gold chain, diamond earrings,
anime, illustration, 3d render, cgi, cartoon,
extra fingers, malformed hands, warped text, unreadable text, watermark,
stock-photo smile, hands on hips power pose, crime scene, police tape
```

**為什麼要排除這些(不是隨便列的):**
- `teeth gap removed / veneers / perfect closed teeth`:上排門牙中間的縫是他的第一辨識點之一。生圖最容易把它「修掉」。
- `full beard / goatee`:他只留細細的八字鬍。換成落腮鬍就是換人,也會撞到其他人物的鬍子設定。
- `dreadlocks hanging loose over face / blond locs`:他的 locs 是深棕近黑、及肩、**通常在後頸綁起來**。散在臉前或染色都是漂移。
- `visible sports team logo / visible brand logo on cap`:那頂帽子是 Coliseum 停車場買的仿品,繡的標誌已經洗到看不出來。**任何真實球隊標誌都是法遵問題。**
- `readable license plate / readable street sign`:停車場與路邊的畫面很多,**不能讓真實車牌或街名出現**。
- `broken glass / shattered car window / crime scene / police tape`:車窗被砸是他的過去,**不准拍成畫面**,也不准變成恐懼素材(`08 § 9.6`)。
- `gaming setup / battlestation / LED strip / multiple monitors wall`:他不是 desk setup 帳號,他的桌子在客廳凸窗下,跟 Noor 共用。
- `purple LED glow / RGB`:畫面漂向科技網紅。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | Desmond "Dez" Okafor |
| slug | `dez-okafor` |
| age_appearance | **30–34** |
| gender | 男 / cis |
| ethnicity | 黑人美國人(父親奈及利亞伊博族,母親 Oakland 黑人家庭)。**不偏向任何一種刻板的「科技業黑人」或「運動員」樣子** |
| build_class | 高、瘦、跑者的身形。肩膀不寬,小腿明顯 |
| location_look | 灣區的日常:不曬黑、不蒼白;夏天跑步會在後頸留一點帽子的曬痕 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | 長橢圓,顴骨高,下顎線清楚但不方 | |
| **膚色** | `#6B4A36` 深棕,暖調 | |
| **膚質** | **有毛孔,鼻翼與額頭偶爾出油。** 下巴有一點點刮鬍的痕跡 | 反美肌,32 歲 |
| **眼睛** | 深棕色,杏眼偏長,**眼尾微微往下**,看起來比實際放鬆 | |
| **眼下** | 很淡的陰影,面試週明顯一點 | |
| **眉毛** | 濃、自然,眉峰平 | |
| **鼻子** | 鼻樑中等,鼻翼寬 | |
| **嘴** | 中等偏厚 | |
| **牙齒** | 自然的白,不刻意。**【辨識點】上排兩顆門牙中間有一道約 2 mm 的縫,一笑就看得到** | 從小就有,媽媽說像外公。他從來沒想過要補 |
| **鬍子** | **只留細細的八字鬍,下巴與兩頰刮乾淨。** 每三天刮一次,所以有時候下巴有一點青 | |
| **表情基準** | **放鬆,嘴角習慣性地往一邊歪一點,像在想一個笑話** | 見 3.6 |

### 3.2 頭髮

- 深棕近黑(`#1E1612`),**locs,長度到肩膀**,粗細一致(大約鉛筆粗)。
- **日常:在後頸用一條黑色彈性髮帶綁成一束低馬尾。** 跑步時塞進帽子後面。
- 髮根:兩週整理一次,所以有時候髮根比較蓬。
- **在家放下來的時候很少**,大部分畫面都是綁著的。
- 戴帽子時:帽子正戴,locs 從後面帽扣的洞穿出來。

### 3.3 身體

- **身高 183 cm(6'0")。體重約 72 kg。**
- 跑者的身形:瘦、腿長、小腿明顯,肩膀不寬。
- **姿勢:站的時候重心在一隻腳,另一隻腳的腳尖點地。** 坐著時會把一隻腳踝放在另一邊膝蓋上。
- 手:**手指長,指甲剪得很短很乾淨。** 右手食指側面有一點點因為打字留下的繭(不明顯,不用畫)。
- 左手手腕:Apple Watch,黑色運動錶帶。
- **不戴戒指**(沒訂婚,`02 § 4`)。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **【第一辨識點】上排門牙中間約 2 mm 的縫。** 任何笑開的畫面都必須有。
2. **【第二辨識點】及肩的深色 locs,綁在後頸。**
3. 細細的八字鬍,其他地方刮乾淨。
4. **不可以出現的:** 臉上或手上的任何疤、雀斑、白髮、眼鏡、耳環(這幾樣已經被其他人物用作辨識點,也不屬於他)。

### 3.5 眼鏡

**不戴。** 視力正常。**開車時偶爾戴一副很普通的黑色太陽眼鏡**,只在 92 西向下午的陽光下(停車就拿下來,不入鏡為主)。

### 3.6 表情庫(九宮格)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 放鬆,嘴角往一邊歪一點,眼尾往下 | 60% 的畫面 |
| **thinking** | 眼睛往上看一點,下巴往前,嘴抿著 | 看到一個「特例」的那一秒 |
| **half-smile** | 閉著嘴的笑,一邊嘴角比較高 | 他最常見的笑 |
| **real laugh** | 頭往後仰一點,**露出門牙中間的縫**,眼睛瞇起來 | 跟 Terrell、跟 Noor、跟爸爸 |
| **unimpressed** | 眉毛平,嘴唇抿平,看東西不看人 | 看到「fits most cars」 |
| **satisfied** | 輕輕點頭,嘴角收著 | 一個東西在每個地方都一樣的時候 |
| **tired** | 眼下加深,locs 有幾根掉出來 | 面試週、880 塞了一個半小時 |
| **checking** | **回頭看,肩膀轉一半,臉不轉完** | **走離車的那一秒(主錨點動作的最後一格)** |
| **alert** | 整個人停住,眼睛先動,身體後動 | 停車場地上有碎東西 |

**❌ 絕對不出現的表情:** 對鏡頭比讚、比 YA、嘟嘴、眨眼、網紅式的驚訝摀嘴、「開心的科技新創員工」圖庫笑容、對鏡頭講話的興奮臉。

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | 中低的男聲(baritone),基頻約 **105–120 Hz** |
| 語速 | **偏快,約每分鐘 165 詞。** 講到時間與數字時會慢下來 |
| 口音 | **北加州 / 灣區本地:** 母音偏平,偶爾「hella」,高速公路不加 the(「880」不是「the 880」) |
| 音色 | 乾淨,溫的。**跟爸爸講話時會不自覺帶一點伊博家庭的語調**(只在家人場景) |
| 特徵 | **講「special case」時會停半拍**,像在念一個專有名詞 |
| 笑聲 | 大聲、短,一聲「HA」,然後低頭 |
| 填充詞 | 「like」、「lowkey」(少)、「I mean」 |
| 情緒起伏 | 中。**講 Oakland 的事會快、會熱** |
| 絕不出現 | 播報腔、廣告腔、「Hey guys!」、「what's up y'all」、科技發表會的語氣 |

### 3.8 鏡頭前的肢體習慣

- **走離車子之前回頭看一眼。** 招牌動作,任何停車鏡頭都要有(`04 § 15`)。
- **用手指推一下東西,確認它不會動。** 支架、桌子、杯子。他確認東西「住得穩」的方式。
- **把東西排成一樣的方向**:三個收納袋、兩雙鞋、遙控器。
- 想事情時把帽子往後推一點,再拉回來。
- **講話時兩手會比出「兩邊」**(左手一個地方、右手一個地方),然後把兩手合起來:**「同一個」**。
- **不看鏡頭。** 他看東西、看路、看手上的事。

### 3.9 拍照與自拍行為(決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **一年 3–6 張。** 多半是跟家人或 Terrell 的合照,他在旁邊 |
| 出現在畫面裡的方式 | **手、側面、背影(帽子 + locs)。** 臉不多但不是沒有 |
| 拍什麼 | **湖與城市(35%)、吃的(25%)、車與停車(20%)、家人與朋友(15%)、其他(5%)** |
| 構圖 | 隨手,不擺拍。**停車的畫面一定從副駕的角度** |
| 後製 | 不調色。偶爾裁切 |
| 器材 | iPhone 16 Pro |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「手、車、湖」,不是「臉」,也不是「桌子」。**

---

## 四、服裝系統(三套 + 變體)

外型必須對得起 `02 § 10`:**錢花在「每個地方都一樣」的東西上。** 他的衣服很少,同款很多。沒有任何看得見的 logo。

### 4.1 Office Outfit(進辦公室,週二到週四)

```
- 橄欖綠帆布工作外套(chore jacket),有兩個內袋,左內袋常常鼓一塊(支架)
- 炭黑色長袖 henley(他有三件一樣的,另有三件燕麥色)
- 深藍色直筒牛仔褲
- 灰白色的跑步風格運動鞋(跟跑鞋同一個牌子的日常款,沒有看得見的 logo)
- Apple Watch,黑色運動錶帶
- locs 綁在後頸
```

### 4.2 Home / Weekend(在家工作、週末)

```
- 黑色連帽衫(沒有任何字)或白色 T-shirt
- 灰色運動褲
- 拖鞋(室內)
- 週末出門:同一件工作外套 + 那頂綠黃色球帽
```

### 4.3 Run(湖邊跑步)

```
- 黑色短袖跑步上衣、黑色短褲
- 那雙跑鞋(兩雙一樣的其中一雙)
- 綠黃色球帽,locs 塞在後面
- Apple Watch
```

### 4.4 Driving(車內畫面)

```
- 4.1 或 4.2
- 駕駛座前方儀表罩上緣偏右的彈簧夾式支架,球頭加圓形 MagSafe 頭,手機在上面
- 下午西向時偶爾戴太陽眼鏡
- 中央扶手箱:開車時關著,停在外面時打開(空的);**支架停車時在外套左內袋**
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | Apple Watch,黑色運動錶帶 |
| 帽子 | **洗到看不出標誌的綠黃色球帽**(2012 年 US$10) |
| 包 | 一個黑色的通勤後背包,側袋固定放灰色收納袋 |
| 髮帶 | 黑色彈性髮帶(綁 locs) |
| 太陽眼鏡 | 很普通的黑色款,只在開車時 |
| **不戴的** | 戒指、項鍊、耳環、手鍊、名牌、任何有大 logo 的東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

### 五個不可變的錨(Immutable Anchors)

1. **上排門牙中間的縫**,笑開時必須有,不准修掉
2. **及肩的深色 locs,綁在後頸**,不准散在臉前、不准染色、不准剪短
3. **只有細細的八字鬍**,不准落腮鬍、不准山羊鬍
4. **皮膚有毛孔、不磨皮**
5. **停車畫面裡,支架一定是被拔下來、塞進外套左內袋的那一刻**,而且沒有任何真實的車牌或街名

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 科技網紅 / 新創 CEO 樣 | 他是一個在客廳凸窗下寫程式的人 |
| 2 | 門牙的縫被修掉 | 第一辨識點 |
| 3 | 落腮鬍、山羊鬍、光頭、短髮 | 換人 |
| 4 | desk setup、RGB、多螢幕牆 | 他的桌子是共用的 |
| 5 | 豪車、跑車、看得見的車廠標誌 | 他開的是 2017 年的珍珠白二手 Leaf |
| 6 | 任何真實球隊或品牌的標誌 | 法遵 |
| 7 | 碎玻璃、被砸的車窗、警察、犯罪畫面 | **不准把他的經驗拍成恐懼素材** |
| 8 | 對鏡頭笑、比讚、power pose | 圖庫感 |
| 9 | 金鍊、鑽石耳環、名牌 | 違反 `02 § 10` 的消費邏輯,也是刻板印象 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段 |

### 連續性檢查表(每次出圖後跑)

- [ ] 笑開的圖,門牙中間的縫在嗎?
- [ ] locs 是深色、及肩、綁在後頸嗎?
- [ ] 鬍子只有八字鬍嗎?
- [ ] 皮膚有沒有被磨皮?
- [ ] 帽子上有沒有任何看得出來的標誌?(不可以)
- [ ] 有沒有出現真實的車牌、街名、車廠標誌?(不可以)
- [ ] 停車畫面:支架是在外套口袋、扶手箱是打開而且空的嗎?(公寓車庫的畫面例外:支架在儀表罩上)
- [ ] 有沒有碎玻璃、警察、犯罪的暗示?(不可以)
- [ ] 臉、手、眉毛有沒有被畫出疤?有沒有被加上眼鏡?(不可以)
- [ ] 手有沒有畫壞?

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic candid smartphone photograph, available light only,
no retouching, visible skin texture and pores, mild noise indoors,

a 32-year-old Black American man, 183cm, lean runner's build with narrow
shoulders and long legs, long oval face with high cheekbones and a clean
jawline, warm deep brown skin (#6B4A36),
dark brown almond eyes with slightly downturned outer corners,
thick natural eyebrows, medium-wide nose, medium-full lips,
a thin mustache and an otherwise clean-shaven face with faint stubble shadow,
a natural gap of about 2mm between his upper front teeth, visible when he smiles,
shoulder-length very dark brown locs (#1E1612) of even pencil thickness,
tied back at the nape with a black elastic band,
no glasses, no earrings, no rings, no visible scars,
a black Apple-style smartwatch on his left wrist,

relaxed expression with one corner of the mouth slightly raised, as if
thinking of a joke, looking at what he is doing rather than at the camera,

colour palette: olive canvas #3E4A3A, faded green #1F5C4A, faded gold #C9A227
under 8% of frame, pearl white #E6E3DC, plaster cream #F2EDE4
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, in front of a 1920s cream plaster
wall beside a bay window, olive canvas chore jacket over a dark grey crew-neck
t-shirt, soft side light from the bay window on the left,
a closed-mouth half-smile, shallow depth of field f/2.8,

--ar 4:5
```

### 6.3 Parking ritual(主錨點鏡頭:支架進口袋,9:16)

```
[MASTER CHARACTER BLOCK]

shot from the passenger seat of a pearl white 2017-era compact electric
hatchback with a black interior, a deep dashboard and a steeply raked
windshield, a two-tier instrument display and a small centre screen,
no visible brand logo anywhere,
parked in an open office parking lot in flat midday California light,
his hand unclipping a small black spring-clamp phone mount with a ball
joint and a round magnetic head from the top edge of the instrument hood
and sliding it, clamp facing in, into the left inside pocket of his olive
canvas chore jacket, two tiny shiny pressure marks left on the hood edge,
the centre armrest lid open and the bin empty, the back seat empty,
a small electronic toll tag at the top centre of the windshield,
no license plates, no street signs, no other people,

--ar 9:16
```

### 6.4 Walking away(回頭看,9:16)

```
[MASTER CHARACTER BLOCK]

full body from behind and slightly to the side, walking away from a pearl
white compact electric hatchback in an open parking lot, turning his shoulders half
back to glance at the car without fully turning his face,
olive canvas chore jacket with a visible bulge in the left inside pocket,
dark jeans, grey-white running-style sneakers, black backpack,
the rear hatch window shows an empty cargo area with the cover rolled away,
flat late-morning light, long shadow, no license plates readable,

--ar 9:16
```

### 6.5 Shared desk(客廳凸窗下的共用桌,16:9)

```
[MASTER CHARACTER BLOCK]

a small 1920s Oakland apartment living room, a light-oak laminate desk
under a bay window with trees outside, a 14-inch laptop and a 15.6-inch
portable monitor on a folding stand, he is on a video call wearing a black
hoodie, beside the laptop a basket and a stack of someone else's paper forms
with a highlighter (his partner's evening work, she is not in frame),
a white four-port wall charger plugged into a power strip on the floor,
one USB-A port on it visibly empty, the portable monitor screen momentarily
black while the laptop screen is on, his eyes on the black monitor,
warm desk lamp, late afternoon side light, no RGB, no LED strips,

--ar 16:9
```

### 6.6 Garage(公寓車庫,例外的那一刻,9:16)

```
[MASTER CHARACTER BLOCK]

inside a small underground gated apartment garage with fluorescent tube
lighting and painted concrete columns, seen through the driver's window,
he sits in the driver's seat with the engine off, hands resting on the
wheel, eyes on the rear-view mirror where a roll-up metal gate is closing
behind the car, the phone still on the clamp mount on the instrument hood,
the armrest closed, the jacket on the passenger seat lying flat, a single
numbered parking space marker on the column
(number 6), no other cars' plates visible,

--ar 9:16
```

### 6.7 Lake run(湖邊,4:5)

```
[MASTER CHARACTER BLOCK]

early morning on a lakeside path in Oakland, a string of small round lights
along the lake edge still on in the blue hour, he is running away from the
camera wearing a faded green and gold baseball cap with no visible logo
(the embroidery washed out), locs tucked through the back, black running
shirt and shorts, an old man on a bench in soft focus reading a newspaper,

--ar 4:5
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing
in every panel, head and shoulders, plain warm grey background, locs tied back
in every panel:
1 relaxed with one mouth corner raised, 2 thinking with eyes up and lips
pressed, 3 closed-mouth half-smile, 4 a real laugh with head tipped back
showing the gap between his upper front teeth, 5 unimpressed with flat
eyebrows, 6 satisfied with a small nod, 7 tired with deeper under-eye
shadows and a few locs loose, 8 checking over his shoulder with the face only
half turned, 9 alert and completely still with only the eyes moving,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
before walking away from his parked car he always glances back once,
shoulders half turned, face not fully turned. he tests whether an object is
stable by pushing it once with one finger. he lines objects up facing the
same direction. when explaining, his hands mark two different places, then
come together to mean "the same one". he does not look at the camera; he
looks at the car, the road, or the thing in his hands.

VOICE: baritone male voice, around 110 Hz, about 165 words per minute,
Northern California / Bay Area accent, says "880" without "the", occasional
"hella", slows down on times and numbers, a short loud "HA" laugh, no
broadcast or sales tone.

CAMERA: handheld, slight natural drift, 26mm phone lens, available light,
parking scenes always shot from the passenger seat.
```

---

## 七、外型與人設的一致性驗算

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 跑者身形 | `02 § 8`、`06 § 五` 一週跑湖三次 | ✓ |
| 門牙的縫 | `07 § 3.1` 從小就有,不補(`02 § 10`:不在看得到的地方花錢) | ✓ |
| locs 綁起來 | 工作與跑步都方便;家族照片裡的一致樣子 | ✓ |
| 不戴戒指 | `02 § 4` 沒訂婚 | ✓ |
| 三件一樣的 henley、兩雙一樣的鞋 | `02 § 10` 一致性的消費邏輯 | ✓ |
| 沒有珠寶 | `02 § 10-2` 不在看得到的地方花錢;**也避開刻板印象** | ✓ |
| 外套內袋鼓一塊 | `04 § 15` 支架整天在身上 | ✓ |
| 綠黃色無標誌帽子 | `03 § 3-1` Coliseum、A's 離開 | ✓ |
| 停車回頭看 | `03 § 6-1` 2022 年之後的習慣 | ✓ |
| 沒有疤、沒有眼鏡、沒有白髮 | 刻意:避開與其他人物撞型(`00 § 四` 第 13 項) | ✓ |

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲音、3.8 肢體、6.3 停車鏡頭、6.9 影片提示詞、五個不可變錨。**停車畫面一律從副駕拍,不准出現真實車牌與街名。**
**Ivy(Amazon 素材):** 讀 6.1 master block、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**他是 iOS 工程師這件事,不可以出現在任何 MagSafe、充電、手機發熱相關的商業素材上**(專家薦證風險,見 `08 § 9.6`)。
**車窗被砸的經驗,不可以出現在任何支架的商業素材上**(恐懼訴求,見 `08 § 9.6`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生成)* | | | |
| parking_ritual | *(本輪未生成)* | | | |
| walking_away | *(本輪未生成)* | | | |
| shared_desk | *(本輪未生成)* | | | |
| garage | *(本輪未生成)* | | | |
| expression_sheet | *(本輪未生成)* | | | |

> **本輪任務指定不生圖。** 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。
> **第一次出圖要特別檢查門牙的縫有沒有被修掉、帽子有沒有被畫上標誌**,這是這個人物最容易失敗的兩個地方。

---

*檔案版本:v1.0 — 2026-10-21 建立*
