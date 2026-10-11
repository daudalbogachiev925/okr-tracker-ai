import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PROMPT = """Ты опытный OKR-коуч. Сгенерируй 3-5 измеримых Key Results для цели:
"{objective}"

Требования:
- Конкретные метрики (число, процент, срок)
- Амбициозные, но достижимые
- Формат: список строк, только KR, без пояснений
"""

def generate_key_results(objective: str) -> list[str]:
    msg = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": PROMPT.format(objective=objective)}]
    )
    text = msg.content[0].text
    return [l.strip("-• ").strip() for l in text.splitlines() if l.strip()]
