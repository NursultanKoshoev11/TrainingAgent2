# Service Map

## Backend Core

- `app.api`: HTTP API routes.
- `app.server`: FastAPI server entrypoint.
- `app.settings`: environment configuration.

## Market Data

- `app.market_data`: direct public Binance and Bybit candle endpoints.
- `app.exchange_adapter`: optional CCXT adapter.
- `app.market_service`: normalized market snapshot builder.
- `app.streaming`: event layer for future WebSocket and Cryptofeed integration.
- `app.stream_worker`: snapshot-polling stream worker.

## News and Context

- `app.news_data`: RSS news collection.
- `app.external_news`: optional CryptoPanic source.
- `app.sentiment`: local and external sentiment scoring.
- `app.model_adapter`: optional external model API adapter.
- `app.macro`: macro context contract.
- `app.social`: social sentiment contract.

## Decision Layer

- `app.advisor_core`: scoring math.
- `app.liquidity`: liquidity estimate.
- `app.event_risk`: event-risk detection.
- `app.risk`: base risk score.
- `app.data_quality`: quality flags.
- `app.advice_service`: final advisory response.
- `app.score_explainer`: explanation lines.

## Portfolio and Reports

- `app.overview_service`: watchlist overview.
- `app.market_universe`: larger default universe.
- `app.universe_service`: broader market scan.
- `app.portfolio`: watchlist bias.
- `app.alerts`: alert output.
- `app.reporting`: text and JSON reports.
- `app.export_service`: signal export.

## Storage and Runtime

- `app.storage`: SQLite signal history.
- `app.database`: database adapter wrapper.
- `app.db_schema`: expanded schema draft.
- `app.db`: extra table helper layer.
- `app.scheduler`: repeated advisory cycles.
- `app.runtime_status`: combined runtime status.
