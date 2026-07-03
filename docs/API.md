# API Reference

## Health and runtime

- `GET /ping`
- `GET /api/providers/health`
- `GET /api/database/status`
- `GET /api/streaming/status`
- `GET /api/runtime/status`
- `GET /api/scheduler/status`
- `GET /api/context/status`

## Watchlist and universe

- `GET /api/watchlist`
- `GET /api/universe?exchange=binance&timeframe=1h&limit=10`
- `GET /api/screener?exchange=binance&timeframe=1h&limit=10`

## Market and news

- `GET /api/market/snapshot?symbol=BTC/USDT&exchange=binance&timeframe=1h`
- `GET /api/market/regime?symbol=BTC/USDT&exchange=binance&timeframe=1h`
- `GET /api/news/latest?symbol=BTC/USDT&limit=12`

## Advice

- `GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h`
- `GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h&save=true`
- `GET /api/advice/explain?symbol=BTC/USDT&exchange=binance&timeframe=1h`
- `GET /api/overview?exchange=binance&timeframe=1h`

## Reports and backtesting

- `GET /api/reports/json?exchange=binance&timeframe=1h`
- `GET /api/reports/text?exchange=binance&timeframe=1h`
- `GET /api/backtest?symbol=BTC/USDT&exchange=binance&timeframe=1h&limit=200&window=40`

## Stored signals

- `GET /api/signals/recent?limit=50`
- `GET /api/signals/export?limit=50`

## Response principles

- Every recommendation is advisory-only.
- Every advice response should include risk score and confidence.
- Risk flags and quality flags are part of the decision context.
- No endpoint sends exchange orders.
