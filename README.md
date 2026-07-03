# Crypto AI Advisor

Crypto AI Advisor — это advisory-only система для анализа крипторынка. Проект собирает публичные market data, новости, sentiment, risk signals, liquidity/context flags, сохраняет advisory signals, строит market screener, reports, backtesting helpers, streaming foundation, diagnostics и explainable recommendations.

Важно: проект анализирует и объясняет. Он не исполняет сделки и не отправляет ордера на биржи.

## Что уже реализовано

- Backend package structure.
- FastAPI server с CORS: `backend/app/server.py`.
- Основной API router: `backend/app/api.py`.
- Extra API router: `backend/app/api_extra.py`.
- Explanation API router: `backend/app/api_explain.py`.
- Screener API router: `backend/app/api_screener.py`.
- Market scoring core: `backend/app/advisor_core.py`.
- Public market data service: `backend/app/market_data.py`.
- Optional exchange adapter через CCXT: `backend/app/exchange_adapter.py`.
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
- Cryptofeed adapter и runner: `backend/app/cryptofeed_adapter.py`, `backend/app/feed_callbacks.py`, `backend/app/cryptofeed_runner.py`.
- Data quality checks: `backend/app/data_quality.py`.
- Score explainer: `backend/app/score_explainer.py`.
- Advisory rules: `backend/app/strategy_rules.py`.
- Advice explainer: `backend/app/advice_explainer.py`.
- Full advice service: `backend/app/advice_service.py`.
- Persistence pipeline: `backend/app/pipeline.py`.
- Batch pipeline: `backend/app/batch_pipeline.py`.
- Job endpoints: `/api/jobs/symbol` и `/api/jobs/batch`.
- Readiness endpoint: `/api/readiness`.
- Diagnostics endpoint: `/api/diagnostics`.
- Deep health endpoint: `/api/health/deep`.
- Runtime check script: `scripts/runtime_check.py`.
- PostgreSQL init script: `scripts/init_postgres.py`.
- Real PostgreSQL adapter через psycopg: `backend/app/postgres_adapter.py`.
- PostgreSQL/Timescale schema draft: `database/timescale_schema.sql`.
- SQLite fallback storage: `backend/app/storage.py`.
- Scheduler: `backend/app/scheduler.py`.
- Stream worker: `backend/app/stream_worker.py`.
- Reports/export/backtest services.
- Static dashboard: `frontend/index.html` и `frontend/app.js`.
- Next.js dashboard scaffold: `frontend-next/`.
- Production docs, runtime docs, deployment docs, systemd templates.

## Запуск backend

```bash
cd backend
python -m pip install fastapi uvicorn
python -m uvicorn app.server:server --reload
```

Или:

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
GET /api/diagnostics
GET /api/health/deep
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

## Источники market data

```text
binance
bybit
```

## Optional dependency groups

```bash
pip install -e '.[exchange]'
pip install -e '.[postgres]'
pip install -e '.[streaming]'
pip install -e '.[production]'
```

## Optional integrations

```text
CRYPTOPANIC_API_KEY=
SENTIMENT_MODEL_URL=
GDELT_ENABLED=false
DATABASE_URL=
```

## Workers

```bash
cd backend
python -m app.worker
python -m app.scheduler
python -m app.stream_worker
python -m app.cryptofeed_runner
```

Workers используют symbols из `DEFAULT_SYMBOLS`.

## Dashboards

```bash
# Static prototype
open frontend/index.html

# Next.js scaffold
cd frontend-next
npm install
NEXT_PUBLIC_API_BASE=http://localhost:8000 npm run dev
```

## Текущая готовность

95% готово по коду и архитектуре.

Что осталось до честных 100%:

1. Запустить backend и исправить runtime errors.
2. Проверить optional dependencies: `ccxt`, `psycopg`, `cryptofeed`.
3. Проверить PostgreSQL на реальном `DATABASE_URL`.
4. Проверить `cryptofeed_runner` на установленной версии `cryptofeed`.
5. Доделать polished UI для Next.js dashboard.
6. Dockerfile/compose блокировались GitHub write tooling, поэтому добавлены deployment docs и systemd templates.

## Правило безопасности

Проект должен оставаться advisory-only. Не добавлять default exchange order execution и не хранить приватные exchange credentials в репозитории.
