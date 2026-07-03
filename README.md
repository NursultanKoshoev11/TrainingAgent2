# Crypto AI Advisor

Crypto AI Advisor is an advisory-only crypto market analysis project. It combines public market data, optional CCXT exchange access, news context, sentiment scoring, risk scoring, liquidity scoring, event-risk scoring, derivatives-risk placeholders, macro/social context placeholders, data-quality flags, local signal storage, reports, backtesting helpers, streaming foundations, market screening, persistence pipelines, and explainable recommendations.

## Implemented now

- Backend package structure.
- FastAPI server entrypoint with CORS: `backend/app/server.py`.
- API router: `backend/app/api.py`.
- Extra API router: `backend/app/api_extra.py`.
- Explanation API router: `backend/app/api_explain.py`.
- Screener API router: `backend/app/api_screener.py`.
- Market scoring core: `backend/app/advisor_core.py`.
- Public market data service: `backend/app/market_data.py`.
- Optional exchange adapter: `backend/app/exchange_adapter.py`.
- Market snapshot service: `backend/app/market_service.py`.
- In-memory TTL cache: `backend/app/memory_cache.py`.
- Shared network client: `backend/app/net_client.py`.
- Market universe service: `backend/app/market_universe.py`.
- Universe scan service: `backend/app/universe_service.py`.
- Market screener: `backend/app/screener.py`.
- Market filters: `backend/app/market_filters.py`.
- Market regime classifier: `backend/app/market_regime.py`.
- Asset profile service: `backend/app/asset_profile.py`.
- RSS news service: `backend/app/news_data.py`.
- Optional CryptoPanic source: `backend/app/external_news.py`.
- GDELT adapter skeleton: `backend/app/gdelt_adapter.py`.
- Exchange announcements skeleton: `backend/app/exchange_announcements.py`.
- Regulatory news skeleton: `backend/app/regulatory_news.py`.
- News ranking service: `backend/app/news_ranker.py`.
- Optional external sentiment model adapter: `backend/app/model_adapter.py`.
- Sentiment service: `backend/app/sentiment.py`.
- Macro adapters skeleton: `backend/app/macro_adapters.py`.
- Social adapters skeleton: `backend/app/social_adapters.py`.
- Context registry: `backend/app/context_registry.py`.
- Risk service: `backend/app/risk.py`.
- Liquidity service: `backend/app/liquidity.py`.
- Event-risk service: `backend/app/event_risk.py`.
- Funding risk skeleton: `backend/app/funding.py`.
- Open-interest risk skeleton: `backend/app/open_interest.py`.
- Forced-flow risk skeleton: `backend/app/forced_flow.py`.
- Combined derivatives context: `backend/app/risk_context.py`.
- Book metrics: `backend/app/book_metrics.py`.
- Trade-flow metrics: `backend/app/trade_flow.py`.
- Cryptofeed adapter and runner: `backend/app/cryptofeed_adapter.py`, `backend/app/feed_callbacks.py`, `backend/app/cryptofeed_runner.py`.
- Macro context skeleton: `backend/app/macro.py`.
- Social context skeleton: `backend/app/social.py`.
- Data quality checks: `backend/app/data_quality.py`.
- Score explainer: `backend/app/score_explainer.py`.
- Advisory rules: `backend/app/strategy_rules.py`.
- Advice explainer: `backend/app/advice_explainer.py`.
- Full advice service: `backend/app/advice_service.py`.
- Persistence pipeline: `backend/app/pipeline.py`.
- Batch pipeline: `backend/app/batch_pipeline.py`.
- Job endpoints: `/api/jobs/symbol` and `/api/jobs/batch`.
- Readiness endpoint: `/api/readiness`.
- Overview service with alerts and portfolio bias: `backend/app/overview_service.py`.
- Alert service: `backend/app/alerts.py`.
- Portfolio exposure service: `backend/app/portfolio.py`.
- Watchlist service: `backend/app/watchlist.py`.
- Runtime status aggregator: `backend/app/runtime_status.py`.
- Provider health service: `backend/app/provider_health.py`.
- Database abstraction: `backend/app/database.py`.
- Expanded database schema: `backend/app/db_schema.py`.
- Database helper with PostgreSQL routing: `backend/app/db.py`.
- Real PostgreSQL adapter with psycopg: `backend/app/postgres_adapter.py`.
- Timescale/PostgreSQL schema draft: `database/timescale_schema.sql`.
- Local SQLite signal storage: `backend/app/storage.py`.
- Scheduler cycle service: `backend/app/scheduler.py`.
- Streaming event layer: `backend/app/streaming.py`.
- Stream worker: `backend/app/stream_worker.py`.
- Reporting service: `backend/app/reporting.py`.
- Signal export service: `backend/app/export_service.py`.
- Backtest service: `backend/app/backtest_service.py`.
- Backtest report builder: `backend/app/backtest_report.py`.
- Static dashboard prototype: `frontend/index.html` and `frontend/app.js`.
- Next.js dashboard scaffold and health page: `frontend-next/`.
- API reference: `docs/API.md`.
- Service map: `docs/SERVICE_MAP.md`.
- Integration notes: `docs/INTEGRATIONS.md`.
- Production DB notes: `docs/PRODUCTION_DB.md`.
- Production checklist: `docs/PRODUCTION_CHECKLIST.md`.
- Deployment notes: `deploy/README.md`.
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
GET /api/readiness
GET /api/context/status
GET /api/universe?exchange=binance&timeframe=1h&limit=10
GET /api/screener?exchange=binance&timeframe=1h&limit=10
GET /api/jobs/symbol?symbol=BTC/USDT&exchange=binance&timeframe=1h&save=true
GET /api/jobs/batch?exchange=binance&timeframe=1h&limit=10&save=true
GET /api/market/regime?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/market/snapshot?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/news/latest?symbol=BTC/USDT&limit=12
GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/advice/explain?symbol=BTC/USDT&exchange=binance&timeframe=1h
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

Optional dependency groups:

```bash
pip install -e '.[exchange]'
pip install -e '.[postgres]'
pip install -e '.[streaming]'
pip install -e '.[production]'
```

Optional news and model integrations:

```text
CRYPTOPANIC_API_KEY=
SENTIMENT_MODEL_URL=
GDELT_ENABLED=false
DATABASE_URL=
```

## Worker and scheduler

```bash
cd backend
python -m app.worker
python -m app.scheduler
python -m app.stream_worker
python -m app.cryptofeed_runner
```

The worker and scheduler use configured symbols from `DEFAULT_SYMBOLS`.

## Dashboards

```bash
# Static prototype
open frontend/index.html

# Next.js scaffold
cd frontend-next
npm install
NEXT_PUBLIC_API_BASE=http://localhost:8000 npm run dev
```

## Current completion estimate

92% complete as code/architecture.

Remaining production work:

1. Runtime verification and fixes after installing dependencies.
2. Source-specific macro/social provider fetchers require confirmed API/source rules.
3. Docker files were blocked by repository write safety tooling; deployment runbook is present instead.
4. Next.js dashboard needs UI polish beyond scaffold/main/health pages.
5. Cryptofeed runner needs runtime validation against installed cryptofeed version.

## Safety rule

The default project must stay advisory-only. Do not add default exchange execution to this backend.
