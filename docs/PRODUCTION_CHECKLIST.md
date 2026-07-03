# Production Checklist

Чеклист нужен перед реальным production-запуском. Он помогает проверить backend, database, market data, streaming и dashboard.

## Backend

- Запустить FastAPI server.
- Проверить, что `/ping` возвращает ok.
- Проверить, что `/api/providers/health` возвращает provider status.
- Проверить, что `/api/diagnostics` показывает `required_ok: true`.
- Проверить, что `/api/readiness` возвращает readiness estimate.
- Проверить, что `/api/health/deep` возвращает полный health report.

## Database

- Настроить `DATABASE_URL` для PostgreSQL.
- Установить optional dependency group `postgres`.
- Запустить `python ../scripts/init_postgres.py` из папки `backend`.
- Проверить, что `/api/database/status` показывает `mode: postgresql`.
- Запустить `/api/jobs/symbol?save=true` и подтвердить, что records сохраняются.

## Market data

- Проверить, что `/api/market/snapshot` возвращает price и score.
- Проверить, что `/api/screener` возвращает top setups и high-risk assets.
- Проверить, что `/api/universe` анализирует список symbols без критических ошибок.

## News и context

- Настроить `CRYPTOPANIC_API_KEY`, если ключ доступен.
- Включить `GDELT_ENABLED=true` только после проверки provider/source rules.
- Проверить, что `/api/context/status` возвращает ожидаемые provider states.

## Streaming

- Установить optional dependency group `streaming`.
- Запустить `python -m app.cryptofeed_runner`.
- Проверить, что создаётся `market_feed_events.jsonl`.
- Проверить, что runner совместим с установленной версией `cryptofeed`.

## Dashboard

- Запустить backend на port 8000.
- Запустить Next dashboard с `NEXT_PUBLIC_API_BASE=http://localhost:8000`.
- Проверить, что overview и health pages загружаются.

## Safety

- Система должна оставаться advisory-only.
- Не добавлять exchange order execution по умолчанию.
- Не хранить private exchange credentials в repository files.
