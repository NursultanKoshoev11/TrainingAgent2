# Implementation Roadmap

## Phase 1: Advisory MVP

Status: started.

Goals:

- Backend boots.
- Demo advisory endpoint works.
- Core scoring logic exists.
- No real exchange execution exists.

## Phase 2: Public market data

Add public-only collectors:

- Binance public candles.
- Bybit public candles.
- Normalized symbol format.
- Retry and timeout handling.

## Phase 3: News and sentiment

Add:

- RSS collector.
- Crypto news API adapter.
- Sentiment scoring.
- Asset extraction from headlines.

## Phase 4: Storage

Add database tables:

- market_snapshots
- news_items
- sentiment_scores
- advisory_signals
- risk_flags

## Phase 5: Dashboard

Add pages:

- Overview.
- Asset detail.
- News feed.
- Risk explanation.
- Signal history.

## Phase 6: Research validation

Add historical testing scripts and reports before trusting any signal.
