create table if not exists market_candles (
    time timestamptz not null,
    exchange text not null,
    symbol text not null,
    timeframe text not null,
    open numeric,
    high numeric,
    low numeric,
    close numeric,
    volume numeric,
    primary key (time, exchange, symbol, timeframe)
);

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
);

create table if not exists news_items (
    id bigserial primary key,
    created_at timestamptz default now(),
    symbol text not null,
    title text not null,
    url text,
    source text,
    published_at timestamptz,
    payload jsonb not null
);

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
);

create index if not exists idx_market_snapshots_symbol_created on market_snapshots(symbol, created_at desc);
create index if not exists idx_news_items_symbol_created on news_items(symbol, created_at desc);
create index if not exists idx_advisory_signals_symbol_created on advisory_signals(symbol, created_at desc);
