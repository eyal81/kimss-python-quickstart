# AI Integration — Kimss Gateway (Agent-to-Agent)

**Strict directive for coding assistants using this quickstart.**

1. **Never** use a custom `KimssClient` for chat/completions.
2. **Always** use the standard OpenAI native SDK.
3. **Always** set `base_url` to `https://api.kimss.ai/v1`.
4. **Always** inject `X-Kimss-Agent-Id` (and `X-Kimss-Agent-Name`) via `extra_headers`.
5. Hermis / interceptors: forward those headers; never strip them.

Prefer [`example_02_openai_override.py`](example_02_openai_override.py). Anthropic is vaulted BYO — call governed models through the OpenAI client only.

Kill switch: `agent_disabled`. Keys: `kimss_...`.
