"""生圖。主力平台 AIRiter,DMXAPI 保留為備援。

  python gen.py --prompt "..." --out out.png [--ref 產品圖.jpg] [--ref 參考圖.jpg]
                [--ratio 4:3] [--res 2K] [--provider airiter] [--dry-run]

  python gen.py --batch prompts.json --outdir ./imgs   # 一次多張

**預設會實際呼叫付費 API。** 先用 --dry-run 確認 payload 再實跑。
金鑰讀環境變數,不寫死、不印出:
  AIRITER_API_KEY  (預設平台)
  DMXAPI_API_KEY   (--provider dmxapi 時才需要)
"""
import argparse, base64, io, json, mimetypes, os, sys, time, uuid
import urllib.error, urllib.request

# ── AIRiter ────────────────────────────────────────────────────────────────
# 非同步:submit 拿 out_task_id,再輪詢 query 取圖。
AIR_SUBMIT = "https://aireiter.com/api/openapi/submit"
AIR_QUERY = "https://aireiter.com/api/openapi/query"
AIR_MODELS = {
    "seedreampro": "seedream_v5_pro",     # 預設。文字渲染正確,且支援自訂 size
    "seedreamlite": "seedream_v5_lite",   # 便宜,但畫面上的英文會拼錯,勿用於帶文案的圖
}
# aspect_ratio 只吃這幾種。Pro 另有 size 可指定任意尺寸,所以 A+ 版位優先走 size。
AIR_RATIOS = ["1:1", "3:2", "2:3", "4:3", "3:4", "16:9", "9:16", "21:9"]
AIR_FALLBACK = {
    "5:2": "21:9", "2:1": "16:9", "61:25": "21:9",
    "5:3": "16:9", "15:8": "16:9", "15:7": "21:9",
    "97:60": "16:9", "4:5": "3:4", "5:4": "4:3",
}
# size 限制:寬高皆為 16 的倍數,總像素 921600 ~ 4194304
PX_MIN, PX_MAX = 921600, 4194304


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def exact_size(ratio):
    """把 "5:2" 這種比例換成合法的 WxH(16 倍數、像素數在範圍內),取最大可用的。

    Pro 支援 size,所以 A+ 那些 aspect_ratio 清單裡沒有的版位可以精準命中,
    不必退到 21:9 再手動裁。
    """
    try:
        a, b = [int(x) for x in ratio.split(":")]
    except Exception:
        return None
    if a <= 0 or b <= 0:
        return None
    g = gcd(a, b)
    a, b = a // g, b // g
    best = None
    for k in range(1, 400):
        w, h = 16 * a * k, 16 * b * k
        px = w * h
        if px > PX_MAX:
            break
        if px >= PX_MIN:
            best = (w, h)
    return "%dx%d" % best if best else None

# ── DMXAPI(備援)──────────────────────────────────────────────────────────
DMX_BASE = "https://www.dmxapi.cn"
DMX_MODELS = {
    "seedreampro": "doubao-seedream-5-0-pro-260628",
    "seedream": "doubao-seedream-5.0-lite",
    "wan": "wan2.7-image",
}
DMX_SIZE = {
    "1:1": "2048x2048", "4:3": "2304x1728", "3:4": "1728x2304",
    "16:9": "2560x1440", "9:16": "1440x2560", "3:2": "2496x1664",
    "2:3": "1664x2496", "4:5": "1856x2320", "5:4": "2320x1856",
    "5:2": "2560x1024", "97:60": "2328x1440", "61:25": "2440x1000",
    "2:1": "2560x1280", "5:3": "2400x1440", "15:8": "2400x1280",
    "15:7": "2520x1176",
}


def key(name):
    k = os.environ.get(name)
    if not k:
        sys.exit("缺少環境變數 %s。設定後重試,不要把金鑰寫進指令。" % name)
    return k


def as_data_url(path):
    """本機圖轉 data URL —— 平台的伺服器連不到你的本機路徑。"""
    ctype = mimetypes.guess_type(path)[0] or "image/jpeg"
    with open(path, "rb") as f:
        b = f.read()
    if len(b) > 10 * 1024 * 1024:
        sys.exit("參考圖 %s 超過 10MB,平台會拒收。" % os.path.basename(path))
    return "data:%s;base64,%s" % (ctype, base64.b64encode(b).decode())


def post(url, body, headers, timeout=300):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"),
        headers=headers, method="POST")
    try:
        return json.load(urllib.request.urlopen(req, timeout=timeout)), None
    except urllib.error.HTTPError as e:
        # 伺服器的錯誤訊息在 body 裡,不吐出來會讓人誤判成提示詞或尺寸的問題。
        return None, {"error": "HTTP %d" % e.code,
                      "body": e.read().decode("utf-8", "replace")[:500]}
    except (TimeoutError, urllib.error.URLError, ConnectionError) as e:
        return None, {"error": "network: %s" % e}


def save(url, out):
    """下載結果圖。CDN 常擋沒有 User-Agent 的請求,所以要帶,並重試兩次。"""
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    if url.startswith("data:"):
        data = base64.b64decode(url.split(",", 1)[1])
    else:
        last = None
        data = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Accept": "image/*,*/*",
                })
                data = urllib.request.urlopen(req, timeout=180).read()
                break
            except Exception as e:
                last = e
                time.sleep(2 * (attempt + 1))
        if data is None:
            raise RuntimeError("下載失敗(已重試 3 次): %s | url=%s" % (last, url[:160]))
    open(out, "wb").write(data)
    return len(data)


# ── AIRiter 實作 ───────────────────────────────────────────────────────────
def air_body(prompt, refs, ratio, res, model):
    mid = AIR_MODELS.get(model, model)
    params = {"prompt": prompt}
    # Pro 支援 size(與 aspect_ratio/resolution 互斥),用它精準命中 A+ 版位比例。
    sz = exact_size(ratio) if mid == "seedream_v5_pro" else None
    if sz:
        params["size"] = sz
        used = "size=%s (%s)" % (sz, ratio)
    else:
        used = ratio if ratio in AIR_RATIOS else AIR_FALLBACK.get(ratio, "1:1")
        params["aspect_ratio"] = used
        params["resolution"] = res
    if refs:
        params["image_url"] = [as_data_url(r) if os.path.exists(r) else r
                               for r in refs][:10]
    return {
        "model": mid,
        "params": params,
        "out_task_id": "tcc_%s" % uuid.uuid4().hex[:16],
    }, used


def air_generate(prompt, refs, ratio, res, model, out, dry, poll_max=180):
    body, used = air_body(prompt, refs, ratio, res, model)
    note = None
    if used != ratio and not used.startswith("size="):
        note = None if used.startswith("size=") else "%s 不支援,改用 %s,交付前需裁切" % (ratio, used)
    if dry:
        shown = json.loads(json.dumps(body))
        if "image_url" in shown["params"]:
            shown["params"]["image_url"] = "<%d 張參考圖,已轉 data URL>" % len(refs)
        shown["params"]["prompt"] = shown["params"]["prompt"][:120] + "…"
        return {"dry_run": True, "provider": "airiter", "payload": shown,
                "ratio_substituted": note}

    H = {"Authorization": "Bearer " + key("AIRITER_API_KEY"),
         "Content-Type": "application/json"}
    t0 = time.time()
    j, err = post(AIR_SUBMIT, body, H)
    if err:
        return dict(ok=False, provider="airiter", **err)
    tid = ((j or {}).get("data") or {}).get("out_task_id") or body["out_task_id"]

    # 輪詢:前 30 秒每 3 秒,之後每 5 秒
    waited = 0
    while waited < poll_max:
        gap = 3 if waited < 30 else 5
        time.sleep(gap)
        waited += gap
        q, qerr = post(AIR_QUERY, {"out_task_id": tid}, H, timeout=60)
        if qerr:
            # 輪詢逾時/暫時性錯誤不代表任務失敗(已提交、已計費),繼續輪詢。
            if waited >= poll_max - 5:
                return dict(ok=False, provider="airiter", task_id=tid, **qerr)
            continue
        d = (q or {}).get("data") or {}
        st = d.get("status")
        if st == "completed":
            outs = d.get("output") or []
            if not outs or not outs[0].get("url"):
                return {"ok": False, "provider": "airiter", "task_id": tid,
                        "error": "completed 但沒有 output url", "raw": json.dumps(d)[:300]}
            try:
                n = save(outs[0]["url"], out)
            except Exception as e:
                # 圖已經生成(也已計費),只是抓不下來 —— 把 url 交出去讓人手動存,
                # 不要讓例外把整批批次炸掉。
                return {"ok": False, "provider": "airiter", "task_id": tid,
                        "error": "圖已生成但下載失敗", "detail": str(e)[:300],
                        "image_url": outs[0]["url"], "credits": d.get("credits_used")}
            r = {"ok": True, "provider": "airiter", "out": out, "sizeKB": n // 1024,
                 "model": body["model"], "aspect_ratio": used,
                 "credits": d.get("credits_used"),
                 "tookSec": round(time.time() - t0, 1), "task_id": tid}
            if note:
                r["ratio_substituted"] = note
            return r
        if st == "failed":
            return {"ok": False, "provider": "airiter", "task_id": tid,
                    "error": "任務失敗", "raw": json.dumps(d)[:400]}
    return {"ok": False, "provider": "airiter", "task_id": tid,
            "error": "輪詢逾時 %d 秒,任務可能仍在跑" % poll_max}


# ── DMXAPI 實作(備援)─────────────────────────────────────────────────────
def dmx_generate(prompt, refs, ratio, model, out, dry):
    body = {"model": DMX_MODELS.get(model, model), "input": prompt,
            "size": DMX_SIZE.get(ratio, "2048x2048"), "output_format": "png",
            "response_format": "url", "watermark": False}
    if refs:
        imgs = [as_data_url(r) if os.path.exists(r) else r for r in refs]
        body["image"] = imgs[0] if len(imgs) == 1 else imgs
    if dry:
        shown = dict(body)
        if "image" in shown:
            shown["image"] = "<%d 張參考圖>" % len(refs)
        shown["input"] = shown["input"][:120] + "…"
        return {"dry_run": True, "provider": "dmxapi", "payload": shown}

    t0 = time.time()
    j, err = post(DMX_BASE + "/v1/responses", body,
                  {"Content-Type": "application/json",
                   "Authorization": key("DMXAPI_API_KEY")})
    if err:
        return dict(ok=False, provider="dmxapi", **err)
    urls = []

    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get("url"), str) and o["url"].startswith("http"):
                urls.append(o["url"])
            if isinstance(o.get("b64_json"), str):
                urls.append("data:image/png;base64," + o["b64_json"])
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(j)
    if not urls:
        return {"ok": False, "provider": "dmxapi", "error": "回應沒有圖片 url",
                "raw": json.dumps(j)[:400]}
    n = save(urls[0], out)
    return {"ok": True, "provider": "dmxapi", "out": out, "sizeKB": n // 1024,
            "model": body["model"], "tookSec": round(time.time() - t0, 1)}


def generate(prompt, refs, ratio, res, model, out, dry, provider):
    if provider == "dmxapi":
        return dmx_generate(prompt, refs, ratio, model, out, dry)
    return air_generate(prompt, refs, ratio, res, model, out, dry)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt")
    ap.add_argument("--out")
    ap.add_argument("--ref", action="append", default=[])
    ap.add_argument("--ratio", default="1:1")
    ap.add_argument("--res", default="2K", choices=["1K", "2K"])
    ap.add_argument("--model", default="seedreampro")
    ap.add_argument("--provider", default="airiter", choices=["airiter", "dmxapi"])
    ap.add_argument("--batch", help="JSON: [{prompt, out, ratio?, ref?}]")
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if a.batch:
        jobs = json.load(io.open(a.batch, encoding="utf-8"))
        res = []
        for i, j in enumerate(jobs, 1):
            o = j.get("out") or os.path.join(a.outdir, "img_%02d.png" % i)
            r = generate(j["prompt"], j.get("ref", a.ref), j.get("ratio", a.ratio),
                         j.get("res", a.res), j.get("model", a.model), o,
                         a.dry_run, j.get("provider", a.provider))
            r["index"] = i
            print(json.dumps(r, ensure_ascii=False))
            res.append(r)
        print(json.dumps({"summary": {"total": len(res),
                                      "ok": sum(1 for r in res if r.get("ok") or r.get("dry_run"))}},
                         ensure_ascii=False))
    else:
        if not a.prompt or not a.out:
            sys.exit("需要 --prompt 與 --out,或改用 --batch")
        print(json.dumps(generate(a.prompt, a.ref, a.ratio, a.res, a.model,
                                  a.out, a.dry_run, a.provider), ensure_ascii=False))
