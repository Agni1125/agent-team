# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人,也是同一張桌子。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。
>
> **這個人物的視覺主體是桌子,不是臉。** 他的 IG 九成是桌面照,露臉不到一成。
> 所以這份檔案的「桌子一致性」跟「臉一致性」一樣重要。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   tzu-chien-wei
display_name:     魏子謙 Wei Tzu-Chien(TC)

art_style:        photorealistic desk and lifestyle photography
                  # 不是 CG、不是 3D 渲染、不是型錄。是一個很會拍的人用 APS-C 相機拍自己的桌子。
style_reference:  night-time desk photography on a small tripod, APS-C 23mm (35mm equivalent),
                  f/5.6, long exposure 1/4s–2s, ISO 160,
                  lit only by a monitor light bar and one small 2700K desk lamp,
                  warm-neutral white balance, deep but not crushed shadows,
                  real dust and wear visible, no CGI smoothness

color_palette:
  - "#2B2D31"   # graphite — 鍵盤鋁殼、螢幕邊框、夜晚的房間
  - "#5A4535"   # walnut — 胡桃木紋桌板、白熊做的木架
  - "#6E7076"   # felt grey — 毛氈桌墊
  - "#8A6A4F"   # coffee stain — 桌墊左下角那塊咖啡漬。**只能在那個位置**
  - "#F0B46A"   # 2700K lamp amber — 檯燈的暖光。點綴用,不超過畫面 10%
  - "#C8102E"   # velcro red — 那條「不准關」的魔鬼氈。**只能是一個小點,而且通常在桌下**

lighting_default: practical light only.
                  夜景(主):螢幕掛燈打在桌墊中央 + 2700K 小檯燈從右後方;房間其他地方暗。
                  白天(少):西曬被深灰捲簾擋住,只有捲簾縫的光。
                  公司:不拍。
                  **不用環形燈、不用柔光箱、不用 RGB、不用藍紫色電競光。**

aspect_ratios:
  portrait:  4:5     # IG feed(他的主場)
  vertical:  9:16    # Threads 圖、IG 限動、TikTok、Reels
  square:    1:1
  wide:      16:9    # 很少用

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  **桌面要跟人一樣鎖 seed。** 同一版(v9)的桌面照用同一組 seed 微調;
                  換版本(v10)才換 seed,並在 changelog 寫清楚改了什麼。
```

### Negative prompt seed(所有生圖必帶)

```
k-pop idol, korean male model, boy band, styled hair, perm, dyed hair,
v-shaped face, sharp jawline model, six-pack, gym influencer, flexing,
airbrushed skin, beauty filter, porcelain skin, glass skin,
designer clothes, luxury watch, gold jewelry, rings, necklace,
RGB lighting, neon, purple and blue gaming lights, LED strips, gaming chair,
perfectly clean CGI desk, 3d render, product catalog render, showroom,
floating cables, cable spaghetti, tangled wires on desk surface,
fake brand logos, readable brand names, unreadable chinese characters, garbled text,
simplified chinese signage, watermark, UI text overlay,
coffee latte art, flat lay with flowers, pastel aesthetic,
extra fingers, malformed hands, warped keyboard keys, melted cables, bent monitor
```

**為什麼要排除這些(不是隨便列的):**
- `k-pop idol / korean male model / styled hair / v-shaped face` — AI 生「台灣年輕男性」最常滑過去的方向。他是羅東長大的後端工程師。
- `six-pack / gym influencer` — 他抱石,前臂粗,但身材普通。不是健身網紅。
- `RGB / neon / gaming chair` — 違反 `02 § 11`「RGB 是 2018 年的事」。
- `perfectly clean CGI desk / 3d render / showroom` — **這是最重要的一條。** 他的桌子很整齊,
  AI 很容易把它生成成型錄渲染圖。**品牌 TA v1.2 的反感清單明寫「AI 味的完美渲染圖」會掉單。**
  他的桌子要看得出有人在用:桌墊的咖啡漬、鍵帽的油光、螢幕上一點灰。
- `cable spaghetti / tangled wires on desk surface` — **反向的錯。** 他的線是整齊的,
  但不是「不存在」。線要看得到,沿著桌腳、在線槽裡,有半徑地轉彎。
- `readable brand names / fake brand logos` — 法遵,也符合他「只寫規格不寫牌子」的規矩。
- `simplified chinese signage` — 他在台北。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 魏子謙(TC) |
| slug | `tzu-chien-wei` |
| age_appearance | **28–31** |
| gender | 男 / he-him |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系偶像** |
| build_class | 精瘦,肩膀普通寬,**前臂明顯比上臂粗**(抱石),脖子略往前(久坐) |
| location_look | 台北科技業上班族。**不曬,但不白**;手指有繭 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **長橢圓臉**,顴骨略高,下巴圓鈍不尖 | 反 V 臉、反方下巴模特臉 |
| **膚色** | `#C99A72` 偏暖的小麥色,**不白**。額頭與鼻翼偏油 | 台灣男性的常態,不曬也不白 |
| **膚質** | **有毛孔,鼻翼與額頭偏油,沒有痘疤。** 週一下巴有一點鬍渣(週末沒刮) | 反美肌 |
| **眼睛** | 深棕色,**很窄的內雙**,眼型偏細長,眼尾平。**看螢幕太久時眼白有一點紅** | |
| **眉毛** | 濃、平、眉頭略粗,**完整,沒有疤** | 斷眉是 `persona_tw_06` 的辨識點 |
| **鼻子** | **鼻樑中段一個小凸起,略往右偏;眼鏡因此永遠微微往左斜。** 鼻頭略寬 | **第一辨識點。** 十歲騎腳踏車在羅東運動公園摔的 |
| **嘴** | 唇形中等,嘴角平。**不笑的時候看起來在想事情** | |
| **表情基準** | **平、專注、眉頭不皺。** 看東西時頭會微微歪向右邊(在檢查對齊) | 見 3.6 |

### 3.2 頭髮

- 黑色(`#1A1A1A`),**沒染過**。
- **短髮,兩側推短(不是很短的漸層,是普通理髮店的推短),頭頂約 5 公分,自然往右前撥。**
- **頭頂偏後有一個髮旋,那裡永遠有一小撮翹起來。** 他壓不下去,也放棄了。
  ← 這條寫死,它是「這個人沒有在打理髮型」的視覺速記,也是側面與背面的辨識點。
- 一個月剪一次,內湖一間百元理髮。剪完一週最整齊,三週後兩側長出來。
- 不抓髮蠟。**不要畫成韓系的逗號瀏海或旁分油頭。**

### 3.3 身體

- **176 cm、68 kg。**
- 肩膀普通寬,**脖子略往前**(久坐 + 看螢幕),他意識到的時候會挺一下。
- **前臂:** 抱石練出來的,前臂肌肉線條明顯,**比上臂看起來粗**。手腕不細。
- 腰腹平,沒有腹肌線條。腿普通。
- **手:** 手指長,指節略粗。**指腹有繭,左手中指第二節常常貼一小段白色運動膠布,或有結痂。**
  指甲剪得很短很平。**手是這個人物最常入鏡的身體部位,任何近景都要拍到。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **鼻樑中段的小凸起與微微左斜的眼鏡。** 任何正臉或側臉都必須有。**第一辨識點。**
2. **頭頂的髮旋翹毛。** 任何側面或背面都必須有。
3. **左手中指的白色運動膠布 / 結痂。** 出現機率 60%。
4. **左手腕一支黑色運動錶帶的智慧錶**(不露品牌)。on-call 週一定戴。

### 3.5 眼鏡(狀態指示器)

- **透明灰色膠框方形眼鏡**,框不粗,近視約 -4.00。鏡片有一點抗藍光的反光。
- **在家、上班、晚上戴眼鏡;抱石、拍照(自己入鏡時)、約會戴隱形眼鏡。**

| 眼鏡狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 戴著 | 工作、桌子時間、深夜 | 桌前、公司、凌晨 |
| 推到額頭上 | 靠近看線怎麼走、看鍵盤的細節 | 理線、組裝 |
| 沒戴(隱眼) | 抱石、約會、回宜蘭的正式場合 | 岩館、外出 |
| 掛在 T 恤領口 | 剛洗完臉、剛從岩館回來 | 晚上進門 |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 平,專注,嘴角平,眼睛看物件 | 70% 的畫面 |
| **checking alignment** | **頭微微歪向右,一隻眼睛瞇一點**,在看東西有沒有對齊 | 擺桌子、拍照前 |
| **real smile** | **嘴角往右邊歪一點、不露齒,鼻子出一口氣。** 他真正的笑 | 一條線走得剛剛好、阿廷講幹話 |
| **laugh** | 低頭,肩膀抖,手背擋一下嘴 | 跟阿甫、阿廷吃飯 |
| **deadpan** | 眼睛半閉,嘴角完全不動 | PM 說「這個很簡單吧」 |
| **satisfied** | 往椅背一靠,雙手放在頭後面,看著桌子 | v9 上線那天 |
| **tired** | 眼鏡推到額頭,拇指跟食指捏鼻樑 | on-call 半夜 |
| **reading a log** | 身體往前,臉靠近螢幕,嘴唇微微動 | 告警響的時候 |
| **pinching slack** | **用拇指與食指捏住一段線,估量多出來的長度** | 理線,他的招牌動作 |

**❌ 絕對不出現的表情:** 比 YA、對鏡頭眨眼、歪頭裝可愛、網紅式的「露齒大笑看鏡頭」、
任何韓系或日系偶像的表情、**戲劇化的「驚訝臉」縮圖表情**。

### 3.7 聲音(給 Libai,**很少用**)

| 參數 | 設定 |
|---|---|
| 使用頻率 | **很低。** 他的 TikTok 九成沒有人聲,只有環境音與字卡。人聲一個月最多一支 |
| 音高 | **中低**,基頻約 **115–130 Hz** |
| 語速 | **約每分鐘 210 字。** 平穩,不太有起伏 |
| 口音 | **台灣國語,台北上班族的標準口音。** 宜蘭腔只在跟爸爸講台語時出現 |
| 音色 | 乾淨、略悶,**像在會議室裡講話** |
| 英文術語 | 自然念出,不刻意標準:「rollback」「changelog」「known issue」 |
| 特徵 | **句子短,常用「然後」接下一句。** 講完一段會停半秒 |
| 笑聲 | 鼻子出一口氣,「哼」一聲 |
| 填充詞 | 「然後」(多)、「就是」(中)、「對」(句尾確認)、「嗯」(開頭) |
| 絕不出現 | 「哈囉大家好」「各位朋友」「家人們」、播報腔、開箱 YouTuber 的高亢、中國腔兒化音 |

### 3.8 鏡頭前的肢體習慣

- **捏線估長度:** 用拇指與食指捏住一段線,往外拉一點,看多出來幾公分。招牌動作。
- **擺完東西,用食指在桌邊敲兩下。** 他自己叫這個「merge」。
- **頭歪向右、一隻眼瞇一點**,檢查東西有沒有對齊。
- 用**食指指節**把眼鏡推回去,不用指尖。
- 抱石前會把十根手指一根一根往後扳。
- 告警響的時候,**第一個動作是看左手腕的錶**,第二個動作才是拿手機。
- **他看鏡頭的時間很短,看物件的時間很長。**

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎沒有。** IG 一年一兩張,通常是鏡子裡拿著相機的倒影 |
| 出現在畫面裡的方式 | **手(打鍵盤、捏線、拿相機)、手腕、背影、側面的剪影。** TikTok 露臉 < 10% |
| 拍什麼 | **桌子。** 全景、俯拍、45 度、桌下走線、局部特寫。其次是岩館的牆、窗台的黃金葛 |
| 構圖 | **非常準。** 對稱或嚴格的三分線,水平線一定是平的 |
| 光線 | **控制過。** 只用螢幕掛燈 + 2700K 小檯燈,長曝。**這是他跟一般隨手拍最大的差別** |
| 後製 | **輕。** 拉白平衡、拉陰影,不加濾鏡、不加顆粒 |
| 器材 | 二手富士 APS-C + 23mm,小腳架。限動與 Threads 用 iPhone |
| **刻意保留的瑕疵** | 咖啡漬、鍵帽油光、螢幕一點灰、黃金葛一片黃葉。**他說「沒有瑕疵的桌面照是渲染圖」** |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「桌、線、手」,臉是例外。**
> **構圖要準,光要控制,但一定要有使用痕跡。** 太完美就是 AI 圖,而他的讀者就是會抓 AI 圖的那群人。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**錢花在桌子上,身上穿的是普通的、乾淨的、不顯眼的東西。** 他沒有在打扮,但他不邋遢。

### 4.1 Office Outfit(進公司日)

```
- 深灰色或黑色素 T(平價快時尚,NT$390 上下),沒有印字
- 黑色連帽外套(公司的週年紀念 hoodie,左胸一個很小的 logo,**生圖時一律不可辨識**)
- 深藍色直筒機能長褲
- 灰色慢跑鞋(穿了兩年,鞋底有磨損)
- 黑色後背包(機能款,側邊掛一個小登山扣,上面沒掛東西)
- 黑色錶帶智慧錶,左手
- 透明灰膠框方形眼鏡
← 公司的冷氣很冷,所以 hoodie 一年四季都在
```

### 4.2 Desk Night Outfit(桌子時間,家裡)

```
- 洗到很軟的黑色舊 T(有一件是大學系 T,背後的字已經裂了,**生圖不露字**)
- 灰色棉質短褲
- 黑色室內拖鞋
- 眼鏡戴著
- 錶拿下來放在白熊做的木架上(他不戴錶睡覺)
- 頭頂的髮旋翹起來
```

### 4.3 Climbing Outfit(抱石館)

```
- 寬鬆的灰色或橄欖綠素 T
- 深色彈性攀岩褲,膝蓋有粉的白痕
- 抱石鞋(紅黑色,鞋頭磨損)
- 腰上掛粉袋
- 隱形眼鏡
- **左手中指的白色膠布**
```

### 4.4 Going Out(約會、回宜蘭、朋友婚禮以外的外出)

```
- 白色素 T 或淺藍牛津襯衫
- 橄欖綠工作外套(十月起)
- 黑色直筒牛仔褲
- 白色帆布鞋(洗過,但洗不乾淨了)
- 隱形眼鏡
- 頭髮會用手撥一下,但那撮翹毛還在
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **黑色運動錶帶的智慧錶**(不露品牌)。不是機械錶 |
| 眼鏡 | 透明灰膠框方形(見 3.5) |
| 背包 | 黑色機能後背包,裡面一個黑色小收納包「出差包」 |
| 手機殼 | 深灰色矽膠殼,邊角磨白,背面有 MagSafe 的圓形壓痕 |
| 耳機 | 白色無線耳機(不露品牌) |
| 膠布 | 白色運動膠布,左手中指 |
| **不戴的** | 戒指、項鍊、手環、名牌包、機械錶、耳環、任何 logo 很大的東西 |

---

## 五、Desk Visual DNA(桌子的視覺一致性,**跟臉一樣重要**)

> 這個人物的臉一個月出現不到一次,桌子每天出現。**桌子換一個樣子,讀者會比臉換了更快發現。**

### 5.1 桌子 A(v9)的不可變元素

| 元素 | 描述 |
|---|---|
| 桌板 | **140×70 深色胡桃木紋**(不是實木,是美耐板木紋),左前角有一點磕痕 |
| 桌墊 | **深灰毛氈,約 90×40,左下角手掌大咖啡漬**,形狀像歪掉的逗號 |
| 螢幕 | 27 吋,**黑色細邊框**,夾式螢幕臂(深灰色),螢幕上緣夾著一支黑色螢幕掛燈 |
| 鍵盤 | **65% 鋁殼,深灰色**,鍵帽灰白兩色,空白鍵是深灰 |
| 觸控板 | 在鍵盤右邊,深灰色 |
| 筆電 | 直立架,在螢幕左邊,深空灰色 |
| 右邊 | 三合一充電立架(黑色)、白熊的胡桃木小架子 |
| 檯燈 | **黑色小檯燈,右後方**,2700K |
| 窗台 | 黃金葛,一片黃葉 |
| 桌下 | 黑色金屬網線槽、**白色充電器(唯一的白色)**、紅色魔鬼氈、Mac mini 在夾式層板上 |

### 5.2 線的規則(AI 最容易畫錯的地方)

- **桌面上看得到的線只有三條:** 筆電一條、鍵盤一條(充電時)、立架一條。都沿著桌面後緣走。
- 線轉彎有半徑,不會折成直角,不會懸空。
- **桌下的線都在線槽裡,沿桌腳下去。** 一條紅色魔鬼氈綁在左後桌腳那條延長線上。
- 線是黑色的,有一條是灰色編織線。**沒有彩色線。**

### 5.3 禁止的桌面

- 沒有任何線的「魔法桌」(他的線是整齊的,不是不存在)
- 桌面上纏成一團的線(那是別人的桌子)
- RGB 燈條、電競椅、電競耳機架
- 任何可辨識品牌的 logo
- **SPACION 桌面充電站本體或渲染圖(產品不存在)**

---

## 六、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **鼻樑的小凸起、眼鏡微微左斜**,露臉就要有
2. **頭頂髮旋的翹毛**,側面與背面就要有
3. **透明灰膠框方形眼鏡**(在家、上班的畫面),換款式等於換人
4. **前臂比上臂粗、左手中指膠布**,手部近景就要有
5. **深灰桌墊左下角的咖啡漬**,桌面照就要有

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系男偶像 / 型男模特 / V 臉 | 違反人物出身,也是 AI 最容易滑過去的方向 |
| 2 | 健身網紅身材、緊身衣 | 他抱石,不是健身 |
| 3 | 精緻髮型、染髮、油頭 | 百元理髮、翹毛 |
| 4 | 名牌衣服、機械錶、飾品 | 錢在桌子上 |
| 5 | RGB 電競桌 | 他的審美 |
| 6 | **型錄渲染圖式的完美桌面** | **TA 反感清單,而且他的讀者會抓 AI 圖** |
| 7 | 桌面上一團亂線 | 那不是他 |
| 8 | 大量正臉自拍 | 他的帳號主體是桌子 |
| 9 | 出現可辨識的真實品牌 logo 或真人臉 | 法遵 |
| 10 | 桌子的元素在不同圖之間變化(桌板顏色、鍵盤顏色、咖啡漬位置) | 用同 seed + 第五節解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 鼻樑的小凸起在嗎、眼鏡有沒有微微左斜(如果露臉);眉毛有沒有被畫出疤(不可以)
- [ ] 頭頂的翹毛在嗎(如果是側面或背面)
- [ ] 眼鏡是不是透明灰膠框方形
- [ ] 手:前臂比上臂粗?左手中指有膠布或結痂?手指數量對?
- [ ] 桌墊左下角的咖啡漬在不在?位置對不對?
- [ ] 桌板是深色胡桃木紋?鍵盤是深灰 65%?
- [ ] 桌面上看得到的線是不是只有三條、而且整齊?
- [ ] 有沒有使用痕跡(咖啡漬、灰塵、黃葉)?**太完美就重生**
- [ ] 有沒有 RGB、有沒有品牌 logo、有沒有亂碼中文
- [ ] 色板有沒有跑掉(紅色魔鬼氈是不是只有一個小點、在桌下)

---

## 七、生圖提示詞(英文,可直接使用)

### 7.1 Master character block(人物共用段,不要改)

```
photorealistic photograph, practical light only, APS-C 23mm lens,
natural skin texture with visible pores, no retouching,

a 29-year-old Taiwanese man, 176cm, lean build, slightly forward head posture
from long hours at a desk, forearms noticeably more muscular than his upper arms
from bouldering,
long oval face with slightly high cheekbones and a soft rounded chin,
warm wheat skin tone (#C99A72), slightly oily forehead and nose, visible pores, no acne scars,
dark brown eyes with very narrow inner double eyelids, thick straight unbroken eyebrows with no scar,
a small healed bump in the middle of his nose bridge, the bridge very slightly bent to the right,
so his glasses always sit a little tilted to the left,
short black hair, sides clipped short at an ordinary barbershop, about 5cm on top
brushed to the right, a cowlick at the crown that always sticks up,
translucent grey rectangular acetate glasses,
long fingers with calloused fingertips, a strip of white athletic tape on the second
joint of his left middle finger, short flat nails,
a smartwatch with a plain black sport band on his left wrist, no visible brand,

calm focused expression, mouth neutral, head tilted very slightly to the right
as if checking alignment, looking at an object, not at the camera
```

### 7.2 Master desk block(桌子 A v9 共用段,不要改)

```
a 140x70cm electric standing desk with a dark walnut-grain laminate top,
a small dent on the front left corner,
a dark grey felt desk mat about 90x40cm with a palm-sized brown coffee stain
shaped like a crooked comma in its lower left corner, darker at the edges,
a 27-inch black thin-bezel monitor on a clamp-mounted dark grey monitor arm,
a black monitor light bar clipped on top of the monitor,
a dark grey 65% aluminium mechanical keyboard with grey and off-white keycaps,
a dark grey trackpad to its right, a space grey laptop in a vertical stand left of the monitor,
a black three-in-one charging stand and a small walnut wooden shelf on the right,
a small black desk lamp at the back right glowing 2700K,
a pothos plant on the windowsill with one yellowing leaf,
only three cables visible on the desk, all black or grey braided, running neatly along
the back edge with gentle curves, no loose or tangled wires,
real signs of use: faint dust on the monitor, slight shine on the most-used keycaps,
no brand logos anywhere, no readable text

colour palette: graphite #2B2D31, walnut #5A4535, felt grey #6E7076,
coffee stain #8A6A4F only in the lower left of the mat,
warm 2700K amber #F0B46A under 10% of the frame
```

### 7.3 Desk at night / 桌子 A 全景(他的招牌照片,4:5)

```
[MASTER DESK BLOCK]

night-time photograph of a small rented studio apartment in Taipei,
the room dark except for the monitor light bar pooling cool-white light on the centre
of the felt mat and the warm desk lamp from the back right,
the monitor shows a dark code editor with no readable text,
shot from a small tripod at seated eye height, 45-degree angle from the front left,
long exposure, f/5.6, perfectly level horizon, symmetrical composition,
dark grey roller blind behind the desk, no people

--ar 4:5
```

### 7.4 Top-down / 俯拍(changelog 輪播第一張,4:5)

```
[MASTER DESK BLOCK]

straight top-down overhead photograph of the desk surface at night,
the coffee stain clearly visible in the lower left of the felt mat,
keyboard centred, trackpad right, charging stand and walnut shelf right edge,
light bar pool of light in the centre fading to darkness at the edges,
everything aligned to an invisible grid, no hands, no people

--ar 4:5
```

### 7.5 Under the desk / 桌下走線(他最得意的一張,4:5)

```
photorealistic photograph looking up at the underside of a dark walnut-grain standing desk,
a black metal mesh cable tray clamped under the back edge holding neatly coiled black cables,
a white six-port GaN charger attached under the desk with black velcro, the only white
object in the frame,
a small clamp-on shelf holding a compact silver desktop computer,
two power strips running down two different desk legs, one wrapped with a single
red velcro strap (#C8102E),
cables turning with gentle radius curves, cable ties evenly spaced,
lit by a phone flashlight from below mixed with spill from the desk lamp,
no brand logos, no readable text

--ar 4:5
```

### 7.6 Hands / detail(招牌手部鏡頭,1:1)

```
[MASTER DESK BLOCK — cropped to the lower left of the mat]

close-up of a man's hands, long fingers with calloused fingertips and white athletic
tape on the left middle finger, pinching a black braided USB-C cable between thumb and
index finger to measure the slack, the coffee stain on the felt mat visible beside his
left wrist, a black-band smartwatch on the left wrist,
shallow depth of field, warm lamp light from the right, no face

--ar 1:1
```

### 7.7 Portrait(頭肩,少用,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle from his left so the bump on his nose bridge is visible,
translucent grey rectangular glasses, washed-out black t-shirt,
sitting at his desk at night, cool light from the monitor light bar on his face from above,
warm lamp from the back right, the out-of-focus felt mat and keyboard in the foreground,
f/2.8, subject slightly off-centre

--ar 4:5
```

### 7.8 Bouldering gym(9:16)

```
[MASTER CHARACTER BLOCK — no glasses, contact lenses]

full body from behind and slightly to the side, standing under a bouldering wall in an
indoor gym in Taipei, looking up at a route, chalk bag on his waist, loose olive-green
t-shirt, dark climbing trousers with chalk marks at the knees, worn red-and-black
climbing shoes, chalk on his hands, white tape on the left middle finger,
the cowlick at the crown of his head visible, colourful holds out of focus,
ordinary gym fluorescent light

--ar 9:16
```

### 7.9 The deprecated box / deprecated 箱(1:1)

```
photorealistic photograph of the lower shelf of a small wardrobe in a rented apartment,
a white plastic storage box with a lid, a black-on-white label-maker strip on the lid
reading "deprecated" in lowercase,
lid slightly open showing an indistinct jumble of chargers, cables, small stands and
keycaps inside, nothing in focus enough to identify any brand,
on the shelf above, a row of empty product boxes in plain colours with no readable printing,
warm room light, a man's hand with white tape on the left middle finger placing a
small black object into the box

--ar 1:1
```

### 7.10 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in every
panel, head and shoulders, plain dark grey background, glasses on:
1 calm and focused, 2 head tilted right with one eye slightly narrowed checking alignment,
3 a closed-mouth lopsided smile pulled to the right with a short breath out of the nose,
4 laughing with head down and the back of a hand near his mouth,
5 deadpan with half-closed eyes and a completely still mouth,
6 leaning back with both hands behind his head looking satisfied,
7 tired with glasses pushed up on his forehead pinching the bridge of his nose,
8 leaning close to a screen reading with lips slightly moving,
9 looking down pinching a cable between thumb and index finger

--ar 1:1
```

### 7.11 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]
[MASTER DESK BLOCK]

MOTION / BEHAVIOUR:
he works on the desk mostly with his hands in frame and his face out of frame.
he pinches a cable between thumb and index finger and pulls gently to judge the slack.
when he finishes placing an object he taps the edge of the desk twice with his index finger.
he tilts his head slightly to the right and narrows one eye to check alignment.
he pushes his glasses up with the knuckle of his index finger, not the fingertip.
when a notification arrives his first move is to glance at the watch on his left wrist.
he glances at the camera very briefly, if at all, and returns his eyes to the desk.

VOICE (rarely used): calm mid-low male voice, fundamental around 120 Hz, clean and a little
muffled like speaking in a meeting room, Taiwanese Mandarin with a standard Taipei accent,
around 210 Chinese characters per minute, short sentences joined with "然後",
English technical words said naturally, no greeting, no "記得追蹤", no YouTuber energy.

SOUND: most videos have no voice at all. the sound is the desk: velcro being pulled,
a cable clicking into a port, keyboard switches, the standing desk motor humming,
the soft click of a desk lamp.

CAMERA: locked-off on a small tripod, top-down or 45 degrees, practical light only,
night time, slow and deliberate cuts.
```

---

## 八、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 前臂比上臂粗、指腹繭、中指膠布 | `02 § 8`、`06 § 六` 抱石,2024 A2 拉傷 | ✓ |
| 脖子略往前 | `06 § 六` 久坐、升降桌站得不夠 | ✓ |
| 鼻樑小凸起 | `03` 第一節「小事件」(2007 年十歲,運動公園摔車) | ✓ |
| 頭頂翹毛、百元理髮 | `02 § 10`「藏起來的東西要便宜」延伸到自己身上 | ✓ |
| 平價素 T、公司 hoodie | `02 § 10` 錢在桌子上 | ✓ |
| 智慧錶不是機械錶 | `03 § 1-1` on-call;`02 § 11`「手錶收藏不是他的興趣」 | ✓ |
| 沒有飾品 | `02` 全檔沒有裝飾性消費 | ✓ |
| 桌面照構圖準、光控制 | `02 § 11` 拍桌面是他的嗜好 | ✓ |
| 咖啡漬 | `03 § 7-0` | ✓ |
| 紅色魔鬼氈 | `06 § 一` 那條「不准關」的線 | ✓ |
| 白色充電器在桌下 | `02 § 10`「藏起來的東西要便宜」、`03 § 6-2` | ✓ |
| 很少自拍 | `04 § 13` E 值 45、線上比線下多話 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 九、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線(**幾乎不用**)、3.8 肢體、7.11 影片提示詞、五個不可變錨、**5.2 線的規則**。
**Ivy(素材):** 讀 7.1、7.2 兩個 master block、7.5 桌下鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**
**也不得把他桌下那顆白色充電器畫成任何可辨識的真實品牌。**

---

## 十、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| desk_night_v9 | *(本輪未生圖)* | | | |
| desk_topdown_v9 | *(本輪未生圖)* | | | |
| under_desk_v9 | *(本輪未生圖)* | | | |
| hands_detail | *(本輪未生圖)* | | | |
| portrait | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,不是圖(與 Nathan、葉沛璇相同)。
> 需要出圖時走 `gen-image` skill,把 7.1 與 7.2 兩個 master block 帶進去,生完把 seed 回填到這張表。
> **桌面圖要先生、先鎖。** 這個帳號的讀者對桌子的一致性比對臉更敏感。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.2 | 2026-10-20 | 跨人物撞型修正:第一辨識點由左眉尾疤改為鼻樑中段的小凸起(同一次摔車;左眉尾疤保留給 `persona_tw_06`);拿掉兩頰痘疤(`persona_tw_03`、`persona_tw_04b` 已有) | 主 session 統一 QA:第二批平行生成,十人之間仍有句型、外型辨識點與標點記號撞在一起 |

*檔案版本:v1.2 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
