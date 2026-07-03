# Storage Model Specification

## current_advisory_signals

Current local SQLite table.

Fields:

- id
- symbol
- recommendation
- final_score
- risk_score
- payload
- created_at

## planned_market_candles

Future production table.

Fields:

- id
- exchange
- symbol
- timeframe
- timestamp
- open
- high
- low
- close
- volume

## planned_news_items

Fields:

- id
- source
- title
- url
- published_at
- related_assets
- raw_payload

## planned_sentiment_scores

Fields:

- id
- news_item_id
- label
- score
- confidence
- engine
- created_at

## planned_risk_snapshots

Fields:

- id
- symbol
- risk_score
- base_risk_score
- liquidity_score
- event_risk_score
- risk_flags
- quality_flags
- created_at
