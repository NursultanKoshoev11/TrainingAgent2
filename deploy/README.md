# Deployment

Deployment target:

- backend API service
- scheduler process
- stream process
- PostgreSQL or TimescaleDB
- optional Next.js dashboard

Backend command:

```bash
cd backend
python -m pip install fastapi uvicorn
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

Scheduler command:

```bash
cd backend
python -m app.scheduler
```

Stream command:

```bash
cd backend
python -m app.stream_worker
```

Production storage:

- Set `DATABASE_URL=postgresql://...`
- Install optional backend dependency group `postgres`
- Run backend once; the adapter initializes required tables.

Safety:

- This app is advisory-only.
- Do not add private exchange keys to deployment configuration.
