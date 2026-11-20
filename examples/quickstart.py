#!/usr/bin/env python3
"""按关键词搜抖音视频，存成 CSV：文案、作者、点赞、评论、分享、收藏、发布时间、链接。

    python3 quickstart.py 露营装备 --pages 2          # 只报价，不调用
    python3 quickstart.py 露营装备 --pages 2 --yes    # 真跑

每页一次调用，$0.02 一页，出错不收费。--sort latest 按最新，popular 按最多点赞；
--within day / week / half_year 只要最近一段时间发的。
"""

from __future__ import annotations

import argparse
import csv
import sys
from decimal import Decimal
from pathlib import Path

from dataxapi import Api, ApiError, need_key

SOURCE = "gh-douyin-api"
SIGN_UP = f"https://dataxapi.com/zh/signin/?button={SOURCE}"
PRICE = Decimal("0.02")  # 现价见 https://dataxapi.com/zh/apis/douyin/videos/search/
COLUMNS = ["发布时间", "文案", "作者", "粉丝", "点赞", "评论", "分享", "收藏", "链接", "作品 ID"]


def main() -> None:
    parser = argparse.ArgumentParser(description="按关键词搜抖音视频")
    parser.add_argument("query", help="搜索词")
    parser.add_argument("--pages", type=int, default=1, help="取几页，每页一次调用")
    parser.add_argument("--sort", choices=["relevance", "latest", "popular"], default="relevance")
    parser.add_argument("--within", choices=["day", "week", "half_year"])
    parser.add_argument("--out", default="douyin_search.csv")
    parser.add_argument("--yes", action="store_true", help="确认调用（不加只报价）")
    args = parser.parse_args()

    print(f"搜“{args.query}”{args.pages} 页：最多调用 {args.pages} 次、${PRICE * args.pages}，出错不收费。")
    if not args.yes:
        print("加 --yes 真跑。")
        return
    need_key(SIGN_UP)

    api, rows, cursor = Api(SOURCE), [], None
    for page in range(args.pages):
        try:
            answer = api.call("douyin.videos.search", query=args.query, sort=args.sort, published_within=args.within, cursor=cursor)
        except ApiError as error:
            print(f"第 {page + 1} 页没取到：{error}（出错不扣费，已取到的照常保存）", file=sys.stderr)
            break
        for item in answer["data"]["items"]:
            author, metrics = item.get("author") or {}, item.get("metrics") or {}
            rows.append({
                "发布时间": item.get("published_at"),
                "文案": item.get("text"),
                "作者": author.get("name"),
                "粉丝": author.get("followers"),
                "点赞": metrics.get("likes"),
                "评论": metrics.get("comments"),
                "分享": metrics.get("shares"),
                "收藏": metrics.get("favorites"),
                "链接": item.get("url"),
                "作品 ID": item.get("id"),
            })
        cursor = (answer.get("page") or {}).get("next_cursor")
        if not cursor:
            break

    with Path(args.out).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"写好 {args.out}：{len(rows)} 条，调用 {api.calls} 次，实际花费 ${api.charged}。")


if __name__ == "__main__":
    main()
