#!/usr/bin/env python3
"""Zero-rewrite adoption: keep the official `openai` client, change one line.

Point `base_url` at the Kimss OpenAI-compatible endpoint and pass your Kimss
key. Existing OpenAI code becomes governed traffic - identity, audit trail,
and kill switch apply without touching your call sites.

Env: KIMSS_API_KEY (required), KIMSS_MODEL (logical model id from your
workspace), KIMSS_BASE_URL (optional).
"""
from __future__ import annotations

import os
import sys

from openai import OpenAI


def main() -> None:
    key = (os.environ.get("KIMSS_API_KEY") or "").strip()
    model = (os.environ.get("KIMSS_MODEL") or "").strip()
    if not key or not model:
        print(
            "Set KIMSS_API_KEY and KIMSS_MODEL in .env (see README steps 1-2).",
            file=sys.stderr,
        )
        raise SystemExit(1)
    base = (os.environ.get("KIMSS_BASE_URL") or "https://api.kimss.ai").rstrip("/")

    # The only change from a stock OpenAI integration: base_url + Kimss key.
    client = OpenAI(base_url=f"{base}/v1", api_key=key)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "One sentence: why should AI traffic route through a gateway?",
            }
        ],
    )
    print(resp.choices[0].message.content)


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass
    main()
