#!/usr/bin/env python3
"""Match a need against the Sitewright craft library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "library" / "catalog.json"
GUILDS = ("games", "images", "video", "frontend", "data", "research", "web")


def tokenize(text: str) -> list[str]:
    text = text.lower().strip()
    parts = re.split(r"[\s,，、|/]+", text)
    return [p for p in parts if p]


def haystack(card: dict) -> str:
    bits = [
        card.get("id", ""),
        card.get("title", ""),
        card.get("problem", ""),
        card.get("when", ""),
        card.get("when_not", ""),
        " ".join(card.get("teaches") or []),
        " ".join(card.get("interaction") or []),
        " ".join(card.get("tags") or []),
        card.get("guild", ""),
    ]
    return " ".join(bits).lower()


def score(card: dict, terms: list[str]) -> int:
    blob = haystack(card)
    n = 0
    for term in terms:
        t = term.lower()
        if t in blob:
            n += 3 if t in (card.get("id") or "").lower() else 2
            if t in (card.get("title") or "").lower():
                n += 2
            tags = " ".join(card.get("tags") or []).lower()
            if t in tags:
                n += 1
    return n


def load() -> list[dict]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    return data["cards"]


def print_card(card: dict, points: int | None = None) -> None:
    prefix = f"[{points}] " if points is not None else ""
    print(f"{prefix}{card['id']}  ·  {card['title']}  ({card['guild']})")
    print(f"    问题：{card['problem']}")
    print(f"    何时：{card['when']}")
    print(f"    不用：{card['when_not']}")
    path = ROOT / "library" / card["file"]
    missing = "" if path.is_file() else "  （文件缺失）"
    print(f"    正文：{path}{missing}")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从 Sitewright 工艺库匹配方案。先匹配，再发明。"
    )
    parser.add_argument("query", nargs="*", help="关键词或一句话")
    parser.add_argument("--guild", choices=GUILDS, help="只搜一个行当")
    parser.add_argument("--list", action="store_true", help="列出全部卡片")
    parser.add_argument("-n", type=int, default=8, help="最多几条（默认 8）")
    args = parser.parse_args()

    cards = load()
    if args.guild:
        cards = [c for c in cards if c["guild"] == args.guild]

    if args.list or not args.query:
        if not args.query and not args.list:
            parser.print_help()
            print("\n例子：")
            print('  python3 scripts/match.py "分层 史料 传说"')
            print("  python3 scripts/match.py --guild video 循环")
            print("  python3 scripts/match.py --list")
            return 0
        print(f"{len(cards)} 张卡片\n")
        for card in cards:
            print_card(card)
        return 0

    terms = tokenize(" ".join(args.query))
    ranked = []
    for card in cards:
        n = score(card, terms)
        if n:
            ranked.append((n, card))
    ranked.sort(key=lambda x: (-x[0], x[1]["id"]))

    if not ranked:
        print("没有命中。换机制词再试（分层 / 配对 / 无声循环），或读 library/research/ 外出检索。")
        return 1

    print(f"查询：{' '.join(terms)}  ·  命中 {len(ranked)}，显示前 {min(args.n, len(ranked))}\n")
    for points, card in ranked[: args.n]:
        print_card(card, points)
    return 0


if __name__ == "__main__":
    sys.exit(main())
