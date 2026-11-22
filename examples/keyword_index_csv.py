#!/usr/bin/env python3
"""抖音指数（巨量算数）导出成 CSV：1 到 5 个关键词，每天一行的搜索指数和综合指数。

    python3 keyword_index_csv.py 咖啡 露营 --since 2026-10-01 --until 2026-10-31          # 只报价，不调用
    python3 keyword_index_csv.py 咖啡 露营 --since 2026-10-01 --until 2026-10-31 --yes    # 真跑

一次调用最多 5 个词，$0.006 一次，出错不收费。指数是平台算出的热度分，不是搜索次数；
日期是中国时间（UTC+8）的自然日。平台每天的数晚一到两天才出，还没出的日子是空的，不会写成 0。
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
PRICE = Decimal("0.006")  # 现价见 https://dataxapi.com/zh/apis/douyin/index/keywords/history/?ref=gh-douyin-api


def main() -> None:
    parser = argparse.ArgumentParser(description="抖音指数（巨量算数）导出成 CSV")
    parser.add_argument("keywords", nargs="+", help="1 到 5 个关键词")
    parser.add_argument("--since", required=True, help="开始日期，如 2026-10-01")
    parser.add_argument("--until", required=True, help="结束日期，如 2026-10-31")
    parser.add_argument("--out", default="douyin_index.csv")
    parser.add_argument("--yes", action="store_true", help="确认调用（不加只报价）")
    args = parser.parse_args()
    if len(args.keywords) > 5:
        sys.exit("一次最多 5 个关键词。")

    print(f"{len(args.keywords)} 个词，{args.since} 到 {args.until}：调用 1 次，最多 ${PRICE}，出错不收费。")
    if not args.yes:
        print("加 --yes 真跑。")
        return
    need_key(SIGN_UP)

    api = Api(SOURCE)
    try:
        answer = api.call("douyin.index.keywords.history", keywords=args.keywords, since=args.since, until=args.until)
    except ApiError as error:
        sys.exit(f"没取到：{error}（出错不扣费）")

    rows = []
    for item in answer["data"]["items"]:
        for point in item.get("points") or []:
            rows.append({
                "日期": (point.get("date") or "")[:10],
                "关键词": item.get("keyword"),
                "搜索指数": point.get("search_index"),
                "综合指数": point.get("composite_index"),
            })
    missing = set(args.keywords) - {item.get("keyword") for item in answer["data"]["items"]}
    with Path(args.out).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["日期", "关键词", "搜索指数", "综合指数"])
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: (r["关键词"] or "", r["日期"])))
    print(f"写好 {args.out}：{len(rows)} 行。实际花费 ${api.charged}。")
    if missing:
        print(f"平台没收录这些词：{'、'.join(sorted(missing))}")


if __name__ == "__main__":
    main()
