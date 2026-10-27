# 07 — Visual Bible(視覺聖經 / Visual DNA)

> 走 `ai-avatar` 的**靈感模式**:所有參數由既有人設反推,不停下來提問。
> 不確定的項目已列進 `00_generation_notes.md` 的 LOW-CONFIDENCE 清單。
>
> **這份檔案的唯一目的:讓十次生圖看起來是同一個人。**
> 給 Libai(影片模特提示詞)與 Ivy(素材)使用。
>
> **本人物有一個兩歲的女兒。任何生圖、影片都不得出現可辨識的小孩臉、小孩全身或小孩的身體特寫。**
> 女兒的存在一律用物件表現(小鞋子、蠟筆、鯨魚貼紙、門框刻度、白板)。見第五節。
>
> **撞型提醒(2026-10-20 交叉比對後修改):** 同批人物裡已有人使用「左眉尾斷眉疤」「鬢角早白」「方框眼鏡」
> 「素面婚戒」「polo + 卡其褲」「孩子貼的恐龍貼紙」「藍色識別證掛繩」。**本人物刻意全部避開**,見 `00 § 四` 第 13 項。

---

## 一、Visual Anchor(視覺錨點,最先鎖定,不可變更)

```yaml
# consistency.yaml 等價內容
character_slug:   ching-heng-chiu
display_name:     邱敬恆 Chiu Ching-Heng(阿恆 / Henry)

art_style:        photorealistic documentary photography
                  # 是照片。不是 CG、不是插畫、不是男性時尚雜誌照、不是科技廣告的工程師形象照。
style_reference:  candid smartphone-quality photo of an ordinary Taiwanese office worker,
                  flat practical light, slight noise in low light, no retouching,
                  realistic skin with pores and stubble shadow, f/2.8–f/5.6,
                  composition often centred and straight-on like evidence photos

color_palette:
  - "#3A3D42"   # hoodie charcoal — 他平日穿的素面帽 T、夜裡的客廳
  - "#E6E3DC"   # new-build wall off-white — 竹北新大樓的牆、書房、玄關
  - "#8C9196"   # northeast-monsoon grey — 九降風天空、竹科建築、地下停車場
  - "#F4F4F0"   # whiteboard white — 臥室門背面的白板、延長線防護盒、白牌充電頭
  - "#6FA8DC"   # whale sticker blue — 女兒的鯨魚貼紙。**點綴用,不超過畫面 5%**
  - "#D94141"   # power-strip pilot red — 防護盒縫透出的開關小燈。**只能是一兩個小點**

lighting_default: practical light only.
                  公司:天花板日光燈,冷白,平;
                  家裡:3000K 暖色吸頂燈 + 螢幕冷光;
                  夜裡:嬰兒監視器家長端的灰綠夜視光、手機最低亮度;
                  車上:中控螢幕的光 + 地下停車場的日光燈管。
                  **不用環形燈、不用棚燈、不用電影感調色(teal and orange)、不用逆光剪影。**

aspect_ratios:
  portrait:  4:5     # IG feed
  vertical:  9:16    # Threads 圖、IG 限動、TikTok、Reels
  square:    1:1
  wide:      16:9    # YouTube

seed_policy:      第一次生成留空,記錄回傳 seed 後鎖定並寫回本檔第九節。
                  微調同一張圖用同 seed;換場景換 seed 但保留完整外貌描述段。
```

### Negative prompt seed(所有生圖必帶)

```
child face, toddler face, baby face, any visible child, child body, kid in frame,
k-pop idol, male model, sharp jawline model, chiseled jaw, six-pack, gym body, muscular arms,
styled beard, designer stubble, slicked-back hair, undercut fashion haircut, dyed hair, grey hair,
eyeglasses, spectacles, eyebrow scar, earrings, tattoos, rings, wedding ring,
luxury watch, gold jewellery, designer logo, visible brand logos,
readable company name, ID badge, employee photo,
sports car, luxury car interior, tesla interior,
suit and tie, polo shirt, tech CEO stage, startup office with neon sign, gaming RGB lights,
perfectly tidy minimalist desk, desk setup influencer aesthetic, cable-free desk,
dinosaur sticker, dinosaur toy,
studio lighting, ring light catchlight, teal-and-orange grade, cinematic backlight,
airbrushed skin, beauty filter, plastic skin,
anime, illustration, 3d render, cgi,
simplified chinese signage, mainland china street, japanese street signs,
unreadable chinese characters, garbled text, watermark,
extra fingers, malformed hands, warped cables, melted plastic
```

**為什麼要排除這些(不是隨便列的):**
- `child face / toddler face / any visible child` — **合規優先。** 生成擬真小孩影像有平台政策與法遵風險,而且這個人物的規則是女兒不露臉。見第五節第 9 條。
- `male model / chiseled jaw / six-pack / gym body` — AI 生「台灣男性工程師」很容易滑向兩個極端:男模或宅男刻板。他兩個都不是:普通體型,這兩年胖了 7 公斤。
- `eyeglasses / eyebrow scar / grey hair / wedding ring / polo shirt / dinosaur sticker` — **同批人物撞型。** 本人物不戴眼鏡、沒有眉疤、沒有白髮、平日不戴婚戒、不穿 polo、女兒的貼紙是鯨魚。AI 生「三十幾歲爸爸工程師」時很容易自動補上這些,要主動擋。
- `luxury watch / sports car / tesla interior` — **竹科新貴刻板印象。** 違反 `02 § 3` 與 `06 § 三`(二手汽油小休旅)。
- `perfectly tidy minimalist desk / desk setup influencer aesthetic / cable-free desk` — 他放棄桌面改造了,而且他的書房桌被全家占用。違反 `04 § 16`。
- `readable company name / ID badge` — **保密。** 識別證不入鏡。
- `simplified chinese signage / japanese street signs` — 場景漂移。他在竹北與竹科,招牌是繁體。

---

## 二、Identity Card

| 欄位 | 內容 |
|---|---|
| display_name | 邱敬恆(阿恆 / Henry) |
| slug | `ching-heng-chiu` |
| age_appearance | **31–35**(臉圓,看起來不老;累是看眼下跟姿勢) |
| gender | 男 / he-him |
| ethnicity | 台灣人,屏東閩南家庭,**東亞面孔,不混血、不韓系、不日系** |
| build_class | 中等身材,微胖。肚子有一點,肩膀不寬,左肩比右肩低一點(抱小孩都抱左邊) |
| location_look | 竹北與竹科的上班族:**左手前臂比右手黑一階**(開車時左窗的日照),臉色是辦公室的白,底子是南部的黑 |

---

## 三、Visual DNA(外貌細節,可圖化)

### 3.1 臉

| 部位 | 描述 | 為什麼是這樣 |
|---|---|---|
| **臉型** | **圓臉**,兩頰有一點肉,下巴短,低頭時有一點雙下巴的影子 | 反男模。`06 § 六` 的 7 公斤 |
| **膚色** | `#C9A27E` 暖調小麥色,臉比手臂白一點(辦公室),**兩隻手臂一樣深** | 屏東長大 + 竹科上班 + 開車 |
| **膚質** | 有毛孔,鼻翼兩側略油。**晚上九點以後下巴有青色鬍渣陰影**(早上刮的) | 反美肌 |
| **眼睛** | 深棕色,**單眼皮,眼睛細長**,眼神平。**眼下有輕微的黑眼圈** | 06:30 被叫起床 |
| **眉毛** | 濃、平、偏短,眉尾自然收。**右眉中段有一顆約 3 mm 的深色痣,眉毛從痣上長過去,近看才看得到** | **第一辨識點(臉)** |
| **鼻子** | 鼻樑中等,鼻頭圓 | |
| **嘴** | 唇形中等,嘴角平。**不笑的時候嘴角略往下,看起來很嚴肅** | 見 3.6 |
| **耳朵** | 普通,沒有耳洞。**右耳常常塞著一顆 AirPods**(見 3.5) | |
| **表情基準** | **平。專注時眉頭不皺,嘴巴抿著。** 他看起來永遠像在聽一個不太確定的 bug 回報 | |

### 3.2 頭髮

- 黑色(`#141414`),**沒有白髮**,沒染過。
- **自己用電剪推的短髮:兩側約 6 mm,頭頂約 1.5 cm。** 女兒出生之後他就沒進過理髮店,
  每三週週六早上在浴室自己推一次。**後腦勺右下有一小塊推得不平**(他自己看不到,太太說的)。
- 早上沒時間整理,但頭髮短到不會亂。**這是他選這個髮型的全部理由。**
- 狀態指示:

| 頭髮怎麼樣 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| 剛推完,很短、很整齊 | 週六早上、週末 | 週末出遊 |
| 長出來一點,頭頂毛躁 | 第三週、忙的時候 | 平日 |
| **後腦勺那一塊不平** | 一直都在 | 背影鏡頭 |

### 3.3 身體

- **身高 172 cm。體重 75 kg。** 2024 年 68 kg。
- 肩膀中等寬,**左肩比右肩低一點**。站著的時候重心在右腳(左邊習慣留給小孩)。
- 腰腹有一點肉,帽 T 下襬在肚子那裡會撐出一點弧度。**他不在意,也沒有在管。**
- 手:**大,指節略粗,指甲剪得很短很平。**
  **右手食指第二指節外側有一道約 0.8 公分的白色淡疤**(2012 年大二實驗,第一塊燒掉的板子那天被烙鐵燙到,見 `03 § 3-1`)。
  **手是這個人物最重要的身體部位之一**,任何近景都要拍到:拔插頭、寫白板、按長尾夾、拍口袋。
- **平日不戴婚戒。** 婚戒放在主臥床頭的一個小瓷盤裡(「打鍵盤會卡」),只有過年、喝喜酒、結婚紀念日戴。
- 手腕:左手戴一支 **Apple Watch SE,星光色(米白)運動錶帶,邊緣有點髒**(太太選的顏色)。
  **錶帶的位置有一圈比較白的皮膚。**

### 3.4 標誌性特徵(Distinguishing Marks)

1. **右眉中段的痣,眉毛從上面長過去。** 正臉或右側臉近景才看得到。**臉的第一辨識點。**
2. **右手食指第二指節的白色燙疤。** 手部近景必須有。**手的第一辨識點。**
3. **自己推的短髮,後腦勺右下一塊不平。** 背影鏡頭用。
4. **左肩略低(抱小孩都抱左邊)+ 星光色錶帶。** 站姿與穿短袖時看得出來。

### 3.5 右耳的 AirPods(狀態指示器)

- **他不戴眼鏡。** 視力 0.9 / 1.0,體檢說輕微近視,不用矯正。
- 他的狀態指示器是**右耳那一顆 AirPods**(哄睡時只戴右耳,所以右耳永遠先沒電,見 `02 § 9`)。

| 右耳狀態 | 代表什麼 | 用在什麼內容 |
|---|---|---|
| **右耳塞著一顆** | 在聽東西但隨時要回應人(哄睡、開車、等小兒科叫號) | 夜裡、通勤、週末 |
| 兩耳都有 | 在公司專心寫程式 | 上班 |
| 兩耳都沒有 | 跟家人在一起、有人在跟他講話 | 家裡、岳家 |
| **拿在手上轉** | 在想事情 | 想 bug、等 log |

### 3.6 表情庫(九宮格,給生圖用)

| 表情 | 描述 | 什麼時候出現 |
|---|---|---|
| **default(預設)** | 平、專注,嘴唇抿著,眉頭平,看著螢幕或物件 | 70% 的畫面 |
| **counting** | **右手舉起,用手指數步驟**(一、二、三),眼睛往左上 | 解釋順序的時候 |
| **real smile** | **閉嘴笑,細長的眼睛瞇成一條線,兩頰往上推** | 女兒早上叫他、bug 重現 |
| **laugh** | **低頭,鼻子短短出氣一聲,肩膀動一下** | 跟學弟、跟太太 |
| **deadpan** | 眼神完全平,嘴角不動,點一下頭 | 聽到「我只是改了一個小地方」 |
| **quietly pleased** | 眉毛抬高一點,嘴角往一邊動,**右手在桌下握一下拳** | bug 重現了 |
| **tired** | **手掌從額頭往下搓過整張臉,停在下巴** | 夜裡、女兒生病、on-call |
| **listening** | 頭偏一點,眼睛往下看,**右手食指按著右耳的 AirPods** | Teams 會議、小兒科叫號 |
| **checking** | **雙手拍三下口袋:左褲袋、右褲袋、帽 T 前口袋** | 出門前 |

**❌ 絕對不出現的表情:** 比讚、比 YA、對鏡頭眨眼、商務照的自信微笑、
雙手抱胸的「工程師主管」姿勢、任何男性時尚雜誌的表情。

### 3.7 聲音(給 Libai 的口播與畫外音)

| 參數 | 設定 |
|---|---|
| 音高 | **中低音**,基頻約 **110–130 Hz**。不渾厚、不播音腔 |
| 語速 | **畫外音約每分鐘 210 字;平常講話約 230 字。** 解釋事情時會變慢 |
| 口音 | **台灣國語,南部人。** ㄓㄔㄕ 捲得不明顯,句尾偶爾帶一點台語的語調。累的時候更明顯 |
| 音色 | 平、乾淨、有一點悶(像在會議室講話)。**夜裡錄的會壓低音量,因為女兒在睡** |
| 特徵 | **句子短,常用「重點是」「對」「就是」。** 列點時會真的說「第一、第二」 |
| 台語 | 跟爸媽講台語。內容裡偶爾一個詞:「無法度」「好啦」。**不刻意,不當笑點** |
| 客家話 | **不會講。** 偶爾轉述岳母或女兒的一兩個詞,而且會念錯,他自己知道 |
| 笑聲 | **鼻子短短出氣一聲「哼」**,或低頭肩膀動一下 |
| 填充詞 | 「就是」(多)、「對」(句尾確認,多)、「然後」(中)、「欸」(少) |
| 情緒起伏 | **低。** 好笑的時候語氣更平,這是他的笑點來源 |
| 絕不出現 | 「哈囉大家好」「各位爸爸們」、播報腔、業配腔的上揚尾音、中國腔兒化音、「超級無敵」 |

### 3.8 鏡頭前的肢體習慣

- **出門前拍三下口袋:左褲袋(鑰匙)、右褲袋(手機)、帽 T 前口袋(AirPods 盒)。** 一定是這個順序。
- **用手指數步驟。** 解釋任何事都會舉起右手開始數。
- **拔插頭一定捏著插頭,先關開關。** 任何有插頭的畫面都要照這個順序演。
- 站起來之前**用指節敲兩下桌面**。
- **手機拿在左手,在胸口的高度。** 右手留著(以前留給滑鼠,現在留給女兒)。
- 抱小孩、扛東西一律用左邊。**(畫面裡不出現小孩,但他左手提東西、右手空著的姿勢會出現)**
- 想事情的時候**把右耳的 AirPods 拿下來在指間轉**,轉很久。
- 寫白板的時候**把白板筆的蓋子咬在嘴裡**。
- **他會看鏡頭,但很快就看回手上的東西。** 像在跟一個同事講話,不是在對鏡頭表演。

### 3.9 拍照與自拍行為(重要,決定內容的視覺調性)

| 行為 | 設定 |
|---|---|
| **自拍** | **幾乎沒有。** 一年三四次,而且是全家合照時他拿手機(他的臉在畫面邊緣) |
| 出現在畫面裡的方式 | **手、手腕、背影、側面、鏡子或螢幕倒影。** TikTok 約 10% 露臉 |
| 拍什麼 | **物件。** 白板、防護盒、號碼牌、門框刻度、長尾夾、風箏、溪邊步道的推車輪子 |
| 構圖 | **正面、置中、水平,像在拍 bug 的證據照。** 他會把東西擺正再拍。太太說他拍什麼都像在報修 |
| 光線 | **有什麼用什麼,晚上會開閃光燈**(他覺得看得清楚比較重要) |
| 後製 | **零。** 不加濾鏡、不調色、不裁 |
| 器材 | iPhone。**二手相機在防潮盒裡,一個月拿出來一次** |

> **這一條對 Libai 與 Ivy 是硬約束:這個帳號的視覺主體是「物件與手」,臉是配角,小孩不入鏡。**
> 需要臉的時候(TikTok 少數片段、商業素材)才用完整人像,而且臉要符合第五節的不可變錨。
> **構圖要正、光線要平、像證物照。** 這是他跟其他工程師帳號、育兒帳號最大的差別。

---

## 四、服裝系統(四套 + 變體)

外型必須對得起 `02 § 3` 的收入與 `02 § 7` 的消費行為:
**他自己身上的東西幾乎都是平價、穿到舊;女兒的汽座是全家最貴的單品。**

### 4.1 Workday(竹科上班)

```
- 深灰色或墨綠色素面帽 T(平價快時尚,NT$590–990),**沒有任何 logo 或字**,帽繩一邊比較短
  裡面一件白色或灰色圓領 T
- 深藍色直筒牛仔褲,膝蓋有一點褪色
- 灰色慢跑鞋(看不到品牌),鞋帶有點舊
- 辦公室冷氣很強,帽 T 一年穿十個月
- 公司識別證**放在褲子口袋,不掛脖子**(刷完門禁就收起來,保密習慣)
- Apple Watch SE 星光色錶帶
- 右耳一顆 AirPods(通勤時)
← 竹科辦公室的樣子之一。不時尚,不邋遢
```

### 4.2 Home Evening(家裡的晚上)

```
- 灰色舊 T 恤(2019 年公司運動會發的,**胸前的字已經褪到看不清楚**,生圖時不要有字)
- 黑色運動短褲
- 光腳,或灰色室內拖鞋
- 手腕上的 Watch 拿掉了(在床頭充電),**留下一圈比較白的皮膚**
- 右耳 AirPods(哄睡時)
```

### 4.3 Weekend Dad(週末、溪邊、南寮、小兒科)

```
- 卡其色工作外套(九降風季),拉鍊拉到一半
- 灰色或白色素 T
- 黑色運動長褲或短褲
- 黑色拖鞋(夏天)或灰色休閒鞋(秋冬)
- **黑色後背式媽媽包**(側袋插著一瓶水跟一包濕紙巾)
- 推著一台摺疊推車,**推車的遮陽篷永遠放下來**(畫面裡看不到車裡)
- Watch
```

### 4.4 Family Occasion(屏東、岳家過年、婚禮)

```
- 白色長袖襯衫,袖子捲到前臂
- 深色休閒長褲
- 黑色休閒皮鞋(一雙,婚禮那年買的)
- **這一天戴婚戒**
- 頭髮前一天晚上剛推過
```

### 4.5 配件(全部,不要再加)

| 配件 | 細節 |
|---|---|
| 錶 | **Apple Watch SE(44 公釐),星光色運動錶帶,邊緣有點髒** |
| 耳機 | **AirPods Pro 2,右耳那顆常常單獨塞著** |
| 戒指 | **平日不戴。** 婚戒在床頭小瓷盤,只有特定場合 |
| 識別證 | 黑色掛繩、透明卡套,**放在褲子口袋,不入鏡** |
| 包 | 平日:黑色電腦後背包(公司配的,無 logo);週末:黑色媽媽包 |
| 車鑰匙 | 一般的鑰匙,**掛著一個女兒幼兒園做的紙黏土小吊飾**(看不出是什麼,他說是鯨魚) |
| 手機殼 | 黑色矽膠,邊角磨白 |
| **不戴的** | 眼鏡、項鍊、手鍊、耳環、名錶、名牌包、任何 logo 很大的東西、運動品牌的大字 |

---

## 五、Visual Identity Rules(長期一致性規則)

**這一節是煞車。每次生圖前對照。**

### 五個不可變的錨(Immutable Anchors)

1. **右眉中段的痣,眉毛從上面長過去**,露臉就要有
2. **圓臉、單眼皮細長眼、兩頰有肉**,不准變男模臉、不准變尖下巴、不准變雙眼皮大眼
3. **自己推的短髮(兩側 6 mm、頂 1.5 cm),全黑、沒有白髮**,不准油頭、不准變長
4. **不戴眼鏡**,任何畫面加了眼鏡就等於換人
5. **右手食指第二指節的白色燙疤 + 中等微胖、左肩略低**,不准變健身體型

### 十條禁止漂移(Banned Drift)

| # | 不可以變成 | 為什麼 |
|---|---|---|
| 1 | 男模、韓系男神、健身網紅 | 違反 `06 § 六` 的身體設定,也是 AI 最容易滑過去的方向 |
| 2 | 竹科新貴:名錶、進口車、名牌、西裝 | 違反 `02 § 3` 與 `06 § 三` |
| 3 | 宅男刻板:格子襯衫、油膩、凌亂、一桌泡麵 | 違反 `01 § 十一`,另一個極端 |
| 4 | 桌面改造網紅:乾淨無線的桌、RGB 燈、螢幕懸臂 | **他的書房桌被全家占用**,違反 `04 § 16` |
| 5 | **同批人物的外型:眼鏡、眉疤、鬢角白髮、polo、素面婚戒、恐龍貼紙** | **撞型。** 見本檔開頭與 `00 § 四` 第 13 項 |
| 6 | 簡體字招牌、中國或日本街景 | **他在竹北與竹科**,招牌是繁體 |
| 7 | 出現識別證、公司名、公司 logo | **保密**,而且他本人絕不會拍 |
| 8 | 出現可辨識的真實品牌 logo 或真人臉 | 法遵 |
| 9 | **出現小孩的臉、小孩全身、小孩身體特寫** | **合規優先 + 人設規則。** 女兒只能用物件表現 |
| 10 | 臉部特徵在不同圖之間變化 | 用同 seed + 完整外貌段解決 |

### 連續性檢查表(每次出圖後跑)

- [ ] 右眉中段的痣在嗎(如果露臉)
- [ ] 是圓臉、單眼皮細長眼嗎,有沒有被修成男模臉或雙眼皮
- [ ] **有沒有被自動加上眼鏡**
- [ ] 頭髮是不是自己推的短髮、全黑,有沒有被加上白髮
- [ ] 右手食指的燙疤在嗎(如果有手部近景)
- [ ] 身材是不是中等微胖,有沒有被修成健身體型
- [ ] 有沒有出現名錶、名牌、大 logo、戒指(除了 4.4 的場合)
- [ ] **識別證有沒有入鏡**(不准)
- [ ] **畫面裡有沒有任何小孩(包括遠處、倒影、照片裡的照片)**
- [ ] 場景是不是台灣(繁體字、新大樓、園區、地下停車場)
- [ ] 色板有沒有跑掉(`#6FA8DC` 藍色只能是貼紙那麼小;`#D94141` 只能是一兩個小點)
- [ ] 手有沒有畫壞,線、插頭、長尾夾有沒有變形
- [ ] 有沒有出現亂碼中文、假 logo

---

## 六、生圖提示詞(英文,可直接使用)

### 6.1 Master character block(所有提示詞的共用段,不要改)

```
photorealistic documentary photograph, ordinary smartphone-quality image,
practical light only, slight noise, no retouching, visible skin texture and pores,

a 33-year-old Taiwanese man, 172cm, average build with a slightly soft belly,
left shoulder sitting slightly lower than the right,
round face with slightly full cheeks and a short chin,
single-lidded narrow dark brown eyes, calm flat gaze, faint under-eye shadows,
thick flat short eyebrows, a small 3mm dark mole in the middle of the right eyebrow
with brow hair growing over it,
medium nose with a rounded tip, neutral mouth with corners resting slightly down,
warm medium wheat skin (#C9A27E), both forearms the same tone,
light stubble shadow on the jaw,
very short black hair clipped at home with electric clippers, sides about 6mm,
top about 1.5cm, a slightly uneven patch at the lower right of the back of the head,
no grey hair, NO GLASSES,
large hands with short flat-cut nails, a small pale 0.8cm burn scar on the outer side
of the right index finger's middle knuckle, no rings,
a smartwatch with a cream-coloured sport band on the left wrist,
a single wireless earbud in his right ear,

focused neutral expression, lips lightly pressed, brows relaxed,
looking at an object or a screen, not at the camera,

colour palette: hoodie charcoal #3A3D42, new-build wall off-white #E6E3DC,
monsoon grey #8C9196, whiteboard white #F4F4F0,
with a tiny accent of sticker blue #6FA8DC under 5% of the frame
and at most one or two tiny red pilot lights #D94141
```

### 6.2 Portrait(頭肩,4:5)

```
[MASTER CHARACTER BLOCK]

head and shoulders, three-quarter angle from his right side so the eyebrow mole is visible,
wearing a plain charcoal hoodie with no logo or text over a white crew-neck t-shirt,
one hoodie string shorter than the other,
standing in a plain corridor of a new apartment building, flat cool fluorescent light,
shallow depth of field f/2.8, no glasses, no badge, no lanyard,

--ar 4:5
```

### 6.3 Full body(全身,週末推推車,9:16)

```
[MASTER CHARACTER BLOCK]

full body, walking on a paved riverside path in Zhubei on a windy grey autumn afternoon,
wearing a khaki work jacket half zipped over a grey t-shirt, black track pants,
grey casual shoes, a black diaper backpack on his back with a water bottle in the side pocket,
pushing a folding stroller with the sun canopy pulled fully down so the seat is hidden,
NO CHILD VISIBLE ANYWHERE IN THE FRAME,
new residential high-rises in the background, wind bending the grass,
flat overcast light,

--ar 9:16
```

### 6.4 Hands / detail(招牌鏡頭,1:1)

```
photorealistic close-up photograph taken straight-on with a phone flash, slightly harsh,

close-up of a man's large hands with short flat nails and a small pale burn scar on the
right index finger's middle knuckle, no rings,
one hand writing a numbered list with a black whiteboard marker on a white A4 whiteboard
hanging on the back of a bedroom door, the other hand flat against the door,
no readable text, no logos,

--ar 1:1
```

### 6.5 Home desk at night / 桌子 B(4:5)

```
[MASTER CHARACTER BLOCK]

sitting on the edge of a chair at an electric standing desk in a small study room of a new
Taiwanese apartment at 11pm, grey faded t-shirt with no readable print,
rubbing his face downward with one palm, the earbud in his right ear,
a black desktop with a laptop, a 27-inch monitor, a blue folder and sticky notes,
a box of crayons, a small plastic toy whale, a baby-monitor parent screen glowing grey-green,
a white electric nasal aspirator charging, three black binder clips clamped on the desk edge
holding cables so they do not hang down,
under the desk a white plastic power-strip safety box with one tiny red light leaking
through the gap, a small blue whale sticker stuck crooked on its lid,
warm 3000K ceiling light mixed with cool monitor glow,
NO CHILD IN THE FRAME, NO GLASSES,

--ar 4:5
```

### 6.6 Bedroom-door whiteboard(主錨點,4:5)

```
photorealistic photograph taken straight-on with a phone flash, slightly harsh,

a white A4 whiteboard hanging from a small hook on the back of a white bedroom door
in a Taiwanese apartment, handwritten in neat upright black marker strokes in traditional
Chinese, a short title at the top left, a tally mark of seven strokes in the top right corner
(the Chinese tally character 正 plus two strokes), five numbered lines below, the last line clearly written,
a black marker hanging on a string beside it, a child's crayon drawing taped below it,
the door slightly ajar, warm hallway light, no people,

--ar 4:5
```

> **注意:** AI 生中文字常是亂碼。這張若要用在商業素材,**白板上的字一律後製上**,
> 內容照 `03 § 8-1`:「睡前(右上角正字七筆)/ 1. 選睡衣 / 2. 刷牙 + 火金姑 / 3. 書(兩本)/ 4. 關燈 / 5. 叫媽媽」。

### 6.7 Office / 桌子 A(16:9)

```
[MASTER CHARACTER BLOCK]

wide shot of an open-plan office in a science-park building, rows of grey desks with
120cm partitions, he sits at his desk in a dark green plain hoodie, both earbuds in,
two 24-inch monitors showing dense scrolling log text that is not readable,
a small circuit test board on an acrylic stand, a USB-to-serial cable, an anti-static wrist strap
hanging on the partition, a child's purple crayon drawing taped to the partition,
a black desk mat, a stainless tumbler,
flat cool fluorescent light, NO LOGOS, NO COMPANY NAME, NO READABLE TEXT, NO ID BADGE,

--ar 16:9
```

### 6.8 Expression sheet(九宮格)

```
[MASTER CHARACTER BLOCK]

nine-panel expression sheet of the same man, identical lighting and framing in every panel,
head and shoulders, plain off-white background, no glasses, charcoal hoodie:
1 neutral focused with lips lightly pressed,
2 counting steps on the fingers of his raised right hand with eyes up to the left,
3 a closed-mouth smile with narrow eyes squeezed into lines and cheeks pushed up,
4 laughing quietly with head down and a short exhale through the nose,
5 deadpan with completely flat eyes and a small nod,
6 quietly pleased with brows slightly raised and one corner of the mouth moving,
7 tired, dragging one palm down over his face and stopping at the chin,
8 listening with head slightly tilted and his right index finger pressing the earbud in his right ear,
9 patting his trouser pocket with both hands as if checking for keys,

--ar 1:1
```

### 6.9 影片模特提示詞(給 Libai,含行為)

```
[MASTER CHARACTER BLOCK]

MOTION / BEHAVIOUR:
before leaving he pats three pockets in a fixed order: left trouser pocket, right trouser
pocket, the front pouch of his hoodie. when he explains anything he raises his right hand and
counts steps on his fingers. when unplugging anything he first switches the device off, then
pinches the plug body (never pulls the cable), then waits a beat before touching it again.
before standing up he knocks twice on the desk with his knuckles. he holds his phone in his
left hand at chest height. when thinking he takes the earbud out of his right ear and turns it
between his fingers. when writing on a whiteboard he holds the marker cap in his teeth.
he glances at the camera briefly, like talking to a colleague, and goes back to the object in
his hands. NO CHILD APPEARS IN ANY SHOT; a child's presence is shown only through objects.

VOICE: mid-low male voice, fundamental around 120 Hz, flat and clean, slightly muffled like
someone in a meeting room, southern Taiwanese Mandarin accent with soft retroflexes,
around 210 Chinese characters per minute in voice-over, slower when explaining steps,
lowers his volume at night because someone is asleep, says "first, second" when listing,
no influencer greeting, no broadcast tone, no rising sales intonation.

CAMERA: handheld phone or locked-off on a small tripod, straight-on and centred,
eye level or top-down, flat practical light, sometimes phone flash.
```

---

## 七、外型與人設的一致性驗算

**每一條外型設定都要對得起前面的檔案。這一節是自我檢查。**

| 外型設定 | 對應到 | 是否成立 |
|---|---|---|
| 微胖、圓臉、兩頰有肉 | `06 § 六` 2024 年 68 → 75 kg | ✓ |
| 左肩略低 | `06 § 六` 抱小孩都抱左邊 | ✓ |
| 左肩略低 | `05` 抱小孩都抱左邊 | ✓ |
| 右手食指的燙疤 | `03 § 3-1` 2012 年第一塊燒掉的板子 | ✓ |
| 自己推的短髮 | `02 § 7` 自己的東西能省就省、`06 § 六` 沒時間 | ✓ |
| 不戴眼鏡 | `06 § 六` 體檢輕微近視不用矯正 | ✓ |
| 右耳一顆 AirPods | `02 § 9` 哄睡時只戴右耳 | ✓ |
| 晚上的鬍渣陰影 | `06 § 四` 早上刮、晚上九點後 | ✓ |
| 平價帽 T、舊 T、穿到舊 | `02 § 7` 自己的東西能用就好 | ✓ |
| Apple Watch SE | `02 § 9` 抱小孩看不到手機 | ✓ |
| 平日不戴婚戒 | `06 § 一` 主臥床頭的小瓷盤 | ✓ |
| 識別證不入鏡 | `06 § 二` 保密習慣 | ✓ |
| 二手汽油小休旅,不是進口車 | `06 § 三` | ✓ |
| 證物照式的構圖、開閃光 | `03 § 5-1` 重現與紀錄的習慣 | ✓ |
| 很少自拍,小孩不入鏡 | `04 § 13` E 值 38、`02 § 17` | ✓ |

**沒有一條外型設定是憑空的。**

---

## 八、給下游角色的最小可用摘要

**Libai(影片):** 讀 3.7 聲線、3.8 肢體、6.9 影片提示詞、五個不可變錨。**小孩不入鏡是硬規則。**
**Ivy(素材):** 讀 6.1 master block、6.4 手部、6.6 白板、五個不可變錨、十條禁止漂移。
**注意:** 這個人物若出現在商業素材上,揭露義務見 `08_social_persona.md` 第九節。
**產品還沒上市(嘖嘖預定 2027 年 6 月中),任何畫面都不得出現 SPACION 桌面充電站本體或渲染圖。**

---

## 九、Seed 紀錄(生圖後回填)

| 用途 | Seed | 模型 | 日期 | 備註 |
|---|---|---|---|---|
| portrait | *(本輪未生圖)* | | | |
| full_body_weekend | *(本輪未生圖)* | | | |
| hands_whiteboard | *(本輪未生圖)* | | | |
| desk_night | *(本輪未生圖)* | | | |
| door_whiteboard | *(本輪未生圖)* | | | |
| expression_sheet | *(本輪未生圖)* | | | |

> **本輪任務未包含生圖。** Owner 這次要的是人物檔,seed 表照指示留空。
> 需要出圖時走 `gen-image` skill,把 6.1 的 master block 帶進去,生完把 seed 回填到這張表。

---


---

## 變更紀錄(跨人物撞型修正)

| 版本 | 日期 | 改了什麼 | 為什麼 |
|---|---|---|---|
| v1.2 | 2026-10-20 | 跨人物撞型修正:睡前流程的版次由「Rev A–G」改為「第一稿–第七稿」+ 白板右上角的正字記號(版本號當生活語言保留給 `persona_tw_02b`);白板內容、步驟、日期不變;口頭禪「先講結論」改為「一句話版:」(「先講結論:」保留給 `persona_tw_06`);拿掉「左前臂比右前臂深」(開車曬黑的左前臂是 `persona_tw_06` 的視覺錨) | 主 session 統一 QA:第二批平行生成,與 `02b`、`03`、`06` 仍有版本語言、家族事件、口頭禪、外型撞在一起 |

*檔案版本:v1.2 — 2026-10-20 跨人物撞型修正(先前:2026-10-20 建立)*
