# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人,而且是一個有兩個小孩、每天開會的 37 歲台灣男人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   shu-wei-hsu
display_name:     許書維 Hsu Shu-Wei(Shawn)

art_style:        photorealistic documentary photography
                  # 照片。不是型男雜誌、不是商業形象照、不是圖庫的「幸福家庭」。
style_reference:  candid smartphone or 35mm look, available light only
                  (desk lamp, monitor, office fluorescent, car dashboard, overcast window),
                  mild grain, moderate depth of field (f/2.8–f/5.6),
                  no beauty retouching, visible skin texture, East Asian skin rendered true,
                  slightly tired, ordinary middle-class Taiwanese setting

color_palette:
  - "#2B2F33"   # graphite — 車內、筆電、夜裡的房間
  - "#E6E3DC"   # IKEA white — 家裡的白色桌板與牆
  - "#8A9199"   # office partition grey — 公司隔板、地下室水泥柱
  - "#D9A066"   # 3000K desk lamp — 22:30 之後書桌的暖光,點綴,不超過畫面 10%
  - "#3E6FB0"   # bead blue — 珠珠吊飾的藍色繩子與珠子。**只能是小面積,不超過 5%**
  - "#F2D04B"   # post-it yellow — 「平板睡覺的地方」那張便利貼。**只能是一個小點**

lighting_default: available light only.
                  公司:天花板日光燈 + 螢幕;
                  家裡白天:窗光(陰天居多);
                  家裡夜間:一盞暖色檯燈 + 螢幕冷光的混色;
                  車內:儀表板與中控螢幕的光,地下室日光燈從擋風玻璃進來。
                  **不用環形燈、不用棚燈、不用逆光剪影的勵志感、不用暖色濾鏡的「爸爸好溫暖」。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok、Reels
  square:    1:1
  wide:      16:9

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty filter, k-pop idol, korean oppa hairstyle,
two-block perm, dyed hair, male model, chiseled jawline, six-pack, gym physique,
muscular arms, tight shirt, suit and tie, luxury watch, gold chain, designer bag,
influencer pose, thumbs up, peace sign, smiling at camera like stock photo,
happy family stock photo, golden hour backlight, warm nostalgic filter,
teal-and-orange grade, studio lighting, ring light catchlight,
rgb gaming desk, led strip lighting, minimalist perfect desk setup, cable-free desk,
visible children's faces, child face, kid looking at camera,
company logo, brand logo, id badge, lanyard, readable text, garbled text,
unreadable chinese characters, simplified chinese signage, mainland china street,
japanese street signs, tesla interior, sports car,
anime, illustration, 3d render, cgi, extra fingers, malformed hands,
warped cables, melted plastic, distorted glasses frames
```

**為什麼要排除這些(不是隨便列的):**
- `k-pop idol / korean oppa hairstyle / two-block perm / male model / chiseled jawline`:AI 生「東亞男性」最常滑過去的方向。他是 37 歲、兩個小孩的 PM,頭髮是 NT$250 快剪。
- `six-pack / gym physique / tight shirt`:他有輕度脂肪肝,慢跑一週 0.6 次。違反 `06 § 六`。
- `suit and tie / luxury watch / designer bag`:他的公司不穿西裝;他的錶是智慧手錶;違反 `02 § 3` 的「每一筆都要排順位」。
- `happy family stock photo / golden hour backlight / warm nostalgic filter`:**「暖爸」漂移**,違反 `04 § 16`。
- `rgb gaming desk / minimalist perfect desk setup / cable-free desk`:他的桌子是 120 公分的 IKEA,晚上是平板睡覺的地方。
- `visible children's faces / child face`:**硬規則。** 小孩只能是背影、手、腳、遠處模糊的身影。
- `company logo / id badge / lanyard`:公司不具名;他上班不掛識別證,門禁扣在鑰匙圈上。
- `tesla interior / sports car`:他開的是 2020 年款日系七人座 MPV(汽油),不是電動車。
- `distorted glasses frames`:眼鏡是不可變錨之一,AI 很容易把方框畫歪。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 許書維(Shawn) |
| slug | `shu-wei-hsu` |
| age_appearance | **36–40**(鬢角白髮與晚上的鬍渣讓他看起來比實際年齡累一點) |
| gender | 男 / he-him |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 中等身高,**微胖。** 肩膀圓、小腹微凸,不是運動身材,也不是胖 |
| location_look | 雙北都會、開車通勤、坐辦公室的人:**膚色不黑**,左手臂比右手臂深一點(開車時左手靠窗) |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **長方臉,下顎寬而平**,兩頰有一點肉,下巴不尖 | 反型男。這是他最重要的「普通」特徵 |
| **膚色** | `#D2AE8C` 偏黃的中間膚色,**不白**。額頭與鼻翼略油,傍晚會更油 | 辦公室與車內的人,台灣濕熱 |
| **膚質** | **有毛孔,兩頰有幾顆淡淡的舊痘疤。** 眼下略浮 | 反美肌。`06 § 六` 的睡眠 |
| **眼睛** | 深棕色,**窄的外雙眼皮**,眼型偏長、眼尾平。**眼下有淡淡的細紋與浮腫** | 37 歲、睡 6 小時 50 分 |
| **眉毛與眉心** | 濃、平、偏直,眉頭靠得近。**眉心有一道淺淺的直紋**(長年開會皺眉,不皺眉的時候也看得到) | **第一辨識點**,來源 `04 § 9`(會議上的他)、`06 § 四` |
| **鼻子** | 鼻樑中等,鼻頭略寬 | |
| **嘴** | 唇形中等,上唇薄、下唇略厚。**不笑的時候嘴角平,看起來像在聽人報告** | 見 3.6 |
| **鬍子** | 早上刮乾淨;**傍晚到晚上下巴與上唇有一層青色的鬍渣** | 時間指示器,見 3.2 |
| **表情基準** | **專注時眉頭微微往中間,嘴巴閉著。** 在會議上會點頭,幅度很小 | |

### 3.2 頭髮

- 黑色(`#1A1918`),**鬢角兩側各有幾根白髮**(約 10–15 根,不是一片),頭頂沒有。不染。
- **兩側推短(約 6mm),頂部約 4 cm,自然往右邊分。** 樓下的快剪,NT$250,五週剪一次。
- 不抓髮蠟。**早上出門時頂部是整齊的,下午會塌下來,晚上會因為他一直用手抓而有點亂。**
- 狀態指示(寫死):

| 頭髮與鬍子 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 頂部整齊、沒有鬍渣 | 早上 07:00–09:00 | 校門口、早餐、出門 |
| 頂部塌、輕微鬍渣 | 公司、下午 | 開會、午餐、汐止 |
| **頂部亂(被手抓過)、明顯鬍渣** | **晚上 19:00 之後** | **B3 車內、21:00 收平板、22:30 書桌** |
| 週末:頂部扁(戴過帽子) | 週六 | 游泳課等候區、公園 |

### 3.3 身體

- **身高 172 cm。體重 78 kg。** 2018 年是 70 kg。
- 肩膀圓、略前傾(開會與開車)。**小腹微凸**,穿 polo 衫時看得出來,坐下時更明顯。
- 手臂普通,沒有肌肉線條。**左前臂比右前臂深一階**(開車靠窗)。
- 手:**中等大小,手指偏粗,指甲剪短。左手無名指一枚素面白 K 婚戒**(沒有鑽,婚戒在指根壓出一道淺痕)。
  **右手拇指與食指的指腹會不自覺地互相搓**(轉珠珠星星的習慣,手上沒東西時也會做)。
- 腿:普通。週末穿短褲時可以看到膝蓋上一道小時候騎腳踏車摔的疤(不重要,可省略)。

### 3.4 標誌性特徵(Distinguishing Marks)

1. **眉心一道淺淺的直紋。** 任何正臉都必須有。**第一辨識點。**
1b. **右手虎口一道一公分的白色細疤**(1998 年書桌底下的鐵片)。任何手部近景都必須有。
2. **深灰色霧面方框眼鏡**(TR90 材質,鏡框不粗不細),見 3.5。
3. **左手無名指的素面婚戒。**
4. **左手腕的黑色智慧手錶**(運動錶帶),錶面朝內(他開會時翻手腕看時間)。**不露品牌。**
5. **車鑰匙上的珠珠吊飾**(藍色繩子、六顆塑膠珠、一顆黃色星星,一顆藍珠裂過)。**主錨點**,見 `04 § 15`。

### 3.5 眼鏡(永遠戴著)

- **深灰色霧面方框眼鏡,TR90,鏡腳是同色。** 近視約 -4.25,鏡片有一點螢幕的反光。
- **他沒有隱形眼鏡,也不戴太陽眼鏡(開車時用車上的遮陽板)。** 所有畫面都戴這副。
- 狀態:

| 眼鏡狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 正常戴著 | 平常 | 幾乎所有畫面 |
| **推到額頭上** | 累了,用手捏鼻樑 | B3 車內、22:30 書桌 |
| 拿在手上擦 | 想事情、或在等某個人說完 | 會議 |
| 摘下來放在桌上 | 要睡了 | 23:40 書桌的最後一個畫面 |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 專注,眉頭微微往中間,嘴閉著,看螢幕或物件 | 70% 的畫面 |
| **listening** | 頭微微偏右,小幅度點頭,嘴角平 | 會議、太太講話時 |
| **real smile** | **嘴角往上但嘴巴閉著,眼睛變細,鼻子出一口氣。** 這是他真正的笑 | 小孩、阿周、一個好的產品頁 |
| **laugh** | 低頭、肩膀抖一下、手摸後腦 | 爸爸那句「所以就是不會修」 |
| **deadpan** | 眼皮半垂,完全不動 | 業務說「使用者會習慣的」 |
| **pleased** | 眉毛抬高一下,嘴巴微開「喔」 | 看到產品頁寫「不適合:___ 的人」 |
| **tired** | **眼鏡推到額頭,拇指與食指捏鼻樑,頭靠在車椅頭枕上** | B3 熄火後、DVT 週 |
| **checking** | **低頭,把平板斜過來看充電圖示**,嘴唇無聲在數 | 21:00 收平板 |
| **reading the fine print** | 把說明書拿遠一點,眼睛瞇一下,手指壓著某一行 | 看說明書、看規格表 |

**❌ 絕對不出現的表情:** 對鏡頭比讚、對鏡頭微笑的圖庫感、「爸爸抱小孩看夕陽」的勵志感、
酷酷的型男側臉、任何韓系或日系的偶像表情。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中低音**,基頻約 **115–125 Hz**。不渾厚、不尖 |
| 語速 | **會議約每分鐘 230 字;家裡與畫外音約 180 字。** 講到時程與數字會變快 |
| 口音 | **台灣國語,北部腔。** 沒有特別的地方腔;跟爸爸講台語時很慢 |
| 音色 | 平、略乾。**晚上錄的會有一點鼻音**(開了一天的冷氣) |
| 特徵 | **會條列。** 「第一,……;第二,……」。句尾常收在「對。」 |
| 台語 | 只跟爸爸講。**畫外音不用台語** |
| 笑聲 | 鼻子出一口氣,或一聲很短的「呵」 |
| 填充詞 | 「其實」(多)、「基本上」(多,他自己知道)、「那個」、「對」(句尾確認) |
| 情緒起伏 | **低。** 好笑的事他會用更平的語氣講,這就是笑點 |
| 絕不出現 | 「哈囉大家好」「各位爸爸們」、播報腔、業配的熱情上揚、中國腔的兒化音、**從深圳帶回來的「質量」「物料」** |

### 3.8 鏡頭前的肢體習慣

- **伸手到桌子底下插東西,手背一定朝上,貼著桌面底下慢慢伸進去。** 來源 `03 § 1-1`。這是可以拍的細節。
- **開會時鑰匙放在筆記本旁,他無意識地用拇指與食指轉珠珠上那顆黃色星星。**
- 累的時候把眼鏡推到額頭,用拇指與食指捏鼻樑。
- **在 B3 熄火後,頭往後靠在頭枕上,雙手還放在方向盤下緣。**
- 講條列的時候,用左手的手指一根一根數。
- **21:00 收平板時,把每一台斜過來看螢幕上的充電圖示**,然後才放進籃子。
- 看說明書時把它拿遠一點(他沒有老花,是習慣)。
- **他會看鏡頭,但很短,像在會議上看發言的人,然後看回物件。**

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎不。** 一年兩三次,是全家合照(小孩的臉用貼圖蓋掉,或只發他自己的半邊) |
| 出現在畫面裡的方式 | **手、手腕(錶與婚戒)、背影、車窗倒影、筆電螢幕的反光。** TikTok 露臉約 10% |
| 拍什麼 | **物件與狀況。** 書桌的籃子、抽屜、車內儀表板、說明書的某一行、游泳池等候區的地板、家庭共用日曆的截圖 |
| 構圖 | **很平。正面、置中、像要放進簡報。** 他會把東西排整齊再拍,像在拍規格照 |
| 光線 | 隨便。日光燈、檯燈、儀表板 |
| 後製 | **零。** 他不知道 IG 的濾鏡在哪裡 |
| 器材 | iPhone,主鏡頭,不用人像模式 |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「物件、桌子、車內、手」,臉是配角,小孩永遠不露臉。**
> 需要臉的時候(TikTok 少數鏡頭、商業素材)才用完整人像,而且臉要符合第五節的不可變錨。
> **構圖要像規格照,光線不能美。** 這是他跟生活風格帳號最大的差別。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**他的錢花在家裡的系統上,身上穿的是快時尚與公司發的。**

### 4.1 Office(汐止,週一到週四)

```
- 素色 polo 衫(深藍、灰、黑三件輪流,快時尚品牌,NT$590–790),沒有 logo
  或淺藍色牛津布襯衫(重要會議),袖子捲到手肘
- 深灰色或卡其色的休閒長褲(chino),腰圍比兩年前大一號
- 灰色慢跑鞋(穿了三年,鞋底側邊磨平)
- 車鑰匙(珠珠吊飾)放在左邊褲子口袋,吊飾垂在口袋外
- 黑色智慧手錶、素面婚戒
- 黑色電腦後背包(2019 年尾牙抽到的,側邊口袋插著一把摺疊傘)
- 頭髮:早上整齊,下午塌
```

### 4.2 WFH Friday / 晚上的書桌

```
- 灰色素 T(穿到領口有點鬆)
- 深藍色棉質居家長褲
- 藍白拖或室內拖鞋
- **視訊會議時:上半身換上 polo 衫,下半身不換**(他自己會講這個梗)
- 眼鏡、手錶、婚戒
- 頭髮:被手抓亂
```

### 4.3 Weekend Dad(週六游泳課、公園、Costco)

```
- 深色排汗衫(墨綠或深灰)
- 卡其色短褲(多口袋,放鑰匙、手機、小孩的髮圈)
- 運動涼鞋或那雙灰色慢跑鞋
- 一頂深藍色棒球帽(沒有 logo)
- 黑色後背包,側邊插著**兩支小孩的水壺**(一支粉色、一支綠色)
- 車鑰匙掛在短褲的腰帶環上,珠珠吊飾晃著
```

### 4.4 深圳出差

```
- 淺藍色牛津布襯衫 + 深色長褲 + 黑色皮鞋(唯一一雙,出差與婚喪喜慶用)
- 後背包 + 一個 20 吋登機箱(深灰,邊角磨白)
- **ODM 的訪客證**(夾在襯衫口袋,正面不入鏡)
- 飯店房間裡:灰色素 T,打開筆電改規格表
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 眼鏡 | 深灰色霧面方框 TR90(見 3.5) |
| 錶 | 黑色智慧手錶,運動錶帶。**不露品牌、不露錶面 logo** |
| 戒指 | 左手無名指,素面白 K |
| 鑰匙 | 車鑰匙 + 公司門禁扣 + 大樓感應扣,**掛在珠珠吊飾上**。門禁扣上的公司名不入鏡 |
| 背包 | 黑色電腦後背包(尾牙抽到的),側邊口袋有摺疊傘 |
| 鑰匙 | 車鑰匙 + 家門感應扣,掛在一個妍妍做的珠珠吊飾上 |
| 手機殼 | 黑色矽膠,背面磁吸環 |
| **不戴的** | 項鍊、手鍊、名錶、名牌包、耳環、任何大 logo 的東西、太陽眼鏡 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **眉心的淺直紋**,露臉就要有;**右手虎口的白色細疤**,手部近景就要有
2. **深灰色霧面方框眼鏡**,永遠戴著(推到額頭也算),換款式等於換人
3. **兩側推短、頂部約 4 cm 往右分的黑髮,鬢角幾根白髮**,不准染、不准燙、不准變韓系髮型
4. **長方臉、寬平下顎、窄的外雙眼皮,晚上有鬍渣**,不准變尖下巴、不准變大雙眼皮
5. **微胖身形:圓肩、小腹微凸**,不准變健身身材、不准變瘦

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系型男 / 偶像臉 / 尖下巴 | 違反人物年紀與職業,也是 AI 最容易滑過去的方向 |
| 2 | 健身身材、緊身衣 | 違反 `06 § 六` 的身體設定 |
| 3 | 西裝、名錶、名牌 | 違反 `02 § 3` 收入分配與 `07 § 4` |
| 4 | 「暖爸」圖庫:逆光、抱小孩看夕陽、暖色濾鏡 | 違反 `04 § 16` |
| 5 | **小孩露臉** | **硬規則,也是合規要求** |
| 6 | 完美的桌面 setup、RGB 燈條、無線的桌面 | **他的桌子晚上是平板睡覺的地方** |
| 7 | 電動車、跑車、Tesla 內裝、轎車 | 他開 2020 年款日系七人座 MPV(汽油) |
| 8 | 簡體字招牌、中國或日本街景(在台灣的畫面) | **他在板橋與汐止**,招牌是繁體 |
| 9 | 可辨識的公司 logo、門禁扣上的公司名、產品樣品、模型盒正面 | 法遵與公司守則 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 眉心的直紋在嗎(如果露臉);右手虎口的疤在嗎(如果拍到手)
- [ ] **眉毛有沒有被畫出疤或斷眉**(那是同批其他人物的特徵,他沒有)
- [ ] 眼鏡是不是深灰色方框,有沒有被畫歪
- [ ] 髮型是不是兩側推短、頂部往右分,鬢角有幾根白
- [ ] 臉型是長方臉寬下顎,有沒有被修成尖下巴
- [ ] 身形是不是微胖,有沒有被修成健身身材
- [ ] **有沒有任何小孩的臉**
- [ ] 有沒有出現公司 logo、門禁扣上的字、品牌、模型盒正面
- [ ] 珠珠吊飾是不是六顆塑膠珠加一顆黃色星星、藍色繩子(如果入鏡)
- [ ] 場景是不是台灣(繁體字、電梯大樓、地下室停車場、汐止辦公室)
- [ ] 色板有沒有跑掉(珠珠的藍與便利貼的黃是不是只有小點)
- [ ] 手有沒有畫壞、婚戒在不在左手、線與充電器有沒有變形

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, available light only, 35mm lens,
mild grain, no retouching, visible skin texture and pores,

a 37-year-old Taiwanese man, 172cm, slightly overweight with rounded shoulders
and a small belly, an ordinary office-worker build, not athletic,
rectangular face with a broad flat jawline and slightly full cheeks,
narrow double eyelids, dark brown eyes with faint under-eye puffiness and fine lines,
thick straight eyebrows set close together with NO scar and no gap in the brows,
a faint vertical frown line between the eyebrows that stays visible even when relaxed,
a thin 1cm pale scar on the web between the thumb and index finger of his RIGHT hand,
medium nose with a slightly wide tip, thin upper lip,
warm yellow-beige skin (#D2AE8C), slightly oily forehead, a few faint old acne marks on the cheeks,
short black hair (#1A1918), sides clipped to about 6mm, about 4cm on top parted to the right,
a few scattered grey hairs at both temples,
matte dark grey rectangular TR90 glasses,
a plain white-gold wedding band on his left ring finger,
a black smartwatch with a sport band on his left wrist, face of the watch turned inward,

calm focused expression, brows slightly drawn together, mouth closed,
looking at a screen or an object, not at the camera,

colour palette: graphite #2B2F33, IKEA white #E6E3DC, office partition grey #8A9199,
warm 3000K desk lamp amber #D9A066 under 10% of the frame,
a small accent of bead blue #3E6FB0 under 5%, at most one tiny spot of post-it yellow #F2D04B
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, the faint vertical frown line between his brows visible,
plain navy polo shirt without logo, no lanyard, sitting in an open-plan office in New Taipei,
grey desk partitions and fluorescent ceiling light behind him, a laptop in front of him,
a car key on the desk beside his notebook with a small handmade bead charm (blue cord,
six plastic beads and one yellow star bead),
evening five-o'clock shadow just starting, hair slightly flattened,
moderate depth of field f/4,

--ar 4:5
```

### 6.3 Full body(週六游泳課等候區,9:16)

```
[MASTER CHARACTER BLOCK]

full body, sitting on a plastic bench in the parents' waiting area of a public sports
centre swimming pool in Taiwan, wet tiled floor, a glass window to the pool behind him
blurred, other parents out of focus with no visible faces,
dark green moisture-wicking t-shirt, khaki cargo shorts, grey running shoes,
a navy baseball cap without logo, a black backpack beside him with a pink and a green
child's water bottle in the side pockets, a car key with a small handmade bead charm
clipped to the belt loop of his shorts,
laptop on his knees, typing, overcast daylight mixed with fluorescent light,
no children's faces in frame,

--ar 9:16
```

### 6.4 Hands / detail(主錨點,1:1)

```
photorealistic close-up photograph, office fluorescent light, 50mm lens,
moderate depth of field,

close-up of a man's hands on a grey office desk beside a closed black 14-inch laptop,
holding a car key ring with a small handmade bead charm made by a child: a blue cord,
six round plastic beads in blue, white and pink, and one yellow star-shaped bead in the
middle, one blue bead has a visible hairline crack glued back with clear nail polish,
his right thumb and index finger turning the yellow star, a thin pale 1cm scar on the web
between his right thumb and index finger, two plain access fobs on the same
ring (no logos, no text), a plain white-gold wedding band on the left ring finger,
a black smartwatch, short-cut nails, no brand logos, no readable text,

--ar 1:1
```

### 6.5 Car / B3(品牌原點時刻,9:16)

```
[MASTER CHARACTER BLOCK]

sitting in the driver's seat of a parked seven-seat Japanese MPV in an underground residential
car park in Taiwan, engine off, dashboard lights just faded, cool fluorescent light from
the car park coming through the windscreen, concrete pillar (no visible number) outside,
head tilted back against the headrest, glasses pushed up onto his forehead,
thumb and index finger pinching the bridge of his nose, both hands resting on the lower
rim of the steering wheel, a phone in a magnetic vent mount, a cheap dual USB-A charger
in the 12V socket, two empty child car seats in the second row visible in the rear-view mirror,
crumbs and a small toy garbage truck on the rear floor mat,
his right hand holding the car key, the small bead charm hanging below the steering wheel,
evening stubble, hair messed up by his hand, navy polo,

--ar 9:16
```

### 6.6 Desk at 21:00 / 桌子 A(第二錨點,4:5)

```
photorealistic documentary photograph, warm desk lamp mixed with the cool light of a
monitor, 35mm lens,

a small white 120cm IKEA-style desk against a window in a cluttered spare room of a
Taiwanese apartment at 9pm, on the right a light grey plastic storage basket with a yellow
sticky note on the front hand-written in a child's handwriting (characters unreadable,
small), two older tablets standing upright in the basket with charging cables,
a kid's smartwatch lying on the basket edge with a short magnetic charging cable,
a black 4-port desktop USB charger in the back corner with many cables,
a white 6-outlet power strip with a clear plastic cover over the master switch,
a smartphone pushed to the far edge of the desk on a wireless charging pad,
a small toy garbage truck plugged into one port of the charger with a short USB cable,
a smartwatch charging puck half hidden under a tablet, a cold coffee cup,
above the desk a shelf with three unopened plastic model kit boxes seen from the side only,
a folded guest bed and a toy cabinet in the background,
his hand entering the frame, tilting one tablet to check its charging icon,
no faces, no brand logos,

--ar 4:5
```

### 6.7 Office / 桌子 B(16:9)

```
[MASTER CHARACTER BLOCK]

wide shot of an open-plan office in Xizhi, New Taipei, rows of grey desks with low
partitions, he sits at his desk with two monitors and a laptop on a USB-C dock,
a hand-drawn child's crayon picture pinned to his partition, a printed timeline chart
(unreadable) pinned beside it, a desk drawer half open showing a tangle of spare cables,
a colleague in the background leaning over asking to borrow a cable (no clear face),
fluorescent ceiling light and grey overcast daylight from the window,
light blue oxford shirt with sleeves rolled to the elbow,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in every
panel, head and shoulders, plain off-white background, glasses on, frown line between the brows visible:
1 focused with brows slightly drawn together, mouth closed,
2 listening with head tilted slightly right, small nod,
3 a closed-mouth real smile with eyes narrowing, a short breath out of the nose,
4 laughing with head down, one hand on the back of his head,
5 deadpan with half-lowered eyelids, no movement,
6 pleased with eyebrows lifted and lips slightly open in a small "oh",
7 tired with glasses pushed up on his forehead, pinching the bridge of his nose,
8 looking down at a tablet tilted towards him, lips silently counting,
9 holding a printed instruction leaflet slightly away, eyes narrowed, finger on one line,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
before crouching under a desk to plug something in, he first places his left hand flat on
the desk corner above his head. in meetings his right index finger absent-mindedly picks
the yellow star bead on the charm of his car key lying beside his notebook. when tired he pushes his
glasses up onto his forehead and pinches the bridge of his nose. after switching off the
car engine he leans his head back on the headrest and does not move for several seconds.
when listing things he counts on the fingers of his left hand. at 9pm he tilts each
tablet to look at its charging icon before placing it in the basket. he reads instruction
leaflets holding them slightly away from his face. he glances at the camera briefly,
the way he would look at a colleague who is speaking, and returns to the object.

VOICE: mid-low male voice, fundamental around 120 Hz, flat and slightly dry, a little
nasal late at night, northern Taiwanese Mandarin accent, likes to enumerate ("first...,
second..."), sentences often end with a short "對。", voice-over around 180 Chinese
characters per minute, gets faster around numbers and dates, deadpan delivery,
no influencer greeting, no salesy rising energy, no broadcast tone.

CAMERA: handheld phone or locked-off, eye level or top-down over the desk, available
light only. children appear only as hands, backs or out-of-focus shapes, never faces.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 右手虎口的疤 | `03 § 1-1` 1998 插座在書桌後面 | ✓ |
| 眉心直紋 | `04 § 9` 公司會議的衝突風格、`06 § 四` 一天的會議量 | ✓ |
| 微胖、小腹 | `06 § 六` 每個小孩 4 公斤、脂肪肝 | ✓ |
| 圓肩前傾 | `06 § 四` 開會加開車 | ✓ |
| 鬢角白髮 | 37 歲、`02 § 16` 組織不安 | ✓ |
| 晚上的鬍渣 | `06 § 四` 07:00 出門,19:20 到家 | ✓ |
| 左前臂比較深 | `06 § 三` 開車靠窗 | ✓ |
| 婚戒素面 | `02 § 4` 結婚八年、`02 § 3` 不花在自己身上 | ✓ |
| 智慧手錶、不是名錶 | `02 § 9` Apple 生態、隔代才換 | ✓ |
| 快時尚 polo、快剪頭髮 | `02 § 3` 錢的順位 | ✓ |
| 珠珠吊飾在鑰匙上 | `03 § 6-5` 妍妍「這樣你就不會忘記回家」 | ✓ |
| 拇指食指互搓 | `04 § 15` 轉珠珠星星的習慣 | ✓ |
| 規格照式的構圖 | `02 § 6` PM、簡報習慣 | ✓ |
| 幾乎不自拍 | `04 § 13` 私下 E 值 32 | ✓ |
| 小孩永遠不露臉 | `02 § 17` 硬性禁止 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.9 影片提示詞、五個不可變錨、**小孩不露臉**。
**Ivy(素材):** 讀 6.1 master block、6.4 手部鏡頭、6.6 書桌 21:00、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**
**6.6 的桌充是他 2023 年買的那顆黑色塑膠四孔,不得畫成任何鋁殼、伸縮線、主開關的造型。**

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| full_body | *(本輪未生圖)* | | | |
| hands_detail | *(本輪未生圖)* | | | |
| car_b3 | *(本輪未生圖)* | | | |
| desk_2100 | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** 主 session 指定「不生圖,seed 表留空」。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.2 | 2026-10-20 | 跨人物撞型修正:配角改名:初階 PM 陳郁婷 → 陳安琪(Tina 不變,避開 `persona_tw_02d` 主角簡郁婷);大學同學周哲宇的暱稱「阿哲」→「阿周」(避開 `persona_tw_04b` 的阿哲學長) | 主 session 統一 QA:第二批平行生成,與 `035`、`07` 的主開關判斷平行度過高,配角名撞 `02d`、`04b` |

*檔案版本:v1.2 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
