# API Reference

Этот файл описывает основные API endpoints проекта. Названия endpoints остаются на английском, потому что это часть технического контракта backend.

## Health и runtime

- `GET /ping` — базовая проверка, что API отвечает.
- `GET /api/providers/health` — общий статус источников и адаптеров.
- `GET /api/database/status` — текущий storage mode: SQLite или PostgreSQL.
- `GET /api/streaming/status` — статус streaming layer.
- `GET /api/runtime/status` — общий runtime status.
- `GET /api/scheduler/status` — статус scheduler config.
- `GET /api/readiness` — процентная оценка готовности системы.
- `GET /api/diagnostics` — проверка imports, optional dependencies и env.
- `GET /api/health/deep` — deep health report: diagnostics + readiness + provider health.
- `GET /api/context/status` — статус context providers: GDELT, macro, social, regulatory, announcements.

## Watchlist и universe

- `GET /api/watchlist` — список отслеживаемых symbols.
- `GET /api/universe?exchange=binance&timeframe=1h&limit=10` — анализ расширенного списка монет.
- `GET /api/screener?exchange=binance&timeframe=1h&limit=10` — market screener: top setups, high-risk, low-confidence.

## Jobs и persistence

- `GET /api/jobs/symbol?symbol=BTC/USDT&exchange=binance&timeframe=1h&save=true` — запуск pipeline по одному symbol.
- `GET /api/jobs/batch?exchange=binance&timeframe=1h&limit=10&save=true` — запуск batch pipeline по universe.

## Market и news

- `GET /api/market/snapshot?symbol=BTC/USDT&exchange=binance&timeframe=1h` — market snapshot и market score.
- `GET /api/market/regime?symbol=BTC/USDT&exchange=binance&timeframe=1h` — классификация рыночного режима.
- `GET /api/news/latest?symbol=BTC/USDT&limit=12` — последние новости и sentiment enrichment.

## Advice

- `GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h` — advisory recommendation.
- `GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h&save=true` — advisory recommendation с сохранением signal.
- `GET /api/advice/explain?symbol=BTC/USDT&exchange=binance&timeframe=1h` — объяснение recommendation и rules.
- `GET /api/overview?exchange=binance&timeframe=1h` — overview по watchlist.

## Reports и backtesting

- `GET /api/reports/json?exchange=binance&timeframe=1h` — JSON report.
- `GET /api/reports/text?exchange=binance&timeframe=1h` — text report.
- `GET /api/backtest?symbol=BTC/USDT&exchange=binance&timeframe=1h&limit=200&window=40` — простой backtest report.

## Stored signals

- `GET /api/signals/recent?limit=50` — последние сохранённые signals.
- `GET /api/signals/export?limit=50` — export signals в plain text.

## Принципы response

- Каждая recommendation является advisory-only.
- Каждый advice response должен включать risk score и confidence.
- Risk flags и quality flags должны быть частью decision context.
- Ни один endpoint не должен отправлять exchange orders.
