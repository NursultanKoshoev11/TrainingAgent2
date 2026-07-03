# Crypto AI Advisor

Crypto AI Advisor is an advisory-only crypto market analysis project. It combines public market data, news context, sentiment scoring, risk scoring, and explainable recommendations.

## Implemented now

- Backend package structure.
- FastAPI server entrypoint: `backend/app/server.py`.
- API router: `backend/app/api.py`.
- Market scoring core: `backend/app/advisor_core.py`.
- Public market data service: `backend/app/market_data.py`.
- Market snapshot service: `backend/app/market_service.py`.
- RSS news service: `backend/app/news_data.py`.
- Sentiment service: `backend/app/sentiment.py`.
- Risk service: `backend/app/risk.py`.
- Full advice service: `backend/app/advice_service.py`.
- Overview service: `backend/app/overview_service.py`.
- Worker: `backend/app/worker.py`.
- Static dashboard prototype: `frontend/index.html`.
- Research helper: `research/simple_backtest.py`.

Important: this project analyzes and explains. It does not execute trades.

## Run backend

```bash
cd backend
python -m pip install fastapi uvicorn
python -m uvicorn app.server:server --reload
```

Or:

```bash
cd backend
bash run_backend.sh
```

## API endpoints

```text
GET /ping
GET /api/demo-advice
GET /api/market/snapshot?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/news/latest?symbol=BTC/USDT&limit=12
GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/overview?exchange=binance&timeframe=1h
```

Supported public market sources in this version:

```text
binance
bybit
```

## Worker

```bash
cd backend
python -m app.worker
```

The worker checks all configured symbols from `DEFAULT_SYMBOLS`.

## Next steps

1. Add persistent database storage.
2. Add stronger sentiment model adapter.
3. Add WebSocket market feed layer.
4. Add proper React or Next.js dashboard.
5. Add validation reports and more complete backtesting.

## Safety rule

The default project must stay advisory-only. Do not add default exchange execution to this backend.
