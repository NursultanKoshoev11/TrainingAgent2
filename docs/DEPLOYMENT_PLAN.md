# Deployment Plan

Target deployment should stay advisory-only.

## Services

- backend API
- scheduler worker
- dashboard frontend
- database
- optional cache
- optional external sentiment model service

## Environments

- local
- staging
- production

## Required environment variables

- DEFAULT_EXCHANGE
- DEFAULT_SYMBOLS
- DEFAULT_TIMEFRAME
- USE_CCXT
- CRYPTOPANIC_API_KEY
- SENTIMENT_MODEL_URL
- DATABASE_BACKEND
- DATABASE_URL

## Local mode

Local mode can use SQLite and public exchange endpoints.

## Production mode

Production mode should use PostgreSQL or TimescaleDB for persistent analytics storage.

## Safety controls

- No order execution service.
- No private exchange keys.
- No leverage settings.
- No trading buttons in the dashboard.
