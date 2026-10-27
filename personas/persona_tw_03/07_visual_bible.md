# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   chi-wei-fan
display_name:     范啟維 Fan Chi-Wei(Chewie)

art_style:        photorealistic documentary photography
                  # 不是 CG、不是遊戲角色立繪、不是電競廣告。是照片。
style_reference:  candid smartphone or 35mm look, mild grain, practical lights only
                  (monitor glow, warm-white desk LED, window daylight),
                  depth of field f/2.8–f/4, no beauty retouching, visible skin texture,
                  East Asian skin rendered true, slightly underexposed night interiors

color_palette:
  - "#101418"   # monitor-off black — 螢幕邊框、主機、夜裡的書房
  - "#4A6FA5"   # screen glow blue — 螢幕打在臉上的冷光
  - "#F3E9D2"   # baked warm white — 他「烘焙掉」的靜態暖白燈(約 3000K)
  - "#2B3A55"   # launch-tee navy — 那件停營運手遊的紀念 T 恤
  - "#6E7681"   # new-build grey — 新大樓的牆、機捷月台、青埔的天空
  - "#F2C94C"   # sticky-note yellow — 「16.6」便利貼。**只能是一個小方塊,不超過畫面 5%**

lighting_default: practical light only.
                  書房夜間:螢幕冷光 + 主機靜態暖白光的混色,房間其他地方偏暗;
                  白天:窗光(西窗,下午會斜射);
                  客廳:電視的光 + 一盞落地燈。
                  **不用 RGB 彩光、不用霓虹、不用電競紅、不用賽博龐克色調。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok、Reels
  square:    1:1
  wide:      16:9    # YouTube、橫式素材

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
k-pop idol, boy band face, v-shaped jaw, sharp chin, flawless skin, airbrushed skin,
beauty filter, glass skin, perfect hair, styled quiff, slicked back hair, man bun,
six-pack, gym body, muscular arms, fashion model pose, smoldering gaze,
designer streetwear logos, luxury watch, gold chain, rings, earrings,
rgb rainbow lighting, neon lights, cyberpunk, red-and-black gaming setup,
gaming chair advertisement, energy drink cans, led strip rainbow, esports jersey,
anime, illustration, 3d render, cgi, video game character, game screenshot of real games,
readable code on screen, readable ui text, fake brand logos, unreadable chinese characters,
garbled text, watermark, simplified chinese signage, mainland china street,
japanese street signs, extra fingers, malformed hands, warped game controller,
melted cables, double glasses, contact lens look when glasses are required
```

**為什麼要排除這些(不是隨便列的):**
- `k-pop idol / boy band face / v-shaped jaw / flawless skin` — AI 生「台灣年輕男性」最常滑過去的方向。他是網咖長大、微胖、高度近視的 TA。
- `six-pack / gym body / muscular arms` — 違反 `06 § 六`:他不運動,腰圍多了兩吋。
- `rgb rainbow / neon / red-and-black gaming setup / energy drink` — **這是「玩家」最大的刻板印象,也是他 2025 年「烘焙掉」的東西**(`03 § 8-3`)。違反 `04 § 16`。
- `luxury watch / gold chain / designer streetwear logos` — 違反 `02 § 3` 的房貸與 `02 § 10` 的消費邏輯。
- `readable code on screen / readable ui text / game screenshot of real games` — **NDA 與版權。** 螢幕上只能是模糊的光與色塊,不能有可讀的程式碼、編輯器介面或真實遊戲畫面。
- `simplified chinese signage / mainland china street / japanese street signs` — **場景漂移。他在桃園。** 招牌要是繁體中文,或乾脆不出現文字。
- `warped game controller / melted cables` — 這個人物的畫面一定有手把與線,AI 很容易畫壞。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 范啟維(Chewie) |
| slug | `chi-wei-fan` |
| age_appearance | **30–33**(微胖讓他看起來比實際年齡圓一點,黑眼圈讓他看起來累一點) |
| gender | 男 / he-him |
| ethnicity | 台灣人,父系閩南、母系客家,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 中等偏壯,微胖,肩膀不窄但習慣性前傾,腹部有一點肉。**不是健身身材,也不是瘦宅** |
| location_look | 桃園室內工作者:**膚色偏室內**(不曬),手腕有滑鼠繭,眼鏡壓出的鼻樑印 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **寬臉,兩頰有肉**,下顎線因為微胖有點圓、不銳利 | 反 V 臉。這是他「不像偶像」最重要的特徵 |
| **膚色** | `#D9B896` 中性偏暖的淺小麥色,**偏室內、不曬** | 室內工作,不騎車通勤(機捷) |
| **膚質** | **兩頰有青春期留下的淺痘疤**,T 字部位略油,鼻翼毛孔明顯 | 反美肌。網咖長大的青春期 |
| **鬍子** | 平日刮乾淨但下巴有青色鬍根;**週末兩天沒刮,上唇與下巴有短鬍渣** | 狀態指示器,見下表 |
| **眼睛** | 深棕色,**窄的內雙**,眼型偏細長。**輕微黑眼圈**。看螢幕時會微微瞇 | 高度近視、一點半睡 |
| **眉毛** | 濃、平直、偏粗,**完整,不畫疤、不畫斷眉** | 斷眉是 `persona_tw_06` 的辨識點 |
| **疤** | **右額角、髮際線下方一道約 1 cm 的舊疤,微凹、比膚色淺。眼鏡推到額頭時剛好壓在疤上** | **第一辨識點**(`03 § 1-1`,七歲撞櫃檯桌角) |
| **鼻子** | 鼻樑中等,鼻頭略寬。**鼻樑兩側有眼鏡壓出的淺紅印** | 摘下眼鏡時才看得到 |
| **嘴** | 中等厚度,下唇略厚。**專注時會把下唇往內咬** | 見 3.6 |
| **表情基準** | 不笑的時候看起來很平、有點睏。**一笑會露齒,眼睛直接瞇不見** | 反差是他的親和力來源 |

**鬍子狀態表(寫死):**

| 狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 刮乾淨、有青色鬍根 | 平日上班 | 機捷、公司、週一到週四 |
| 短鬍渣 | 週末、若涵在飛的連續幾天 | 週六日在家、深夜 |
| 明顯鬍渣 + 黑眼圈加深 | 趕工期 | 里程碑前兩週 |

### 3.2 頭髮

- 黑色(`#16130F`),**沒染過**。
- **兩側推短(約 3 mm),頭頂留 4–5 cm,沒有造型,自然塌。**
- **後腦勺被電競椅頭枕壓塌一塊**,下午以後最明顯,他從來不去撥。**頭頂不翹**(翹毛是 `persona_tw_02b` 的辨識點)。
  ← 這條寫死,因為它是「這個人有在剪頭髮但從不整理」的視覺速記。
- 六週剪一次,家附近的快剪。剪完第五週頭頂會蓋到額頭。
- **不要畫成韓系逗號瀏海、不要油頭、不要漸層推剪的精緻版。** 就是快剪。

### 3.3 身體

- **身高 176 cm。體重 74 kg。**
- 肩膀不窄,**習慣性前傾**(打電腦姿勢),坐著時背是圓的。
- **腹部有一點肉**,T 恤會在肚子那裡繃一點。手臂普通,沒有線條。
- 手:**手指偏長,指節普通,指甲剪短。右手腕骨外側有一塊微紅的滑鼠繭。**
  手是這個人物最重要的身體部位之一:**握手把、敲鍵盤、點便利貼**,任何近景都要拍到。
- 腳:在家穿藍白拖,常常一隻腳盤在椅子上,拖鞋掉在地上。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **右額角髮際線下的舊疤。** 任何正臉或右側臉都必須有。**第一辨識點。**
2. **黑色粗方框膠框眼鏡**(見 3.5)。**第二辨識點。**
3. **後腦勺被椅背壓塌的那一塊頭髮。**
4. **右手腕骨的滑鼠繭。** 手部近景時出現。
5. **左手腕的黑色運動手環**(看通知、量睡眠,不是智慧手錶、不是錶)。

### 3.5 眼鏡(狀態指示器)

- **黑色粗方框膠框眼鏡**,近視約 -5.25,**鏡片邊緣明顯有厚度**(高度近視),
  側面看得到鏡片邊的一圈白。正面看,眼睛在鏡片後面會顯得小一點。
- **他幾乎都戴著。** 高度近視的人看近的東西會把眼鏡推上去或拿下來,這是他的招牌動作之一。

| 眼鏡狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 戴著 | 預設狀態 | 90% 的畫面 |
| **推到額頭上,手機拿到離臉十公分** | 看手機上的小字、看測試機 | 機捷、看數字、看留言 |
| 拿在手上,另一隻手揉眼睛 | 累、趕工期 | 深夜、凌晨 |
| 放在鍵盤上方 | 去洗臉、去睡覺前 | 桌面靜物 |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 臉很平,眼睛微瞇看螢幕,下唇微咬 | 70% 的畫面 |
| **counting** | 眼睛往左上,嘴唇無聲在動,手指在桌上點,他在算毫秒 | 工作、看數字 |
| **real smile** | **露齒,眼睛瞇到不見,顴骨往上推,頭微微往後** | 週三團、若涵、遊戲在低階機跑很順 |
| **laugh** | 一聲「哈」,頭往後仰一下,手拍桌子一次 | 週三團 |
| **deadpan** | 眼皮半垂,嘴角不動,看著鏡頭外 | 有人說「上線前會優化」 |
| **genuinely pleased** | 眉毛抬一下,輕輕點頭兩次,嘴角往一邊拉 | 一個東西有顯示內部數字 |
| **exhausted** | 眼鏡拿在手上,拇指跟食指捏鼻樑 | 趕工期、凌晨 |
| **squinting at phone** | **眼鏡推到額頭,手機拿到離臉十公分,眉頭皺起** | 看手機上的數字或留言 |
| **controller dead** | **雙手還握著手把,看著電視,完全靜止三秒** | 手把在 Boss 最後一滴血沒電 |

**❌ 絕對不出現的表情:** 比 YA、對鏡頭眨眼、歪頭、帥氣的側臉凝視、
電競選手式的握拳吶喊、任何韓系或日系的偶像表情、遊戲廣告式的驚訝臉。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中音偏低**,男聲基頻約 **110–125 Hz**。不渾厚、不磁性,就是普通 |
| 語速 | **畫外音約每分鐘 210 字;講到技術會變快,約 260 字** |
| 口音 | **桃園國語,很標準但很平。** 幾乎沒有台語腔。偶爾冒一個客語詞(外婆的「食飽吂」) |
| 音色 | 略悶,鼻音一點點。**深夜錄的會比較低** |
| 語調 | **很平,起伏小。** 講笑話也用平的語調講,笑點在內容不在聲音 |
| 特徵 | 數字講得很清楚:「二點一毫秒」「十六點六」「七十五瓦」 |
| 英文 | 術語直接講英文:shader、profile、frame time、LOD、build,發音偏台式但正確 |
| 笑聲 | 一聲短的「哈」,或鼻子哼一聲 |
| 填充詞 | 「就是說」(多)、「對啊」(多)、「然後」、「欸」(開頭)、「基本上」(講技術時) |
| 情緒起伏 | **低。** 好笑的時候語速變快,累的時候句子變更短 |
| 絕不出現 | 「哈囉大家好」「兄弟們」「各位觀眾」、遊戲實況主式的高亢、電競解說腔、播報腔、中國腔兒化音 |

### 3.8 鏡頭前的肢體習慣

- **用中指把眼鏡往上推。** 一天幾十次,他沒發現。
- **看近的東西會把眼鏡推到額頭,東西拿到臉前面。**
- **講技術時在空中畫圖**:手指在空氣裡畫一條 frame time 的折線,畫到尖峰時停一下。
- **用手指點螢幕上的便利貼。** 講「預算」的時候。
- 坐著時**一隻腳盤在椅子上**,藍白拖掉在地上。
- 手指在桌上用四拍敲。
- **手把沒電時完全靜止三秒,然後笑出來。**
- **他會看鏡頭,但很短,然後看回螢幕或手上的東西。**

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎不拍。** 一個月最多一次,通常是若涵拍的,或在電梯鏡子裡 |
| 出現在畫面裡的方式 | **手、手把、背影、螢幕反光裡的臉、側臉的眼鏡框。** TikTok 露臉約 10% |
| 拍什麼 | **螢幕、便利貼、手把、主機、陽台看出去的球場燈、機捷月台、管理室的包裹** |
| 構圖 | **置中、對稱。** 他喜歡對稱(TA 職業病:檢查畫面時習慣置中比對)。他會吐槽自己 |
| 光線 | **有什麼用什麼**:螢幕光、主機的暖白、窗光。夜景常常偏暗 |
| 後製 | **零。** 他每天在調畫面,自己的照片完全不調 |
| **特殊:拍電視** | **他常用手機直接拍電視上的遊戲畫面,畫面會有摩爾紋。** 他知道可以截圖,他就是懶 |
| 器材 | iPhone。**公司的任何東西都不拍** |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「螢幕、手、手把、便利貼」,臉是配角。**
> 需要臉的時候(TikTok 口播、商業素材)才用完整人像,而且臉要符合第五節的不可變錨。
> **畫面要像一個工程師隨手拍的:置中、對稱、光線很普通、偶爾有摩爾紋。** 這是他的視覺簽名。

---

## 四、服裝系統(五套 + 變體)

外型必須對得起 `02 § 3` 的房貸與 `02 § 10` 的消費行為:
**顯卡跟螢幕可以貴,身上穿的幾乎都是公司發的跟平價的。**

### 4.1 Office Outfit(公司,週一到週四)

```
- 專案或遊戲展的紀念 T 恤(黑色或深灰),胸前圖案小、看不清楚、沒有可讀的字
- 深灰色拉鍊帽 T(公司冷氣很強),袖口有點起毛
- 深藍色直筒牛仔褲
- 灰色慢跑鞋,鞋頭有點髒
- 黑色後背包(公司的活動贈品,logo 已經磨掉)
- 員工識別證掛繩,**識別證翻面或塞進口袋,看不到任何字**
- 黑色運動手環
- 黑色粗框眼鏡
```

### 4.2 Home Outfit(在家,夜間與週末)

```
- **那件停營運手遊的紀念 T 恤**(深藍色,胸前印刷裂開,看不出原本是什麼)
- 灰色運動短褲
- **藍白拖**
- 頭髮完全沒整理,後腦壓塌
- 週末:短鬍渣
- 冬天:外面套一件灰色刷毛帽 T
```

### 4.3 Commute / Rain(通勤、雨天)

```
- 4.1 的內容 + 一件黑色防風外套
- 一把摺疊傘(青埔風大,傘骨歪過)
- 耳朵上 AirPods
- 眼鏡起霧(進冷氣車廂的時候)
```

### 4.4 Visit Outfit(去台中見若涵家、過年)

```
- 深藍色素面襯衫(若涵買的),紮一半
- 卡其色休閒褲
- 白色休閒鞋(只有這種場合穿,所以很新)
- 頭髮剛剪過(他會算好在過年前一週剪)
- 鬍子刮乾淨
```

### 4.5 Ballpark(走路六分鐘的球場)

```
- 灰色素面 T 恤
- 黑色棒球帽(**沒有任何球隊 logo**)
- 運動短褲、藍白拖(是的,他穿藍白拖去看球)
- 手上一個球場便當
```

### 4.6 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 眼鏡 | **黑色粗方框膠框**,鏡片邊緣厚(見 3.5) |
| 手環 | **黑色運動手環**,左手腕。不是智慧手錶 |
| 手機殼 | 黑色矽膠殼,邊角磨白 |
| 背包 | 黑色後背包,公司贈品,logo 磨掉 |
| 耳機 | AirPods Pro 2(外出);在家是無線遊戲耳機(大、黑、耳罩式) |
| 識別證 | **永遠翻面,看不到字** |
| **不戴的** | 戒指、項鍊、耳環、手錶、任何名牌、任何大 logo、任何電競周邊品牌的衣服 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **右額角髮際線下的舊疤**,露臉就要有
2. **黑色粗方框膠框眼鏡,鏡片邊緣有厚度**,換款式等於換人
3. **寬臉、兩頰有肉、窄內雙、下顎不銳利**,不准變 V 臉、不准變大眼
4. **兩側推短、頭頂自然塌、後腦壓塌**,不准造型、不准染
5. **微胖的身形與偏室內的皮膚、兩頰淺痘疤**,不准變健身身材、不准磨皮

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系男團臉 / 偶像 / V 臉 | 違反人物出身,也是 AI 最容易滑過去的方向 |
| 2 | 健身身材、精緻穿搭、名錶 | 違反 `06 § 六` 與 `02 § 3` |
| 3 | **RGB 彩虹燈、霓虹、紅黑電競風** | **他 2025 年烘焙掉了**(`03 § 8-3`),而且這是玩家最大的刻板印象 |
| 4 | 能量飲料、電競椅廣告、電競選手 | 刻板印象 |
| 5 | 帥氣側臉凝視、握拳吶喊 | 圖庫感 + 遊戲廣告感 |
| 6 | 簡體字招牌、中國或日本街景 | **他在桃園**,招牌是繁體 |
| 7 | 乾淨無線的桌面 | **他的桌子一定有線**,而且他不藏 |
| 8 | 螢幕上出現可讀的程式碼、編輯器介面、真實遊戲畫面 | **NDA 與版權** |
| 9 | 出現可辨識的真實品牌 logo、真實遊戲角色、真人臉 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 右額角的疤在嗎(如果露臉);眉毛有沒有被畫出疤或斷眉(不可以)
- [ ] 眼鏡是不是黑色粗方框、鏡片邊有厚度
- [ ] 臉是不是寬臉、下顎不銳利,有沒有被修成 V 臉
- [ ] 頭髮是不是快剪、後腦是不是壓塌(頭頂不翹)
- [ ] 身形是不是微胖,有沒有被修成健身身材
- [ ] 皮膚有沒有被磨皮
- [ ] 燈光有沒有變成 RGB 或霓虹
- [ ] 螢幕上有沒有可讀的文字、程式碼、遊戲畫面
- [ ] 場景是不是台灣(繁體字或無字、新大樓、機捷)
- [ ] 色板有沒有跑掉(`#F2C94C` 是不是只有便利貼那一小塊)
- [ ] 手把有沒有畫壞,線有沒有變形,手指數對不對

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, practical light only, 35mm lens,
mild grain, no retouching, visible skin texture and pores,

a 31-year-old Taiwanese man, 176cm, average build with a slight belly,
shoulders rounded forward from years at a desk, soft arms with no visible muscle definition,
broad face with full cheeks and a soft, rounded jawline that is not sharp,
narrow eyes with a faint inner double eyelid, dark brown, slightly squinting,
mild under-eye shadows, thick straight unbroken eyebrows with no scar,
a small pale old scar about 1cm long on the right side of his forehead just below the hairline, slightly indented,
medium nose bridge with a slightly wide nose tip, faint red marks on both sides of the nose
from glasses, medium lips with a slightly fuller lower lip,
light warm skin tone (#D9B896), faint old acne scars on both cheeks, slightly oily T-zone,
short black hair (#16130F), sides clipped very short, 4-5cm on top falling flat and unstyled,
hair at the back of the head pressed flat from a chair headrest, nothing sticking up at the crown,
thick black square acetate glasses with noticeably thick lens edges,
a black fitness band on the left wrist, a faint reddish mouse callus on the right wrist bone,
long fingers with short-cut nails,

calm, slightly sleepy expression, lower lip slightly tucked in,
looking at a screen or an object, not at the camera,

colour palette: monitor-off black #101418, screen-glow blue #4A6FA5,
baked warm white #F3E9D2, launch-tee navy #2B3A55, new-build grey #6E7681,
with sticky-note yellow #F2C94C only as one small square under 5% of the frame,
no rgb lighting, no neon
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle from his right side so the forehead scar is visible,
wearing a faded navy t-shirt with a cracked, unreadable print on the chest,
sitting at a desk at night, the cool blue glow of a monitor lighting one side of his face,
a soft static warm-white glow from a desktop pc behind him on the other side,
the rest of the room dark, mixed colour temperature,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,客廳,手把,9:16)

```
[MASTER CHARACTER BLOCK]

full body, sitting on a grey fabric sofa in a small new-build Taiwanese apartment living room
at night, leaning forward with elbows on knees, holding a white game controller with both hands,
frozen, staring at a television off-frame, the controller's charging cable lying unplugged
on the sofa beside him, a second black controller on the cushion,
wearing a faded navy t-shirt, grey sports shorts, blue-and-white rubber slippers,
one slipper fallen on the rug, hair unstyled and pressed flat at the back,
light stubble on his upper lip and chin,
lit only by the television glow and one floor lamp,
no readable screen content, no brand logos,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up photograph, monitor glow mixed with a warm-white desk light,
50mm lens, shallow depth of field,

close-up of the bottom-left corner of a black computer monitor bezel,
a slightly crooked yellow square sticky note stuck on it,
hand-written in black marker "16.6" and below it in smaller writing "(33.3)",
a man's hand with long fingers and short nails resting a white game controller
on the desk in front of the monitor, a USB-C cable plugged into the controller,
a faint reddish callus on the wrist bone,
a white multi-port charger with several cables partly visible at the edge of the frame,
the screen itself out of focus and showing only soft blurred colour, no readable content,
no faces, no brand logos,

--ar 1:1
```

### 6.5 Commute / 機捷月台(9:16)

```
[MASTER CHARACTER BLOCK]

standing on an elevated airport metro platform in Taoyuan in the morning,
wide modern concrete platform, glass platform screen doors behind him,
overcast grey sky and new high-rise apartment buildings in the distance,
no readable signage or only out-of-focus traditional Chinese characters,
wearing a charcoal zip hoodie over a black t-shirt, dark jeans, grey running shoes,
a black backpack on one shoulder, AirPods in his ears,
glasses pushed up onto his forehead, holding his phone about ten centimetres from his face,
frowning slightly as he reads, not looking at the camera,

--ar 9:16
```

### 6.6 Desk at night / 桌子 A(4:5)

```
[MASTER CHARACTER BLOCK]

sitting with one leg tucked up on an old black office chair with a worn armrest wrapped in a cut
strip of mousepad, at a black electric standing desk set to sitting height,
in a small study of a new Taiwanese apartment at 1am, wearing a faded navy t-shirt,
two 27-inch monitors, the left one with a small yellow sticky note on the bottom-left bezel,
monitor screens showing only blurred abstract colour, no readable text,
a wired mechanical keyboard, a large desk mat, a wireless gaming headset hanging on a hook
at the desk edge, a white multi-port charger with five or six tangled cables,
two game controllers lying on the desk with cables plugged in,
a mid-tower pc with a glass side panel under the desk glowing a single static warm white,
a white power strip running along the skirting board with all its little red switch lights on,
looking at the screen,

--ar 4:5
```

### 6.7 書房廣角 / 錯的那面牆(16:9)

```
[MASTER CHARACTER BLOCK]

wide shot of a small study room in a new Taiwanese apartment, evening,
on the right a black standing desk against the wall with two monitors and a man sitting at it
seen from behind, a white power strip running along the skirting board from a single wall outlet,
on the opposite wall a wall-mounted air conditioner high up, and below it a tall wooden
bookshelf covering most of the wall, with only one white wall outlet visible at the bottom edge
of the bookshelf, a robot vacuum docked and charging in front of that one outlet,
plain white walls, grey floor tiles, window with evening light on the left,
no brand logos,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in every panel,
head and shoulders, plain grey background, glasses on unless stated:
1 calm and slightly sleepy looking at a screen with lower lip tucked in,
2 counting silently with eyes up and to the left and lips moving,
3 a wide toothy real smile with eyes squeezed nearly shut and head tilted slightly back,
4 a single short laugh with head thrown back,
5 deadpan with half-lowered eyelids,
6 genuinely pleased with eyebrows briefly raised and mouth pulled to one side,
7 exhausted holding his glasses in one hand and pinching the bridge of his nose,
8 glasses pushed up on his forehead, frowning at a phone held ten centimetres from his face,
9 completely frozen, still holding a game controller, staring off-frame,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
he pushes his glasses up with his middle finger every so often without noticing.
to read anything small he pushes his glasses up onto his forehead and brings the phone
close to his face. while explaining something technical he draws a line graph in the air
with one finger and pauses at the spike. when he talks about a budget he taps the yellow
sticky note on the monitor bezel. he sits with one leg tucked up on the chair and a slipper
on the floor. when a controller dies he freezes completely for three seconds, then laughs once.
he glances at the camera only briefly and goes back to the screen or the object.

VOICE: ordinary mid-low male voice, fundamental around 115 Hz, slightly nasal, flat intonation,
standard Taiwanese Mandarin with almost no accent, says numbers very clearly,
technical words in English (shader, profile, frame time), voice-over around 210 Chinese
characters per minute, faster when talking about tech, jokes delivered deadpan,
no streamer energy, no influencer greeting, no esports hype.

CAMERA: handheld phone or locked-off on the desk, 35mm, centred and symmetrical framing,
practical light only, no rgb, screens always blurred with no readable content.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 右額角的疤 | `03 § 1-1` 七歲撞網咖櫃檯桌角 | ✓ |
| 高度近視、粗框眼鏡 | `02 § 8` 每天十幾小時螢幕 | ✓ |
| 微胖、腰圍多兩吋 | `06 § 六` 不運動、泡麵、升降桌沒在升 | ✓ |
| 偏室內膚色 | `06 § 三` 機捷通勤、不騎車 | ✓ |
| 兩頰淺痘疤 | 網咖長大的青春期 | ✓ |
| 右手腕滑鼠繭 | `02 § 9` 每天工作與遊戲 | ✓ |
| 快剪髮型、後腦壓塌 | `04 § 13` 家裡 C 值 35 | ✓ |
| 專案紀念 T 恤、公司贈品背包 | `02 § 3` 錢花在硬體,不花在衣服 | ✓ |
| 那件停營運的 T 恤當睡衣 | `03 § 5-1` | ✓ |
| 藍白拖 | 台灣在家的普遍樣子;`06` | ✓ |
| 運動手環不是智慧手錶 | `02 § 9` 生活科技被推著走 | ✓ |
| 不戴任何飾品 | `02` 全檔沒有裝飾性消費 | ✓ |
| 主機燈是靜態暖白 | `03 § 8-3` 烘焙掉 | ✓ |
| 構圖置中對稱、拍電視有摩爾紋 | `02 § 6` 職業病 + `04 § 4` 家裡什麼都隨便 | ✓ |
| 幾乎不自拍 | `04 § 13` 實體 E 值 30 | ✓ |
| 識別證永遠翻面 | `02 § 17` NDA | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.9 影片提示詞、五個不可變錨。**螢幕永遠模糊、不可讀。**
**Ivy(素材):** 讀 6.1 master block、6.4 手部鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| full_body | *(本輪未生圖)* | | | |
| hands_detail | *(本輪未生圖)* | | | |
| desk_night | *(本輪未生圖)* | | | |
| study_wide | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,Coordinator 指定 seed 表留空。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.1 | 2026-10-20 | 跨人物撞型修正:第一辨識點由左眉尾疤改為右額角髮際線下的疤(左眉尾疤留給 `persona_tw_06`);臉型由長橢圓改為寬臉;頭頂翹毛改為後腦被椅背壓塌(翹毛留給 `persona_tw_02b`) | 主 session 統一 QA:第二批平行生成,十人之間仍有句型、口頭禪、外型辨識點撞在一起 |

*檔案版本:v1.1 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
