# Operations Guide

## Environment

Use `deploy/env.example.production` as a production template.

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

## Rule

The deployment must remain advisory-only.
