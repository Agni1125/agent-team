# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
> `ai-avatar` 原本要求的 `output/<slug>/` 資料夾與 `system_prompt.md` 不另外拆檔,
> 對白樣本與互動邊界已在 `09`、`10`、`13`,本檔只管外型與生圖。原因寫在 `00 § 一`。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   yung-ching-su
display_name:     蘇詠晴 Su Yung-Ching(Ching)

art_style:        photorealistic smartphone photography, candid, everyday
                  # 不是 CG、不是插畫、不是韓系網美照、不是 lifestyle 圖庫。是手機照。
style_reference:  iPhone main camera look, natural daylight or late-afternoon
                  west-facing window light, slight overexposure in highlights,
                  no beauty retouching, visible skin texture, real tan lines,
                  Southern Taiwan humidity (slight shine on skin)

color_palette:
  - "#E8DCCB"   # starlight oat — MacBook 星光色、米白針織衫、她的大腸髮圈
  - "#C49A6C"   # light oak — 淺木色桌板、地板
  - "#D9B26F"   # kraft-box tan — 待退的紙箱、牛皮紙袋、出貨單。點綴,不超過 6%
  - "#B5E61D"   # highlighter green — 公務機的殼、綠色的線、綠色出差收納包。**只能是一小塊,不超過畫面 5%**
  - "#5E6B78"   # Kaohsiung storm grey — 午後雷陣雨前的天、老大樓的磁磚
  - "#F0B67F"   # west-sun amber — 下午三點的西曬,透過半拉的窗簾

lighting_default: 自然光為主。
                  白天:窗光,下午有西曬的暖色斜光(窗簾條紋影子可入鏡);
                  晚上:檯燈 + 螢幕光;
                  台北辦公室:日光燈的平光,有點冷。
                  **不用環形燈、不用美肌補光、不用柔焦。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok
  square:    1:1
  wide:      16:9

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
plastic skin, airbrushed skin, beauty filter, porcelain white skin, pale skin,
k-pop idol, korean ulzzang makeup, big doe eyes, coloured contacts, v-shaped face,
sharp chin, tiny face, glass skin, heavy contour, false eyelashes, glossy lips,
influencer pose, peace sign, duck face, laptop on the beach, digital nomad aesthetic,
cafe latte art, flat lay with flowers, pastel aesthetic, soft focus glow,
ring light catchlight, studio beauty lighting, teal-and-orange grade,
all-white minimalist desk, empty perfectly clean desk, rgb gaming setup,
anime, illustration, 3d render, cgi, doll-like, model physique,
designer handbag, luxury jewelry, long acrylic nails, nail art, glasses,
fake brand logos, readable brand names, unreadable chinese characters, garbled text,
watermark, simplified chinese signage, mainland china street, japanese street signs,
extra fingers, malformed hands, two phones merged into one, warped phone case
```

**為什麼要排除這些(不是隨便列的):**
- `k-pop idol / ulzzang / big doe eyes / v-shaped face` — AI 生「亞洲年輕女性」最常滑過去的方向。她是左營長大、騎機車、曬過太陽的人。
- `porcelain white skin / pale skin / glass skin` — **她的皮膚是曬過的**,顴骨上有淡斑,手腕有錶帶的白痕。美白就不是她了。
- `laptop on the beach / digital nomad aesthetic` — **遠端工作最容易漂移的方向。** 她的遠端是一個人在家、西曬、短褲加針織衫。
- `all-white minimalist desk / empty perfectly clean desk` — 她的桌子是淺木色,上面有兩支手機、一盆小植物、線、一個馬克杯。
- `rgb gaming setup` — 她不是電競桌。
- `glasses` — **她不戴眼鏡。** 這一條是跟其他人物拉開視覺距離的硬條件。
- `long acrylic nails / nail art` — 她有做單色凝膠,但很短、而且長出來了。長甲與彩繪不行。
- `two phones merged into one / warped phone case` — 這個人物的畫面常常同時有兩支手機,AI 很容易把它們畫成一支或畫歪。
- `readable brand names` — 她的公司、她用的產品,**畫面上一律不能出現可辨識的品牌**。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 蘇詠晴(Ching) |
| slug | `yung-ching-su` |
| age_appearance | **26–29**(看起來跟實際年齡差不多,累的時候眼下會暗) |
| gender | 女 / she-her |
| ethnicity | 台灣人,閩南家庭,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 中等身材,不纖細。肩膀有一點圓(長時間拿手機),小腿有騎車的線條 |
| location_look | 高雄,曬過太陽的人:**顴骨與鼻樑有淡淡的曬斑,左手腕有 Apple Watch 錶帶的白色曬痕**,脖子後面比臉深一階 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **圓臉**,下顎線柔和,臉頰有肉,笑起來蘋果肌很明顯 | 反 V 臉 |
| **膚色** | `#C99A73` 暖調小麥色,**曬過**。夏天更深,十月還沒退 | 高雄、騎車、走路 |
| **膚質** | 有毛孔,T 字部位在高雄的濕度下會有一點油光;**顴骨與鼻樑有淡斑** | 反美肌 |
| **眼睛** | 深棕色,**自然的內雙(很窄的一條摺)**,眼型偏圓,眼尾平;有一點臥蠶 | 跟單眼皮的人物拉開距離,又不是大眼雙眼皮 |
| **眉毛** | **平眉,修過**,有在畫(視訊開會要見人),顏色比髮根淺 | 她每天早上只做這一件事 |
| **鼻子** | 鼻樑中等,鼻頭小而圓 | |
| **嘴** | 中等厚度,嘴角天生微微上揚。**平常只擦護唇膏,視訊日擦一支豆沙色唇釉** | |
| **疤** | **下巴左下方一道約 1.5 cm 的淺色細疤**(十九歲騎車滑倒,縫四針) | **第一辨識點** |
| **表情基準** | **看手機時下唇會輕輕咬住**,眉頭微抬,像在讀一則很長的留言 | 見 3.6 |

### 3.2 頭髮

- **長到肩胛骨,有層次,霧感奶茶棕**(`#9C7A5B`),髮尾褪成偏黃的暖棕。
- **髮根長出約 3 公分的黑色**(`#1E1B19`)。她三個月沒去補染,「等檔期過」。
  ← 這條寫死,因為它是「這個人有在打理,但工作壓過了」的視覺速記。
- 髮質偏細,高雄的濕度讓髮尾有一點毛躁。
- 狀態指示(寫死):

| 頭髮怎麼弄 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| **半紮,用米白色大腸髮圈** | 平常在家工作 | 書桌、午休、美術館散步 |
| **高馬尾,紮很緊** | **直播場控模式** | 週三晚上的桌前 |
| 放下來,梳過 | 視訊重要會議、台北出差、婚禮 | 正式一點的場合 |
| 戴漁夫帽,頭髮塞耳後 | 白天出門(防曬) | 好市多、騎車、內惟市場 |

- **左手腕永遠套著一條米白色的大腸髮圈**,沒紮頭髮的時候也在。

### 3.3 身體

- **身高 162 cm。體重 53 kg。**
- 肩膀有一點圓(長時間低頭看手機),右肩比左肩高一點點(公務機常夾在右手)。
- 腰腹普通,腿是普通的腿,**小腿有騎車的線條**,腳背有拖鞋的曬痕。
- 手:**中等大小,手指細。指甲做單色裸粉色凝膠,短,但已經長出約 2 mm 的空隙**(六週沒去補)。
  **右手拇指指腹常有一點乾裂**(一天打字十小時)。
  **手是這個人物最重要的身體部位之一:她的畫面常常是手拿兩支手機。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **下巴左下方的淺色細疤。** 任何正臉或四分之三側臉都必須有。**第一辨識點。**
2. **左手腕 Apple Watch 錶帶的白色曬痕。** 錶拿下來的時候看得到。
3. **髮根三公分的黑色。** 任何拍到頭頂或分線的畫面都要有。
4. **顴骨與鼻樑的淡斑。** 曬出來的幾點,不多,不要畫成滿臉雀斑。

### 3.5 眼鏡

**她不戴眼鏡。** 視力兩眼各輕微近視(約 -0.75),不矯正。
戶外戴一副便宜的黑色太陽眼鏡(好市多,兩副一組),常常推在頭上。
**任何室內畫面不得出現眼鏡。**

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | **看手機,下唇輕咬,眉頭微抬** | 60% 的畫面 |
| **reading a long comment** | 眼睛往下快速掃,嘴唇無聲在動 | 看留言區 |
| **real smile** | **嘴角往上、露出上排牙齒的一半,蘋果肌鼓起,眼睛變細** | 跟芒果、跟安安、看到一則回得很好的留言 |
| **laugh** | **頭往後仰一點,手拍一下桌子** | 跟哥哥互虧、Allen 講冷笑話 |
| **polite customer-service face** | 嘴角固定、眼睛不笑。**她自己知道這張臉** | 視訊會議、老闆說話時 |
| **caught** | 眉毛一高一低,嘴巴抿成一條線 | 被發現在退貨、被問「妳 HR 回了沒」 |
| **tired** | 兩手掌撐著臉頰,眼神放空看螢幕 | 直播結束後 |
| **wrong phone** | 拿起一支手機,停頓,換另一支 | 每天都會發生一次 |
| **drawer close** | 側臉,看著抽屜,手推上,肩膀放下來 | 18:30 下線。**她最重要的一個表情** |

**❌ 絕對不出現的表情:** 比 YA、嘟嘴、歪頭裝可愛、對鏡頭眨眼、
網美式的「看遠方微笑」、「拿著咖啡杯對窗外沉思」、任何韓系或日系的偶像表情。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中音偏高**,基頻約 **215–235 Hz**。不嗲,但比較亮 |
| 語速 | **工作模式(視訊、場控):約每分鐘 240 字,很快、很清楚。** 私人畫外音:約每分鐘 190 字,比較懶 |
| 口音 | **南部的台灣國語。** 尾音比較軟,「齁」「啦」「欸」比較多;累的時候「是不是」會變成「係不係」那種收音 |
| 音色 | 乾淨,有一點鼻音,早上剛起床會沙 |
| 特徵 | **會條列。** 「第一,第二,然後第三是我自己」 |
| 台語 | 偶爾:「嘿啊」「莫啦」。**不刻意,不當笑點** |
| 笑聲 | 短促的「欸嘿」,或一聲「哈」加拍桌 |
| 填充詞 | 「就是」(多)、「對啊」、「然後」、「齁」(句尾) |
| 情緒起伏 | **中高。** 講到別人回得好的留言會變快、變亮 |
| 絕不出現 | 「哈囉大家好」「寶寶們」「家人們」「親~」(那是她上班的聲音)、播報腔、嗲聲、網紅式上揚尾音、中國腔兒化音 |

### 3.8 鏡頭前的肢體習慣

- **兩隻手各拿一支手機,用兩個拇指同時滑。** 這是她最有辨識度的姿勢。
- **每天至少一次拿錯手機:** 拿起綠色的,停一下,放下,拿透明的。
- **思考時用食指指節敲桌面兩下。**
- **緊張時把手腕上的大腸髮圈拉起來彈一下。**
- 看留言時下唇輕咬,身體往螢幕靠。
- 開視訊前三秒:把椅背上的米白針織衫拉過來套上,**下半身是短褲**。
- **18:30 把綠色的公務機放進抽屜,關上,雙手放在桌上停兩秒。**
- 她看鏡頭的時間比較長(她習慣視訊),但講到重點會看旁邊的螢幕。

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **給摯友的限動常有臉(一週兩三次)。** 公開的 feed 九張裡最多一張有臉 |
| 出現在畫面裡的方式 | **手(拿兩支手機)、側臉、鏡子、視訊畫面的截圖**。TikTok 約 15% 露臉 |
| 拍什麼 | **螢幕、留言截圖(去識別化)、桌面、好市多推車、美術館草皮、芒果的手和腳(不露臉)、西曬** |
| 構圖 | **中等。** 她會拍,但不像攝影師那樣講究。豎拍為主 |
| 光線 | **她喜歡西曬。** 下午三點窗簾條紋打在桌上的照片她拍過很多次 |
| 後製 | **輕。** 用手機內建的調整拉一點亮度、加一點暖。不用濾鏡 App |
| 器材 | 私人 iPhone。**公務機的相機只拍公司的東西**(這條是她的界線) |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「螢幕、手、兩支手機、生活的小角落」。**
> 臉可以出現,但不是主角。**最重要的視覺訊號是綠色與透明兩支手機同框。**
> **光線可以好看(西曬),構圖不用完美。** 這是她跟網美最大的差別:她的照片是生活截圖,不是作品。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 10` 的消費行為:
**Apple 的東西是工具(可以貴),身上穿的是平價、好市多、蝦皮,外加幾件「上台北才穿」的衣服。**

### 4.1 WFH Outfit(在家工作,上半身與下半身是兩個人)

```
- 上:灰色或白色的寬版素 T(沒有字,洗到領口有點鬆)
- **視訊時:椅背上那件米白色的薄針織開衫,開會前三秒套上**
- 下:棉質短褲(深藍或黑色),**入鏡時常常被看到**
- 腳:室內拖鞋(灰色,好市多)
- 頭髮:半紮,米白大腸髮圈
- Apple Watch(星光色錶帶)
- 素顏 + 畫眉 + 護唇膏
← 「上半身開會,下半身放假」是遠端工作者的真實樣子,也是她的固定梗
```

### 4.2 Kaohsiung Out(白天出門:好市多、內惟市場、騎車)

```
- 寬版亞麻襯衫(米白或淺藍),當外套穿,裡面一件素 T
- 牛仔寬褲,或運動短褲(去好市多)
- 黑色涼鞋或拖鞋
- 米色漁夫帽,黑色太陽眼鏡推在帽緣
- **騎車時:淺灰色防曬袖套**(她知道很醜,她說「這是高雄的制服」)
- 帆布托特包(2021 年第一個募資的那個,米白色,洗到有點灰)
```

### 4.3 Taipei Office Day(一個月兩天)

```
- 白色襯衫 + 黑色針織背心
- 黑色或灰色西裝寬褲
- 黑色樂福鞋(一雙,穿兩年,鞋跟磨了)
- **一件薄的灰色外套:台北冷氣很冷,她每次都帶**
- 頭髮放下,梳過
- 豆沙色唇釉
- **後背包:那個 NT$3,280 的機能後背包,霧灰色,在日光燈下看起來偏綠**
- 背包裡:綠色出差收納包
```

### 4.4 Weekend / 左營(好市多、回爸媽家、帶芒果)

```
- 寬版 T + 運動褲或寬短褲
- 白色球鞋(有點髒)
- 帽子
- 頭髮半紮或鯊魚夾
- 手上常常抱著芒果,或推著好市多的推車
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **Apple Watch Series 9,星光色錶帶**(前男友送的)。不換錶帶 |
| 髮圈 | **米白色大腸髮圈,永遠在左手腕** |
| 耳環 | **兩邊各一顆小珍珠耳針**(媽媽送的,好市多買的) |
| 太陽眼鏡 | 黑色,便宜,常常推在頭上 |
| 包 | 平日:米白帆布托特;台北:霧灰機能後背包 |
| 手機 | **私人:沙漠色 iPhone 16 Pro,透明殼,白色與淺藍珠珠手機鍊;公務:iPhone 14,螢光綠矽膠殼,背面白色油漆筆寫的「公」** |
| **不戴的** | 戒指、項鍊、手鍊、名牌包、彩繪美甲、大耳環、眼鏡、任何 logo 很大的東西 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **下巴左下方的淺色細疤**,露臉就要有
2. **圓臉、自然內雙、曬過的暖小麥色皮膚加顴骨淡斑**,不准變 V 臉、不准美白
3. **長到肩胛骨的霧奶茶棕頭髮,髮根三公分黑色**,不准變全黑、不准變短、不准染新的
4. **不戴眼鏡**,室內任何畫面都沒有眼鏡
5. **左手腕的米白大腸髮圈 + 星光色 Apple Watch**

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 韓系網美 / 偶像臉 / V 臉大眼 | AI 最容易滑過去的方向 |
| 2 | 白皙、柔焦、美肌 | 她曬過太陽,這是高雄 |
| 3 | 海邊開筆電、咖啡廳擺拍、數位遊牧 | **遠端的漂移方向。** 她的遠端是家裡的書桌 |
| 4 | 純白極簡桌面 | 她的桌子是淺木色加雜物加線 |
| 5 | 電競桌、RGB 燈 | 不是她 |
| 6 | 精緻全妝、長甲、名牌包 | 違反 `02 § 3` 收入與 `02 § 10` 的消費 |
| 7 | 戴眼鏡 | 她不戴 |
| 8 | 只有一支手機 | **她的工作畫面一定是兩支,綠色那支要在** |
| 9 | 簡體字招牌、中國或日本街景 | 她在高雄,招牌是繁體 |
| 10 | 出現可辨識的品牌 logo、公司名、真人臉 | 法遵;她任職的公司永遠不露 |

### 連續性檢查表(每次出圖後跑)

- [ ] 下巴的疤在嗎(如果露臉)
- [ ] 是圓臉、自然內雙嗎,有沒有被修成 V 臉大眼
- [ ] 皮膚有沒有被美白、磨皮;顴骨的淡斑在不在
- [ ] 頭髮的髮根黑色有沒有被畫掉
- [ ] 有沒有不小心戴上眼鏡
- [ ] 左手腕的髮圈與錶在不在
- [ ] 工作畫面裡綠色的公務機在不在;兩支手機有沒有被畫成一支
- [ ] 綠色有沒有超過畫面 5%
- [ ] 場景是不是台灣南部(繁體字、電梯舊大樓、機車、西曬)
- [ ] 有沒有出現亂碼中文、假 logo、可辨識的品牌

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic candid smartphone photograph, natural light, no retouching,
visible skin texture and pores, slight humidity shine on skin,

a 28-year-old Taiwanese woman, 162cm, average build, shoulders slightly rounded
from looking down at phones,
round face with a soft jawline and full cheeks, natural narrow inner double eyelids,
dark brown eyes, slightly round eye shape, faint aegyo sal,
straight groomed eyebrows, small rounded nose tip, medium lips with naturally
upturned corners, bare lips with balm,
warm tan skin (#C99A73) with a few faint sun spots on the cheekbones and nose bridge,
a thin pale 1.5cm scar under the left side of her chin,
long layered hair past the shoulder blades, faded milk-tea brown (#9C7A5B)
with 3cm of dark black roots grown out, slightly frizzy ends from humidity,
no glasses,
small pearl stud earrings, a starlight Apple-style smartwatch on the left wrist
with a pale tan line around it, an off-white fabric scrunchie on the left wrist,
short nude-pink gel nails with 2mm of grown-out gap,

looking down at a phone with her lower lip lightly bitten, brows slightly raised,
not looking at the camera,

colour palette: starlight oat #E8DCCB, light oak #C49A6C, storm grey #5E6B78,
west-sun amber #F0B67F, with a small highlighter-green accent #B5E61D
under 5% of the frame and kraft-box tan #D9B26F under 6%
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle, sitting at a light oak desk by a window
in a small Kaohsiung apartment, late afternoon west sun coming through a
half-drawn curtain, warm striped light across her face and shoulder,
grey loose t-shirt with a thin off-white cardigan pulled over it,
hair half-up with an off-white scrunchie,
holding a phone in a clear case, shallow depth of field f/2.8,

--ar 4:5
```

### 6.3 Two phones(招牌鏡頭,主錨點,1:1)

```
photorealistic close-up photograph, natural window light with warm afternoon sun,
50mm, shallow depth of field,

close-up of a young woman's hands with short nude-pink gel nails (grown out),
an off-white scrunchie on the left wrist and a starlight smartwatch,
holding two phones at once and scrolling with both thumbs:
in the left hand an older phone in a bright highlighter-green silicone case
with the single traditional Chinese character "公" hand-written on the back
in white paint marker, the last stroke slightly worn,
in the right hand a desert-titanium phone in a clear case with a white and
pale blue beaded phone strap,
a light oak desk below with a white three-in-one wireless charging stand,
a starlight laptop on a stand in the background, a ceramic mug,
no faces, no brand logos,

--ar 1:1
```

### 6.4 Drawer close(18:30,9:16)

```
[MASTER CHARACTER BLOCK]

side view at a light oak desk at 6:30pm, she is placing a phone in a
highlighter-green case into the open left drawer of the desk and pushing it closed,
shoulders dropping, a starlight laptop closed on a stand, the monitor turned off,
a small potted plant, evening light fading blue through the window,
one warm desk lamp on,
grey t-shirt, dark cotton shorts, hair half-up,

--ar 9:16
```

### 6.5 Livestream control desk(週三直播場控,16:9)

```
[MASTER CHARACTER BLOCK]

wide shot of a cluttered home desk at 9pm during a live-selling stream,
she sits with her hair in a tight high ponytail, wireless earbuds in,
a laptop showing an order dashboard (no readable text), a tablet on a stand
showing a livestream video (no faces visible, no text), a phone in a
highlighter-green case resting on a small phone stand with a magnetic
power bank fixed to the stand with a strip of black velcro,
a second phone face-down on a white three-in-one charging stand,
cables running down the back of the desk to a white 6-outlet power strip on the floor,
desk lamp and screen light only, she is typing on the green phone with one thumb,

--ar 16:9
```

### 6.6 Costco(週六早上,9:16)

```
[MASTER CHARACTER BLOCK]

pushing a large warehouse-store shopping cart in a wide aisle with tall shelves,
an older Taiwanese woman (her mother, back view only, face not visible)
walking ahead reading a receipt,
she wears a beige bucket hat with black sunglasses pushed up on it,
a loose pale-blue linen shirt over a white t-shirt, sports shorts, white sneakers,
looking at her phone in a clear case, overhead fluorescent warehouse light,
no brand logos or readable signage,

--ar 9:16
```

### 6.7 Return shelf(待退盒子區,4:5)

```
photorealistic smartphone photograph, flat daylight,

a small white three-tier shoe-side cabinet by an apartment front door,
the middle shelf holding three neatly re-taped product boxes of different sizes
and one folded padded mailer, each shipping label marked in black marker
with a date (only numbers legible), a pair of grey slippers
and a scooter helmet on the floor beside it, old beige floor tiles,
no brand logos, no readable text other than dates,

--ar 4:5
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same woman, identical lighting and framing
in every panel, head and shoulders, plain off-white wall background, no glasses:
1 reading a phone with lower lip lightly bitten and brows raised,
2 eyes scanning down quickly with lips silently moving,
3 a real smile showing half of the upper teeth with lifted cheeks and narrowed eyes,
4 laughing with head tipped slightly back,
5 a polite fixed customer-service smile where the eyes do not smile,
6 caught out with one eyebrow up and lips pressed into a line,
7 tired with both palms holding her cheeks and an unfocused gaze,
8 pausing with a phone half-raised as if she picked up the wrong one,
9 side profile with shoulders dropping as she closes a drawer,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
she holds two phones at once and scrolls both with her thumbs. at least once
she picks up the wrong phone, pauses, puts it down and picks up the other.
when thinking she taps the desk twice with the knuckle of her index finger.
when nervous she pulls the scrunchie on her left wrist and lets it snap back.
three seconds before a video call she pulls an off-white cardigan from the
chair back over her t-shirt while still wearing shorts. at 6:30pm she places
the green phone in the left desk drawer, slides it shut, and rests both hands
flat on the desk for two seconds. she looks at the camera longer than most
people, then glances at a side screen when making a point.

VOICE: bright mid-high female voice, fundamental around 225 Hz, clean with a
slight nasal tone, Southern Taiwanese Mandarin with soft sentence endings,
work mode about 240 Chinese characters per minute and very clear,
personal voice-over about 190 characters per minute and more relaxed,
lists things ("first, second, and the third one is me"),
no influencer greeting, no cutesy tone, no customer-service "qin~" voice.

CAMERA: handheld phone or a small tripod at desk height, 26mm phone lens look,
natural window light with west sun, screens and hands as the main subject.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 曬過的皮膚、顴骨淡斑 | `06 § 三` 騎車、`06 § 四` 每天早上走路、`01` 高雄 | ✓ |
| 錶帶曬痕 | `02 § 9` Apple Watch 每天戴 | ✓ |
| 下巴的疤 | `06 § 六` 十九歲騎車滑倒 | ✓ |
| 髮根三公分沒補染 | `11` 雙 11 檔期、`04 § 13` 生活 C 值 55 | ✓ |
| 凝膠長出空隙 | 同上;單色凝膠符合 `02 § 3` 收入 | ✓ |
| 右肩比較高、肩膀圓 | `06 § 六` 公務機常夾右手 | ✓ |
| 拇指乾裂 | `02 § 8` 螢幕時間九小時 | ✓ |
| 不戴眼鏡 | 視力輕微近視,`02` 未設定矯正 | ✓ |
| 上半身針織衫、下半身短褲 | `06 § 四` 遠端工作、視訊會議 | ✓ |
| 防曬袖套 | `01 § 五` 高雄機車 | ✓ |
| 帆布托特、機能後背包 | `03 § 8` 第一個與唯一破線的募資 | ✓ |
| 珍珠耳針、好市多 | `05 § 2` 媽媽 | ✓ |
| Apple Watch 不換 | `05 § 12`「錶又沒做錯事」 | ✓ |
| 兩支手機、綠色殼 | `03 § 5-3` 2023 手滑限動 | ✓ |
| 公務機的相機只拍公司的東西 | `03 § 5-3` 界線要是實體的 | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.9 影片提示詞、五個不可變錨。
**Ivy(素材):** 讀 6.1 master block、6.3 兩支手機的鏡頭、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**
**她任職的寢具品牌是虛構的,任何畫面都不得出現該品牌的 logo 或可辨識的商品包裝。**

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| two_phones | *(本輪未生圖)* | | | |
| drawer_close | *(本輪未生圖)* | | | |
| livestream_desk | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,不是圖。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.2 | 2026-10-20 | 跨人物撞型修正:台語詞「足熱」改為「莫啦」(避開 `persona_tw_02` 的「足累」同型) | 主 session 統一 QA:第二批平行生成,口頭禪、笑點記號、配角名與其他人物撞在一起 |

*檔案版本:v1.2 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
