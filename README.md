# Crypto AI Advisor

Crypto AI Advisor is an advisory-only crypto market analysis project. It is being built to combine market data, news context, sentiment, risk scoring, and explainable recommendations.

## Current repository state

Implemented now:

- Backend package structure.
- FastAPI router skeleton.
- Advisory scoring core in `backend/app/advisor_core.py`.
- Demo advisory endpoint in `backend/app/api.py`.
- Server entrypoint in `backend/app/server.py`.
- Architecture documentation in `docs/ARCHITECTURE.md`.
- Environment example in `.env.example`.

Important: this is not a real-money trading system. It is for analytics and advice only.

## Current demo endpoint

After installing FastAPI and Uvicorn, run:

```bash
cd backend
python -m pip install fastapi uvicorn
python -m uvicorn app.server:server --reload
```

Then open:

```text
GET http://localhost:8000/ping
GET http://localhost:8000/api/demo-advice
```

## Next implementation steps

1. Add public exchange-data collectors for Binance and Bybit.
2. Add news collectors from RSS and API sources.
3. Add a stronger sentiment module.
4. Add database storage for market snapshots, news, and generated signals.
5. Add a dashboard.
6. Add historical testing scripts.

## Safety rule

The default project must stay advisory-only. Do not add real exchange execution to the default backend.
