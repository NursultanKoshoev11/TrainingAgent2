# Runtime Check

Эти команды нужно выполнить после установки backend dependencies. Это не торговый запуск, а техническая проверка API, diagnostics, database и streaming.

## Минимальный запуск

```bash
cd backend
python -m pip install fastapi uvicorn
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

Открыть в браузере или через curl:

```text
http://localhost:8000/ping
http://localhost:8000/api/diagnostics
http://localhost:8000/api/readiness
http://localhost:8000/api/health/deep
http://localhost:8000/api/providers/health
```

## Локальный diagnostic script

```bash
cd backend
python ../scripts/runtime_check.py
```

Скрипт должен вывести diagnostics report и readiness report.

## PostgreSQL

```bash
cd backend
python -m pip install -e '.[postgres]'
export DATABASE_URL=postgresql://user:password@localhost:5432/crypto_ai_advisor
python ../scripts/init_postgres.py
python -m uvicorn app.server:server --host 0.0.0.0 --port 8000
```

Потом открыть:

```text
http://localhost:8000/api/database/status
http://localhost:8000/api/jobs/symbol?symbol=BTC/USDT&save=true
```

Ожидаемый результат: `/api/database/status` должен показать `mode: postgresql`, если `DATABASE_URL` настроен правильно.

## Streaming

```bash
cd backend
python -m pip install -e '.[streaming]'
python -m app.cryptofeed_runner
```

Ожидаемый output file:

```text
backend/market_feed_events.jsonl
```

## Что считать успешной проверкой

- `/ping` отвечает без ошибки.
- `/api/diagnostics` показывает `required_ok: true`.
- `/api/readiness` возвращает readiness estimate.
- `/api/health/deep` возвращает combined health report.
- `/api/jobs/symbol?...&save=true` сохраняет advisory signal.
- При PostgreSQL mode записи уходят в PostgreSQL.

## Важно

Система остаётся advisory-only. Runtime check не должен добавлять order execution или private exchange credentials.
