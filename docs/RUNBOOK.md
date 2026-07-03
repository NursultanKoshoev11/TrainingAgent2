# Runbook

## Backend

```bash
cd backend
python -m pip install fastapi uvicorn
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

## Worker

```bash
cd backend
python -m app.worker
```

## Scheduler

```bash
cd backend
python -m app.scheduler
```

## Stream worker

```bash
cd backend
python -m app.stream_worker
```

## Dashboard

Open `frontend/index.html` in a browser after the backend starts.

## Notes

Keep the default system advisory-only.
