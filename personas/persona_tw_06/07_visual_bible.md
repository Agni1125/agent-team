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
character_slug:   yen-chun-kuo
display_name:     郭彥鈞 Kuo Yen-Chun(Jim)

art_style:        photorealistic documentary photography
                  # 不是 CG、不是插畫、不是「型男設計師」形象照。是工地與家裡的照片。
style_reference:  natural-light candid photography, smartphone or 35mm look,
                  mild grain, harsh southern Taiwan daylight outdoors,
                  practical lights indoors (fluorescent tube, warm pendant lamp, laptop glow),
                  no beauty retouching, visible skin texture, sun-tanned East Asian skin rendered true

color_palette:
  - "#9C9A93"   # site concrete grey — 新大樓工地的水泥牆、地坪
  - "#D8C6A5"   # white oak — 白橡大桌、木皮樣本
  - "#4A4E52"   # dark graphite — 旅行車的車色、工作褲、陰影
  - "#E2B227"   # tape-measure yellow — 文公尺捲尺外殼。點綴用,不超過畫面 6%
  - "#6F8A94"   # harbour blue-grey — 週日清晨堤防的海與天
  - "#B8322A"   # lucky-red — 文公尺的紅字、紅色原子筆。**只能是很小的面積**

lighting_default: 室外:台南的強日光,硬影子,中午的頂光也可以;
                  工作室:日光燈加一盞暖色吊燈,窗外的光從玻璃門進來;
                  家裡餐桌:暖色吊燈 + 筆電螢幕的冷光;
                  車內:擋風玻璃的大面積日光。
                  **不用棚燈、不用柔光箱、不用美肌補光、不用電影感的青橘調色。**

aspect_ratios:
  portrait:  4:5     # IG feed、FB
  vertical:  9:16    # 限動、短影音
  square:    1:1
  wide:      16:9    # YouTube、FB 橫圖

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty filter, pale porcelain skin,
k-pop idol, korean male idol makeup, slick pompadour, glossy hair wax, undercut fashion haircut,
sharp v-line jaw, tiny face, six-pack, gym-built physique, bodybuilder arms,
designer suit, luxury watch with diamonds, gold chain, tattoo sleeve, earrings on men,
fashion model pose, hand on chin pose, arms crossed hero pose, smiling at camera like an ad,
black turtleneck architect cliche, minimalist luxury showroom, hotel lobby,
cafe latte art, flat lay with flowers, teal-and-orange grade, cinematic haze,
anime, illustration, 3d render, cgi, doll-like,
fake brand logos, readable brand names on clothing, unreadable chinese characters, garbled text, watermark,
simplified chinese signage, mainland china street, japanese street signs,
extra fingers, malformed hands, warped tape measure, melted cables, floating objects
```

**為什麼要排除這些(不是隨便列的):**
- `slick pompadour / undercut fashion haircut / k-pop idol` — AI 生「亞洲男性設計師」最常滑向的方向。他是台南的工地設計師,頭髮是家庭理髮店剪的。
- `six-pack / gym-built physique` — 他 79 公斤、有肚子、痛風,違反 `06 § 六`。
- `designer suit / black turtleneck architect cliche / minimalist luxury showroom` — 「豪宅設計師」形象漂移,違反 `04 § 16`。他的日常是工地與 polo 衫。
- `luxury watch with diamonds / gold chain / tattoo` — 違反 `02 § 7`。他只有一支手上鍊的素面錶。
- `simplified chinese signage / mainland china street / japanese street signs` — **場景漂移。他在台南。** 招牌是繁體中文,巷子是透天厝。
- `unreadable chinese characters / garbled text` — AI 生中文常常是亂碼,寧可不出現文字。
- `warped tape measure / melted cables` — 這個人物的畫面一定有捲尺與線,AI 很容易畫壞。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 郭彥鈞(Jim) |
| slug | `yen-chun-kuo` |
| age_appearance | **40–43**(曬黑、鬢角白、眼尾紋,看起來比實際年齡多一兩歲,不顯老態) |
| gender | 男 / he-him |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系偶像** |
| build_class | 中等偏壯。肩寬,微凸的肚子,前臂粗,手大 |
| location_look | 南部開車跑工地的人:**左前臂比右前臂黑一階**(開車靠窗那隻),後頸曬紅,手背有細小的刮痕 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **偏長的方臉**,顴骨略寬,下顎方但不尖 | 反 V 臉。最重要的「不像形象照」特徵 |
| **膚色** | `#B98A63` 曬過的小麥偏深,**額頭與鼻樑更深一點**,T 字部位有油光 | 工地日曬、開車 |
| **膚質** | **毛孔明顯,鼻翼有點紅,兩頰有幾個淡的舊痘疤** | 反美肌 |
| **眼睛** | 深棕色,**外雙眼皮但褶很窄**,眼型偏長,**眼尾有三四條細紋**,眼白在晚上會有血絲 | 四十歲、睡五小時多 |
| **眉毛** | 濃、平、偏直。**左眉尾有一小段約 4 公釐的斷眉**(15 歲在安平堤防的消波塊上滑倒,縫了三針) | **第一辨識點** |
| **鼻子** | 鼻樑中等,鼻翼略寬,鼻頭圓 | |
| **嘴** | 唇形中等偏厚,嘴角自然往下一點點,**不笑的時候看起來在想事情** | 見 3.6 |
| **鬍子** | **兩天沒刮的短鬍渣**,下巴與兩頰,夾著幾根白的 | 他兩天刮一次 |
| **皺紋** | 額頭兩道淺抬頭紋,法令紋開始出現 | 他常挑眉看圖 |

### 3.2 頭髮

- 黑色(`#1E1C1A`),**鬢角與耳上約一成五是白髮**,頭頂還是黑的。不染。
- **兩側推短(約 3 公釐),頂部約 4–5 公分,往右邊隨手撥。** 東區家庭理髮店,四週剪一次,NT$250。
- 額頭髮線**微微後退**,兩邊的 M 字角比 30 歲時深。
- 工地戴安全帽之後頭頂會壓扁,**他不整理**。
- 狀態指示(寫死):

| 頭髮怎麼樣 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 頂部被安全帽壓扁、額頭有一道帽緣壓痕 | 剛從工地出來 | 工地、車上午餐 |
| 隨手撥到右邊,有點亂 | 日常、工作室 | 工作室、建材行 |
| 用水抓過、比較整齊 | 屋主簡報、見客戶 | 簡報、驗收 |
| 洗完澡,半乾往後撥 | 晚上在家 | 餐桌、深夜 |

### 3.3 身體

- **身高 175 cm。體重 79 kg。腰圍 92 cm。**
- 肩寬,背有一點駝(看圖、開車),**肚子微凸**,polo 衫紮進褲子時看得出來。
- **前臂粗,手大。** 指節粗,指甲剪很短,**手背有工地刮痕**,指甲縫偶爾有洗不掉的灰。
- **左手食指第二節一道約 1.5 公分的白色舊疤**(大學木工課的鑿刀滑進扶料的手,縫了五針)。
- **手是這個人物最重要的身體部位,任何近景都要拍到。**
- 右腳大拇趾關節略腫(痛風之後),**不需要特別畫,但他穿涼鞋時看得到。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **左眉尾的斷眉。** 正臉或左側臉必須有。**第一辨識點。**
2. **左耳的黑色單耳藍牙耳機。** 工地、開車、建材行的畫面出現機率 80%。在家不戴。
3. **左手食指的白色舊疤。** 手部近景必須有。
4. **左前臂比右前臂黑。** 穿短袖的畫面要看得出來。
5. **左手腕的手上鍊錶**(白色錶盤、細黑針、舊的咖啡色皮錶帶),錶帶下有一圈白色曬痕。

### 3.5 眼鏡(狀態指示器)

- **平常不戴眼鏡。** 近視很輕,不影響。
- **一副 +1.00 的老花眼鏡**(細的霧黑色金屬框,方形),放在車上遮陽板夾層。
  **他只在車上一個人看施工圖時戴。** 在屋主、師傅、員工面前,他用 iPad 放大。

| 眼鏡狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 沒戴 | 99% 的畫面 | 全部 |
| 車上一個人戴著老花,看 iPad | **他不想被看到的樣子** | 極少,只能是背影或車內側拍,一年一兩次 |
| 老花眼鏡夾在遮陽板 | 物件鏡頭 | 「眼睛開始差兩分」的內容 |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 嘴角平、眉頭微收,眼睛看著物件或牆角,像在算尺寸 | 70% 的畫面 |
| **inspecting** | 微微低頭,眼睛瞇一點,下巴往內收,**看捲尺上的刻度** | 工地、驗收 |
| **real smile** | **嘴角往兩邊拉,不太露齒,眼尾紋全部出來。** 他真正的笑,很短 | 長輩屋主在粉筆線裡走完一圈、兒子吐槽他 |
| **laugh** | 頭往後仰一點,一聲短的「哈」,手拍一下大腿 | 跟阿輝師、阿翰 |
| **deadpan** | 眼皮半垂,嘴角不動,眉毛一邊微抬 | 屋主說「我要高級感」 |
| **genuinely pleased** | 眉毛抬高,嘴巴往下撇著點頭(南部男人的「不錯喔」) | 一個東西量起來跟標示的一模一樣 |
| **tired** | 一手捏鼻樑,眼睛閉著,另一手還握著紅筆 | 晚上十一點的餐桌 |
| **listening** | 頭微側,左耳朝前(耳機那邊),眼睛看地上 | 講電話、聽師傅解釋 |
| **knocking** | **一手指節敲在物體表面,頭側過去聽** | 招牌動作,判斷材質 |

**❌ 絕對不出現的表情:** 比讚對鏡頭、雙手抱胸的英雄姿勢、手托下巴的形象照、
對鏡頭露齒微笑的廣告笑、任何韓系或日系偶像的表情、「設計師凝視遠方」。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **低,基頻約 110–125 Hz。** 有一點鼻腔共鳴 |
| 語速 | **畫外音約每分鐘 170 字;工地講話約 210 字;講台語時更快。** |
| 口音 | **台南腔國語,台語母語級。** 國語的尾音會帶「啦」「喔」「嘛」,不刻意 |
| 音色 | 略沙、偏乾,是在工地隔著電鑽聲喊話喊出來的。**他不抽菸,不要做成菸嗓** |
| 特徵 | **句子完整,常先講結論。** 「先講結論,這個不行。」數字一定精確到公釐或分 |
| 台語 | 自然混入:「差兩分爾爾」「嘛是可以」「歹勢」「足熱」「好啦」。**不當笑點,是工地的語言** |
| 笑聲 | 一聲短的「哈」,或鼻子出氣的「哼」 |
| 填充詞 | 「嗯」(思考,多)、「其實」(多)、「講白一點」(中)、「對啦」(句尾) |
| 情緒起伏 | **低到中。** 講長輩的家的時候語速變慢,講尺寸的時候變快 |
| 絕不出現 | 「哈囉大家好我是設計師」「今天要跟大家分享」「家人們」、播報腔、業務腔、中國腔兒化音 |

### 3.8 鏡頭前的肢體習慣

- **拿到任何東西,第一個動作是用右手食指的指節敲一下,頭側過去聽。** 然後拿捲尺量。
- **用右手食指的指節敲。** 敲桌面、敲牆、敲一個產品的外殼,頭側過去聽。
- **蹲下來看踢腳板。** 進任何房間都會蹲一次,膝蓋會響。
- **拉文公尺捲尺:** 左手拇指壓住頭,右手拉,「唰」;量完用拇指按鈕,讓它捲回去,卡一下,他用手指推一下。
- 講尺寸的時候,**用拇指與食指比出寬度**:「三公釐,大概這樣。」
- 手指**順著牆面的縫畫過去**,像爸爸看九二一的裂縫。
- 講電話時**左手扶著左耳的耳機**,右手在空中比劃。
- **他看鏡頭的時間很短,然後看回物件或牆。** 他不習慣被拍。

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎沒有。** FB 一年有兩三張家族合照,是太太拍的 |
| 出現在畫面裡的方式 | **手、手臂、背影、蹲著的側影(左側,耳機那邊)、安全帽的頭頂。** 短影音露臉 ≤5% |
| 拍什麼 | **牆角、插座、天花板、捲尺貼在牆上的刻度、工地、週日的海平線。** |
| 構圖 | **很「施工照」**:正對牆面、水平拉直、物件在中間,有時候手指入鏡指著問題點 |
| 光線 | 有什麼光用什麼光。工地的日光燈、正午的太陽 |
| 後製 | **零。** 但他會用手寫筆在照片上畫紅圈(給師傅看的習慣),有時候直接把這種照片發出去 |
| 海平線照片 | **唯一例外:** 週日清晨在堤防,海平線一定拉到完全水平,畫面一半是天一半是海,很像施工圖 |
| 器材 | 手機。**他沒有相機。** 工作室的完工照是小葳與外聘攝影師拍的 |

> **這一條對 Libai 與 Ivy 是硬約束:這個人物的視覺主體是「手、尺、牆角、工地」,臉幾乎不出現。**
> 需要臉的時候(商業素材),臉要符合第五節的不可變錨。
> **他拍的照片像施工紀錄,不像作品集。** 週日的海平線是唯一的例外,但那也是水平拉直的。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**每天碰、留很久的東西可以貴(錶、椅子、鞋),身上穿的大多是太太買的、工作室訂的。**

### 4.1 Site Outfit(工地,70% 的畫面)

```
- 深藍色 polo 衫,左胸一個小小的白色刺繡「線寬」(工作室訂了二十件,太太訂的)
- 卡其色工作褲,寬直筒,膝蓋有水泥灰,右邊口袋夾著文公尺捲尺
- 黑色防滑工作鞋(痛風之後買的好走那雙,NT$4,800)
- 左耳:黑色單耳藍牙耳機
- 左手腕:手上鍊錶
- 工地現場:白色安全帽(帽沿貼著「線寬」小貼紙)
- polo 衫領口插著一支紅色原子筆
← polo 衫是他的工作服,一週穿五天,不同的件
```

### 4.2 Presentation Outfit(屋主簡報、驗收)

```
- 白色或淺藍色牛津布襯衫,袖子捲兩折到前臂中段
- 深灰色西裝褲(不成套)
- 深咖啡色綁帶皮鞋(結婚那年買的,換過兩次鞋底)
- 手上鍊錶
- 耳機拿下來放口袋
- 頭髮用水抓過
- 文公尺捲尺:**還是在褲子口袋**,西裝褲口袋被撐出一個方形
```

### 4.3 Sunday Outfit(週日清晨堤防、回永康)

```
- 洗到變軟的灰色素 T(沒有字),外面一件深藍色防風薄外套(清晨海風)
- 深藍色短褲,到膝上
- **一雙黑色防滑溯溪鞋**(鞋底有齒。爸爸 2001 年那句「下次穿有齒的鞋」)
- 一頂沒有 logo 的深藍色舊棒球帽
- 天亮前額頭上一支 USB-C 頭燈
- 一個軍綠色帆布斜背包(手機、一包面紙、一瓶無糖茶、一盒蝦)
- 兩支釣竿、一個白色保冷箱(大部分時候是空的)
- 沒有耳機,沒有捲尺(**這是他唯一不帶捲尺的時候**)
- 手上鍊錶
- 十點回永康時換回皮革涼鞋
```

### 4.4 Home Outfit(晚上的餐桌)

```
- 一件大學系上的舊 T 恤(深灰,胸前的字已經洗掉一半,看不出寫什麼)
- 運動短褲
- 室內拖鞋
- 洗完澡,頭髮半乾往後撥
- 錶拿下來放在餐桌上
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **手上鍊的包浩斯風格素面錶**(白色錶盤、細黑針、無日期窗),舊的咖啡色皮錶帶。不是智慧錶,不是潛水錶 |
| 捲尺 | **黃色外殼 7.5 公尺文公尺**,白色油漆筆「郭」字,外殼一個凹痕 |
| 耳機 | 黑色單耳藍牙耳機,左耳 |
| 筆 | 紅色原子筆,插在領口或襯衫口袋 |
| 婚戒 | **素面白金戒,左手無名指**。工地也不拿下來,上面全是刮痕 |
| 背包 | 一個深灰色的電腦後背包(裝筆電與那顆 240W 變壓器),拉鍊頭換過 |
| 手機殼 | 黑色矽膠殼,邊角磨白,**手寫筆插在機身裡** |
| **不戴的** | 項鍊、手鍊、耳環、名牌包、皮帶大 logo、太陽眼鏡掛領口(他開車戴的太陽眼鏡收在車上) |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **左眉尾的斷眉**,露臉就要有
2. **偏長的方臉、窄外雙、眼尾細紋、兩天的鬍渣(夾白)**,不准變 V 臉、不准刮乾淨變小鮮肉
3. **兩側推短、鬢角一成五白髮、額頭髮線微退**,不准染、不准油頭、不准變長髮
4. **曬黑的皮膚,左前臂比右前臂黑**,不准磨皮、不准美白
5. **右邊褲子口袋的黃色文公尺捲尺**(工地與簡報畫面),換成別的捲尺等於換人

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系男神 / 油頭型男 / V 臉 | 違反人物出身與職業,也是 AI 最容易滑過去的方向 |
| 2 | 健身體態、六塊肌、緊身 T | 違反 `06 § 六`,他有肚子、痛風 |
| 3 | 豪宅設計師:黑高領、西裝、精品家具展示間 | 他離開台北就是離開這個 |
| 4 | 白皙、柔焦、美肌 | 他曬黑,毛孔明顯 |
| 5 | 對鏡頭比讚、雙手抱胸、手托下巴 | 形象照感 |
| 6 | 簡體字招牌、中國或日本街景 | **他在台南**,透天厝、騎樓、繁體字 |
| 7 | 乾淨無線的極簡桌面 | **他的白橡大桌一定看得到那個彈跳插座,桌下一定有那顆變壓器** |
| 8 | 大量正臉 | 他的帳號主體是手、尺、牆角、工地 |
| 9 | 出現可辨識的真實品牌 logo 或真人臉 | 法遵 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 左眉尾的斷眉在嗎(如果露臉)
- [ ] 臉是不是偏長方臉、窄外雙、有鬍渣,有沒有被修成 V 臉小鮮肉
- [ ] 鬢角有沒有白髮,髮型是不是兩側推短、不是油頭
- [ ] 皮膚有沒有被磨皮或美白,左前臂是不是比較黑
- [ ] 文公尺捲尺是不是黃色外殼、在右邊口袋
- [ ] 耳機是不是在左耳
- [ ] 錶是不是素面手上鍊,不是智慧錶
- [ ] 場景是不是台灣南部(繁體字、透天厝、騎樓、新大樓工地)
- [ ] 手有沒有畫壞,捲尺刻度有沒有變形,左手食指的疤在不在
- [ ] 有沒有出現亂碼中文、假 logo

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, natural or practical light only, 35mm lens,
mild grain, no retouching, visible skin texture and pores,

a 40-year-old Taiwanese man, 175cm, medium-heavy build, broad shoulders,
a slight belly, thick forearms, large hands with short nails and small scratches,
a 1.5cm pale old scar on the middle knuckle of his LEFT index finger,
a long squarish face with slightly wide cheekbones and a square but not sharp jaw,
narrow natural double eyelids, dark brown eyes, three or four fine lines at the outer corners,
thick straight eyebrows with a small 4mm gap near the end of the LEFT eyebrow,
medium nose bridge with slightly wide nostrils, medium-full lips resting slightly downturned,
two-day stubble on chin and cheeks with a few grey hairs,
sun-tanned skin (#B98A63), darker on forehead and nose, visible pores, slight shine on the T-zone,
his LEFT forearm visibly more tanned than his right,
short black hair (#1E1C1A), sides clipped to about 3mm, 4-5cm on top pushed casually to the right,
about fifteen percent grey at the temples, slightly receding hairline at the corners,
a black single-ear bluetooth headset in his LEFT ear,
a plain hand-wound watch with a white dial and thin black hands on a worn brown leather strap, left wrist,
a plain scratched white-gold wedding band on his left ring finger,

calm focused expression, mouth neutral, brows slightly drawn,
looking at an object or a wall corner, not at the camera,

colour palette: site concrete grey #9C9A93, white oak #D8C6A5, dark graphite #4A4E52,
harbour blue-grey #6F8A94, with tape-measure yellow #E2B227 under 6% of the frame
and only tiny touches of lucky red #B8322A
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter view from his LEFT side so the headset and the eyebrow gap are visible,
navy blue polo shirt with a tiny white embroidered mark on the left chest (no readable text),
a red ballpoint pen clipped at the collar,
standing inside an unfinished new apartment in southern Taiwan, bare concrete walls,
electrical boxes without cover plates, harsh daylight from a window,
hair slightly flattened on top from a safety helmet with a faint line on his forehead,
shallow depth of field f/2.8, subject slightly off-centre,

--ar 4:5
```

### 6.3 Full body(全身,工地,9:16)

```
[MASTER CHARACTER BLOCK]

full body, crouching on one knee in a newly built apartment, checking the skirting board joint,
navy polo shirt tucked into wide khaki work trousers with concrete dust on the knees,
black non-slip work shoes, a yellow-cased tape measure clipped to his right trouser pocket,
a white safety helmet resting on the floor next to him,
bare concrete floor partly covered with protective board, masking tape on door frames,
daylight from a large window, slightly overexposed background,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up photograph, harsh natural daylight, 50mm lens, shallow depth of field,

close-up of a man's large tanned hands with short nails, small scratches and a pale old scar
on the left index finger knuckle, pulling out a yellow-cased tape measure whose blade shows
alternating red and black traditional Taiwanese auspicious markings beside the centimetre scale
(markings rendered as abstract red and black blocks, no readable characters),
the casing has a small dent and a hand-painted white character mark (abstract, unreadable),
his left thumb pressing the blade against a door frame of an unfinished apartment,
no faces, no brand logos,

--ar 1:1
```

### 6.5 Desk A / 工作室白橡大桌(16:9)

```
photorealistic documentary photograph, mixed fluorescent and warm pendant light, 35mm lens,

a long solid white oak table (about 280cm) in a small design studio on the ground floor of an
old Taiwanese townhouse, worn 1980s beige 30x30 floor tiles with three replaced tiles of a slightly different shade,
in the centre of the table a small pop-up power socket with two USB-A ports,
one of the USB-A ports plugged with a tiny hand-cut white oak wooden plug,
a laptop, an iPad-sized tablet with a stylus, A3 construction drawings with red pen marks,
a wooden tray of tile and wood veneer samples,
a small white charger partly hidden behind a standing veneer sample book,
on the white wall behind: an old 90cm wooden T-square hung horizontally with faded markings,
and below it a small framed sheet of hand-drawn straight ink lines,
no people, no readable text, no brand logos,

--ar 16:9
```

### 6.6 Desk B / 家裡餐桌,深夜(4:5)

```
[MASTER CHARACTER BLOCK]

sitting at a walnut dining table at 11pm in a modest 2001-built apartment in Tainan,
glossy beige 60x60 porcelain floor tiles, a warm pendant lamp above,
wearing a faded dark grey old university t-shirt with the print half washed away (unreadable),
hair half-dry pushed back, no headset, his watch taken off and lying on the table,
a 16-inch laptop, a large black laptop power brick on the floor under the table,
a white three-outlet power strip on the floor with a cable running under a rug to the sideboard,
a round woven bamboo basket on the sideboard with chargers and cables,
pinching the bridge of his nose with one hand, a red pen in the other,
the cool laptop glow on his face and warm pendant light from above,

--ar 4:5
```

### 6.7 Car / 旅行車午餐(16:9)

```
[MASTER CHARACTER BLOCK]

inside a dark graphite 2019 station wagon parked at a Taiwanese convenience store car park at noon,
seen from the passenger side, he sits in the driver seat eating a boxed lunch,
phone mounted on the air vent showing a messaging app (no readable text),
a cheap two-port charger in the 12V socket with a cable to the phone,
harsh midday sun through the windscreen, sunshade visor folded down with a parking card tucked in,
cargo area behind shows a grey tool case of tile samples and a white safety helmet,

--ar 16:9
```

### 6.8 Sunday / 堤防(4:5)

```
[MASTER CHARACTER BLOCK]

5:50am on a concrete breakwater near Anping, Tainan, before sunrise, blue hour turning pale,
he sits on a concrete tetrapod edge in a grey plain t-shirt under a navy windbreaker,
navy shorts, black non-slip water shoes, a plain navy cap with no logo,
a small LED headlamp pushed up on the cap, no headset, no tape measure,
two fishing rods leaning on a railing, a white cooler box next to him, lid open and empty,
holding his phone perfectly level to photograph the horizon,
the sea and sky split exactly in half, a few other lone fishermen far away,
seen from behind and slightly to his left,

--ar 4:5
```

### 6.9 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in every panel,
head and shoulders, plain off-white wall background, navy polo shirt, headset in left ear:
1 calm focused with mouth neutral, 2 inspecting with chin tucked and eyes narrowed,
3 a short closed-mouth real smile with all the eye-corner lines showing,
4 a short laugh with head tipped back slightly, 5 deadpan with half-lowered lids and one brow raised,
6 genuinely pleased, eyebrows raised and mouth pulled down while nodding,
7 tired, pinching the bridge of his nose with eyes closed,
8 listening with head tilted and left ear forward, eyes on the floor,
9 knocking on a surface with his right index knuckle, head turned to listen,

--ar 1:1
```

### 6.10 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
when he picks up any object he first knocks on it with his right index knuckle and tilts his head to listen,
then measures it with the yellow tape measure.
when he enters a room he crouches once to look at the skirting board joint; his knee clicks.
he pulls the yellow tape measure with his left thumb holding the end, a sharp "shhk" sound,
then lets it retract, it catches once and he pushes it with a finger.
when talking about a size he shows the width between thumb and index finger.
on the phone he holds the left-ear headset with his left hand and gestures with the right.
he glances at the camera only briefly and returns his eyes to the wall or the object.

VOICE: low male voice, fundamental around 115 Hz, dry and slightly rough from calling across job sites,
Tainan-accented Mandarin with natural Taiwanese Hokkien words mixed in, complete sentences,
often starts with the conclusion, voice-over around 170 Chinese characters per minute,
no influencer greeting, no sales tone, no broadcast energy.

CAMERA: handheld phone or locked-off on a small tripod, 35mm, eye level or crouched low at skirting height,
practical light only. face appears in under 5% of the frames; hands, tape measure, wall corners and job sites are the subject.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 曬黑、左前臂較黑 | `06 § 三` 一天開車兩三小時、跑工地 | ✓ |
| 鬢角白、眼尾紋 | `02 § 1` 四十歲 | ✓ |
| 微凸的肚子、79 公斤 | `06 § 五` 牛肉湯、車上便當;`06 § 六` | ✓ |
| 兩天的鬍渣 | `06 § 四` 06:15 起床、07:10 送小孩 | ✓ |
| 左手食指的疤 | `03 § 3-1` 大學木工課 | ✓ |
| 左眉尾斷眉 | `03 § 2-2` 安平堤防的消波塊 | ✓ |
| 文公尺捲尺 | `01 § 二`、`04 § 15` | ✓ |
| 單耳藍牙耳機(micro-USB) | `02 § 9`、`06 § 三` | ✓ |
| polo 衫是工作室訂的 | `05 § 3` 太太管行政 | ✓ |
| 手上鍊錶,不是智慧錶 | `02 § 7` 願意為設計付錢、`02 § 9` 不戴智慧錶 | ✓ |
| 老花眼鏡藏在車上 | `03 § 八`、`04 § 0` 衍生矛盾 #5 | ✓ |
| 家庭理髮,四週一次 | `02 § 7` 小錢很南部 | ✓ |
| 幾乎不自拍、拍照像施工紀錄 | `04 § 13` 私下 E 值 40、`02 § 6` 職業反射 | ✓ |
| 海平線照片也拉水平 | `02 § 11` 嗜好 #1、`02 § 6` 職業反射 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.10 影片提示詞、五個不可變錨。**露臉 ≤5%,手與捲尺是主角。**
**Ivy(素材):** 讀 6.1 master block、6.4 手部鏡頭、6.5 白橡大桌、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**他的身分是「設計師」,商業素材上的風險比一般使用者人物更高(專家薦證)。**
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| full_body | *(本輪未生圖)* | | | |
| hands_detail | *(本輪未生圖)* | | | |
| desk_a_studio | *(本輪未生圖)* | | | |
| desk_b_dining | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,不是圖(與 Nathan、沛璇相同)。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.1 | 2026-10-20 | 跨人物撞型修正:大學木工課的鑿刀疤由右手食指改到左手食指(鑿刀滑進扶料的那隻手;右手食指指節的疤是 `persona_tw_035` 的手部辨識點);事件本身不變 | 主 session 統一 QA:第二批平行生成,手部辨識點與 `035` 落在同一根手指同一節 |

*檔案版本:v1.1 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
