import json
import os


def postgres_enabled():
    return os.getenv('DATABASE_URL', '').startswith('postgresql')


def _connect():
    try:
        import psycopg
    except ImportError as exc:
        raise RuntimeError('psycopg is not installed. Install backend optional dependency: postgres.') from exc
    return psycopg.connect(os.getenv('DATABASE_URL'))


def init_postgres():
    with _connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute('''
                create table if not exists advisory_signals (
                    id bigserial primary key,
                    created_at timestamptz default now(),
                    exchange text,
                    symbol text not null,
                    timeframe text,
                    recommendation text not null,
                    final_score numeric,
                    risk_score numeric,
                    confidence numeric,
                    payload jsonb not null
                )
            ''')
            cursor.execute('''
                create table if not exists market_snapshots (
                    id bigserial primary key,
                    created_at timestamptz default now(),
                    exchange text not null,
                    symbol text not null,
                    timeframe text not null,
                    latest_price numeric,
                    market_score numeric,
                    volatility_percent numeric,
                    volume_ratio numeric,
                    payload jsonb not null
                )
            ''')
            cursor.execute('''
                create table if not exists news_items (
                    id bigserial primary key,
                    created_at timestamptz default now(),
                    symbol text not null,
                    title text not null,
                    url text,
                    source text,
                    published_at text,
                    payload jsonb not null
                )
            ''')
            cursor.execute('create index if not exists idx_advisory_signals_symbol_created on advisory_signals(symbol, created_at desc)')
            cursor.execute('create index if not exists idx_market_snapshots_symbol_created on market_snapshots(symbol, created_at desc)')
            cursor.execute('create index if not exists idx_news_items_symbol_created on news_items(symbol, created_at desc)')
    return {'ok': True, 'mode': 'postgresql'}


def save_advisory_signal_pg(payload):
    init_postgres()
    with _connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                '''insert into advisory_signals (exchange, symbol, timeframe, recommendation, final_score, risk_score, confidence, payload)
                   values (%s, %s, %s, %s, %s, %s, %s, %s::jsonb)
                   returning id''',
                (
                    payload.get('exchange'),
                    payload.get('symbol'),
                    payload.get('timeframe'),
                    payload.get('recommendation'),
                    payload.get('final_score'),
                    payload.get('risk_score'),
                    payload.get('confidence'),
                    json.dumps(payload),
                ),
            )
            return cursor.fetchone()[0]


def save_market_snapshot_pg(snapshot):
    init_postgres()
    with _connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                '''insert into market_snapshots (exchange, symbol, timeframe, latest_price, market_score, volatility_percent, volume_ratio, payload)
                   values (%s, %s, %s, %s, %s, %s, %s, %s::jsonb)
                   returning id''',
                (
                    snapshot.get('exchange'),
                    snapshot.get('symbol'),
                    snapshot.get('timeframe'),
                    snapshot.get('latest_price'),
                    snapshot.get('score'),
                    snapshot.get('volatility_percent'),
                    snapshot.get('volume_ratio'),
                    json.dumps(snapshot),
                ),
            )
            return cursor.fetchone()[0]


def save_news_items_pg(symbol, items):
    init_postgres()
    ids = []
    with _connect() as connection:
        with connection.cursor() as cursor:
            for item in items:
                cursor.execute(
                    '''insert into news_items (symbol, title, url, source, published_at, payload)
                       values (%s, %s, %s, %s, %s, %s::jsonb)
                       returning id''',
                    (symbol, item.get('title'), item.get('url'), item.get('source'), item.get('published_at'), json.dumps(item)),
                )
                ids.append(cursor.fetchone()[0])
    return ids


def list_recent_advisory_signals_pg(limit=50):
    init_postgres()
    with _connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                'select id, symbol, recommendation, final_score, risk_score, payload, created_at from advisory_signals order by id desc limit %s',
                (limit,),
            )
            rows = cursor.fetchall()
    return [
        {
            'id': row[0],
            'symbol': row[1],
            'recommendation': row[2],
            'final_score': float(row[3]) if row[3] is not None else None,
            'risk_score': float(row[4]) if row[4] is not None else None,
            'payload': row[5],
            'created_at': row[6].isoformat() if row[6] else None,
        }
        for row in rows
    ]


def postgres_status():
    return {
        'enabled': postgres_enabled(),
        'mode': 'postgresql' if postgres_enabled() else 'sqlite',
        'adapter': 'psycopg',
    }
