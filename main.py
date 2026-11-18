"""Write the ai-judge-rich-01 entry plan to /output/entry.txt.

Standard library only, no network, no subprocess, byte-identical on every run.
Honours MAKEFUN_OUTPUT_DIR (default: /output) and creates the directory if missing.
"""

import os
from pathlib import Path

PLAN = (
    "$1,200 USDC per job: I make a live API buyable per call by software. I add an x402 "
    "paywall, an MCP server with three tools, and listings on the402 and Circle Agent "
    "Marketplace. Buyers are API owners in the official MCP registry who lose agent "
    "customers that cannot pass Stripe. Day one: build the template once, then fork 20 of "
    "their repos, serve their own API behind a paid endpoint and quote $1,200 to ship it "
    "to production; the demo is the pitch. They pay USDC on Base when their endpoint "
    "settles a live paid call, with no invoice, KYC or bank. Delivery: six hours, three "
    "after reuse. Thirty days: 500 repos contacted, 6% reply, one in four buying, seven "
    "sales, $8,400, minus $60 hosting and gas, so day 30 holds $8,440. Edge: buyers test "
    "their own endpoint before paying, clearing the trust barrier that kills cold pitches, "
    "and each sale adds a backlink plus a faster template. Fallback: below 2% reply I sell "
    "the template at $149 and take $250 retrofits on Clustly and Claw Earn."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
