#!/usr/bin/python3
"""Send a Markdown file to Telegram using HTML parse mode."""

import os
import sys
import markdown
import urllib.parse
import urllib.request


def send_html(chat_id: str, token: str, html: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "parse_mode": "HTML",
        "text": html,
    }).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as resp:
        resp.read()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: send_telegram.py <markdown_file>")
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        md_text = f.read()

    html_text = markdown.markdown(md_text)

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.stderr.write("Environment variables TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set\n")
        return 1

    send_html(chat_id, token, html_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

