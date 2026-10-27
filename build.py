#!/usr/bin/env python3
"""Inline the SUIT font into src/index.html and write the two builds.

  index.html            standalone page served by GitHub Pages
  .artifact/index.html  fragment for the claude.ai artifact (its viewer adds the document shell)

Usage: python3 build.py
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent

SHELL_HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="아이디어를 말풍선으로 띄우고, 비슷한 것끼리 묶고, 고른 것만 프롬프트로 정리하는 브레인스토밍 도구">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect x='4' y='10' width='56' height='38' rx='19' fill='%231973DD'/%3E%3Cpath d='M14 44 L8 56 L26 46 Z' fill='%231973DD'/%3E%3C/svg%3E">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}[hidden]{display:none!important}</style>
"""


def main():
    src = (ROOT / "src/index.html").read_text(encoding="utf-8")
    font = base64.b64encode((ROOT / "fonts/SUIT-SemiBold.woff2").read_bytes()).decode()
    assert src.count("__SUIT_WOFF2__") == 1, "font placeholder missing"
    page = src.replace("__SUIT_WOFF2__", font)

    head, sep, body = page.partition('<div class="app">')
    assert sep, "app root not found"
    standalone = SHELL_HEAD + head + "</head>\n<body>\n" + sep + body + "</body>\n</html>\n"
    (ROOT / "index.html").write_text(standalone, encoding="utf-8")

    (ROOT / ".artifact").mkdir(exist_ok=True)
    (ROOT / ".artifact/index.html").write_text(page, encoding="utf-8")
    print("built index.html and .artifact/index.html")


if __name__ == "__main__":
    main()
