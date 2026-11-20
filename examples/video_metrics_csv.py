#!/usr/bin/env python3
"""一批抖音视频的播放量导出成 CSV。抖音只给作者本人看播放数，这里每条视频读一次此刻的播放数和点赞数。

    python3 video_metrics_csv.py links.txt          # 只报价，不调用
    python3 video_metrics_csv.py links.txt --yes    # 真跑

links.txt 一行一条：视频链接（douyin.com/video/…）、分享短链（v.douyin.com/…）、App 复制的整段分享文字，
或作品 ID 都行。每条 $0.002，出错不收费；没取到的那条写进 CSV 的“没取到”一列，其余照常。
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from decimal import Decimal
from pathlib import Path

from dataxapi import Api, ApiError, need_key

SOURCE = "gh-douyin-api"
SIGN_UP = f"https://dataxapi.com/zh/signin/?button={SOURCE}"
PRICE = Decimal("0.002")  # 现价见 https://dataxapi.com/zh/apis/douyin/videos/metrics/


def target(line: str) -> dict:
    line = line.strip()
    if re.fullmatch(r"\d{15,20}", line):
        return {"id": line}
    return {"url": line}


def main() -> None:
    parser = argparse.ArgumentParser(description="抖音视频播放量导出成 CSV")
    parser.add_argument("links", help="一行一条视频链接或 ID 的文本文件")
    parser.add_argument("--out", default="douyin_metrics.csv")
    parser.add_argument("--yes", action="store_true", help="确认调用（不加只报价）")
    args = parser.parse_args()

    lines = [l for l in Path(args.links).read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"{len(lines)} 条视频：调用 {len(lines)} 次，最多 ${PRICE * len(lines)}，出错不收费。")
    if not args.yes:
        print("加 --yes 真跑。")
        return
    need_key(SIGN_UP)

    api = Api(SOURCE)
    columns = ["输入", "作品 ID", "播放", "点赞", "没取到"]
    with Path(args.out).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for n, line in enumerate(lines, 1):
            row = {"输入": line.strip()}
            try:
                item = api.call("douyin.videos.metrics", **target(line))["data"]["item"]
                metrics = item.get("metrics") or {}
                row.update({"作品 ID": item.get("id"), "播放": metrics.get("views"), "点赞": metrics.get("likes")})
            except ApiError as error:
                row["没取到"] = str(error)
            writer.writerow(row)
            print(f"  {n}/{len(lines)} {row.get('播放') if not row.get('没取到') else '没取到'}", file=sys.stderr)
    print(f"写好 {args.out}。实际花费 ${api.charged}。")


if __name__ == "__main__":
    main()
