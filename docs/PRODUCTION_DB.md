# Production Database Plan

The current MVP uses SQLite for local signal history. Production should use PostgreSQL or TimescaleDB.

## Recommended tables

- market_candles
- market_snapshots
- news_items
- sentiment_scores
- risk_flags
- advisory_signals

## Schema

See `database/timescale_schema.sql`.

## Migration direction

1. Keep SQLite for local development.
2. Add a PostgreSQL repository implementation.
3. Switch by `DATABASE_URL`.
4. Use Timescale hypertables for candles after TimescaleDB is enabled.

## Rule

Storage is for analytics and auditability only. It should not store private exchange keys.
