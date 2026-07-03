# Crypto AI Advisor

Crypto AI Advisor is a non-custodial, non-trading market intelligence system for crypto markets. It collects exchange data, reads crypto news, calculates market/sentiment/risk scores, and returns explainable advisory signals.

> This project does **not** place real orders. It is an analytics and advisory system only.

## What it does

- Collects market data from Binance, Bybit, or any exchange supported by CCXT.
- Computes technical market metrics: trend, volatility, volume strength, RSI, EMA trend, and liquidity notes.
- Collects crypto news from CryptoPanic when an API key is configured, with RSS fallback support.
- Converts news into structured sentiment signals.
- Combines market, sentiment, and risk into a final advisory recommendation.
- Exposes a FastAPI backend.
- Includes a simple dashboard.
- Includes optional Freqtrade and vectorbt research skeletons for future paper-trading/backtesting.

## Architecture

```text
Exchange APIs / News APIs
        |
        v
Collectors -> PostgreSQL -> Signal Engine -> Risk Engine -> FastAPI -> Dashboard
```

Main modules:

```text
backend/      FastAPI API, scoring, database models
workers/      Scheduled collectors for market and news data
frontend/     Minimal dashboard
strategies/   Optional Freqtrade strategy skeleton
research/     Optional vectorbt research scripts
docs/         Architecture and safety notes
```

## Quick start

1. Copy environment variables:

```bash
cp .env.example .env
```

2. Start the stack:

```bash
docker compose up --build
```

3. Open:

```text
Backend API: http://localhost:8000/docs
Dashboard:   http://localhost:3000
```

## Default API endpoints

```text
GET /health
GET /api/market/snapshot?symbol=BTC/USDT&exchange=binance&timeframe=1h
GET /api/news/latest?symbol=BTC
GET /api/advice?symbol=BTC/USDT&exchange=binance&timeframe=1h
```

## Recommendation labels

```text
STRONG_BULLISH_SETUP  Strong positive setup, but still not a command to buy.
BULLISH_SETUP         Positive setup with normal caution.
WAIT                  Mixed or weak signal.
HIGH_RISK_AVOID       Risk is too high or data is not reliable enough.
BEARISH_SETUP         Negative setup.
```

## Safety rules

- No real trading by default.
- No exchange private keys required for the MVP.
- Public market data only.
- Every signal includes risk flags and a confidence score.
- The system is advisory only and must not be treated as financial advice.

## Next steps

- Add persistent scheduled ingestion with Celery or Dramatiq.
- Add TimescaleDB hypertables for candles.
- Add real FinGPT/FinBERT model server for stronger sentiment analysis.
- Add more exchanges through CCXT and Cryptofeed.
- Add walk-forward backtesting before any paper-trading experiment.
