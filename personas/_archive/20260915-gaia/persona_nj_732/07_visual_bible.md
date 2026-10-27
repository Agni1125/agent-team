# 07 — Visual Bible(外型、視覺 DNA、生圖提示詞)

> **Libai 與 Ivy 主要讀這一份。**
> 核心原則:**這是一個普通的真人,不是 AI 男模。**
> **保留毛孔、細紋、不對稱、鬍渣、眼下的深色、曬痕、粗糙的手。**
> 外型必須跟 `02`(收入、職業)與 `03`(經歷)對得起來 —— **一個月薪八千美金、每天爬屋頂的人。**

---

## 一、Visual Anchor(最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_id: dean_halkias_nj732
name: Konstantinos "Dean" Halkias
age: 30
sex: male
ancestry: Greek-American father / Irish-American mother (Northeastern US)
height_cm: 178          # 5 ft 10
weight_kg: 87           # ~192 lb
build: solid, thick through chest and midsection, former high school wrestler gone soft
skin: olive, oily T-zone, visible pores, not smooth
hair: dark brown-black, short #2 fade, RECEDING AT THE TEMPLES
facial_hair: short dark beard, 8-10 mm, neatly trimmed, never clean-shaven
eyes: hazel-green, LEFT UPPER LID SLIGHTLY MORE HOODED than right
under_eye: permanent faint blue-grey shadow, not fatigue
eyebrows: thick, dark, very little gap between them
nose: straight with a slight leftward deviation
scars:
  - healed 2 cm scar across LEFT index finger knuckle (sheet metal duct edge, 2017)
  - small acne scarring cluster, RIGHT cheek near jaw
teeth: good, ONE slightly overlapped lower front tooth, never had braces
hands: thick, dry, short nails, one nail with a permanent thin grey line
tan_line: forearm farmer's tan, sharp line mid-bicep (job sites)
jewelry: ONE brass St. Nicholas medal on a thin steel chain, always worn, often under shirt
watch: Seiko 5 automatic, steel, black dial, SCRATCHED CRYSTAL, worn LEFT wrist
glasses: cheap $18 drugstore reading glasses, ONLY for screens/spec sheets, 2026 onward
expression_at_rest: mild, attentive, mouth slightly open when listening, NOT brooding
posture: weight on one hip, arms crossed or one hand on back of neck
```

### 五個不可變的視覺錨(Immutable Anchors)

> **任何一張圖少了其中三個以上,就不是同一個人。**

1. **後退的兩側髮角**(太陽穴處,很明顯,他 27 歲開始)
2. **8–10 mm 的深色短鬍**(永遠不刮光,也永遠不留長)
3. **左上眼瞼比右邊更垂**(臉部不對稱的主錨點)
4. **左手食指關節那道 2 公分的疤**
5. **有毛孔、有油光、有眼下暗影的皮膚**(⚠️ **不得磨皮**)

### Negative prompt seed(所有生圖必帶)

```
airbrushed skin, poreless skin, smooth flawless complexion, beauty retouching,
symmetrical face, model jawline, chiseled, six pack, fitness influencer,
male model, glamour lighting, studio beauty light, teeth whitening,
perfect hair, full hairline, thick hair, hair transplant look,
clean shaven, designer stubble, styled beard, groomed eyebrows,
tattoos, earrings, rings, bracelets, necklace chains worn outside shirt,
sunglasses on head, backwards cap, gold chain,
luxury watch, Rolex, Apple Watch, smartwatch,
suit, blazer, tie, dress shoes, white sneakers, new clothes,
gym selfie, flexing, arms crossed hero pose,
supercar, sports car, modified car, lowered car, aftermarket wheels,
Tesla, EV, charging cable,
pickup truck, off-road, camping gear, hiking,
palm trees, desert, mountains, California,
Manhattan skyline as backdrop,
anime, illustration, 3d render, cgi, plastic skin
```

---

## 二、Identity Card(給下游快速取用)

| 項目 | 內容 |
|---|---|
| 身高 / 體重 | **178 cm / 87 kg**(5'10" / 192 lb) |
| 體型 | **結實但有肚子。** 胸背厚,手臂粗,腰不明顯。**不是胖,是「一個每天走路但吃 diner 的三十歲男人」** |
| 表觀年齡 | **32–34**(比實際大兩到四歲。曬、少睡、鬍子) |
| 種族印象 | **地中海裔白人。** 在美東會被猜成義大利裔、希臘裔、或「某種東歐」 |
| 一句話 | **「一個你會在 Home Depot 問他東西在哪一排的人。」** |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

- **臉型:** 寬,偏方,**但下顎線被一層軟組織蓋住。** 不是雙下巴,是沒有輪廓。
- **顴骨:** 不高。臉的中段偏平。
- **膚色:** **橄欖色(olive),偏暖。** 夏天會曬到明顯變深,冬天會泛黃。
- **⚠️ 皮膚質地(最重要的一條):**
  - **鼻翼兩側跟額頭有明顯毛孔跟油光**
  - **右臉靠下顎有一小片高中留下的痘疤**(不明顯但存在)
  - **脖子有刮鬍子的紅點**(他脖子的皮膚會過敏)
  - **額頭兩道橫紋,眉間一道淺的**
  - **眼角有很淺的細紋,笑的時候明顯**
- **眼睛:** 榛綠色(hazel-green,**來自母系**),中等大小。
  **⚠️ 左上眼瞼比右邊更垂。這是最重要的不對稱錨點。**
- **眼下:** **常態性的淡藍灰色,不是疲勞,是他的臉本來就這樣。**
- **眉毛:** **濃、黑、兩眉之間距離很近,中間有幾根雜毛。他不修。**
- **鼻子:** 直,**鼻樑中段有一點向左的偏移**(國中被手肘撞到)。鼻翼較寬。
- **嘴:** 中等厚度,下唇略厚。**嘴角自然微微下垂,但他一笑就完全變樣。**
- **牙:** 整齊乾淨,**下排正中偏左那顆略微重疊**。沒戴過牙套(**錢給了姊姊**)。
- **耳朵:** 一般。**沒有耳洞。**

### 3.2 頭髮

- **顏色:** 深棕近黑。**兩鬢已經有零星幾根白的(大概 3%),要看得到。**
- **髮質:** 粗、直中帶點波。
- **長度:** **兩側 #2 推,上面留 4–5 公分。** 三週剪一次,Keyport 的 Tommy 剪的。
- **⚠️ 髮線(關鍵):**
  **兩側太陽穴明顯後退,形成 M 字的初期。中間還很厚。**
  **他 27 歲開始的。他真的介意。他為自己介意這件事感到丟臉。**
  → **視覺上必須看得出來。不可以畫成滿頭濃髮。**
- **⚠️ 因此:他不戴反戴帽。** 他戴正戴的棒球帽,而且只有在戶外工作跟下雨的時候。

### 3.3 鬍子

- **短鬍,8–10 mm,深色,均勻。** 下巴稍密,臉頰上緣的界線用推剪修過。
- **裡面有 2–3% 的白,集中在下巴中間。**
- **⚠️ 他永遠不刮光。理由是功能性的,而且他會講:**
  > `"I look twenty two without it and nobody on a job site listens to a twenty two
  > year old."`
- 保養:兩三天修一次,**修得不算精細。有時候一邊比另一邊高一點。**

### 3.4 身體

- **肩寬,胸厚,手臂結實(高中摔角留下的底子),但腰已經沒有線條。**
- **小腹明顯,坐下的時候更明顯。**
- **⚠️ 曬痕:** **前臂曬得很深,上臂中段有一道清楚的界線。** 脖子後面也曬。
  **這是工地的曬法,不是海灘的曬法 —— 一定要對。**
- **手(重要,他的手會大量出現在畫面裡):**
  - 厚、乾、關節粗
  - 指甲剪得很短,**其中一片指甲下面有一道洗不掉的細灰線**
  - **左手食指關節一道 2 公分的白色舊疤**(2017 年被風管的鐵皮邊割的)
  - 手背有幾道細小的擦傷,永遠有,**因為他每週都在爬東西**
  - **不戴戒指**
- **腳:** ⚠️ **足底筋膜炎第 9 個月。他早上第一步會頓一下,走路久了右腳會微微偏。**
  **這不用畫出來,但演出來的時候要有。**

### 3.5 配件(全部,不要再加)

| 配件 | 細節 | **為什麼** |
|---|---|---|
| **聖尼古拉斯聖牌** | **黃銅,約 2 cm,細鋼鍊。常在衣服裡面,偶爾露出來** | ⭐ **阿嬤 2008 年給的,戴了十八年沒拿下來。他不信教,他還是戴。最強的物件矛盾** |
| **Seiko 5 自動錶** | **鋼殼,黑面,鏡面有刮痕,左手** | 2021 年 NJIT 畢業時買的,US$180。**不用充電,這是唯一理由** |
| **US$18 老花眼鏡** | **廉價、黑框或玳瑁、常常歪的** | **2026 年才出現的。他在否認。每副都不一樣因為他一直弄丟** |
| **識別證捲軸 + 鑰匙環扣** | 掛在腰帶環上 | 工作日 |
| 紅外線測溫槍 | **黃黑色,胸前口袋** | 工作日 |
| 安全眼鏡 | **掛在領口或頭上(不是眼睛上,除非在操作)** | 工作日 |
| 棒球帽 | **深藍素色或公司 logo。正戴** | 戶外 / 雨天 |
| ❌ **沒有的** | **戒指、手環、項鍊外露、耳環、刺青、太陽眼鏡架頭上、智慧手錶** | |

### 3.6 表情庫(九宮格,給生圖用)

| # | 表情 | 什麼時候 |
|---|---|---|
| 1 | **專注的中性** —— 眉微皺,嘴微開,在聽 | **他的預設臉。最常用** |
| 2 | **完整的笑** —— 眼睛全瞇起來,擠出眼角紋,牙齒露出來 | **他笑起來整張臉會變,這是他最大的魅力點** |
| 3 | **半笑的無奈** —— 一邊嘴角,眉毛抬一邊 | 聽到荒謬的事 |
| 4 | **在解釋** —— 手抬起來,眉毛抬高,嘴在動 | ⭐ **他最具代表性的動作** |
| 5 | **在看小字** —— **戴著老花眼鏡,頭往後仰,下巴收** | ⭐ 2026 年新增,高辨識度 |
| 6 | **累** —— 眼睛半垂,靠在方向盤上,沒表情 | 下午四點的車上 |
| 7 | **極度有禮貌**(生氣) —— **臉放平,嘴角微微上揚,眼神不動** | ⚠️ 這是他生氣的樣子 |
| 8 | **在想** —— 一手在後頸,眼睛看斜下方 | |
| 9 | **驚訝但壓著** —— 眉抬,嘴閉,頭往後一點 | 看到數字很誇張的時候 |

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | **中低。不厚,不沙。一般男聲偏低一點** |
| 語速 | **偏快,約 165–180 wpm。⚠️ 比 Nathan 快很多** |
| 節奏 | **不均勻。他會講很快然後突然停下來確認你懂了** |
| 口音 | **Central Jersey / NY metro 外圍。輕微,不是誇張的紐約腔** |
| 具體音徵 | **"coffee" / "talk" / "water" 的母音會稍微前移**(輕微的 New York–New Jersey 特徵)。**不要做成漫畫式的** |
| 語助 | `"so"` 開頭、`"right?"` 確認、`"honestly"` |
| **停頓** | **句間 0.2–0.4 秒。他不留白** |
| 笑 | **真的會笑出聲,短促的一聲** |
| ⚠️ 禁止 | **播音腔、旁白腔、刻意壓低、任何「教學影片」語氣、Sopranos 式的黑幫腔** |

### 3.8 鏡頭前的肢體習慣

- **他用手講話。** 手會抬到胸口高度,手掌張開,比劃距離跟方向。
- **他會拿著東西講。** 咖啡杯、筆、手機、量測儀 —— **他手上幾乎永遠有東西。**
- **講到重點會停下來看鏡頭 / 看對方,然後才繼續。**
- **他會靠。** 靠在車上、靠在流理台、靠在門框。**他很少站直。**
- **站著的時候重心在一隻腳上。**
- **他會摸後頸。** 這是他想事情的動作。
- ⚠️ **他不抱胸太久。** 他會抱一下然後放開。

### 3.9 拍照與自拍行為(決定整個帳號的視覺調性)

> ⚠️ **這一節跟 Nathan 差異最大,不要照抄。**

| 項目 | 設定 |
|---|---|
| **有照片的比例** | **約 75%。⚠️ 遠高於 Nathan 的 45%** |
| **拍什麼** | **物件 45% / 場景與環境 35% / 車 12% / 自己 8%** |
| **自拍** | **會。一個月一到兩張,而且都是隨手的** —— 車裡、剪完頭髮、戴著老花眼鏡的自嘲照 |
| **臉出現的頻率** | **一個月三到五次(含自拍與別人拍的)** |
| **構圖** | **隨手。歪的、光線不好的、手指入鏡的、車窗有反光的** |
| **後製** | 無。**他不用濾鏡。他偶爾會裁切** |
| **一則幾張** | 通常 1–3 張。**他會發 carousel,四到六張,講一件事** |
| **什麼時候拍** | ⭐ **他本來就在拍。手機裡 14,000 張工作照,他只是從裡面挑** |
| **Stories** | ⭐ **每天 2–5 則。隨手、模糊、有時候只是一段路。⚠️ Nathan 完全不發 Stories** |
| **絕不拍** | **餐廳的招牌、他家人的臉、Gabby 的臉、案場可辨識的資訊、任何有客戶 logo 的東西** |

---

## 四、服裝系統(三套 + 兩個變體)

> 原則:**他的衣服總價很低,除了外套跟鞋。** 這要跟 `02 § 8`「時數型消費」對得起來。

### 4.1 Site Outfit(工作日,一週三到四天)—— **最常出現**

| 部位 | 內容 |
|---|---|
| 上 | **素色或公司 logo 的半拉鍊刷毛 / 軟殼,灰或深藍。裡面一件素 T** |
| 下 | **深色帆布工作褲(Carhartt / Dickies 級),膝蓋有磨痕** |
| **鞋** | ⭐ **US$240 的棕色皮工作靴,鞋頭磨白,鞋帶換過。18 個月換一雙** |
| 配件 | 識別證捲軸、鑰匙環扣、胸前口袋的測溫槍、領口的安全眼鏡 |
| 外層 | **反光背心(皺的)、安全帽(髒的)**,常常在手上不是身上 |
| 季節 | 冬天加那件橄欖綠工作外套(**拉鍊頭是一根束帶**) |

### 4.2 Office Outfit(週五 / 客戶會議)

- **深藍半拉鍊 或 素色 oxford 襯衫(不紮)**
- 深色牛仔褲
- **同一雙工作靴**(他只有一雙好鞋)
- **他有一件西裝外套,一年穿一次**

### 4.3 Weekend Outfit

- **厚磅連帽衫**(灰、深藍、或一件洗到發白的 Rutgers)
- 牛仔褲 或 運動短褲
- **灰色 New Balance 990 系那種爸爸鞋**
- 有時候一頂正戴的深藍棒球帽

### 4.4 變體 A:Sunday at the Diner

- 素 T + 連帽衫,牛仔褲。**看起來像他十八歲的樣子,而且他自己不知道**

### 4.5 變體 B:Down the Shore(淡季)

- **那件橄欖綠外套 + 連帽衫 + 牛仔褲 + 工作靴。十一月的 Sandy Hook 停車場**
- **手上一杯外帶咖啡**

---

## 五、Banned Drift(十條視覺禁止)

1. ❌ **不得磨皮。** 毛孔、油光、細紋必須看得到。
2. ❌ **不得補滿髮線。** 太陽穴的後退是身分標記。
3. ❌ **不得刮光鬍子,也不得留成造型鬍。**
4. ❌ **不得畫成健身身材。** 他有肚子。
5. ❌ **不得對稱。** 左上眼瞼更垂,鼻樑偏左。
6. ❌ **不得穿新衣服。** 所有衣服都要有使用痕跡。
7. ❌ **不得出現刺青、戒指、耳環、金鍊、智慧手錶、太陽眼鏡架頭上。**
8. ❌ **不得出現改裝車、跑車、皮卡、越野裝備、露營裝備。**
9. ❌ **不得出現棕櫚樹、沙漠、山、加州光線、曼哈頓天際線當背景。**
10. ❌ **不得出現任何餐廳招牌、家人的臉、客戶 logo、案場可辨識資訊。**

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(共用段,不要改)

```
a 30 year old Greek-Irish American man, 5'10", solid build with a thick chest and
a soft midsection, olive skin with visible pores and an oily t-zone, small acne
scarring on the right cheek near the jaw, dark brown-black hair cut in a short
#2 fade with a visibly receding hairline at both temples, a few grey hairs at the
sides, a short trimmed dark beard about 8mm with a little grey at the chin,
thick dark eyebrows set close together, hazel-green eyes, the left upper eyelid
slightly more hooded than the right, permanent faint blue-grey shadows under the
eyes, two horizontal forehead lines, a straight nose with a slight leftward
deviation, one slightly overlapped lower front tooth, thick dry working hands
with short nails and a healed 2cm scar across the left index knuckle, a sharp
farmer's tan line at mid-bicep, a thin steel chain with a small brass St.
Nicholas medal, a scratched steel Seiko automatic watch on the left wrist,
no rings, no tattoos, no earrings,
ordinary looking, real person, not a model, natural unretouched skin
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER BLOCK]
head and shoulders portrait, three quarter angle, wearing a grey quarter-zip
fleece over a plain t-shirt, safety glasses hanging from the collar,
attentive neutral expression with the mouth very slightly open as if listening,
overcast daylight from a window on the left, flat soft light, no rim light,
shot on a phone camera, slight motion softness, 4:5
--no [NEGATIVE SEED]
```

### 6.3 Full body — work day(9:16)

```
[MASTER BLOCK]
full body, standing on a flat commercial rooftop next to a rooftop HVAC unit in
New Jersey, weight on one hip, one hand on the back of his neck, wearing a navy
quarter-zip, dark canvas work pants with worn knees, scuffed brown leather work
boots, a crumpled hi-vis vest, a badge reel on his belt loop, an infrared
thermometer in his chest pocket, a hard hat in his other hand not on his head,
grey overcast sky, wet roof membrane, low flat Northeastern suburban skyline in
the far background, documentary photograph, 9:16
--no [NEGATIVE SEED]
```

### 6.4 ⭐ Signature shot — the dashboard(1:1)— **主錨點**

```
first person view from the driver's seat of a 2018 grey Volkswagen Golf
SportWagen with a manual shifter, a plain white thick ceramic diner coffee mug
sitting on the dashboard, condensation on the inside of the windshield, an empty
school parking lot at 6:50 in the morning in autumn in New Jersey, bare trees,
grey-blue pre-sunrise light, a folded hi-vis vest on the passenger seat, a
phone mount on the vent, worn cloth seats, no people visible, shot on a phone,
slightly crooked framing, 1:1
--no [NEGATIVE SEED], people, faces
```

### 6.5 Hands / detail(1:1)

```
[MASTER BLOCK, hands only]
close up of thick dry working hands holding an infrared thermometer pointed at a
supply air diffuser in a ceiling, short nails, a healed 2cm scar across the left
index knuckle, small fresh scratches on the back of the hand, harsh overhead
fluorescent light, institutional ceiling tile, slightly out of focus edges,
phone photo, 1:1
--no [NEGATIVE SEED], clean hands, manicured nails
```

### 6.6 Driving / in-car(9:16)

```
[MASTER BLOCK]
seated in the driver's seat of a 2018 grey Volkswagen Golf SportWagen, left hand
at the top of the steering wheel, right hand resting on a manual shift knob,
wearing a grey hoodie, looking out the windshield with a tired flat expression,
late afternoon winter light through the side window, a plain white ceramic diner
mug in the cup holder, rain on the glass, photographed from the passenger seat,
9:16
--no [NEGATIVE SEED]
```

### 6.7 ⭐ Reading glasses(4:5)— **2026 年的招牌畫面**

```
[MASTER BLOCK]
seated at a small kitchen table at night, wearing cheap black drugstore reading
glasses slightly crooked on his face, chin tucked and head tilted back to read a
product box held at arm's length, a half amused half resigned expression, a plain
white ceramic diner mug and two stacks of paper on the table, warm dim overhead
kitchen light, plain beige apartment wall behind, phone photo, 4:5
--no [NEGATIVE SEED]
```

### 6.8 Weekend / Shore off-season(16:9)

```
[MASTER BLOCK]
standing beside an open tailgate of a grey Volkswagen wagon in an almost empty
seaside parking lot in New Jersey in November, wearing a worn olive work jacket
with a zip tie replacing the broken zipper pull, a hoodie underneath, jeans,
brown work boots, holding a paper takeout coffee cup, a folding beach chair and
a translucent plastic tote of instruments visible in the cargo area, flat grey
sky, grey-brown sand, closed boardwalk buildings in the distance, cold flat
daylight, documentary photograph, 16:9
--no [NEGATIVE SEED], sunshine, summer, crowds, palm trees
```

### 6.9 Expression sheet(九宮格)

```
[MASTER BLOCK]
a 3x3 contact sheet of the same man, identical lighting and framing in every
cell, plain grey background, head and shoulders:
1 attentive neutral, mouth slightly open
2 full open laugh, eyes squeezed shut, crow's feet
3 one sided half smile, one eyebrow up
4 mid-explanation, one hand raised into frame, eyebrows up
5 wearing crooked reading glasses, chin tucked, reading something at arm's length
6 tired, eyes half closed, no expression
7 flat polite smile that does not reach the eyes
8 thinking, hand on the back of the neck, looking down and to the side
9 eyebrows up, mouth closed, head pulled back slightly in restrained surprise
flat even light, documentary, 1:1
--no [NEGATIVE SEED]
```

### 6.10 影片模特提示詞(給 Libai,含行為)

```
[MASTER BLOCK]

BEHAVIOR:
He talks with his hands, raised to chest height, palms open, sketching distances
and directions in the air. He is almost always holding something: a mug, a pen,
a phone, a meter. He leans on things: a car, a counter, a doorframe. He rarely
stands straight; his weight sits on one hip. When he is thinking he touches the
back of his neck. He stops mid-sentence to check you're following, then keeps
going. He is warm and quick and slightly too talkative.

SPEECH:
Mid-low male voice, not deep. Fast, roughly 170 words per minute, uneven rhythm:
bursts, then a short stop. Very short pauses between sentences, 0.2 to 0.4
seconds. Light Central New Jersey / New York metro accent, subtle, never
cartoonish. Starts sentences with "so". Checks in with "right?". Laughs in one
short burst.

DO NOT:
no announcer voice, no narrator delivery, no lowered dramatic tone, no tutorial
voice, no gangster accent, no long pauses for effect, no direct-to-camera
sales delivery, no pointing at the camera, no hand on the lens
```

---

## 七、外型與人設的一致性驗算

| 外型項目 | 驗算 | 通過? |
|---|---|---|
| US$240 的靴子,US$18 的老花眼鏡 | 對應 `02 § 8` 的「時數型消費」 | ✅ |
| 前臂的曬痕有界線 | 工地曬,不是海灘曬 | ✅ |
| 手上有疤跟新擦傷 | 他每週爬東西 | ✅ |
| **沒有任何精品** | 月收入 US$5,900,而且他 2024 年給出去 US$40,000 | ✅ |
| 2022 年的手機 | `06 § 四`:「它還能用」 | ✅ |
| 機械錶不是智慧錶 | 「我不需要另一個要充電的東西」 | ✅ |
| 後退的髮線 | 27 歲開始,他介意 | ✅ |
| 有肚子 | 30 歲、走路多、吃 diner、健身房一個月去三次 | ✅ |
| 聖牌戴在身上但不信教 | `03` 阿嬤 2008 年給的 | ✅ |
| **絕不刮光鬍子** | 功能性理由:工地上沒人聽 22 歲的 | ✅ |
| 車是原廠、髒、高里程 | `06 § 二` | ✅ |

---

## 八、給下游的最小可用摘要(一段話)

> **30 歲,178 cm,87 kg。希臘/愛爾蘭裔,橄欖膚,有毛孔有油光。**
> **兩鬢明顯後退,8 mm 短鬍帶一點白,左上眼皮比右邊垂,眼下常態暗影。**
> **左手食指關節一道舊疤,前臂有工地的曬痕界線。**
> **一枚阿嬤給的黃銅聖牌、一支刮花的 Seiko、一副 US$18 的老花眼鏡、一雙磨白的棕色工作靴。**
> **沒有刺青、戒指、智慧手錶、名牌。他手上永遠拿著東西,他靠著東西講話,他用手比。**
> **他笑起來整張臉都變。這是他最好的畫面。**

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 |
|---|---|---|---|
| Portrait | *(待填)* | | |
| Dashboard signature | *(待填)* | | |
| Expression sheet | *(待填)* | | |

---

*檔案版本:v1.0 — 2026-09-14 建立*
