# Runtime Check

Run these commands after installing backend dependencies.

## Minimal

```bash
cd backend
python -m pip install fastapi uvicorn
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

Open:

```text
http://localhost:8000/ping
http://localhost:8000/api/diagnostics
http://localhost:8000/api/readiness
http://localhost:8000/api/providers/health
```

## Local diagnostic script

```bash
cd backend
python ../scripts/runtime_check.py
```

## PostgreSQL

```bash
cd backend
python -m pip install -e '.[postgres]'
export DATABASE_URL=postgresql://user:password@localhost:5432/crypto_ai_advisor
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

Then open:

```text
http://localhost:8000/api/database/status
http://localhost:8000/api/jobs/symbol?symbol=BTC/USDT&save=true
```

## Streaming

```bash
cd backend
python -m pip install -e '.[streaming]'
python -m app.cryptofeed_runner
```

Expected output file:

```text
backend/market_feed_events.jsonl
```
