# AI Integration — Kimss Gateway (Agent-to-Agent)

1. Never use `KimssClient` for chat/completions/messages.
2. Keep native `openai` or `anthropic` SDK.
3. OpenAI → `https://api.kimss.ai/v1`. Anthropic → `https://api.kimss.ai`.
4. Always inject `X-Kimss-Agent-Id`.

Prefer `example_02_openai_override.py` (OpenAI) or add Anthropic with the same Agent-Id headers.
