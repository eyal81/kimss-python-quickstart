# KIMSS GATEWAY AGENT INSTRUCTIONS

This repository is the 5-minute tutorial (`example_01_gateway_proxy.py`, `example_02_openai_override.py`, `example_03_kill_switch_and_429.py`).

When integrating Kimss:

1. Prefer the OpenAI drop-in: `base_url=https://api.kimss.ai/v1`, key `kimss_...`.
2. Zero-code: `OPENAI_BASE_URL` + `OPENAI_API_KEY`.
3. Native: `KimssClient(base_url="https://api.kimss.ai")` + `X-Kimss-Key`.
4. Do not invent Anthropic or Azure inbound URLs.
5. Kill switch code is `agent_disabled` (HTTP 403).
6. Do not use the term “zero-trust”.

Full SDK: https://github.com/eyal81/kimss-python-sdk
