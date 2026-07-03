# Crypto AI Advisor

Crypto AI Advisor is an advisory-only crypto market analysis project. It combines public market data, optional CCXT exchange access, news context, sentiment scoring, risk scoring, liquidity scoring, event-risk scoring, derivatives-risk placeholders, macro/social context placeholders, data-quality flags, local signal storage, reports, backtesting helpers, streaming foundations, and explainable recommendations.

## Implemented now

- Backend package structure.
- FastAPI server entrypoint: `backend/app/server.py`.
- API router: `backend/app/api.py`.
- Extra API router: `backend/app/api_extra.py`.
- Market scoring core: `backend/app/advisor_core.py`.
- Public market data service: `backend/app/market_data.py`.
- Optional exchange adapter: `backend/app/exchange_adapter.py`.
- Market snapshot service: `backend/app/market_service.py`.
- Market universe service: `backend/app/market_universe.py`.
- Universe scan service: `backend/app/universe_service.py`.
- Market regime classifier: `backend/app/market_regime.py`.
- RSS news service: `backend/app/news_data.py`.
- Optional CryptoPanic source: `backend/app/external_news.py`.
- News ranking service: `backend/app/news_ranker.py`.
- Optional external sentiment model adapter: `backend/app/model_adapter.py`.
- Sentiment service: `backend/app/sentiment.py`.
- Risk service: `backend/app/risk.py`.
- Liquidity service: `backend/app/liquidity.py`.
- Event-risk service: `backend/app/event_risk.py`.
- Funding risk skeleton: `backend/app/funding.py`.
- Open-interest risk skeleton: `backend/app/open_interest.py`.
- Forced-flow risk skeleton: `backend/app/forced_flow.py`.
- Combined derivatives context: `backend/app/risk_context.py`.
- Book metrics: `backend/app/book_metrics.py`.
- Trade-flow metrics: `backend/app/trade_flow.py`.
- Cryptofeed adapter skeleton: `backend/app/cryptofeed_adapter.py`.
- Macro context skeleton: `backend/app/macro.py`.
- Social context skeleton: `backend/app/social.py`.
- Data quality checks: `backend/app/data_quality.py`.
- Score explainer: `backend/app/score_explainer.py`.
- Full advice service: `backend/app/advice_service.py`.
- Overview service with alerts and portfolio bias: `backend/app/overview_service.py`.
- Alert service: `backend/app/alerts.py`.
- Portfolio exposure service: `backend/app/portfolio.py`.
- Watchlist service: `backend/app/watchlist.py`.
- Runtime status aggregator: `backend/app/runtime_status.py`.
- Provider health service: `backend/app/provider_health.py`.
- Database abstraction: `backend/app/database.py`.
- Expanded database schema: `backend/app/db_schema.py`.
- Database helper: `backend/app/db.py`.
- PostgreSQL adapter skeleton: `backend/app/postgres_adapter.py`.
- Local SQLite signal storage: `backend/app/storage.py`.
- Scheduler cycle service: `backend/app/scheduler.py`.
- Streaming event layer: `backend/app/streaming.py`.
- Stream worker: `backend/app/stream_worker.py`.
- Reporting service: `backend/app/reporting.py`.
- Signal export service: `backend/app/export_service.py`.
- Backtest service: `backend/app/backtest_service.py`.
- Backtest report builder: `backend/app/backtest_report.py`.
- Static dashboard prototype: `frontend/index.html` and `frontend/app.js`.
- API reference: `docs/API.md`.
- Service map: `docs/SERVICE_MAP.md`.
- Integration notes: `docs/INTEGRATIONS.md`.
- Runbook: `docs/RUNBOOK.md`.

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
GET /api/watchlist
GET /api/providers/health
GET /api/database/status
GET /api/streaming/status
GET /api/runtime/status
GET /api/scheduler/status
GET /api/universe?exchange=binance&timeframe=1h&limit=10
GET /api/market/regime?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/market/snapshot?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/news/latest?symbol=BTC/USDT&limit=12
GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h&save=true
GET /api/overview?exchange=binance&timeframe=1h
GET /api/reports/json?exchange=binance&timeframe=1h
GET /api/reports/text?exchange=binance&timeframe=1h
GET /api/backtest?symbol=BTC/USDT&exchange=binance&timeframe=1h&limit=200&window=40
GET /api/signals/recent?limit=50
GET /api/signals/export?limit=50
```

Supported public market sources in this version:

```text
binance
bybit
```

Optional CCXT mode:

```text
USE_CCXT=true
```

Optional news and model integrations:

```text
CRYPTOPANIC_API_KEY=
SENTIMENT_MODEL_URL=
```

## Worker and scheduler

```bash
cd backend
python -m app.worker
python -m app.scheduler
python -m app.stream_worker
```

The worker and scheduler use configured symbols from `DEFAULT_SYMBOLS`.

## Next build steps

1. Replace placeholder macro/social providers with real data adapters.
2. Add deeper PostgreSQL or TimescaleDB production persistence.
3. Wire actual Cryptofeed callbacks into the streaming worker.
4. Add deployment files when repository write restrictions allow it.
5. Polish the dashboard into a full React or Next.js frontend.

## Safety rule

The default project must stay advisory-only. Do not add default exchange execution to this backend.
