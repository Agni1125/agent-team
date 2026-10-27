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
character_slug:   danny-truong
display_name:     Daniel "Danny" Duy Truong

art_style:        photorealistic smartphone documentary photography
                  # 照片。不是 CG、不是插畫、不是 3D、不是汽車廣告、不是醫療廣告。
style_reference:  bright Southern California daylight filtered through a parking
                  structure, iPhone front or back camera look, slight wide-angle
                  distortion in car interiors, no beauty retouching, visible skin texture

color_palette:
  - "#3A3F44"   # parking-structure concrete — 停車結構、柏油、車內陰影
  - "#BFC3C7"   # silver car paint — 他的車、正午的反光
  - "#D9C6A8"   # Irvine stucco beige — 公寓外牆、乾燥的地面
  - "#6B4426"   # cà phê sữa đá brown — 杯架裡的冰咖啡、公事包的皮革拉帶
  - "#C8102E"   # expired-badge red — 識別證的紅色斜紋。唯一的高彩度色,點綴用,不超過畫面 5%

lighting_default: 現場光。
                  白天:停車結構的斜射陽光(一邊亮、一邊是混凝土陰影)、車內的頂光。
                  晚上:公寓書房的白色 LED 檯燈、手機手電筒、車棚的鈉燈或 LED 路燈。
                  **不用棚燈、不用環形燈、不用美肌補光、不用霓虹。**

aspect_ratios:
  portrait:  4:5
  vertical:  9:16   # TikTok / Reels / Threads
  square:    1:1
  wide:      16:9

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  同一張圖微調用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty retouch, glamour lighting,
fashion model, influencer pose, thumbs up, peace sign, gym mirror selfie,
flat ears pinned back against the head, small symmetrical ears, straight pinky finger,
glasses, beard, goatee, long hair, man bun, dyed hair, bleached hair,
scrubs, surgical cap, surgical mask, stethoscope, lab coat, white coat,
hospital corridor, operating room, surgery, blood, medical equipment, IV pole,
hospital logo, readable badge text, readable hospital name, barcode,
visible car brand logo, luxury car advertisement, car dealership,
holding phone while driving, texting while driving, phone in hand on steering wheel,
suit and tie, gold chain, luxury watch, designer logo, flashy sneakers,
studio lighting, ring light, softbox, neon lights, RGB lighting, teal-and-orange grade,
HDR, oversaturated, cyberpunk, anime, illustration, 3d render, cgi, cartoon,
extra fingers, malformed hands, warped text, watermark,
stock-photo smile, corporate headshot, beach, surfboard, palm-tree postcard
```

**為什麼要排除這些(不是隨便列的):**
- `flat ears pinned back / straight pinky finger`:招風耳(左耳較明顯)與歪小指是他的辨識點。生圖最容易把耳朵修平、把手指修直。
- `scrubs / surgical cap / stethoscope / hospital corridor / operating room / blood`:**醫療權威暗示是這個人物最大的合規風險**(`08 § 9.6`)。
  他在手術室工作是設定,**畫面裡永遠不出現。**
- `readable badge text / readable hospital name / barcode`:識別證是主錨點,但醫院名稱必須塗黑、不可辨識。
- `holding phone while driving / texting while driving`:**開車用手機的畫面一律禁止**,行駛中的車內鏡頭手機只能在副駕的包裡或 CarPlay 托盤上,沒有人碰。
- `visible car brand logo / luxury car advertisement`:他的車是租來的辦公室,不能變成豪車廣告,也不能出現可辨識的車廠標誌。
- `suit and tie / luxury watch / gold chain`:醫材業務的刻板印象是西裝與名錶。他穿 quarter-zip 與健走鞋,錢花在看不出牌子的東西上(`02 § 10`)。
- `beach / surfboard / palm-tree postcard`:場景漂移。他在南加州,但他的南加州是停車結構的 P4。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | Daniel "Danny" Duy Truong |
| slug | `danny-truong` |
| age_appearance | **32–36** |
| gender | 男 / cis |
| ethnicity | 越南裔美國人。**東南亞骨相,不要被生成成東亞(日韓)或混血的平均臉** |
| build_class | 精實偏厚,肩膀與前臂比一般業務厚(守門員十二年),腰有一點點軟(車上坐太久) |
| location_look | 南加州的膚色,但他大部分時間在室內與停車結構,**沒有海灘曬痕** |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | 橢圓偏方,顴骨略寬,下顎線清楚但不尖 | 東南亞骨相 |
| **膚色** | `#B5875E` 暖調淺小麥色 | 越南裔,南加州 |
| **膚質** | **有毛孔,T 字部位下午會出油,下巴到了下午四點有一點青色的鬍渣陰影。** 鼻翼旁偶爾一顆小痘 | 反美肌,34 歲,一天在外面十二小時 |
| **眼睛** | 深棕色,單眼皮,眼型細長,外眼角微微上揚 | |
| **眼下** | 淡淡的陰影,加刀的隔天明顯 | |
| **眉毛** | 黑、濃、平直,眉尾稍微往下 | 他不修 |
| **鼻子** | 鼻樑中低,鼻頭寬圓 | |
| **嘴** | 中厚,嘴角自然微微上揚(業務的休息臉) | |
| **牙齒** | 整齊、自然的米白色 | |
| **【第一辨識點】耳朵** | **兩邊都有一點招風,左耳比右耳明顯更往外翻,正面就看得到。** | 天生的。小學被笑過,現在他自己先講。**任何一張圖都不可以把它修成貼平的耳朵** |
| **表情基準** | **友善、專注、嘴角帶一點笑**(業務的預設表情) | 見 3.6 |

### 3.2 頭髮

- 黑色(`#1A1714`),直,髮質粗硬。
- **低漸層(low taper)兩側推短,頂部約 6 公分,左側分線,抹一點霧面髮蠟,往右後梳。**
- **永遠是剛剪完兩週內的樣子**:他每兩週去 Westminster 的 Tony 那裡剪一次(`05 § 11`)。
- 週日踢完球:頭髮塌掉、有汗,這是唯一亂的時候。
- **不可以:** 長髮、染髮、挑染、油頭大背頭、男生的髮髻、白髮。

### 3.3 身體

- **身高 173 cm(5'8")。體重約 74 kg。**
- 肩膀厚,前臂粗(守門員),手掌寬。腰有一點軟,polo 衫下面看得出來。
- **姿勢:站的時候重心在兩腳中間,雙手常常插在褲子前口袋(其實是在確認兩支手機)。** 坐在車裡時椅背調得比較直(他在車上打字)。
- 手:**手指粗短,指甲短而乾淨。右手小指第二節往外歪**(2009 年守門脫臼沒固定,`03` 小事件)。
  **他拿手機時,小指剛好卡在手機底部,像一個小架子。**
- **不戴戒指**(訂婚了,男方沒有戒指)。左手腕 Apple Watch,黑色運動錶帶。
- 沒有刺青、沒有耳洞、沒有疤。**頭髮兩側推短,所以耳朵永遠露在外面。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **【第一辨識點】招風耳,左耳比右耳更往外。** 正面與側面的畫面都必須看得到,而且左右不對稱。
2. **右手小指第二節往外歪。** 手部特寫必須有;拿手機的姿勢會讓它更明顯。
3. 低漸層加左側分線,永遠很整齊。
4. **不可以出現的:** 雀斑、單側白髮、眉毛上的疤、臉上或手上的任何疤痕、門牙缺角、曬黑的單邊前臂(這些已經被其他人物用作辨識點,或在撞型檢查時被拿掉過,也不屬於他)。

### 3.5 眼鏡

**不戴。** 視力正常。**開車往西的那段下午,他戴一副黑色的普通太陽眼鏡**(沒有牌子),停好車就推到頭頂或掛在 polo 的領口。

### 3.6 表情庫(九宮格)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 友善、專注,嘴角微微上揚,眼睛看著對方或手上的東西 | 60% 的畫面 |
| **listening** | 頭微微偏一邊,輕輕點頭,嘴唇閉著 | 聽客戶講話、聽媽媽的語音 |
| **half smile** | 閉嘴笑,嘴角兩邊往上,眼尾有細紋 | 他最常見的笑 |
| **real laugh** | 頭往後仰一點,眼睛瞇成一條線,露出上排牙齒 | 跟 Khang、跟 Lauren |
| **"Appreciate it. Pass."** | 很有禮貌的閉嘴微笑,頭輕輕搖一下,眼睛沒有在笑 | 拒絕 IT、拒絕業配 |
| **demo face** | 眼睛微瞇,嘴往一邊撇,下巴稍微往後收 | 看產品示範影片、找剪接點 |
| **tired** | 後腦靠在頭枕上,眼睛閉著,polo 領口鬆開 | 加刀之後,車位裡 |
| **irritated** | 下巴收緊,看著那個東西,**不看人、不皺眉**,手很用力 | 手機卡在支架上、iPad 沒電 |
| **"dạ dạ"** | 一直點頭,嘴巴說「是、是」,眼神有一點放空 | 聽媽媽講婚宴 |

**❌ 絕對不出現的表情:** 誇張大笑對鏡頭、比讚、比 YA、嘟嘴、網紅式驚訝摀嘴、「成功業務」的雙手抱胸、企業形象照的露齒笑。

### 3.7 聲音(給 Libai 的口播用)

| 參數 | 設定 |
|---|---|
| 音高 | 男中音(baritone),基頻約 **110–120 Hz** |
| 語速 | **快,約每分鐘 170 詞。** 講到站數與時間時會停一下,把數字講清楚 |
| 口音 | **南加州一般美語**,母音放鬆,句尾偶爾有一點氣泡音(vocal fry)。**講越語時是南越口音** |
| 音色 | 溫暖、有一點沙。**一天講了八小時的話之後,晚上的聲音比早上低** |
| 特徵 | **講到「Not a doctor.」時會變快、變平**(他講過太多次了) |
| 笑聲 | 先一聲短的 "heh",然後如果真的好笑,會變成一個大笑 |
| 填充詞 | "so"、"honestly"、"like"(少);只跟 Khang 講 "dude" |
| 情緒起伏 | 中。**興奮時講更快、手會攤開(業務的手勢),然後他會發現自己在做手勢,把手收回口袋** |
| 絕不出現 | 播報腔、廣告腔、「Hey guys!」、「What's up, fam」、業務勵志腔、醫療專業腔 |

### 3.8 鏡頭前的肢體習慣

- **下車前拍四下口袋:左前、右前、後口袋、鑰匙。** 招牌動作,任何下車鏡頭都可以用。
- **停好車,用指節在方向盤上敲兩下**,然後熄火。
- 下車後**抬頭看停車結構的樓層標示**(P4、East),他在記位置。
- 講話時會攤開手掌(業務的手勢),**發現自己在做之後,把手插回口袋。**
- 拿手機:右手,**歪掉的小指撐在手機底部。**
- 聽媽媽語音時:手機貼耳,另一隻手扶著方向盤或車門,一直點頭。
- **他會看鏡頭**(他是業務,他習慣看人的眼睛),但時間短,而且只在停好的車裡。

### 3.9 拍照與自拍行為(決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | 一年 10–20 張,**全部在停好的車裡或家裡**,多半是跟 Lauren、跟家人 |
| 出現在畫面裡的方式 | **TikTok:停好的車裡,前鏡頭,半身。** 也常常只有手(拿咖啡、翻下遮陽板、拍口袋) |
| 拍什麼 | **車裡(50%)、食物(20%)、家人與活動(20%)、停車結構的景(10%)** |
| 構圖 | 隨手,第一人稱視角多,儀表板常常入鏡 |
| 後製 | 不調色。TikTok 用平台內建字卡 |
| 器材 | iPhone 17 Pro(私人)。**公司手機不拍任何東西** |
| **絕不拍** | **醫院內部、手術室、刷手服、任何病人、任何醫院名稱、行駛中的車內(除非手機架在固定位置自動錄、他沒碰手機)** |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「停好的車」與「他的手」,不是醫院,也不是他穿刷手服的樣子。**

---

## 四、服裝系統(三套 + 變體)

外型必須對得起 `02 § 10`:**錢花在每天用、看不出牌子的東西上。** 沒有任何看得見的 logo。

### 4.1 Field Outfit(跑醫院的日子,週一到週五早上)

```
- 深藍或炭灰色的 quarter-zip 機能套頭衫(沒有 logo;公司發的那件有 logo,他不穿上鏡頭)
- 白色或淺藍色 polo 衫在裡面
- 灰色修身卡其褲
- 白色皮革健走鞋,鞋頭有一點刮痕(同一款的第三雙,US$245)
- Apple Watch,黑色運動錶帶
- 褐色皮帶
- 熱的下午:quarter-zip 脫下來,掛在副駕椅背後面
- 進手術室時會換醫院的刷手服(**不入鏡**)
```

### 4.2 Admin / Home(週五下午、晚上)

```
- 灰色圓領 T 恤
- 黑色運動長褲
- 拖鞋
- 頭髮還是整齊的(髮蠟到晚上才塌)
```

### 4.3 Weekend(週六爸媽家、週日足球)

```
- 週六:短袖素色或低調小圖案的襯衫、卡其褲、白色球鞋。媽媽喜歡他穿襯衫
- 週日:黑色長袖守門員球衣、黑色短褲、守門員手套、頭髮塌掉
```

### 4.4 Driving(車內畫面)

```
- 依當天是 4.1 或 4.2
- 下午往西開:黑色普通太陽眼鏡,停好就推到頭頂
- 2026 年 10 月 8 日之後:公司手機在副駕的公事包開口裡,螢幕朝上;私人手機在中控台的無線充電托盤上
- 之前(歷史畫面):公司手機夾在儀表板右側的彈簧夾支架上(支架四號,看不出牌子)
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | Apple Watch,黑色運動錶帶。**不是機械錶、不是名錶** |
| 戒指 | **沒有**(訂婚了,男方沒有) |
| 太陽眼鏡 | 黑色普通款,沒有牌子 |
| 包 | **2019 年的深灰彈道尼龍拉桿公事包,握把磨亮的一塊** |
| 眼鏡 | **不戴** |
| **不戴的** | 項鍊、手鍊、名錶、領帶、西裝、有大 logo 的任何東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

### 五個不可變的錨(Immutable Anchors)

1. **招風耳,左耳比右耳更往外**,不可以被修平
2. **右手小指第二節往外歪**,手部特寫必須有
3. **黑色低漸層、左側分線,永遠整齊**,換髮型等於換人
4. **皮膚有毛孔、下午有鬍渣陰影、不磨皮**,反美肌
5. **場景是停好的車、停車結構、公寓,永遠不是醫院內部**

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 穿刷手服、戴手術帽、掛聽診器、醫院走廊 | 醫療權威暗示,`08 § 9.6` 第一條 |
| 2 | 耳朵被修平或變對稱、小指被修直 | 第一與第二辨識點 |
| 3 | 西裝、領帶、名錶、金鍊 | 違反 `02 § 10` 的消費邏輯,也是醫材業務的刻板印象 |
| 4 | 豪車廣告、看得見車廠標誌 | 他的車是租來的辦公室 |
| 5 | 開車時手上拿手機 | 法規與安全,`08 § 9.6` |
| 6 | 健身房鏡子自拍、肌肉展示 | 他不是健身帳號 |
| 7 | 海灘、衝浪、棕櫚樹明信片 | 他的南加州是 P4 |
| 8 | 東亞(日韓)或混血平均臉 | 越南裔骨相 |
| 9 | 出現可辨識的醫院名稱、識別證文字、真實品牌 logo | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段 |

### 連續性檢查表(每次出圖後跑)

- [ ] 耳朵是招風的嗎?左耳是不是比右耳更往外?
- [ ] 右手小指是歪的嗎?(有手的圖)
- [ ] 髮型是低漸層、左側分線、整齊?
- [ ] 皮膚有沒有被磨皮?
- [ ] 有沒有任何醫療元素(刷手服、聽診器、手術室、醫院走廊)?(不可以)
- [ ] 識別證上的醫院名稱是不是塗黑、看不出來?
- [ ] 有沒有車廠 logo、品牌 logo?(不可以)
- [ ] 車在行駛中嗎?如果是,他的手有沒有碰手機?(不可以)
- [ ] 場景是不是停車結構、車內或公寓?
- [ ] 手有沒有畫壞?

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic smartphone documentary photograph, available light only,
no retouching, visible skin texture and pores,

a 34-year-old Vietnamese American man, 173cm, compact solid build with thick
shoulders and forearms and a slightly soft waist,
oval-square face with slightly wide cheekbones and a clean jawline,
warm light tan skin (#B5875E), slight shine on the forehead and nose,
a faint five o'clock shadow on the chin and upper lip,
dark brown monolid eyes, narrow and slightly upturned at the outer corners,
thick straight black eyebrows,
a medium-low nose bridge with a broad rounded tip, medium-full lips with corners
naturally turned up,
slightly protruding ears, his LEFT ear sticking out noticeably more than the right,
clearly visible because the sides of his head are cut short,
straight coarse black hair (#1A1714) in a neat low taper fade,
about 6cm on top, parted on the left and brushed back to the right with matte pomade,
no glasses, no beard, no jewelry except a black sport-band smartwatch on his left wrist,
thick short fingers with short clean nails, the right pinky finger visibly bent
outward at the middle joint,

friendly, attentive expression with a slight closed-mouth smile,

colour palette: parking-structure concrete #3A3F44, silver car paint #BFC3C7,
Irvine stucco beige #D9C6A8, iced coffee brown #6B4426,
with a small accent of badge red #C8102E under 5% of frame
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, seated in the driver's seat of a parked silver mid-size SUV
with a black interior, no visible brand logo, inside a concrete parking structure,
hard afternoon sunlight cutting in from the open side of the structure across
half his face, navy quarter-zip pullover over a white polo,
smiling, his left ear sticking out more than the right and clearly visible,
shot from the passenger seat with an iPhone, slight wide-angle,

--ar 4:5
```

### 6.3 Full body(全身,停車結構,9:16)

```
[MASTER CHARACTER BLOCK]

full body standing next to the open driver's door of a parked silver SUV on
level P4 of a concrete parking structure, a painted sign reading "P4" on a pillar
behind him, patting his front pockets with both hands, a dark grey ballistic nylon
rolling briefcase with a worn shiny patch on the handle standing beside him,
navy quarter-zip, grey slim chinos, white leather walking sneakers with a scuffed toe,
mid-morning light, oil stains on the concrete, no hospital signage visible,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up photograph, natural car-interior light, 35mm phone lens,

the underside of a lowered driver's sun visor inside a parked car, about thirty
expired paper visitor badge stickers overlapping like roof shingles in one
horizontal row, only the top edge of each sticker showing, each edge with red
diagonal "EXPIRED" stripes, the last sticker on the right fully visible with its
institution name completely blacked out with thick black marker, the small photo
box on it too small and blurred to identify, the vanity mirror half covered,
no readable text, no barcodes,
a man's hand with a visibly bent right pinky finger pulling the visor down,
no faces, no logos,

--ar 1:1
```

### 6.5 In-car / lunch on P4(9:16)

```
[MASTER CHARACTER BLOCK]

parked in a concrete parking structure on the top shaded level, engine on for
air conditioning, a folded silver reflective sunshade across the windshield,
eating a banh mi wrapped in paper, a laptop balanced on the center armrest,
two iced Vietnamese coffees in the cupholders (one full, one with melted ice),
a smartphone lying face up on the console wireless charging tray,
a second phone in a thick black rugged case lying face up in the open top of a
briefcase on the passenger seat,
he is looking at the laptop, not at the camera, relaxed,
shot from the passenger side,

--ar 9:16
```

### 6.6 Home desk / 6:10 a.m.(4:5)

```
[MASTER CHARACTER BLOCK]

a small apartment second bedroom before dawn, the room lit only by a phone
flashlight held in his left hand, a white standing desk at fixed height,
a power strip with a red rocker switch and a three-way splitter sitting on the
back right corner of the desk with a tangle of white and black cables,
he is unplugging a tablet with his right hand, a thick black rugged-case phone,
a second phone, a smartwatch, earbuds case and a power bank lined up on the desk,
a folding exercise bike and cardboard boxes marked "5.8", "5.15", "5.22" at the edge of frame,
grey crew-neck t-shirt, hair still neat, sleepy,
no blue or purple glow, no brand logos,

--ar 4:5
```

### 6.7 Office-in-car / between stops(16:9)

```
[MASTER CHARACTER BLOCK]

wide shot through the open passenger window of a parked silver SUV in a
parking structure, the man in the driver's seat on a phone call using the car's
hands-free system, both hands visible and empty (one resting on the steering
wheel, one gesturing with an open palm), a briefcase on the passenger seat with
its top pocket open and a phone in a thick black case lying face up inside,
the dashboard to the right of the centre screen bare and clean,
concrete pillars and a "P3" sign, cool shade with a strip of bright sun on the
hood,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in
every panel, head and shoulders, plain warm grey background, navy quarter-zip,
his left ear visibly sticking out more than the right in every panel:
1 friendly attentive default with a slight closed-mouth smile,
2 listening with head slightly tilted and a small nod,
3 closed-mouth half smile with crinkled eye corners,
4 a real laugh with head tipped back, eyes squeezed shut, upper teeth showing,
5 a polite closed-mouth smile with a small head shake and unsmiling eyes,
6 skeptical with eyes narrowed and mouth pulled to one side,
7 tired with the back of his head against a car headrest and eyes closed,
8 irritated with a set jaw, looking down at an object, no frown,
9 nodding with slightly glazed eyes while listening to a phone held to his ear,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
before getting out of the car he pats four places in order: left front pocket,
right front pocket, back pocket, then the keys in his hand.
when he parks he taps the steering wheel twice with a knuckle, then turns off
the engine. after stepping out he glances up at the parking level sign.
when he explains something his palms open like a salesperson, and when he
notices he is doing it he puts his hands back in his pockets.
he holds his phone in his right hand with the bent pinky resting under the
bottom edge. he never touches a phone while the car is moving.
he looks at the camera briefly and warmly, only inside a parked car.

VOICE: baritone, around 115 Hz, about 170 words per minute, relaxed Southern
California American vowels with a little vocal fry at the end of sentences,
numbers and times spoken slowly ("six ten a.m.", "stop nine of nine"),
"not a doctor" said fast and flat, a short "heh" before a real laugh.
no broadcast energy, no sales pitch tone, no medical or clinical vocabulary.

CAMERA: handheld iPhone, front camera or passenger-seat angle, slight
wide-angle, available light only, parked car or apartment only,
never inside a hospital.
```

---

## 七、外型與人設的一致性驗算

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 招風耳(左耳較明顯) | `04 § 15` 走廊上的人先記得那對耳朵 | ✓ |
| 右手小指歪 | `03` 2009 年守門脫臼 | ✓ |
| 肩膀與前臂厚 | `02 § 11` 守門員十二年 | ✓ |
| 腰有一點軟 | `06 § 五` 車上坐太久 | ✓ |
| 低漸層、兩週一剪 | `05 § 11` Tony | ✓ |
| quarter-zip、健走鞋、沒有 logo | `02 § 10-2` 看不出牌子的貴 | ✓ |
| 沒有戒指 | `02 § 4` 訂婚 | ✓ |
| 不戴眼鏡,下午戴太陽眼鏡 | `01 § 1-B` 往西的下午 | ✓ |
| 從不在醫院入鏡 | `02 § 17`、`08 § 9.6` | ✓ |
| 拍口袋四下 | `02 § 6` 兩支手機、識別證、鑰匙 | ✓ |
| 沒有雀斑、白髮、疤 | 刻意:避開與其他人物撞型(`00 § 四` 第 13 項) | ✓ |

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲音、3.8 肢體、6.9 影片提示詞、五個不可變錨。**場景只能是停好的車、停車結構、公寓。**
**Ivy(Amazon 素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**他是醫材業務這件事,不可以出現在任何商業素材上**:不穿刷手服、不出現識別證、不出現醫院、不出現「醫療」任何字眼(`08 § 9.6`)。

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait_parked | *(本輪未生成)* | | | |
| full_body_P4 | *(本輪未生成)* | | | |
| visor_badges | *(本輪未生成)* | | | |
| lunch_P4 | *(本輪未生成)* | | | |
| desk_0610 | *(本輪未生成)* | | | |
| expression_sheet | *(本輪未生成)* | | | |

> **本輪任務指定不生圖。** 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。
> **第一次出圖要特別檢查兩件事:耳朵有沒有被修平(左耳要比右耳更往外)、識別證上有沒有長出可讀的醫院名稱。** 這是這個人物最容易失敗的兩個地方。

---

*檔案版本:v1.0 — 2026-10-21 建立*
