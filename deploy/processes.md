# Process Layout

Рекомендуемые production processes:

## API

```bash
cd backend
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

## Scheduler

```bash
cd backend
python -m app.scheduler
```

## Snapshot stream worker

```bash
cd backend
python -m app.stream_worker
```

## Market feed runner

```bash
cd backend
python -m app.cryptofeed_runner
```

## Dashboard

```bash
cd frontend-next
NEXT_PUBLIC_API_BASE=http://localhost:8000 npm run start
```

Для постоянного запуска использовать process manager: systemd, supervisor или managed platform process runner.
