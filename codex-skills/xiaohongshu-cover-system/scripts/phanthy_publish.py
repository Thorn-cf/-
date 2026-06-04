#!/usr/bin/env python3
"""Upload carousel images to Phanthy and create a post."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import struct
import sys
import urllib.error
import urllib.request
from pathlib import Path


API_BASE = "https://www.phanthy.com/api/v1"
ALLOWED_TAGS = {"小说", "游戏", "音乐", "动漫", "新闻", "图像", "代码", "视频", "科普", "生活", "娱乐"}


def request_json(method: str, url: str, api_key: str | None, payload: dict | None = None) -> dict:
    data = None
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code} from {url}: {body}") from exc


def put_file(upload_url: str, path: Path, content_type: str) -> None:
    req = urllib.request.Request(
        upload_url,
        data=path.read_bytes(),
        headers={"Content-Type": content_type},
        method="PUT",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as res:
            if not 200 <= res.status < 300:
                raise SystemExit(f"Upload failed with status {res.status}: {path}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Upload failed with HTTP {exc.code}: {body}") from exc


def image_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return struct.unpack(">II", data[16:24])
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        chunk = data[12:16]
        if chunk == b"VP8X":
            width = 1 + int.from_bytes(data[24:27], "little")
            height = 1 + int.from_bytes(data[27:30], "little")
            return width, height
    if data.startswith((b"GIF87a", b"GIF89a")):
        width = int.from_bytes(data[6:8], "little")
        height = int.from_bytes(data[8:10], "little")
        return width, height
    if data.startswith(b"\xff\xd8"):
        i = 2
        while i < len(data):
            while i < len(data) and data[i] == 0xFF:
                i += 1
            marker = data[i]
            i += 1
            if marker in (0xD8, 0xD9):
                continue
            length = int.from_bytes(data[i : i + 2], "big")
            if 0xC0 <= marker <= 0xC3:
                height = int.from_bytes(data[i + 3 : i + 5], "big")
                width = int.from_bytes(data[i + 5 : i + 7], "big")
                return width, height
            i += length
    raise SystemExit(f"Cannot determine image dimensions for {path}")


def content_type(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(path.name)
    if guessed == "image/jpg":
        return "image/jpeg"
    if guessed in {"image/png", "image/jpeg", "image/webp", "image/gif"}:
        return guessed
    raise SystemExit(f"Unsupported image content type for {path}")


def upload_image(api_key: str, path: Path) -> dict:
    ctype = content_type(path)
    size = path.stat().st_size
    if size <= 0:
        raise SystemExit(f"Empty file: {path}")
    width, height = image_size(path)
    payload = {"filename": path.name, "contentType": ctype, "size": size}
    share = request_json("POST", f"{API_BASE}/openclaw/file_share", api_key, payload)
    data = share.get("data") or {}
    upload_url = data.get("uploadUrl")
    public_url = data.get("publicUrl")
    if not upload_url or not public_url:
        raise SystemExit(f"Invalid file_share response for {path}: {share}")
    put_file(upload_url, path, ctype)
    return {"url": public_url, "aspectRatio": width / height, "path": str(path)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish a multi-image Phanthy post.")
    parser.add_argument("--api-key", default=os.environ.get("PHANTHY_API_KEY"))
    parser.add_argument("--title", required=True)
    parser.add_argument("--content", required=True)
    parser.add_argument("--cover-prompt", default=None)
    parser.add_argument("--tags", default="", help="Comma-separated Phanthy tags.")
    parser.add_argument("images", nargs="+", help="Local image files; first image is the cover.")
    args = parser.parse_args()

    if not args.api_key:
        raise SystemExit("Missing API key. Pass --api-key or set PHANTHY_API_KEY.")
    if len(args.title) > 200:
        raise SystemExit("Title must be at most 200 characters.")

    tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    invalid_tags = [tag for tag in tags if tag not in ALLOWED_TAGS]
    if invalid_tags:
        raise SystemExit(f"Invalid tags: {', '.join(invalid_tags)}")

    paths = [Path(p).expanduser().resolve() for p in args.images]
    for path in paths:
        if not path.exists():
            raise SystemExit(f"Image not found: {path}")

    uploaded = [upload_image(args.api_key, path) for path in paths]
    payload = {
        "title": args.title,
        "content": args.content,
        "coverImageUrl": uploaded[0]["url"],
        "images": [{"url": item["url"], "aspectRatio": item["aspectRatio"]} for item in uploaded[1:20]],
    }
    if args.cover_prompt:
        payload["coverPrompt"] = args.cover_prompt
    if tags:
        payload["tags"] = tags

    post = request_json("POST", f"{API_BASE}/openclaw/post", args.api_key, payload)
    result = {"success": post.get("success"), "post": post.get("post"), "uploaded": uploaded}
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
