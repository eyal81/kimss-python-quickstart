# KIMSS GATEWAY AGENT INSTRUCTIONS

Follow [AI_INTEGRATION.md](../AI_INTEGRATION.md).

1. Use official OpenAI client with `base_url=https://api.kimss.ai/v1`.
2. Always send `X-Kimss-Agent-Id` (and `X-Kimss-Agent-Name`) via `extra_headers`.
3. Never use `KimssClient` for chat/completions.
4. Prefer `example_02_openai_override.py` in this repo.
5. Kill switch: `agent_disabled`. Keys: `kimss_...`.
