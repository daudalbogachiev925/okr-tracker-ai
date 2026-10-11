Описание: OKR-трекер с ИИ-ассистентом. Генерация KR через LLM, ежедневные напоминания, прогресс-трекинг, дашборд, интеграция со Slack.

Стек: Next.js (frontend), FastAPI + PostgreSQL (backend), OpenAI/Anthropic, Redis, Docker.

# okr-tracker-ai

OKR-трекер с ИИ-генерацией Key Results.

## Возможности
- Создание целей и KR
- ИИ-генерация KR через Claude
- Прогресс-трекинг
- Slack-напоминания
- Дашборд для руководителя

## Быстрый старт

git clone https://github.com/your-org/okr-tracker-ai
cd okr-tracker-ai
cp .env.example .env
docker-compose up

Frontend: http://localhost:3000
API: http://localhost:8000/docs

## Лицензия
MIT
