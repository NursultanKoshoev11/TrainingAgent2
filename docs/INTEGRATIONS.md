# Integrations

## Market Data

Current:

- Binance public HTTP candles
- Bybit public HTTP candles
- Optional CCXT adapter

Planned:

- Cryptofeed trades
- Cryptofeed order book
- Cryptofeed ticker

## News

Current:

- Cointelegraph RSS
- CoinDesk RSS
- Optional CryptoPanic API

Planned:

- GDELT
- Exchange announcements
- Project official blogs
- Regulatory headline sources

## Sentiment

Current:

- Local keyword scoring
- Optional external model endpoint through `SENTIMENT_MODEL_URL`

Planned:

- FinBERT service
- FinGPT service
- Custom LLM explanation service

## Risk Context

Current contracts:

- funding context
- open-interest context
- forced-flow context
- event-risk context
- liquidity context

These contracts are intentionally advisory-only and do not execute trades.
