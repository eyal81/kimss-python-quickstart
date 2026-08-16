#!/usr/bin/env python3
"""Step 3 of the quickstart: route one local call through the Kimss gateway.

The gateway checks identity (X-Kimss-Key), applies policy, writes the governed
audit record, then forwards to the model endpoint you vaulted in the Kimss UI.

Env: KIMSS_API_KEY (required), KIMSS_AGENT_ID (required), KIMSS_BASE_URL (optional).
"""
from __future__ import annotations

import json
import os
import sys

from kimss import KimssClient


def main() -> None:
    key = (os.environ.get("KIMSS_API_KEY") or "").strip()
    agent_id = (os.environ.get("KIMSS_AGENT_ID") or "").strip()
    if not key or not agent_id:
        print(
            "Set KIMSS_API_KEY and KIMSS_AGENT_ID in .env (see README steps 1-2).\n"
            "Get a free key at https://kimss.ai/app/signup "
            "(25,000 governed requests/mo included. No credit card).",
            file=sys.stderr,
        )
        raise SystemExit(1)
    base = (os.environ.get("KIMSS_BASE_URL") or "https://api.kimss.ai").rstrip("/")

    client = KimssClient(api_key=key, base_url=base)
    result = client.agents.run(
        agent_id,
        "Hello from the Kimss quickstart. Confirm this call was governed.",
        stream=False,
    )

    print("--- governed response ---")
    print(result.text)
    print("--- raw payload ---")
    print(json.dumps(result, indent=2, default=str))
    print()
    print(
        "Done. Open your dashboard to see this call in the governed audit trail:\n"
        f"  {base.replace('api.', '').rstrip('/')}/app/gateway  (Recent calls)\n"
        f"  {base.replace('api.', '').rstrip('/')}/app/governance/audit-log"
    )


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass
    main()
