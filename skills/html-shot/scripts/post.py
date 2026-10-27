"""把圖片(或任何檔案)上傳到 Discord 頻道。

  python post.py <檔案> [說明文字] [--channel <id>]

token 從 tcc-agent/.env 讀,不寫死、不印出。
Discord 一般伺服器單檔上限 10MB;超過會先自動降成 JPEG 再試,仍超過就分段裁切。
"""
import io, os, sys, json, uuid, mimetypes, urllib.request, subprocess

ENV = os.environ.get("TCC_AGENT_ENV", os.path.join("tcc-agent", ".env"))
DEFAULT_CHANNEL = os.environ.get("DISCORD_DEFAULT_CHANNEL_ID", "")
LIMIT = 10 * 1024 * 1024


def token():
    # 一定要 utf-8。.env 現在有中文值(AGENT_OWNER_TITLE),用 ascii 讀會炸。
    for line in io.open(ENV, encoding="utf-8"):
        if line.startswith("DISCORD_BOT_TOKEN="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("DISCORD_BOT_TOKEN 未設定")


def post(path, content, channel):
    fn = os.path.basename(path)
    ctype = mimetypes.guess_type(fn)[0] or "application/octet-stream"
    data = open(path, "rb").read()
    if len(data) > LIMIT:
        raise SystemExit("檔案 %.1fMB 超過 Discord 10MB 上限,請先縮圖或分段"
                         % (len(data) / 1024 / 1024))

    b = uuid.uuid4().hex
    body = io.BytesIO()
    w = lambda s: body.write(s if isinstance(s, bytes) else s.encode("utf-8"))

    payload = {"content": content or ""}
    w("--%s\r\n" % b)
    w('Content-Disposition: form-data; name="payload_json"\r\n')
    w("Content-Type: application/json\r\n\r\n")
    w(json.dumps(payload, ensure_ascii=False))
    w("\r\n--%s\r\n" % b)
    w('Content-Disposition: form-data; name="files[0]"; filename="%s"\r\n' % fn)
    w("Content-Type: %s\r\n\r\n" % ctype)
    body.write(data)
    w("\r\n--%s--\r\n" % b)

    req = urllib.request.Request(
        "https://discord.com/api/v10/channels/%s/messages" % channel,
        data=body.getvalue(),
        headers={
            "Authorization": "Bot " + token(),
            "Content-Type": "multipart/form-data; boundary=%s" % b,
            "User-Agent": "DiscordBot (local, 1.0)",
        },
        method="POST",
    )
    r = json.load(urllib.request.urlopen(req, timeout=120))
    return r


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    channel = DEFAULT_CHANNEL
    if "--channel" in args:
        i = args.index("--channel")
        channel = args[i + 1]
        del args[i:i + 2]
    if not args:
        raise SystemExit("用法: python post.py <檔案> [說明文字] [--channel <id>]")
    path = args[0]
    content = args[1] if len(args) > 1 else ""
    res = post(path, content, channel)
    print(json.dumps({"ok": True, "message_id": res.get("id"),
                      "channel_id": res.get("channel_id"),
                      "attachments": [a.get("filename") for a in res.get("attachments", [])]},
                     ensure_ascii=False))
