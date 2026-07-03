# Production Checklist

## Backend

- Start FastAPI server.
- Confirm `/ping` returns ok.
- Confirm `/api/providers/health` returns provider status.
- Confirm `/api/readiness` returns readiness estimate.

## Database

- Set `DATABASE_URL` for PostgreSQL.
- Install `psycopg` optional dependency.
- Confirm `/api/database/status` shows `mode: postgresql`.
- Run `/api/jobs/symbol?save=true` and confirm records are saved.

## Market data

- Confirm `/api/market/snapshot` returns price and score.
- Confirm `/api/screener` returns top setups and high-risk assets.

## News and context

- Set `CRYPTOPANIC_API_KEY` if available.
- Set `GDELT_ENABLED=true` after provider review.
- Confirm `/api/context/status` returns expected provider states.

## Streaming

- Install `cryptofeed` optional dependency.
- Run `python -m app.cryptofeed_runner`.
- Confirm `market_feed_events.jsonl` is created.

## Dashboard

- Run backend on port 8000.
- Run Next dashboard with `NEXT_PUBLIC_API_BASE=http://localhost:8000`.
- Confirm overview and health pages load.

## Safety

- Keep the system advisory-only.
- Do not add exchange order execution by default.
- Do not store private exchange credentials in repository files.
