# Route your first governed AI call in 5 minutes

[![PyPI](https://img.shields.io/pypi/v/kimss.svg?color=indigo)](https://pypi.org/project/kimss/)
[![Python](https://img.shields.io/pypi/pyversions/kimss.svg?color=purple)](https://pypi.org/project/kimss/)
[![License: MIT](https://img.shields.io/badge/License-MIT-indigo.svg)](LICENSE)

**Track, govern, and secure autonomous agents with exactly 1 line of code. Zero data-plane refactoring required.**

Dual-listener: OpenAI (`/v1/chat/completions`) and Anthropic (`/v1/messages`). Keep your native SDK.

[Kimss](https://kimss.ai) is a **Secure AI Gateway** and **Governance Control Plane**. Point the official OpenAI client at Kimss, add an Agent ID header, and every request is identified, audited, and kill-switchable. Kimss never hosts your models (**BYOI**).

> **AI coding assistants:** [AI_INTEGRATION.md](AI_INTEGRATION.md)

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("KIMSS_GATEWAY_URL", "https://api.kimss.ai/v1"),
    api_key=os.getenv("KIMSS_WORKSPACE_KEY") or os.getenv("KIMSS_API_KEY"),
)
resp = client.chat.completions.create(
    model=os.getenv("KIMSS_MODEL", "custom:your-vaulted-model"),
    messages=[{"role": "user", "content": "Hello via Kimss"}],
    extra_headers={
        "X-Kimss-Agent-Id": os.getenv("KIMSS_AGENT_ID", "my_agent"),
        "X-Kimss-Agent-Name": os.getenv("KIMSS_AGENT_NAME", "My Agent"),
    },
)
```

```mermaid
flowchart LR
  App[Your_app] --> GW["Kimss_Gateway"]
  GW --> Model[Vaulted_provider]
  GW --> Trail[Governed_audit_trail]
```

---

## 3-step setup

### 1. Sign In & Vault

[Create Free Account →](https://kimss.ai/app/signup). Open **Governance → Connected Infrastructure** and vault your provider endpoint + key.

### 2. Mint Key

**Gateway → Generate Key**. Copy `kimss_...`. Note your `agent_id` (or register one under Gateway).

### 3. Route Traffic (zero refactoring)

```bash
git clone https://github.com/eyal81/kimss-python-quickstart.git
cd kimss-python-quickstart
pip install -r requirements.txt
cp .env.example .env   # KIMSS_WORKSPACE_KEY / KIMSS_API_KEY, KIMSS_AGENT_ID, KIMSS_MODEL
python example_02_openai_override.py
```

Open **Gateway → Recent calls** to see the governed audit trail.

---

## Scripts

| Script | What it proves |
|--------|----------------|
| [`example_02_openai_override.py`](example_02_openai_override.py) | **Primary** — OpenAI client + `base_url` + Agent-Id headers |
| [`example_01_gateway_proxy.py`](example_01_gateway_proxy.py) | Raw HTTP / key header path |
| [`example_03_kill_switch_and_429.py`](example_03_kill_switch_and_429.py) | Kill switch + monthly cap errors |

## Related

- SDK: [eyal81/kimss-python-sdk](https://github.com/eyal81/kimss-python-sdk) · [kimss.ai](https://kimss.ai)

## License

MIT — see [LICENSE](LICENSE).
