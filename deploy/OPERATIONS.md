# Operations Guide

Инструкция для запуска проекта на сервере без Docker. Dockerfile/compose ранее блокировались GitHub write tooling, поэтому текущий production-вариант описан через processes и systemd templates.

## Environment

Использовать `deploy/env.example.production` как production template. Перед запуском заменить placeholder values:

- `DATABASE_URL`
- `CRYPTOPANIC_API_KEY`, если используется
- `SENTIMENT_MODEL_URL`, если используется внешний model service
- `CORS_ORIGINS`
- `NEXT_PUBLIC_API_BASE`

## API process

```bash
cd backend
python -m pip install -e '.[production]'
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

## PostgreSQL init

```bash
cd backend
python ../scripts/init_postgres.py
```

После этого проверить:

```text
/api/database/status
/api/readiness
/api/health/deep
```

## Worker processes

```bash
cd backend
python -m app.scheduler
python -m app.stream_worker
python -m app.cryptofeed_runner
```

## Systemd templates

- `deploy/systemd-api.service`
- `deploy/systemd-scheduler.service`
- `deploy/systemd-stream.service`
- `deploy/systemd-feed.service`

## Runtime status URLs

- `/api/diagnostics`
- `/api/readiness`
- `/api/health/deep`
- `/api/providers/health`

## Правило

Deployment должен оставаться advisory-only. Не добавлять order execution и не хранить private exchange credentials в репозитории.
