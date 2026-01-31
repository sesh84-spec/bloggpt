# bloggpt — Telegram post generator (FastAPI)

Сервис генерирует пост для Telegram по заданной теме через OpenAI API.

## Требования
- Python 3.10+
- Переменная окружения `OPENAI_API_KEY`

## Установка и запуск локально

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
